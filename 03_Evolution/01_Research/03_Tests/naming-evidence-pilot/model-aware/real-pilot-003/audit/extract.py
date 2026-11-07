"""Read-only extraction of REAL-408-003. No inference, semantic scoring or repair.
Source evidence remains authoritative; packets are reproducible projections.
The current author's prior exposure prevents an independent-blind-review claim.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import unicodedata

SOURCE_BLOB = '67a46c1f84f368c7f924f893f3c700e9290184bb'
SOURCE_COMMIT = 'edde49b36c4fc39df0fa64c6959f9a01b75b2f09'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result: raise ValueError('duplicate_key:' + key)
        result[key] = value
    return result

def decode(text):
    text = text.strip()
    if text.startswith('```json\n') and text.endswith('\n```'): text = text[8:-4]
    return json.loads(text, object_pairs_hook=unique)

def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()

def norm(name):
    return unicodedata.normalize('NFKC', name).strip().casefold()

def build(source: Path, output: Path):
    raw = source.read_bytes()
    assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == SOURCE_BLOB
    evidence = decode(raw.decode()); files = evidence['files']
    for key, entry in files.items():
        assert sha(entry['content'].encode()) == entry['sha256'], key
    def read(key): return decode(files[key]['content'])
    summary = read('model/summary.json')
    cells, variants, names, origins = [], {}, {}, []
    for cell in summary['cells']:
        cell = dict(cell); label = cell['cell']; base = 'model/' + label + '/'
        plan = read(base + 'plan.json'); generated = []
        gen_steps = ['r1g1','r1g2','r1g3'] if cell['method'] == 'redesign' else ['r1g1']
        for step in gen_steps:
            path = base + 'steps/' + step + '/answer.raw'
            answer = read(path)
            for row in answer['candidates']:
                assert set(row) == {'name','pronunciation','meaning','derivation','risk'}
                assert all(isinstance(v,str) and v.strip() for v in row.values())
                key = norm(row['name']); nid = 'N-' + sha(('audit003-name|' + key).encode())[:8]
                xid = 'X-' + sha(canonical(row))[:8]
                assert nid not in names or norm(names[nid]['name']) == key
                names.setdefault(nid, {'id': nid, 'name': row['name']})
                variants.setdefault(xid, dict(row, id=xid, name_id=nid))
                generated.append((dict(row),nid,xid))
                origins.append({'cell':label,'name_id':nid,'explanation_id':xid,'source_path':path,'raw_model_path':base+'calls/'+step+'/output.txt'})
        random.Random(plan['seed'] + 1).shuffle(generated)
        pool, seen = [], set()
        for row,nid,xid in generated:
            key=norm(row['name'])
            if key in seen: continue
            seen.add(key); pool.append(dict(row,id='C'+str(len(pool)+1).zfill(3),name_id=nid,explanation_id=xid))
        mapped={row['id']:row['name_id'] for row in pool}
        cell.update(generated_occurrences=len(generated),pool=pool,within_cell_duplicates=len(generated)-len(pool),stages={})
        for stage in ['r1surface','r1explained','r1audit']:
            input_path=base+'steps/'+stage+'/input.json'; answer_path=base+'steps/'+stage+'/answer.raw'
            if input_path not in files: continue
            request=read(input_path); question=decode(request['task']['question'])
            expected=[row['id'] for row in question['items']]
            answer=read(answer_path) if answer_path in files else None
            rows=answer.get('reviews',[]) if answer else []
            actual=[row.get('id') for row in rows]
            valid=(len(actual)==len(expected) and set(actual)==set(expected) and len(set(actual))==len(actual))
            cell['stages'][stage]={'input_path':input_path,'answer_path':answer_path if answer else None,
                'expected_ids':expected,'returned_ids':actual,'coverage_valid':valid,
                'missing_ids':sorted(set(expected)-set(actual)), 'unexpected_ids':sorted(set(actual)-set(expected)),
                'duplicate_ids':[k for k,v in Counter(actual).items() if v>1],
                'reviews':[dict(row,name_id=mapped.get(row.get('id'))) for row in rows]}
        round_path=base+'round-1.json'
        if round_path in files:
            rnd=read(round_path)
            expected=[{k:v for k,v in row.items() if k not in ('name_id','explanation_id')} for row in pool]
            assert rnd['pool']==expected,label
            cell['retained_after_audit_ids']=rnd['intrinsic_shortlist_ids']
            cell['audit_disagreement_ids']=rnd['audit_disagreement_ids']
        calls=[]
        for key,entry in files.items():
            if key.startswith(base+'calls/') and key.endswith('/record.json'):
                record=decode(entry['content']); receipt=record['receipt']
                output_key=key.removesuffix('record.json')+'output.txt'
                assert sha(files[output_key]['content'].encode())==record['output_sha256']
                calls.append({'step':key.split('/')[-2],'input_tokens':receipt['input_tokens'],
                    'output_tokens':receipt['output_tokens'],'seconds':receipt['costs']['local_seconds'],'outcome':receipt['outcome']})
        assert len(calls)==cell['calls']
        cell['call_costs']=calls
        cell['generation_cost']={
            'calls':sum(x['step'] in gen_steps for x in calls),
            'input_tokens':sum(x['input_tokens'] for x in calls if x['step'] in gen_steps),
            'output_tokens':sum(x['output_tokens'] for x in calls if x['step'] in gen_steps),
            'seconds':sum(x['seconds'] for x in calls if x['step'] in gen_steps)}
        cells.append(cell)
    packets={'kind':'anonymous_materials_not_proof_of_reviewer_blindness','brief':plan['task']['brief'],
             'names':sorted(names.values(),key=lambda row:row['id']),
             'explanations':sorted(variants.values(),key=lambda row:row['id']),
             'instruction':'First assess names against brief; freeze those observations before viewing explanations. No availability claims or knowledge of origin. Separate exploratory opinion from validated naming outcome.'}
    data={'source_commit':SOURCE_COMMIT,'source_blob':SOURCE_BLOB,'source_sha256':sha(raw),'verified_embedded_files':len(files),
          'model_calls_during_extraction':0,'reviewer_blindness':'not_established_current_author_preexposed',
          'prior_model_calls':summary['real_inference_attempts'],'occurrences':len(origins),'unique_names':len(names),
          'unique_explanations':len(variants),'cells':cells,'origins':origins,
          'summary':summary,'limits':'One fictional task, two seeds, one quantized model. No significance or adoption inference. Do not score censored cells as naming failures.'}
    output.mkdir(parents=True,exist_ok=True)
    for name,value in [('packets.json',packets),('data.json',data)]:
        target=output/name;blob=canonical(value)
        if target.exists(): assert target.read_bytes()==blob,'Projection conflict:'+name
        else: target.write_bytes(blob)
    print(json.dumps({'verified_files':len(files),'occurrences':len(origins),'unique_names':len(names),'prior_calls':summary['real_inference_attempts'],'new_model_calls':0}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();build(args.source,args.output)
