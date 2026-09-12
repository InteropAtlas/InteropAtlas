"""Self-contained, resumable *development* naming workflow; no ChatGPT dependency.

Frozen brief -> isolated proposals -> name-only review -> explained review ->
rejection audit -> supplied screening evidence -> substantive owner feedback.
No web searches, paid backend, IA/holdout tasks, silent retries or adoption.
"""
from __future__ import annotations
import argparse
import copy
from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import random
import re
import unicodedata
import protocol as p
import local_runner as r
import format_adapter as f
import selection_policy as selection

HERE = Path(__file__).resolve().parent
LENSES = (
    '从简报中的主体关系及个人能动性寻找表达，不将使命词语直接拼接。',
    '从简报中的变化、作用过程及可持续结果寻找间接表达。',
    '从对象需要建立的独立长期身份寻找表达，不要求裸名解释完整使命。',
)
CANDIDATE_FIELDS = ('name', 'pronunciation', 'meaning', 'derivation', 'risk')
DECISIONS = ('keep', 'hold', 'drop')


def require(ok: bool, message: str):
    if not ok:
        raise ValueError(message)


def text(value, limit=1200):
    return isinstance(value, str) and bool(value.strip()) and len(value) <= limit


def source_hashes():
    return {n: p.digest((HERE / n).read_bytes()) for n in ('workflow.py', 'protocol.py', 'local_runner.py', 'format_adapter.py', 'selection_policy.py')}


@contextmanager
def lock(root: Path):
    target = root / 'workflow.lock'
    with target.open('xb') as stream:
        stream.write(p.canonical({'created_at': r.now(), 'note': 'Never auto-break an abandoned lock; inspect pending dispatch first.'}))
    try:
        yield
    finally:
        target.unlink()


def initialize(root: Path, config: dict, task: dict, runtime: dict, method='simple',
               rounds=1, seed=91, diagnostic_preview=False):
    p.validate_config(config)
    require(task.get('record_kind') == 'synthetic' and task.get('scope') == 'method_development',
            'only_synthetic_development_tasks_not_ia_or_holdout')
    require(method in ('simple', 'redesign') and type(rounds) is int and 1 <= rounds <= 3, 'invalid_method_or_round_limit')
    require(type(seed) is int and 0 <= seed < 2**31, 'invalid_seed')
    require(config['default_mode'] == 'local_only' and not config['authorization']['paid_calls'], 'local_only_no_paid_backend')
    require(all(text(runtime.get(k)) for k in ('endpoint', 'model_id', 'revision', 'runtime_version')), 'explicit_runtime_required')
    r.endpoint(runtime['endpoint'])
    require(all(task.get('brief', {}).get(k) for k in ('object', 'mission', 'name_jobs')), 'frozen_brief_required')
    # Copy only current task data, not controller candidate history or exclusions.
    clean = {k: copy.deepcopy(task[k]) for k in ('id', 'record_kind', 'scope', 'brief')}
    clean['brief'] = {k: v for k, v in clean['brief'].items() if k in p.BRIEF_FIELDS}
    require(text(clean['id'], 80), 'task_id_required')
    c = copy.deepcopy(config)
    # Fixed per-session identity, not a license to reset a running ledger.
    nonce = p.digest(p.canonical({'task': clean, 'runtime': runtime, 'method': method, 'seed': seed, 'path': str(root.resolve())}))[:16]
    c['experiment_id'] += '-flow-' + nonce
    plan = {'schema_version': 2, 'selection_policy': selection.VERSION, 'created_at': r.now(), 'task': clean, 'config': c,
            'runtime': runtime, 'method': method, 'max_rounds': rounds, 'seed': seed,
            'diagnostic_preview_authorized': bool(diagnostic_preview), 'source_hashes': source_hashes(),
            'candidate_target': 6, 'generation_output_allowance': c['budgets']['max_output_tokens_per_call'],
            'review_output_allowance': c['budgets']['max_output_tokens_per_call'],
            'screening_freshness_days': 7,
            'execution_scope': 'synthetic_development_not_adoption',
            'runtime_controller': 'this_program_and_selected_local_model_no_external_assistant'}
    require(plan['generation_output_allowance'] >= 600, 'generation_allowance_too_small_for_this_pilot')
    root.mkdir(parents=True, exist_ok=False)
    p.write_new(root / 'plan.json', plan)
    (root / 'plan.sha256').write_text(p.digest(p.canonical(plan)), encoding='utf-8')
    return {'status': 'prepared_no_calls', 'workdir': str(root), 'cloud_calls': 0}


def load_plan(root: Path):
    plan = p.read(root / 'plan.json')
    require(p.digest(p.canonical(plan)) == (root / 'plan.sha256').read_text(), 'plan_changed_create_explicit_new_session')
    require(plan['source_hashes'] == source_hashes(), 'implementation_changed_explicit_migration_required')
    require(plan.get('selection_policy') == selection.VERSION, 'explicit_policy_migration_required')
    return plan


class LocalBackend:
    """A new stateless request per step, using the same chosen local model."""
    def __init__(self, sdk=None):
        self.sdk = sdk  # Test injection is explicitly recorded by local_runner.

    def __call__(self, root, plan, step, task, role, limit):
        prepared = root / 'prepared' / step
        spec = plan['runtime']
        if not prepared.exists():
            r.prepare(plan['config'], task, spec['endpoint'], spec['model_id'], spec['revision'],
                      spec['runtime_version'], plan['method'], role, prepared, True,
                      sdk=self.sdk, output_limit=limit, sampling_seed=plan['seed'])
        frozen = p.read(prepared / 'packet.json')
        require(frozen['max_output_tokens'] == limit, 'cached_output_allowance_changed')
        # The model and loaded configuration must stay fixed across the workflow.
        binding = {'profile': frozen['profile_fingerprint'],
                   'observed': p.read(prepared / 'config.json')['local_transport']['observed_model']}
        bp = root / 'runtime-binding.json'
        if bp.exists():
            require(p.read(bp) == binding, 'runtime_changed_within_workflow')
        else:
            p.write_new(bp, binding)
        run_root = root / 'calls'
        record_path = run_root / step / 'record.json'
        if not record_path.exists():
            # Existing ambiguous run directory is refused by run(), not resent.
            r.run(prepared, run_root, step, execute=True)
        record = p.read(record_path)
        require(record['receipt']['outcome'] == 'completed' and not record['violations'], 'transport_not_completed:' + step)
        raw = (record_path.parent / 'output.txt').read_bytes()
        require(p.digest(raw) == record['output_sha256'], 'raw_output_changed')
        return raw, str(record_path.relative_to(root)), record['receipt']['execution_kind']


def json_answer(raw: bytes):
    body = raw.decode('utf-8').strip()
    if body.startswith('```json\n') and body.endswith('\n```'):
        body = body[8:-4]
    value = json.loads(body, object_pairs_hook=p.unique,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite_json')))
    require(isinstance(value, dict), 'model_must_return_one_json_object')
    return value


def step_call(root, plan, step, question, role, limit, backend, instruction=''):
    task = copy.deepcopy(plan['task'])
    task.update(question=question, materials=[], requires_independent_context=True)
    if instruction:
        task['materials'] = [{'text': instruction, 'source_ref': 'owner-feedback:next_instruction', 'permitted_roles': [role]}]
    directory = root / 'steps' / step
    directory.mkdir(parents=True, exist_ok=True)
    expected = {'task': task, 'role': role, 'limit': limit}
    ip = directory / 'input.json'
    if ip.exists():
        require(p.read(ip) == expected, 'step_input_changed')
    else:
        p.write_new(ip, expected)
    op = directory / 'parsed.json'
    if op.exists():
        saved = p.read(op)
        require(p.digest((directory / 'answer.raw').read_bytes()) == saved['raw_sha256'], 'cached_answer_changed')
        normalized = normalized_answer(directory, (directory / 'answer.raw').read_bytes(), question)
        return json_answer(normalized)
    raw, execution_ref, execution_kind = backend(root, plan, step, task, role, limit)
    raw_path = directory / 'answer.raw'
    if raw_path.exists():
        require(raw_path.read_bytes() == raw, 'raw_answer_conflict')
    else:
        with raw_path.open('xb') as stream:
            stream.write(raw)
    normalized = normalized_answer(directory, raw, question)
    parsed = json_answer(normalized)  # No semantic repairs or automatic model retries.
    p.write_new(op, {'raw_sha256': p.digest(raw), 'execution_ref': execution_ref,
                    'execution_kind': execution_kind})
    return parsed


def candidates(answer, maximum):
    rows = answer.get('candidates')
    require(isinstance(rows, list) and 0 < len(rows) <= maximum, 'candidate_count_invalid')
    for row in rows:
        require(isinstance(row, dict) and set(row) == set(CANDIDATE_FIELDS), 'candidate_fields_invalid')
        for key in CANDIDATE_FIELDS:
            require(text(row[key], 80 if key in ('name', 'pronunciation') else 400), 'candidate_text_invalid:' + key)
    return rows


def reviews(answer, ids):
    rows = answer.get('reviews')
    require(isinstance(rows, list) and len(rows) == len(ids), 'review_coverage_incomplete')
    require(all(isinstance(v, dict) for v in rows), 'review_object_required')
    require(len({v.get('id') for v in rows}) == len(ids) and {v.get('id') for v in rows} == set(ids), 'review_ids_changed_or_duplicated')
    for row in rows:
        require(set(row) == {'id', 'decision', 'reason'} and row['decision'] in DECISIONS and text(row['reason']), 'review_fields_invalid')
    return rows


def normalized_answer(directory, raw, question):
    normalized, audit = f.normalize(raw, json.loads(question))
    target = directory / 'normalization.json'
    if target.exists():
        require(p.read(target) == audit, 'normalization_audit_changed')
    else:
        p.write_new(target, audit)
    if audit['action'].startswith('refused_'):
        raise ValueError(audit['action'])
    if audit['changed']:
        target = directory / 'normalized-answer.json'
        if target.exists():
            require(target.read_bytes() == normalized, 'normalized_answer_changed')
        else:
            with target.open('xb') as stream:
                stream.write(normalized)
    return normalized


def review_question(stage, rows):
    return selection.review_question(stage, rows)

def compute_round(root, plan, round_no, backend, instruction=''):
    prefix = 'r' + str(round_no)
    count = plan['candidate_target']
    routes = LENSES if plan['method'] == 'redesign' else ('根据完整简报直接探索不同表达，独立形成有价值的候选；不限定构词法。',)
    all_rows = []
    total = plan['generation_output_allowance']
    for index, route in enumerate(routes):
        n = count // len(routes)
        limit = total // len(routes) + (index < total % len(routes))
        question = p.canonical({'stage': 'proposal', 'exploration_question': route, 'maximum_candidates': n,
            'output_contract': {'candidates': [{k: '非空字符串' for k in CANDIDATE_FIELDS}]},
            'limits': '只返回JSON。不编造词源，不预测可注册性，不排名。允许少于上限，不凑数。'}).decode()
        answer = step_call(root, plan, prefix + 'g' + str(index + 1), question, 'generate', limit, backend, instruction)
        all_rows.extend(candidates(answer, n))
    seen, pool, duplicate_count = set(), [], 0
    random.Random(plan['seed'] + round_no).shuffle(all_rows)
    for row in all_rows:
        norm = unicodedata.normalize('NFKC', row['name']).strip().casefold()
        if norm in seen:
            duplicate_count += 1
            continue
        seen.add(norm)
        pool.append(dict(row, id='C' + str(len(pool) + 1).zfill(3)))
    ids = [v['id'] for v in pool]
    # First call genuinely has no pronunciation/meaning/rationale or route labels.
    surface_items = [{'id': v['id'], 'name': v['name']} for v in pool]
    surface = reviews(step_call(root, plan, prefix + 'surface', review_question('name_only', surface_items),
                               'select', plan['review_output_allowance'], backend), ids)
    explained = reviews(step_call(root, plan, prefix + 'explained', review_question('with_explanation', pool),
                                 'select', plan['review_output_allowance'], backend), ids)
    dropped = [v['id'] for v in explained if v['decision'] == 'drop']
    # No cardinal scores: a deterministic boundary proxy plus a random rejected item.
    boundary = [v['id'] for v in surface if v['decision'] != 'drop' and v['id'] in dropped]
    sampled = (boundary or dropped)[:1]
    rest = [v for v in dropped if v not in sampled]
    if rest:
        sampled += random.Random(plan['seed'] + 1000 + round_no).sample(rest, 1)
    audit = []
    if sampled:
        selected = [v for v in pool if v['id'] in sampled]
        audit = reviews(step_call(root, plan, prefix + 'audit', review_question('independent_recheck', selected),
                                  'select', plan['review_output_allowance'], backend), sampled)
    disputed = {v['id'] for v in audit if v['decision'] != 'drop'}
    kept = [v['id'] for v in explained if v['decision'] != 'drop' or v['id'] in disputed]
    result = {'round': round_no, 'pool': pool, 'surface': surface, 'explained': explained,
              'audit': audit, 'rejected_sample_ids': sampled, 'audit_disagreement_ids': sorted(disputed),
              'intrinsic_shortlist_ids': kept, 'exact_duplicates_removed': duplicate_count,
              'review_independence': 'separate_requests_same_model_not_independent_expert',
              'semantic_truth': 'not_programmatically_verified', 'reality_clearance': 'not_assessed'}
    result.update(selection.resource_queues(result))
    result['unverified_inquiries'] = selection.inquiry_register(pool)
    rp = root / ('round-' + str(round_no) + '.json')
    if rp.exists():
        require(p.read(rp) == result, 'round_projection_changed')
    else:
        p.write_new(rp, result)
    return result


def screening_status(root, plan, result, report=None):
    if report is None:
        paths = sorted(root.glob('screening-' + str(result['round']) + '-*.json'))
        if not paths:
            return [], list(result['screening_queue_ids'])
        report = p.read(paths[-1])
    require(report.get('round_digest') == p.digest(p.canonical(result)), 'screening_from_different_round')
    rows = report.get('items')
    require(isinstance(rows, list), 'screening_items_required')
    allowed, unresolved, seen = [], [], set()
    for row in rows:
        ident = row.get('id')
        require(ident in result['intrinsic_shortlist_ids'] and ident not in seen, 'screening_candidate_invalid')
        seen.add(ident)
        require(row.get('status') in ('pass', 'unknown', 'conflict'), 'invalid_screening_status')
        evidence = row.get('evidence', [])
        require(isinstance(evidence, list), 'evidence_list_required')
        verified = bool(evidence)
        for source in evidence:
            require(text(source.get('source_ref')) and text(source.get('file')), 'evidence_locator_required')
            target = (root / source['file']).resolve()
            require(target.is_relative_to(root.resolve()) and target.is_file(), 'evidence_must_be_local_file_inside_workdir')
            require(p.digest(target.read_bytes()) == source.get('sha256'), 'evidence_digest_mismatch')
            at = p.stamp(source['checked_at'])
            age = (datetime.now(timezone.utc) - at).total_seconds()
            verified = verified and 0 <= age <= plan['screening_freshness_days'] * 86400
        # Only checks supplied evidence identity/freshness, not its truth or legal scope.
        if ident in result['priority_ids'] and row['status'] == 'pass' and verified and text(row.get('reviewer_ref')) and text(row.get('scope')):
            allowed.append(ident)
        else:
            unresolved.append(ident)
    return allowed, sorted(set(unresolved) | (set(result['screening_queue_ids']) - seen))


def summarize_calls(root):
    records = [p.read(path) for path in sorted((root / 'calls').glob('*/record.json'))]
    costs = {}
    for key in ('cloud_spend', 'setup_spend', 'owner_minutes', 'local_seconds'):
        vals = [v['receipt']['costs'][key] for v in records]
        costs[key] = {'known_sum': sum(v for v in vals if v is not None), 'unknown_count': sum(v is None for v in vals)}
    return {'recorded_attempts': len(records), 'completed': sum(v['receipt']['outcome'] == 'completed' for v in records),
            'real_service_attempts': sum(v['receipt']['execution_kind'] != 'mock_transport_test' for v in records),
            'mock_attempts': sum(v['receipt']['execution_kind'] == 'mock_transport_test' for v in records),
            'pending_without_receipt': len(list((root / 'calls').glob('*/dispatch-intent.json'))) - len(records),
            'costs_including_failed_and_synthetic_task_attempts': costs,
            'naming_effectiveness': 'not_assessed', 'actual_adoption': 'not_assessed'}


def validate_feedback(plan, result, allowed, feedback):
    require(feedback.get('round_digest') == p.digest(p.canonical(result)), 'feedback_from_different_round')
    require(text(feedback.get('source_ref')) and text(feedback.get('verbatim')), 'feedback_source_and_verbatim_required')
    require(feedback.get('action') in ('continue_search', 'stop', 'accept_for_research'), 'unsupported_feedback_action')
    targets = feedback.get('candidate_ids', [])
    require(isinstance(targets, list) and all(isinstance(v, str) for v in targets)
            and len(set(targets)) == len(targets), 'invalid_feedback_ids')
    permitted = result['intrinsic_shortlist_ids'] if plan['diagnostic_preview_authorized'] else allowed
    require(set(targets) <= set(permitted), 'feedback_targets_not_exposed')
    patch = feedback.get('brief_patch', {})
    require(isinstance(patch, dict) and set(patch) <= {'mission', 'name_jobs', 'non_jobs', 'confirmed_preferences'}, 'brief_patch_cannot_change_object_or_constraints')
    if patch:
        require(feedback.get('brief_change_authorized') is True and feedback['action'] == 'continue_search', 'brief_change_needs_explicit_feedback_authority')
        require(all(isinstance(v, (str, list)) and bool(v) for v in patch.values()), 'brief_patch_values_invalid')
    if feedback['action'] == 'continue_search':
        require(text(feedback.get('next_instruction')), 'explicit_next_instruction_required_no_invented_preference_reason')
    if feedback['action'] == 'accept_for_research':
        require(bool(targets), 'research_acceptance_requires_visible_target')


def _advance(root: Path, execute=False, backend=None):
    require(execute, 'explicit_execute_required')
    plan = load_plan(root)
    backend = backend or LocalBackend()
    with lock(root):
        instruction = ''
        round_plan = copy.deepcopy(plan)
        for round_no in range(1, plan['max_rounds'] + 1):
            result = compute_round(root, round_plan, round_no, backend, instruction)
            allowed, unknown = screening_status(root, plan, result)
            fp = root / ('feedback-' + str(round_no) + '.json')
            if fp.exists():
                feedback = p.read(fp)
                validate_feedback(plan, result, allowed, feedback)
                if feedback['action'] == 'continue_search':
                    require(text(feedback.get('next_instruction')), 'explicit_next_instruction_required_no_invented_preference_reason')
                    instruction = feedback['next_instruction']
                    round_plan['task']['brief'].update(copy.deepcopy(feedback.get('brief_patch', {})))
                    if round_no < plan['max_rounds']:
                        continue
                    status = 'round_budget_exhausted'
                else:
                    status = 'stopped' if feedback['action'] == 'stop' else 'research_review_complete_not_adoption'
            else:
                status = ('awaiting_owner_feedback' if allowed or plan['diagnostic_preview_authorized']
                          else 'awaiting_screening_evidence' if result['priority_ids'] else 'awaiting_substantive_hold_resolution' if result['hold_ids'] else 'no_intrinsic_survivor')
            visible = result['intrinsic_shortlist_ids'] if plan['diagnostic_preview_authorized'] else allowed
            summary = {'status': status, 'round': round_no, 'round_digest': p.digest(p.canonical(result)),
                'diagnostic_only': plan['diagnostic_preview_authorized'],
                'display': [dict(v, intrinsic_decision=next(x['decision'] for x in result['explained'] if x['id'] == v['id']),
                    audit_disagreement=v['id'] in result['audit_disagreement_ids']) for v in result['pool'] if v['id'] in visible],
                'priority_ids': result['priority_ids'], 'hold_ids': result['hold_ids'],
                'not_pursued_ids': result['not_pursued_ids'],
                'unresolved_screening_ids': unknown, 'costs': summarize_calls(root),
                'next_step_owner_dependency': 'substantive_feedback_or_evidence_only_not_external_assistant',
                'limits': 'Synthetic development; supplied screening requires semantic verification; no adoption or method efficacy claim.'}
            # A replaceable report is a projection, never original evidence.
            (root / 'report.json').write_bytes(p.canonical(summary))
            return summary
    raise ValueError('no_round_executed')


def advance(root: Path, execute=False, backend=None):
    try:
        return _advance(root, execute, backend)
    except (OSError, ValueError, KeyError, TypeError, ImportError) as error:
        if root.exists() and not (root / 'workflow.lock').exists():
            path = root / 'report.json'
            prior = p.read(path) if path.exists() else {}
            projection = {k: prior[k] for k in ('round', 'round_digest') if k in prior}
            projection.update(status='blocked', error=str(error), display=[], automatic_retry=False,
                              costs=summarize_calls(root))
            path.write_bytes(p.canonical(projection))
        raise


def attach(root: Path, kind: str, file: Path):
    require(kind in ('feedback', 'screening'), 'unknown_attachment_kind')
    plan = load_plan(root)
    with lock(root):
        report = p.read(root / 'report.json')
        value = p.read(file)
        result = p.read(root / ('round-' + str(report['round']) + '.json'))
        require(value.get('round_digest') == report['round_digest'], 'attachment_must_reference_current_round_digest')
        if kind == 'screening':
            screening_status(root, plan, result, value)
            revision = len(list(root.glob('screening-' + str(report['round']) + '-*.json'))) + 1
            target = root / ('screening-' + str(report['round']) + '-' + str(revision).zfill(4) + '.json')
        else:
            allowed, _ = screening_status(root, plan, result)
            validate_feedback(plan, result, allowed, value)
            target = root / ('feedback-' + str(report['round']) + '.json')
        p.write_new(target, value)
    return {'status': kind + '_recorded_not_yet_accepted', 'model_calls': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    q = sub.add_parser('init')
    for key in ('config', 'task', 'workdir'):
        q.add_argument('--' + key, type=Path, required=True)
    for key in ('endpoint', 'model', 'revision', 'runtime-version'):
        q.add_argument('--' + key, required=True)
    q.add_argument('--method', choices=('simple', 'redesign'), default='simple')
    q.add_argument('--rounds', type=int, default=1)
    q.add_argument('--seed', type=int, default=91)
    q.add_argument('--diagnostic-preview-authorized', action='store_true')
    q = sub.add_parser('advance'); q.add_argument('--workdir', type=Path, required=True); q.add_argument('--execute', action='store_true')
    for command in ('feedback', 'screening'):
        q = sub.add_parser(command); q.add_argument('--workdir', type=Path, required=True); q.add_argument('--file', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'init':
            result = initialize(args.workdir, p.read(args.config), p.read(args.task),
                {'endpoint': args.endpoint, 'model_id': args.model, 'revision': args.revision,
                 'runtime_version': args.runtime_version}, args.method, args.rounds, args.seed,
                args.diagnostic_preview_authorized)
        elif args.command == 'advance':
            result = advance(args.workdir, args.execute)
        else:
            result = attach(args.workdir, args.command, args.file)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, ImportError) as error:
        print(json.dumps({'status': 'blocked', 'error': str(error), 'automatic_retry': False}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
