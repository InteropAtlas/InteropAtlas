#!/usr/bin/env python3
"""Deterministic tests for the first Human Route Search slice (#103)."""

from __future__ import annotations

import unittest
from pathlib import Path

import human_route_runtime as human_route
import human_route_search as human_search
import render_markdown as human_markdown
import render_site_semantic as semantic_site
from bootstrap_query import index_objects, load_atlas
from render_markdown import display_name, output_path


ROOT = Path(__file__).resolve().parents[2]


class HumanRouteSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        objects, _ = load_atlas(ROOT)
        index = index_objects(objects)
        rendered = []
        for obj in index.values():
            if semantic_site.semantic_site_view_type(obj) not in semantic_site.SUPPORTED_VIEW_TYPES:
                continue
            path = output_path(obj)
            if path:
                rendered.append((obj, Path(path).with_suffix('.html')))
        cls.rows = human_search.build_search_index(
            rendered,
            display_name,
            human_markdown.summary_of,
            lambda obj: human_route.human_object_type_label(obj, semantic_site.semantic_site_view_type),
        )

    def row(self, object_id: str) -> dict[str, str]:
        return next(row for row in self.rows if row['id'] == object_id)

    def test_representative_resources_are_indexed(self) -> None:
        for object_id in ('forgejo_actions', 'automated_build_deployment', 'yaml_1.2.2', 'apple'):
            with self.subTest(object_id=object_id):
                self.assertTrue(self.row(object_id)['url'].startswith('objects/'))

    def test_index_uses_human_type_labels(self) -> None:
        self.assertEqual(self.row('forgejo_actions')['type_label'], '实现')
        self.assertEqual(self.row('automated_build_deployment')['type_label'], '能力')
        self.assertEqual(self.row('yaml_1.2.2')['type_label'], '标准 / 规范')
        self.assertEqual(self.row('apple')['type_label'], '组织')

    def test_search_projection_contains_expected_human_terms(self) -> None:
        self.assertIn('Forgejo', self.row('forgejo_actions')['search_text'])
        self.assertIn('自动构建', self.row('automated_build_deployment')['search_text'])
        self.assertIn('YAML', self.row('yaml_1.2.2')['search_text'])
        self.assertIn('Apple', self.row('apple')['search_text'])

    def test_index_is_deterministically_sorted(self) -> None:
        keys = [(row['name'].casefold(), row['id']) for row in self.rows]
        self.assertEqual(keys, sorted(keys))


if __name__ == '__main__':
    unittest.main()
