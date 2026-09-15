"""Frozen anonymous fixtures against the real baseline and task-local preflight.

Same-author deterministic validation; no model A/B, held-out, or semantic-review claim.
Emits exact inputs and outputs in --output for reproducibility. No network calls.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import yaml
from validate_evidence import REQUIRED, STAGES, validate
from control_gate import check_record, check_state, digest, guarded_write, load

BASE = 'fc84a477c805e828ce47666dbb5c3e0470c57324'
STATE = '03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml'
BASE_STATE_BLOB = 'ddbfe980613eaf06a08cf66a181aea640afa5416'
BASE_VALIDATOR_BLOB = 'a045604850ec9490ce0bce37f44f90e003891e5d'

def git_blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()

def canonical(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()

def base():
    ids = ['A1', 'A2', 'B1', 'B2']
    r = {'record_kind':'synthetic', 'owner_paused':True, 'generation_resume_requested':False,
         'artifacts':[{'id':'IN','kind':'synthetic','text':'比较匿名ID的结构；合成定向情境可比较同一形态，预算4。'},
                      {'id':'OUT','kind':'synthetic','text':'A1 A2 B1 B2 仅为匿名测试标识；形态及查询结果均为合成数据。'},
                      {'id':'FB','kind':'synthetic','text':'我更喜欢A1。'}],
         'recovery':{key:{'status':'present','value':'synthetic-state'} for key in REQUIRED}}
    for a in r['artifacts']:
        a['sha256'] = digest(a['text'].encode())
    r['batches'] = [{'batch_id':'SYN-CONTROL','purpose':'exploration','method_ref':'pilot-v86-structural-baseline',
        'runtime':{'level':'synthetic'}, 'inputs':['IN'], 'outputs':['OUT'],
        'stages':{s:list(ids) for s in STAGES}, 'decisions':[],
        'feedback':[{'source_artifact':'FB','quote':'我更喜欢A1。','interpretation':'原因未知。',
                     'basis':'inference','role':'prefer','observation_type':'ranking',
                     'claim_type':'ranking','interpretation_status':'hypothesis'}],
        'screenings':[{'candidate_id':i,'claim':'available','observed_at':'2026-09-12T00:00:00Z',
                      'queries':[{'intent':k,'source':'synthetic-fixture','result':'合成清晰结果',
                                  'outcome':'clear','evidence_ref':'OUT'} for k in ('identity','public_tm','domain')]} for i in ids],
        'candidate_features':{i:{'form_family':'F'+str(n),'evidence_ref':'OUT','classification_status':'reviewed'} for n,i in enumerate(ids)},
        'batch_review':{'assessment':'匿名合成分类，不是名称效果评价。','stage_observations':{s:'synthetic' for s in STAGES},'evidence_refs':['OUT']}}]
    return r

def fixture(recipe):
    r=base(); b=r['batches'][0]; fb=b['feedback'][0]
    def same_family():
        for f in b['candidate_features'].values(): f['form_family']='F0'
    def focus():
        same_family(); b['purpose']='exploitation'
        b['focus_contract']={'budget':4,'form_family':'F0','source_artifact':'IN',
                             'quote':'比较同一形态，预算4','rationale':'只检验一个形态内的差异。','exit_condition':'到4项停止，不推广为一般偏好。'}
    def narrow(stage):
        b['candidate_features']['A1']['form_family']='F0'; b['candidate_features']['A2']['form_family']='F0'
        ix=STAGES.index(stage)
        for s in STAGES[ix:]:b['stages'][s]=['A1','A2']
        b['decisions']=[{'candidate_id':i,'from':STAGES[ix-1],'to':stage,'reason':'synthetic-stage-filter'} for i in ('B1','B2')]
    if recipe=='clean':pass
    elif recipe=='focused':focus()
    elif recipe=='monoculture':same_family()
    elif recipe=='unbudgeted':same_family();b['purpose']='exploitation'
    elif recipe=='intrinsic_narrowing':narrow('intrinsic')
    elif recipe=='reality_narrowing':narrow('reality')
    elif recipe=='wrong_attribution':narrow('reality');b['batch_review']['first_recorded_concentration_stage']='generated'
    elif recipe=='rank_as_reason':fb.update(basis='direct_reason',claim_type='reason',interpretation='用户喜欢的是F0。',interpretation_status='confirmed')
    elif recipe=='rank_hypothesis':fb.update(claim_type='reason',interpretation='可能喜欢F0，待验证。')
    elif recipe in ('explicit_reason','explicit_constraint'):
        text='我喜欢A1的结构。' if recipe=='explicit_reason' else '最终候选必须符合约束Q。'
        r['artifacts'][2].update(text=text,sha256=digest(text.encode()))
        fb.update(quote=text,basis='direct_reason',observation_type=recipe,
                  claim_type='reason' if recipe=='explicit_reason' else 'constraint',interpretation_status='recorded',interpretation='按合成原句记录。')
        if recipe=='explicit_constraint':fb.update(role='gate',gate_authorization_quote=text)
    elif recipe=='rank_as_gate':fb.update(basis='direct_reason',role='gate',claim_type='constraint',gate_authorization_quote=fb['quote'])
    elif recipe=='hash_mismatch':r['artifacts'][0]['sha256']='0'*64
    elif recipe=='dangling_ref':r['recovery']['mission_value_model']={'status':'referenced','commit':'f'*40,'path':'AGENTS.md','section':'# AGENTS.md'}
    elif recipe=='screen_unknown':b['screenings'][0]['queries'][2]['outcome']='unknown'
    elif recipe=='screen_no_artifact':b['screenings'][0]['queries'][2].pop('evidence_ref')
    elif recipe=='reported_as_direct':r['artifacts'][2]['kind']='reported';fb.update(basis='direct_reason')
    elif recipe=='resume_paused':r['generation_resume_requested']=True
    elif recipe=='incomplete_audit':b['inputs']=[]
    elif recipe=='missing_features':b.pop('candidate_features')
    elif recipe=='over_budget':focus();b['focus_contract']['budget']=2
    elif recipe=='isolation_overclaim':b['runtime']={'level':'best_effort_same_context','unseen_context_claim':True}
    elif recipe=='feature_unreviewed':b['candidate_features']['A1']['classification_status']='inferred'
    elif recipe=='screen_blocked':b['screenings'][0]['queries'][2]['outcome']='blocked'
    elif recipe=='path_escape':r['artifacts'][0]['file']='../not-in-repository'
    elif recipe=='blanket_waiver':same_family();b['batch_review']['waiver']='reviewed, all good'
    elif recipe=='boolean_budget':focus();b['focus_contract']['budget']=True
    elif recipe=='single_candidate':
        for s in STAGES:b['stages'][s]=['A1']
        b['screenings']=b['screenings'][:1]
    else:raise ValueError('unknown frozen recipe '+recipe)
    return r

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repository',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--baseline-ref',default=BASE)
    a=p.parse_args();root=a.repository.resolve();here=Path(__file__).resolve().parent
    code=(here/'validate_evidence.py').read_bytes()
    if git_blob(code)!=BASE_VALIDATOR_BLOB:raise RuntimeError('Baseline implementation changed; cannot claim frozen comparison')
    suite_raw=(here/'control-cases.json').read_bytes();suite=json.loads(suite_raw)
    rows=[]
    for c in suite['cases']:
        record=fixture(c['recipe'])
        old=validate(record);new=check_record(record,root,'audit' if c['recipe']=='incomplete_audit' else 'expose')
        rows.append({**c,'input':record,'input_sha256':digest(canonical(record)),
                     'baseline_actual':old,'gate_actual':new,'passed':new['disposition']==c['expected']})
    state_raw=subprocess.check_output(['git','-C',str(root),'show',a.baseline_ref+':'+STATE])
    if git_blob(state_raw)!=BASE_STATE_BLOB:raise RuntimeError('State baseline byte mismatch')
    before=load(state_raw);after=copy.deepcopy(before);after['task']['snapshot_version']+=1
    state_rows=[]
    def state_test(name,change,expected):
        proposed=copy.deepcopy(after);change(proposed)
        out=check_state(before,proposed,root)
        state_rows.append({'case':name,'proposed_sha256':digest(canonical(proposed)),'actual':out,'expected_write_allowed':expected,'passed':out['write_allowed']==expected})
    state_test('same_job_audit_update_preserves_unknowns',lambda s:None,True)
    state_test('required_field_silently_deleted',lambda s:s.pop('mission_value_model'),False)
    def relocate(s):
        s.pop('mission_value_model');s['recovery_refs']={'mission_value_model':{'commit':a.baseline_ref,'path':STATE,'section':'mission_value_model:'}}
    state_test('equivalent_pinned_relocation',relocate,True)
    def bad_ref(s):relocate(s);s['recovery_refs']['mission_value_model']['commit']='f'*40
    state_test('dangling_relocation',bad_ref,False)
    state_test('pause_removed',lambda s:s['process_review'].update(generation_paused=False),False)
    state_test('snapshot_reused',lambda s:s['task'].update(snapshot_version=86),False)
    state_test('commercial_gate_drift',lambda s:s['constraint_registry']['confirmed_hard_constraints'][2].update(primary_domain='.org'),False)
    state_test('unknown_silently_cleared',lambda s:s['audit_recovery'].update(missing_current_state=[]),False)
    state_test('unknown_filled_with_unmeasured_zero',lambda s:s.update(search_landscape={'attempts':0}),False)
    state_test('unknown_replaced_by_empty_value',lambda s:s.update(search_landscape=0),False)
    state_test('mission_not_silently_flattened',lambda s:s.update(mission_value_model={'statement':'only-three-keywords'}),False)
    state_test('name_job_not_silently_replaced',lambda s:s.update(name_job_model={'status':'complete'}),False)
    extra=[]
    def item(name,ok,detail=None):extra.append({'check':name,'passed':bool(ok),'detail':detail})
    with tempfile.TemporaryDirectory(prefix='.control-test-',dir=root) as directory:
        dest=Path(directory)/'state.yaml';dest.write_bytes(state_raw)
        bad=copy.deepcopy(after);bad.pop('mission_value_model')
        failed=guarded_write(dest,state_raw,canonical(bad),root)
        item('bad_write_leaves_file_unchanged',not failed['written'] and dest.read_bytes()==state_raw,failed)
        good=guarded_write(dest,state_raw,canonical(after),root)
        item('valid_write_commits_exact_bytes',good['written'] and dest.read_bytes()==canonical(after),good)
        conflict=guarded_write(dest,state_raw,canonical(after),root)
        item('stale_expected_bytes_rejected',not conflict['written'] and 'destination_changed' in conflict['errors'],conflict)
        lock=dest.with_name(dest.name+'.pilot-lock');lock.touch()
        busy=guarded_write(dest,state_raw,canonical(after),root);lock.unlink()
        item('cooperative_writer_lock_respected',not busy['written'] and 'writer_lock_exists' in busy['errors'],busy)
    for raw,suffix,label in [(b'a: 1\na: 2\n','.yaml','duplicate_yaml'),(b'{"a":1,"a":2}','.json','duplicate_json')]:
        try:load(raw,suffix);ok=False
        except ValueError:ok=True
        item(label+'_rejected',ok)
    invalid_time=base();invalid_time['batches'][0]['screenings'][0]['observed_at']='not-a-timestamp'
    time_result=check_record(invalid_time,root,'expose')
    item('invalid_timestamp_rejected','screen_timestamp_invalid' in time_result['errors'],time_result)
    no_zone=base();no_zone['batches'][0]['screenings'][0]['observed_at']='2026-09-12T01:00:00'
    zone_result=check_record(no_zone,root,'expose')
    item('timestamp_requires_timezone','screen_timestamp_invalid' in zone_result['errors'],zone_result)
    # Metamorphic transformations must not change the decision when structure is unchanged.
    for recipe in ('clean','focused','monoculture','reality_narrowing'):
        original=fixture(recipe);changed=copy.deepcopy(original)
        b=changed['batches'][0]
        ids={i:'ID'+str(n+10) for n,i in enumerate(b['stages']['generated'])}
        for st in STAGES:b['stages'][st]=list(reversed([ids[i] for i in b['stages'][st]]))
        for d in b['decisions']:d['candidate_id']=ids[d['candidate_id']]
        for s in b['screenings']:s['candidate_id']=ids[s['candidate_id']]
        b['candidate_features']={ids[i]:v for i,v in b['candidate_features'].items()}
        one=check_record(original,root,'expose');two=check_record(changed,root,'expose')
        item('id_and_order_invariance:'+recipe,one['disposition']==two['disposition'] and one['errors']==two['errors'] and one['review_required']==two['review_required'])
    item('late_filter_not_attributed_to_generator',next(r for r in rows if r['recipe']=='reality_narrowing')['gate_actual']['stage_observations'][0]['first_recorded_concentration_stage']=='reality')
    item('original_defects_still_caught_by_baseline',all(not r['baseline_actual']['capture_complete'] for r in rows if r['recipe'] in ('reported_as_direct','resume_paused','incomplete_audit')))
    report={'kind':'deterministic_control_comparison_not_model_or_skill_efficacy','baseline_commit':BASE,
            'local_state_source_ref':a.baseline_ref,'case_definition_sha256':digest(suite_raw),
            'baseline_validator_blob':BASE_VALIDATOR_BLOB,'gate_sha256':digest((here/'control_gate.py').read_bytes()),
            'runner_sha256':digest(Path(__file__).read_bytes()),'cases':rows,'state_cases':state_rows,'integration_checks':extra,
            'limits':['same author designed cases and implementation; not blinded or independent review',
                      'honest feature/feedback/query labels are an input assumption, not semantic truth',
                      'baseline is the real structural checker, not the full Skill or model',
                      'all screened outcomes and candidate identifiers in cases are synthetic',
                      'pass is not generation permission or real-world clearance']}
    report['summary']={'control_cases_passed':sum(r['passed'] for r in rows),'control_cases_total':len(rows),
        'state_cases_passed':sum(r['passed'] for r in state_rows),'state_cases_total':len(state_rows),
        'integration_checks_passed':sum(r['passed'] for r in extra),'integration_checks_total':len(extra),
        'baseline_complete_but_gate_review_or_block':sum(r['baseline_actual']['capture_complete'] and r['gate_actual']['disposition']!='pass' for r in rows),
        'valid_control_cases':sum(r['expected']=='pass' for r in rows),
        'false_holds_among_valid_cases':sum(r['expected']=='pass' and r['gate_actual']['disposition']!='pass' for r in rows)}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_bytes(canonical(report))
    print(json.dumps(report['summary'],ensure_ascii=False))
    for r in rows:
        if not r['passed']:print('FAIL',r['id'],r['expected'],r['gate_actual'])
    for r in state_rows:
        if not r['passed']:print('FAIL-STATE',r)
    return 0 if all(r['passed'] for r in rows+state_rows+extra) else 1

if __name__=='__main__':
    raise SystemExit(main())
