"""Verify LIVE-411-001 from frozen actual artifacts. No network or generation.
This is same-executor verification, not independent naming-quality validation.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

BASE = '64d7896254c9a320c3632f55d41b5bb879f96cb8'
PILOT = '03_Evolution/01_Research/03_Tests/naming-evidence-pilot'
TRIAL = PILOT + '/live-trial-001'
STATE = '03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml'
AUTH = 'https://github.com/InteropAtlas/InteropAtlas/issues/411#issuecomment-5643216469'
PINNED = {
    'plan.md': 'a9feb76acf5086ef35e5d9eca8dcce7be7ad9011',
    'generated.json': '930cfa6681b21b541652bcb44749ddf66f3eaddb',
    'intrinsic-review.json': 'a595725398ed3b56fbdaea91b9497dc3dfbaa26f',
    'screening.json': '1fc7887fc68bc18e18a04c77102370871f6a767c',
    'screening-recheck.json': '716985ef0ab1a0643a6df57b5c8b43c909d98cee',
}

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repository', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    root, out = args.repository.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(root / PILOT))
    from control_gate import check_record, load, digest

    def git(*parts: str) -> bytes:
        return subprocess.check_output(['git', '-C', str(root), *parts])

    def save(name: str, value: object) -> None:
        (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    originals, manifest, artifacts = {}, [], []
    for name, commit in PINNED.items():
        path = TRIAL + '/' + name
        raw = git('show', commit + ':' + path)
        assert raw == (root / path).read_bytes(), 'Frozen artifact changed: ' + name
        sha = digest(raw)
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        ident = name.split('.')[0]
        originals[name] = json.loads(raw) if name.endswith('.json') else raw.decode()
        artifacts.append({'id': ident, 'kind': 'original', 'file': path,
            'text': raw.decode(), 'sha256': sha,
            'source_url': 'https://github.com/InteropAtlas/InteropAtlas/blob/' + commit + '/' + path,
            'provenance_note': '当次实际文件原文；筛查文件是有标记的选择性工具捕获和执行者判断，不是完整供应商日志。'})
        manifest.append({'file': path, 'commit': commit, 'blob': blob, 'sha256': sha})
        target = out / 'frozen-sources' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    generated = originals['generated.json']
    quality = originals['intrinsic-review.json']
    screening = originals['screening.json']
    fresh = originals['screening-recheck.json']
    before_raw = git('show', BASE + ':' + STATE)
    before = load(before_raw)
    (out / 'state-v87.yaml').write_bytes(before_raw)
    ids = [c['id'] for c in generated['candidates']]
    selected = quality['stages']['intrinsic']
    assert len(ids) == len(set(ids)) == 8
    assert set(selected) == {'L001-01', 'L001-03', 'L001-04', 'L001-07'}
    assert quality['stages']['generated'] == ids
    assert generated['plan_commit'] == PINNED['plan.md']
    assert quality['input_commit'] == PINNED['generated.json']
    assert screening['quality_frozen_commit'] == PINNED['intrinsic-review.json']
    assert screening['exposure_ready_ids'] == []
    assert not quality['reality_results_seen_at_review']
    assert not quality['independent_review']
    assert screening['registrar_call']['returned_payload'] == fresh['registrar_recheck']['returned_payload']
    assert git('show', BASE + ':02_Runtime/02_Tools/adaptive_naming/SKILL.md') == (root / '02_Runtime/02_Tools/adaptive_naming/SKILL.md').read_bytes()
    for name in ('validate_evidence.py', 'control_gate.py'):
        assert git('show', BASE + ':' + PILOT + '/' + name) == (root / PILOT / name).read_bytes()

    coarse = {'L001-01':'compound','L001-02':'compound',
              'L001-03':'blend','L001-04':'blend',
              'L001-05':'phrase','L001-06':'phrase',
              'L001-07':'derivation','L001-08':'root_sound_extension'}
    features = {i:{'form_family':coarse[i], 'evidence_ref':'intrinsic-review',
        'classification_status':'reviewed', 'reviewer':'same_executor_not_independent'} for i in ids}
    decisions = []
    for item in quality['items']:
        if item['id'] not in selected:
            decisions.append({'candidate_id':item['id'],'from':'generated','to':'intrinsic',
                'reason':item['quality'],'disposition':'deferred_within_trial_not_global_rejection'})
    for item in screening['candidate_dispositions']:
        decisions.append({'candidate_id':item['candidate_id'],'from':'intrinsic','to':'reality',
            'reason':item['decision'],'source_artifact':'screening'})
    stamp = fresh['capture_window']['finished_at']
    def query(intent, source, value, outcome, evidence='screening-recheck'):
        return {'intent':intent,'source':source,'result':value,'outcome':outcome,'evidence_ref':evidence}
    screens = [
        {'candidate_id':'L001-01','claim':'unknown','observed_at':stamp,
         'queries':[query('identity','screening.json/web_calls',
            'Limited earlier indexed search found no material exact identity; not independently cleared','unknown','screening'),
            query('public_tm','screening.json/web_calls/7',
            'Official-site indexed search is not an official trademark database search','unknown','screening'),
            query('domain','Namecheap.domain-bulk-check',
            '.com isAvailable=false; .org isAvailable=true; aftermarket practical obtainability unknown','unknown')]},
        {'candidate_id':'L001-03','claim':'unavailable','observed_at':stamp,
         'queries':[query('identity','https://unfoldry.ai/',
            'Exact-name official AI/automation consultancy; decisive task-local identity collision','blocked')]},
        {'candidate_id':'L001-04','claim':'unknown','observed_at':stamp,
         'queries':[query('identity','https://houjin.jp/c/3290005020152',
            'Exact organization in secondary directory; official identity/adjacency not yet verified','unknown')]},
        {'candidate_id':'L001-07','claim':'unknown','observed_at':stamp,
         'queries':[query('identity','https://www.commonarylabs.com/',
            'Official same-base-name Labs page and an exact retail product; material risk, not legal conclusion','unknown'),
            query('public_tm','https://trademarking.in/details/Commonary-6886362.html',
            'Earlier secondary application lead; official status not verified','unknown','screening')]},
    ]
    for s in screens:
        s['timestamp_meaning'] = 'executor_capture_window_end_not_provider_query_timestamp'
        s['capture_window'] = fresh['capture_window']
        s['earlier_query_timing'] = 'Earlier indexed identity/TM queries retain date/order only in screening.json; not backdated into this window.'
    recovery = {
        'mission_value_model': {'status':'present','value':before['mission_value_model'], 'scope':'current_reconstructed_not_historical_input'},
        'name_job_model': {'status':'present','value':before['name_job_model'], 'scope':'current_reconstructed_not_historical_input'},
        'search_landscape': {'status':'present','value':{'scope':'this_trial_only','regions':'alternate possibility; unfolding/making; relational recombination; shared foundation','coarse_forms':coarse,'coverage_claim':'not_exhaustive_no_historical_coverage_estimate'}},
        'scheduler_state': {'status':'present','value':{'scope':'this_trial_only','pattern':'single_context_portfolio_probe','budget':8,'actual_generated':8,'intrinsic_prioritized':4,'display_eligible':0,'no_additional_generation':True}},
        'generation_runtime_evidence': {'status':'present','value':{'scope':'current_trial','level':'best_effort_same_context','independent_worker':False,'unseen_context_claim':False,'artifacts':['plan','generated','intrinsic-review']}},
        'candidate_reality_evidence_links': {'status':'present','value':{'scope':'this_trial_observations_not_clearance','artifacts':['screening','screening-recheck'],'unresolved':['L001-01','L001-04','L001-07'],'no_approved_candidate':True}},
    }
    record = {'record_kind':'live','owner_paused':False,'generation_resume_requested':False,
        'authorization':{'source':AUTH,'scope':'one_bounded_trial_contextual_authorization','general_resume':False,
            'note':'owner_paused=false applies only to this scoped trial, not to the global open-ended generation policy.'},
        'artifacts':artifacts,'recovery':recovery,'batches':[{
            'batch_id':'LIVE-411-001','purpose':'exploration','method_ref':BASE+':Skill0.4.0+task-local-control-gate',
            'runtime':{'level':'best_effort_same_context','unseen_context_claim':False,'independent_review':False,'evidence_ref':'plan'},
            'inputs':['plan'],'outputs':['generated'],
            'stages':{'generated':ids,'intrinsic':selected,'reality':[],'exposed':[]},
            'decisions':decisions,'feedback':[],'screenings':screens,'candidate_features':features,
            'batch_review':{'assessment':'No single coarse form covers all generated/selected items; 2 of 4 selected are blends. No exposure because identity/obtainability evidence does not meet thresholds. No causal or naming-effectiveness conclusion.',
                'stage_observations':{'generated':'8 across five coarse declared families','intrinsic':'4 across three coarse families','reality':'0 sufficiently cleared','exposed':'0 candidate-review invitations'},
                'evidence_refs':['generated','intrinsic-review','screening','screening-recheck'],
                'first_recorded_concentration_stage':None}}],
        'historical_unknowns':{'unchanged':True,'scope':'RND130 and global history; not filled by this new record'},
        'tool_ui_visibility':'Domain-check UI may show queried strings; no screened candidate presentation was issued.'}
    save('record.json',record)
    checks = {'actual':check_record(record,root,'audit'), 'exposure_readiness':check_record(record,root,'expose')}
    assert not checks['actual']['errors'], checks['actual']
    assert checks['actual']['disposition']=='review'
    assert 'screen_result_unresolved' in checks['actual']['review_required']
    assert checks['exposure_readiness']['disposition']=='review'
    assert not checks['exposure_readiness']['baseline']['capture_complete']
    assert not checks['actual']['generation_authorization']
    # Counterfactual mutations are tests only, never actual exposure events.
    bad = copy.deepcopy(record)
    bad['batches'][0]['stages']['reality']=['L001-03']
    bad['batches'][0]['stages']['exposed']=['L001-03']
    checks['counterfactual_expose_collision']=check_record(bad,root,'expose')
    assert 'exposed_despite_negative_screen' in checks['counterfactual_expose_collision']['errors']
    bad = copy.deepcopy(record)
    bad['batches'][0]['screenings'][0]['claim']='available'
    checks['counterfactual_promote_unknown']=check_record(bad,root,'expose')
    assert checks['counterfactual_promote_unknown']['disposition']!='pass'
    checks['counterfactual_note']='Mutated audit copies only. No actual candidate display, changed query, or new name.'
    save('checks.json',checks)
    save('summary.json',{'batch_id':'LIVE-411-001','base':BASE,'budget':8,'generated':8,
        'intrinsic_prioritized':4,'display_eligible':0,'presented_for_owner_decision':0,
        'dispositions':screening['candidate_dispositions'],
        'record_disposition':checks['actual']['disposition'],
        'record_errors':checks['actual']['errors'],'remaining_review':checks['actual']['review_required'],
        'structural_capture_complete':checks['actual']['baseline']['capture_complete'],
        'frozen_source_manifest':manifest,'record_sha256':digest((out/'record.json').read_bytes()),
        'control_gate_unchanged':True,'skill_unchanged':True,'historical_gaps_unchanged':True,
        'counterfactual_guards_behaved_as_expected':True,'reproducible_output_excludes_wallclock':True,
        'limits':['single-context real trial, no independent semantic reviewer','index absence is not trademark clearance','no aftermarket domain acquisition path verified','capture_complete=false because unresolved screening remains; complete raw generation is not legal clearance','no Owner candidate preferences observed or invented','no method effectiveness, production error-rate, or historical replay claim']})
    for name in ('control_gate.py','validate_evidence.py'):
        shutil.copy2(root/PILOT/name,out/name)
    shutil.copy2(Path(__file__),out/'check_trial.py')
    print(json.dumps({'generated':8,'intrinsic_prioritized':4,'display_eligible':0,
        'audit':checks['actual']['disposition'],'errors':checks['actual']['errors'],
        'review_required':checks['actual']['review_required']},ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
