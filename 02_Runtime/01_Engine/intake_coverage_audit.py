#!/usr/bin/env python3
"""Validate the real Inbox carriers and derive a non-Canonical coverage view.

Machine checks never supply independent semantic review or acceptance authority.
No generated status tables are committed back to the knowledge source.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from candidate_identity_validator import canonical_identifier_index, identity_route, validate_candidate
from acceptance_event_validator import validate_acceptance_event

PLAN = Path('01_State/Inbox/relations/intake-coverage-20260913.yaml')
BATCH_EVENTS = Path('01_State/Inbox/acceptance-events/rfc-intake-20260913.yaml')

def documents(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding='utf-8') as stream:
        return [x for x in yaml.safe_load_all(stream) if isinstance(x, dict)]

def records(directory: Path) -> list[dict[str, Any]]:
    result = []
    for path in sorted(directory.rglob('*')):
        if path.suffix in {'.yaml', '.yml'}:
            result.extend(documents(path))
    return result

def unique(items: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    result = {}
    for item in items:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f'Missing {key}')
        if value in result:
            raise ValueError(f'Duplicate {key}: {value}')
        result[value] = item
    return result

def audit(root: Path) -> dict[str, Any]:
    objects = unique(records(root / '01_State/01_Objects'), 'id')
    candidates = unique(records(root / '01_State/Inbox/candidates'), 'candidate_id')
    events = unique(records(root / '01_State/Inbox/acceptance-events'), 'event_id')
    schema = json.loads((root / '01_State/01_Objects/candidate-object.v1.schema.json').read_text())
    event_schema = json.loads((root / '01_State/Inbox/acceptance-events/acceptance-event.v1.schema.json').read_text())
    index = canonical_identifier_index(objects.values())
    failures: list[str] = []
    for item in candidates.values():
        failures.extend(f'{item["candidate_id"]}: {x.message}' for x in validate_candidate(item, schema, index))
        failures.extend(f'{item["candidate_id"]}: {x.message}' for x in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(item))
    accepted: dict[str, dict[str, Any]] = {}
    for event in events.values():
        failures.extend(f'{event["event_id"]}: {x.message}' for x in validate_acceptance_event(event, event_schema))
        failures.extend(f'{event["event_id"]}: {x.message}' for x in Draft202012Validator(event_schema, format_checker=FormatChecker()).iter_errors(event))
        cid = event['candidate_id']
        if cid not in candidates:
            failures.append(f'Event has missing Candidate: {cid}')
        if event['decision'] == 'accepted':
            oid = event.get('accepted_canonical_id')
            if oid not in objects:
                failures.append(f'Accepted object missing: {oid}')
            candidate = candidates.get(cid, {})
            if oid not in candidate.get('identity_resolution', {}).get('matched_canonical_ids', []):
                failures.append(f'Accepted Candidate does not point to its object: {cid}')
            accepted[cid] = event
    # Reconstruct the bounded pre-materialization index. This is not a historical
    # replay if unrelated main changes have subsequently landed; the report says so.
    batch = documents(root / BATCH_EVENTS)
    batch_ids = {e['accepted_canonical_id'] for e in batch if e['decision'] == 'accepted'}
    prior_index = canonical_identifier_index(o for oid, o in objects.items() if oid not in batch_ids)
    prior_routes = {}
    for event in batch:
        cid = event['candidate_id']
        candidate = candidates[cid]
        proposal = dict(candidate)
        proposal['identity_resolution'] = dict(state='new', matched_canonical_ids=[], reasons=[], merge_authorized=False)
        route = identity_route(proposal, prior_index)
        prior_routes[cid] = route
        if route != event['machine_route']:
            failures.append(f'Pre-materialization route mismatch: {cid} -> {route}')
        oid = event['accepted_canonical_id']
        provenance = objects.get(oid, {}).get('intake_provenance', {})
        if provenance.get('acceptance_event_id') != event['event_id']:
            failures.append(f'Object/event linkage missing: {oid}')
        if provenance.get('candidate_executor') == event['review']['reviewer']:
            failures.append(f'Frozen Candidate executor equals reviewer: {cid}')
        # Different labels alone are NOT proof of independence. Human/Agent review
        # of the immutable blob and the disclosed scope remains necessary.
    plan = documents(root / PLAN)[0]
    categories = unique(plan['categories'], 'id')
    grouped = {cid: [] for cid in categories}
    def resolve(ref: dict[str, str]) -> dict[str, str]:
        surface, rid = ref['surface'], ref['id']
        if surface == 'canonical':
            if rid not in objects:
                raise ValueError(f'Missing canonical reference: {rid}')
            return dict(surface=surface, id=rid, status='canonical_record', label=objects[rid].get('name_zh', rid))
        if surface != 'candidate' or rid not in candidates:
            raise ValueError(f'Missing candidate reference: {rid}')
        item = candidates[rid]
        status = 'accepted' if rid in accepted else identity_route(item, index)
        return dict(surface=surface, id=rid, status=status, label=item['label'])
    seen = set()
    for membership in plan['memberships']:
        cid = membership['category_id']
        if cid not in categories:
            raise ValueError(f'Missing category: {cid}')
        ref = membership['ref']
        key = (cid, ref['surface'], ref['id'])
        if key in seen:
            raise ValueError(f'Duplicate membership: {key}')
        seen.add(key)
        grouped[cid].append(resolve(ref))
    unique(plan['proposals'], 'id')
    for edge in plan['proposals']:
        resolve(edge['source']); resolve(edge['target'])
        if edge['status'] != 'review_required' or not edge.get('evidence'):
            failures.append(f'Unsafe proposed relationship: {edge["id"]}')
    if failures:
        raise ValueError('\n'.join(failures))
    rows = [dict(**categories[cid], members=grouped[cid]) for cid in categories]
    return dict(outcome='PASS / STRUCTURAL AND REFERENCE CHECKS ONLY',
        totals=dict(canonical_records=len(objects), candidate_records=len(candidates), acceptance_events=len(events)),
        candidate_routes=dict(Counter(identity_route(x, index) for x in candidates.values())),
        plan=dict(categories=len(categories), memberships=len(seen), proposed_technical_relations=len(plan['proposals'])),
        pre_materialization_routes=prior_routes, categories=rows,
        boundaries=['独立性由冻结原稿与真实执行者核查，不由不同名称或机器检查证明。',
                    '前置路由重算基于当前树移除本批六个对象，不冒充任意未来时点的历史回放。',
                    '类别为本轮非互斥种子；不表示全库已分类或全球覆盖率。',
                    '候选技术关系尚未接纳；通用 Map UI 未接入此叠加层。'])

def markdown(report: dict[str, Any]) -> str:
    lines = ['# 收录覆盖候选视图（派生）', '', report['outcome'], '']
    for category in report['categories']:
        lines += [f'## {category["name_zh"]} · {category["priority"]}', '', category['rationale_zh'], '']
        for member in category['members']:
            lines.append(f'- `{member["id"]}` — {member["label"]} · **{member["status"]}**')
        lines.append('')
    lines += ['## 边界', ''] + report['boundaries']
    return '\n'.join(lines) + '\n'

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--json', type=Path)
    parser.add_argument('--markdown', type=Path)
    args = parser.parse_args()
    try:
        report = audit(args.root)
        text = json.dumps(report, ensure_ascii=False, indent=2)
        for target, content in [(args.json, text), (args.markdown, markdown(report))]:
            if target:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding='utf-8')
        print(text)
        return 0
    except (ValueError, KeyError, OSError, yaml.YAMLError) as exc:
        print(f'FAIL: {exc}')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
