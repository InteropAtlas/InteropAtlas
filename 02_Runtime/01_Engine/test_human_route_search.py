#!/usr/bin/env python3
"""Deterministic tests for the first Human Route Search slice (#103)."""

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

import human_route_runtime as human_route
import human_route_search as human_search
import render_markdown as human_markdown
import render_site_semantic as semantic_site
from bootstrap_query import index_objects, load_atlas
from render_markdown import display_name, output_path
from workspace_projection import NOT_RECORDED, RECORDED, project_evidence, project_field


ROOT = Path(__file__).resolve().parents[2]


class HumanRouteSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        objects, _ = load_atlas(ROOT)
        index = index_objects(objects)
        cls.index = index
        rendered = []
        for obj in index.values():
            if semantic_site.semantic_site_view_type(obj) not in semantic_site.SUPPORTED_VIEW_TYPES:
                continue
            path = output_path(obj)
            if path:
                rendered.append((obj, Path(path).with_suffix('.html')))
        cls.rendered = rendered
        cls.rows = human_search.build_search_index(
            rendered,
            display_name,
            human_markdown.summary_of,
            lambda obj: human_route.human_object_type_label(obj, semantic_site.semantic_site_view_type),
        )

    def row(self, object_id: str) -> dict[str, str]:
        return next(row for row in self.rows if row['id'] == object_id)

    def test_representative_resources_are_indexed(self) -> None:
        for object_id in ('forgejo_actions', 'automated_build_deployment', 'yaml_1.2.2', 'apple'):
            with self.subTest(object_id=object_id):
                self.assertTrue(self.row(object_id)['url'].startswith('objects/'))

    def test_index_uses_human_type_labels(self) -> None:
        self.assertEqual(self.row('forgejo_actions')['type_label'], '实现')
        self.assertEqual(self.row('automated_build_deployment')['type_label'], '能力')
        self.assertEqual(self.row('yaml_1.2.2')['type_label'], '标准 / 规范')
        self.assertEqual(self.row('apple')['type_label'], '组织')

    def test_search_projection_contains_expected_human_terms(self) -> None:
        self.assertIn('Forgejo', self.row('forgejo_actions')['search_text'])
        self.assertIn('自动构建', self.row('automated_build_deployment')['search_text'])
        self.assertIn('YAML', self.row('yaml_1.2.2')['search_text'])
        self.assertIn('Apple', self.row('apple')['search_text'])

    def test_index_is_deterministically_sorted(self) -> None:
        keys = [(row['name'].casefold(), row['id']) for row in self.rows]
        self.assertEqual(keys, sorted(keys))

    def test_subtitle_search_ids_recover_serializable_fields_and_human_values(self) -> None:
        # A read-only integration fixture, not an Agent search API or query contract.
        before = copy.deepcopy(self.index)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            human_search.build_search_artifacts(
                output, self.rendered, semantic_site.page_shell, display_name,
                human_markdown.summary_of,
                lambda obj: human_route.human_object_type_label(obj, semantic_site.semantic_site_view_type),
            )
            rows = json.loads((output / 'search-index.json').read_text(encoding='utf-8'))
        matches = {row['id']: row for row in rows if '字幕' in row['search_text']}
        for object_id in ('w3c_imsc', 'ebu_tt_d'):
            with self.subTest(object_id=object_id):
                row = matches[object_id]
                record = self.index[row['id']]
                self.assertEqual(row['url'], f'objects/{object_id}.html')
                self.assertEqual(record['_source'], f'objects/{object_id}.yaml')
                fields = {field: project_field(record, field) for field in ('version', 'scope_notes_zh')}
                evidence = project_evidence(record)
                payload = {'fields': fields, 'evidence': evidence}
                decoded = json.loads(json.dumps(payload, ensure_ascii=False))
                self.assertEqual(decoded, payload)
                rendered = human_markdown.render_object(record, self.index)
                for field, projection in decoded['fields'].items():
                    self.assertEqual(projection['state'], RECORDED)
                    self.assertEqual(projection['value'], record[field])
                    self.assertEqual(projection['recoverable_from'], {
                        'canonical_object_id': object_id, 'canonical_field': field,
                    })
                    # These are object-level sources, not field-specific proof.
                    self.assertEqual(projection['evidence'], decoded['evidence']['sources'])
                self.assertIn('- **记录版次：** ' + decoded['fields']['version']['value'], rendered)
                self.assertIn(decoded['fields']['scope_notes_zh']['value'], rendered)
                self.assertEqual(decoded['evidence']['evidence_state'], RECORDED)
                self.assertEqual(decoded['evidence']['assessment']['state'], NOT_RECORDED)
                self.assertFalse(decoded['evidence']['assessment']['is_external_evidence'])
                self.assertFalse(decoded['evidence']['semantic_boundaries']['projection_is_canonical_write'])
                sources = decoded['evidence']['sources']
                self.assertEqual(len(sources), len(record['sources']))
                for source, canonical in zip(sources, record['sources']):
                    for field in ('url', 'title', 'accessed'):
                        self.assertEqual(source[field], canonical[field])
                    self.assertEqual(source['recoverable_from'], {
                        'canonical_object_id': object_id, 'canonical_field': 'sources',
                    })
                    self.assertIn(source['url'], rendered)
        self.assertEqual(self.index, before)

    def test_subtitle_json_preserves_versions_and_not_recorded_without_mutation(self) -> None:
        before = copy.deepcopy(self.index)
        for object_id in ('w3c_imsc', 'ebu_tt_d'):
            with self.subTest(object_id=object_id):
                record = self.index[object_id]
                projections = {field: project_field(record, field) for field in ('versions', 'capabilities')}
                decoded = json.loads(json.dumps(projections, ensure_ascii=False))
                self.assertEqual(decoded, projections)
                for field, projection in decoded.items():
                    expected = RECORDED if field in record and record[field] is not None else NOT_RECORDED
                    self.assertEqual(projection['state'], expected)
                    self.assertEqual(projection['value'], record.get(field))
                    self.assertEqual(projection['recoverable_from'], {
                        'canonical_object_id': object_id, 'canonical_field': field,
                    })
                self.assertEqual(decoded['capabilities']['state'], NOT_RECORDED)
                self.assertIsNone(decoded['capabilities']['value'])
        self.assertEqual(project_field(self.index['w3c_imsc'], 'versions')['state'], NOT_RECORDED)
        self.assertEqual(project_field(self.index['ebu_tt_d'], 'versions')['state'], RECORDED)
        self.assertEqual(self.index, before)


if __name__ == '__main__':
    unittest.main()
