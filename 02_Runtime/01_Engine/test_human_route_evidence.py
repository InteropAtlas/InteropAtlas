#!/usr/bin/env python3
"""Deterministic tests for Human Evidence / Assessment presentation."""

from __future__ import annotations

import unittest

from human_route_evidence import inject_evidence_workspace
from render_markdown import add_evidence_and_assessment


class HumanEvidencePresentationTests(unittest.TestCase):
    def test_sources_and_ia_notes_are_presented_as_distinct_roles(self) -> None:
        lines: list[str] = []
        add_evidence_and_assessment(
            lines,
            {
                "notes_zh": ["这是 InteropAtlas 的边界说明。"],
                "sources": [{"title": "Official documentation", "url": "https://example.com/official"}],
            },
            include_notes=True,
        )
        rendered = "\n".join(lines)
        self.assertIn("## InteropAtlas 说明与评估", rendered)
        self.assertIn("不等同于第三方权威来源", rendered)
        self.assertIn("## 来源与依据", rendered)
        self.assertLess(rendered.index("## InteropAtlas 说明与评估"), rendered.index("## 来源与依据"))

    def test_missing_sources_are_explicitly_not_recorded_not_false(self) -> None:
        lines: list[str] = []
        add_evidence_and_assessment(lines, {}, include_notes=False)
        rendered = "\n".join(lines)
        self.assertIn("当前记录未提供来源 / Evidence 链接", rendered)
        self.assertIn("不等于该事实为 false、none", rendered)

    def test_workspace_projection_is_injected_without_replacing_source_facts(self) -> None:
        content = '<h2 id="evidence">来源与依据</h2><ul><li>existing source list</li></ul>'
        obj = {
            "id": "alpha",
            "sources": [{"title": "Official source", "url": "https://example.test/source"}],
            "notes_zh": ["IA assessment"],
        }
        rendered = inject_evidence_workspace(content, obj)
        self.assertIn("Evidence Projection 读取到 1 条 Canonical sources", rendered)
        self.assertIn("不是第三方权威来源", rendered)
        self.assertIn("Projection 只读，不构成 Canonical 写入", rendered)
        self.assertIn("existing source list", rendered)

    def test_workspace_missing_evidence_is_not_recorded_not_negative_claim(self) -> None:
        content = '<h2 id="evidence">来源与依据</h2>'
        rendered = inject_evidence_workspace(content, {"id": "beta"})
        self.assertIn("not_recorded", rendered)
        self.assertIn("不表示现实中不存在依据", rendered)

    def test_workspace_does_not_invent_section_where_resource_has_none(self) -> None:
        content = "<h2>基本信息</h2>"
        self.assertEqual(inject_evidence_workspace(content, {"id": "gamma"}), content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
