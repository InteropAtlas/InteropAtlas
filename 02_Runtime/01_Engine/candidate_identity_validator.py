#!/usr/bin/env python3
"""Validate V1 Candidate identity-resolution safety boundaries.

This validator is intentionally conservative. It never decides that two
Canonical subjects should be merged. It checks whether a Candidate's declared
identity-resolution state is internally consistent and whether known identifier
collisions are routed to duplicate/review states rather than silently becoming
new Canonical subjects.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

import yaml
from jsonschema import Draft202012Validator

from legacy_identity_adapter import evidence_backed_legacy_identifiers


SAFE_STATES = {
    "new",
    "duplicate",
    "possible_duplicate",
    "identity_risk",
    "deferred",
}

BLOCKING_STATES = {"possible_duplicate", "identity_risk", "deferred"}


@dataclass(frozen=True)
class IdentityFinding:
    code: str
    severity: str
    message: str
    candidate_id: str | None = None


def normalized_identifier(namespace: str, value: str) -> tuple[str, str]:
    return namespace.strip().lower(), " ".join(value.strip().lower().split())


def canonical_identifier_index(records: Iterable[Mapping[str, Any]]) -> dict[tuple[str, str], set[str]]:
    """Build one conservative index across structured V1 and evidence-backed Legacy IDs."""
    index: dict[tuple[str, str], set[str]] = {}
    for record in records:
        record_id = record.get("id")
        if not isinstance(record_id, str):
            continue

        identifiers = record.get("external_identifiers")
        if isinstance(identifiers, list):
            for item in identifiers:
                if not isinstance(item, Mapping):
                    continue
                namespace = item.get("namespace")
                value = item.get("value")
                if not isinstance(namespace, str) or not isinstance(value, str):
                    continue
                key = normalized_identifier(namespace, value)
                index.setdefault(key, set()).add(record_id)

        for namespace, value in evidence_backed_legacy_identifiers(record):
            key = normalized_identifier(namespace, value)
            index.setdefault(key, set()).add(record_id)

    return index


def candidate_collisions(
    candidate: Mapping[str, Any],
    canonical_index: Mapping[tuple[str, str], set[str]],
) -> set[str]:
    collisions: set[str] = set()
    for item in candidate.get("external_identifiers") or []:
        if not isinstance(item, Mapping):
            continue
        namespace = item.get("namespace")
        value = item.get("value")
        if isinstance(namespace, str) and isinstance(value, str):
            collisions.update(canonical_index.get(normalized_identifier(namespace, value), set()))
    return collisions


def identity_route(
    candidate: Mapping[str, Any],
    canonical_index: Mapping[tuple[str, str], set[str]],
) -> str:
    """Return the next deterministic intake route without accepting Canonical state.

    This is an explicit acceptance boundary: the strongest ordinary-machine
    result is ``review_required``. No route here means ``accepted`` and no route
    authorizes merge/split.
    """
    resolution = candidate.get("identity_resolution")
    if not isinstance(resolution, Mapping):
        return "blocked_invalid_identity_state"

    state = resolution.get("state")
    collisions = candidate_collisions(candidate, canonical_index)

    if state == "new":
        return "blocked_invalid_identity_state" if collisions else "review_required"
    if state == "duplicate":
        matched = set(resolution.get("matched_canonical_ids") or [])
        if not matched or (collisions and not collisions.issubset(matched)) or len(collisions) > 1:
            return "blocked_invalid_identity_state"
        return "duplicate_existing"
    if state in {"possible_duplicate", "identity_risk"}:
        return "identity_review_required"
    if state == "deferred":
        return "deferred"
    return "blocked_invalid_identity_state"


def validate_candidate(
    candidate: Mapping[str, Any],
    schema: Mapping[str, Any],
    canonical_index: Mapping[tuple[str, str], set[str]],
) -> list[IdentityFinding]:
    candidate_id = candidate.get("candidate_id") if isinstance(candidate.get("candidate_id"), str) else None
    findings: list[IdentityFinding] = []

    validator = Draft202012Validator(schema)
    for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.path)):
        path = ".".join(str(item) for item in error.path)
        findings.append(
            IdentityFinding(
                "IA-ID-001",
                "error",
                f"Candidate schema violation{f' at {path}' if path else ''}: {error.message}",
                candidate_id,
            )
        )

    resolution = candidate.get("identity_resolution")
    if not isinstance(resolution, Mapping):
        return findings

    state = resolution.get("state")
    if state not in SAFE_STATES:
        return findings

    if resolution.get("merge_authorized") is not False:
        findings.append(
            IdentityFinding(
                "IA-ID-002",
                "error",
                "Ordinary Candidate validation cannot authorize identity merge/split.",
                candidate_id,
            )
        )

    matched = set(resolution.get("matched_canonical_ids") or [])
    collisions = candidate_collisions(candidate, canonical_index)

    if collisions and state == "new":
        findings.append(
            IdentityFinding(
                "IA-ID-003",
                "error",
                "Known normalized external-identifier collision cannot be routed as new; use duplicate or identity-review state.",
                candidate_id,
            )
        )

    if state == "duplicate":
        if not matched:
            findings.append(
                IdentityFinding(
                    "IA-ID-004",
                    "error",
                    "Duplicate disposition requires at least one matched Canonical ID.",
                    candidate_id,
                )
            )
        if collisions and not collisions.issubset(matched):
            findings.append(
                IdentityFinding(
                    "IA-ID-005",
                    "error",
                    "Declared duplicate target does not cover known normalized identifier collision(s).",
                    candidate_id,
                )
            )

    if len(collisions) > 1 and state not in BLOCKING_STATES:
        findings.append(
            IdentityFinding(
                "IA-ID-006",
                "error",
                "One Candidate identifier set collides with multiple Canonical subjects; identity resolution must defer/escalate.",
                candidate_id,
            )
        )

    if state in BLOCKING_STATES and not resolution.get("reasons"):
        findings.append(
            IdentityFinding(
                "IA-ID-007",
                "error",
                "Identity-review/deferred state requires an explicit reason.",
                candidate_id,
            )
        )

    return findings


def load_yaml_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if isinstance(document, dict):
                records.append(document)
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--canonical", type=Path, action="append", default=[])
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("01_State/01_Objects/candidate-object.v1.schema.json"),
    )
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    canonical_records: list[dict[str, Any]] = []
    for path in args.canonical:
        canonical_records.extend(load_yaml_records(path))
    index = canonical_identifier_index(canonical_records)

    findings: list[IdentityFinding] = []
    candidates = load_yaml_records(args.candidate)
    routes: list[dict[str, str | None]] = []
    for candidate in candidates:
        findings.extend(validate_candidate(candidate, schema, index))
        routes.append(
            {
                "candidate_id": candidate.get("candidate_id") if isinstance(candidate.get("candidate_id"), str) else None,
                "route": identity_route(candidate, index),
            }
        )

    errors = [item for item in findings if item.severity == "error"]
    payload = {
        "validator": "candidate-identity-v1",
        "outcome": "FAIL" if errors else "PASS / IDENTITY-SAFE-PREFLIGHT",
        "candidates": len(candidates),
        "errors": len(errors),
        "routes": routes,
        "findings": [asdict(item) for item in findings],
        "boundary": (
            "PASS means the Candidate is structurally safe for ordinary identity preflight only. "
            "The strongest machine route is review_required; no route authorizes Canonical acceptance, merge, or split."
        ),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
