#!/usr/bin/env python3
"""Validate the real Inbox carriers and derive a non-Canonical coverage view.

Machine checks never supply independent semantic review or acceptance authority.
No generated status tables are committed back to the knowledge source.
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from candidate_identity_validator import canonical_identifier_index, identity_route, normalized_identifier, validate_candidate
from acceptance_event_validator import validate_acceptance_event

PLAN = Path('01_State/Inbox/relations/intake-coverage-20260913.yaml')

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

def git_text(root: Path, *args: str) -> str:
    """Read Git objects locally; do not fetch networks or execute a shell."""
    try:
        result = subprocess.run(
            ['git', '-C', str(root), *args], check=True, capture_output=True,
            text=True, encoding='utf-8', timeout=30)
    except (OSError, subprocess.SubprocessError, UnicodeError) as exc:
        raise ValueError('Frozen Git evidence unavailable; use a repository checkout with its referenced history.') from exc
    return result.stdout


def object_sha(value: Any) -> str:
    if not isinstance(value, str) or not re.fullmatch(r'[0-9a-f]{40}', value):
        raise ValueError('Frozen evidence requires a full 40-character Git object SHA')
    return value


def frozen_context(root: Path, commit: str, cache: dict) -> dict[str, Any]:
    if commit not in cache:
        # The baseline must belong to this checkout's history, not an unrelated
        # object supplied beside it. Shallow/archive exports fail closed.
        git_text(root, 'merge-base', '--is-ancestor', commit, 'HEAD')
        tree = git_text(root, 'ls-tree', '-r', '-z', commit, '--',
                        '01_State/01_Objects', '01_State/Inbox/candidates')
        objects = []
        candidate_blobs = set()
        for entry in tree.split('\0'):
            if not entry:
                continue
            metadata, path = entry.split('\t', 1)
            mode, kind, blob = metadata.split()
            if kind != 'blob' or mode not in {'100644', '100755'}:
                continue
            if Path(path).suffix not in {'.yaml', '.yml'}:
                continue
            if path.startswith('01_State/Inbox/candidates/'):
                candidate_blobs.add(blob)
            elif path.startswith('01_State/01_Objects/'):
                for document in yaml.safe_load_all(git_text(root, 'cat-file', 'blob', blob)):
                    if not isinstance(document, dict):
                        raise ValueError(f'Non-record in frozen Canonical file: {path}')
                    objects.append(document)
        indexed = unique(objects, 'id')
        cache[commit] = dict(objects=indexed, index=canonical_identifier_index(indexed.values()),
                             candidate_blobs=candidate_blobs)
    return cache[commit]


def identifier_set(record: dict[str, Any]) -> set[tuple[str, str]]:
    return {normalized_identifier(item['namespace'], item['value'])
            for item in record.get('external_identifiers', [])}


def verify_frozen_acceptance(root: Path, event: dict[str, Any], candidate: dict[str, Any],
                             obj: dict[str, Any], schema: dict, cache: dict) -> str:
    """Verify an ordinary materialization; this is not semantic approval."""
    provenance = obj.get('intake_provenance', {})
    if provenance.get('acceptance_event_id') != event['event_id']:
        raise ValueError(f'Object/event linkage missing: {obj["id"]}')
    if provenance.get('candidate_id') != candidate['candidate_id']:
        raise ValueError('Object/frozen Candidate linkage missing')
    blob = object_sha(provenance.get('reviewed_candidate_blob'))
    commit = object_sha(provenance.get('reviewed_against_commit'))
    context = frozen_context(root, commit, cache)
    if blob not in context['candidate_blobs']:
        raise ValueError('Frozen Candidate blob is not in the referenced baseline Candidate tree')
    documents = list(yaml.safe_load_all(git_text(root, 'cat-file', 'blob', blob)))
    matches = [doc for doc in documents if isinstance(doc, dict)
               and doc.get('candidate_id') == candidate['candidate_id']]
    if len(matches) != 1:
        raise ValueError('Frozen Candidate snapshot must contain exactly one matching candidate_id')
    frozen = matches[0]
    errors = validate_candidate(frozen, schema, context['index'])
    if errors:
        raise ValueError('Invalid frozen Candidate preflight: ' + '; '.join(x.message for x in errors))
    route = identity_route(frozen, context['index'])
    if route != 'review_required' or route != event['machine_route']:
        raise ValueError(f'Frozen pre-materialization route mismatch: {candidate["candidate_id"]} -> {route}')
    if obj['id'] in context['objects']:
        raise ValueError('Accepted target already existed in the frozen Canonical baseline')
    if candidate['identity_resolution']['state'] != 'duplicate':
        raise ValueError('Accepted Candidate must resolve to its single materialized object, not remain blocked')
    if candidate['identity_resolution']['matched_canonical_ids'] != [obj['id']]:
        raise ValueError('Accepted Candidate must resolve to exactly one Canonical object')
    frozen_ids = identifier_set(frozen)
    if not frozen_ids or frozen_ids != identifier_set(candidate) or frozen_ids != identifier_set(obj):
        raise ValueError('Frozen/current/Canonical external identifiers do not agree')
    executor = frozen['provenance']['executor']
    if provenance.get('candidate_executor') != executor:
        raise ValueError('Candidate executor differs from frozen source')
    if executor == event['review']['reviewer']:
        raise ValueError('Frozen Candidate executor equals reviewer')
    # Label inequality is merely a contradiction check, not proof that two
    # sessions are independent; actual scope must be independently reviewed.
    return route


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
    accepted_targets: dict[str, str] = {}
    for event in events.values():
        failures.extend(f'{event["event_id"]}: {x.message}' for x in validate_acceptance_event(event, event_schema))
        failures.extend(f'{event["event_id"]}: {x.message}' for x in Draft202012Validator(event_schema, format_checker=FormatChecker()).iter_errors(event))
        cid = event['candidate_id']
        if cid not in candidates:
            failures.append(f'Event has missing Candidate: {cid}')
        if event['decision'] == 'accepted':
            # An event ID identifies a decision, not a new subject. Never let a
            # second accepted event silently replace the first for a candidate.
            if cid in accepted:
                failures.append(f'Repeated acceptance of Candidate: {cid}')
                continue
            oid = event.get('accepted_canonical_id')
            if oid in accepted_targets:
                failures.append(f'Repeated materialization of Canonical target: {oid}')
            elif isinstance(oid, str):
                accepted_targets[oid] = cid
            if oid not in objects:
                failures.append(f'Accepted object missing: {oid}')
            candidate = candidates.get(cid, {})
            if oid not in candidate.get('identity_resolution', {}).get('matched_canonical_ids', []):
                failures.append(f'Accepted Candidate does not point to its object: {cid}')
            accepted[cid] = event
    # Every accepted event, regardless of filename, must bind an immutable
    # candidate blob and the Canonical tree actually used for its preflight.
    # Never invent a historical state by rewriting the current candidate to new.
    prior_routes = {}
    frozen_contexts = {}
    for cid, event in accepted.items():
        oid = event['accepted_canonical_id']
        if oid not in objects or cid not in candidates:
            continue
        try:
            prior_routes[cid] = verify_frozen_acceptance(
                root, event, candidates[cid], objects[oid], schema, frozen_contexts)
        except (ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
            failures.append(f'{event["event_id"]}: {exc}')
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
                    '每个 accepted 事件使用 Git 冻结候选 blob 和冻结底库提交复算；缺历史则失败，不猜测。',
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
