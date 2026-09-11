#!/usr/bin/env python3
"""Deterministic tests for dedicated Compare Human View and candidate discovery."""

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
        self.assertIn("自动构建与部署", self.body)
        self.assertIn("Forgejo Actions", self.body)
        self.assertIn("GitHub Actions", self.body)
        self.assertIn("objects/forgejo_actions.html", self.body)
        self.assertIn("objects/github_actions.html", self.body)

    def test_candidate_discovery_is_projected_from_capabilities(self) -> None:
        candidates = compare.capability_candidates(compare.CONTEXT_ID, self.index)
        candidate_ids = {str(candidate.get("id")) for candidate in candidates}
        self.assertIn("forgejo_actions", candidate_ids)
        self.assertIn("github_actions", candidate_ids)
        for candidate in candidates:
            self.assertIn(compare.CONTEXT_ID, candidate.get("capabilities") or [])

    def test_capability_entry_lists_candidates_before_bounded_compare(self) -> None:
        capability = self.index[compare.CONTEXT_ID]
        entry = compare.inject_compare_entry("<h2>一跳邻居</h2>", capability, self.index)
        self.assertIn("支持这个能力的实现", entry)
        self.assertIn("objects/forgejo_actions.html", entry)
        self.assertIn("objects/github_actions.html", entry)
        self.assertIn("比较 Forgejo Actions 与 GitHub Actions", entry)
        self.assertIn("只覆盖上述这一对候选", entry)

    def test_non_capability_without_candidates_gets_no_compare_entry(self) -> None:
        other = self.index["forgejo_actions"]
        original = "<h2>一跳邻居</h2>"
        self.assertEqual(compare.inject_compare_entry(original, other, self.index), original)

    def test_compare_preserves_missing_semantics(self) -> None:
        self.assertIn("GPL-3.0-or-later", self.body)
        self.assertIn("当前记录未提供（not recorded）", self.body)
        self.assertNotIn("没有许可证", self.body)

    def test_compare_preserves_relation_boundary(self) -> None:
        self.assertIn("alternative_to", self.body)
        self.assertIn("compatible_with", self.body)
        self.assertIn("不追求完全兼容", self.body)
        self.assertNotIn("两者完全兼容", self.body)
        self.assertNotIn("已建立 compatible_with", self.body)

    def test_compare_does_not_create_ranking(self) -> None:
        self.assertIn("不输出 winner", self.body)
        self.assertNotIn("overall score（总分）：", self.body)
        self.assertNotIn("最佳选择", self.body)


if __name__ == "__main__":
    unittest.main()
