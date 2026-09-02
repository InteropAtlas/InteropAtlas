#!/usr/bin/env python3
"""Report lifecycle / contribution / verification coverage for InteropAtlas.

This is report-only. Coverage gaps do not make the command fail.
An age-based staleness threshold is optional because the current Provenance
Profile intentionally does not define one universal repository-wide value.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "02_Runtime" / "01_Engine"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))

from bootstrap_query import is_relation_document  # noqa: E402

DOC_BLOCK_RE = re.compile(r"<!-- InteropAtlas Document Metadata v0\n(?P<body>.*?)\n-->", re.S)
DOC_FIELD_RE = re.compile(r"(?m)^(?P<key>[A-Za-z ]+):\s*(?P<value>.+?)\s*$")


def parse_time(value: Any) -> datetime | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text.startswith("Unknown"):
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def document_paths(root: Path) -> list[Path]:
    paths: set[Path] = set()
    for path in root.glob("*.md"):
        if path.is_file():
            paths.add(path)
    for base in [root / "docs", root / "03_Evolution"]:
        if base.exists():
            for path in base.rglob("*.md"):
                if path.is_file():
                    paths.add(path)
    for base in [root / "01_State", root / "02_Runtime"]:
        if base.exists():
            for path in base.rglob("README.md"):
                if path.is_file():
                    paths.add(path)
    pr_template = root / ".github" / "PULL_REQUEST_TEMPLATE.md"
    if pr_template.exists():
        paths.add(pr_template)
    return sorted(paths)


def parse_document(path: Path, root: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = DOC_BLOCK_RE.search(text)
    fields: dict[str, str] = {}
    if match:
        for item in DOC_FIELD_RE.finditer(match.group("body")):
            fields[item.group("key").strip()] = item.group("value").strip()
    created = fields.get("Document Created At")
    updated = fields.get("Document Updated At")
    lifecycle_provenance = fields.get("Lifecycle Time Provenance")
    identity_provenance = fields.get("Contribution Identity Provenance")
    reviewer_match = re.search(r"(?m)^\s*Reviewer:\s*(.+?)\s*$", match.group("body") if match else "")
    return {
        "artifact": path.relative_to(root).as_posix(),
        "kind": "document",
        "metadata_block": bool(match),
        "created_at": created,
        "updated_at": updated,
        "lifecycle_complete": bool(parse_time(created) and parse_time(updated)),
        "lifecycle_time_provenance": lifecycle_provenance,
        "contribution_identity_provenance": identity_provenance,
        "reviewer": reviewer_match.group(1).strip() if reviewer_match else None,
    }


def load_objects(root: Path) -> list[dict[str, Any]]:
    result = []
    for path in sorted((root / "01_State" / "01_Objects").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not data.get("id"):
            continue
        result.append(record_snapshot(data, path.relative_to(root).as_posix(), "object"))
    return result


def load_relations(root: Path) -> list[dict[str, Any]]:
    result = []
    for path in sorted((root / "01_State" / "02_Relations").glob("*.yaml")):
        with path.open("r", encoding="utf-8") as handle:
            for data in yaml.safe_load_all(handle):
                if isinstance(data, dict) and is_relation_document(data):
                    result.append(record_snapshot(data, path.relative_to(root).as_posix(), "relation"))
    return result


def record_snapshot(data: dict[str, Any], path: str, kind: str) -> dict[str, Any]:
    metadata_provenance = data.get("metadata_provenance") if isinstance(data.get("metadata_provenance"), dict) else {}
    latest = data.get("latest_substantive_contribution") if isinstance(data.get("latest_substantive_contribution"), dict) else {}
    source_count = 0
    if isinstance(data.get("sources"), list):
        source_count += len(data["sources"])
    if isinstance(data.get("evidence"), list):
        source_count += len(data["evidence"])
    return {
        "artifact": str(data.get("id")),
        "path": path,
        "kind": kind,
        "created_at": str(data.get("record_created_at")) if data.get("record_created_at") is not None else None,
        "updated_at": str(data.get("record_updated_at")) if data.get("record_updated_at") is not None else None,
        "lifecycle_complete": bool(data.get("record_created_at") and data.get("record_updated_at")),
        "lifecycle_time_provenance": metadata_provenance.get("lifecycle_time"),
        "contribution_identity_provenance": metadata_provenance.get("contribution_identity"),
        "reviewer": latest.get("reviewer"),
        "last_verified_at": str(data.get("last_verified_at")) if data.get("last_verified_at") is not None else None,
        "last_verified_by": str(data.get("last_verified_by")) if data.get("last_verified_by") is not None else None,
        "source_or_evidence_count": source_count,
    }


def summarize_lifecycle(items: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(items)
    complete = sum(bool(item.get("lifecycle_complete")) for item in items)
    provenance = Counter(item.get("lifecycle_time_provenance") or "missing" for item in items)
    identity = Counter(item.get("contribution_identity_provenance") or "missing" for item in items)
    reviewer = Counter(str(item.get("reviewer") or "missing") for item in items)
    return {
        "total": total,
        "lifecycle_complete": complete,
        "lifecycle_coverage_pct": round(100 * complete / total, 2) if total else 100.0,
        "lifecycle_time_provenance": dict(sorted(provenance.items())),
        "contribution_identity_provenance": dict(sorted(identity.items())),
        "reviewer_state": dict(sorted(reviewer.items())),
    }


def summarize_verification(items: list[dict[str, Any]], as_of: datetime, threshold_days: int | None) -> dict[str, Any]:
    verified = []
    never = []
    incomplete = []
    stale = []
    source_gap = []
    for item in items:
        stamp = item.get("last_verified_at")
        verifier = item.get("last_verified_by")
        if not stamp and not verifier:
            never.append(item)
        elif not stamp or not verifier or parse_time(stamp) is None:
            incomplete.append(item)
        else:
            verified.append(item)
            if threshold_days is not None:
                age_days = (as_of - parse_time(stamp)).total_seconds() / 86400
                if age_days >= threshold_days:
                    stale.append({
                        "artifact": item["artifact"],
                        "path": item.get("path"),
                        "last_verified_at": stamp,
                        "last_verified_by": verifier,
                        "age_days": round(age_days, 2),
                    })
        if int(item.get("source_or_evidence_count") or 0) == 0:
            source_gap.append({"artifact": item["artifact"], "path": item.get("path")})
    total = len(items)
    return {
        "total": total,
        "verified": len(verified),
        "verification_coverage_pct": round(100 * len(verified) / total, 2) if total else 100.0,
        "never_verified": [{"artifact": x["artifact"], "path": x.get("path")} for x in never],
        "verification_incomplete": [{"artifact": x["artifact"], "path": x.get("path")} for x in incomplete],
        "stale_by_threshold": stale,
        "source_or_evidence_gaps": source_gap,
        "revalidation_candidate_count": len(never) + len(incomplete) + len(stale),
    }


def markdown_report(report: dict[str, Any]) -> str:
    docs = report["documents"]
    objects = report["objects"]
    relations = report["relations"]
    threshold = report["staleness_policy"]
    lines = [
        "# InteropAtlas Provenance Coverage / Staleness Report",
        "",
        f"Generated at: `{report['generated_at']}`",
        f"As-of: `{report['as_of']}`",
        "",
        "## Coverage",
        "",
        "| Artifact | Total | Lifecycle complete | Verification | Source / evidence gaps |",
        "|---|---:|---:|---:|---:|",
        f"| Documents | {docs['lifecycle']['total']} | {docs['lifecycle']['lifecycle_complete']} | n/a — Document Metadata v0 has no generic verification pair | n/a |",
        f"| Objects | {objects['lifecycle']['total']} | {objects['lifecycle']['lifecycle_complete']} | {objects['verification']['verified']} | {len(objects['verification']['source_or_evidence_gaps'])} |",
        f"| Relations | {relations['lifecycle']['total']} | {relations['lifecycle']['lifecycle_complete']} | {relations['verification']['verified']} | {len(relations['verification']['source_or_evidence_gaps'])} |",
        "",
        "## Staleness",
        "",
        f"- Universal age threshold configured: **{'yes' if threshold['configured'] else 'no'}**",
        f"- Threshold days: `{threshold['days']}`",
        f"- Never-verified Objects: **{len(objects['verification']['never_verified'])}**",
        f"- Never-verified Relations: **{len(relations['verification']['never_verified'])}**",
        f"- Objects stale by configured threshold: **{len(objects['verification']['stale_by_threshold'])}**",
        f"- Relations stale by configured threshold: **{len(relations['verification']['stale_by_threshold'])}**",
        "",
        "`never_verified` is not assigned a fabricated verification age. If an age threshold is supplied, only records with a real `last_verified_at` are evaluated against it.",
        "",
        "## Structural boundary",
        "",
        "Document Metadata Block v0 currently records lifecycle and contribution provenance but does not define a generic `last_verified_at` / `last_verified_by` pair for Documents. Document verification staleness therefore cannot be claimed from `Document Updated At`; that would conflate modification with verification.",
        "",
        "The JSON report contains the full revalidation-candidate and evidence-gap lists.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--as-of", help="RFC3339 timestamp used for age calculations; defaults to current UTC")
    parser.add_argument("--stale-after-days", type=int, default=None, help="optional age threshold; no repository-wide default exists")
    parser.add_argument("--json", required=True)
    parser.add_argument("--markdown")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    as_of = parse_time(args.as_of) if args.as_of else datetime.now(timezone.utc)
    if as_of is None:
        raise SystemExit("--as-of must be RFC3339 / ISO 8601")
    if args.stale_after_days is not None and args.stale_after_days < 0:
        raise SystemExit("--stale-after-days must be >= 0")

    docs_items = [parse_document(path, root) for path in document_paths(root)]
    object_items = load_objects(root)
    relation_items = load_relations(root)

    report = {
        "schema": "interopatlas.provenance-coverage.v0.1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": as_of.isoformat(),
        "staleness_policy": {
            "configured": args.stale_after_days is not None,
            "days": args.stale_after_days,
            "default_policy": "none_in_provenance_profile_v0.1",
        },
        "documents": {
            "lifecycle": summarize_lifecycle(docs_items),
            "verification": {
                "model": "not_defined_in_document_metadata_block_v0",
                "note": "Do not use Document Updated At as a verification timestamp.",
            },
            "artifacts": docs_items,
        },
        "objects": {
            "lifecycle": summarize_lifecycle(object_items),
            "verification": summarize_verification(object_items, as_of, args.stale_after_days),
        },
        "relations": {
            "lifecycle": summarize_lifecycle(relation_items),
            "verification": summarize_verification(relation_items, as_of, args.stale_after_days),
        },
    }

    json_path = Path(args.json)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        md_path = Path(args.markdown)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(markdown_report(report), encoding="utf-8")

    print(json.dumps({
        "documents": report["documents"]["lifecycle"],
        "objects_lifecycle": report["objects"]["lifecycle"],
        "objects_verification": {k: v if not isinstance(v, list) else len(v) for k, v in report["objects"]["verification"].items()},
        "relations_lifecycle": report["relations"]["lifecycle"],
        "relations_verification": {k: v if not isinstance(v, list) else len(v) for k, v in report["relations"]["verification"].items()},
        "staleness_policy": report["staleness_policy"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
