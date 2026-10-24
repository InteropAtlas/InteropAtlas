"""#411 evidence pilot: structural checks, never semantic/reality clearance."""
import argparse
import json
import re

REQUIRED = ('mission_value_model', 'name_job_model', 'search_landscape',
            'scheduler_state', 'generation_runtime_evidence', 'candidate_reality_evidence_links')
STAGES = ('generated', 'intrinsic', 'reality', 'exposed')

def validate(record, previous=None):
    errors, gaps = [], []
    artifacts = {}
    for item in record.get('artifacts', []):
        ident = item.get('id')
        if not ident or ident in artifacts:
            errors.append('artifact_id_invalid_or_duplicate')
        artifacts[ident] = item
        if item.get('kind') not in ('original', 'reported', 'reconstructed', 'synthetic') or not item.get('text'):
            errors.append('artifact_payload_invalid')
    def artifact(ident):
        if ident not in artifacts:
            errors.append('artifact_reference_missing')
            return {}
        return artifacts[ident]
    synthetic = record.get('record_kind') == 'synthetic'
    if record.get('record_kind') not in ('synthetic', 'live', 'reconstruction'):
        errors.append('record_kind_invalid')
    if not record.get('batches'):
        gaps.append('batches_missing')
    for item in artifacts.values():
        if not synthetic and item.get('kind') == 'synthetic':
            errors.append('synthetic_artifact_in_real_record')
        if not synthetic and item.get('kind') == 'original':
            location = ((item.get('origin') == 'local_execution' and item.get('execution_ref'))
                or item.get('source_url') or (
                re.fullmatch(r'[0-9a-f]{40}', item.get('commit', '')) and item.get('path')))
            if not location:
                gaps.append('original_source_locator_missing')
    for batch in record.get('batches', []):
        if not batch.get('batch_id') or not batch.get('method_ref') or not batch.get('runtime'):
            errors.append('batch_identity_missing')
        if batch.get('purpose') not in ('exploration', 'exploitation', 'validation'):
            errors.append('batch_purpose_invalid')
        for field in ('inputs', 'outputs'):
            if not batch.get(field):
                gaps.append(field + '_missing')
            for ident in batch.get(field, []):
                a = artifact(ident)
                if a.get('kind') != 'original' and not (synthetic and a.get('kind') == 'synthetic'):
                    gaps.append(field + '_not_original')
        stages = batch.get('stages', {})
        for stage in STAGES:
            if stage not in stages:
                gaps.append('stage_missing:' + stage)
            ids = stages.get(stage, [])
            if len(ids) != len(set(ids)):
                errors.append('duplicate_candidate_id')
        decisions = batch.get('decisions', [])
        for left, right in zip(STAGES, STAGES[1:]):
            if left not in stages or right not in stages:
                continue
            before, after = set(stages.get(left, [])), set(stages.get(right, []))
            if not after <= before:
                errors.append('candidate_added_after_generation')
            for ident in before - after:
                if not any(d.get('candidate_id') == ident and d.get('from') == left and d.get('to') == right and d.get('reason') for d in decisions):
                    errors.append('drop_reason_missing')
        for feedback in batch.get('feedback', []):
            source = artifact(feedback.get('source_artifact'))
            quote = feedback.get('quote')
            if not quote or quote not in source.get('text', ''):
                errors.append('feedback_quote_not_in_source')
            basis = feedback.get('basis')
            if basis not in ('direct_reason', 'inference', 'reported'):
                errors.append('feedback_basis_invalid')
            if source.get('kind') in ('reported', 'reconstructed') and basis != 'reported':
                errors.append('reported_feedback_promoted_to_direct')
            if not feedback.get('interpretation'):
                errors.append('feedback_interpretation_missing')
            if feedback.get('role') not in ('prefer', 'gate'):
                errors.append('feedback_role_invalid')
            if feedback.get('role') == 'gate':
                auth = feedback.get('gate_authorization_quote')
                if basis != 'direct_reason' or not auth or auth not in source.get('text', ''):
                    errors.append('gate_without_direct_authorization')
                if not synthetic and source.get('kind') != 'original':
                    errors.append('gate_source_not_original')
        for screen in batch.get('screenings', []):
            if not screen.get('claim'):
                errors.append('screen_claim_missing')
            elif screen['claim'] in ('unknown', 'not_assessed', 'error'):
                gaps.append('screen_result_unresolved')
            if 'generated' in stages and screen.get('candidate_id') not in stages['generated']:
                errors.append('screen_candidate_unknown')
            queries = screen.get('queries', [])
            if not screen.get('observed_at') or not queries or any(not all(q.get(k) for k in ('intent', 'source', 'result')) for q in queries):
                gaps.append('screen_evidence_incomplete')
            if screen.get('claim') == 'available' and not {'identity', 'public_tm', 'domain'} <= {q.get('intent') for q in queries}:
                errors.append('available_without_required_evidence')
        for ident in stages.get('exposed', []):
            screens = [s for s in batch.get('screenings', []) if s.get('candidate_id') == ident]
            if not screens:
                gaps.append('exposed_without_screen')
            for screen in screens:
                queries = screen.get('queries', [])
                if not screen.get('observed_at') or not queries or any(not all(q.get(k) for k in ('intent', 'source', 'result')) for q in queries):
                    gaps.append('screen_evidence_incomplete')
                if screen.get('claim') == 'available' and not {'identity', 'public_tm', 'domain'} <= {q.get('intent') for q in queries}:
                    errors.append('available_without_required_evidence')
        review = batch.get('batch_review', {})
        if not all(review.get(k) for k in ('assessment', 'stage_observations', 'evidence_refs')):
            gaps.append('batch_review_missing')
        for ident in review.get('evidence_refs', []):
            artifact(ident)
    recovery = record.get('recovery', {})
    for key in REQUIRED:
        item = recovery.get(key, {})
        status = item.get('status')
        if status == 'present' and item.get('value'):
            continue
        if status == 'referenced' and re.fullmatch(r'[0-9a-f]{40}', item.get('commit', '')) and item.get('path') and item.get('section'):
            continue
        if status == 'unknown' and item.get('reason'):
            gaps.append('recovery_unknown:' + key)
        else:
            errors.append('recovery_invalid:' + key)
    if previous:
        for key in previous.get('recovery', {}):
            if key not in recovery:
                errors.append('recovery_entry_dropped:' + key)
    if record.get('generation_resume_requested') and (errors or gaps or record.get('owner_paused')):
        errors.append('resume_not_ready')
    return {'errors': sorted(set(errors)), 'gaps': sorted(set(gaps)),
            'capture_complete': not errors and not gaps,
            'semantic_and_reality_clearance': 'not_assessed'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record')
    parser.add_argument('--previous')
    args = parser.parse_args()
    with open(args.record, encoding='utf-8') as stream:
        record = json.load(stream)
    previous = None
    if args.previous:
        with open(args.previous, encoding='utf-8') as stream:
            previous = json.load(stream)
    result = validate(record, previous)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['errors'] else 2 if result['gaps'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
