"""v94: input provenance and resource queues, not semantic truth certification."""
from __future__ import annotations
import copy
import protocol as p

VERSION = '0.2.0-experimental'
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
    # Risk text remains in the original pool and the unresolved inquiry register.
    # It is deliberately not a quality selector input or a source of verified facts.
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


def resource_queues(result: dict) -> dict:
    """Project declared decisions; never rejudge or manufacture confidence."""
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
