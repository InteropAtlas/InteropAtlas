"""Bounded lossless JSON-envelope normalization; original bytes stay authoritative.

Only complete unambiguous candidate arrays and the exact output_contract wrapper
are accepted. No field, decision, ID, reason, risk or missing answer is invented.
"""
from __future__ import annotations
import json
from typing import Any
import protocol as p

CANDIDATE_FIELDS = {'name', 'pronunciation', 'meaning', 'derivation', 'risk'}
REVIEW_FIELDS = {'id', 'decision', 'reason'}


def _decode(raw: bytes) -> Any:
    body = raw.decode('utf-8').strip()
    if body.startswith('```json\n') and body.endswith('\n```'):
        body = body[8:-4]
    return json.loads(body, object_pairs_hook=p.unique,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite_json')))


def _valid_candidate_rows(value: Any) -> bool:
    return (isinstance(value, list) and bool(value)
            and all(isinstance(row, dict) and set(row) == CANDIDATE_FIELDS
                    and all(isinstance(row[key], str) and bool(row[key].strip()) for key in CANDIDATE_FIELDS)
                    for row in value))


def normalize(raw: bytes, question: dict) -> tuple[bytes, dict]:
    value = _decode(raw)
    stage = question.get('stage')
    audit = {'schema_version': 2, 'stage': stage, 'raw_sha256': p.digest(raw),
             'changed': False, 'action': 'none', 'semantic_fields_added': False,
             'semantic_fields_removed': False, 'limits': 'Representation-only; semantic truth is not assessed.'}
    original = value
    wrapped = isinstance(value, dict) and set(value) == {'output_contract'}
    if wrapped:
        value = value['output_contract']
    if stage == 'proposal':
        rows = value if isinstance(value, list) else value.get('candidates') if isinstance(value, dict) and set(value) == {'candidates'} else None
        if not _valid_candidate_rows(rows):
            audit['action'] = 'refused_candidate_array_not_complete_exact_contract'
            return raw, audit
        maximum = question.get('maximum_candidates')
        if maximum is not None and (type(maximum) is not int or len(rows) > maximum):
            audit['action'] = 'refused_candidate_count'; return raw, audit
        if wrapped or isinstance(original, list):
            value = {'candidates': rows}
            action = 'unwrap_exact_output_contract' if wrapped else 'wrap_complete_candidate_array_in_candidates_object'
        else:
            return raw, audit
    else:
        if not isinstance(value, dict) or set(value) != {'reviews'} or not isinstance(value['reviews'], list):
            audit['action'] = 'refused_ambiguous_or_unknown_review_envelope'; return raw, audit
        items = question.get('items')
        if not isinstance(items, list) or not items or not all(isinstance(v, dict) and isinstance(v.get('id'), str) and isinstance(v.get('name'), str) for v in items):
            audit['action'] = 'refused_review_without_input_items'; return raw, audit
        names = {v['id']: v['name'] for v in items}
        rows = value['reviews']
        if len(names) != len(items) or len(rows) != len(items) or not all(isinstance(v, dict) and isinstance(v.get('id'), str) for v in rows) or {v['id'] for v in rows} != set(names):
            audit['action'] = 'refused_review_coverage_or_input_ambiguity'; return raw, audit
        normalized_rows, removed = [], []
        for row in rows:
            keys = set(row)
            if keys not in (REVIEW_FIELDS, REVIEW_FIELDS | {'name'}) or row.get('decision') not in ('keep', 'hold', 'drop') or not isinstance(row.get('reason'), str) or not row['reason'].strip():
                audit['action'] = 'refused_review_extra_or_mismatched_field'; return raw, audit
            if 'name' in row:
                if row['name'] != names[row['id']]:
                    audit['action'] = 'refused_review_extra_or_mismatched_field'; return raw, audit
                removed.append({'id': row['id'], 'field': 'name', 'value_sha256': p.digest(row['name'].encode())})
            normalized_rows.append({k: row[k] for k in ('id', 'decision', 'reason')})
        if not wrapped and not removed:
            return raw, audit
        value = {'reviews': normalized_rows}
        action = 'unwrap_exact_output_contract' if wrapped else 'remove_exact_redundant_review_name_fields'
        audit['removed'] = removed
    normalized = p.canonical(value)
    audit.update(changed=True, action=action, normalized_sha256=p.digest(normalized),
                 exact_outer_wrapper_removed=wrapped)
    return normalized, audit
