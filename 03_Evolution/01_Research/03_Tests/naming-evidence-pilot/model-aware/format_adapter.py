"""Lossless boundary normalization for model JSON envelopes.

This module may repair only representation differences whose semantic payload is
fully present and mechanically provable. Raw model bytes remain authoritative and
must be stored separately by the caller. It never invents candidates, IDs,
decisions, reasons or screening facts.
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
    """Return normalized bytes plus an audit record; unsafe differences stay raw."""
    value = _decode(raw)
    stage = question.get('stage')
    audit = {'schema_version': 1, 'stage': stage, 'raw_sha256': p.digest(raw),
             'changed': False, 'action': 'none', 'semantic_fields_added': False,
             'semantic_fields_removed': False, 'limits': 'Representation-only; semantic truth is not assessed.'}

    if stage == 'proposal' and isinstance(value, list):
        if not _valid_candidate_rows(value):
            audit['action'] = 'refused_candidate_array_not_complete_exact_contract'
            return raw, audit
        normalized = p.canonical({'candidates': value})
        audit.update(changed=True, action='wrap_complete_candidate_array_in_candidates_object',
                     normalized_sha256=p.digest(normalized), rows=len(value))
        return normalized, audit

    if stage != 'proposal' and isinstance(value, dict) and isinstance(value.get('reviews'), list):
        items = question.get('items')
        if not isinstance(items, list):
            audit['action'] = 'refused_review_without_input_items'
            return raw, audit
        names = {row.get('id'): row.get('name') for row in items
                 if isinstance(row, dict) and isinstance(row.get('id'), str) and isinstance(row.get('name'), str)}
        normalized_rows, removed = [], []
        for row in value['reviews']:
            if not isinstance(row, dict):
                audit['action'] = 'refused_review_non_object'
                return raw, audit
            keys = set(row)
            if keys == REVIEW_FIELDS:
                normalized_rows.append(row)
                continue
            if keys == REVIEW_FIELDS | {'name'} and row.get('id') in names and row.get('name') == names[row['id']]:
                normalized_rows.append({key: row[key] for key in ('id', 'decision', 'reason')})
                removed.append({'id': row['id'], 'field': 'name', 'value_sha256': p.digest(row['name'].encode())})
                continue
            audit['action'] = 'refused_review_extra_or_mismatched_field'
            audit['refused_id'] = row.get('id')
            return raw, audit
        if removed:
            normalized_value = dict(value, reviews=normalized_rows)
            normalized = p.canonical(normalized_value)
            audit.update(changed=True, action='remove_exact_redundant_review_name_fields',
                         normalized_sha256=p.digest(normalized), removed=removed)
            return normalized, audit

    return raw, audit
