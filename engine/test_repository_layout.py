#!/usr/bin/env python3
"""Regression checks for the InteropAtlas repository layout contract."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from bootstrap_query import load_atlas
from render_markdown import output_path
from repository_layout import repository_layout, validate_data_root


class RepositoryLayoutTests(unittest.TestCase):
    @staticmethod
    def write_standard(root: Path, data_root: Path, marker: str) -> Path:
        path = root / data_root / "standards" / "sample.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "\n".join(
                [
                    "id: sample_standard",
                    "type: standard",
                    f"name_en: Sample Standard {marker}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return path

    def test_logical_source_and_generated_path_survive_data_root_move(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_standard(root, Path("."), "current")
            self.write_standard(root, Path("data"), "future")

            current_objects, current_relations = load_atlas(root)
            future_objects, future_relations = load_atlas(root, Path("data"))

            self.assertEqual(len(current_objects), 1)
            self.assertEqual(len(future_objects), 1)
            self.assertEqual(current_relations, [])
            self.assertEqual(future_relations, [])

            current = current_objects[0]
            future = future_objects[0]

            self.assertEqual(current["id"], future["id"])
            self.assertEqual(current["_source"], "standards/sample.yaml")
            self.assertEqual(future["_source"], "standards/sample.yaml")
            self.assertEqual(current["_physical_source"], "standards/sample.yaml")
            self.assertEqual(future["_physical_source"], "data/standards/sample.yaml")
            self.assertEqual(output_path(current), "standards/sample.md")
            self.assertEqual(output_path(future), "standards/sample.md")

    def test_data_root_is_repository_relative(self) -> None:
        with self.assertRaises(ValueError):
            validate_data_root(Path("../outside"))
        with self.assertRaises(ValueError):
            validate_data_root(Path("/absolute/data"))

    def test_unknown_family_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            layout = repository_layout(Path(temporary))
            with self.assertRaises(ValueError):
                layout.family_path("not-a-family")


if __name__ == "__main__":
    unittest.main()
