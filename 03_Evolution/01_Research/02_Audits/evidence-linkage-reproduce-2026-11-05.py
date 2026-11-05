#!/usr/bin/env python3
"""One-time evidence-linkage audit using unchanged IA loaders/projections; no network or upstream execution."""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys

SPEC = json.loads(r'''
{
  "baseline": "314d70148ae1f154c852c85f9d4886804c74ac54",
  "updated_at": "2026-11-05T18:11:55.002588+00:00",
  "scope": "One-time six-object linkage of six completed study questions. No new type/schema/API/query contract or future maintenance rule. Supporting factual artifacts are separated from IA-authored notes.",
  "current_contribution": {
    "initiator": "Human Owner — ff6962757",
    "executor": "Agent — OpenAI / dot / finish_wot_evidence",
    "reviewer": "Independent Agent — OpenAI / dot / review_evidence_integration",
    "github_actor": "ff6962757"
  },
  "allowed_metadata_delta": {
    "rfc3339": {
      "metadata_provenance": {
        "lifecycle_time": "mixed",
        "contribution_identity": "commit_explicit"
      }
    }
  },
  "rows": [
    {
      "id": "wot_td_1.1",
      "object_path": "01_State/01_Objects/wot_td_1.1.yaml",
      "question": "同一 Recommendation 身份是否固定验证资源？",
      "report_path": "03_Evolution/02_Experiments/02_Pilots/wot-td-resource-runtime-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/wot-td-resource-runtime-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105-manifest.json#L1-L224",
          "title": "IA historical source locator — fixed official TD/TM resource identities and hashes; not a new specification",
          "accessed": "2026-11-05"
        },
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105-result.json",
          "title": "IA historical observed results — fixed TD/TM resources with Draft7; no node-wot or JSON-LD execution",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "ddfe9ecd6fa68d78e7c7cdddbcef808284e0d33a942d1952d56296b32d968a13",
      "candidate_object_sha256": "1419af2eb32f6241f7240758c504260dd33bbfcc2f1ee76f062c6f3205161698",
      "report_sha256": "075fa5074b9edfa25834ae19081cf1a071f8164b0da0653332235f2eb7f2357d",
      "added_notes": [
        "IA 研究判断：规范身份、辅助资源字节与验证器行为须分别确定。固定前后 TD/TM schema 的部分合成输入判定不同；所列 Draft7 观察不等于完整 TD 符合性、node-wot 或 JSON-LD 运行。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/wot-td-resource-runtime-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105-manifest.json": "2d193145ab96f811d90e5de6ea09046303208f3608cee8e791b78a6881b819a3",
        "03_Evolution/02_Experiments/03_Evidence/wot-td-resource-probe-20261105-result.json": "e1c7fe4b7db7c3a4a9cf469a1830636522c105765667d019631cc4ffdf79460b"
      }
    },
    {
      "id": "mcp_python_sdk",
      "object_path": "01_State/01_Objects/mcp_python_sdk.yaml",
      "question": "所声明的工具模式在哪些路径实际被验证？",
      "report_path": "03_Evolution/02_Experiments/02_Pilots/mcp-schema-responsibility-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/mcp-schema-responsibility-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/03_Evidence/mcp-schema-source-manifest-20261105.json",
          "title": "IA historical source manifest — MCP Python SDK 1.26.0 fixed static paths; not SDK execution",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "8ce239b089d91dbd67728c8311487dd5e0c7ae742330a75e783cdc73c9ce58a4",
      "candidate_object_sha256": "cbc3d78442520e32e0f8f39ebb4beace412dcd2591ef3c0d85c0810286fbc30d",
      "report_sha256": "3717d23e9026e7e6be7568658b6b608c49f1680d30f28869cfe66e78c1d33866",
      "added_notes": [
        "IA 研究判断：固定 SDK 1.26.0 的低层、FastMCP 与客户端存在不同验证条件，应按具体调用分支解释。该研究的 SDK 证据仅为静态源码；独立 jsonschema4.26.0 方言实验不是 SDK 执行，也不更新其依赖版本或既有实现边。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/mcp-schema-responsibility-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/02_Experiments/03_Evidence/mcp-schema-source-manifest-20261105.json": "55a08647fd9dde95e31febff514064ff8410003ab853dbd711fbb8504d2e08a3"
      }
    },
    {
      "id": "rfc3339",
      "object_path": "01_State/01_Objects/rfc3339.yaml",
      "question": "共同时间语法是否表示同一事实并保留同样信息？",
      "report_path": "03_Evolution/01_Research/01_Prior_Art/timestamp-portability-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/timestamp-portability-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/timestamp-portability-2026-11-05-sources.json#L67-L1008",
          "title": "IA historical source locator — dated standards, fixed implementation sources and prior observations; no new execution",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "b9fe7d7b4cf4ea824655b68fb5c7584ff68ad8df64633a436b7c7d4722701000",
      "candidate_object_sha256": "98ef5063ef7995e54a0a0d3f7f9e981718648a9836be8dcaa881c4f41a323c4b",
      "report_sha256": "bdfaf17aba923cf504d6c2ef3e77d91fac00a9ba71c9678b3b73d42b42ac2ce4",
      "added_notes": [
        "IA 研究判断：发生、创建、记录与查询时间的字段含义，以及缺失、偏移、精度和时钟质量须分别判断；共同 RFC3339 语法不保证它们等价。该比较引用固定规范、静态实现路径和明确标注的历史观察，本次接合没有新增实现执行。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/timestamp-portability-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/01_Research/01_Prior_Art/timestamp-portability-2026-11-05-sources.json": "e24999994e6237a761a1dce15c3108718400dbd833a5e96ac28157cd0fe73171"
      }
    },
    {
      "id": "problem_details_rfc9457",
      "object_path": "01_State/01_Objects/problem_details_rfc9457.yaml",
      "question": "HTTP 问题内容与其他失败信号各自说明什么？",
      "report_path": "03_Evolution/01_Research/01_Prior_Art/failure-signal-comparison-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/failure-signal-comparison-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/failure-signal-comparison-2026-11-05-sources.json#L67-L657",
          "title": "IA historical source locator — HTTP and JSON-RPC/MCP normative and fixed-code references only; excludes unexecuted illustrations",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "f2746daf00695579b4b4f5c28281ba8ec51ba9d8bc282fa180460b3eea2c6edf",
      "candidate_object_sha256": "b0122bdad3e6847d0902e58746dfa81a98b8153a6bef914885d3d55b2094936f",
      "report_sha256": "bc1a276db68dd46a97c2f0d2bcec40b62f575b2f584df53ff505e6a8887f07aa",
      "added_notes": [
        "IA 研究判断：HTTP 状态、问题内容、JSON-RPC error、MCP 工具失败及本地异常的来源和责任不同，解析或返回成功不足以证明业务完成。比较不建立统一错误映射、优先级或重试规则；其中说明输入未作为真实交换执行。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/failure-signal-comparison-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/01_Research/01_Prior_Art/failure-signal-comparison-2026-11-05-sources.json": "63629e4363828fea6b86ed2f734259a63c6723f41faf4fca648fa5726faeaddb"
      }
    },
    {
      "id": "senml_rfc8428",
      "object_path": "01_State/01_Objects/senml_rfc8428.yaml",
      "question": "相同 JSON 数字是否足以跨格式保留量值？",
      "report_path": "03_Evolution/01_Research/01_Prior_Art/quantity-preservation-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/quantity-preservation-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/quantity-preservation-2026-11-05-evidence.json#L80-L462",
          "title": "IA historical source locator — external source identities, hashes and clauses only; not quantity conversion or observed illustration results",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "08e70ef650cb5166ea3162ab38df581eada9459c52877777100fcd60f513b5e3",
      "candidate_object_sha256": "2f143c3c10544d49b58d042e005afa18c8398e0f1649304f78c25b8b36307fc7",
      "report_sha256": "bf5778f6b43316a2b878c6e3eceafc4b50ea2c8c66d2a8e8d96ba09c434562d7",
      "added_notes": [
        "IA 研究判断：SenML base/单位继承与 FHIR Quantity 的单位身份、comparator、缺值及展示精度不是可直接互换的条件。研究保留两份规范的差别；JSON 说明例明确未执行，一次性 Decimal 算术不是格式校验或实际转换。本接合不改 FHIR 摘要或创建通用转换规则。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/01_Research/01_Prior_Art/quantity-preservation-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/01_Research/01_Prior_Art/quantity-preservation-2026-11-05-evidence.json": "5b8c148c4ecd1f40fc30cf8c1119aea9df2c05aa3c16d401fbe1474927dc476d"
      }
    },
    {
      "id": "uri_rfc3986",
      "object_path": "01_State/01_Objects/uri-rfc3986.yaml",
      "question": "引用标识何时成为被实际使用的资源？",
      "report_path": "03_Evolution/02_Experiments/02_Pilots/resource-resolution-boundary-2026-11-05.zh-CN.md",
      "report_url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/resource-resolution-boundary-2026-11-05.zh-CN.md",
      "added_sources": [
        {
          "url": "https://www.rfc-editor.org/rfc/rfc3986#section-1.2.2",
          "title": "RFC3986 section 1.2.2 — identification does not imply access; operations depend on the containing protocol or format",
          "accessed": "2026-11-05"
        },
        {
          "url": "https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/03_Evidence/resource-resolution-20261105-sources.json#L293-L346",
          "title": "IA historical context-source locator — RFC3986, CloudEvents and fixed MCP source identities; not RFC3986 runtime validation",
          "accessed": "2026-11-05"
        }
      ],
      "baseline_object_sha256": "941b7ab26ce0e70f120ca38f8d8c4cda3351e8b0c8a44ee855874a65cf45c13f",
      "candidate_object_sha256": "014ee35510b9b9f13a5cbd3ee1b06c22292d963a8fe1a24b9b2df4d22bef2385",
      "report_sha256": "4e421c6f1436b1e4f9781429b81c7c91027c4b47c4757d0dd4fb219689fc7bda",
      "added_notes": [
        "IA 研究判断：标识、基址、供应资源、缓存/加载与处理结果须分开。九个离线案例只属于 jsonschema4.26.0/referencing0.37.0 的显式内存配置，PyLD3.3.0 部分仅静态；不是 RFC3986 任意实现的运行保证，也不扩大 uriparser 入边。本链接采用已澄清官方 $schema URI 与合成资源 URL 区别的报告。 [研究报告](https://github.com/InteropAtlas/InteropAtlas/blob/314d70148ae1f154c852c85f9d4886804c74ac54/03_Evolution/02_Experiments/02_Pilots/resource-resolution-boundary-2026-11-05.zh-CN.md)。"
      ],
      "historical_source_files": {
        "03_Evolution/02_Experiments/03_Evidence/resource-resolution-20261105-sources.json": "50447faaf6c9000c0a74acae858f24d75e3bfad2ac64af7483fe2f37fb4bd349"
      }
    }
  ]
}
''')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str).encode()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--baseline-root', type=Path, required=True)
    args = parser.parse_args()
    root, baseline = args.root.resolve(), args.baseline_root.resolve()
    assert subprocess.check_output(['git', '-C', str(baseline), 'rev-parse', 'HEAD'], text=True).strip() == SPEC['baseline']
    engine = '02_Runtime/01_Engine/'
    engine_names = ['bootstrap_query.py', 'workspace_projection.py', 'relation_model.py', 'repository_layout.py']
    for name in engine_names:
        assert (root / engine / name).read_bytes() == (baseline / engine / name).read_bytes(), name
    sys.path.insert(0, str(root / engine))
    from bootstrap_query import load_atlas
    from workspace_projection import project_evidence, project_field
    before_objects, before_relations = load_atlas(baseline)
    after_objects, after_relations = load_atlas(root)
    before = {row['id']: row for row in before_objects}
    after = {row['id']: row for row in after_objects}
    assert before.keys() == after.keys()
    assert encoded(before_relations) == encoded(after_relations), 'Relations must remain unchanged'
    selected = {row['id'] for row in SPEC['rows']}
    for object_id in before.keys() - selected:
        assert encoded(before[object_id]) == encoded(after[object_id]), object_id
    results = []
    for row in SPEC['rows']:
        object_id = row['id']; old, new = before[object_id], after[object_id]
        assert digest(baseline / row['object_path']) == row['baseline_object_sha256']
        assert digest(root / row['object_path']) == row['candidate_object_sha256']
        assert digest(baseline / row['report_path']) == row['report_sha256']
        assert digest(root / row['report_path']) == row['report_sha256'], 'Historical study changed'
        for path, sha in row['historical_source_files'].items():
            assert digest(baseline / path) == sha and digest(root / path) == sha
        assert row['report_url'] not in json.dumps(old, ensure_ascii=False, default=str)
        assert 'notes_zh' not in old
        assert new['notes_zh'] == row['added_notes'] and isinstance(new['notes_zh'], list)
        assert all(isinstance(note, str) for note in new['notes_zh'])
        assert new['sources'] == old['sources'] + row['added_sources'], 'Old source order/values changed'
        allowed = {'sources', 'notes_zh', 'record_updated_at', 'latest_substantive_contribution'}
        if object_id == 'rfc3339':
            allowed.add('metadata_provenance')
            assert new['metadata_provenance'] == SPEC['allowed_metadata_delta']['rfc3339']['metadata_provenance']
        assert encoded({k: v for k, v in old.items() if k not in allowed}) == encoded({k: v for k, v in new.items() if k not in allowed})
        assert new['record_updated_at'] == SPEC['updated_at']
        assert new['latest_substantive_contribution'] == SPEC['current_contribution']
        for field in ['last_verified_at', 'last_verified_by']:
            assert (field in old) == (field in new) and old.get(field) == new.get(field)
        original_projection, projection = project_evidence(old), project_evidence(new)
        assert original_projection['assessment']['state'] == 'not_recorded'
        assert projection['assessment']['state'] == 'recorded'
        assert projection['assessment']['authority'] == 'interopatlas_authored'
        assert projection['assessment']['is_external_evidence'] is False
        assert projection['assessment']['notes'] == row['added_notes']
        assert projection['semantic_boundaries'] == original_projection['semantic_boundaries']
        added = projection['sources'][len(old['sources']):]
        assert projection['sources'][:len(old['sources'])] == original_projection['sources']
        for source, expected in zip(added, row['added_sources'], strict=True):
            assert source['url'] == expected['url'] and source['title'] == expected['title']
            assert str(source['accessed']) == expected['accessed']
            assert source['recoverable_from'] == {'canonical_object_id': object_id, 'canonical_field': 'sources'}
        notes_field = project_field(new, 'notes_zh')
        assert notes_field['state'] == 'recorded' and notes_field['value'] == row['added_notes']
        results.append({
            'object_id': object_id, 'question': row['question'],
            'before': {'original_source_count': len(old['sources']), 'assessment_state': original_projection['assessment']['state'], 'report_already_present_at_baseline': True, 'report_link_in_selected_record': False},
            'after': {'added_factual_source_references': added, 'assessment': projection['assessment'], 'notes_field_recovery': notes_field['recoverable_from']},
            'preserved': {'old_source_prefix_sha256': hashlib.sha256(encoded(old['sources'])).hexdigest(), 'last_verified_at': {'present': 'last_verified_at' in new, 'value': new.get('last_verified_at')}, 'last_verified_by': {'present': 'last_verified_by' in new, 'value': new.get('last_verified_by')}, 'all_other_record_fields_equal_except_declared_metadata': True},
            'historical_report': {'url': row['report_url'], 'sha256': row['report_sha256']},
            'historical_source_files': row['historical_source_files'],
            'rendering_limit': 'Existing standard views expose sources and assessment count, not notes text; existing implementation view exposes notes. Search index does not include source/assessment text. No renderer changes.'
        })
    print(json.dumps({'kind': 'one_time_evidence_linkage_audit', 'baseline': SPEC['baseline'], 'environment': {'python': sys.version, 'PyYAML': importlib.metadata.version('PyYAML')}, 'selected_objects': len(selected), 'added_source_entries': sum(len(row['added_sources']) for row in SPEC['rows']), 'added_assessment_notes': len(selected), 'unselected_object_records_unchanged': len(before)-len(selected), 'all_relation_records_unchanged': True, 'results': results, 'engine_sha256': {engine+n: digest(root/engine/n) for n in engine_names}, 'recipe_sha256': digest(Path(__file__)), 'boundary': 'This is a finite retrieval/preservation audit, not new upstream execution, revalidation of whole records, completeness measurement, new source authority, query contract or maintenance gate. Before not_recorded meant the selected record lacked an assessment link, not that research was absent.'}, ensure_ascii=False, indent=2, default=str))

if __name__ == '__main__':
    main()
