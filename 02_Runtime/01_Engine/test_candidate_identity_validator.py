#!/usr/bin/env python3
"""Deterministic safety tests for P6 Slice 0 Candidate identity preflight."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from candidate_identity_validator import canonical_identifier_index, identity_route, validate_candidate
from legacy_identity_adapter import evidence_backed_legacy_identifiers


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "01_State/01_Objects/candidate-object.v1.schema.json"


def candidate(state: str, identifiers: list[dict[str, str]], matched: list[str] | None = None, reasons: list[str] | None = None) -> dict:
    return {
        "contract_version": "candidate-object-v1",
        "candidate_id": f"test-{state.replace('_', '-')}",
        "label": "Test Candidate",
        "publisher": "Test Publisher",
        "family": None,
        "kind": "specification",
        "external_identifiers": identifiers,
        "locators": [{"url": "https://example.org/spec", "role": "official"}],
        "identity_resolution": {
            "state": state,
            "matched_canonical_ids": matched or [],
            "reasons": reasons or [],
            "merge_authorized": False,
        },
        "unknowns": [],
        "provenance": {
            "initiator": "Human — test",
            "executor": "Agent — test",
            "reviewer": None,
        },
    }


class CandidateIdentitySafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    def test_new_unique_identifier_is_review_required_not_auto_accepted(self) -> None:
        record = candidate("new", [{"namespace": "rfc", "value": "9114"}])
        findings = validate_candidate(record, self.schema, {})
        self.assertEqual([], [item for item in findings if item.severity == "error"])
        self.assertEqual("review_required", identity_route(record, {}))

    def test_known_duplicate_routes_to_existing_without_merge(self) -> None:
        canonical = [{"id": "bcp47_rfc5646", "official_url": "https://www.rfc-editor.org/rfc/rfc5646.html"}]
        index = canonical_identifier_index(canonical)
        record = candidate(
            "duplicate",
            [{"namespace": "rfc", "value": "5646"}],
            matched=["bcp47_rfc5646"],
        )
        findings = validate_candidate(record, self.schema, index)
        self.assertEqual([], [item for item in findings if item.severity == "error"])
        self.assertEqual("duplicate_existing", identity_route(record, index))

    def test_collision_cannot_be_declared_new(self) -> None:
        canonical = [{"id": "existing", "external_identifiers": [{"namespace": "rfc", "value": "9114"}]}]
        index = canonical_identifier_index(canonical)
        record = candidate("new", [{"namespace": "RFC", "value": " 9114 "}])
        codes = {item.code for item in validate_candidate(record, self.schema, index)}
        self.assertIn("IA-ID-003", codes)
        self.assertEqual("blocked_invalid_identity_state", identity_route(record, index))

    def test_one_candidate_colliding_with_multiple_subjects_must_block(self) -> None:
        canonical = [
            {"id": "subject-a", "external_identifiers": [{"namespace": "test", "value": "same"}]},
            {"id": "subject-b", "external_identifiers": [{"namespace": "test", "value": "same"}]},
        ]
        index = canonical_identifier_index(canonical)
        record = candidate(
            "identity_risk",
            [{"namespace": "test", "value": "same"}],
            matched=["subject-a", "subject-b"],
            reasons=["Identifier collision spans multiple Canonical subjects."],
        )
        findings = validate_candidate(record, self.schema, index)
        self.assertEqual([], [item for item in findings if item.severity == "error"])
        self.assertEqual("identity_review_required", identity_route(record, index))

    def test_legacy_adapter_does_not_guess_from_title(self) -> None:
        record = {
            "id": "lookalike",
            "name_en": "RFC 5646",
            "official_url": "https://example.org/rfc5646",
        }
        self.assertEqual(set(), evidence_backed_legacy_identifiers(record))

    def test_rfc_editor_locator_is_evidence_backed_legacy_identifier(self) -> None:
        record = {
            "id": "bcp47_rfc5646",
            "official_url": "https://www.rfc-editor.org/rfc/rfc5646.html",
        }
        self.assertEqual({("rfc", "5646")}, evidence_backed_legacy_identifiers(record))


if __name__ == "__main__":
    unittest.main()
