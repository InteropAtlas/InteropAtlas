#!/usr/bin/env python3
"""Regression tests for #61 I4 Relation compatibility."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from graph_index import GraphIndex
from relation_model import compatibility_warnings, normalize_relation


ROOT = Path(__file__).resolve().parents[2]
RELATION_SCHEMA = ROOT / "01_State" / "02_Relations" / "relation.v0.schema.json"


class RelationModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with RELATION_SCHEMA.open("r", encoding="utf-8") as handle:
            cls.schema = json.load(handle)
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def test_v0_relation_uses_id_only_refs(self) -> None:
        record = {
            "id": "a_to_b",
            "type": "relation",
            "source": "a",
            "relation": "compatible_with",
            "target": "b",
            "context": {"capabilities": ["cap"]},
        }
        self.assertEqual(list(self.validator.iter_errors(record)), [])
        descriptor = normalize_relation(record)
        self.assertTrue(descriptor.canonical_refs)
        self.assertEqual(descriptor.source_id, "a")
        self.assertEqual(descriptor.context["capabilities"], ["cap"])

    def test_v0_schema_rejects_legacy_ref_and_bare_confidence(self) -> None:
        legacy_ref = {
            "id": "a_to_b",
            "type": "relation",
            "source": {"type": "implementation", "id": "a"},
            "relation": "compatible_with",
            "target": "b",
        }
        self.assertTrue(list(self.validator.iter_errors(legacy_ref)))
        bare_confidence = {
            "id": "a_to_b",
            "type": "relation",
            "source": "a",
            "relation": "compatible_with",
            "target": "b",
            "confidence": 0.8,
        }
        self.assertTrue(list(self.validator.iter_errors(bare_confidence)))

    def test_legacy_context_normalizes_without_mutation(self) -> None:
        record = {
            "id": "legacy",
            "type": "relation",
            "source": {"type": "implementation", "id": "a"},
            "relation": "alternative_to",
            "target": {"type": "implementation", "id": "b"},
            "capability_context": ["cap"],
            "scenario_context": "scenario",
            "conditions_zh": "条件",
        }
        original = dict(record)
        descriptor = normalize_relation(record)
        self.assertEqual(descriptor.context["capabilities"], ["cap"])
        self.assertEqual(descriptor.context["scenarios"], ["scenario"])
        self.assertEqual(descriptor.context["conditions_zh"], "条件")
        self.assertEqual(record, original)

    def test_stale_type_hint_is_warning_not_broken_edge(self) -> None:
        objects = {
            "a": {"id": "a", "type": "system", "kind": "software"},
            "b": {"id": "b", "type": "system", "kind": "service"},
        }
        relation = {
            "id": "legacy",
            "type": "relation",
            "source": {"type": "implementation", "id": "a"},
            "relation": "compatible_with",
            "target": {"type": "implementation", "id": "b"},
        }
        warnings = compatibility_warnings(relation, objects)
        self.assertEqual(len(warnings), 2)
        graph = GraphIndex(objects, [relation])
        self.assertEqual(graph.issues, [])
        self.assertEqual(len(graph.edges), 1)
        self.assertEqual(len(graph.compatibility_warnings), 2)


if __name__ == "__main__":
    unittest.main()
