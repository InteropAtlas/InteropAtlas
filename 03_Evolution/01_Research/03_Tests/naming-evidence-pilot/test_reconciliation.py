"""#411 v86 task-local source/recovery checks; never naming-effectiveness tests.

Run with full repository history. An optional cached v85 directory may contain
state-v85.yaml when network-isolated; its bytes must match the pinned Git blob.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import yaml
from validate_evidence import validate

BASE = 'd4aaf5d773dee7d25459cc90e36cb98d437ba5ad'
HISTORY = '10125cb04dcbe4270230f3ba7db45f039c7a7330'
STATE = '03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml'
BASE_BLOB = '9e4aaea32de7053b64bbdb72cf2821686e7154a0'

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result:
            raise ValueError('duplicate YAML key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', type=Path, required=True)
    parser.add_argument('--cached-v85', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = args.repository.resolve()
    pilot = root / Path(STATE).parent / 'naming-evidence-pilot'
    checks = []

    def git(*parts):
        return subprocess.check_output(['git', '-C', str(root), *parts])

    def read(ref, path):
        result = subprocess.run(['git', '-C', str(root), 'show', ref + ':' + path], capture_output=True)
        if result.returncode == 0:
            return result.stdout
        if ref == BASE and path == STATE and args.cached_v85:
            data = (args.cached_v85 / 'state-v85.yaml').read_bytes()
            if blob_sha(data) != BASE_BLOB:
                raise ValueError('Cached baseline does not match the verified v85 blob')
            return data
        raise RuntimeError(result.stderr.decode())

    def check(name, passed):
        checks.append({'check': name, 'passed': bool(passed)})
        if not passed:
            raise AssertionError(name)

    before = yaml.load(read(BASE, STATE), Loader=UniqueLoader)
    current_bytes = (root / STATE).read_bytes()
    current = yaml.load(current_bytes, Loader=UniqueLoader)
    record_bytes = (pilot / 'rnd130-reconstruction.json').read_bytes()
    record = json.loads(record_bytes)
    previous = json.loads(read(HISTORY, str(Path(STATE).parent / 'naming-evidence-pilot/rnd130-reconstruction.json')))
    check('same_job_v86_skill040', current['task'] == dict(before['task'], snapshot_version=86))
    check('paused_and_no_resume_permission', current['process_review']['generation_paused'] and not current['audit_recovery']['generation_resume_readiness'] and not record['generation_resume_requested'] and record['owner_paused'])
    check('candidate_preference_constraint_values_unchanged', all(current[k] == before[k] for k in ('candidates', 'owner_preferences', 'constraint_registry', 'mission_value_model', 'name_job_model', 'decision_criteria')))
    check('four_unknown_state_fields_retained', current['audit_recovery']['missing_current_state'] == before['audit_recovery']['missing_current_state'])
    check('no_new_original_generation_artifacts', record['record_kind'] == 'reconstruction' and all(a['kind'] in ('reported', 'reconstructed') for a in record['artifacts']))
    batch = record['batches'][0]
    check('same_reported_seven_exposed_ids', batch['stages'] == previous['batches'][0]['stages'])
    check('feedback_not_promoted_to_direct', all(f['basis'] == 'reported' and f['role'] != 'gate' for f in batch['feedback']))
    sources = record['reconciliation']['source_registry']
    loaded = {}
    for ident, source in sources.items():
        raw = read(source['commit'], source['path'])
        check('source_blob_' + ident, blob_sha(raw) == source['blob'])
        loaded[ident] = yaml.load(raw, Loader=UniqueLoader)
    check('scheduler_field_loss_and_surrogate', all(k in loaded['SCHED50'] and k not in loaded['DROP51'] for k in ('workflow_scheduler', 'method_scheduler')) and 'search_control' in loaded['DROP51'])
    check('landscape_last_dedicated_field_loss', 'search_landscape' in loaded['LAND61'] and 'search_landscape' not in loaded['DROP62'])
    check('portfolio_loss_adjacent_to_rnd130', 'morphotype_portfolio' in loaded['POLICY79'] and 'morphotype_portfolio' not in loaded['BATCH80'])
    check('reported_screening_matrix_exact', all(any(c['id'] == item['candidate_id'] and c['domain_status']['com'] == item['reported_com'] and c['domain_status']['org'] == item['reported_org'] and c['reality_status'] == item['reported_identity'] for c in loaded['BATCH80']['candidates']) for item in record['reconciliation']['reported_candidate_screening']))
    check('n143_conflict_unresolved', current['audit_recovery']['known_inconsistency'] == before['audit_recovery']['known_inconsistency'] and record['reconciliation']['screening_conflict']['resolution'].startswith('unresolved'))
    check('recovery_refs_current_not_original_input', all(record['recovery'][key]['status'] == 'referenced' and record['recovery'][key]['commit'] == BASE for key in ('mission_value_model', 'name_job_model')))
    result = validate(record, previous)
    check('expected_incomplete_not_false_pass', not result['errors'] and not result['capture_complete'] and len(result['gaps']) == 10)
    requested = copy.deepcopy(record)
    requested['generation_resume_requested'] = True
    check('resume_request_rejected', 'resume_not_ready' in validate(requested, previous)['errors'])
    check('ci_not_claimed_as_naming_validation', record['reconciliation']['ci_check']['run_count'] == 2 and record['reconciliation']['ci_check']['artifact_outcome'] == 'PASS + SEMANTIC REVIEW REQUIRED')
    check('next_step_synthetic_not_historical_replay', current['next_action']['action'] == 'design_and_run_anonymous_synthetic_control_cases_no_new_names' and not current['evidence_reconciliation']['historical_exact_replay_ready'])
    check('stable_skill_file_unchanged', git('show', HISTORY + ':02_Runtime/02_Tools/adaptive_naming/SKILL.md') == (root / '02_Runtime/02_Tools/adaptive_naming/SKILL.md').read_bytes())
    result['reconciliation_validation'] = {
        'kind': 'source_and_state_structural_self_check_not_independent_review',
        'passed': sum(c['passed'] for c in checks), 'total': len(checks), 'checks': checks,
        'record_sha256': hashlib.sha256(record_bytes).hexdigest(),
        'state_sha256': hashlib.sha256(current_bytes).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits': 'No original replay, no new names, no current reality clearance, no causal/method-effectiveness validation.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': len(checks), 'capture_complete': result['capture_complete'], 'gaps': result['gaps']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
