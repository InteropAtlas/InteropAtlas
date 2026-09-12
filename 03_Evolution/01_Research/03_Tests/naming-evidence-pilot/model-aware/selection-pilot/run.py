"""SELECT-408-001: four bounded real selection requests, zero name generation."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import urllib.request

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
sys.path.insert(0,str(HOME))
import protocol as p
import local_runner as r
import selection_policy as s
import format_adapter as f
import workflow as w

ORIGIN='http://127.0.0.1:8081'
SOURCE='real-pilot-003/results/evidence.json'
ORDER=[('cell-2-simple-411921','old',411921),('cell-2-simple-411921','new',411921),
       ('cell-3-simple-411922','new',411922),('cell-3-simple-411922','old',411922)]

def request(path,body):
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
    q=urllib.request.Request(ORIGIN+path,data=p.canonical(body),headers={'Content-Type':'application/json'})
    with opener.open(q,timeout=300) as response: raw=response.read(8_000_001)
    if len(raw)>8_000_000:raise ValueError('response_cap')
    return json.loads(raw),raw

def prepare(output,runtime):
    output.mkdir(parents=True,exist_ok=False);runtime.mkdir(parents=True,exist_ok=True)
    identity=p.read(HOME/'real-pilot-003/results/identity.json')
    assert identity['revision']=='a06e946bb6b655725eafa393f4a9745d460374c9'
    assert identity['weights_sha256']=='3605803b982cb64aead44f6c1b2ae36e3acdb41d8e46c8a94c6533bc4c67e597'
    p.write_new(output/'plan.json',{'id':'SELECT-408-001','order':ORDER,'source_sha256':p.digest((HOME/SOURCE).read_bytes()),
        'model':identity,'source_hashes':w.source_hashes(),'requests':4,'new_names':0,'per_request_max_output_tokens':2000,
        'per_request_timeout_seconds':300,'retries':0,'temperature':0.7,'top_p':0.9,
        'changed_factors':'typed_creator_intent, risk_not_input, evidence_instruction_bundle',
        'questions':['complete IDs','unsupported risk rationale','priority/hold/not_pursued','cost'],
        'independent_review':False,'held_out':False,'quality_ground_truth':None})
    url='https://huggingface.co/'+identity['model_repo']+'/resolve/'+identity['revision']+'/'+identity['filename']
    count=0;sha=hashlib.sha256()
    with urllib.request.urlopen(url,timeout=180) as response,(runtime/'model.gguf').open('xb') as out:
        while block:=response.read(4*1024*1024):
            count+=len(block)
            if count>3_000_000_000:raise ValueError('model_size_cap')
            out.write(block);sha.update(block)
    assert count==identity['size_bytes'] and sha.hexdigest()==identity['weights_sha256']
    p.write_new(output/'runtime-identity.json',{'weights_sha256':sha.hexdigest(),'llama_cpp_commit':identity['llama_cpp_commit'],
        'cpu':subprocess.check_output(['lscpu'],text=True),'model_revision':identity['revision'],'user_machine':False})

def execute(output):
    frozen=p.read(output/'plan.json');ev=p.read(HOME/SOURCE)['files']
    assert p.digest((HOME/SOURCE).read_bytes())==frozen['source_sha256']
    for val in ev.values():assert p.digest(val['content'].encode())==val['sha256']
    assert w.source_hashes()==frozen['source_hashes']
    cfg=p.read(HOME/'experiment.json');cfg['authorization'].update(model_trials=True,diagnostic_untested_roles=True)
    profile=cfg['profiles']['local']
    profile.update(deployment_id='SELECT-408-001-Qwen4B',revision=frozen['model']['revision'],quantization='Q4_K_M',
        runtime_version='llama.cpp@'+frozen['model']['llama_cpp_commit'],context_limit_tokens=8192,
        token_counter='llama.cpp.loaded.tokenize',reasoning_mode='instruct_non_thinking',identity_verified=True,
        execution_location='local',billing='unmetered_local')
    results=[]
    for index,(cell,arm,seed) in enumerate(ORDER):
        root=output/('request-'+str(index+1));root.mkdir()
        original=json.loads(ev['model/'+cell+'/steps/r1explained/input.json']['content'])
        task=copy.deepcopy(original['task']);question=json.loads(task['question']);rows=question['items']
        assert len(rows)==6
        if arm=='new':task['question']=s.review_question('with_explanation',rows)
        task['context']={'actual_level':'fresh_context','evidence_ref':'request.json','limits':'same model, not independent experts'}
        profile['sampling']={'temperature':0.7,'top_p':0.9,'seed':seed}
        packet=p.packet(cfg,task,'local','simple','select')
        messages=[{'role':'system','content':r.SYSTEM},{'role':'user','content':p.canonical(packet['model_input']).decode()}]
        rendered,_=request('/apply-template',{'messages':messages,'add_generation_prompt':True})
        tokenized,_=request('/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True})
        tokens=tokenized['tokens'];packet.update(input_tokens=len(tokens),token_counter='llama.cpp.loaded.tokenize')
        check=p.preflight(cfg,packet,{'calls':index,'packet_attempts':0,'cloud_calls':0,'cloud_spend':0,'output_tokens':index*2000})
        assert check['dispatch_allowed'],check
        wire={'prompt':tokens,'n_predict':2000,'temperature':0.7,'top_p':0.9,'seed':seed,'stream':False,'cache_prompt':False}
        p.write_new(root/'input.json',{'arm':arm,'source_cell':cell,'seed':seed,'packet':packet,'messages':messages})
        p.write_new(root/'request.json',wire)
        p.write_new(root/'intent.json',{'started_at':r.now(),'reserved_output_tokens':2000,'retry':False})
        start=time.monotonic();result={'arm':arm,'source_cell':cell,'seed':seed,'request':index+1,'status':'blocked'}
        try:
            body,raw=request('/completion',wire);(root/'response.json').write_bytes(raw)
            answer=body['content'].encode();(root/'answer.raw').write_bytes(answer)
            result.update(input_tokens=body.get('tokens_evaluated'),output_tokens=body.get('tokens_predicted'))
            assert body.get('tokens_evaluated')==len(tokens) and type(body.get('tokens_predicted')) is int and body['tokens_predicted']<=2000
            assert not body.get('truncated') and (body.get('stop_type') in ('eos','word') or body.get('stopped_eos') or body.get('stopped_word'))
            normalized,audit=f.normalize(answer,json.loads(task['question']));p.write_new(root/'normalization.json',audit)
            assert not audit['action'].startswith('refused_'),audit
            (root/'normalized.json').write_bytes(normalized)
            reviewed=w.reviews(json.loads(normalized),[v['id'] for v in rows])
            result.update(status='selection_complete_not_clearance',reviews=reviewed,queues=s.resource_queues({'pool':rows,'explained':reviewed}),
                          generator_risk_in_model_input=(arm=='old'))
        except Exception as error:
            result['error']=repr(error)
        result['seconds']=time.monotonic()-start
        p.write_new(root/'result.json',result);results.append(result)
        (output/'summary.json').write_bytes(p.canonical({'id':'SELECT-408-001','requests_dispatched':index+1,'new_names':0,
            'paid_api_calls':0,'independent_quality_review':False,'causal_method_winner':'not_established','results':results}))
        print(json.dumps(result,ensure_ascii=False),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args()
    if a.command=='prepare':prepare(a.output,a.runtime)
    else:execute(a.output)
