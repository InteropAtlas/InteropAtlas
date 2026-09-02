#!/usr/bin/env python3
"""Deterministic evidence for the Gate B Minimal Compare contract (#94)."""

from __future__ import annotations

import unittest
from pathlib import Path

from bootstrap_query import index_objects, load_atlas
from relation_model import normalize_relation


ROOT = Path(__file__).resolve().parents[2]
CAPABILITY = "automated_build_deployment"
CANDIDATES = ("forgejo_actions", "github_actions")


class MinimalCompareContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        objects, relations = load_atlas(ROOT)
        cls.index = index_objects(objects)
        cls.relations = relations

    def test_candidates_share_explicit_compare_context(self) -> None:
        for object_id in CANDIDATES:
            record = self.index[object_id]
            self.assertIn(CAPABILITY, record.get("capabilities", []))

    def test_gate_b_dimensions_are_recorded_facts(self) -> None:
        forgejo = self.index["forgejo_actions"]
        github = self.index["github_actions"]

        self.assertIs(forgejo.get("open_source"), True)
        self.assertIs(github.get("open_source"), False)
        self.assertIs(forgejo.get("self_hostable"), True)
        self.assertIs(github.get("self_hostable"), False)
        self.assertEqual(forgejo.get("license_expression"), "GPL-3.0-or-later")
        self.assertNotIn("license_expression", github)
        self.assertIn("self_hosted_runner", forgejo.get("deployment_models", []))
        self.assertIn("self_hosted_runner", github.get("deployment_models", []))
        self.assertIn("self_hosted_platform", forgejo.get("deployment_models", []))
        self.assertNotIn("self_hosted_platform", github.get("deployment_models", []))

    def test_alternative_relation_is_contextual_not_compatibility(self) -> None:
        relation = next(
            item
            for item in self.relations
            if item.get("id") == "forgejo_actions_alternative_to_github_actions"
        )
        descriptor = normalize_relation(relation)

        self.assertEqual(descriptor.source_id, "forgejo_actions")
        self.assertEqual(descriptor.target_id, "github_actions")
        self.assertEqual(descriptor.predicate, "alternative_to")
        self.assertIn(CAPABILITY, descriptor.context.get("capabilities", []))
        self.assertNotEqual(descriptor.predicate, "compatible_with")
        self.assertNotEqual(descriptor.predicate, "equivalent_to")

    def test_missing_license_is_absence_not_negative_fact(self) -> None:
        github = self.index["github_actions"]
        self.assertNotIn("license_expression", github)
        self.assertIs(github.get("open_source"), False)


if __name__ == "__main__":
    unittest.main()
