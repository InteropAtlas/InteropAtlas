#!/usr/bin/env python3
"""Browser evidence for the first dedicated Compare UI slice (#105)."""

from __future__ import annotations

import os
import unittest
from urllib.parse import urljoin, urlparse

from playwright.sync_api import expect, sync_playwright


BASE_URL = os.environ.get('IA_E2E_BASE_URL', 'http://127.0.0.1:8000/').rstrip('/') + '/'
COMPARE_URL = urljoin(
    BASE_URL,
    'compare/automated_build_deployment--forgejo_actions--github_actions.html',
)


class DedicatedCompareBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def test_capability_to_compare_candidate_and_back(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            capability_url = urljoin(BASE_URL, 'objects/automated_build_deployment.html')
            page.goto(capability_url)
            link = page.get_by_role('link', name='比较 Forgejo Actions 与 GitHub Actions')
            expect(link).to_be_visible()
            link.click()
            self.assertEqual(urlparse(page.url).path, urlparse(COMPARE_URL).path)
            expect(page.locator('main h1')).to_have_text('比较 Forgejo Actions 与 GitHub Actions')
            expect(page.locator('main')).to_contain_text('比较上下文')
            forgejo = page.get_by_role('link', name='Forgejo Actions').first
            expect(forgejo).to_be_visible()
            forgejo.click()
            self.assertEqual(
                urlparse(page.url).path,
                urlparse(urljoin(BASE_URL, 'objects/forgejo_actions.html')).path,
            )
            page.go_back()
            self.assertEqual(urlparse(page.url).path, urlparse(COMPARE_URL).path)
        finally:
            context.close()

    def test_compare_exposes_missing_and_semantic_boundaries(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(COMPARE_URL)
            main = page.locator('main')
            expect(main).to_contain_text('当前记录未提供（not recorded）')
            expect(main).to_contain_text('alternative_to')
            expect(main).to_contain_text('不追求完全兼容')
            expect(main).to_contain_text('不输出 winner（胜者）、overall score（总分）或推荐结论')
        finally:
            context.close()

    def test_compare_reflows_on_narrow_viewport(self) -> None:
        context = self.browser.new_context(viewport={'width': 375, 'height': 812})
        page = context.new_page()
        try:
            page.goto(COMPARE_URL)
            metrics = page.evaluate(
                '() => ({scrollWidth:document.documentElement.scrollWidth, clientWidth:document.documentElement.clientWidth})'
            )
            self.assertLessEqual(metrics['scrollWidth'], metrics['clientWidth'] + 1, metrics)
            expect(page.get_by_role('link', name='Forgejo Actions').first).to_be_visible()
            expect(page.get_by_role('link', name='GitHub Actions').first).to_be_visible()
        finally:
            context.close()

    def test_compare_is_readable_without_javascript(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            response = page.goto(COMPARE_URL)
            self.assertTrue(response and response.ok)
            expect(page.locator('main h1')).to_be_visible()
            expect(page.get_by_role('link', name='Forgejo Actions').first).to_be_visible()
            expect(page.locator('main')).to_contain_text('许可证表达')
        finally:
            context.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
