"""One-shot deterministic v95 wiring. No model calls or semantic rescoring."""
from pathlib import Path
import json

ROOT=Path('03_Evolution/01_Research/03_Tests/naming-evidence-pilot/model-aware')

# workflow.py: replace sampled rejection audit with same-seed full reverse-order crosscheck.
p=ROOT/'workflow.py';s=p.read_text()
s=s.replace('Frozen brief -> isolated proposals -> name-only review -> explained review ->\nrejection audit -> supplied screening evidence -> substantive owner feedback.',
            'Frozen brief -> isolated proposals -> name-only review -> two-order explained crosscheck ->\nsupplied screening evidence -> substantive owner feedback.')
s=s.replace("plan = {'schema_version': 2, 'selection_policy': selection.VERSION,", "plan = {'schema_version': 3, 'selection_policy': selection.VERSION,")
old="""    explained = reviews(step_call(root, plan, prefix + 'explained', review_question('with_explanation', pool),
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
"""
new="""    explained = reviews(step_call(root, plan, prefix + 'explained', review_question('with_explanation', pool),
                                 'select', plan['review_output_allowance'], backend), ids)
    # SELECT-408-002 showed strong order sensitivity. Re-run the exact same
    # selection task with the same seed and reversed item order. This is not an
    # independent expert; it is a conservative single-model stability check.
    reverse_pool = list(reversed(pool))
    explained_reverse = reviews(step_call(root, plan, prefix + 'explained_reverse',
        review_question('with_explanation', reverse_pool), 'select',
        plan['review_output_allowance'], backend), ids)
    queues = selection.order_crosschecked_queues(pool, explained, explained_reverse)
    kept = [v['id'] for v in pool if v['id'] not in queues['not_pursued_ids']]
    result = {'round': round_no, 'pool': pool, 'surface': surface, 'explained': explained,
              'explained_reverse': explained_reverse,
              'audit': [], 'rejected_sample_ids': [], 'audit_disagreement_ids': [],
              'intrinsic_shortlist_ids': kept, 'exact_duplicates_removed': duplicate_count,
              'review_independence': 'two_order_permutations_same_model_same_seed_not_independent_experts',
              'semantic_truth': 'not_programmatically_verified', 'reality_clearance': 'not_assessed'}
    result.update(queues)
"""
assert old in s,'workflow target block changed';s=s.replace(old,new)
s=s.replace("audit_disagreement=v['id'] in result['audit_disagreement_ids'])", "audit_disagreement=False, order_disagreement=v['id'] in result.get('order_disagreement_ids', []))")
p.write_text(s)

# test_workflow.py: fixture intentionally disagrees on C001 when item order reverses.
p=ROOT/'test_workflow.py';s=p.read_text()
old="""        else:
            answer = {'reviews': [{'id': v['id'], 'decision': 'drop' if v['id'] == 'C001' and stage != 'independent_recheck' else 'keep',
                'reason': 'TEST_ONLY_JUDGMENT_NOT_SEMANTIC_EVIDENCE'} for v in q['items']]}
            if self.mode == 'missing_review': answer['reviews'] = []
"""
new="""        else:
            reversed_explained = stage == 'with_explanation' and q['items'] and q['items'][0]['id'] != 'C001'
            answer = {'reviews': [{'id': v['id'],
                'decision': ('keep' if v['id'] != 'C001' or reversed_explained else 'drop'),
                'reason': 'TEST_ONLY_JUDGMENT_NOT_SEMANTIC_EVIDENCE'} for v in q['items']]}
            if self.mode == 'missing_review': answer['reviews'] = []
"""
assert old in s,'handler target changed';s=s.replace(old,new)
s=s.replace("['proposal']*3 + ['name_only', 'with_explanation', 'independent_recheck']", "['proposal']*3 + ['name_only', 'with_explanation', 'with_explanation']")
old="""    def test_rejection_audit_keeps_disagreement_visible(self):
        self.init();self.run_flow();r1=p.read(self.root/'round-1.json')
        self.assertEqual(r1['audit_disagreement_ids'], ['C001']);self.assertIn('C001',r1['intrinsic_shortlist_ids'])
"""
new="""    def test_order_crosscheck_moves_disagreement_to_hold(self):
        self.init();self.run_flow();r1=p.read(self.root/'round-1.json')
        self.assertEqual(r1['order_disagreement_ids'], ['C001'])
        self.assertIn('C001',r1['hold_ids']);self.assertNotIn('C001',r1['priority_ids'])
        self.assertNotIn('C001',r1['not_pursued_ids']);self.assertIn('C001',r1['intrinsic_shortlist_ids'])
        self.assertEqual(r1['audit'],[])
"""
assert old in s,'test target changed';s=s.replace(old,new)
p.write_text(s)

# Experimental docs only; stable Adaptive Naming Skill remains untouched.
p=ROOT/'SKILL.md';s=p.read_text();s=s.replace('version: 0.2.0-experimental','version: 0.3.0-experimental')
s=s.replace('记录keep/hold/drop及理由。生成者risk保留在原始记录和待查问题登记，不进入质量评审包；',
            '记录keep/hold/drop及理由。同一候选池用相同seed再做一次反向顺序解释后评审；只有两次都keep才进入priority，两次都drop才停止投入，其余进入hold。生成者risk保留在原始记录和待查问题登记，不进入质量评审包；')
p.write_text(s)

p=ROOT/'README.md';s=p.read_text()+'''\n\n## v95：顺序交叉检查（实验）\n\nSELECT-408-002 在同一候选、同一brief/intent、同一seed下仅倒转候选顺序时出现4/6决定变化。因此单次批量selector不再作为priority/drop的单点依据。实验工作流0.3.0使用相同seed的正序与反序两次解释后评审：`keep+keep → priority`、`drop+drop → not_pursued`，任何hold或顺序分歧均进入hold。该规则只保守分配后续核查资源，不证明语义正确，也不是独立专家复核。\n\nname-only review继续作为观察层；旧的抽样rejection audit不再是新工作流默认步骤。生成方式仍默认simple、redesign显式可选。旧实验继续按冻结源码解释，不用v95回写旧结果。\n''';p.write_text(s)

print(json.dumps({'status':'patched','files':['workflow.py','test_workflow.py','SKILL.md','README.md'],'model_calls':0},ensure_ascii=False))
