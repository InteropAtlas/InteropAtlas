#!/usr/bin/env python3
"""Regression tests for #75 / #61 I6 representative migration pilot."""

from __future__ import annotations

import unittest
from pathlib import Path

from bootstrap_query import index_objects, load_atlas, run
from kind_registry import has_profile, load_kind_registry
from relation_model import normalize_relation
from semantic_model import normalize_record


ROOT = Path(__file__).resolve().parents[2]


class RepresentativeMigrationPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.objects, cls.relations = load_atlas(ROOT)
        cls.index = index_objects(cls.objects)
        cls.registry = load_kind_registry()
        cls.relation_index = {
            record.get("id"): record
            for record in cls.relations
            if isinstance(record.get("id"), str)
        }

    def test_capability_migrated_without_id_change(self) -> None:
        record = self.index["automated_build_deployment"]
        descriptor = normalize_record(record)
        self.assertEqual(record["id"], "automated_build_deployment")
        self.assertEqual((descriptor.family, descriptor.kind), ("concept", "capability"))
        self.assertEqual(descriptor.migration_status, "v0")
        self.assertTrue(has_profile(record, "capability", self.registry))

    def test_scenario_migrated_to_structured_requires(self) -> None:
        record = self.index["engine_v0_1_bootstrap"]
        descriptor = normalize_record(record)
        self.assertEqual((descriptor.family, descriptor.kind), ("concept", "scenario"))
        self.assertNotIn("requirements", record)
        self.assertGreaterEqual(len(record["requires"]), 1)
        self.assertTrue(all("capability" in item for item in record["requires"]))
        self.assertTrue(all(item.get("priority") == "required" for item in record["requires"]))

    def test_platform_services_share_v0_implementation_profile(self) -> None:
        for object_id in ("forgejo_actions", "github_actions"):
            record = self.index[object_id]
            descriptor = normalize_record(record)
            self.assertEqual((descriptor.family, descriptor.kind), ("system", "platform_service"))
            self.assertTrue(has_profile(record, "implementation", self.registry))
            self.assertIn("automated_build_deployment", record.get("capabilities", []))

    def test_organization_migrated_to_agent_identity(self) -> None:
        record = self.index["apple"]
        descriptor = normalize_record(record)
        self.assertEqual((descriptor.family, descriptor.kind), ("agent", "organization"))
        self.assertEqual(record.get("jurisdiction"), "global")
        self.assertTrue(has_profile(record, "organization", self.registry))

    def test_relation_migrated_to_id_only_refs(self) -> None:
        record = self.relation_index["engine_v0_1_uses_semver"]
        descriptor = normalize_relation(record)
        self.assertTrue(descriptor.canonical_refs)
        self.assertEqual(descriptor.source_id, "engine_v0_1_bootstrap")
        self.assertEqual(descriptor.target_id, "semantic_versioning_2_0_0")

    def test_supportability_query_preserves_results_and_scope(self) -> None:
        result = run(ROOT, "automated_build_deployment")
        ids = set(result["implementation_ids"])
        self.assertEqual(ids, {"forgejo_actions", "github_actions"})
        self.assertEqual(set(result["open_source_and_self_hostable_ids"]), {"forgejo_actions"})
        self.assertEqual(
            result["alternative_relations"],
            [
                {
                    "source": "forgejo_actions",
                    "relation": "alternative_to",
                    "target": "github_actions",
                }
            ],
        )

    def test_negative_cases_remain_legacy_for_semantic_reasons(self) -> None:
        artifact = self.index["semantic_versioning_2_0_0"]
        self.assertEqual(artifact.get("type"), "standard")
        self.assertIn("maturity", artifact)

        relation = self.relation_index["forgejo_actions_alternative_to_github_actions"]
        self.assertIsInstance(relation.get("source"), dict)
        self.assertIn("confidence", relation)


if __name__ == "__main__":
    unittest.main()
