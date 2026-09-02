#!/usr/bin/env python3
"""Deterministic tests for the first Human Evidence / Assessment presentation slice."""

from __future__ import annotations

import unittest

from render_markdown import add_evidence_and_assessment


class HumanEvidencePresentationTests(unittest.TestCase):
    def test_sources_and_ia_notes_are_presented_as_distinct_roles(self) -> None:
        lines: list[str] = []
        add_evidence_and_assessment(
            lines,
            {
                "notes_zh": ["这是 InteropAtlas 的边界说明。"],
                "sources": [
                    {
                        "title": "Official documentation",
                        "url": "https://example.com/official",
                    }
                ],
            },
            include_notes=True,
        )
        rendered = "\n".join(lines)
        self.assertIn("## InteropAtlas 说明与评估", rendered)
        self.assertIn("不等同于第三方权威来源", rendered)
        self.assertIn("这是 InteropAtlas 的边界说明。", rendered)
        self.assertIn("## 来源与依据", rendered)
        self.assertIn("[Official documentation](https://example.com/official)", rendered)
        self.assertLess(rendered.index("## InteropAtlas 说明与评估"), rendered.index("## 来源与依据"))

    def test_missing_sources_are_explicitly_not_recorded_not_false(self) -> None:
        lines: list[str] = []
        add_evidence_and_assessment(lines, {}, include_notes=False)
        rendered = "\n".join(lines)
        self.assertIn("## 来源与依据", rendered)
        self.assertIn("当前记录未提供来源 / Evidence 链接", rendered)
        self.assertIn("未记录", rendered)
        self.assertIn("不等于该事实为 false、none", rendered)

    def test_notes_section_is_not_invented_when_no_notes_exist(self) -> None:
        lines: list[str] = []
        add_evidence_and_assessment(
            lines,
            {"sources": [{"title": "Source", "url": "https://example.com/source"}]},
            include_notes=True,
        )
        rendered = "\n".join(lines)
        self.assertNotIn("## InteropAtlas 说明与评估", rendered)
        self.assertIn("## 来源与依据", rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
