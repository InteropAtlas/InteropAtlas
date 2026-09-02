#!/usr/bin/env python3
"""Browser contract for the first task-oriented Homepage entry slice."""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin, urlparse

from playwright.sync_api import expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"


class HomepageTaskEntryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def test_homepage_exposes_real_task_entries_and_boundaries(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            response = page.goto(BASE_URL)
            self.assertTrue(response and response.ok)
            main = page.locator("main")
            expect(main.get_by_role("heading", name="你想做什么？", exact=True)).to_be_visible()
            expected = {
                "查找对象": "search.html",
                "理解一个对象": "objects/automated_build_deployment.html",
                "比较候选方案": "compare/automated_build_deployment--forgejo_actions--github_actions.html",
                "验证来源": "objects/forgejo_actions.html#evidence",
                "探索关系": "objects/forgejo_actions.html#local-map",
            }
            for label, href in expected.items():
                with self.subTest(label=label):
                    expect(main.get_by_role("link", name=label, exact=True)).to_have_attribute("href", href)
            expect(main).to_contain_text("尚不是全站任意对象比较")
            expect(main).to_contain_text("尚不是大型 Graph Explorer")
            expect(main.get_by_role("heading", name="按能力浏览", exact=True)).to_be_visible()
        finally:
            context.close()

    def test_homepage_verify_and_explore_land_on_real_fragments_without_javascript(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            page.goto(BASE_URL)
            verify = page.get_by_role("link", name="验证来源", exact=True)
            expect(verify).to_be_visible()
            verify.click()
            self.assertEqual(urlparse(page.url).fragment, "evidence")
            expect(page.locator("#evidence")).to_be_visible()
            expect(page.locator("#evidence")).to_have_text("来源与依据")

            page.goto(BASE_URL)
            explore = page.get_by_role("link", name="探索关系", exact=True)
            expect(explore).to_be_visible()
            explore.click()
            self.assertEqual(urlparse(page.url).fragment, "local-map")
            expect(page.locator("#local-map.local-map")).to_be_visible()
        finally:
            context.close()

    def test_homepage_task_entries_work_without_javascript(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            page.goto(BASE_URL)
            link = page.get_by_role("link", name="查找对象", exact=True)
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
