"""SEM-408-001: blind single-candidate semantic review using a different model family.

No name generation. Reviewer sees the frozen brief and exactly one bare name per
request; it does not see Qwen decisions, creator intent/risk, method origin,
other candidates, reality screening or owner preference. Cross-model agreement
is not ground truth.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.request

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
SOURCE=HOME/'real-pilot-003/results/evidence.json'
SOURCE_CELL='cell-2-simple-411921'
MODEL_REPO='ggml-org/gemma-3-4b-it-GGUF'
MODEL_FILE='gemma-3-4b-it-Q4_K_M.gguf'
LLAMA='56381e407c0ccfb3a6f71e668a27a901001d22ce'
ORIGIN='http://127.0.0.1:8082'
SEED=63001
MAX_OUTPUT=900


def canonical(v):
    return (json.dumps(v,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()


def get(url,body=None,timeout=300):
    opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
    req=urllib.request.Request(url,data=canonical(body) if body is not None else None,
        headers={'User-Agent':'InteropAtlas-SEM-408-001','Content-Type':'application/json'})
    with opener.open(req,timeout=timeout) as response: raw=response.read(8_000_001)
    if len(raw)>8_000_000: raise ValueError('response_cap')
    return json.loads(raw),raw


def save(path,value):
    if path.exists(): raise FileExistsError(path)
    path.write_bytes(canonical(value))


def sha(raw): return hashlib.sha256(raw).hexdigest()


def source_material():
    ev=json.loads(SOURCE.read_text())['files']
    for v in ev.values():
        assert sha(v['content'].encode())==v['sha256']
    key='model/'+SOURCE_CELL+'/steps/r1surface/input.json'
    inp=json.loads(ev[key]['content']);question=json.loads(inp['task']['question'])
    rows=question['items'];brief=inp['task']['brief']
    assert len(rows)==6 and all(set(v)=={'id','name'} for v in rows)
    assert len({v['id'] for v in rows})==6
    return brief,rows,sha(SOURCE.read_bytes())


def prepare(output:Path,runtime:Path):
    output.mkdir(parents=True,exist_ok=False);runtime.mkdir(parents=True,exist_ok=True)
    meta,raw=get('https://huggingface.co/api/models/'+MODEL_REPO+'?blobs=true',timeout=60)
    revision=meta['sha'];siblings={v['rfilename']:v for v in meta['siblings']}
    assert MODEL_FILE in siblings
    (output/'hub-model.json').write_bytes(raw)
    url='https://huggingface.co/'+MODEL_REPO+'/resolve/'+revision+'/'+MODEL_FILE
    digest=hashlib.sha256();count=0;start=time.monotonic()
    with urllib.request.urlopen(url,timeout=180) as src,(runtime/'model.gguf').open('xb') as dst:
        while block:=src.read(4*1024*1024):
            count+=len(block)
            if count>3_000_000_000: raise ValueError('model_size_cap')
            dst.write(block);digest.update(block)
    assert 2_000_000_000<count<3_000_000_000
    brief,rows,source_hash=source_material()
    plan={
      'id':'SEM-408-001','source_cell':SOURCE_CELL,'source_sha256':source_hash,
      'review_model_repo':MODEL_REPO,'review_model_revision':revision,'review_model_file':MODEL_FILE,
      'weights_sha256':digest.hexdigest(),'weights_bytes':count,'llama_cpp_commit':LLAMA,
      'download_seconds':time.monotonic()-start,'candidates':rows,'brief':brief,
      'requests':len(rows),'one_candidate_per_request':True,'new_names':0,
      'reviewer_blind_to':['Qwen decisions','v95 priority/hold','creator pronunciation','creator meaning','creator derivation','creator risk','method origin','other candidates','reality screening','owner preference'],
      'temperature':0.2,'top_p':0.9,'seed':SEED,'max_output_tokens':MAX_OUTPUT,'timeout_seconds':300,'retries':0,
      'quality_ground_truth':None,'meaning':'cross-model independent reviewer opinion, not truth or adoption'
    }
    save(output/'plan.json',plan)
    save(output/'runtime-identity.json',{'repo':MODEL_REPO,'revision':revision,'file':MODEL_FILE,
      'weights_sha256':digest.hexdigest(),'bytes':count,'llama_cpp_commit':LLAMA,
      'cpu':subprocess.check_output(['lscpu'],text=True),'user_machine':False})


def question(brief,row):
    return {
      'role':'Independent naming semantics reviewer',
      'brief':brief,
      'candidate':row,
      'blindness':'You have only this one candidate. Do not infer other candidates, prior rankings, generation method or reviewer decisions.',
      'rules':[
        'observable_form must be grounded only in the visible spelling; do not invent etymology.',
        'The brief does not require the bare name to literally encode every product function.',
        'association_hypotheses are hypotheses requiring human or linguistic evidence, never facts.',
        'Do not make trademark, domain, collision, registration, market-presence or legal claims; no reality evidence is supplied.',
        'advance/hold/stop means only intrinsic semantic research priority, not clearance or adoption.',
      ],
      'output_contract':{
        'id':'exact input id',
        'observable_form':['1-3 concise observations'],
        'pronunciation_uncertainty':{'level':'low/medium/high','reason':'grounded reason'},
        'brief_fit':{'level':'strong/mixed/weak','reason':'grounded reason'},
        'association_hypotheses':['0-3 concise hypotheses explicitly needing validation'],
        'disposition':'advance/hold/stop',
        'reason':'why this intrinsic research disposition follows; do not cite unavailable reality facts'
      }
    }


def parse(raw,candidate_id):
    body=raw.decode('utf-8').strip()
    if body.startswith('```json\n') and body.endswith('\n```'): body=body[8:-4]
    v=json.loads(body)
    required={'id','observable_form','pronunciation_uncertainty','brief_fit','association_hypotheses','disposition','reason'}
    if not isinstance(v,dict) or set(v)!=required or v['id']!=candidate_id: raise ValueError('review_schema_or_id')
    if not isinstance(v['observable_form'],list) or not 1<=len(v['observable_form'])<=3 or not all(isinstance(x,str) and x.strip() for x in v['observable_form']): raise ValueError('observable_form')
    if not isinstance(v['association_hypotheses'],list) or len(v['association_hypotheses'])>3 or not all(isinstance(x,str) and x.strip() for x in v['association_hypotheses']): raise ValueError('association_hypotheses')
    for k,allowed in [('pronunciation_uncertainty',{'low','medium','high'}),('brief_fit',{'strong','mixed','weak'})]:
        obj=v[k]
        if not isinstance(obj,dict) or set(obj)!={'level','reason'} or obj['level'] not in allowed or not isinstance(obj['reason'],str) or not obj['reason'].strip(): raise ValueError(k)
    if v['disposition'] not in {'advance','hold','stop'} or not isinstance(v['reason'],str) or not v['reason'].strip(): raise ValueError('disposition')
    return v


def execute(output:Path):
    plan=json.loads((output/'plan.json').read_text());brief,rows,source_hash=source_material()
    assert source_hash==plan['source_sha256'] and rows==plan['candidates'] and brief==plan['brief']
    results=[]
    for index,row in enumerate(rows,1):
        root=output/f'review-{index}-{row["id"]}';root.mkdir()
        prompt=question(brief,row)
        messages=[{'role':'user','content':json.dumps(prompt,ensure_ascii=False,sort_keys=True,indent=2)}]
        rendered,_=get(ORIGIN+'/apply-template',{'messages':messages,'add_generation_prompt':True},30)
        toks,_=get(ORIGIN+'/tokenize',{'content':rendered['prompt'],'add_special':False,'parse_special':True},30)
        wire={'prompt':toks['tokens'],'n_predict':MAX_OUTPUT,'temperature':0.2,'top_p':0.9,'seed':SEED,'stream':False,'cache_prompt':False}
        save(root/'input.json',{'candidate':row,'prompt':prompt,'messages':messages,'input_tokens':len(toks['tokens'])})
        save(root/'request.json',wire);save(root/'dispatch-intent.json',{'started_at':time.time(),'retry':False,'candidate_id':row['id']})
        start=time.monotonic();record={'id':row['id'],'name':row['name'],'status':'blocked'}
        try:
            body,raw=get(ORIGIN+'/completion',wire,300);(root/'response.json').write_bytes(raw)
            answer=body.get('content','').encode();(root/'answer.raw').write_bytes(answer)
            assert body.get('tokens_evaluated')==len(toks['tokens']) and type(body.get('tokens_predicted')) is int and body['tokens_predicted']<=MAX_OUTPUT
            assert not body.get('truncated') and (body.get('stop_type') in ('eos','word') or body.get('stopped_eos') or body.get('stopped_word'))
            review=parse(answer,row['id']);save(root/'parsed.json',review)
            record.update(status='review_complete_not_truth',review=review,input_tokens=body['tokens_evaluated'],output_tokens=body['tokens_predicted'])
        except Exception as error:
            record['error']=repr(error)
        record['seconds']=time.monotonic()-start;save(root/'result.json',record);results.append(record)
        summary={'id':'SEM-408-001','new_names':0,'paid_api_calls':0,'quality_ground_truth':None,
          'review_model':MODEL_REPO,'requests_dispatched':index,'results':results}
        (output/'summary.json').write_bytes(canonical(summary))
        print(json.dumps(record,ensure_ascii=False),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['prepare','execute']);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--runtime',type=Path)
    a=ap.parse_args();prepare(a.output,a.runtime) if a.command=='prepare' else execute(a.output)
