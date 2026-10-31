"""v95: input provenance and resource queues, not semantic truth certification."""
from __future__ import annotations
import copy
import protocol as p

VERSION = '0.3.0-experimental'
DEFAULT_METHOD = 'simple'
STAGES = {'name_only', 'with_explanation', 'independent_recheck'}


def review_question(stage: str, rows: list[dict]) -> str:
    if stage not in STAGES:
        raise ValueError('unknown_selection_stage')
    ids = [v['id'] for v in rows]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError('selection_input_ids_not_unique')
    items = []
    for row in rows:
        item = {k: row[k] for k in ('id', 'name')}
        if stage != 'name_only':
            item['suggested_pronunciation'] = row['pronunciation']
            item['creator_intent'] = {k: row[k] for k in ('meaning', 'derivation')}
            item['creator_intent_status'] = 'unverified_proposal_not_linguistic_or_external_fact'
        items.append(item)
    return p.canonical({
        'stage': stage,
        'task': '逐一评估全部给定ID，不生成名称。只完成本阶段；keep=值得优先进一步核查，hold=待证保留，drop=当前不再投入。不要凑足keep数量，也不要因不确定就一律淘汰。',
        'evidence_rules': [
            '直接依据是名称可观察形式和已给简报。简报没有要求裸名逐字表达全部功能，不能自行增加这个硬门槛。',
            'creator_intent只是生成者希望表达的意思，不证明词源、常见读法、用户联想或产品能力。可以质疑它，不能照单全收。',
            '没有现实核查资料。不得声称存在或不存在商标/域名/同名冲突；没有查证不等于冲突。',
            '联想是判断而非事实：说明由名称哪部分、怎样影响简报要求；尚待用户/语言/现实验证的推测不得单独支持确定淘汰。速度、轻量或抽象不自动意味着云端、联网或不专业。',
        ],
        'items': items,
        'verified_external_facts': [],
        'output_contract': {'reviews': [{'id': '原ID', 'decision': 'keep/hold/drop', 'reason': '具体名称特征、简报要求和推理；不确定明确注明'}]},
    }).decode()


def _decision_map(rows: list[dict], ids: list[str]) -> dict[str, str]:
    if not isinstance(rows, list) or len(rows) != len(ids):
        raise ValueError('incomplete_crosscheck_reviews')
    if any(not isinstance(v, dict) for v in rows):
        raise ValueError('crosscheck_review_object_required')
    if len({v.get('id') for v in rows}) != len(ids) or {v.get('id') for v in rows} != set(ids):
        raise ValueError('crosscheck_ids_changed_or_duplicated')
    decisions = {v['id']: v.get('decision') for v in rows}
    if any(v not in ('keep', 'hold', 'drop') for v in decisions.values()):
        raise ValueError('crosscheck_unknown_decision')
    return decisions


def order_crosschecked_queues(pool: list[dict], first_reviews: list[dict], second_reviews: list[dict]) -> dict:
    """Conservative resource allocation across two order permutations.

    The two reviews must cover the exact same candidate IDs. This function does
    not decide semantic truth. It only prevents one batch ordering from being a
    single-point priority/drop decision: keep+keep -> priority, drop+drop ->
    not_pursued, everything else -> hold.
    """
    ids = [v['id'] for v in pool]
    if not ids or len(ids) != len(set(ids)):
        raise ValueError('duplicate_or_empty_pool_id')
    first = _decision_map(first_reviews, ids)
    second = _decision_map(second_reviews, ids)
    priority = [i for i in ids if first[i] == second[i] == 'keep']
    not_pursued = [i for i in ids if first[i] == second[i] == 'drop']
    hold = [i for i in ids if i not in set(priority + not_pursued)]
    disagreements = [i for i in ids if first[i] != second[i]]
    return {
        'priority_ids': priority,
        'hold_ids': hold,
        'not_pursued_ids': not_pursued,
        'screening_queue_ids': priority,
        'order_disagreement_ids': disagreements,
        'decision_pairs': {i: [first[i], second[i]] for i in ids},
        'crosscheck_semantics': 'conservative_resource_allocation_not_quality_truth',
        'priority_semantics': 'keep_in_both_order_permutations_relative_research_investment_only',
        'hold_semantics': 'any_hold_or_order_disagreement_preserved_not_auto_screened',
        'semantic_truth': 'not_programmatically_verified',
        'reality_clearance': 'not_assessed',
    }


def resource_queues(result: dict) -> dict:
    """Project one declared review plus optional rejection audit; legacy v94 path."""
    ids = [v['id'] for v in result['pool']]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate_pool_id')
    rows = result['explained']
    if len(rows) != len(ids) or {v['id'] for v in rows} != set(ids):
        raise ValueError('incomplete_queue_input')
    decisions = {v['id']: v['decision'] for v in rows}
    if any(v not in ('keep', 'hold', 'drop') for v in decisions.values()):
        raise ValueError('unknown_queue_decision')
    audit = result.get('audit', [])
    if len({v['id'] for v in audit}) != len(audit) or any(v['id'] not in decisions for v in audit):
        raise ValueError('invalid_audit_ids')
    disagreements = {v['id'] for v in audit if v['decision'] != decisions[v['id']]}
    priority = [i for i in ids if decisions[i] == 'keep' and i not in disagreements]
    hold = [i for i in ids if decisions[i] == 'hold' or i in disagreements]
    dropped = [i for i in ids if i not in set(priority + hold)]
    return {
        'priority_ids': priority, 'hold_ids': hold, 'not_pursued_ids': dropped,
        'screening_queue_ids': priority, 'audit_disagreement_ids': sorted(disagreements),
        'priority_semantics': 'relative_research_investment_not_quality_proof_or_clearance',
        'hold_semantics': 'preserved_but_not_automatically_scheduled_or_exposed_as_passed',
        'semantic_truth': 'not_programmatically_verified',
        'reality_clearance': 'not_assessed',
    }


def inquiry_register(pool: list[dict]) -> list[dict]:
    return [{'id': v['id'], 'creator_risk_hypothesis': copy.deepcopy(v['risk']),
             'verification': 'not_checked', 'source': 'original_generator_output',
             'use': 'possible_inquiry_only_not_a_quality_or_reality_verdict'} for v in pool]
