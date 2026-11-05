#!/usr/bin/env python3
"""Finite offline probe. No external schema reads; all input JSON bytes are recorded."""
import sys
AUDIT = []
PHASE = 'bootstrap'
def guard(event, args):
    denied = event.startswith(('socket.', 'subprocess.', 'urllib.', 'http.client.')) or event in {'os.system', 'os.exec', 'os.posix_spawn', 'pty.spawn'} or (PHASE == 'probe' and event == 'open')
    if denied:
        AUDIT.append({'phase': PHASE, 'event': event, 'args': repr(args)})
        raise RuntimeError('offline audit guard rejected ' + event)
sys.addaudithook(guard)
import argparse, json, hashlib, inspect, importlib.metadata as metadata
from pathlib import Path
import jsonschema, jsonschema.validators, jsonschema._keywords, jsonschema.exceptions
import referencing, referencing._core, referencing.jsonschema, referencing.exceptions
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from referencing.exceptions import NoSuchResource
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', required=True, type=Path, help='New explicit output directory, different from the script directory')
D = parser.parse_args().output_dir.resolve()
if D == Path(__file__).resolve().parent:
    parser.error('output directory must differ from script directory')
if D.exists():
    parser.error('output directory must not already exist; choose a fresh directory')
D.mkdir(parents=True)
(D / 'sources').mkdir()

def raw(value): return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def sha(data): return hashlib.sha256(data).hexdigest()
def typename(obj): return type(obj).__module__ + '.' + type(obj).__qualname__
def resource(contents): return Resource.from_contents(contents, default_specification=DRAFT202012)
base_a = 'https://example.invalid/a/root.json'
base_b = 'https://example.invalid/b/root.json'
target_a = 'https://example.invalid/a/target.json'
target_b = 'https://example.invalid/b/target.json'
root_a = {'$schema':'https://json-schema.org/draft/2020-12/schema','$id':base_a,'$ref':'target.json'}
root_b = dict(root_a, **{'$id':base_b})
integer = {'type':'integer'}
string = {'type':'string'}
def case(name, schema, instance, entries=None, callback=None):
    return dict(name=name,schema_json=raw(schema),instance_json=raw(instance),registry_json={k:raw(v) for k,v in (entries or {}).items()},callback_json={k:raw(v) for k,v in (callback or {}).items()})
cases = [
 case('id_only_accept',{'$id':'https://example.invalid/identity-only','type':'integer'},7),
 case('id_only_reject_instance',{'$id':'https://example.invalid/identity-only','type':'integer'},'seven'),
 case('same_root_registry_A',root_a,7,{target_a:integer}),
 case('same_root_registry_B',root_a,7,{target_a:string}),
 case('relative_base_a',root_a,7,{target_a:integer,target_b:string}),
 case('relative_base_b',root_b,7,{target_a:integer,target_b:string}),
 case('missing_resource_rejected_callback',root_a,7),
 case('explicit_memory_callback',root_a,7,callback={target_a:integer}),
 case('registered_resource_bad_instance',root_a,'seven',{target_a:integer}),
]
(D/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
results=[]
PHASE='probe'
for c in cases:
    callbacks=[]
    def retrieve(uri):
        callbacks.append(uri)
        if uri in c['callback_json']:
            return resource(json.loads(c['callback_json'][uri]))
        raise NoSuchResource(ref=uri)
    registry=Registry(retrieve=retrieve).with_resources((uri,resource(json.loads(data))) for uri,data in c['registry_json'].items())
    schema=json.loads(c['schema_json']); instance=json.loads(c['instance_json'])
    row={'name':c['name'],'resource_supply':('preloaded_registry' if c['registry_json'] else ('memory_only_callback' if c['callback_json'] else 'none')),'retrieve_policy':('memory_only_or_reject' if c['callback_json'] else 'reject'),'callback_urls':callbacks,'audit_start':len(AUDIT)}
    try:
        errors=list(Draft202012Validator(schema,registry=registry).iter_errors(instance))
        row.update(outcome='instance_rejected' if errors else 'accepted',errors=[{'class':typename(e),'message':e.message,'validator':e.validator,'schema_path':list(e.schema_path),'instance_path':list(e.path)} for e in errors])
    except Exception as e:
        chain=[]; seen=set(); current=e
        while current is not None and id(current) not in seen:
            seen.add(id(current));chain.append({'class':typename(current),'message':str(current),'repr':repr(current),'suppress_context':current.__suppress_context__})
            current=current.__cause__ or (current.__context__ if not current.__suppress_context__ else None)
        row.update(outcome='resolution_exception',exception_chain=chain)
    row['blocked_audit_events']=AUDIT[row.pop('audit_start'):]
    results.append(row)
PHASE='record'
expected=['accepted','instance_rejected','accepted','instance_rejected','accepted','instance_rejected','resolution_exception','accepted','instance_rejected']
assert [r['outcome'] for r in results]==expected
assert [r['callback_urls'] for r in results]==[[],[],[],[],[],[],[target_a],[target_a],[]]
assert not AUDIT
modules=[jsonschema.validators,jsonschema._keywords,jsonschema.exceptions,referencing._core,referencing.jsonschema,referencing.exceptions]
sources=[]
for mod in modules:
    path=Path(inspect.getfile(mod)); data=path.read_bytes(); dest=D/'sources'/(mod.__name__+'.py');dest.write_bytes(data)
    sources.append({'module':mod.__name__,'package_relative_path':mod.__name__.replace('.', '/') + '.py','snapshot':str(dest.relative_to(D)),'sha256':sha(data),'bytes':len(data)})
api={name:{'signature':str(inspect.signature(obj)),'source':inspect.getsource(obj)} for name,obj in [
('Registry.get_or_retrieve',Registry.get_or_retrieve),('Registry.with_resources',Registry.with_resources),('Resolver.lookup',referencing._core.Resolver.lookup),('Resource.from_contents',Resource.from_contents),('Draft202012Validator._validate_reference',Draft202012Validator._validate_reference),('Draft202012Validator.__attrs_post_init__',Draft202012Validator.__attrs_post_init__),('ref',jsonschema._keywords.ref)]}
(D/'api-inspection.json').write_text(json.dumps(api,indent=2)+'\n')
manifest={'baseline':'7f58751be3be669159036df039a208f2d1e9ec30','IA_object_version_unchanged':'python_jsonschema 4.25.1','python':sys.version,'platform':sys.platform,'distributions':{n:{'version':metadata.version(n),'requires':metadata.requires(n)} for n in ['jsonschema','referencing','jsonschema-specifications','attrs','rpds-py']},'module_sources':sources,'probe_sha256':sha(Path(__file__).read_bytes()),'cases_sha256':sha((D/'cases.json').read_bytes()),'guard':'Before third-party imports: reject socket.*, subprocess.*, urllib.*, http.client.*, os.system, os.exec, os.posix_spawn, pty.spawn; during probe reject open. Only explicit memory-only/rejecting callbacks tested; no sockets or network-resource loading tested.','limits':'Audit guard is observation/defense for this Python process, not a universal sandbox; no new installation or execution of freshly downloaded code; only identified already-installed third-party libraries imported.'}
(D/'environment-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
output={'results':results,'audit_blocked_events':AUDIT,'assertions':'9 expected classifications and callback lists matched; zero guarded events','interpretation':'Callback invocation is a retrieval request, not proof of network access. These results cover only the explicit in-memory registry/callback configuration.'}
(D/'results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
