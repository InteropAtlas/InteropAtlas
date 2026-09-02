#!/usr/bin/env python3
"""Representative Gate B human-task walkthrough evidence (#96)."""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin, urlparse

from playwright.sync_api import Browser, Playwright, expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"


def page_url(object_id: str) -> str:
    return urljoin(BASE_URL, f"objects/{object_id}.html")


class RepresentativeHumanTaskWalkthrough(unittest.TestCase):
    playwright: Playwright
    browser: Browser

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def new_page(self):
        context = self.browser.new_context()
        return context, context.new_page()

    def test_identify_and_find_implementations_from_capability(self) -> None:
        context, page = self.new_page()
        try:
            response = page.goto(page_url("automated_build_deployment"))
            self.assertTrue(response and response.ok)
            expect(page.locator("main h1")).to_contain_text("自动构建与部署")

            heading = page.get_by_role("heading", name="哪些实现提供这个能力？")
            expect(heading).to_be_visible()
            forgejo = page.get_by_role("link", name="Forgejo Actions").first
            github = page.get_by_role("link", name="GitHub Actions").first
            expect(forgejo).to_be_visible()
            expect(github).to_be_visible()

            forgejo.click()
            self.assertEqual(urlparse(page.url).path, urlparse(page_url("forgejo_actions")).path)
            expect(page.locator("main h1")).to_contain_text("Forgejo Actions")
        finally:
            context.close()

    def test_follow_meaningful_relation_and_return(self) -> None:
        context, page = self.new_page()
        try:
            origin = page_url("forgejo_actions")
            page.goto(origin)
            relation_heading = page.get_by_role("heading", name="替代与兼容")
            expect(relation_heading.first).to_be_visible()
            github = page.get_by_role("link", name="GitHub Actions").first
            expect(github).to_be_visible()
            github.click()
            self.assertEqual(urlparse(page.url).path, urlparse(page_url("github_actions")).path)
            page.go_back()
            self.assertEqual(page.url, origin)
        finally:
            context.close()

    def test_verify_source_from_implementation_page(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            sources = page.get_by_role("heading", name="来源")
            expect(sources).to_be_visible()
            official = page.get_by_role("link", name="Forgejo Actions and GitHub Actions")
            expect(official).to_be_visible()
            href = official.get_attribute("href")
            self.assertTrue(href and href.startswith("https://forgejo.org/"), href)
        finally:
            context.close()

    def test_local_map_success_path_remains_in_walkthrough_slice(self) -> None:
        context, page = self.new_page()
        try:
            origin = page_url("forgejo_actions")
            page.goto(origin)
            button = page.locator(".map-recenter").first
            expect(button).to_be_visible()
            before = page.locator(".local-map").get_attribute("data-center-id")
            button.click()
            section = page.locator(".local-map")
            expect(section.locator(".map-status")).to_have_text("地图中心已更新。")
            after = section.get_attribute("data-center-id")
            self.assertNotEqual(before, after)
            self.assertEqual(page.url, origin)
        finally:
            context.close()

    def test_local_map_failure_keeps_primary_detail_navigation(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            button = page.locator(".map-recenter").first
            page.evaluate(
                """() => {
                  window.fetch = () => Promise.reject(new Error('walkthrough forced failure'));
                  recenterLocalMap(document.querySelector('.map-recenter'));
                }"""
            )
            expect(page.locator(".local-map .map-status")).to_have_text(
                "局部地图载入失败；可以重试，或通过对象标题链接打开详情。"
            )
            expect(button).to_be_enabled()
            expect(page.locator(".local-map .map-node-name a").first).to_be_visible()
        finally:
            context.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
