#!/usr/bin/env python3
"""Browser checks for the read-only maintenance view; no live API dependency."""
from __future__ import annotations
import os
from pathlib import Path
import sys
import unittest
from urllib.parse import urljoin
from playwright.sync_api import expect, sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / '01_Engine'))
from maintenance_dashboard import render

BASE_URL = os.environ.get('IA_E2E_BASE_URL', 'http://127.0.0.1:8000/').rstrip('/') + '/'


class MaintenanceDashboardBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.context = self.browser.new_context(viewport={'width': 1440, 'height': 1000})
        self.page = self.context.new_page()

    def tearDown(self):
        self.context.close()

    def assert_no_horizontal_overflow(self):
        self.assertTrue(self.page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'))

    def test_homepage_navigation_and_back(self):
        self.page.goto(BASE_URL)
        self.page.locator('a[href="maintenance.html"]').click()
        expect(self.page).to_have_url(urljoin(BASE_URL, 'maintenance.html'))
        expect(self.page.get_by_role('heading', name='维护指挥台', exact=True)).to_be_visible()
        self.page.get_by_role('link', name='← 知识地图', exact=True).click()
        expect(self.page).to_have_url(urljoin(BASE_URL, 'index.html'))
        self.page.go_back()
        expect(self.page.get_by_role('heading', name='维护指挥台', exact=True)).to_be_visible()

    def test_offline_snapshot_explains_unknown_and_details_toggle(self):
        self.page.goto(urljoin(BASE_URL, 'maintenance.html'))
        expect(self.page.locator('.notice').first).to_contain_text('不是实时在线状态')
        self.assertEqual(self.page.locator('.metric strong').all_text_contents()[:2], ['未知', '未知'])
        expect(self.page.locator('.notice').first).to_contain_text('未采集')
        self.assertEqual(self.page.locator('.bar-column').count(), 0)
        details = self.page.locator('footer details')
        details.locator('summary').focus()
        self.page.keyboard.press('Enter')
        self.assertTrue(details.evaluate('element => element.open'))
        expect(details.get_by_role('link', name='下载本次公开数据快照')).to_be_visible()
        self.page.keyboard.press('Enter')
        self.assertFalse(details.evaluate('element => element.open'))
        expect(details.get_by_role('link', name='下载本次公开数据快照')).to_be_hidden()
        self.page.set_viewport_size({'width': 390, 'height': 844})
        self.assert_no_horizontal_overflow()

    def test_populated_snapshot_layout_and_escaped_original_title(self):
        # Only a transient browser document, never a deployed or canonical fixture.
        record = {'number': 1, 'title': 'docs: <script>中文测试</script>', 'updated_at': '2026-10-21T08:00:00Z', 'merged_at': '2026-10-21T08:00:00Z', 'draft': False}
        snapshot = {'generated_at': '2026-10-21T08:00:00+00:00', 'window_start': '2026-10-08', 'sources': {'open_prs': [], 'issues': [], 'merged_prs': [record]}}
        self.page.set_content(render(snapshot))
        self.assertEqual(self.page.locator('script').count(), 0)
        self.assertEqual(self.page.locator('.bar-column').count(), 14)
        self.assert_no_horizontal_overflow()
        first_panel = self.page.locator('.grid > section').first
        expect(first_panel.get_by_role('heading')).to_have_text('交付活动 / 近14天')
        details = self.page.locator('.work-list details').first
        details.locator('summary').click()
        expect(details.get_by_role('link')).to_have_attribute('href', 'https://github.com/InteropAtlas/InteropAtlas/issues/1')
        expect(details.get_by_role('link')).to_contain_text('<script>中文测试</script>')
        self.page.set_viewport_size({'width': 390, 'height': 844})
        self.assert_no_horizontal_overflow()
        # All 14 bars fit the chart itself, including the latest date.
        self.assertTrue(self.page.locator('.chart').evaluate('element => element.scrollWidth <= element.clientWidth'))


if __name__ == '__main__':
    unittest.main()
