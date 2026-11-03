#!/usr/bin/env python3
"""Browser evidence for the first task-oriented Search slice (#103)."""

from __future__ import annotations

import os
import unittest
from urllib.parse import parse_qs, urljoin, urlparse

from playwright.sync_api import expect, sync_playwright


BASE_URL = os.environ.get('IA_E2E_BASE_URL', 'http://127.0.0.1:8000/').rstrip('/') + '/'


class HumanRouteSearchBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()

    def test_homepage_exposes_search_entry(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(urljoin(BASE_URL, 'index.html'))
            link = page.get_by_role('link', name='开始搜索')
            expect(link).to_be_visible()
            link.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(BASE_URL, 'search.html')).path)
            expect(page.locator('main h1')).to_have_text('搜索 InteropAtlas')
        finally:
            context.close()

    def test_query_url_result_navigation_and_back(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(urljoin(BASE_URL, 'search.html'))
            search = page.get_by_role('searchbox', name='搜索词')
            search.fill('Forgejo')
            search.press('Enter')
            self.assertEqual(parse_qs(urlparse(page.url).query).get('q'), ['Forgejo'])
            expect(page.locator('#atlas-search-status')).to_contain_text('找到')
            result = page.get_by_role('link', name='Forgejo Actions')
            expect(result).to_be_visible()
            result.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(BASE_URL, 'objects/forgejo_actions.html')).path)
            page.go_back()
            self.assertEqual(parse_qs(urlparse(page.url).query).get('q'), ['Forgejo'])
            expect(page.get_by_role('link', name='Forgejo Actions')).to_be_visible()
        finally:
            context.close()

    def test_representative_queries_find_expected_resources(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            cases = (
                ('自动构建', '自动构建与部署'),
                ('YAML', 'YAML'),
                ('Apple', '苹果公司'),
            )
            for query, expected in cases:
                with self.subTest(query=query):
                    page.goto(urljoin(BASE_URL, 'search.html') + '?q=' + query)
                    expect(page.get_by_role('link', name=expected).first).to_be_visible()
        finally:
            context.close()

    def test_search_reflows_on_narrow_viewport(self) -> None:
        context = self.browser.new_context(viewport={'width': 375, 'height': 812})
        page = context.new_page()
        try:
            page.goto(urljoin(BASE_URL, 'search.html?q=Forgejo'))
            metrics = page.evaluate('() => ({scrollWidth:document.documentElement.scrollWidth, clientWidth:document.documentElement.clientWidth})')
            self.assertLessEqual(metrics['scrollWidth'], metrics['clientWidth'] + 1, metrics)
        finally:
            context.close()

    def test_failed_index_remains_distinct_from_no_matches_after_submit_and_history(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.route('**/search-index.json', lambda route: route.fulfill(status=503, body='Unavailable'))
            page.goto(urljoin(BASE_URL, 'search.html?q=Forgejo'))
            search = page.get_by_role('searchbox', name='搜索词')
            status = page.locator('#atlas-search-status')
            expect(search).to_have_value('Forgejo')
            expect(status).to_contain_text('搜索索引载入失败')

            for query in ('YAML', ''):
                search.fill(query)
                search.press('Enter')
                self.assertEqual(parse_qs(urlparse(page.url).query).get('q', ['']), [query])
                expect(status).to_contain_text('搜索索引载入失败')
                expect(page.locator('.search-result')).to_have_count(0)

            for navigate, query in ((page.go_back, 'YAML'), (page.go_back, 'Forgejo'), (page.go_forward, 'YAML')):
                navigate()
                expect(search).to_have_value(query)
                expect(status).to_contain_text('搜索索引载入失败')
                expect(page.locator('.search-result')).to_have_count(0)

            home = page.get_by_role('link', name='InteropAtlas').first
            home.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(BASE_URL, 'index.html')).path)
        finally:
            context.close()

    def test_pending_index_preserves_query_and_searches_latest_submission_when_loaded(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.add_init_script("""
                const realFetch = window.fetch.bind(window);
                window.fetch = (...args) => {
                    if (args[0] !== 'search-index.json') return realFetch(...args);
                    return new Promise((resolve, reject) => {
                        window.__iaLoadSearchIndex = () => realFetch(...args).then(resolve, reject);
                    });
                };
            """)
            page.goto(urljoin(BASE_URL, 'search.html?q=Forgejo'))
            search = page.get_by_role('searchbox', name='搜索词')
            status = page.locator('#atlas-search-status')
            expect(search).to_have_value('Forgejo')
            expect(status).to_have_text('正在载入搜索索引…')

            search.fill('YAML')
            search.press('Enter')
            expect(status).to_have_text('正在载入搜索索引…')
            expect(page.locator('.search-result')).to_have_count(0)
            self.assertEqual(parse_qs(urlparse(page.url).query).get('q'), ['YAML'])

            page.evaluate('() => window.__iaLoadSearchIndex()')
            expect(page.locator('.search-result a[href="objects/yaml_1.2.2.html"]')).to_be_visible()
            expect(search).to_have_value('YAML')
            expect(status).to_contain_text('找到')
        finally:
            context.close()

    def test_loaded_index_distinguishes_empty_query_no_matches_and_hits(self) -> None:
        context = self.browser.new_context()
        page = context.new_page()
        try:
            page.goto(urljoin(BASE_URL, 'search.html'))
            search = page.get_by_role('searchbox', name='搜索词')
            status = page.locator('#atlas-search-status')
            expect(status).to_have_text('输入名称、关键词或稳定 ID 开始搜索。')
            expect(page.locator('.search-result')).to_have_count(0)

            search.fill('interopatlas-no-such-object-915c8a6f')
            search.press('Enter')
            expect(status).to_have_text('没有找到结果。')
            expect(page.locator('.search-result')).to_have_count(0)

            search.fill('Forgejo')
            search.press('Enter')
            expect(page.get_by_role('link', name='Forgejo Actions')).to_be_visible()
            expect(status).to_contain_text('找到')

            search.fill('')
            search.press('Enter')
            expect(status).to_have_text('输入名称、关键词或稳定 ID 开始搜索。')
            expect(page.locator('.search-result')).to_have_count(0)
        finally:
            context.close()

    def test_js_disabled_keeps_search_explanation_and_home_navigation(self) -> None:
        context = self.browser.new_context(java_script_enabled=False)
        page = context.new_page()
        try:
            response = page.goto(urljoin(BASE_URL, 'search.html?q=Forgejo'))
            self.assertTrue(response and response.ok)
            expect(page.locator('main h1')).to_have_text('搜索 InteropAtlas')
            expect(page.locator('.search-progressive-note')).to_contain_text(
                '对象页、首页入口和稳定链接不依赖 Search'
            )
            home = page.get_by_role('link', name='InteropAtlas').first
            expect(home).to_be_visible()
            home.click()
            self.assertEqual(urlparse(page.url).path, urlparse(urljoin(BASE_URL, 'index.html')).path)
        finally:
            context.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
