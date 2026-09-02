#!/usr/bin/env python3
"""Regression tests for permanent Human Route shell / breadcrumb boundary (#107)."""

from __future__ import annotations

import unittest

import human_route_shell as shell


class FakeSite:
    STYLE = "body{color:black}"
    THEME_SCRIPT = "<script>theme()</script>"
    MAP_SCRIPT = "<script>map()</script>"


class HumanRouteShellTests(unittest.TestCase):
    def test_page_shell_owns_stable_document_semantics(self) -> None:
        page = shell.page_shell(FakeSite, "测试", "<h1>正文</h1>", "../", '<span aria-current="page">测试</span>')
        self.assertIn('<html lang="zh-CN">', page)
        self.assertIn('<nav class="site-nav" aria-label="主导航">', page)
        self.assertIn('href="../index.html"', page)
        self.assertIn('<nav class="breadcrumb" aria-label="面包屑">', page)
        self.assertIn('<main><h1>正文</h1></main>', page)
        self.assertIn(FakeSite.STYLE, page)
        self.assertIn(FakeSite.THEME_SCRIPT, page)
        self.assertIn(FakeSite.MAP_SCRIPT, page)

    def test_capability_breadcrumb_is_a_view_with_category_link(self) -> None:
        obj = {"id": "cap", "name_zh": "能力 A", "category": "exchange"}
        breadcrumb = shell.breadcrumb_for(
            obj,
            "../",
            display_name=lambda record, fallback: record.get("name_zh", fallback),
            view_type_resolver=lambda _: "capability",
            human_value=lambda value: {"exchange": "交换"}.get(str(value), str(value)),
            category_anchor=lambda category: f"category-{category}",
        )
        self.assertIn('href="../index.html"', breadcrumb)
        self.assertIn('href="../index.html#category-exchange"', breadcrumb)
        self.assertIn('<span>能力</span>', breadcrumb)
        self.assertIn('aria-current="page">能力 A</span>', breadcrumb)

    def test_non_capability_breadcrumb_uses_human_view_label(self) -> None:
        obj = {"id": "org", "name_zh": "组织 A"}
        breadcrumb = shell.breadcrumb_for(
            obj,
            "../",
            display_name=lambda record, fallback: record.get("name_zh", fallback),
            view_type_resolver=lambda _: "organization",
            human_value=str,
            category_anchor=lambda category: category,
        )
        self.assertIn('<span>组织</span>', breadcrumb)
        self.assertNotIn('agent', breadcrumb)


if __name__ == "__main__":
    unittest.main()
