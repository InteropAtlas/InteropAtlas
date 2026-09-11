#!/usr/bin/env python3
"""Integration regression tests for I1 semantic consumers."""

from __future__ import annotations

import unittest

from bootstrap_query import implementations_for_capability
from graph_index import GraphIndex


class SemanticConsumerTests(unittest.TestCase):
    def test_graph_accepts_v0_capability_reference(self) -> None:
        objects = {
            "cap": {
                "id": "cap",
                "type": "concept",
                "kind": "capability",
                "name_zh": "能力",
                "name_en": "Capability",
            },
            "tool": {
                "id": "tool",
                "type": "implementation",
                "kind": "software",
                "capabilities": ["cap"],
            },
        }
        graph = GraphIndex(objects, [])
        self.assertEqual(graph.issues, [])
        self.assertEqual(len(graph.edges), 1)
        self.assertEqual(graph.edges[0].target_id, "cap")

    def test_query_treats_legacy_and_v0_implementation_profiles_equally(self) -> None:
        objects = [
            {
                "id": "legacy",
                "type": "implementation",
                "kind": "software",
                "capabilities": ["cap"],
            },
            {
                "id": "v0-service",
                "type": "system",
                "kind": "service",
                "capabilities": ["cap"],
            },
            {
                "id": "not-implementation",
                "type": "system",
                "kind": "design_system",
                "capabilities": ["cap"],
            },
        ]
        matches = implementations_for_capability(objects, "cap")
        self.assertEqual([item["id"] for item in matches], ["legacy", "v0-service"])


if __name__ == "__main__":
    unittest.main()
