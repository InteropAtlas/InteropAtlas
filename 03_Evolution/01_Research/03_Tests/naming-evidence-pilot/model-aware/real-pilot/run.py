"""REAL-408-001: genuine CPU inference on frozen v91 code; no answer repair.
Run from the existing model-aware directory. A synthetic task is not a mock
model call. No adoption, independent-review or target-user-device claim.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = Path(__file__).resolve().parent
HOME = HERE.parent
sys.path.insert(0, str(HOME))
import protocol as p
import local_runner as r
import workflow as w

BASE = 'e5d538964e15db5f84d2c73296a5d033b9e2f68f'
LLAMA = '56381e407c0ccfb3a6f71e668a27a901001d22ce'
MODEL_REPO = 'unsloth/Qwen3-4B-Instruct-2507-GGUF'
TASK_ID = 'DEV-02'
ORDER = [('redesign',411921),('simple',411921),('simple',411922),('redesign',411922)]
ORIGIN = 'http://127.0.0.1:8081'
TIME_CAP = 1200


def get(url, body=None, timeout=60):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    request = urllib.request.Request(url, data=p.canonical(body) if body is not None else None,
                                    headers={'User-Agent':'InteropAtlas-REAL-408-001','Content-Type':'application/json'})
    with opener.open(request, timeout=timeout) as response:
        raw = response.read(16*1024*1024+1)
    if len(raw)>16*1024*1024:
        raise ValueError('response_size_limit')
    return json.loads(raw), raw


def save(path, value):
    p.write_new(path, value)


def setup(output, runtime):
    output.mkdir(parents=True, exist_ok=False)
    runtime.mkdir(parents=True, exist_ok=True)
    meta, raw = get('https://huggingface.co/api/models/'+MODEL_REPO+'?blobs=true')
    (output/'hub-model.json').write_bytes(raw)
    revision=meta['sha']
    choices=[s for s in meta['siblings'] if s['rfilename'].endswith('-Q4_K_M.gguf')]
    if len(choices)!=1: raise ValueError('exact_quantized_file_unresolved')
    selected=choices[0]
    filename=selected['rfilename']; lfs=selected.get('lfs',{})
    if not (0<lfs.get('size',0)<3_000_000_000 and lfs.get('sha256')):
        raise ValueError('model_size_or_lfs_identity_unresolved')
    url='https://huggingface.co/'+MODEL_REPO+'/resolve/'+revision+'/'+filename
    model=runtime/'model.gguf'
    started=time.monotonic(); digest=hashlib.sha256(); total=0
    with urllib.request.urlopen(url,timeout=180) as source, model.open('xb') as target:
        while chunk:=source.read(4*1024*1024):
            total+=len(chunk)
            if total>lfs['size']: raise ValueError('download_overrun')
            target.write(chunk); digest.update(chunk)
    if digest.hexdigest()!=lfs['sha256'] or total!=lfs['size']:
        raise ValueError('weight_hash_mismatch')
    config=p.read(HOME/'experiment.json')
    task=next(t for t in p.read(HOME/'development-tasks.json')['tasks'] if t['id']==TASK_ID)
    assert config['budgets']['max_output_tokens_per_call']==2000
    identity={'model_repo':MODEL_REPO,'revision':revision,'filename':filename,'weights_sha256':digest.hexdigest(),
              'size_bytes':total,'quantization':'Q4_K_M','model_family':'Qwen3-4B-Instruct-2507',
              'llama_cpp_commit':LLAMA,'download_seconds':time.monotonic()-started,
              'execution_site':'GitHub standard public-repository CPU runner, not Owner machine',
              'cpu':subprocess.check_output(['lscpu'],text=True),
              'source_sha256':w.source_hashes(),'task_sha256':p.digest(p.canonical(task)),
              'created_at':r.now()}
    save(output/'identity.json',identity)
    save(output/'preregistered-plan.json',{'id':'REAL-408-001','baseline':BASE,'task':task,
        'order':ORDER,'caps':config['budgets'],'global_max_calls':20,'inference_time_cap_seconds':TIME_CAP,
        'transport':'llama.cpp native tokenized completion, no semantic prompt edits',
        'temperature':0.7,'top_p':0.9,'context_tokens':8192,'retries':0,
        'runtime_controller':'frozen v91 workflow, no developer answer repair',
        'primary_observations':['completion_or_failure_stage','raw_candidates_and_reviews','tokens_and_walltime','rejection_audit_disagreement'],
        'quality_review':'post_run_author_audit_only_no_independent_reviewer','adoption':'not_assessed',
        'limits':'One fictional task, two seeds, one 4B quantization. No causal/general/Owner-Qwen effectiveness conclusion.'})
    print(json.dumps({'stage':'weights_verified','revision':revision,'sha256':digest.hexdigest(),'bytes':total}),flush=True)


class Backend:
    def __init__(self, identity, started, overall):
        self.identity=identity; self.started=started; self.overall=overall

    def __call__(self, root, plan, step, task, role, limit):
        if time.monotonic()-self.started>TIME_CAP: raise ValueError('global_time_cap')
        records=[p.read(f) for f in (root/'calls').glob('*/record.json')]
        reservations=list((root/'calls').glob('*/dispatch-intent.json'))
        if len(reservations)>=6 or self.overall[0]>=20: raise ValueError('call_budget')
        if sum(p.read(f)['reserved_tokens'] for f in reservations)+limit>12000: raise ValueError('token_reservation_budget')
        config=copy.deepcopy(plan['config'])
        profile=config['profiles']['local']
        profile.update(deployment_id='REAL-408-001-Qwen4B',revision=self.identity['revision'],
            quantization='Q4_K_M',runtime_version='llama.cpp@'+LLAMA,context_limit_tokens=8192,
            token_counter='llama.cpp.loaded.tokenize',reasoning_mode='instruct_non_thinking',
            sampling={'temperature':0.7,'top_p':0.9,'seed':plan['seed']},identity_verified=True,
            execution_location='local',billing='unmetered_local',roles={x:'untested' for x in p.ROLES})
        config['authorization'].update(model_trials=True,diagnostic_untested_roles=True)
        current=copy.deepcopy(task)
        current['context']={'actual_level':'fresh_context','evidence_ref':'calls/'+step+'/request.json',
                            'limits':'Stateless tokenized input; same model, not independent experts.'}
        packet=p.packet(config,current,'local',plan['method'],role)
        packet['max_output_tokens']=limit
        messages=[{'role':'system','content':r.SYSTEM},{'role':'user','content':p.canonical(packet['model_input']).decode()}]
        rendered, rendered_raw=get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True})
        tokenized, tokenized_raw=get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True})
        tokens=tokenized['tokens']
        if not tokens or not all(type(x) is int for x in tokens): raise ValueError('bad_token_ids')
        packet.update(input_tokens=len(tokens),token_counter=profile['token_counter'])
        usage={'calls':len(reservations),'packet_attempts':0,'cloud_calls':0,'cloud_spend':0,
               'output_tokens':sum(f['reserved_tokens'] for f in map(p.read,reservations))}
        pre=p.preflight(config,packet,usage)
        if not pre['dispatch_allowed']: raise ValueError('preflight:'+str(pre['blockers']))
        call=root/'calls'/step;call.mkdir(parents=True,exist_ok=False)
        wire={'prompt':tokens,'n_predict':limit,'temperature':0.7,'top_p':0.9,'seed':plan['seed'],
              'stream':False,'cache_prompt':False}
        save(call/'packet.json',packet);save(call/'messages.json',{'messages':messages})
        (call/'rendered-prompt.txt').write_text(rendered['prompt'])
        (call/'tokenization.json').write_bytes(tokenized_raw)
        save(call/'request.json',wire)
        save(call/'dispatch-intent.json',{'started_at':r.now(),'reserved_tokens':limit,'request_sha256':p.digest(p.canonical(wire)),
            'backend':'real_llama_cpp_weights','local_to_runner_not_owner':True,'no_automatic_retry':True})
        self.overall[0]+=1
        start=r.now(); clock=time.monotonic(); raw=b''; body={}; content=b''; failure=None; outcome='failed'
        try:
            body,raw=get(ORIGIN+'/completion',wire,timeout=300)
            (call/'response.json').write_bytes(raw)
            content=body.get('content','').encode('utf-8')
            predicted=body.get('tokens_predicted'); evaluated=body.get('tokens_evaluated')
            ended_normally=(body.get('stop_type') in ('eos','word') or body.get('stopped_eos') is True or body.get('stopped_word') is True)
            outcome='completed' if content.strip() and ended_normally and not body.get('truncated') and evaluated==len(tokens) and type(predicted) is int and predicted<=limit else 'invalid_output'
        except Exception as error:
            failure=repr(error)
            if isinstance(error,urllib.error.HTTPError): (call/'http-error.raw').write_bytes(error.read())
        (call/'output.txt').write_bytes(content)
        receipt={'run_id':root.name+'-'+step,'record_kind':'synthetic','execution_kind':'actual_cpu_model_on_synthetic_task',
                 'execution_ref':'calls/'+step+'/response.json','dispatch_evidence_ref':'calls/'+step+'/dispatch-intent.json',
                 'runtime_fingerprint':p.fingerprint(profile),'started_at':start,'ended_at':r.now(),
                 'outcome':outcome,'input_tokens':body.get('tokens_evaluated'),'output_tokens':body.get('tokens_predicted'),
                 'costs':{'cloud_spend':0,'setup_spend':None,'owner_minutes':0,'local_seconds':time.monotonic()-clock,'currency':'USD'},
                 'error':failure,'backend_model_execution_confirmed':bool(raw),'weights_sha256':self.identity['weights_sha256']}
        record=p.capture(packet,content,receipt);save(call/'record.json',record)
        print(json.dumps({'cell':root.name,'step':step,'outcome':outcome,'output_tokens':receipt['output_tokens'],
                          'seconds':receipt['costs']['local_seconds'],'error':failure}),flush=True)
        if outcome!='completed' or record['violations']: raise ValueError('transport_or_output_invalid:'+step)
        return content,'calls/'+step+'/record.json',receipt['execution_kind']


def execute(output):
    identity=p.read(output/'identity.json'); started=time.monotonic();overall=[0]
    config=p.read(HOME/'experiment.json')
    task=next(t for t in p.read(HOME/'development-tasks.json')['tasks'] if t['id']==TASK_ID)
    results=[]
    for i,(method,seed) in enumerate(ORDER):
        label='cell-'+str(i+1)+'-'+method+'-'+str(seed)
        if time.monotonic()-started>TIME_CAP:
            results.append({'cell':label,'method':method,'seed':seed,'status':'not_run_time_cap'});continue
        root=output/label
        runtime={'endpoint':ORIGIN,'model_id':'REAL-408-001-Qwen4B','revision':identity['revision'],'runtime_version':'llama.cpp@'+LLAMA}
        w.initialize(root,config,task,runtime,method,1,seed,False)
        try:
            report=w.advance(root,True,Backend(identity,started,overall))
            error=None
        except Exception as exc:
            error=repr(exc)
            report=p.read(root/'report.json') if (root/'report.json').exists() else {'status':'failed'}
        files=list((root/'calls').glob('*/record.json'));records=[p.read(x) for x in files]
        result={'cell':label,'method':method,'seed':seed,'status':report['status'],'error':error,
                'calls':len(records),'input_tokens':sum(x['receipt']['input_tokens'] or 0 for x in records),
                'output_tokens':sum(x['receipt']['output_tokens'] or 0 for x in records),
                'unknown_token_receipts':sum(x['receipt']['output_tokens'] is None for x in records),
                'inference_seconds':sum(x['receipt']['costs']['local_seconds'] for x in records)}
        if (root/'round-1.json').exists():
            rnd=p.read(root/'round-1.json')
            result.update(candidate_count=len(rnd['pool']),shortlisted=len(rnd['intrinsic_shortlist_ids']),
                          audit_disagreements=len(rnd['audit_disagreement_ids']),duplicates=rnd['exact_duplicates_removed'])
        results.append(result)
        projection={'experiment_id':'REAL-408-001','created_at':r.now(),'real_inference_attempts':overall[0],
                    'paid_inference_api_calls':0,'task_kind':'synthetic','model_execution':'real',
                    'cells':results,'adoption':'not_assessed','independent_semantic_review':'not_performed',
                    'causal_effectiveness':'not_established','user_model_validation':'not_performed'}
        (output/'summary.json').write_bytes(p.canonical(projection))
        print(json.dumps(result),flush=True)
    save(output/'completed.json',{'finished_at':r.now(),'attempts':overall[0],'cells_recorded':len(results)})


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['setup','execute'])
    parser.add_argument('--output',type=Path,required=True);parser.add_argument('--runtime',type=Path)
    args=parser.parse_args()
    if args.command=='setup': setup(args.output,args.runtime)
    else: execute(args.output)
