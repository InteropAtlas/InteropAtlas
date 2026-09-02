#!/usr/bin/env python3
"""Gate B representative Resource Page contract across four identity families."""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin

from playwright.sync_api import expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"


def page_url(object_id: str) -> str:
    return urljoin(BASE_URL, f"objects/{object_id}.html")


class RepresentativeResourcePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def test_four_core_identity_families_have_stable_human_resources(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            representatives = {
                "automated_build_deployment": "自动构建与部署",
                "yaml_1.2.2": "YAML",
                "forgejo_actions": "Forgejo Actions",
                "apple": "苹果公司",
            }
            for object_id, title_fragment in representatives.items():
                with self.subTest(object_id=object_id):
                    response = page.goto(page_url(object_id))
                    self.assertTrue(response and response.ok)
                    self.assertEqual(page.url, page_url(object_id))
                    expect(page.locator("main h1")).to_contain_text(title_fragment)
                    self.assertEqual(page.locator("main").count(), 1)
                    self.assertEqual(page.locator('nav[aria-label="面包屑"] [aria-current="page"]').count(), 1)
                    expect(page.locator("main")).to_contain_text("基本信息")
        finally:
            context.close()

    def test_organization_page_has_identity_context_key_facts_and_source(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(page_url("apple"))
            main = page.locator("main")
            expect(main).to_contain_text("Apple Inc. 是 InteropAtlas 当前记录的company组织对象")
            expect(main).to_contain_text("对象类型： 组织（Organization）")
            expect(main).to_contain_text("官方名称： Apple Inc.")
            expect(main).to_contain_text("组织类别： company")
            expect(main).to_contain_text("活动范围 / 管辖： global")
            expect(main.locator('a[href="https://developer.apple.com/design/human-interface-guidelines/"]')).to_be_visible()
            expect(page.locator('nav[aria-label="面包屑"]')).to_contain_text("组织")
        finally:
            context.close()

    def test_representative_pages_expose_profile_specific_key_facts(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            cases = (
                ("automated_build_deployment", "能力类别"),
                ("yaml_1.2.2", "标准类别"),
                ("forgejo_actions", "实现类别"),
                ("apple", "组织类别"),
            )
            for object_id, key_fact in cases:
                with self.subTest(object_id=object_id):
                    page.goto(page_url(object_id))
                    expect(page.locator("main")).to_contain_text(key_fact)
                    expect(page.locator("main")).to_contain_text("本页由 InteropAtlas 结构化数据自动生成")
        finally:
            context.close()

    def test_local_map_center_uses_human_semantic_type_labels(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            cases = (
                ("automated_build_deployment", "当前地图中心 · 能力", "concept"),
                ("yaml_1.2.2", "当前地图中心 · 标准 / 规范", "artifact"),
                ("forgejo_actions", "当前地图中心 · 实现", "system"),
                ("apple", "当前地图中心 · 组织", "agent"),
            )
            for object_id, expected, raw_type in cases:
                with self.subTest(object_id=object_id):
                    page.goto(page_url(object_id))
                    center = page.locator(".local-map .map-center .map-edge")
                    expect(center).to_have_text(expected)
                    self.assertNotEqual(center.inner_text(), f"当前地图中心 · {raw_type}")
        finally:
            context.close()

    def test_implementation_separates_ia_notes_from_canonical_sources(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            main = page.locator("main")
            expect(main).to_contain_text("InteropAtlas 说明与评估")
            expect(main).to_contain_text("不等同于第三方权威来源")
            expect(main).to_contain_text("来源与依据")
            expect(main).to_contain_text("Renderer 不维护第二份来源事实")
            expect(main.locator('a[href="https://forgejo.org/docs/latest/user/actions/github-actions/"]')).to_be_visible()
            headings = main.locator("h2").all_inner_texts()
            self.assertLess(headings.index("InteropAtlas 说明与评估"), headings.index("来源与依据"))
        finally:
            context.close()

    def test_standard_has_source_section_without_invented_assessment(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            page.goto(page_url("yaml_1.2.2"))
            main = page.locator("main")
            expect(main).to_contain_text("来源与依据")
            expect(main.locator('a[href="https://yaml.org/spec/1.2.2/"]')).to_be_visible()
            self.assertEqual(main.get_by_role("heading", name="InteropAtlas 说明与评估", exact=True).count(), 0)
        finally:
            context.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
