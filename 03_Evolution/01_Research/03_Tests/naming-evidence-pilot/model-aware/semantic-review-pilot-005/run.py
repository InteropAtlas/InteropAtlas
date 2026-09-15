"""SEM-408-005: two-case confirmation of reviewer task understanding.

Uses two existing DEV-02 candidates chosen before execution for distinct prior
SEM-408-003 failure classes:
- C002 / Diffly: instruction-or-brief leakage into candidate evidence;
- C006 / Sublyte: circular candidate grounding.

Packaging is identical to SEM-408-004. Requests are independent, no retry, no new
names. Stop immediately if the first completed review is not task-gate pass.
Even two passes establish only task-understanding eligibility, not semantic truth.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
FOUR_PATH=HOME/'semantic-review-pilot-004/run.py'
ORIGIN='http://127.0.0.1:8086'
TARGETS=[{'id':'C002','name':'Diffly'},{'id':'C006','name':'Sublyte'}]


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

four=load('sem408004',FOUR_PATH)
base=four.base
iface=four.iface
gate=four.gate
SYSTEM=four.SYSTEM


def source_material():
    brief,rows,source_hash=base.source_material()
    index={v['id']:v for v in rows}
    selected=[index[v['id']] for v in TARGETS]
    assert selected==TARGETS
    return brief,selected,source_hash


def prepare(output:Path,runtime:Path):
    base.prepare(output,runtime)
    brief,rows,source_hash=source_material()
    plan=json.loads((output/'plan.json').read_text())
    plan.update(
      id='SEM-408-005',prior_experiments=['SEM-408-003','SEM-408-004'],source_sha256=source_hash,
      candidates=rows,brief=brief,requests_max=2,retries=0,existing_candidates_only=True,new_names=0,paid_api_calls=0,
      purpose='confirm_task_understanding_across_two_distinct_historical_failure_types',
      historical_failure_types={'C002':'instruction_or_brief_leakage','C006':'circular_candidate_grounding'},
      packaging_source='SEM-408-004 byte-equivalent SYSTEM and task_text implementation',
      stop_on_first_nonpass=True,automatic_expansion=False,quality_ground_truth=None,semantic_quality_validated=False)
    (output/'plan.json').write_bytes(base.canonical(plan))


def execute(output:Path):
    plan=json.loads((output/'plan.json').read_text());brief,rows,source_hash=source_material()
    assert plan['id']=='SEM-408-005' and source_hash==plan['source_sha256'] and plan['candidates']==rows
    results=[];stopped_early=False
    for index,row in enumerate(rows,1):
        root=output/f'review-{index}-{row["id"]}';root.mkdir()
        prompt=four.task_text(brief,row)
        messages=[{'role':'system','content':SYSTEM},{'role':'user','content':prompt}]
        rendered,_=base.get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
        toks,_=base.get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
        wire={'prompt':toks['tokens'],'n_predict':base.MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':base.SEED,
              'stream':False,'cache_prompt':False,'json_schema':iface.SCHEMA}
        base.save(root/'input.json',{'candidate':row,'prompt':prompt,'system':SYSTEM,'messages':messages,
          'input_tokens':len(toks['tokens']),'blind_single_candidate':True,'existing_candidate_only':True})
        base.save(root/'request.json',wire);base.save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,
          'candidate_id':row['id'],'sequence_index':index,'stop_on_first_nonpass':True})
        start=time.monotonic();record={'id':row['id'],'name':row['name'],'status':'blocked'}
        try:
            body,raw=base.get(ORIGIN+'/completion',wire,300);(root/'response.json').write_bytes(raw)
            answer=body.get('content','').encode();(root/'answer.raw').write_bytes(answer)
            assert body.get('tokens_evaluated')==len(toks['tokens']) and type(body.get('tokens_predicted')) is int and body['tokens_predicted']<=base.MAX_OUTPUT
            assert not body.get('truncated') and (body.get('stop_type') in ('eos','word') or body.get('stopped_eos') or body.get('stopped_word'))
            review=base.parse(answer,row['id']);base.save(root/'parsed.json',review)
            gate_result=gate.evaluate(row['name'],review);base.save(root/'task-gate.json',gate_result)
            record.update(status='review_complete_not_truth',review=review,task_gate=gate_result,
                          semantic_evidence_eligible=gate_result['eligible_for_semantic_evidence'],
                          input_tokens=body['tokens_evaluated'],output_tokens=body['tokens_predicted'])
        except Exception as error:
            record['error']=repr(error)
        record['seconds']=time.monotonic()-start;base.save(root/'result.json',record);results.append(record)
        if record.get('task_gate',{}).get('task_understanding')!='pass':
            stopped_early=True
        summary={'id':'SEM-408-005','new_names':0,'paid_api_calls':0,'quality_ground_truth':None,
          'review_model':base.MODEL_REPO,'requests_dispatched':len(results),'requests_max':2,
          'stop_on_first_nonpass':True,'stopped_early':stopped_early,'automatic_expansion':False,
          'semantic_quality_validated':False,'results':results}
        (output/'summary.json').write_bytes(base.canonical(summary))
        print(json.dumps(record,ensure_ascii=False),flush=True)
        if stopped_early:break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args();prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
