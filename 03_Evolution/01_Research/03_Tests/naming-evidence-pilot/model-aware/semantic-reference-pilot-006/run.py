"""SEM-408-006: bounded independent-family reference opinions for frozen packet 001.

This is not name generation and not ground truth. It runs exactly the four existing
DEV-02 names frozen in SEM-408-REF-PACKET-001 through Mistral-Nemo 12B Q4_K_M.
No retry, no reality search, no method labels, no prior decisions, no automatic
expansion. Results are reference opinions for later claim-level calibration only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import urllib.request

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
PACKET=HOME/'semantic-validation-contract/reference-packet-001.json'
MODEL_REPO='bartowski/Mistral-Nemo-Instruct-2407-GGUF'
MODEL_FILE='Mistral-Nemo-Instruct-2407-Q4_K_M.gguf'
EXPECTED_SHA256='7c1a10d202d8788dbe5628dc962254d10654c853cae6aaeca0618f05490d4a46'
LLAMA='56381e407c0ccfb3a6f71e668a27a901001d22ce'
ORIGIN='http://127.0.0.1:8087'
SEED=64006
MAX_OUTPUT=900

SCHEMA={
  'type':'object','additionalProperties':False,
  'properties':{
    'id':{'type':'string'},
    'observable_form':{'type':'array','minItems':1,'maxItems':3,'items':{'type':'object','additionalProperties':False,'properties':{
      'claim':{'type':'string'},'evidence_class':{'type':'string','enum':['observable','unknown']},'reason':{'type':'string'}},'required':['claim','evidence_class','reason']}},
    'pronunciation':{'type':'object','additionalProperties':False,'properties':{
      'candidate_readings':{'type':'array','maxItems':3,'items':{'type':'string'}},
      'uncertainty':{'type':'string','enum':['low','medium','high','unknown']},
      'evidence_class':{'type':'string','enum':['hypothesis','supported','unknown']},'reason':{'type':'string'}},'required':['candidate_readings','uncertainty','evidence_class','reason']},
    'associations':{'type':'array','maxItems':3,'items':{'type':'object','additionalProperties':False,'properties':{
      'claim':{'type':'string'},'evidence_class':{'type':'string','enum':['hypothesis','supported','unknown']},'reason':{'type':'string'}},'required':['claim','evidence_class','reason']}},
    'brief_fit':{'type':'object','additionalProperties':False,'properties':{
      'level':{'type':'string','enum':['strong','mixed','weak','unknown']},'reason':{'type':'string'},'confidence':{'type':'string','enum':['low','medium','high']}},'required':['level','reason','confidence']},
    'hard_failure':{'type':'array','maxItems':3,'items':{'type':'object','additionalProperties':False,'properties':{
      'code':{'type':'string'},'reason':{'type':'string'},'evidence_class':{'type':'string','enum':['supported','unknown']}},'required':['code','reason','evidence_class']}},
    'research_priority':{'type':'string','enum':['priority','hold','not_pursued']},
    'priority_reason':{'type':'string'}
  },
  'required':['id','observable_form','pronunciation','associations','brief_fit','hard_failure','research_priority','priority_reason']
}
SYSTEM=(
  'Act as an independent naming reference reviewer for exactly one frozen candidate. '
  'Your output is a reference opinion, not ground truth. Separate visible observations from hypotheses. '
  'Do not infer method origin, prior decisions, generator intent, owner preference, trademark/domain/legal facts, or other candidates. '
  'Do not require a name to implement product functions. Return only the JSON object required by the server schema.'
)

def canonical(v):return (json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def sha(raw):return hashlib.sha256(raw).hexdigest()

def get(url,body=None,timeout=300):
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
    req=urllib.request.Request(url,data=canonical(body) if body is not None else None,headers={'User-Agent':'InteropAtlas-SEM-408-006','Content-Type':'application/json'})
    with opener.open(req,timeout=timeout) as response:
        raw=response.read(8_000_001)
    if len(raw)>8_000_000:raise ValueError('response_cap')
    return json.loads(raw),raw

def save(path,value):
    if path.exists():raise FileExistsError(path)
    path.write_bytes(canonical(value))

def load_packet():
    raw=PACKET.read_bytes();p=json.loads(raw)
    assert p['id']=='SEM-408-REF-PACKET-001' and p['status']=='frozen_input_no_reference_judgments_yet'
    assert p['source']['existing_candidates_only'] and p['source']['new_names']==0
    assert len(p['cases'])==4 and not p['reference_status']['independent_reference_obtained']
    return p,sha(raw)

def prompt_for(packet,case):
    b=packet['semantic_brief']
    return f'''Evaluate exactly one existing candidate identity label against this frozen semantic brief.\n\nCandidate ID: {case['packet_id']}\nCandidate name: {case['name']}\n\nObject: {b['object']}\nMission: {b['mission']}\nName jobs: {'; '.join(b['name_jobs'])}\nNon-jobs: {'; '.join(b['non_jobs'])}\nConstraints: {'; '.join(b['constraints'])}\nPreferences: {'; '.join(b['preferences'])}\n\nEvidence rules:\n- observable_form: only claims directly supported by visible spelling/structure.\n- pronunciation: propose readings; unless independently established, use hypothesis or unknown rather than fact.\n- associations: hypotheses unless independently supported; do not invent etymology.\n- brief_fit: judge identity-label fit, not whether the name performs the product workflow.\n- hard_failure: only supported hard failures may justify not_pursued; uncertainty is not a hard failure.\n- research_priority is research allocation only, never adoption or clearance.\n- no reality/legal/domain claims and no Owner preference claims.\n\nReturn the schema fields only.'''

def validate_output(packet,case,v):
    if v.get('id')!=case['packet_id']:raise ValueError('reference_id_mismatch')
    raw=json.dumps(v,ensure_ascii=False).casefold()
    for term in packet['context_only_removed']:
        if term.casefold() in raw:raise ValueError('context_only_metadata_leak:'+term)
    for term in ('simple','redesign','generator risk','owner preference','trademark','domain availability','prior selector'):
        if term in raw:raise ValueError('forbidden_context_or_reality_claim:'+term)
    if case['name'].casefold() not in raw:raise ValueError('candidate_not_grounded_anywhere')
    return True

def prepare(output:Path,runtime:Path):
    output.mkdir(parents=True,exist_ok=False);runtime.mkdir(parents=True,exist_ok=True)
    packet,packet_hash=load_packet()
    meta,meta_raw=get('https://huggingface.co/api/models/'+MODEL_REPO+'?blobs=true',timeout=60)
    revision=meta['sha'];siblings={v['rfilename']:v for v in meta['siblings']};assert MODEL_FILE in siblings
    (output/'hub-model.json').write_bytes(meta_raw)
    url='https://huggingface.co/'+MODEL_REPO+'/resolve/'+revision+'/'+MODEL_FILE
    digest=hashlib.sha256();count=0;start=time.monotonic()
    with urllib.request.urlopen(url,timeout=1200) as src,(runtime/'model.gguf').open('xb') as dst:
        while block:=src.read(8*1024*1024):
            count+=len(block)
            if count>8_500_000_000:raise ValueError('model_size_cap')
            dst.write(block);digest.update(block)
    if digest.hexdigest()!=EXPECTED_SHA256:raise ValueError('model_sha256_mismatch')
    if not 7_000_000_000<count<8_000_000_000:raise ValueError('unexpected_model_size')
    plan={'id':'SEM-408-006','purpose':'independent_family_reference_opinion_not_ground_truth','packet_id':packet['id'],'packet_sha256':packet_hash,
      'cases':packet['cases'],'requests':4,'retries':0,'automatic_expansion':False,'new_names':0,'paid_api_calls':0,'ia_generation':False,'reality_search':False,
      'model_repo':MODEL_REPO,'model_revision':revision,'model_file':MODEL_FILE,'weights_sha256':digest.hexdigest(),'weights_bytes':count,'llama_cpp_commit':LLAMA,
      'temperature':0.2,'top_p':0.9,'seed':SEED,'max_output_tokens':MAX_OUTPUT,'download_seconds':time.monotonic()-start,
      'blindness':packet['blindness'],'quality_ground_truth':None,'method_winner_inference':False}
    save(output/'plan.json',plan)
    save(output/'runtime-identity.json',{'model_repo':MODEL_REPO,'revision':revision,'file':MODEL_FILE,'weights_sha256':digest.hexdigest(),'bytes':count,'llama_cpp_commit':LLAMA,'user_machine':False})

def execute(output:Path):
    packet,packet_hash=load_packet();plan=json.loads((output/'plan.json').read_text())
    assert plan['id']=='SEM-408-006' and plan['packet_sha256']==packet_hash and plan['cases']==packet['cases'] and plan['requests']==4 and plan['retries']==0
    results=[]
    for index,case in enumerate(packet['cases'],1):
        root=output/f'reference-{index}-{case["packet_id"]}';root.mkdir()
        prompt=prompt_for(packet,case);messages=[{'role':'system','content':SYSTEM},{'role':'user','content':prompt}]
        rendered,_=get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
        toks,_=get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
        wire={'prompt':toks['tokens'],'n_predict':MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':SEED,'stream':False,'cache_prompt':False,'json_schema':SCHEMA}
        save(root/'input.json',{'case':case,'semantic_brief':packet['semantic_brief'],'prompt':prompt,'system':SYSTEM,'messages':messages,'input_tokens':len(toks['tokens']),'blindness':packet['blindness']})
        save(root/'request.json',wire);save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,'packet_id':case['packet_id'],'max_requests_in_experiment':4})
        start=time.monotonic();record={'packet_id':case['packet_id'],'source_id':case['source_id'],'name':case['name'],'status':'blocked'}
        try:
            body,raw=get(ORIGIN+'/completion',wire,600);(root/'response.json').write_bytes(raw)
            answer=body.get('content','').encode();(root/'answer.raw').write_bytes(answer)
            if body.get('tokens_evaluated')!=len(toks['tokens']) or type(body.get('tokens_predicted')) is not int or body['tokens_predicted']>MAX_OUTPUT:raise ValueError('usage_or_output_cap')
            if body.get('truncated'):raise ValueError('truncated')
            review=json.loads(answer.decode('utf-8').strip());validate_output(packet,case,review);save(root/'parsed.json',review)
            record.update(status='reference_complete_not_truth',reference=review,input_tokens=body['tokens_evaluated'],output_tokens=body['tokens_predicted'])
        except Exception as error:record['error']=repr(error)
        record['seconds']=time.monotonic()-start;save(root/'result.json',record);results.append(record)
        summary={'id':'SEM-408-006','packet_id':packet['id'],'reference_model':MODEL_REPO,'requests_dispatched':index,'requests_max':4,'retries':0,
          'new_names':0,'paid_api_calls':0,'ia_generation':False,'automatic_expansion':False,'quality_ground_truth':None,'method_winner':None,'results':results}
        (output/'summary.json').write_bytes(canonical(summary));print(json.dumps(record,ensure_ascii=False),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('command',choices=['prepare','execute']);p.add_argument('--output',type=Path,required=True);p.add_argument('--runtime',type=Path);a=p.parse_args()
    prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
