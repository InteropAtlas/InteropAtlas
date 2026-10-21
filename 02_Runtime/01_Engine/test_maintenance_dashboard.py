#!/usr/bin/env python3
"""Offline regression coverage for maintenance snapshot and public view."""
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
import maintenance_dashboard as dashboard

NOW = datetime(2026, 10, 21, 8, tzinfo=timezone.utc)

def row(number=1, **kwargs):
    return dict(number=number, title='Example', updated_at='2026-10-21T07:00:00Z', **kwargs)


class DashboardTests(unittest.TestCase):
    def test_missing_is_unknown_not_zero(self):
        with patch.object(dashboard, 'fetch_pages', side_effect=HTTPError('url', 403, 'Forbidden', {}, None)):
            snapshot = dashboard.collect(NOW)
        self.assertEqual(snapshot['sources'], dict(open_prs=None, issues=None, merged_prs=None))
        self.assertEqual(len(snapshot['errors']), 3)
        page = dashboard.render(snapshot)
        self.assertIn('趋势数据未知', page)
        self.assertIn('<strong>未知</strong>', page)
        self.assertNotIn('Forbidden', json.dumps(snapshot))

    def test_network_failure_is_unknown(self):
        with patch.object(dashboard, 'fetch_pages', side_effect=OSError('network')):
            self.assertIsNone(dashboard.collect(NOW)['sources']['issues'])

    def test_merged_filter_and_public_field_allowlist(self):
        values = [[], [row(pull_request={}), row(2, body='private not copied')], [
            row(3, merged_at=None), row(4, merged_at='2026-10-07T23:59:00Z'),
            row(5, merged_at='2026-10-08T00:00:00Z'), row(6, merged_at='2026-10-21T01:00:00Z')]]
        with patch.object(dashboard, 'fetch_pages', side_effect=values):
            snapshot = dashboard.collect(NOW)
        self.assertEqual([r['number'] for r in snapshot['sources']['issues']], [2])
        self.assertEqual([r['number'] for r in snapshot['sources']['merged_prs']], [5, 6])
        self.assertNotIn('private not copied', json.dumps(snapshot))

    def test_pagination_continues_full_page_and_respects_window(self):
        class Response:
            def __init__(self, data): self.data = json.dumps(data)
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self): return self.data
        with patch.object(dashboard.urllib.request, 'urlopen', side_effect=[Response([row(n) for n in range(100)]), Response([row(101)])]) as fetch:
            result = dashboard.fetch_pages('pulls?state=closed', '2026-10-08')
        self.assertEqual(len(result), 101)
        self.assertIn('page=2', fetch.call_args.args[0].full_url)
        with patch.object(dashboard.urllib.request, 'urlopen', return_value=Response([dict(row(n), updated_at='2026-10-01T00:00:00Z') for n in range(100)])) as fetch:
            dashboard.fetch_pages('pulls?state=closed', '2026-10-08')
        self.assertEqual(fetch.call_count, 1)

    def test_escape_and_fixed_link(self):
        result = dashboard.cards([row(title_unused=None) | {'title': '<script>中文</script>', 'html_url': 'javascript:alert(1)'}], '')
        self.assertNotIn('<script>', result)
        self.assertIn('&lt;script&gt;', result)
        self.assertNotIn('javascript:', result)
        self.assertIn('https://github.com/InteropAtlas/InteropAtlas/issues/1', result)

    def test_missing_waiting_field_is_unknown(self):
        snapshot = {'sources': {'issues': [dashboard.compact(row())]}}
        self.assertIn('等待条件数据未知', dashboard.render(snapshot))
        self.assertNotIn('没有标为等待负责人', dashboard.render(snapshot))

    def test_summary_translates_only_known_titles(self):
        self.assertEqual(dashboard.summary({'title': 'data: add bounded FHIR Python model implementation precedent'}), '补充医疗数据的软件实现先例')
        self.assertEqual(dashboard.summary({'title': 'unknown future English title'}), '一项项目改动（展开查看原记录）')
        self.assertEqual(dashboard.summary({'title': 'docs: 补充中文说明'}), '补充中文说明')
        self.assertEqual(dashboard.readable_time('2026-10-21T08:00:00Z'), '2026-10-21 16:00（UTC+8）')
        self.assertEqual(dashboard.readable_time(None), '未知')
        self.assertEqual(dashboard.readable_time('2026-10-21T08:00:00'), '未知')
        self.assertIn('查看原始记录与依据', dashboard.cards([row()], ''))

    def test_chart_has_fourteen_days_and_no_completion_percentage(self):
        snapshot = {'generated_at': NOW.isoformat(), 'window_start': '2026-10-08', 'sources': {'issues': [], 'open_prs': [], 'merged_prs': [row(merged_at='2026-10-21T01:00:00Z')]}}
        page = dashboard.render(snapshot)
        self.assertEqual(page.count('class="bar-column"'), 14)
        self.assertIn('2026-10-21：1 项', page)
        self.assertIn('2026-10-21 16:00:00（UTC+8）', page)
        self.assertIn('不是实时', page)
        self.assertIn('不计算完成率', page)

    def test_local_build_is_offline_and_writes_artifacts(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(dashboard, 'fetch_pages', side_effect=AssertionError('No network')):
            output = Path(directory)
            dashboard.build(output)
            self.assertTrue((output / 'maintenance.html').is_file())
            self.assertIn('未采集', (output / 'maintenance-snapshot.json').read_text())

if __name__ == '__main__':
    unittest.main()
