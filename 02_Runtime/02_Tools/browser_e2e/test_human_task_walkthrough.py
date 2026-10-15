#!/usr/bin/env python3
"""Representative Gate B human-task walkthrough evidence (#96)."""

from __future__ import annotations

import os
import unittest
from pathlib import Path
from urllib.parse import urljoin, urlparse

import yaml
from playwright.sync_api import Browser, Playwright, expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"
REPO_ROOT = Path(__file__).resolve().parents[3]


def page_url(object_id: str) -> str:
    return urljoin(BASE_URL, f"objects/{object_id}.html")


def media_record(object_id: str) -> dict:
    path = REPO_ROOT / "01_State" / "01_Objects" / f"{object_id}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


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
            forgejo = page.get_by_role("link", name="Forgejo Actions", exact=True).first
            github = page.get_by_role("link", name="GitHub Actions", exact=True).first
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
            github = page.get_by_role("link", name="GitHub Actions", exact=True).first
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

    def test_find_subtitle_formats_and_verify_recorded_version_scope_and_sources(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(urljoin(BASE_URL, "search.html"))
            search = page.get_by_role("searchbox", name="搜索词")
            search.fill("字幕")
            page.get_by_role("button", name="搜索", exact=True).click()
            search_url = page.url
            for object_id in ("w3c_imsc", "ebu_tt_d"):
                record = media_record(object_id)
                candidate = page.locator(f'.search-result a[href="objects/{object_id}.html"]')
                expect(candidate).to_be_visible()
                candidate.click()
                self.assertEqual(page.url, page_url(object_id))
                expect(page.locator("main li").filter(has_text="记录版次：")).to_contain_text(record["version"])
                expect(page.get_by_role("heading", name="范围与边界", exact=True)).to_be_visible()
                expect(page.get_by_text(record["scope_notes_zh"], exact=True)).to_be_visible()
                for source in record["sources"]:
                    expect(page.locator(f'main a[href="{source["url"]}"]').first).to_be_visible()
                if record.get("versions"):
                    expect(page.get_by_role("heading", name="版本", exact=True)).to_be_visible()
                page.go_back()
                self.assertEqual(page.url, search_url)
                expect(search).to_have_value("字幕")
        finally:
            context.close()

    def test_media_scope_and_version_remain_available_without_javascript(self) -> None:
        context = self.browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
        page = context.new_page()
        try:
            for object_id in ("w3c_imsc", "ebu_tt_d"):
                record = media_record(object_id)
                response = page.goto(page_url(object_id))
                self.assertTrue(response and response.ok)
                expect(page.locator("main li").filter(has_text="记录版次：")).to_contain_text(record["version"])
                expect(page.get_by_text(record["scope_notes_zh"], exact=True)).to_be_visible()
                expect(page.locator(f'main a[href="{record["sources"][0]["url"]}"]').first).to_be_visible()
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
