#!/usr/bin/env python3
"""Deterministic Machine Review for InteropAtlas.

This is Layer 1 of the approved review model. It reports facts that machines can
check deterministically and explicitly does not make semantic/governance
judgments on behalf of Human/Agent reviewers or maintainers.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping
from urllib.parse import urljoin

import yaml
from jsonschema import Draft202012Validator, RefResolver

from bootstrap_query import is_relation_document
from candidate_identity_validator import canonical_identifier_index, identity_route, validate_candidate
from graph_index import GraphIndex
from kind_registry import load_kind_registry, profiles_for_record, validate_v0_identity
from relation_model import normalize_relation
from repository_layout import repository_layout
from semantic_model import normalize_record


@dataclass(frozen=True)
class MachineFinding:
    code: str
    severity: str
    message: str
    record_id: str | None = None
    source: str | None = None
    path: str | None = None


PROFILE_SCHEMAS = {
    "capability": "capability-profile.v0.schema.json",
    "scenario": "scenario-profile.v0.schema.json",
    "normative_artifact": "normative-artifact-profile.v0.schema.json",
    "implementation": "implementation-profile.v0.schema.json",
    "organization": "organization-profile.v0.schema.json",
}

CANDIDATE_STORAGE_PATH = Path("01_State/03_Candidates")
CANDIDATE_SCHEMA = "candidate-object.v1.schema.json"


def run_machine_review(root: Path) -> dict[str, Any]:
    layout = repository_layout(root)
    findings: list[MachineFinding] = []
    objects: list[dict[str, Any]] = []
    relations: list[dict[str, Any]] = []
    candidates: list[dict[str, Any]] = []
    candidate_routes: list[dict[str, Any]] = []
    sources: dict[tuple[str, str], str] = {}

    for path in layout.iter_yaml_files():
        source = layout.physical_source(path)
        try:
            with path.open("r", encoding="utf-8") as handle:
                documents = list(yaml.safe_load_all(handle))
        except yaml.YAMLError as exc:
            findings.append(
                MachineFinding("IA-MR-001", "error", f"YAML parse error: {exc}", source=source)
            )
            continue

        for document in documents:
            if not isinstance(document, dict):
                continue
            relation_document = is_relation_document(document)
            namespace = "relation" if relation_document else "object"
            record_id = document.get("id") if isinstance(document.get("id"), str) else None
            if record_id:
                key = (namespace, record_id)
                if key in sources:
                    findings.append(
                        MachineFinding(
                            "IA-MR-002",
                            "error",
                            f"Duplicate {namespace} ID; first seen at {sources[key]}",
                            record_id=record_id,
                            source=source,
                        )
                    )
                else:
                    sources[key] = source
            document = dict(document)
            document["_machine_review_source"] = source
            if relation_document:
                relations.append(document)
            else:
                objects.append(document)

    registry = load_kind_registry()
    schema_bundle, schema_findings = _load_schema_bundle(root)
    findings.extend(schema_findings)

    for record in objects:
        descriptor = normalize_record(record)
        if descriptor.migration_status != "v0":
            continue
        source = record.get("_machine_review_source")
        for item in validate_v0_identity(record, registry):
            findings.append(
                MachineFinding(
                    item.code,
                    "error",
                    item.message,
                    record_id=item.object_id,
                    source=source,
                )
            )
        findings.extend(_validate_v0_identity_schemas(record, source, registry, schema_bundle))
        findings.extend(_forbidden_null_findings(record, source))

    for record in relations:
        descriptor = normalize_relation(record)
        if not descriptor.canonical_refs:
            continue
        source = record.get("_machine_review_source")
        findings.extend(_validate_schema(record, source, "relation.v0.schema.json", schema_bundle))
        findings.extend(_forbidden_null_findings(record, source))

    candidate_schema = schema_bundle.get("by_name", {}).get(CANDIDATE_SCHEMA)
    if isinstance(candidate_schema, dict):
        candidate_index = canonical_identifier_index(objects)
        candidate_base = root / CANDIDATE_STORAGE_PATH
        if candidate_base.exists():
            for pattern in ("*.yaml", "*.yml"):
                for path in sorted(candidate_base.rglob(pattern)):
                    source = path.relative_to(root).as_posix()
                    try:
                        with path.open("r", encoding="utf-8") as handle:
                            documents = list(yaml.safe_load_all(handle))
                    except yaml.YAMLError as exc:
                        findings.append(
                            MachineFinding("IA-MR-001", "error", f"YAML parse error: {exc}", source=source)
                        )
                        continue
                    for document in documents:
                        if not isinstance(document, dict):
                            continue
                        candidates.append(document)
                        candidate_routes.append(
                            {
                                "candidate_id": document.get("candidate_id"),
                                "source": source,
                                "route": identity_route(document, candidate_index),
                            }
                        )
                        for item in validate_candidate(document, candidate_schema, candidate_index):
                            findings.append(
                                MachineFinding(
                                    item.code,
                                    item.severity,
                                    item.message,
                                    record_id=item.candidate_id,
                                    source=source,
                                )
                            )
    else:
        findings.append(
            MachineFinding(
                "IA-MR-008",
                "error",
                f"Required schema not found: {CANDIDATE_SCHEMA}",
                source=CANDIDATE_SCHEMA,
            )
        )

    object_index = {
        record["id"]: record
        for record in objects
        if isinstance(record.get("id"), str)
    }
    graph = GraphIndex(object_index, relations)
    for issue in graph.issues:
        code = (
            "IA-MR-004"
            if issue.code.startswith("unknown_") or issue.code == "unknown_reference"
            else "IA-MR-006"
        )
        findings.append(
            MachineFinding(
                code,
                "error",
                f"{issue.code}: {issue.detail}",
                record_id=issue.source_id,
            )
        )

    semantic_review_records = _semantic_review_records(objects)
    candidate_review_records = _candidate_review_records(candidates)
    compatibility_warnings = [asdict(item) for item in graph.compatibility_warnings]
    errors = [item for item in findings if item.severity == "error"]
    if errors:
        outcome = "FAIL"
    elif semantic_review_records or candidate_review_records:
        outcome = "PASS + SEMANTIC REVIEW REQUIRED"
    else:
        outcome = "PASS / ELIGIBLE"

    return {
        "machine_review_version": "0.2",
        "outcome": outcome,
        "summary": {
            "objects": len(objects),
            "relations": len(relations),
            "candidates": len(candidates),
            "graph_edges": len(graph.edges),
            "errors": len(errors),
            "compatibility_warnings": len(compatibility_warnings),
            "semantic_review_records": len(semantic_review_records),
            "candidate_review_records": len(candidate_review_records),
        },
        "findings": [asdict(item) for item in findings],
        "compatibility_warnings": compatibility_warnings,
        "semantic_review_records": semantic_review_records,
        "candidate_review_records": candidate_review_records,
        "candidate_routes": candidate_routes,
        "boundary": (
            "Machine PASS is deterministic evidence only. Identity Target, evidence sufficiency, "
            "new vocabulary terms, high-impact governance, and any identity merge/split remain "
            "independent semantic/governance review work. Candidate state is not Canonical acceptance; "
            "the strongest ordinary-machine route is review_required."
        ),
    }


def _load_schema_bundle(root: Path) -> tuple[dict[str, Any], list[MachineFinding]]:
    schema_paths = sorted((root / "01_State").glob("**/*.schema.json"))
    by_name: dict[str, dict[str, Any]] = {}
    by_id: dict[str, dict[str, Any]] = {}
    findings: list[MachineFinding] = []

    for path in schema_paths:
        source = path.relative_to(root).as_posix()
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        except (json.JSONDecodeError, Exception) as exc:
            findings.append(
                MachineFinding("IA-MR-008", "error", f"Schema load/check error: {exc}", source=source)
            )
            continue
        by_name[path.name] = schema
        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            by_id[schema_id] = schema

    for name, schema in by_name.items():
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str):
            findings.append(
                MachineFinding("IA-MR-008", "error", "Schema is missing logical $id", source=name)
            )
            continue
        for ref in _iter_refs(schema):
            if ref.startswith("#"):
                continue
            target = urljoin(schema_id, ref.split("#", 1)[0])
            if target and target not in by_id:
                findings.append(
                    MachineFinding(
                        "IA-MR-008",
                        "error",
                        f"Unresolvable logical schema reference: {ref}",
                        source=name,
                    )
                )

    return {"by_name": by_name, "by_id": by_id}, findings


def _validate_v0_identity_schemas(
    record: Mapping[str, Any],
    source: str | None,
    registry: Mapping[str, Any],
    schema_bundle: Mapping[str, Any],
) -> list[MachineFinding]:
    findings = _validate_schema(record, source, "identity-object.v0.schema.json", schema_bundle)
    for profile in profiles_for_record(record, registry):
        schema_name = PROFILE_SCHEMAS.get(profile)
        if schema_name:
            findings.extend(_validate_schema(record, source, schema_name, schema_bundle))
    return findings


def _validate_schema(
    record: Mapping[str, Any],
    source: str | None,
    schema_name: str,
    schema_bundle: Mapping[str, Any],
) -> list[MachineFinding]:
    by_name = schema_bundle.get("by_name", {})
    by_id = schema_bundle.get("by_id", {})
    schema = by_name.get(schema_name)
    if not isinstance(schema, dict):
        return [
            MachineFinding(
                "IA-MR-008",
                "error",
                f"Required schema not found: {schema_name}",
                record_id=record.get("id") if isinstance(record.get("id"), str) else None,
                source=source,
            )
        ]
    clean_record = {key: value for key, value in record.items() if not key.startswith("_machine_review_")}
    resolver = RefResolver.from_schema(schema, store=by_id)
    validator = Draft202012Validator(schema, resolver=resolver)
    result: list[MachineFinding] = []
    for error in sorted(validator.iter_errors(clean_record), key=lambda item: list(item.path)):
        path = ".".join(str(item) for item in error.path) or None
        result.append(
            MachineFinding(
                "IA-MR-003",
                "error",
                error.message,
                record_id=clean_record.get("id") if isinstance(clean_record.get("id"), str) else None,
                source=source,
                path=path,
            )
        )
    return result


def _forbidden_null_findings(record: Mapping[str, Any], source: str | None) -> list[MachineFinding]:
    result: list[MachineFinding] = []
    record_id = record.get("id") if isinstance(record.get("id"), str) else None
    for path in _null_paths(record):
        if path.startswith("_machine_review_"):
            continue
        result.append(
            MachineFinding(
                "IA-MR-007",
                "error",
                "Explicit null is not an allowed generic semantic state in v0; omit the field or use an explicit value-state contract.",
                record_id=record_id,
                source=source,
                path=path,
            )
        )
    return result


def _semantic_review_records(objects: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for record in objects:
        descriptor = normalize_record(record)
        if descriptor.migration_status not in {"audit_required", "provisional", "unknown"}:
            continue
        result.append(
            {
                "id": record.get("id"),
                "source": record.get("_machine_review_source"),
                "legacy_type": descriptor.legacy_type,
                "kind": descriptor.kind,
                "migration_status": descriptor.migration_status,
            }
        )
    return result


def _candidate_review_records(candidates: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for candidate in candidates:
        resolution = candidate.get("identity_resolution")
        if not isinstance(resolution, Mapping):
            continue
        state = resolution.get("state")
        if state not in {"possible_duplicate", "identity_risk", "deferred"}:
            continue
        result.append(
            {
                "candidate_id": candidate.get("candidate_id"),
                "identity_state": state,
                "matched_canonical_ids": list(resolution.get("matched_canonical_ids") or []),
                "reasons": list(resolution.get("reasons") or []),
            }
        )
    return result


def _iter_refs(value: Any) -> Iterable[str]:
    if isinstance(value, Mapping):
        ref = value.get("$ref")
        if isinstance(ref, str):
            yield ref
        for item in value.values():
            yield from _iter_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_refs(item)


def _null_paths(value: Any, prefix: str = "") -> Iterable[str]:
    if isinstance(value, Mapping):
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if item is None:
                yield path
            else:
                yield from _null_paths(item, path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            path = f"{prefix}[{index}]"
            if item is None:
                yield path
            else:
                yield from _null_paths(item, path)


def render_markdown(report: Mapping[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "## InteropAtlas Machine Review",
        "",
        f"**Outcome:** `{report['outcome']}`",
        "",
        f"- Objects: {summary['objects']}",
        f"- Relations: {summary['relations']}",
        f"- Candidates: {summary['candidates']}",
        f"- Graph edges: {summary['graph_edges']}",
        f"- Deterministic errors: {summary['errors']}",
        f"- Compatibility warnings: {summary['compatibility_warnings']}",
        f"- Semantic-review records: {summary['semantic_review_records']}",
        f"- Candidate-review records: {summary['candidate_review_records']}",
        "",
    ]
    candidate_routes = report.get("candidate_routes", [])
    if candidate_routes:
        lines.extend(["### Candidate intake routes", ""])
        for item in candidate_routes[:50]:
            lines.append(f"- `{item.get('candidate_id')}` → `{item.get('route')}` ({item.get('source')})")
        if len(candidate_routes) > 50:
            lines.append(f"- … {len(candidate_routes) - 50} more routes in JSON artifact")
        lines.append("")
    findings = report.get("findings", [])
    if findings:
        lines.extend(["### Deterministic findings", ""])
        for item in findings[:50]:
            location = item.get("source") or item.get("record_id") or "repository"
            lines.append(f"- `{item['code']}` {location}: {item['message']}")
        if len(findings) > 50:
            lines.append(f"- … {len(findings) - 50} more findings in JSON artifact")
        lines.append("")
    lines.extend(["### Review boundary", "", str(report["boundary"]), ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--json", type=Path)
    parser.add_argument("--markdown", type=Path)
    args = parser.parse_args()

    report = run_machine_review(args.root)
    markdown = render_markdown(report)
    print(markdown)

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown, encoding="utf-8")

    raise SystemExit(1 if report["outcome"] == "FAIL" else 0)


if __name__ == "__main__":
    main()
