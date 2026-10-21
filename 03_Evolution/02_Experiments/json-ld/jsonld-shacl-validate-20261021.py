"""Explicit graph-selection experiment, not a generalized pipeline contract."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,importlib.metadata as md
from rdflib import Dataset,Graph,Namespace,RDF,Literal
from pyshacl import validate
from pyshacl.errors import ValidationFailure,ReportableRuntimeError
if len(sys.argv)!=2:raise SystemExit('Usage: jsonld-shacl-validate-20261021.py OUTPUT_DIRECTORY')
E=Path(sys.argv[1]);E.mkdir(parents=True,exist_ok=True);start=datetime.now(timezone.utc).isoformat();src=json.load(open(E/'produced.json'));rows=[]
SH=Namespace('http://www.w3.org/ns/shacl#');EX=Namespace('https://example.test/')
prefix='@prefix ex: <https://example.test/> . @prefix sh: <http://www.w3.org/ns/shacl#> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> . @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . '
shape=prefix+'ex:S a sh:NodeShape; sh:targetClass ex:Person; sh:closed true; sh:ignoredProperties (rdf:type); sh:property [sh:path ex:name; sh:minCount 1; sh:maxCount 1; sh:datatype xsd:string].'
shape_node=shape.replace('sh:targetClass ex:Person','sh:targetNode ex:a')
fixtures={x['name']:x for x in src['cases']}
# The union is an explicit alternate policy for contrast, not the graph-source default.
cases=[('valid','default','class',True),('wrong_type','default','class',False),('missing_required','default','class',False),('unmapped_extra','default','class',True),('language_value','default','class',False),('mixed_graphs','default','class',True),('mixed_graphs','union','class',False),('named_only','default','class',True),('named_only','default','node',False),('named_only','union','class',False)]
for key,policy,target,want in cases:
 d=Dataset();d.parse(data=fixtures[key]['nquads'],format='nquads');g=Graph()
 chosen=[d.default_graph] if policy=='default' else list(d.graphs())
 for context in chosen:
  for triple in context:g.add(triple)
 shapes=Graph().parse(data=shape if target=='class' else shape_node,format='turtle')
 conforms,report,text=validate(g,shacl_graph=shapes,inference='none',advanced=False,meta_shacl=False,js=False,do_owl_imports=False)
 assert conforms is want,(key,policy,target,text)
 report_node=next(report.subjects(RDF.type,SH.ValidationReport));assert report.value(report_node,SH.conforms)==Literal(want)
 rows.append(dict(fixture=key,graph_policy=policy,target=target,data_triples=len(g),target_class_nodes=len(set(g.subjects(RDF.type,EX.Person))),conforms=conforms,reported_results=len(list(report.objects(report_node,SH.result))),PASS=True))
# Keep validation violations, returned ValidationFailure, and raised errors distinct.
g=Graph();d=Dataset();d.parse(data=fixtures['valid']['nquads'],format='nquads')
for t in d.default_graph:g.add(t)
bad_query=prefix+'ex:S a sh:NodeShape; sh:targetNode ex:a; sh:sparql [sh:select """PREFIX ex: <https://example.test/> SELECT $this WHERE { VALUES ?x { 1 } $this ex:name ?n . }"""].'
conforms,report,text=validate(g,shacl_graph=Graph().parse(data=bad_query,format='turtle'),inference='none',advanced=False,meta_shacl=False,js=False,do_owl_imports=False)
assert conforms is False and isinstance(report,ValidationFailure)
rows.append(dict(fixture='valid',graph_policy='default',case='forbidden SPARQL VALUES',outcome='returned ValidationFailure, not ordinary validation-results graph',returned_type=type(report).__name__,conforms=conforms,message=str(report),PASS=True))
bad_shape=prefix+'ex:S a sh:NodeShape; sh:targetNode ex:a; sh:property [sh:path ex:name; sh:minCount "bad"].'
try:
 validate(g,shacl_graph=Graph().parse(data=bad_shape,format='turtle'),inference='none',advanced=False,meta_shacl=True,js=False,do_owl_imports=False)
except ReportableRuntimeError as ex:
 rows.append(dict(fixture='valid',graph_policy='default',case='invalid shape with meta_shacl=True',outcome='raised exception, no ordinary conforms result',exception_type=type(ex).__name__,message=str(ex),PASS=True))
else:raise AssertionError('Expected invalid-shape exception')
r={'started_at':start,'completed_at':datetime.now(timezone.utc).isoformat(),'versions':{x:md.version(x) for x in ['pyshacl','rdflib','owlrl','pyparsing','packaging','prettytable','html5rdf','wcwidth']},'cases':rows,'count':len(rows),'all_pass':True,'limits':['Only the listed trusted fixtures with these installed versions and flags. No generalized compatibility edge or complete pipeline established.','An unmapped input property is lost before graph validation; SHACL conformance is not validation of every original JSON field.','Default-only vs explicit union changes validation; named-only data with no targetClass focus nodes can conform vacuously, whereas targetNode still imposes constraints.','No remote documents/imports, security assessment, full conformance certification, RDF1.2, production recommendation or IA adoption.']};(E/'result.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False,indent=2))
