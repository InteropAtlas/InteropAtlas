"""Trusted finite in-memory probe. No network and no process-wide loader change."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,copy,importlib.metadata as md
from pyld import jsonld
if len(sys.argv)!=2:raise SystemExit('Usage: jsonld-shacl-produce-20261021.py OUTPUT_DIRECTORY')
E=Path(sys.argv[1]);E.mkdir(parents=True,exist_ok=True);start=datetime.now(timezone.utc).isoformat();attempts=[]
def deny(url,options=None):attempts.append(url);raise jsonld.JsonLdError('External loading denied','jsonld.LoadDocumentError',code='loading document failed')
options={'documentLoader':deny,'processingMode':'json-ld-1.1'}
context={'ex':'https://example.test/','Person':'ex:Person','name':'ex:name'}
valid={'@context':context,'@id':'ex:a','@type':'Person','name':'Alice'}
wrong=dict(valid,name=42);missing={k:v for k,v in valid.items() if k!='name'};extra=dict(valid,unmapped='not validated as a property');language=dict(valid,name={'@value':'Alice','@language':'en'})
named_invalid={'@context':context,'@graph':[{'@id':'ex:a','@type':'Person','name':'Alice'},{'@id':'ex:g','@graph':[{'@id':'ex:a','@type':'Person','name':42}]}]}
named_only={'@context':context,'@id':'ex:g','@graph':[{'@id':'ex:a','@type':'Person','name':42}]}
rows=[]
for name,doc in [('valid',valid),('wrong_type',wrong),('missing_required',missing),('unmapped_extra',extra),('language_value',language),('mixed_graphs',named_invalid),('named_only',named_only)]:
 original=copy.deepcopy(doc);dropped=[];expanded=jsonld.expand(doc,options,on_property_dropped=dropped.append);nq=jsonld.to_rdf(expanded,{**options,'format':'application/n-quads'});assert original==doc
 rows.append({'name':name,'input':doc,'expanded':expanded,'nquads':nq,'dropped_properties':dropped})
assert rows[3]['dropped_properties'] and 'not validated as a property' not in rows[3]['nquads']
try:jsonld.expand({'@context':'https://example.test/blocked','name':'Alice'},options)
except jsonld.JsonLdError:pass
else:raise AssertionError('remote context was not blocked')
assert attempts==['https://example.test/blocked']
r={'started_at':start,'completed_at':datetime.now(timezone.utc).isoformat(),'versions':{x:md.version(x) for x in ['PyLD','cachetools','frozendict','lxml']},'cases':rows,'rejected_remote_contexts':attempts,'limits':'Trusted inline inputs. Rejecting loader passed to expansion and RDF conversion. No network request, no loader setter, no framing/canonicalization or arbitrary-data guarantee.'};(E/'produced.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print('PRODUCED_7_TRUSTED_FIXTURES_AND_BLOCKED_REMOTE_CONTEXT')
