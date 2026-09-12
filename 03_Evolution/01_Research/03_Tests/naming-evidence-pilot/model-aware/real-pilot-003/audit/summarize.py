"""Aggregate frozen author judgments; never manufacture a semantic ground truth."""
from __future__ import annotations
import argparse
from collections import Counter
from pathlib import Path
import json
from extract import canonical, decode, sha


def build(home: Path, output: Path):
    data=decode((home/'data.json').read_text())
    assessment=decode((home/'assessment.json').read_text())
    packets=decode((home/'packets.json').read_text())
    tiers={x['id']:x['tier'] for x in assessment['surface']}
    assert len(tiers)==len(assessment['surface'])==len(packets['names'])==16
    assert set(tiers)=={x['id'] for x in packets['names']}
    assert assessment['review_kind']=='exploratory_author_assessment_not_independent_blind_review'
    groups={}; rows=[]
    for cell in data['cells']:
        counts=Counter(tiers[x['name_id']] for x in cell['pool'])
        row={'cell':cell['cell'],'method':cell['method'],'seed':cell['seed'],
             'generated_occurrences':cell['generated_occurrences'],'pool_count':len(cell['pool']),
             'author_tiers':dict(counts),'recorded_status':cell['status'],
             'generation_cost':cell['generation_cost']}
        for stage,obj in cell['stages'].items():
            row[stage]={'parser_coverage_valid':obj['coverage_valid'],
                        'decisions':dict(Counter(x['decision'] for x in obj['reviews']))}
        if 'retained_after_audit_ids' in cell:
            row['retained_after_audit']=len(cell['retained_after_audit_ids'])
        rows.append(row)
        group=groups.setdefault(cell['method'],{'name_ids':set(),'generated_occurrences':0,'pool_occurrences':0,
                                                'generation_calls':0,'generation_input_tokens':0,'generation_output_tokens':0,'generation_seconds':0})
        group['name_ids'].update(x['name_id'] for x in cell['pool'])
        group['generated_occurrences']+=cell['generated_occurrences'];group['pool_occurrences']+=len(cell['pool'])
        for a,b in [('generation_calls','calls'),('generation_input_tokens','input_tokens'),('generation_output_tokens','output_tokens'),('generation_seconds','seconds')]:
            group[a]+=cell['generation_cost'][b]
    for group in groups.values():
        group['name_ids']=sorted(group['name_ids'])
        group['unique_names']=len(group['name_ids'])
        group['author_tiers_unique']=dict(Counter(tiers[x] for x in group['name_ids']))
        group['generation_total_tokens']=group['generation_input_tokens']+group['generation_output_tokens']
    R,S=groups['redesign'],groups['simple']
    assert [r['author_tiers'].get('priority',0) for r in rows]==[2,2,1,2]
    assert R['unique_names']==S['unique_names']==10
    assert R['generation_total_tokens']==4160 and S['generation_total_tokens']==1826
    evidence=decode((home/'../results/evidence.json').read_text())
    path='model/cell-3-simple-411922/calls/r1audit/output.txt'
    raw=evidence['files'][path]['content'];assert sha(raw.encode())==evidence['files'][path]['sha256']
    answer=decode(raw)
    expected=data['cells'][2]['stages']['r1audit']['expected_ids']
    nested=answer['output_contract']['reviews']
    assert set(answer)=={'output_contract'} and set(answer['output_contract'])=={'reviews'}
    assert [r['id'] for r in nested]==expected==['C005']
    assert all(set(r)=={'id','decision','reason'} and r['decision'] in ('keep','hold','drop') and r['reason'].strip() for r in nested)
    metrics={'kind':'deterministic_aggregation_of_subjective_author_judgments_not_independent_quality_test',
      'source_sha256':data['source_sha256'],'assessment_surface_sha256':sha(canonical(assessment['surface'])),
      'surface_freeze_commit':'20a93804c3d1fda7cb43f02d4a7d4474f9830b06',
      'verified_embedded_files':data['verified_embedded_files'],'occurrences':data['occurrences'],
      'unique_names':data['unique_names'],'unique_explanations':data['unique_explanations'],
      'new_inference_calls':0,'groups':groups,'cells':rows,
      'generation_cost_ratio_redesign_over_simple':{'total_tokens':R['generation_total_tokens']/S['generation_total_tokens'],
                                                   'observed_seconds':R['generation_seconds']/S['generation_seconds']},
      'sensitivity':{'hypothetical_only':'Move borderline EditGap priority to reserve; original judgments unchanged',
                     'redesign_unique_priority_then':sum(tiers[x]=='priority' for x in R['name_ids'] if x!='N-e2d14018'),
                     'simple_unique_priority_then':sum(tiers[x]=='priority' for x in S['name_ids'])},
      'coverage_error_correction':{'source_path':path,'raw_sha256':sha(raw.encode()),
        'program_reported':'review_coverage_incomplete','root_keys':list(answer),
        'actual_review_location':'output_contract.reviews','expected_ids':expected,'actual_nested_ids':[x['id'] for x in nested],
        'complete_required_content_exists':True,'decision':nested[0]['decision'],
        'old_result_changed':False,'diagnosis':'Nested response envelope, not semantic omission; data.json missing_ids refers only to original parser-visible field.'},
      'independent_review':'not_performed','method_winner':'not_established',
      'recommended_development_default':'simple_pending_independent_evidence_not_runtime_config_change',
      'adoption':'not_assessed','scope':'one fictional task, two seeds, 4B Q4_K_M; no causal or general superiority claim'}
    blob=canonical(metrics)
    if output.exists(): assert output.read_bytes()==blob,'Aggregation conflict'
    else: output.write_bytes(blob)
    print(json.dumps({'unique_names':len(tiers),'priority_by_cell':[r['author_tiers'].get('priority',0) for r in rows],
                      'generation_token_ratio':metrics['generation_cost_ratio_redesign_over_simple']['total_tokens'],
                      'nested_review_present':True,'new_inference_calls':0}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--home',type=Path,default=Path(__file__).resolve().parent);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();build(args.home,args.output)
