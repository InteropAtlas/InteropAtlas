"""SEM-408-004: one existing-candidate task-understanding canary.

No name generation. Exactly one existing DEV-02 candidate (C003 / Linetap) is
reviewed by the same Gemma 3 4B Q4_K_M family used in SEM-408-003. The task
packaging now makes the name/product level explicit. The response is checked by
the frozen deterministic task-understanding gate. Gate pass is eligibility for
later semantic analysis only; it is not name-quality truth.
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
GATE_PATH=HOME/'semantic-review-task-gate/gate.py'
ORIGIN='http://127.0.0.1:8085'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

base=load('sem408001',BASE_PATH)
iface=load('sem408002',IFACE_PATH)
gate=load('sem408taskgate',GATE_PATH)

SYSTEM=(
  'Review exactly one candidate name as an identity label for the frozen brief. '
  'Judge the label itself, not whether the label performs the product workflow. '
  'Do not require the label to implement, enumerate, or literally describe product capabilities. '
  'Keep candidate observations separate from the brief and from these instructions. '
  'Return exactly one JSON object matching the server-enforced schema. '
  'Do not restate these instructions in field values.'
)


def source_material():
    brief,rows,source_hash=base.source_material()
    row=next(v for v in rows if v=={'id':'C003','name':'Linetap'})
    return brief,row,source_hash


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

Task boundary:
- The candidate is an identity label for the product, not the product implementation itself.
- Evaluate whether the label can plausibly serve the brief; do not require the label itself to perform, enumerate, or literally encode product functions.
- Treat the frozen brief only as comparison context. Do not describe words from the brief or instructions as if they were visible features or associations of the candidate.

Evaluate these dimensions independently:
1. observable_form: 1-3 concrete observations grounded in the visible spelling. At least one observation must quote the exact candidate name "{row['name']}". Do not invent etymology.
2. pronunciation_uncertainty: low, medium, or high from the visible spelling only, with a candidate-specific reason.
3. brief_fit: strong, mixed, or weak against the frozen brief. Explain identity-label fit; do not require literal feature encoding.
4. association_hypotheses: up to three plausible user/language associations. State them as hypotheses needing validation, not facts. An empty list is allowed.
5. disposition: advance, hold, or stop for intrinsic semantic research priority only, with a candidate-specific reason.

Do not claim trademark, domain, collision, registration, market presence, legal status, or other reality facts. You have no other candidates, no prior ranking, no generator explanation, no owner preference, and no screening evidence.'''


def prepare(output:Path,runtime:Path):
    base.prepare(output,runtime)
    brief,row,source_hash=source_material()
    plan=json.loads((output/'plan.json').read_text())
    plan.update(
      id='SEM-408-004',prior_experiments=['SEM-408-001','SEM-408-002','SEM-408-003'],
      source_sha256=source_hash,candidates=[row],brief=brief,requests=1,
      existing_candidate_only=True,new_names=0,paid_api_calls=0,
      purpose='qualify_reviewer_task_understanding_not_measure_name_quality',
      task_boundary_changed=True,
      changed_only=['explicit_identity_label_vs_product_implementation_boundary','task_understanding_gate_after_parse'],
      unchanged=['source_pool','candidate_identity','brief','review_model','weights','sampling','review_dimensions','json_schema'],
      task_gate='semantic-review-task-gate/gate.py',
      stop_after_one_request=True,automatic_expansion=False,
      quality_ground_truth=None,semantic_quality_validated=False)
    (output/'plan.json').write_bytes(base.canonical(plan))


def execute(output:Path):
    plan=json.loads((output/'plan.json').read_text());brief,row,source_hash=source_material()
    assert plan['id']=='SEM-408-004' and source_hash==plan['source_sha256']
    assert plan['candidates']==[row] and plan['requests']==1 and plan['stop_after_one_request']
    root=output/f'review-1-{row["id"]}';root.mkdir()
    prompt=task_text(brief,row)
    messages=[{'role':'system','content':SYSTEM},{'role':'user','content':prompt}]
    rendered,_=base.get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
    toks,_=base.get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
    wire={'prompt':toks['tokens'],'n_predict':base.MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':base.SEED,
          'stream':False,'cache_prompt':False,'json_schema':iface.SCHEMA}
    base.save(root/'input.json',{'candidate':row,'prompt':prompt,'system':SYSTEM,'messages':messages,
      'input_tokens':len(toks['tokens']),'blind_single_candidate':True,'existing_candidate_only':True})
    base.save(root/'request.json',wire);base.save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,
      'candidate_id':row['id'],'max_requests_in_experiment':1})
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
    record['seconds']=time.monotonic()-start;base.save(root/'result.json',record)
    summary={'id':'SEM-408-004','new_names':0,'paid_api_calls':0,'quality_ground_truth':None,
      'review_model':base.MODEL_REPO,'requests_dispatched':1,'automatic_expansion':False,
      'semantic_quality_validated':False,'result':record}
    (output/'summary.json').write_bytes(base.canonical(summary))
    print(json.dumps(record,ensure_ascii=False),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args();prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
