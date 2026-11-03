#!/usr/bin/env python3
"""Reproduce this frozen research snapshot, not a supported runtime/API or CI gate.

Use a clean checkout at BASELINE with its full referenced history. This script
only reads that checkout and writes the two files to an explicit output folder.
It reuses the frozen Engine's loader, projections, semantics, graph and audit.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import date, datetime
import json
from pathlib import Path
import subprocess
import sys

BASELINE = '9cb144c3a553ee9dbd4139d570b451aa1cbdfebf'
REPO = 'https://github.com/InteropAtlas/InteropAtlas'
PLAN = '01_State/Inbox/relations/intake-coverage-20260913.yaml'


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def url(path):
    return f'{REPO}/blob/{BASELINE}/{path}'


def counts(values):
    return dict(sorted(Counter(values).items()))


def build(root):
    if git(root, 'rev-parse', 'HEAD') != BASELINE:
        raise ValueError('Input checkout must be at the exact frozen BASELINE commit.')
    inputs = ['01_State', '02_Runtime/01_Engine']
    if git(root, 'diff', 'HEAD', '--name-only', '--', *inputs):
        raise ValueError('Tracked baseline inputs have local modifications.')
    untracked = git(root, 'ls-files', '--others', '--', *inputs).splitlines()
    if any(Path(p).suffix in {'.yaml', '.yml', '.json', '.py'} for p in untracked):
        raise ValueError('Untracked input files would change the frozen data/engine.')
    sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
    from bootstrap_query import index_objects, load_atlas
    from graph_index import GraphIndex
    from intake_coverage_audit import audit, records
    from relation_model import normalize_relation
    from semantic_model import normalize_record
    from workspace_projection import project_field
    import yaml

    objects, relations = load_atlas(root)
    index = index_objects(objects)
    graph = GraphIndex(index, relations)
    if graph.issues:
        raise ValueError('Cannot snapshot a graph with unresolved reference issues.')
    intake = audit(root)  # Includes full frozen acceptance validation; no invented status.
    plan = yaml.safe_load((root / PLAN).read_text())
    candidates = {}
    for path in sorted((root / '01_State/Inbox/candidates').rglob('*.yaml')):
        for candidate in yaml.safe_load_all(path.read_text()):
            if isinstance(candidate, dict):
                candidates[candidate['candidate_id']] = (candidate, str(path.relative_to(root)))
    assert len(candidates) == intake['totals']['candidate_records']
    accepted = {e['candidate_id']: e for e in records(root / '01_State/Inbox/acceptance-events')
                if e['decision'] == 'accepted'}
    from candidate_identity_validator import canonical_identifier_index, identity_route
    identity_index = canonical_identifier_index(index.values())
    candidate_rows = []
    for cid, (c, path) in sorted(candidates.items()):
        candidate_rows.append(dict(candidate_id=cid, label=c['label'], source=url(path),
            identity_route=identity_route(c, identity_index),
            acceptance_event_id=accepted[cid]['event_id'] if cid in accepted else None,
            accepted_canonical_id=accepted[cid]['accepted_canonical_id'] if cid in accepted else None))
    relation_rows = []
    for r in sorted(relations, key=lambda r: r['id']):
        relation_rows.append(dict(**asdict(normalize_relation(r)), source=url(r['_physical_source'])))
    category_members = defaultdict(list)
    covered = set()
    candidate_members = set()
    category_rows = []
    for cat in intake['categories']:
        members = []
        ids = set()
        for m in cat['members']:
            member = dict(m)
            oid = m['id'] if m['surface'] == 'canonical' else None
            if m['surface'] == 'candidate':
                candidate_members.add(m['id'])
                member['source'] = url(candidates[m['id']][1])
                if m['status'] == 'accepted':
                    event = accepted[m['id']]
                    oid = event['accepted_canonical_id']
                    member['acceptance_event_id'] = event['event_id']
            else:
                member['source'] = url(index[oid]['_physical_source'])
            member['resolved_canonical_id'] = oid
            if oid is not None:
                ids.add(oid)
                category_members[oid].append(dict(category_id=cat['id'], surface=m['surface'], ref_id=m['id']))
            members.append(member)
        covered.update(ids)
        touching = [r['relation_id'] for r in relation_rows if r['source_id'] in ids or r['target_id'] in ids]
        internal = [r['relation_id'] for r in relation_rows if r['source_id'] in ids and r['target_id'] in ids]
        category_rows.append(dict(id=cat['id'], name_zh=cat['name_zh'], name_en=cat['name_en'],
            memberships=members, canonical_ids=sorted(ids),
            raw_type_kind_counts=counts(f"{index[i].get('type', 'not_recorded')} / {index[i].get('kind', 'not_recorded')}" for i in ids),
            touching_relation_ids=touching, internal_relation_ids=internal))
    object_rows = []
    tags = defaultdict(list)
    no_domains = []
    no_relations = []
    isolates = []
    for oid, o in sorted(index.items()):
        projected = {f: project_field(o, f) for f in ('type', 'kind', 'domains')}
        domain_values = o.get('domains')
        if domain_values is None:
            no_domains.append(oid)
        elif not isinstance(domain_values, list) or any(not isinstance(t, str) for t in domain_values):
            raise ValueError(f'Unsupported domains representation: {oid}')
        for t in set(domain_values or []):
            tags[t].append(oid)
        explicit = [r['relation_id'] for r in relation_rows if oid in (r['source_id'], r['target_id'])]
        if not explicit:
            no_relations.append(oid)
        if not graph.forward(oid) and not graph.backlinks(oid):
            isolates.append(oid)
        object_rows.append(dict(id=oid, label=o.get('name_zh') or o.get('name_en') or oid,
            source=url(o['_physical_source']), semantic_descriptor=asdict(normalize_record(o)),
            fields=projected, seed_memberships=category_members[oid], explicit_relation_ids=explicit))
    return dict(
        title_zh='IA 领域覆盖底图：2026-10-21 已记录知识快照',
        baseline_commit=BASELINE,
        status='dated_research_snapshot_not_canonical_or_complete_domain_map',
        work_item=f'{REPO}/issues/276',
        sources=dict(seed_plan=url(PLAN), maps=[url(index[i]['_physical_source']) for i in ('interopatlas_self_map','intake_coverage_map')],
                     reused_engine=[url('02_Runtime/01_Engine/'+p+'.py') for p in
                                    ('bootstrap_query','graph_index','semantic_model','workspace_projection','intake_coverage_audit','relation_model')]),
        boundaries=[
            '本报告仅为冻结提交的派生研究快照，不写回 Canonical，也不是持续维护接口。',
            '既有种子类别为 draft / editorial_navigation_only，可重叠，不是正式领域分类或全库分类。',
            '原始 domains 标签逐字保留；不合并同义词、不将标签映射到种子类别。',
            '未记录不等于不存在；无领域标签、无种子成员关系或无图边都不能证明现实领域为空。',
            'Candidate、accepted Candidate 和直接 Canonical 引用保留不同来源；Canonical 数按稳定 ID 去重。',
            '原始 type/kind 与既有规范化描述同时保留；legacy reference_project 不被自动升级成某种成熟先例身份。',
            '互通、对齐、协同是并列非互斥的问题维度，不在此强制分箱或设置阶段。',
            '127 条显式关系与能力字段引用分别列出；候选关系提案不进入 Canonical 图。',
            '无全球或领域总体分母，不计算方案空间覆盖百分比；不重验外部标准的新鲜度。'],
        totals=dict(objects=len(index), explicit_relations=len(relations), graph_edges=len(graph.edges),
            capability_field_references=sum(e.origin=='object' for e in graph.edges),
            candidate_records=len(candidates), acceptance_events=intake['totals']['acceptance_events'],
            accepted_candidates=len(accepted), seed_categories=len(category_rows), seed_memberships=len(plan['memberships']),
            distinct_canonical_seed_members=len(covered), canonical_without_seed_membership=len(index)-len(covered),
            objects_with_recorded_domains=len(index)-len(no_domains), objects_without_recorded_domains=len(no_domains),
            distinct_raw_domain_tags=len(tags), objects_without_explicit_relations=len(no_relations), graph_isolates=len(isolates)),
        raw_type_counts=counts(o.get('type','not_recorded') for o in objects),
        raw_type_kind_counts=counts(f"{o.get('type','not_recorded')} / {o.get('kind','not_recorded')}" for o in objects),
        seed_categories=category_rows,
        raw_domain_tags=[dict(tag=t, canonical_ids=ids) for t,ids in sorted(tags.items())],
        unrecorded=dict(domains=no_domains, seed_membership=sorted(set(index)-covered),
            candidate_seed_membership=sorted(set(candidates)-candidate_members),
            explicit_relations=no_relations, graph_edges=isolates),
        canonical_objects=object_rows, candidate_inventory=candidate_rows,
        explicit_relations=relation_rows,
        capability_field_references=[asdict(e) for e in graph.edges if e.origin=='object'],
        seed_proposals=dict(source=url(PLAN), interpretation='Unchanged plan proposals, not extra Canonical edges; inspect current explicit relations separately.', records=plan['proposals']),
        validation=dict(intake_outcome=intake['outcome'], reference_issues=[asdict(i) for i in graph.issues],
            compatibility_warnings=[asdict(w) for w in graph.compatibility_warnings]))


def markdown(r):
    t=r['totals']; objects={o['id']:o for o in r['canonical_objects']}
    def obj(oid):
        o=objects[oid]
        return f"[{o['label']}]({o['source']}) (`{oid}`)"
    def group(ids):
        return '；'.join(obj(i) for i in ids) or '无已记录成员（不表示现实领域为空）'
    lines=['# IA 领域覆盖底图：2026-10-21 已记录知识快照', '',
        '<!-- InteropAtlas Document Metadata v0\nDocument Status: dated_research_snapshot\nDocument Created At: 2026-10-21T02:31:32+00:00\nDocument Updated At: 2026-10-21T02:31:32+00:00\nMetadata Provenance: direct_record\nLifecycle Time Provenance: direct_record\nContribution Identity Provenance: commit_explicit\nLatest Substantive Contribution:\n  Initiator: Human Owner — ff6962757\n  Executor: Agent — OpenAI / dot\n  Reviewer: see independent review in linked PR / Issue #276\n  GitHub Actor: ff6962757\n-->', '',
        '> 这是一份可检查、可复算的日期化覆盖底图，汇总本轮导航与关系、实现先例补证；不是实时地图或已完成的全领域地图。上一份 [2026-10-20 快照](../domain-coverage-2026-10-20/README.zh-CN.md) 原样保留。', '',
        f"冻结于 [{BASELINE[:12]}]({REPO}/commit/{BASELINE})（2026-10-21）。[机器可读完整清单](snapshot.json) · [复算脚本](reproduce.py) · [工作项 #276]({r['work_item']})。", '',
        '## 先看什么', '',
        '- 看已经有哪些方向：第二节的既有 20 类种子导航，每类列出正式记录和仍待处理的候选。',
        '- 看标准与实现先例：第一节按原始类型/种类计数；没有把所有 artifact 或 reference_project 都叫作标准。',
        '- 看关系：第三节给出真实已记录的关系例子和全量关系入口；每个领域的“涉及关系”只是其成员相接的边，不证明领域等价。',
        '- 看还不知道什么：第四节分别列出没有种子成员关系、没有 domains 标签和没有显式关系的对象。',
        '- 看其他领域线索：第五节完整保留 85 个原始领域标签及成员，不将它们硬塞进 20 个种子类别。', '',
        '## 1. 已记录的知识范围', '',
        f"- Canonical 对象 {t['objects']} 个；显式 Relation {t['explicit_relations']} 条。",
        f"- 图共 {t['graph_edges']} 条边，其中 {t['capability_field_references']} 条只是 capabilities 字段引用，不是额外技术关系。",
        f"- Candidate {t['candidate_records']} 个，验收事件 {t['acceptance_events']} 个，其中 accepted Candidate {t['accepted_candidates']} 个。它们不再重复计作新增 Canonical。",
        f"- 既有 20 类种子有 {t['seed_memberships']} 条成员记录，解析到 {t['distinct_canonical_seed_members']} 个不重复 Canonical 对象。",
        f"- {t['objects_with_recorded_domains']} 个对象记录了 domains，逐字形成 {t['distinct_raw_domain_tags']} 个标签；{t['objects_without_recorded_domains']} 个未记录。", '',
        '| 原始 type / kind | 对象数 |', '| --- | ---: |']
    lines += [f'| `{k}` | {v} |' for k,v in r['raw_type_kind_counts'].items()]
    lines += ['', '`not_recorded` 表示原字段缺失，不是对象没有种类。既有 semantic_model 的规范化结果另存 JSON，不能用规范化默认值冒充原始记录。', '',
        '明确记录为 system / library 的实现先例：'+group([o['id'] for o in r['canonical_objects'] if o['fields']['type']['value']=='system' and o['fields']['kind']['value']=='library'])+'。',
        '这六个库均已进入既有种子成员表；其原记录仍未填写 domains。本快照分别保留编辑归属与原始标签，不把导航补齐当作标准符合性或生产推荐。其他 system 种类仍按上表与各领域原记录读取，不把它们遗漏或统一称作库。', '',
        '## 2. 既有种子领域导航', '',
        f"来源：[原始种子计划]({r['sources']['seed_plan']})。状态仍是 draft / editorial_navigation_only。类别可重叠，不是正式 taxonomy、互斥目录或全库分类。", '',
        '“直接”指计划直接引用 Canonical；“已验收”保留 Candidate 来源，再按验收事件找到 Canonical；“待处理”不进入正式对象数。计数只针对这张种子成员表。', '',
        '| 既有类别 | 去重正式对象 | 待处理候选 | 成员涉及的显式关系 |', '| --- | ---: | ---: | ---: |']
    for cat in r['seed_categories']:
        lines.append(f"| {cat['name_zh']} (`{cat['id']}`) | {len(cat['canonical_ids'])} | {sum(m['resolved_canonical_id'] is None for m in cat['memberships'])} | {len(cat['touching_relation_ids'])} |")
    relation_index = {rel['relation_id']: rel for rel in r['explicit_relations']}
    for cat in r['seed_categories']:
        lines += ['', f"### {cat['name_zh']} · {cat['id']}", '']
        for m in cat['memberships']:
            oid=m['resolved_canonical_id']
            if oid:
                origin='直接 Canonical 引用' if m['surface']=='canonical' else f"已验收 Candidate `{m['id']}`"
                lines.append(f'- {obj(oid)}；{origin}。')
            else:
                lines.append(f"- 待处理：[{m['label']}]({m['source']}) (`{m['id']}`)，状态 `{m['status']}`；不计入正式对象。")
        lines += ['','实际 type / kind：'+('；'.join(f'`{k}` × {v}' for k,v in cat['raw_type_kind_counts'].items()) or '尚无可解析的正式成员')+'。',
                  f"成员相接显式关系 {len(cat['touching_relation_ids'])} 条，其中两端均在该成员集合内 {len(cat['internal_relation_ids'])} 条。详见 JSON 的 touching_relation_ids / internal_relation_ids；不跨类别相加。"]
        if cat['touching_relation_ids']:
            lines += ['', '可继续探索的已记录相接关系（邻居不因此自动归入本类别；适用条件见关系原记录）：', '']
            for rid in cat['touching_relation_ids']:
                rel = relation_index[rid]
                lines.append(f"- {obj(rel['source_id'])} → `{rel['predicate']}` → {obj(rel['target_id'])}。[条件与证据]({rel['source']})")
    lines += ['', '## 3. 已记录关系如何连接这些知识', '',
        '下面展示库中实际存在的关系，不从标题、同类标签或节点邻接推导新关系。适用条件与证据保留在 JSON 的规范化 context / evidence，并链接到冻结原记录。', '']
    example_ids={'ebu_libadm','ebu_libbw64','http3_rfc9114','quic_rfc9000','quic_tls_rfc9001','mcp_2025_11_25'}
    for rel in r['explicit_relations']:
        if rel['source_id'] in example_ids:
            lines.append(f"- {obj(rel['source_id'])} → `{rel['predicate']}` → {obj(rel['target_id'])}。[关系及条件]({rel['source']})")
    lines += ['', f"完整 {t['explicit_relations']} 条显式关系可在 [snapshot.json](snapshot.json) 的 explicit_relations 查询；每个对象的 explicit_relation_ids 可反查。{t['capability_field_references']} 条字段引用单列在 capability_field_references。", '',
        f"{t['objects_without_explicit_relations']} 个对象没有显式关系；即使加上能力字段引用，仍有 {t['graph_isolates']} 个图孤点（包括两张 Map）。Map 的 roots / pinned / groups 是导航元数据，GraphIndex 不把它们当技术关系，所以不能由“Map 是孤点”推断地图没有导航内容。", '',
        '种子计划还保留 2 个关系提案。这里忠实保存原稿，不把它们当作 2 条新增关系；is05_is04 的身份/版本与 opus_update 的谓词边界仍待明确，提案不进入 Canonical 图。', '',
        '## 4. 空白和未知，下一步从哪里补', '',
        '这是记录/映射缺口，不是现实世界的空白证明；不自动产生新 Canonical Open Gap 对象。', '',
        f"1. {t['canonical_without_seed_membership']} 个 Canonical 对象没有这张种子表的成员记录。本轮有明确依据的归属已整理；保留项的[逐项范围/证据限制](https://github.com/InteropAtlas/InteropAtlas/pull/463)不是永久不适用、真实领域空白或新的禁止规则，不为清零强归。",
        f"2. {t['objects_without_recorded_domains']} 个对象未记录 domains。需要逐对象核查；不因所属文件、名称或相邻节点而自动赋值。",
        f"3. {t['objects_without_explicit_relations']} 个对象没有显式关系。应检查具体标准与实现的有证据连接，而不是为了消除孤点随意加边。",
        '4. 标签与种子类别没有已接纳的归一对应；保持两层可读即可，不把正式 taxonomy 设计当作开始整理的前置阻塞。',
        '5. 本快照不另外复核外部版本新鲜度、现实方案总数或方案间完整替代覆盖；按冻结原记录保留已做核查与未知，#276 的总体工作仍未完成。', '',
        '### 未记录种子成员关系的 Canonical 对象', '', group(r['unrecorded']['seed_membership']), '',
        '### 未记录 domains 的 Canonical 对象', '', group(r['unrecorded']['domains']), '',
        '### 未记录显式关系的 Canonical 对象', '', group(r['unrecorded']['explicit_relations']), '',
        '## 5. 原始 domains 标签清单', '',
        '标签按原样、按字典序展示；同一对象可以在多个标签下重复出现。这里的“成员”仅指对象直接记录了该字符串，不代表类别标准化或关联证据已充分。', '',
        '| 原始标签 | 对象数 | 已记录对象 |', '| --- | ---: | --- |']
    for tag in r['raw_domain_tags']:
        lines.append(f"| `{tag['tag']}` | {len(tag['canonical_ids'])} | {group(tag['canonical_ids'])} |")
    lines += ['', '## 6. 如何复算及使用边界', '',
        '复用既有加载、语义、关系与投影代码；没有新 Engine、JSON API 合同、页面或 CI 维护要求。snapshot.json 是日期化研究证据，不是第二事实源。它不会自动跟随 main 更新。', '',
        '在具有完整历史的本地仓库创建冻结 checkout，然后用当前目录的脚本生成到临时目录：', '', '```bash',
        f'git worktree add --detach /tmp/ia-coverage-20261021 {BASELINE}',
        'python 03_Evolution/01_Research/02_Audits/domain-coverage-2026-10-21/reproduce.py \\',
        '  --root /tmp/ia-coverage-20261021 --output /tmp/ia-coverage-output',
        '```', '',
        '依赖使用冻结 Engine 的 requirements.txt。脚本拒绝错误提交、修改过的输入或新增的输入文件；验收审计缺少冻结 Git 历史时会失败，不猜测。', '',
        f"图引用错误 {len(r['validation']['reference_issues'])} 个；兼容性警告 {len(r['validation']['compatibility_warnings'])} 个，均原样保存在 JSON。机器验证只证明结构与引用，不代替独立语义复核。", '',
        '### 边界', ''] + ['- '+x for x in r['boundaries']]
    return '\n'.join(lines)+'\n'


def json_value(value):
    # YAML may parse unquoted source dates. Preserve their ISO representation,
    # but fail for unexpected values instead of silently stringifying them.
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    raise TypeError(f"Unsupported JSON value: {type(value).__name__}")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args=parser.parse_args()
    report=build(args.root.resolve())
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output/'snapshot.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=json_value)+'\n',encoding='utf-8')
    (args.output/'README.zh-CN.md').write_text(markdown(report),encoding='utf-8')
    print(json.dumps(report['totals'],ensure_ascii=False))


if __name__=='__main__':
    main()
