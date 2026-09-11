#!/usr/bin/env python3
from __future__ import annotations

import unittest

from migration_cohort import classify_record


class MigrationCohortTests(unittest.TestCase):
    def test_lossless_binary_relation(self):
        record = {
            "id": "engine_v0_1_uses_semver",
            "type": "relation",
            "source": "engine_v0_1_bootstrap",
            "relation": "uses",
            "target": "semantic_versioning_2_0_0",
        }
        plan = classify_record(record, "relation.yaml")
        self.assertEqual(plan.mapping_class, "A")
        self.assertEqual(plan.disposition, "eligible_dry_run")
        self.assertTrue(plan.stable_id_preserved)
        self.assertEqual(plan.proposed_patch["v1_relation"]["predicate"], "uses")

    def test_additive_locator_and_verification_normalization(self):
        record = {
            "id": "apple_human_interface_guidelines",
            "type": "reference_project",
            "official_url": "https://developer.apple.com/design/human-interface-guidelines/",
            "last_verified": "2026-09-01",
            "project_kind": "other",
        }
        plan = classify_record(record, "hig.yaml")
        self.assertEqual(plan.mapping_class, "B")
        self.assertEqual(plan.disposition, "eligible_dry_run")
        self.assertEqual(plan.proposed_patch["locators"][0]["role"], "official_current")
        self.assertEqual(plan.proposed_patch["last_verified_at"], "2026-09-01T00:00:00Z")
        self.assertIn("official_url", plan.preserved_legacy_fields)
        self.assertNotIn("classification", plan.proposed_patch)

    def test_unknown_semantic_mapping_is_excluded(self):
        record = {"id": "x", "type": "reference_project", "project_kind": "other"}
        plan = classify_record(record, "x.yaml")
        self.assertEqual(plan.mapping_class, "ambiguous")
        self.assertEqual(plan.disposition, "exclude")

    def test_missing_id_is_excluded(self):
        plan = classify_record({"type": "relation"}, "bad.yaml")
        self.assertFalse(plan.stable_id_preserved)
        self.assertEqual(plan.disposition, "exclude")


if __name__ == "__main__":
    unittest.main()
