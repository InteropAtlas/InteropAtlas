"""Task-local preflight for #411. No networking, naming, or semantic clearance.

Wraps the unchanged evidence validator. 'pass' means structural checks only.
Missing evidence is recordable in audit mode, never silently accepted for exposure.
State writes are local, lock-coordinated and atomic; GitHub writes still need blob CAS.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
from typing import Any
import yaml
from validate_evidence import REQUIRED, STAGES, validate

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    pairs = [(loader.construct_object(k, deep=deep), loader.construct_object(v, deep=deep)) for k, v in node.value]
    if len({k for k, _ in pairs}) != len(pairs):
        raise ValueError('duplicate YAML key')
    return dict(pairs)

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def unique_json(pairs):
    if len({k for k, _ in pairs}) != len(pairs):
        raise ValueError('duplicate JSON key')
    return dict(pairs)

def load(raw: bytes, suffix: str = '.yaml') -> dict:
    value = json.loads(raw, object_pairs_hook=unique_json) if suffix == '.json' else yaml.load(raw, Loader=UniqueLoader)
    if not isinstance(value, dict):
        raise ValueError('top-level object required')
    return value

def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def safe_path(root: Path, value: str) -> Path:
    p = PurePosixPath(value)
    if not value or p.is_absolute() or '..' in p.parts or '\\' in value:
        raise ValueError('unsafe relative path')
    result = (root / value).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('path escapes repository')
    return result

def resolve_ref(root: Path, ref: dict) -> bytes:
    commit, path, section = ref.get('commit', ''), ref.get('path', ''), ref.get('section', '')
    if not re.fullmatch(r'[0-9a-f]{40}', commit) or not section:
        raise ValueError('exact commit and section required')
    safe_path(root, path)
    p = subprocess.run(['git', '-C', str(root), 'show', commit + ':' + path], capture_output=True, timeout=15)
    if p.returncode:
        raise ValueError('pinned source not available in local Git objects')
    raw = p.stdout
    if section not in raw.decode('utf-8'):
        raise ValueError('source section absent')
    expected = ref.get('blob')
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if expected and expected != actual:
        raise ValueError('source blob mismatch')
    return raw

def result(errors, reviews, **extras):
    errors, reviews = sorted(set(errors)), sorted(set(reviews))
    return {'disposition': 'block' if errors else 'review' if reviews else 'pass',
            'errors': errors, 'review_required': reviews,
            'semantic_and_reality_clearance': 'not_assessed',
            'generation_authorization': False, **extras}

def check_record(record: dict, root: Path, operation: str = 'audit', previous=None) -> dict:
    """Checks declared evidence, not whether a label/quote is semantically truthful."""
    errors, reviews, observations = [], [], []
    try:
        base = validate(record, previous)
        errors += base['errors']; reviews += base['gaps']
        artifacts = {a['id']: a for a in record.get('artifacts', [])}
        synthetic = record.get('record_kind') == 'synthetic'
        if operation not in ('audit', 'expose', 'resume'):
            errors.append('operation_invalid')
        if not synthetic and operation in ('expose', 'resume') and record.get('owner_paused'):
            errors.append('owner_pause_blocks_action')
        if operation == 'resume':
            # Deliberately no automatic authorization path in this repair-only pilot.
            errors.append('resume_requires_separate_owner_authorization')
        for a in artifacts.values():
            if a.get('sha256') and digest(a['text'].encode()) != a['sha256']:
                errors.append('artifact_hash_mismatch:' + a['id'])
            if a.get('file'):
                try:
                    raw = safe_path(root, a['file']).read_bytes()
                    if not a.get('sha256') or digest(raw) != a['sha256'] or raw != a['text'].encode():
                        errors.append('artifact_file_mismatch:' + a['id'])
                except (ValueError, OSError):
                    errors.append('artifact_file_unresolved_or_unsafe:' + a['id'])
            elif not synthetic and a.get('kind') == 'original':
                reviews.append('original_source_requires_retrieval:' + a['id'])
        for key, entry in record.get('recovery', {}).items():
            if entry.get('status') == 'referenced':
                try:
                    resolve_ref(root, entry)
                except (ValueError, OSError, subprocess.TimeoutExpired):
                    errors.append('recovery_ref_unresolved:' + key)
        for batch in record.get('batches', []):
            stages = batch.get('stages', {})
            for fb in batch.get('feedback', []):
                observation = fb.get('observation_type')
                claim = fb.get('claim_type')
                if observation not in ('ranking', 'explicit_reason', 'explicit_constraint') or claim not in ('ranking', 'reason', 'constraint'):
                    reviews.append('feedback_semantic_classification_missing')
                if observation == 'ranking' and fb.get('basis') == 'direct_reason':
                    errors.append('ranking_promoted_to_direct_reason')
                if observation == 'ranking' and claim == 'reason' and (fb.get('basis') != 'inference' or fb.get('interpretation_status') != 'hypothesis'):
                    errors.append('ranking_reason_not_hypothesis')
                if fb.get('role') == 'gate' and observation != 'explicit_constraint':
                    errors.append('gate_requires_explicit_constraint_not_ranking')
            for screen in batch.get('screenings', []):
                try:
                    stamp = datetime.fromisoformat(screen.get('observed_at', '').replace('Z', '+00:00'))
                    if stamp.tzinfo is None:
                        raise ValueError('timezone required')
                except (TypeError, ValueError):
                    errors.append('screen_timestamp_invalid')
                if screen.get('claim') in ('available', 'clear'):
                    for q in screen.get('queries', []):
                        if q.get('outcome') == 'blocked':
                            errors.append('screen_claim_contradicts_query')
                        elif q.get('outcome') != 'clear':
                            reviews.append('screen_query_not_resolved')
                        if q.get('evidence_ref') not in artifacts:
                            reviews.append('screen_raw_evidence_missing')
                if screen.get('candidate_id') in stages.get('exposed', []) and screen.get('claim') in ('unavailable', 'blocked', 'red'):
                    errors.append('exposed_despite_negative_screen')
            runtime = batch.get('runtime', {})
            if runtime.get('level') == 'best_effort_same_context' and runtime.get('unseen_context_claim'):
                errors.append('same_context_blindness_overclaim')
            if runtime.get('level') in ('isolated_runtime', 'fresh_context') and runtime.get('evidence_ref') not in artifacts:
                reviews.append('isolation_evidence_missing')
            features = batch.get('candidate_features', {})
            if any(i not in features or not features[i].get('form_family') or features[i].get('evidence_ref') not in artifacts for i in stages.get('generated', [])):
                reviews.append('features_or_basis_missing')
                observations.append({'batch_id': batch['batch_id'], 'first_recorded_concentration_stage': 'unknown', 'causal_attribution': 'not_assessed'})
                continue
            if any(features[i].get('classification_status') != 'reviewed' for i in stages.get('generated', [])):
                reviews.append('feature_classification_requires_review')
            counts, first = {}, None
            complete = all(s in stages for s in STAGES)
            for stage in STAGES:
                if stage not in stages:
                    continue
                count = Counter(features[i]['form_family'] for i in stages[stage])
                counts[stage] = dict(sorted(count.items()))
                if first is None and len(stages[stage]) >= 2 and len(count) == 1:
                    first = stage
            observed = first if complete else 'unknown'
            declared = batch.get('batch_review', {}).get('first_recorded_concentration_stage')
            if declared is not None and declared != observed:
                errors.append('concentration_stage_claim_unsupported')
            observations.append({'batch_id': batch['batch_id'], 'family_counts': counts,
                                 'first_recorded_concentration_stage': observed, 'causal_attribution': 'not_assessed'})
            exposed = counts.get('exposed', {})
            if sum(exposed.values()) >= 2 and len(exposed) == 1:
                focus = batch.get('focus_contract', {})
                budget = focus.get('budget')
                valid_budget = type(budget) is int and budget > 0
                if budget is not None and (not valid_budget or len(stages.get('generated', [])) > budget):
                    errors.append('focus_budget_invalid_or_exceeded')
                source = artifacts.get(focus.get('source_artifact'), {})
                explicit = (batch.get('purpose') == 'exploitation' and valid_budget
                            and len(stages.get('generated', [])) <= budget
                            and focus.get('rationale') and focus.get('exit_condition')
                            and focus.get('source_artifact') in batch.get('inputs', [])
                            and focus.get('quote') and focus['quote'] in source.get('text', '')
                            and focus.get('form_family') in exposed)
                if not explicit:
                    reviews.append('concentrated_exposure_requires_bounded_purpose_review')
    except (TypeError, KeyError, ValueError, AttributeError) as exc:
        errors.append('record_shape_invalid:' + type(exc).__name__)
        base = {'capture_complete': False}
    return result(errors, reviews, baseline=base, stage_observations=observations,
                  operation=operation, recordable=not errors,
                  scope='declared_metadata_and_pinned_bytes_not_semantic_truth')

def check_state(previous: dict, proposed: dict, root: Path) -> dict:
    """Review-only state transition. Preserves active job and explicit unknowns."""
    errors, reviews = [], []
    try:
        if proposed['task'] != dict(previous['task'], snapshot_version=previous['task']['snapshot_version'] + 1):
            errors.append('task_identity_or_snapshot_drift')
        if proposed.get('schema_version') != previous.get('schema_version'):
            errors.append('schema_promotion_not_in_scope')
        if not proposed['process_review']['generation_paused'] or proposed['audit_recovery']['generation_resume_readiness']:
            errors.append('pause_or_readiness_changed_without_separate_authorization')
        for field in ('constraint_registry', 'owner_preferences', 'candidates', 'decision_criteria'):
            if proposed.get(field) != previous.get(field):
                errors.append('review_scope_value_changed:' + field)
        unknowns = set(proposed['audit_recovery']['missing_current_state'])
        if unknowns != set(previous['audit_recovery']['missing_current_state']):
            errors.append('unknown_resolution_requires_separate_evidence_review')
        for key in REQUIRED:
            ref = proposed.get('recovery_refs', {}).get(key)
            if key in proposed:
                if key in previous and proposed[key] != previous[key]:
                    errors.append('review_scope_model_changed:' + key)
                if not proposed[key]:
                    errors.append('current_state_empty:' + key)
                elif key in unknowns:
                    errors.append('unknown_filled_without_evidence_review:' + key)
                continue
            if ref:
                try:
                    target = load(resolve_ref(root, ref))
                    if target.get(key) != previous.get(key):
                        errors.append('state_ref_not_equivalent:' + key)
                except (ValueError, OSError, subprocess.TimeoutExpired):
                    errors.append('state_ref_unresolved:' + key)
            elif key in unknowns and key not in previous:
                reviews.append('inherited_unknown:' + key)
            else:
                errors.append('required_state_lost:' + key)
        for ident, entry in proposed.get('state_recovery', {}).get('source_registry', {}).items():
            for section in entry.get('sections', []):
                try:
                    resolve_ref(root, dict(entry, section=section))
                except (ValueError, OSError, subprocess.TimeoutExpired):
                    errors.append('source_registry_unresolved:' + ident)
        for p in proposed.get('owner_preferences', []):
            if set(p) != {'id', 'statement', 'confidence'} or not all(p.values()):
                errors.append('preference_shape_invalid')
    except (TypeError, KeyError, ValueError, AttributeError) as exc:
        errors.append('state_shape_invalid:' + type(exc).__name__)
    return result(errors, reviews, write_allowed=not errors, generation_ready=False,
                  scope='review_only_transition_unknowns_remain_nonblocking_for_audit')

def guarded_write(destination: Path, expected: bytes, proposed: bytes, root: Path) -> dict:
    """Cooperative lock + compare-before-replace. Never writes on failed checks."""
    destination = safe_path(root, str(destination.resolve().relative_to(root.resolve())))
    report = check_state(load(expected), load(proposed), root)
    if not report['write_allowed']:
        return dict(report, written=False)
    lock = destination.with_name(destination.name + '.pilot-lock')
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        return result(['writer_lock_exists'], [], written=False)
    tmp = None
    try:
        os.close(fd)
        if destination.read_bytes() != expected:
            return result(['destination_changed'], [], written=False)
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
            tmp = Path(stream.name); stream.write(proposed); stream.flush(); os.fsync(stream.fileno())
        if destination.read_bytes() != expected:
            return result(['destination_changed'], [], written=False)
        os.replace(tmp, destination); tmp = None
        return dict(report, written=True, before_sha256=digest(expected), after_sha256=digest(proposed))
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('kind', choices=('record', 'state'))
    p.add_argument('input', type=Path)
    p.add_argument('--repository', type=Path, required=True)
    p.add_argument('--previous', type=Path)
    p.add_argument('--operation', choices=('audit', 'expose', 'resume'), default='audit')
    p.add_argument('--write-to', type=Path)
    a = p.parse_args()
    try:
        raw = a.input.read_bytes(); data = load(raw, a.input.suffix)
        oldraw = a.previous.read_bytes() if a.previous else None
        old = load(oldraw, a.previous.suffix) if oldraw else None
        if a.kind == 'state':
            if old is None:
                raise ValueError('state requires --previous')
            out = guarded_write(a.write_to, oldraw, raw, a.repository) if a.write_to else check_state(old, data, a.repository)
        else:
            if a.write_to:
                raise ValueError('records are read-only')
            out = check_record(data, a.repository, a.operation, old)
    except (ValueError, OSError, yaml.YAMLError) as exc:
        out = result(['input_error:' + str(exc)], [], written=False)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    # Audit state updates may retain inherited unknowns; expose cannot.
    if out.get('written') or (a.kind == 'state' and out.get('write_allowed')):
        return 0
    return 1 if out['disposition'] == 'block' else 2 if out['disposition'] == 'review' else 0

if __name__ == '__main__':
    raise SystemExit(main())
