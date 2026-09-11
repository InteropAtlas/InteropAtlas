#!/usr/bin/env python3
"""Validate P5 experiment fixture envelopes.

Passing this validator means only that an experiment fixture is structurally
usable by P5 research. It does NOT validate production Canonical V1 data and
must never be treated as Canonical acceptance.
"""

from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parent
FIXTURES = ROOT / "fixtures"
ALLOWED_MAPPING = {
    None,
    "A_lossless_structural",
    "B_normalization",
    "C_semantic_promotion",
    "D_ambiguous_unresolved",
    "E_identity_destructive",
}
REQUIRED = {
    "fixture_version",
    "fixture_id",
    "experiment",
    "subject",
    "expectations",
    "v1_candidate",
    "unknowns",
    "conflicts",
    "mapping",
    "validation",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"parse_error: {exc}"]
    if not isinstance(data, dict):
        return ["envelope_error: top level must be a mapping"]
    missing = sorted(REQUIRED - set(data))
    if missing:
        errors.append(f"envelope_error: missing keys {missing}")
    if data.get("fixture_version") != "p5-v1-experiment-0":
        errors.append("envelope_error: unsupported fixture_version")
    experiment = data.get("experiment")
    if not isinstance(experiment, dict) or not experiment.get("issue") or not experiment.get("track"):
        errors.append("envelope_error: experiment.issue and experiment.track are required")
    subject = data.get("subject")
    if not isinstance(subject, dict) or not subject.get("label"):
        errors.append("envelope_error: subject.label is required")
    if not isinstance(data.get("expectations"), list) or not data.get("expectations"):
        errors.append("envelope_error: at least one expectation is required")
    if not isinstance(data.get("v1_candidate"), dict):
        errors.append("envelope_error: v1_candidate must be a mapping")
    for key in ("unknowns", "conflicts"):
        if not isinstance(data.get(key), list):
            errors.append(f"envelope_error: {key} must be a list")
    mapping = data.get("mapping")
    if not isinstance(mapping, dict):
        errors.append("envelope_error: mapping must be a mapping")
    elif mapping.get("class") not in ALLOWED_MAPPING:
        errors.append(f"envelope_error: unsupported mapping.class {mapping.get('class')!r}")
    validation = data.get("validation")
    if not isinstance(validation, dict) or "expected_v0_mismatch" not in validation:
        errors.append("envelope_error: validation.expected_v0_mismatch is required")
    return errors


def main() -> int:
    paths = sorted(FIXTURES.glob("*.yaml")) if FIXTURES.exists() else []
    if not paths:
        print("P5 fixtures: 0 (no fixtures yet)")
        return 0
    failures = 0
    for path in paths:
        errors = validate(path)
        if errors:
            failures += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")
    print(f"P5 fixtures: {len(paths)}, failed: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
