#!/usr/bin/env python3
"""Regression tests for Legacy/v0 Human Route rendering compatibility."""

from __future__ import annotations

import unittest

from render_markdown import render_object, semantic_view_type


class SemanticRenderingTests(unittest.TestCase):
    def test_capability_legacy_and_v0_share_renderer(self) -> None:
        legacy = {
            "id": "cap-legacy",
            "type": "capability",
            "name_zh": "能力",
            "name_en": "Capability",
            "category": "coordinate",
        }
        v0 = {
            "id": "cap-v0",
            "type": "concept",
            "kind": "capability",
            "name_zh": "能力",
            "name_en": "Capability",
            "category": "coordinate",
        }
        self.assertEqual(semantic_view_type(legacy), "capability")
        self.assertEqual(semantic_view_type(v0), "capability")
        self.assertIn("能力类别", render_object(v0, {"cap-v0": v0}))

    def test_implementation_legacy_and_v0_share_renderer(self) -> None:
        legacy = {
            "id": "legacy",
            "type": "implementation",
            "kind": "software",
            "name_zh": "实现",
            "name_en": "Implementation",
        }
        v0 = {
            "id": "v0",
            "type": "system",
            "kind": "service",
            "name_zh": "实现",
            "name_en": "Implementation",
        }
        self.assertEqual(semantic_view_type(legacy), "implementation")
        self.assertEqual(semantic_view_type(v0), "implementation")
        self.assertIn("实现类别", render_object(v0, {"v0": v0}))

    def test_normative_artifact_legacy_and_v0_share_renderer(self) -> None:
        legacy = {
            "id": "legacy",
            "type": "standard",
            "kind": "format",
            "name_zh": "格式",
            "name_en": "Format",
        }
        v0 = {
            "id": "v0",
            "type": "artifact",
            "kind": "format",
            "name_zh": "格式",
            "name_en": "Format",
        }
        self.assertEqual(semantic_view_type(legacy), "standard")
        self.assertEqual(semantic_view_type(v0), "standard")
        self.assertIn("标准类别", render_object(v0, {"v0": v0}))


if __name__ == "__main__":
    unittest.main()
