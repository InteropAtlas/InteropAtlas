#!/usr/bin/env python3
"""Deterministic safety tests for P6 Slice 0 Candidate identity preflight."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import yaml

from candidate_identity_validator import canonical_identifier_index, identity_route, load_yaml_records, validate_candidate
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

    def test_identifier_namespace_rejects_hyphen_and_accepts_underscore(self) -> None:
        for namespace, valid in [("agntcy-oasf", False), ("agntcy_oasf", True)]:
            with self.subTest(namespace=namespace):
                record = candidate("new", [{"namespace": namespace, "value": "1.0.0"}])
                errors = [item for item in validate_candidate(record, self.schema, {}) if item.severity == "error"]
                if valid:
                    self.assertEqual([], errors)
                else:
                    self.assertTrue(any(item.code == "IA-ID-001" and "external_identifiers.0.namespace" in item.message for item in errors))

    def test_yaml_date_identifier_rejects_implicit_date_and_accepts_string(self) -> None:
        for value_yaml, valid in [("2026-07-28", False), ('"2026-07-28"', True)]:
            with self.subTest(value_yaml=value_yaml):
                identifiers = yaml.safe_load(f"- namespace: mcp\n  value: {value_yaml}\n")
                self.assertEqual(valid, isinstance(identifiers[0]["value"], str))
                record = candidate("new", identifiers)
                errors = [item for item in validate_candidate(record, self.schema, {}) if item.severity == "error"]
                if valid:
                    self.assertEqual([], errors)
                else:
                    self.assertTrue(any(item.code == "IA-ID-001" and "external_identifiers.0.value" in item.message for item in errors))

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

    def test_library_citations_are_not_rfc_subject_identities(self) -> None:
        library = load_yaml_records(ROOT / "01_State/01_Objects/python_pyrfc3339.yaml")[0]
        legacy_rfc = load_yaml_records(ROOT / "01_State/01_Objects/rfc3339.yaml")[0]
        index = canonical_identifier_index([library, legacy_rfc])
        self.assertEqual(set(), evidence_backed_legacy_identifiers(library))
        self.assertEqual({"python_pyrfc3339"}, index[("github", "kurtraschke/pyrfc3339")])
        self.assertEqual({"python_pyrfc3339"}, index[("pypi", "pyrfc3339")])
        self.assertEqual({"rfc3339"}, index[("rfc", "3339")])
        self.assertNotIn(("rfc", "9557"), index)

        record = candidate("new", [{"namespace": "rfc", "value": "9557"}])
        self.assertEqual([], validate_candidate(record, self.schema, index))
        self.assertEqual("review_required", identity_route(record, index))

        duplicate = candidate("new", [{"namespace": "pypi", "value": "pyRFC3339"}])
        self.assertIn("IA-ID-003", {item.code for item in validate_candidate(duplicate, self.schema, index)})
        self.assertEqual("blocked_invalid_identity_state", identity_route(duplicate, index))

    def test_structured_identifiers_retain_official_and_version_aliases(self) -> None:
        record = {
            "id": "subject",
            "external_identifiers": [{"namespace": "bcp", "value": "14"}],
            "official_url": "https://www.rfc-editor.org/rfc/rfc2119.html",
            "versions": [{"url": "https://www.rfc-editor.org/info/rfc8174"}],
            "sources": [{"url": "https://www.rfc-editor.org/rfc/rfc9557.html"}],
        }
        self.assertEqual({("rfc", "2119"), ("rfc", "8174")}, evidence_backed_legacy_identifiers(record))
        self.assertEqual(
            {("bcp", "14"): {"subject"}, ("rfc", "2119"): {"subject"}, ("rfc", "8174"): {"subject"}},
            canonical_identifier_index([record]),
        )

    def test_explicit_rfc_duplicate_still_blocks_despite_unrelated_bibliography(self) -> None:
        canonical = {
            "id": "existing",
            "external_identifiers": [{"namespace": "rfc", "value": "9557"}],
            "sources": [{"url": "https://www.rfc-editor.org/rfc/rfc3339.html"}],
        }
        index = canonical_identifier_index([canonical])
        record = candidate("new", [{"namespace": "rfc", "value": "9557"}])
        self.assertIn("IA-ID-003", {item.code for item in validate_candidate(record, self.schema, index)})
        self.assertEqual("blocked_invalid_identity_state", identity_route(record, index))

    def test_unusable_explicit_identifiers_preserve_source_fallback(self) -> None:
        malformed_fields = [
            None, [], {}, "rfc:9557", 9557,
            [{"namespace": "rfc"}], [{"value": "9557"}],
            [None], ["rfc:9557"], [{}],
            [{"namespace": "rfc", "value": 9557}],
            [{"namespace": 9557, "value": "9557"}],
            [{"namespace": "", "value": "9557"}],
            [{"namespace": " ", "value": "9557"}],
            [{"namespace": "rfc", "value": ""}],
            [{"namespace": "rfc", "value": " \t\n"}],
            [{"namespace": "invalid-namespace", "value": "9557"}],
            [{"namespace": "RFC", "value": "9557"}],
            [{"namespace": "rfc\n", "value": "9557"}],
            [{"namespace": "rfc", "value": "9557", "extra": True}],
        ]
        valid = {"namespace": "pypi", "value": "pyRFC3339"}
        # A usable item must not hide malformed neighbours in either order.
        for field in list(malformed_fields):
            if isinstance(field, list) and field:
                malformed_fields.extend([[valid, *field], [*field, valid]])
        for field in ["absent", *malformed_fields]:
            with self.subTest(external_identifiers=field):
                record = {
                    "id": "legacy",
                    "sources": [{"url": "https://www.rfc-editor.org/rfc/rfc9557.html"}],
                }
                if field != "absent":
                    record["external_identifiers"] = field
                self.assertEqual({("rfc", "9557")}, evidence_backed_legacy_identifiers(record))
                index = canonical_identifier_index([record])
                self.assertEqual({"legacy"}, index[("rfc", "9557")])
                incoming = candidate("new", [{"namespace": "rfc", "value": "9557"}])
                self.assertEqual("blocked_invalid_identity_state", identity_route(incoming, index))

    def test_valid_explicit_item_shape_suppresses_only_bibliography(self) -> None:
        for identifiers in [
            [{"namespace": "pypi", "value": "pyRFC3339"}],
            [{"namespace": "test_namespace1", "value": " subject "}],
            [{"namespace": "github", "value": "owner/project"}, {"namespace": "pypi", "value": "project"}],
        ]:
            with self.subTest(external_identifiers=identifiers):
                record = candidate("new", identifiers)
                self.assertEqual([], validate_candidate(record, self.schema, {}))
                record["sources"] = [{"url": "https://www.rfc-editor.org/rfc/rfc9557.html"}]
                self.assertEqual(set(), evidence_backed_legacy_identifiers(record))

    def test_source_only_legacy_rfc_and_version_aliases_are_unchanged(self) -> None:
        for filename, identifiers in [
            ("rfc3339.yaml", {("rfc", "3339")}),
            ("json-pointer-rfc6901.yaml", {("rfc", "6901")}),
            ("bcp14-rfc2119-rfc8174.yaml", {("rfc", "2119"), ("rfc", "8174")}),
        ]:
            with self.subTest(filename=filename):
                record = load_yaml_records(ROOT / "01_State/01_Objects" / filename)[0]
                self.assertEqual(identifiers, evidence_backed_legacy_identifiers(record))

    def test_legacy_url_standard_citation_limitation_is_out_of_scope(self) -> None:
        # This source-only record has no structured IDs. Fixing its cross-subject
        # citation requires separate work; do not silently remove Legacy evidence.
        record = load_yaml_records(ROOT / "01_State/01_Objects/url-living-standard.yaml")[0]
        self.assertEqual({("rfc", "3986")}, evidence_backed_legacy_identifiers(record))


if __name__ == "__main__":
    unittest.main()
