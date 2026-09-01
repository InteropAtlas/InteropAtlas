#!/usr/bin/env python3
"""Regression tests for the #61 I1 semantic normalization layer."""

from __future__ import annotations

import unittest

from semantic_model import (
    is_capability,
    is_identity,
    is_implementation_system,
    is_organization_agent,
    normalize_record,
    semantic_family,
    semantic_kind,
)


class SemanticModelTests(unittest.TestCase):
    def test_legacy_capability_and_v0_capability_share_semantics(self) -> None:
        legacy = {"id": "cap", "type": "capability"}
        v0 = {"id": "cap", "type": "concept", "kind": "capability"}

        self.assertTrue(is_capability(legacy))
        self.assertTrue(is_capability(v0))
        self.assertEqual(semantic_family(legacy), "concept")
        self.assertEqual(semantic_kind(v0), "capability")
        self.assertEqual(normalize_record(legacy).profiles, ("capability",))
        self.assertEqual(normalize_record(v0).profiles, ("capability",))

    def test_legacy_and_v0_software_share_implementation_semantics(self) -> None:
        legacy = {"id": "forgejo_actions", "type": "implementation", "kind": "software"}
        v0 = {"id": "forgejo_actions", "type": "system", "kind": "software"}

        self.assertEqual(normalize_record(legacy).family, "system")
        self.assertEqual(normalize_record(legacy).profiles, ("implementation",))
        self.assertEqual(normalize_record(v0).profiles, ("implementation",))
        self.assertTrue(is_implementation_system(legacy))
        self.assertTrue(is_implementation_system(v0))

    def test_reference_implementation_requires_identity_audit_without_guessed_family(self) -> None:
        record = {"id": "sample", "type": "implementation", "kind": "reference_implementation"}
        descriptor = normalize_record(record)
        self.assertIsNone(descriptor.family)
        self.assertEqual(descriptor.migration_status, "audit_required")
        self.assertFalse(is_implementation_system(record))

    def test_organization_open_source_project_requires_audit_without_guessed_family(self) -> None:
        record = {
            "id": "sample",
            "type": "organization",
            "organization_kind": "open_source_project",
        }
        descriptor = normalize_record(record)
        self.assertIsNone(descriptor.family)
        self.assertEqual(descriptor.kind, "open_source_project")
        self.assertEqual(descriptor.migration_status, "audit_required")
        self.assertFalse(is_organization_agent(record))

    def test_legacy_standard_boundary_is_not_guessed(self) -> None:
        clear = normalize_record({"id": "yaml", "type": "standard", "kind": "standard"})
        boundary = normalize_record({"id": "api", "type": "standard", "kind": "api"})
        unknown = normalize_record({"id": "odd", "type": "standard", "kind": "service"})

        self.assertEqual(clear.family, "artifact")
        self.assertEqual(clear.migration_status, "legacy")
        self.assertIsNone(boundary.family)
        self.assertEqual(boundary.migration_status, "audit_required")
        self.assertIsNone(unknown.family)
        self.assertEqual(unknown.migration_status, "audit_required")

    def test_reference_project_has_no_guessed_family(self) -> None:
        descriptor = normalize_record(
            {"id": "apple_hig", "type": "reference_project", "kind": "guideline"}
        )
        self.assertTrue(is_identity({"type": "reference_project"}))
        self.assertIsNone(descriptor.family)
        self.assertEqual(descriptor.migration_status, "audit_required")

    def test_relation_is_statement_even_without_explicit_type(self) -> None:
        relation = {"id": "edge", "source": "a", "relation": "provides", "target": "b"}
        descriptor = normalize_record(relation)
        self.assertEqual(descriptor.record_class, "statement")
        self.assertEqual(descriptor.kind, "relation")
        self.assertFalse(is_identity(relation))

    def test_map_and_open_gap_are_not_identity_families(self) -> None:
        self.assertEqual(normalize_record({"type": "map"}).record_class, "view")
        self.assertEqual(normalize_record({"type": "open_gap"}).record_class, "finding")
        self.assertIsNone(normalize_record({"type": "map"}).family)

    def test_normalization_does_not_mutate_source_record(self) -> None:
        record = {"id": "cap", "type": "capability"}
        before = dict(record)
        normalize_record(record)
        self.assertEqual(record, before)
        self.assertNotIn("record_class", record)
        self.assertNotIn("family", record)


if __name__ == "__main__":
    unittest.main()
