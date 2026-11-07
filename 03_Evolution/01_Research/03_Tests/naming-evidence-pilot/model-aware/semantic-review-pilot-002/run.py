"""SEM-408-002: interface-only retry of blind single-candidate Gemma review.

Same candidates, brief, blindness, model, sampling and semantic task as
SEM-408-001. Only the execution interface changes: an explicit system execution
instruction and llama.cpp json_schema output constraint. SEM-408-001 remains
blocked and is never rescored.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
BASE_PATH=HOME/'semantic-review-pilot/run.py'
spec=importlib.util.spec_from_file_location('sem408001',BASE_PATH)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
ORIGIN='http://127.0.0.1:8083'

SCHEMA={
  'type':'object','additionalProperties':False,
  'properties':{
    'id':{'type':'string'},
    'observable_form':{'type':'array','minItems':1,'maxItems':3,'items':{'type':'string'}},
    'pronunciation_uncertainty':{'type':'object','additionalProperties':False,'properties':{
      'level':{'type':'string','enum':['low','medium','high']},'reason':{'type':'string'}},'required':['level','reason']},
    'brief_fit':{'type':'object','additionalProperties':False,'properties':{
      'level':{'type':'string','enum':['strong','mixed','weak']},'reason':{'type':'string'}},'required':['level','reason']},
    'association_hypotheses':{'type':'array','maxItems':3,'items':{'type':'string'}},
    'disposition':{'type':'string','enum':['advance','hold','stop']},
    'reason':{'type':'string'}
  },
  'required':['id','observable_form','pronunciation_uncertainty','brief_fit','association_hypotheses','disposition','reason']
}
SYSTEM=('Execute the naming-semantics review task in the user message. Do not summarize, '
        'describe, praise, critique, or restate the task itself. Perform the requested review '
        'for the single candidate and return exactly one JSON object matching the requested '
        'fields. No Markdown and no text outside the JSON object.')


def prepare(output:Path,runtime:Path):
    base.prepare(output,runtime)
    plan=json.loads((output/'plan.json').read_text())
    plan.update(id='SEM-408-002',prior_experiment='SEM-408-001',old_results_rescored=False,
      only_interface_change=['explicit_system_execute_not_summarize','llama_cpp_json_schema_constraint'],
      json_schema_sha256=base.sha(base.canonical(SCHEMA)),
      system_instruction_sha256=base.sha(SYSTEM.encode()),
      semantic_task_change=False)
    (output/'plan.json').write_bytes(base.canonical(plan))


def execute(output:Path):
    plan=json.loads((output/'plan.json').read_text());brief,rows,source_hash=base.source_material()
    assert plan['id']=='SEM-408-002' and source_hash==plan['source_sha256'] and rows==plan['candidates'] and brief==plan['brief']
    assert plan['semantic_task_change'] is False and plan['old_results_rescored'] is False
    results=[]
    for index,row in enumerate(rows,1):
        root=output/f'review-{index}-{row["id"]}';root.mkdir()
        prompt=base.question(brief,row)
        messages=[{'role':'system','content':SYSTEM},{'role':'user','content':json.dumps(prompt,ensure_ascii=False,sort_keys=True,indent=2)}]
        rendered,_=base.get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
        toks,_=base.get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
        wire={'prompt':toks['tokens'],'n_predict':base.MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':base.SEED,
              'stream':False,'cache_prompt':False,'json_schema':SCHEMA}
        base.save(root/'input.json',{'candidate':row,'prompt':prompt,'system':SYSTEM,'messages':messages,
          'input_tokens':len(toks['tokens']),'semantic_task_same_as_001':True})
        base.save(root/'request.json',wire);base.save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,
          'candidate_id':row['id'],'prior_001_not_rescored':True})
        start=time.monotonic();record={'id':row['id'],'name':row['name'],'status':'blocked'}
        try:
            body,raw=base.get(ORIGIN+'/completion',wire,300);(root/'response.json').write_bytes(raw)
            answer=body.get('content','').encode();(root/'answer.raw').write_bytes(answer)
            assert body.get('tokens_evaluated')==len(toks['tokens']) and type(body.get('tokens_predicted')) is int and body['tokens_predicted']<=base.MAX_OUTPUT
            assert not body.get('truncated') and (body.get('stop_type') in ('eos','word') or body.get('stopped_eos') or body.get('stopped_word'))
            review=base.parse(answer,row['id']);base.save(root/'parsed.json',review)
            record.update(status='review_complete_not_truth',review=review,input_tokens=body['tokens_evaluated'],output_tokens=body['tokens_predicted'])
        except Exception as error:
            record['error']=repr(error)
        record['seconds']=time.monotonic()-start;base.save(root/'result.json',record);results.append(record)
        summary={'id':'SEM-408-002','prior_experiment':'SEM-408-001','old_results_rescored':False,'new_names':0,
          'paid_api_calls':0,'quality_ground_truth':None,'review_model':base.MODEL_REPO,'requests_dispatched':index,
          'interface_change_only':True,'results':results}
        (output/'summary.json').write_bytes(base.canonical(summary))
        print(json.dumps(record,ensure_ascii=False),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args();prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
