#!/usr/bin/env python3
"""Regression checks for the InteropAtlas physical storage contract."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from bootstrap_query import load_atlas
from render_markdown import output_path
from repository_layout import repository_layout, validate_storage_path


class RepositoryLayoutTests(unittest.TestCase):
    def test_current_storage_keeps_current_generated_path(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "standards" / "sample.yaml"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "id: sample_standard\n"
                "type: standard\n"
                "name_zh: 示例标准\n"
                "name_en: Sample Standard\n",
                encoding="utf-8",
            )

            objects, relations = load_atlas(root, [Path("standards")])

            self.assertEqual(relations, [])
            self.assertEqual(len(objects), 1)
            self.assertEqual(objects[0]["_source"], "standards/sample.yaml")
            self.assertEqual(objects[0]["_physical_source"], "standards/sample.yaml")
            self.assertEqual(output_path(objects[0]), "standards/sample.md")
            self.assertNotIn("_object_family", objects[0])

    def test_mixed_storage_classifies_from_content_not_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mixed = root / "mixed" / "nested"
            mixed.mkdir(parents=True, exist_ok=True)

            (mixed / "standard.yaml").write_text(
                "id: sample_standard\n"
                "type: standard\n"
                "name_zh: 示例标准\n"
                "name_en: Sample Standard\n",
                encoding="utf-8",
            )
            (mixed / "capability.yaml").write_text(
                "id: sample_capability\n"
                "type: capability\n"
                "name_zh: 示例能力\n"
                "name_en: Sample Capability\n",
                encoding="utf-8",
            )
            # Intentionally omit `type: relation` to cover the current legacy
            # structural relation form. It must still work outside relations/.
            (mixed / "edge.yaml").write_text(
                "id: sample_relation\n"
                "source: sample_standard\n"
                "relation: provides\n"
                "target: sample_capability\n",
                encoding="utf-8",
            )

            objects, relations = load_atlas(root, [Path("mixed")])

            self.assertEqual({obj["type"] for obj in objects}, {"standard", "capability"})
            self.assertEqual([relation["id"] for relation in relations], ["sample_relation"])
            self.assertEqual(relations[0]["_physical_source"], "mixed/nested/edge.yaml")

    def test_storage_paths_are_repository_relative(self) -> None:
        with self.assertRaises(ValueError):
            validate_storage_path(Path("../outside"))
        with self.assertRaises(ValueError):
            validate_storage_path(Path("/absolute/data"))

    def test_arbitrary_storage_name_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            layout = repository_layout(Path(temporary), [Path("anything-we-decide-later")])
            self.assertEqual(layout.storage_paths, (Path("anything-we-decide-later"),))


if __name__ == "__main__":
    unittest.main()
