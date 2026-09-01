#!/usr/bin/env python3
"""Regression tests for the #61 I2 controlled kind registry."""

from __future__ import annotations

import unittest

from kind_registry import load_kind_registry, profiles_for_v0_identity, validate_v0_identity


class KindRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = load_kind_registry()

    def test_registered_family_kind_pair_passes(self) -> None:
        record = {"id": "cap", "type": "concept", "kind": "capability"}
        self.assertEqual(validate_v0_identity(record, self.registry), ())
        self.assertEqual(profiles_for_v0_identity(record, self.registry), ("capability",))

    def test_unknown_kind_fails(self) -> None:
        record = {"id": "bad", "type": "concept", "kind": "banana"}
        findings = validate_v0_identity(record, self.registry)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].code, "IA-MR-005")

    def test_kind_in_wrong_family_fails(self) -> None:
        record = {"id": "bad", "type": "agent", "kind": "software"}
        findings = validate_v0_identity(record, self.registry)
        self.assertEqual(len(findings), 1)
        self.assertIn("belongs to family 'system'", findings[0].message)

    def test_v0_identity_without_kind_fails(self) -> None:
        record = {"id": "bad", "type": "concept"}
        findings = validate_v0_identity(record, self.registry)
        self.assertEqual(len(findings), 1)
        self.assertIn("requires a controlled kind", findings[0].message)

    def test_legacy_records_are_not_enforced_by_i2(self) -> None:
        legacy = {"id": "legacy", "type": "implementation", "kind": "software"}
        self.assertEqual(validate_v0_identity(legacy, self.registry), ())

    def test_audit_required_legacy_boundary_is_not_forced(self) -> None:
        boundary = {"id": "api", "type": "standard", "kind": "api"}
        self.assertEqual(validate_v0_identity(boundary, self.registry), ())

    def test_seed_registry_has_no_other_term(self) -> None:
        self.assertNotIn("other", self.registry["terms"])


if __name__ == "__main__":
    unittest.main()
