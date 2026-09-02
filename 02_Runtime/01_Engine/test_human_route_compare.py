#!/usr/bin/env python3
"""Deterministic tests for the first dedicated Compare Human View (#105)."""

from __future__ import annotations

import unittest
from pathlib import Path

import human_route_compare as compare
from bootstrap_query import index_objects, load_atlas


ROOT = Path(__file__).resolve().parents[2]


class HumanRouteCompareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        objects, relations = load_atlas(ROOT)
        cls.index = index_objects(objects)
        cls.relations = relations
        cls.body = compare.build_compare_body(cls.index, cls.relations)

    def test_compare_uses_existing_canonical_candidates_and_context(self) -> None:
        self.assertIn('自动构建与部署', self.body)
        self.assertIn('Forgejo Actions', self.body)
        self.assertIn('GitHub Actions', self.body)
        self.assertIn('objects/forgejo_actions.html', self.body)
        self.assertIn('objects/github_actions.html', self.body)

    def test_compare_preserves_missing_semantics(self) -> None:
        self.assertIn('GPL-3.0-or-later', self.body)
        self.assertIn('当前记录未提供（not recorded）', self.body)
        self.assertNotIn('没有许可证', self.body)

    def test_compare_preserves_relation_boundary(self) -> None:
        self.assertIn('alternative_to', self.body)
        self.assertIn('compatible_with', self.body)
        self.assertIn('不追求完全兼容', self.body)
        self.assertNotIn('完全兼容</span>', self.body)

    def test_compare_does_not_create_ranking(self) -> None:
        self.assertIn('不输出 winner', self.body)
        self.assertNotIn('overall score（总分）：', self.body)
        self.assertNotIn('最佳选择', self.body)

    def test_capability_entry_is_bounded_to_representative_context(self) -> None:
        capability = self.index[compare.CONTEXT_ID]
        other = self.index['forgejo_actions']
        self.assertIn('比较 Forgejo Actions 与 GitHub Actions', compare.inject_compare_entry('<h2>一跳邻居</h2>', capability))
        self.assertEqual(compare.inject_compare_entry('<h2>一跳邻居</h2>', other), '<h2>一跳邻居</h2>')


if __name__ == '__main__':
    unittest.main()
