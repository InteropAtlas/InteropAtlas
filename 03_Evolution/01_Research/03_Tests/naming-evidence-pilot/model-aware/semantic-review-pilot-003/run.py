"""SEM-408-003: task-packaging retry for blind single-candidate Gemma review.

Same frozen candidate pool, brief, blindness, model, sampling and review dimensions.
Unlike SEM-408-002, the user message contains no output-contract examples or
placeholder values. JSON schema constrains representation only. The first real
candidate is also a canary: if its answer is still generic/template-like, stop
without dispatching the remaining five requests.
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
IFACE_PATH=HOME/'semantic-review-pilot-002/run.py'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

base=load('sem408001',BASE_PATH)
iface=load('sem408002',IFACE_PATH)
ORIGIN='http://127.0.0.1:8084'
SYSTEM=(
  'Perform the requested naming review for exactly one candidate. Do not summarize, '
  'explain, praise, critique, or restate the instructions. Judge the candidate itself. '
  'Return exactly one JSON object matching the server-enforced schema, with substantive '
  'candidate-specific content. Do not copy instruction phrases as field values.'
)
BANNED=(
  'grounded reason','3 concise observations','3 concise hypotheses','grounded research priority',
  'independent naming semantics reviewer rules','exact input id','low/medium/high','strong/mixed/weak'
)


def task_text(brief,row):
    jobs='; '.join(brief.get('name_jobs',[]))
    constraints='; '.join(brief.get('constraints',[]))
    nonjobs='; '.join(brief.get('non_jobs',[]))
    prefs='; '.join(brief.get('confirmed_preferences',[]))
    return f'''Review one candidate name only.

Candidate ID: {row['id']}
Candidate name: {row['name']}

Frozen brief:
Object: {brief.get('object','')}
Mission: {brief.get('mission','')}
Name jobs: {jobs}
Constraints: {constraints}
Non-jobs: {nonjobs}
Confirmed preferences: {prefs}

Evaluate these dimensions independently:
1. observable_form: 1-3 concrete observations grounded in the visible spelling. At least one observation must quote the exact candidate name "{row['name']}". Do not invent etymology.
2. pronunciation_uncertainty: low, medium, or high from the visible spelling only, with a candidate-specific reason.
3. brief_fit: strong, mixed, or weak against the frozen brief. The bare name does not need to literally encode every product function.
4. association_hypotheses: up to three plausible user/language associations. State them as hypotheses needing validation, not facts. An empty list is allowed.
5. disposition: advance, hold, or stop for intrinsic semantic research priority only, with a candidate-specific reason.

Do not claim trademark, domain, collision, registration, market presence, legal status, or other reality facts. You have no other candidates, no prior ranking, no generator explanation, no owner preference, and no screening evidence.''' 


def substantive(review,row):
    strings=[]
    def walk(v):
        if isinstance(v,str):strings.append(v)
        elif isinstance(v,list):
            for x in v:walk(x)
        elif isinstance(v,dict):
            for x in v.values():walk(x)
    walk(review)
    joined='\n'.join(strings).casefold()
    if any(x in joined for x in BANNED): raise ValueError('template_or_placeholder_echo')
    observations='\n'.join(review['observable_form'])
    if row['name'].casefold() not in observations.casefold(): raise ValueError('candidate_name_not_grounded_in_observation')
    prose=[*review['observable_form'],review['pronunciation_uncertainty']['reason'],review['brief_fit']['reason'],*review['association_hypotheses'],review['reason']]
    if any(len(x.strip())<8 for x in prose): raise ValueError('non_substantive_short_field')
    return True


def prepare(output:Path,runtime:Path):
    base.prepare(output,runtime)
    plan=json.loads((output/'plan.json').read_text())
    plan.update(
      id='SEM-408-003',prior_experiments=['SEM-408-001','SEM-408-002'],old_results_rescored=False,
      semantic_task_packaging_changed=True,
      changed_only=['remove_user_output_contract_examples','plain_language_single_candidate_task','content_canary_gate'],
      unchanged=['candidate_pool','brief','blindness','review_model','weights','sampling','review_dimensions','json_schema'],
      system_instruction_sha256=base.sha(SYSTEM.encode()),json_schema_sha256=base.sha(base.canonical(iface.SCHEMA)),
      first_real_candidate_is_canary=True,canary_failure_stops_remaining_requests=True)
    (output/'plan.json').write_bytes(base.canonical(plan))


def execute(output:Path):
    plan=json.loads((output/'plan.json').read_text());brief,rows,source_hash=base.source_material()
    assert plan['id']=='SEM-408-003' and source_hash==plan['source_sha256'] and rows==plan['candidates'] and brief==plan['brief']
    results=[];canary_passed=False
    for index,row in enumerate(rows,1):
        root=output/f'review-{index}-{row["id"]}';root.mkdir()
        prompt=task_text(brief,row)
        messages=[{'role':'system','content':SYSTEM},{'role':'user','content':prompt}]
        rendered,_=base.get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
        toks,_=base.get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
        wire={'prompt':toks['tokens'],'n_predict':base.MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':base.SEED,
              'stream':False,'cache_prompt':False,'json_schema':iface.SCHEMA}
        base.save(root/'input.json',{'candidate':row,'prompt':prompt,'system':SYSTEM,'messages':messages,
          'input_tokens':len(toks['tokens']),'blind_single_candidate':True})
        base.save(root/'request.json',wire);base.save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,
          'candidate_id':row['id'],'prior_results_not_rescored':True})
        start=time.monotonic();record={'id':row['id'],'name':row['name'],'status':'blocked'}
        try:
            body,raw=base.get(ORIGIN+'/completion',wire,300);(root/'response.json').write_bytes(raw)
            answer=body.get('content','').encode();(root/'answer.raw').write_bytes(answer)
            assert body.get('tokens_evaluated')==len(toks['tokens']) and type(body.get('tokens_predicted')) is int and body['tokens_predicted']<=base.MAX_OUTPUT
            assert not body.get('truncated') and (body.get('stop_type') in ('eos','word') or body.get('stopped_eos') or body.get('stopped_word'))
            review=base.parse(answer,row['id']);substantive(review,row);base.save(root/'parsed.json',review)
            record.update(status='review_complete_not_truth',review=review,input_tokens=body['tokens_evaluated'],output_tokens=body['tokens_predicted'])
        except Exception as error:
            record['error']=repr(error)
        record['seconds']=time.monotonic()-start;base.save(root/'result.json',record);results.append(record)
        if index==1:
            canary_passed=record['status']=='review_complete_not_truth'
        summary={'id':'SEM-408-003','prior_experiments':['SEM-408-001','SEM-408-002'],'old_results_rescored':False,
          'semantic_task_packaging_changed':True,'new_names':0,'paid_api_calls':0,'quality_ground_truth':None,
          'review_model':base.MODEL_REPO,'requests_dispatched':index,'canary_passed':canary_passed,'results':results}
        (output/'summary.json').write_bytes(base.canonical(summary))
        print(json.dumps(record,ensure_ascii=False),flush=True)
        if index==1 and not canary_passed:
            break

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args();prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
