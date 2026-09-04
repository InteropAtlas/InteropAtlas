#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

FIXTURE_VERSION = "p5-v0"
REQUIRED_KEYS = {
    "fixture_version",
    "sample_id",
    "source",
    "contracts_under_test",
    "mapping",
    "candidate",
    "unknowns",
    "conflicts",
    "expected",
    "notes",
}
ALLOWED_CONTRACTS = {
    "identity",
    "family_kind",
    "relation",
    "evidence_assertion",
    "lifecycle",
    "migration",
    "selection_projection_workspace",
    "human_agent_access",
}
ALLOWED_MAPPING_CLASSES = {"A", "B", "C", "D", "E", None}
ALLOWED_OUTCOMES = {"pass", "contract_mismatch", "unresolved_hypothesis"}
SOURCE_LIST_KEYS = {"legacy_refs", "candidate_refs", "official_sources"}


@dataclass(frozen=True)
class Diagnostic:
    code: str
    category: str
    message: str

    def render(self, path: Path) -> str:
        return f"{path.as_posix()}: {self.category} {self.code}: {self.message}"


def mismatch(code: str, message: str) -> Diagnostic:
    return Diagnostic(code=code, category="CONTRACT_MISMATCH", message=message)


def unresolved(code: str, message: str) -> Diagnostic:
    return Diagnostic(code=code, category="UNRESOLVED_HYPOTHESIS", message=message)


def iter_fixture_paths(inputs: Iterable[str]) -> list[Path]:
    roots = [Path(item) for item in inputs]
    if not roots:
        roots = [Path(__file__).resolve().parent]

    found: set[Path] = set()
    for root in roots:
        if root.is_dir():
            found.update(root.rglob("*.fixture.yaml"))
            found.update(root.rglob("*.fixture.yml"))
        elif root.is_file():
            found.add(root)
    return sorted(found)


def load_fixture(path: Path) -> tuple[Any | None, list[Diagnostic]]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        return None, [Diagnostic("PARSE_ERROR", "PARSE_ERROR", str(exc))]
    if not isinstance(data, dict):
        return None, [Diagnostic("PARSE_ERROR", "PARSE_ERROR", "fixture document must be a mapping")]
    return data, []


def validate_fixture(data: dict[str, Any]) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []

    missing = sorted(REQUIRED_KEYS - set(data))
    if missing:
        diagnostics.append(mismatch("MISSING_TOP_LEVEL_KEYS", f"missing: {', '.join(missing)}"))

    if data.get("fixture_version") != FIXTURE_VERSION:
        diagnostics.append(mismatch("FIXTURE_VERSION", f"expected {FIXTURE_VERSION!r}"))

    sample_id = data.get("sample_id")
    if not isinstance(sample_id, str) or not sample_id.strip():
        diagnostics.append(mismatch("SAMPLE_ID", "sample_id must be a non-empty string"))

    source = data.get("source")
    if not isinstance(source, dict):
        diagnostics.append(mismatch("SOURCE_SHAPE", "source must be a mapping"))
    else:
        missing_source = sorted(SOURCE_LIST_KEYS - set(source))
        if missing_source:
            diagnostics.append(mismatch("SOURCE_KEYS", f"missing source keys: {', '.join(missing_source)}"))
        for key in SOURCE_LIST_KEYS:
            if key in source and not isinstance(source[key], list):
                diagnostics.append(mismatch("SOURCE_LIST", f"source.{key} must be a list"))

    contracts = data.get("contracts_under_test")
    if not isinstance(contracts, list) or not contracts:
        diagnostics.append(mismatch("CONTRACTS_UNDER_TEST", "must be a non-empty list"))
    else:
        unknown_contracts = sorted({item for item in contracts if item not in ALLOWED_CONTRACTS})
        if unknown_contracts:
            diagnostics.append(mismatch("UNKNOWN_CONTRACT", f"unknown: {', '.join(map(str, unknown_contracts))}"))

    mapping = data.get("mapping")
    if not isinstance(mapping, dict):
        diagnostics.append(mismatch("MAPPING_SHAPE", "mapping must be a mapping"))
    else:
        mapping_class = mapping.get("class")
        if mapping_class not in ALLOWED_MAPPING_CLASSES:
            diagnostics.append(mismatch("MAPPING_CLASS", "mapping.class must be A, B, C, D, E, or null"))
        if mapping_class in {"D", "E"} and not str(mapping.get("notes", "")).strip():
            diagnostics.append(unresolved("MAPPING_REQUIRES_REVIEW", "mapping class D/E requires explicit review notes"))

    if not isinstance(data.get("candidate"), dict):
        diagnostics.append(mismatch("CANDIDATE_SHAPE", "candidate must be a mapping"))

    for key in ("unknowns", "conflicts", "notes"):
        if not isinstance(data.get(key), list):
            diagnostics.append(mismatch("LIST_SHAPE", f"{key} must be a list"))

    expected = data.get("expected")
    if not isinstance(expected, dict):
        diagnostics.append(mismatch("EXPECTED_SHAPE", "expected must be a mapping"))
    else:
        outcome = expected.get("outcome")
        if outcome not in ALLOWED_OUTCOMES:
            diagnostics.append(mismatch("EXPECTED_OUTCOME", "expected.outcome is invalid"))
        if not isinstance(expected.get("diagnostics"), list):
            diagnostics.append(mismatch("EXPECTED_DIAGNOSTICS", "expected.diagnostics must be a list"))

    return diagnostics


def expected_codes(data: dict[str, Any]) -> set[str]:
    expected = data.get("expected")
    if not isinstance(expected, dict):
        return set()
    values = expected.get("diagnostics")
    return {str(item) for item in values} if isinstance(values, list) else set()


def evaluate(path: Path) -> tuple[bool, list[str]]:
    data, parse_diagnostics = load_fixture(path)
    if parse_diagnostics:
        return False, [item.render(path) for item in parse_diagnostics]

    assert isinstance(data, dict)
    diagnostics = validate_fixture(data)
    actual_codes = {item.code for item in diagnostics}
    declared_codes = expected_codes(data)
    outcome = data.get("expected", {}).get("outcome") if isinstance(data.get("expected"), dict) else None

    unexpected = [item for item in diagnostics if item.code not in declared_codes]
    missing_declared = sorted(declared_codes - actual_codes)

    has_mismatch = any(item.category == "CONTRACT_MISMATCH" for item in diagnostics)
    has_unresolved = any(item.category == "UNRESOLVED_HYPOTHESIS" for item in diagnostics)

    outcome_ok = (
        (outcome == "pass" and not diagnostics)
        or (outcome == "contract_mismatch" and has_mismatch)
        or (outcome == "unresolved_hypothesis" and has_unresolved and not has_mismatch)
    )

    lines = [item.render(path) for item in diagnostics]
    for code in missing_declared:
        lines.append(f"{path.as_posix()}: EXPECTATION_MISMATCH {code}: declared diagnostic was not produced")
    if unexpected:
        lines.append(
            f"{path.as_posix()}: EXPECTATION_MISMATCH UNDECLARED_DIAGNOSTIC: "
            + ", ".join(item.code for item in unexpected)
        )
    if not outcome_ok:
        lines.append(f"{path.as_posix()}: EXPECTATION_MISMATCH OUTCOME: expected outcome {outcome!r} not observed")

    ok = outcome_ok and not missing_declared and not unexpected
    if ok and not lines:
        lines.append(f"{path.as_posix()}: PASS")
    elif ok:
        lines.append(f"{path.as_posix()}: EXPECTED_{str(outcome).upper()}")
    return ok, lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate P5 experiment-only V1 contract fixtures")
    parser.add_argument("paths", nargs="*", help="fixture files or directories; defaults to this directory")
    args = parser.parse_args(argv)

    paths = iter_fixture_paths(args.paths)
    if not paths:
        print("No *.fixture.yaml files found", file=sys.stderr)
        return 2

    failures = 0
    for path in paths:
        ok, lines = evaluate(path)
        print("\n".join(lines))
        failures += 0 if ok else 1

    print(f"Checked {len(paths)} fixture(s); failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
