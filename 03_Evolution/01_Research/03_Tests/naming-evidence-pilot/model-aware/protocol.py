"""Offline model-aware experiment protocol. No model calls or semantic clearance.

Only model_input is sent to a future execution adapter; envelope metadata stays
with the controller. Preflight is advisory until an adapter enforces it; it does
not reserve a shared budget. Never import synthetic receipts as model evidence.
"""
from __future__ import annotations
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import random
from typing import Any

ROLES = ('generate', 'select', 'extract')
BRIEF_FIELDS = ('object', 'mission', 'name_jobs', 'non_jobs', 'constraints', 'confirmed_preferences')
PROFILE_FIELDS = ('deployment_id', 'revision', 'quantization', 'runtime_version',
                  'context_limit_tokens', 'token_counter', 'reasoning_mode', 'sampling',
                  'execution_location', 'billing')
ROLE_PROMPTS = {
    'generate': '只完成本次提案。输出候选、读音、实际构词依据和风险；不排名、不预测现实可用性，不修改偏好或任务边界。',
    'select': '只比较给定候选。先记录名称本身的读写/身份判断，再查看等长解释；保留不确定、并列与淘汰理由，不生成新名称，不推测方案来源。',
    'extract': '只从所给材料提取事实、原文及其出处；没有记录的值为unknown。不得把搜索未命中或模型记忆当成现实许可。',
}

def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n').encode()

def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result

def read(path: Path) -> dict:
    value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique,
                       parse_constant=lambda _: (_ for _ in ()).throw(ValueError('non-finite JSON number')))
    if not isinstance(value, dict):
        raise ValueError('top-level object required')
    return value

def write_new(path: Path, value: dict) -> None:
    payload = canonical(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation: do not replace an earlier evidence file or symlink.
    with path.open('xb') as stream:
        stream.write(payload)

def number(value: Any, integer: bool = False) -> bool:
    return type(value) in ((int,) if integer else (int, float)) and math.isfinite(value) and value >= 0

def stamp(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('timezone required')
    return dt

def validate_config(config: dict) -> None:
    if config.get('schema_version') != 1:
        raise ValueError('unsupported experiment schema')
    if config.get('default_mode') not in ('local_only', 'hybrid', 'reference'):
        raise ValueError('invalid run mode')
    for key in ('model_trials', 'ia_naming', 'paid_calls', 'diagnostic_untested_roles'):
        if type(config.get('authorization', {}).get(key)) is not bool:
            raise ValueError('explicit boolean authority required: ' + key)
    budget = config['budgets']
    for key in ('max_calls', 'max_cloud_calls', 'max_output_tokens_total',
                'max_output_tokens_per_call', 'max_attempts_per_packet'):
        if not number(budget.get(key), True):
            raise ValueError('invalid budget: ' + key)
    if not number(budget.get('max_cloud_spend')) or not budget.get('currency'):
        raise ValueError('invalid monetary cap/currency')
    for slot in ('local', 'reference'):
        if slot not in config.get('profiles', {}):
            raise ValueError('both model profile slots must be explicit')

def fingerprint(profile: dict) -> dict:
    return {key: copy.deepcopy(profile.get(key)) for key in PROFILE_FIELDS}

def packet(config: dict, task: dict, profile: str, method: str, role: str) -> dict:
    validate_config(config)
    if profile not in config['profiles'] or role not in ROLES:
        raise ValueError('unknown profile or role')
    if method not in ('simple', 'redesign'):
        raise ValueError('legacy uses the full pinned original workflow, not a reduced packet adapter')
    if task.get('record_kind') not in ('real', 'synthetic') or not task.get('id'):
        raise ValueError('task id and explicit real/synthetic kind required')
    if task.get('scope') not in ('method_development', 'method_holdout', 'ia_current'):
        raise ValueError('explicit task scope required')
    brief = task.get('brief', {})
    if not all(brief.get(key) for key in ('object', 'mission', 'name_jobs')):
        raise ValueError('object, mission and name_jobs must be supplied from task sources')
    # Deliberate whitelist: no entire state, candidate history, exclusions or rankings.
    clean = {key: copy.deepcopy(brief[key]) for key in BRIEF_FIELDS if key in brief}
    materials = []
    for item in task.get('materials', []):
        if role in item.get('permitted_roles', []):
            if not item.get('text') or not item.get('source_ref'):
                raise ValueError('material text and source are required')
            materials.append({key: item[key] for key in ('text', 'source_ref')})
    if not task.get('question'):
        raise ValueError('one task question required')
    model_input = {'brief': clean, 'question': task['question'], 'materials': materials,
                   'instruction': ROLE_PROMPTS[role],
                   'stop': '只完成当前任务，不调用工具、不追加轮次；缺少依据明确为unknown。'}
    if role == 'generate' and method == 'redesign':
        model_input['proposal_contract'] = '本提案独立形成，围绕本轮身份/材料问题探索；不读取其他路线的候选与排名。'
    profile_data = config['profiles'][profile]
    return {'schema_version': 1, 'experiment_id': config['experiment_id'],
            'created_at': datetime.now(timezone.utc).isoformat(), 'task_id': task['id'],
            'record_kind': task['record_kind'], 'scope': task['scope'], 'role': role,
            'method': method, 'profile': profile, 'model_input': model_input,
            'input_sha256': digest(canonical(model_input)),
            'profile_fingerprint': fingerprint(profile_data),
            'context': copy.deepcopy(task.get('context', {'actual_level': 'unknown'})),
            'input_tokens': task.get('input_tokens'), 'token_counter': task.get('token_counter'),
            'requires_independent_context': task.get('requires_independent_context', False),
            'max_output_tokens': config['budgets']['max_output_tokens_per_call'],
            'estimated_cost_upper_bound': task.get('estimated_cost_upper_bound'),
            'cost_currency': task.get('cost_currency', config['budgets']['currency']),
            'adapter_status': 'offline_packet_only_not_executed',
            'semantic_review': 'not_assessed'}

def preflight(config: dict, request: dict, usage: dict) -> dict:
    validate_config(config)
    reasons = []
    auth, budget = config['authorization'], config['budgets']
    slot, role = request.get('profile'), request.get('role')
    if slot not in config['profiles'] or role not in ROLES:
        raise ValueError('request profile/role missing')
    model = config['profiles'][slot]
    if request.get('schema_version') != 1 or request.get('record_kind') not in ('real', 'synthetic') or request.get('scope') not in ('method_development', 'method_holdout', 'ia_current') or request.get('method') not in ('simple', 'redesign'):
        raise ValueError('invalid request identity/kind/scope/method')
    if request.get('experiment_id') != config['experiment_id']:
        reasons.append('wrong_experiment')
    if request.get('input_sha256') != digest(canonical(request.get('model_input'))):
        reasons.append('input_bytes_changed')
    if request.get('profile_fingerprint') != fingerprint(model):
        reasons.append('runtime_changed_rebuild_packet')
    if not auth['model_trials']:
        reasons.append('model_trial_not_authorized')
    if request.get('scope') == 'ia_current' and not auth['ia_naming']:
        reasons.append('ia_naming_paused')
    if request.get('scope') == 'method_holdout' and (not config['comparison']['holdout_enabled'] or not config['comparison']['freeze_ref']):
        reasons.append('holdout_not_frozen')
    required = ('deployment_id', 'revision', 'quantization', 'runtime_version', 'token_counter', 'reasoning_mode')
    if model.get('identity_verified') is not True or any(not model.get(k) for k in required) or not isinstance(model.get('sampling'), dict) or not model['sampling']:
        reasons.append('exact_model_configuration_unresolved')
    role_status = model.get('roles', {}).get(role, 'untested')
    if role_status != 'passed' and not (role_status == 'untested' and auth['diagnostic_untested_roles']):
        reasons.append('role_not_validated_or_diagnostic_not_authorized')
    input_tokens, output_limit = request.get('input_tokens'), request.get('max_output_tokens')
    context_limit = model.get('context_limit_tokens')
    if not number(input_tokens, True) or request.get('token_counter') != model.get('token_counter'):
        reasons.append('verified_token_count_required_no_character_proxy')
    elif not number(context_limit, True) or not number(output_limit, True) or input_tokens + output_limit > context_limit:
        reasons.append('context_limit_exceeded_or_unknown')
    if not number(output_limit, True) or not 0 < output_limit <= budget['max_output_tokens_per_call']:
        reasons.append('invalid_output_limit')
    context = request.get('context', {})
    actual = context.get('actual_level')
    if actual not in ('same_context', 'fresh_context', 'isolated_runtime'):
        reasons.append('actual_context_unknown')
    if actual in ('fresh_context', 'isolated_runtime') and not context.get('evidence_ref'):
        reasons.append('isolation_claim_without_evidence')
    if request.get('requires_independent_context') and actual not in ('fresh_context', 'isolated_runtime'):
        reasons.append('required_separation_not_available')
    for key in ('calls', 'cloud_calls', 'output_tokens', 'packet_attempts'):
        if not number(usage.get(key), True):
            raise ValueError('known nonnegative usage required: ' + key)
    if usage['calls'] >= budget['max_calls'] or usage['packet_attempts'] >= budget['max_attempts_per_packet']:
        reasons.append('call_or_retry_budget_exhausted')
    if number(output_limit, True) and usage['output_tokens'] + output_limit > budget['max_output_tokens_total']:
        reasons.append('output_budget_exhausted')
    location, billing = model.get('execution_location'), model.get('billing')
    if location not in ('local', 'cloud') or billing not in ('unmetered_local', 'metered'):
        reasons.append('execution_location_or_billing_unknown')
    if config['default_mode'] == 'local_only' and location != 'local':
        reasons.append('local_only_forbids_cloud')
    if billing == 'metered' or location == 'cloud':
        if not auth['paid_calls']:
            reasons.append('paid_upgrade_disabled')
        estimate, spent = request.get('estimated_cost_upper_bound'), usage.get('cloud_spend')
        if request.get('cost_currency') != budget['currency']:
            reasons.append('currency_mismatch')
        if not number(estimate) or not number(spent):
            reasons.append('unknown_cost_blocks_paid_call')
        elif spent + estimate > budget['max_cloud_spend']:
            reasons.append('cloud_money_cap')
        if usage['cloud_calls'] >= budget['max_cloud_calls']:
            reasons.append('cloud_call_cap')
    return {'dispatch_allowed': not reasons, 'blockers': sorted(set(reasons)),
            'role_support_claim': role_status, 'model_executed': False,
            'automatic_upgrade': False, 'budget_reserved': False,
            'limits': 'Checks declared configuration, not runtime truth; no shared-budget reservation or model call.'}

def matrix(config: dict) -> dict:
    validate_config(config)
    comp = config['comparison']
    if not number(comp.get('repeats'), True) or comp['repeats'] == 0:
        raise ValueError('positive repeats required')
    tasks = comp['task_slots']
    if len({t['id'] for t in tasks}) != len(tasks):
        raise ValueError('task id reused across splits')
    cells = []
    for task in tasks:
        for method in comp['methods']:
            for tier in comp['tiers']:
                for repeat in range(1, comp['repeats'] + 1):
                    cells.append({'task_id': task['id'], 'split': task['split'],
                                  'method': method, 'tier': tier, 'repeat': repeat,
                                  'core': method in comp['core_methods'], 'status': 'not_run',
                                  'brief_bound': bool(task['brief_ref']), 'owner_bound': bool(task['owner_ref'])})
    random.Random(comp['seed']).shuffle(cells)
    return {'experiment_id': config['experiment_id'], 'unit': 'task', 'cells': cells,
            'real_runs': 0, 'results': [], 'limits': 'Planned slots, not subjects recruited or sample-power evidence.'}

def capture(request: dict, raw: bytes, receipt: dict) -> dict:
    """Retain failures/violations rather than censoring them from cost reports."""
    if receipt.get('record_kind') not in ('real', 'synthetic') or receipt['record_kind'] != request.get('record_kind'):
        raise ValueError('real/synthetic mismatch')
    if not receipt.get('run_id') or not receipt.get('execution_ref'):
        raise ValueError('run identity and observable execution reference required')
    if receipt.get('outcome') not in ('completed', 'failed', 'cancelled', 'invalid_output'):
        raise ValueError('explicit outcome required')
    start, end = stamp(receipt['started_at']), stamp(receipt['ended_at'])
    if end < start:
        raise ValueError('negative duration')
    violations = []
    if request.get('input_sha256') != digest(canonical(request.get('model_input'))):
        violations.append('input_bytes_changed')
    if start < stamp(request['created_at']):
        violations.append('run_predates_packet')
    if receipt.get('runtime_fingerprint') != request['profile_fingerprint']:
        violations.append('runtime_fingerprint_mismatch')
    if receipt['outcome'] == 'completed' and not raw.strip():
        violations.append('empty_completed_output')
    for key in ('input_tokens', 'output_tokens'):
        if receipt.get(key) is not None and not number(receipt[key], True):
            raise ValueError('invalid token metric')
    if number(receipt.get('output_tokens'), True) and receipt['output_tokens'] > request['max_output_tokens']:
        violations.append('observed_output_budget_exceeded')
    cost = receipt.get('costs', {})
    for key in ('cloud_spend', 'setup_spend', 'owner_minutes', 'local_seconds'):
        if key not in cost or (cost[key] is not None and not number(cost[key])):
            raise ValueError('explicit number or null cost required: ' + key)
    if not cost.get('currency'):
        raise ValueError('cost currency required')
    if receipt['record_kind'] == 'real' and not receipt.get('dispatch_evidence_ref'):
        violations.append('dispatch_evidence_missing')
    return {'run_id': receipt['run_id'], 'record_kind': receipt['record_kind'],
            'task_id': request['task_id'], 'method': request['method'], 'profile': request['profile'],
            'input_sha256': request['input_sha256'], 'output_sha256': digest(raw),
            'raw_output': raw.decode('utf-8'), 'receipt': copy.deepcopy(receipt),
            'violations': violations, 'execution_seconds': (end - start).total_seconds(),
            'semantic_and_reality_clearance': 'not_assessed',
            'method_effectiveness': 'not_assessed'}

def summarize(records: list[dict]) -> dict:
    if len({r['run_id'] for r in records}) != len(records):
        raise ValueError('duplicate run would double-count cost')
    real = [r for r in records if r['record_kind'] == 'real']
    currencies = {r['receipt']['costs']['currency'] for r in real}
    if len(currencies) > 1:
        raise ValueError('do not add mixed currencies')
    costs = {}
    for key in ('cloud_spend', 'setup_spend', 'owner_minutes', 'local_seconds'):
        values = [r['receipt']['costs'][key] for r in real]
        costs[key] = {'known_sum': sum(x for x in values if x is not None),
                      'unknown_count': sum(x is None for x in values), 'record_count': len(values)}
    return {'real_attempts': len(real), 'synthetic_excluded': len(records) - len(real),
            'failed_or_invalid_attempts': sum(r['receipt']['outcome'] != 'completed' or bool(r['violations']) for r in real),
            'costs_including_failures': costs, 'currency': next(iter(currencies), None),
            'naming_adoption': 'not_assessed', 'method_effectiveness': 'not_assessed'}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    for command in ('matrix', 'packet', 'preflight'):
        p = subs.add_parser(command); p.add_argument('--config', type=Path, required=True)
        if command in ('matrix', 'packet'): p.add_argument('--output', type=Path, required=True)
        if command == 'packet':
            p.add_argument('--task', type=Path, required=True)
            p.add_argument('--profile', choices=('local', 'reference'), required=True)
            p.add_argument('--method', choices=('simple', 'redesign'), required=True)
            p.add_argument('--role', choices=ROLES, required=True)
        if command == 'preflight':
            p.add_argument('--packet', type=Path, required=True); p.add_argument('--usage', type=Path, required=True)
    p = subs.add_parser('capture')
    for key in ('packet', 'response', 'receipt', 'output'): p.add_argument('--' + key, type=Path, required=True)
    p = subs.add_parser('summarize'); p.add_argument('records', type=Path, nargs='+')
    a = parser.parse_args()
    try:
        if a.command == 'matrix': out = matrix(read(a.config))
        elif a.command == 'packet': out = packet(read(a.config), read(a.task), a.profile, a.method, a.role)
        elif a.command == 'preflight': out = preflight(read(a.config), read(a.packet), read(a.usage))
        elif a.command == 'capture': out = capture(read(a.packet), a.response.read_bytes(), read(a.receipt))
        else: out = summarize([read(p) for p in a.records])
        if hasattr(a, 'output'): write_new(a.output, out)
        else: print(canonical(out).decode(), end='')
        return 2 if a.command == 'preflight' and not out['dispatch_allowed'] else 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
