#!/usr/bin/env python3
"""Regression tests for Legacy/v0 Human Route rendering compatibility."""

from __future__ import annotations

import unittest
from pathlib import Path

from bootstrap_query import index_objects, load_atlas
from render_markdown import render_object, semantic_view_type
from workspace_projection import project_field


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

    def test_normative_version_and_scope_are_projected_without_reinterpretation(self) -> None:
        for object_type in ("standard", "artifact"):
            with self.subTest(object_type=object_type):
                record = {
                    "id": "format", "type": object_type, "kind": "format",
                    "name_zh": "格式", "name_en": "Format",
                    "version": "1.2", "scope_notes_zh": "仅固定此版次，不证明实现兼容。",
                }
                rendered = render_object(record, {record["id"]: record})
                self.assertIn("- **记录版次：** " + project_field(record, "version")["value"], rendered)
                self.assertIn("## 范围与边界\n\n" + project_field(record, "scope_notes_zh")["value"], rendered)
                self.assertNotIn("## 版本\n", rendered)
                self.assertNotIn("最新版", rendered)

    def test_singular_version_does_not_replace_or_hide_versions_list(self) -> None:
        record = {
            "id": "format", "type": "artifact", "kind": "format",
            "name_zh": "格式", "name_en": "Format", "version": "2.0",
            "versions": [{"version": "1.0", "status": "published", "date": "2020-01-01"}],
        }
        rendered = render_object(record, {record["id"]: record})
        self.assertIn("- **记录版次：** 2.0", rendered)
        self.assertIn("## 版本\n", rendered)
        self.assertIn("1.0 · 2020-01-01", rendered)

    def test_missing_or_empty_version_and_scope_do_not_create_claims(self) -> None:
        for optional in ({}, {"version": None, "scope_notes_zh": None},
                         {"version": "", "scope_notes_zh": ""},
                         {"version": "  ", "scope_notes_zh": "  "}):
            with self.subTest(optional=optional):
                record = {
                    "id": "format", "type": "artifact", "kind": "format",
                    "name_zh": "格式", "name_en": "Format", **optional,
                }
                rendered = render_object(record, {record["id"]: record})
                self.assertNotIn("记录版次", rendered)
                self.assertNotIn("## 范围与边界", rendered)
                self.assertNotIn("无范围限制", rendered)

    def test_real_media_records_keep_scope_version_and_source(self) -> None:
        objects, _ = load_atlas(Path(__file__).resolve().parents[2])
        index = index_objects(objects)
        for object_id in ("w3c_imsc", "w3c_ttml2", "ebu_tt_d", "aom_av1", "ebu_rf64"):
            with self.subTest(object_id=object_id):
                record = index[object_id]
                rendered = render_object(record, index)
                self.assertIn("- **记录版次：** " + record["version"], rendered)
                self.assertIn(record["scope_notes_zh"], rendered)
                for source in record["sources"]:
                    self.assertIn(source["url"], rendered)
                for version in record.get("versions", []):
                    self.assertIn("## 版本\n", rendered)
                    self.assertIn(str(version["version"]), rendered)


if __name__ == "__main__":
    unittest.main()
