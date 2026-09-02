#!/usr/bin/env python3
"""Gate B browser-level conformance baseline for the Human-readable Route.

This suite intentionally tests user-observable browser behavior rather than HTML
build success alone. It is a representative slice, not a complete WCAG audit.
"""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin, urlparse

from playwright.sync_api import Browser, Page, Playwright, expect, sync_playwright


BASE_URL = os.environ.get("IA_E2E_BASE_URL", "http://127.0.0.1:8000/").rstrip("/") + "/"


def page_url(object_id: str) -> str:
    return urljoin(BASE_URL, f"objects/{object_id}.html")


class HumanRouteBrowserTests(unittest.TestCase):
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

    def new_page(self, **context_options) -> tuple[object, Page]:
        context = self.browser.new_context(**context_options)
        return context, context.new_page()

    def visible_neighbor_ids(self, page: Page) -> set[str]:
        return set(
            page.locator('.map-node[data-neighbor-id]:visible').evaluate_all(
                "nodes => nodes.map(node => node.dataset.neighborId)"
            )
        )

    def test_semantic_shell_is_consistent_across_representative_pages(self) -> None:
        context, page = self.new_page()
        try:
            for object_id in (
                "automated_build_deployment",
                "yaml_1.2.2",
                "forgejo_actions",
            ):
                with self.subTest(object_id=object_id):
                    response = page.goto(page_url(object_id))
                    self.assertIsNotNone(response)
                    self.assertTrue(response.ok)
                    self.assertEqual(page.locator("main").count(), 1)
                    self.assertEqual(page.locator("h1").count(), 1)
                    self.assertEqual(page.locator('nav[aria-label="主导航"]').count(), 1)
                    self.assertEqual(page.locator('nav[aria-label="面包屑"]').count(), 1)
                    self.assertEqual(page.locator('[aria-current="page"]').count(), 1)
        finally:
            context.close()

    def test_stable_link_navigation_back_and_forward(self) -> None:
        context, page = self.new_page()
        try:
            origin = page_url("forgejo_actions")
            page.goto(origin)
            link = page.locator(".local-map .map-node-name a").first
            expect(link).to_be_visible()
            target = link.get_attribute("href")
            self.assertTrue(target)

            link.click()
            self.assertNotEqual(page.url, origin)
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(origin, target)).path)

            page.go_back()
            self.assertEqual(page.url, origin)
            page.go_forward()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(origin, target)).path)
        finally:
            context.close()

    def test_local_map_recenter_updates_map_without_page_navigation(self) -> None:
        context, page = self.new_page()
        try:
            origin = page_url("forgejo_actions")
            page.goto(origin)
            section = page.locator(".local-map")
            expect(section).to_be_visible()
            before_center = section.get_attribute("data-center-id")

            button = page.locator(".map-recenter").first
            expect(button).to_be_visible()
            target_href = button.get_attribute("data-map-href")
            self.assertTrue(target_href)
            expected_center = urlparse(urljoin(origin, target_href)).path.rsplit("/", 1)[-1].removesuffix(".html")

            button.click()
            expect(page.locator(".local-map")).to_have_attribute("data-center-id", expected_center)
            self.assertEqual(page.url, origin)
            self.assertNotEqual(before_center, expected_center)
        finally:
            context.close()

    def test_local_map_loading_state_is_observable(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            page.evaluate(
                """() => {
                  window.fetch = () => new Promise(() => {});
                  recenterLocalMap(document.querySelector('.map-recenter'));
                }"""
            )
            expect(page.locator(".local-map")).to_have_class("local-map map-loading")
            expect(page.locator(".map-recenter").first).to_have_text("载入中…")
        finally:
            context.close()

    def test_current_recenter_failure_preserves_resource_link(self) -> None:
        """Lock the current failure behavior as evidence, while flagging its UI debt.

        The current implementation exposes failure through a disabled button title.
        That keeps a resource link available, but #80 still requires a more directly
        perceivable failure message before Gate B can pass.
        """

        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            page.evaluate(
                """() => {
                  window.fetch = () => Promise.reject(new Error('forced E2E failure'));
                  recenterLocalMap(document.querySelector('.map-recenter'));
                }"""
            )
            button = page.locator(".map-recenter").first
            expect(button).to_be_disabled()
            expect(button).to_have_attribute("title", "局部地图载入失败；对象详情仍可通过标题链接打开")
            expect(page.locator(".local-map .map-node-name a").first).to_be_visible()
        finally:
            context.close()

    def test_relation_and_field_filters_change_visible_map_and_stats(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            current_stats = page.locator(".map-stats-current")
            before_stats = current_stats.inner_text()
            before_neighbors = self.visible_neighbor_ids(page)

            relation_filter = page.locator('.map-filter[data-filter-kind="origin"][data-filter-value="relation"]')
            field_filter = page.locator('.map-filter[data-filter-kind="origin"][data-filter-value="field"]')
            expect(relation_filter).to_be_visible()
            expect(field_filter).to_be_visible()

            relation_filter.click()
            expect(relation_filter).to_have_attribute("aria-pressed", "true")
            relation_stats = current_stats.inner_text()
            relation_neighbors = self.visible_neighbor_ids(page)

            field_filter.click()
            expect(field_filter).to_have_attribute("aria-pressed", "true")
            field_stats = current_stats.inner_text()
            field_neighbors = self.visible_neighbor_ids(page)

            self.assertNotEqual(before_stats, relation_stats)
            self.assertNotEqual(before_stats, field_stats)
            self.assertNotEqual(before_neighbors, relation_neighbors)
            self.assertNotEqual(before_neighbors, field_neighbors)
            self.assertNotEqual(relation_neighbors, field_neighbors)
        finally:
            context.close()

    def test_theme_toggle_changes_explicit_theme_state(self) -> None:
        context, page = self.new_page(color_scheme="light")
        try:
            page.goto(page_url("forgejo_actions"))
            button = page.locator("#theme-toggle")
            expect(button).to_be_visible()
            button.click()
            self.assertEqual(page.locator("html").get_attribute("data-theme"), "dark")
            expect(button).to_have_attribute("aria-label", "切换亮色或深色模式")
        finally:
            context.close()

    def test_keyboard_focus_is_visible_on_core_controls(self) -> None:
        context, page = self.new_page()
        try:
            page.goto(page_url("forgejo_actions"))
            button = page.locator(".map-recenter").first
            button.focus()
            style = button.evaluate(
                """element => {
                  const s = getComputedStyle(element);
                  return {outlineStyle:s.outlineStyle, outlineWidth:s.outlineWidth, boxShadow:s.boxShadow};
                }"""
            )
            has_outline = style["outlineStyle"] != "none" and style["outlineWidth"] != "0px"
            has_shadow = style["boxShadow"] != "none"
            self.assertTrue(has_outline or has_shadow, style)

            # Enter is the keyboard activation contract for the native button.
            page.evaluate("() => { window.fetch = () => new Promise(() => {}); }")
            button.press("Enter")
            expect(button).to_have_text("载入中…")
        finally:
            context.close()

    def test_javascript_disabled_keeps_resource_reading_and_navigation(self) -> None:
        context, page = self.new_page(java_script_enabled=False)
        try:
            origin = page_url("forgejo_actions")
            response = page.goto(origin)
            self.assertTrue(response and response.ok)
            expect(page.locator("main h1")).to_be_visible()
            link = page.locator(".local-map .map-node-name a").first
            expect(link).to_be_visible()
            target = link.get_attribute("href")
            link.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(origin, target)).path)
        finally:
            context.close()

    def test_narrow_viewport_has_no_document_level_horizontal_overflow(self) -> None:
        context, page = self.new_page(viewport={"width": 375, "height": 812})
        try:
            for object_id in ("automated_build_deployment", "forgejo_actions", "yaml_1.2.2"):
                with self.subTest(object_id=object_id):
                    page.goto(page_url(object_id))
                    metrics = page.evaluate(
                        """() => ({scrollWidth:document.documentElement.scrollWidth, clientWidth:document.documentElement.clientWidth})"""
                    )
                    self.assertLessEqual(metrics["scrollWidth"], metrics["clientWidth"] + 1, metrics)
        finally:
            context.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
