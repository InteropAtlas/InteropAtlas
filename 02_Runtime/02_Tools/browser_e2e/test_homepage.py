#!/usr/bin/env python3
"""Browser contract for the provisional search + Atlas status Homepage."""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin, urlparse

from playwright.sync_api import expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"


class HomepageStatusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def test_homepage_has_one_primary_action_and_atlas_status(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            response = page.goto(BASE_URL)
            self.assertTrue(response and response.ok)
            main = page.locator("main")
            expect(main.get_by_role("heading", name="搜索 InteropAtlas", exact=True)).to_be_visible()
            expect(main.get_by_role("link", name="开始搜索", exact=True)).to_have_attribute("href", "search.html")
            expect(main.get_by_role("heading", name="当前地图状态", exact=True)).to_be_visible()
            expect(main).to_contain_text("已收录对象")
            expect(main).to_contain_text("已记录关系")
            expect(main).to_contain_text("当前可阅读页面")
        finally:
            context.close()

    def test_homepage_removes_previous_competing_entry_stack(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(BASE_URL)
            main = page.locator("main")
            for label in ("你想做什么？", "查找对象", "理解一个对象", "比较候选方案", "验证来源", "探索关系", "按能力浏览", "其他入口"):
                expect(main).not_to_contain_text(label)
            self.assertEqual(main.locator("a").count(), 1)
        finally:
            context.close()

    def test_homepage_search_works_without_javascript(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            page.goto(BASE_URL)
            link = page.get_by_role("link", name="开始搜索", exact=True)
            expect(link).to_be_visible()
            target = link.get_attribute("href")
            link.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(BASE_URL, target)).path)
        finally:
            context.close()

    def test_homepage_reflows_without_document_overflow(self) -> None:
        context = self.browser.new_context(viewport={"width": 375, "height": 812})
        page = context.new_page()
        try:
            page.goto(BASE_URL)
            metrics = page.evaluate(
                "() => ({scrollWidth:document.documentElement.scrollWidth, clientWidth:document.documentElement.clientWidth})"
            )
            self.assertLessEqual(metrics["scrollWidth"], metrics["clientWidth"] + 1, metrics)
        finally:
            context.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
