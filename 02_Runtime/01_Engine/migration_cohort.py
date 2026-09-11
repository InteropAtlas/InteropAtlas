#!/usr/bin/env python3
"""Conservative Legacy→V1 migration cohort planner.

The planner is intentionally dry-run only. It classifies explicitly selected
Legacy records and refuses semantic/identity guessing. P6 #147 can use its
output as executable evidence before any Canonical mutation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml

from repository_layout import resolve_repository_root


@dataclass(frozen=True)
class MigrationPlan:
    record_id: str
    source: str
    mapping_class: str
    disposition: str
    stable_id_preserved: bool
    proposed_patch: dict[str, Any]
    preserved_legacy_fields: list[str]
    reasons: list[str]


def load_yaml_record(root: Path, relative_path: str) -> Mapping[str, Any]:
    path = root / relative_path
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"expected mapping document: {relative_path}")
    return data


def classify_record(record: Mapping[str, Any], source: str) -> MigrationPlan:
    record_id = record.get("id")
    if not isinstance(record_id, str) or not record_id:
        return MigrationPlan("<missing>", source, "ambiguous", "exclude", False, {}, [], ["missing stable IA id"])

    proposed: dict[str, Any] = {}
    preserved: list[str] = []
    reasons: list[str] = []

    # Lossless lifecycle normalization: a Legacy date can be represented as a
    # V1 verification timestamp without deleting the Legacy field yet.
    last_verified = record.get("last_verified")
    if isinstance(last_verified, str) and last_verified:
        proposed["last_verified_at"] = f"{last_verified}T00:00:00Z" if len(last_verified) == 10 else last_verified
        preserved.append("last_verified")
        reasons.append("last_verified can be normalized without deleting Legacy evidence")

    # Locator normalization is additive. Do not infer identity from URL.
    official_url = record.get("official_url")
    if isinstance(official_url, str) and official_url:
        proposed["locators"] = [{"role": "official_current", "url": official_url}]
        preserved.append("official_url")
        reasons.append("official_url can be copied into explicit locator semantics")

    # Existing relation triples already have a P5-proven lossless mapping.
    if record.get("type") == "relation" and all(isinstance(record.get(k), str) for k in ("source", "relation", "target")):
        proposed["v1_relation"] = {
            "subject": record["source"],
            "predicate": record["relation"],
            "object": record["target"],
        }
        preserved.extend(["source", "relation", "target"])
        reasons.append("binary Legacy relation has a lossless structural V1 mapping")
        return MigrationPlan(record_id, source, "A", "eligible_dry_run", True, proposed, sorted(set(preserved)), reasons)

    if proposed:
        reasons.append("classification/taxonomy fields remain untouched; additive normalization only")
        return MigrationPlan(record_id, source, "B", "eligible_dry_run", True, proposed, sorted(set(preserved)), reasons)

    return MigrationPlan(
        record_id,
        source,
        "ambiguous",
        "exclude",
        True,
        {},
        [],
        ["no proven lossless/additive mapping rule; semantic promotion would require review"],
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="repository-relative Legacy YAML paths")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = resolve_repository_root(Path(args.root))
    plans = [classify_record(load_yaml_record(root, path), path) for path in args.paths]
    report = {
        "migration_planner_version": "0.1",
        "mode": "dry_run_only",
        "summary": {
            "records": len(plans),
            "eligible": sum(plan.disposition == "eligible_dry_run" for plan in plans),
            "excluded": sum(plan.disposition == "exclude" for plan in plans),
        },
        "plans": [asdict(plan) for plan in plans],
        "boundary": "No Canonical mutation is performed. Stable IDs are preserved; semantic promotion and identity merge/split are excluded.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
