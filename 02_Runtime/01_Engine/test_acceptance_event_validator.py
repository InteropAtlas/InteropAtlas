#!/usr/bin/env python3
"""Deterministic safety tests for the V1 acceptance-event boundary."""

from __future__ import annotations

import json
from pathlib import Path

from acceptance_event_validator import validate_acceptance_event


SCHEMA = json.loads(Path("01_State/04_Acceptance_Events/acceptance-event.v1.schema.json").read_text(encoding="utf-8"))


def event(decision: str, route: str, impact: str = "M1") -> dict:
    value = {
        "contract_version": "acceptance-event-v1",
        "event_id": f"test-{decision}-{route}",
        "candidate_id": "candidate-test",
        "decision": decision,
        "machine_route": route,
        "review": {
            "reviewer": "Agent — independent reviewer",
            "reviewed_at": "2026-09-04T14:30:00+08:00",
            "independent_from_executor": True,
            "notes": []
        },
        "authority": {
            "mutation_impact": impact,
            "ordinary_path": impact in {"M0", "M1"},
            "approver": None if impact in {"M0", "M1"} else "Human Maintainer"
        },
        "evidence_basis": ["https://example.org/official-source"],
        "decided_at": "2026-09-04T14:31:00+08:00",
        "notes": []
    }
    if decision in {"accepted", "duplicate"}:
        value["accepted_canonical_id"] = "canonical-test"
    return value


def codes(value: dict) -> set[str]:
    return {item.code for item in validate_acceptance_event(value, SCHEMA)}


def test_ordinary_acceptance_requires_review_route() -> None:
    assert not codes(event("accepted", "review_required"))


def test_duplicate_is_disposition_not_merge() -> None:
    assert not codes(event("duplicate", "duplicate_existing"))


def test_identity_review_cannot_be_ordinary_acceptance() -> None:
    assert "IA-ACCEPT-001" in codes(event("accepted", "identity_review_required"))
    assert "IA-ACCEPT-002" in codes(event("accepted", "identity_review_required"))


def test_m2_m3_require_explicit_approver() -> None:
    value = event("deferred", "deferred", "M2")
    value["authority"]["ordinary_path"] = True
    value["authority"]["approver"] = None
    found = codes(value)
    assert "IA-ACCEPT-001" in found
    assert "IA-ACCEPT-003" in found


def test_self_review_cannot_authorize_acceptance() -> None:
    value = event("accepted", "review_required")
    value["review"]["independent_from_executor"] = False
    found = codes(value)
    assert "IA-ACCEPT-001" in found
    assert "IA-ACCEPT-004" in found


if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_") and callable(value)]
    for test in tests:
        test()
    print(f"acceptance event checks: PASS ({len(tests)} tests)")
