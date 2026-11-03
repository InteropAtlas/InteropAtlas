"""One-off trusted UBL 2.3/XSD boundary observation; not a UBL validator.
Acquisition must already be complete. No network or unlisted schema resource is allowed.
"""
from pathlib import Path
import argparse,hashlib,json,io,importlib.util,socket,sys,urllib.request
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone
from importlib.metadata import version
import xml.etree.ElementTree as ET
import platform,warnings
ap=argparse.ArgumentParser();ap.add_argument('--sources',type=Path,required=True);ap.add_argument('--source-manifest',type=Path,required=True);ap.add_argument('--meta-manifest',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
R=args.sources.resolve();OUT=args.output.resolve();assert not OUT.exists(),'choose a fresh output directory'
source_bytes=args.source_manifest.read_bytes();assert hashlib.sha256(source_bytes).hexdigest()=='d79ebccf32b8265dfba5499c8a9a73775b4b39f45143874352c5fa7b059f87da','use the frozen official-source manifest'
m=json.loads(source_bytes);allowed={};labels={};installed=[]
for f in m['schema_files']:
 p=(R/f['path']).resolve();assert p.is_relative_to(R) and p.is_relative_to((R/'official').resolve()),f['path']
 b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==f['sha256'],f['path'];allowed[p]=b;labels[p]=f['path']
 for d in f['dependencies']:
  targets=[d['resolved_url']] if 'resolved_url' in d else d['known_namespace_resources']
  assert targets and all(u in {x['url'] for x in m['schema_files']} for u in targets)
pkg=Path(importlib.util.find_spec('xmlschema').origin).parent
meta_bytes=args.meta_manifest.read_bytes();assert hashlib.sha256(meta_bytes).hexdigest()=='ce431f9ad037b6dfef180f4c7f4a262fa30bbc256ef03e5fa8599cf7bd628ee1','use the frozen installed-meta manifest'
expected_meta=json.loads(meta_bytes)
assert expected_meta['package']=='xmlschema' and expected_meta['version']=='4.3.2'
for item in expected_meta['files']:
 label=item['path'];assert label.startswith('installed/xmlschema/schemas/')
 p=(pkg/label.removeprefix('installed/xmlschema/')).resolve();assert p.is_relative_to(pkg.resolve())
 b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==item['sha256'],label
 allowed[p]=b;labels[p]=label;installed.append(item)
assert len(installed)==6 and len(allowed)==22
resource_reads=[];denied=[]
class UnexpectedResourceAccess(RuntimeError):pass
def deny_network(*a,**k):denied.append('network API');raise UnexpectedResourceAccess('network disabled during probe')
socket.getaddrinfo=deny_network;socket.socket.connect=deny_network
# xmlschema XMLResource imports this function. All schema reads, including trusted
# installed meta-schemas during import, use this explicit finite byte allowlist.
def finite_resource(url,*a,**k):
 u=url.full_url if hasattr(url,'full_url') else str(url);parts=urlsplit(u)
 if parts.scheme not in ('','file') or parts.netloc not in ('','localhost'):
  denied.append(u);raise UnexpectedResourceAccess('unlisted nonlocal resource')
 p=Path(unquote(parts.path)).resolve()
 if p not in allowed:
  denied.append(u);raise UnexpectedResourceAccess('unlisted file resource')
 resource_reads.append(labels[p]);fp=io.BytesIO(allowed[p]);fp.url=u;return fp
urllib.request.urlopen=finite_resource
import xmlschema
from xmlschema.exceptions import XMLResourceParseError
from xmlschema.validators.exceptions import XMLSchemaValidationError
assert xmlschema.__version__=='4.3.2' and version('elementpath')=='5.1.4'
root=R/'official/xsd/maindoc/UBL-Invoice-2.3.xsd'
# The finite-resource allowlist above is the restrictive gate. Library allow=local
# avoids a directory sandbox being re-anchored to maindoc and blocking ../common.
with warnings.catch_warnings(record=True) as construction_warnings:
 warnings.simplefilter('always')
 schema=xmlschema.XMLSchema10(root,allow='local',defuse='always',use_fallback=False)
assert not construction_warnings,[str(w.message) for w in construction_warnings]
assert schema.built and schema.validation=='strict'
BASE='''<?xml version="1.0" encoding="UTF-8"?>
<Invoice xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"
 xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
 xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">
 <cbc:ID>synthetic-invoice-1</cbc:ID><cbc:IssueDate>2020-01-01</cbc:IssueDate>
 <cac:AccountingSupplierParty><cac:Party><cac:PartyName><cbc:Name>Synthetic supplier</cbc:Name></cac:PartyName></cac:Party></cac:AccountingSupplierParty>
 <cac:AccountingCustomerParty><cac:Party><cac:PartyName><cbc:Name>Synthetic customer</cbc:Name></cac:PartyName></cac:Party></cac:AccountingCustomerParty>
 <cac:LegalMonetaryTotal><cbc:PayableAmount currencyID="XXX">1.00</cbc:PayableAmount></cac:LegalMonetaryTotal>
 <cac:InvoiceLine><cbc:ID>1</cbc:ID><cbc:LineExtensionAmount currencyID="XXX">1.00</cbc:LineExtensionAmount><cac:Item><cbc:Name>Synthetic item</cbc:Name></cac:Item></cac:InvoiceLine>
</Invoice>'''
supplier='<cac:AccountingSupplierParty><cac:Party><cac:PartyName><cbc:Name>Synthetic supplier</cbc:Name></cac:PartyName></cac:Party></cac:AccountingSupplierParty>'
inputs={
 'nonempty_reference':BASE,
 'empty_supplier_container':BASE.replace(supplier,'<cac:AccountingSupplierParty/>'),
 'empty_note_scalar':BASE.replace('</cbc:IssueDate>','</cbc:IssueDate><cbc:Note/>'),
 'invalid_date_lexical':BASE.replace('2020-01-01','not-a-date'),
 'malformed_xml':BASE.replace('</Invoice>','</WrongInvoice>')}
obs=[]
for name,xml in inputs.items():
 o={'case':name,'input_sha256':hashlib.sha256(xml.encode()).hexdigest()}
 try:
  e=ET.fromstring(xml);o['xml_well_formed']=True
  # Only literal zero-child/zero-text nodes in these generated examples. This is
  # NOT a general IND5, null, whitespace, semantic or full UBL conformance checker.
  o['literal_empty_leaf_tags']=[n.tag for n in e.iter() if len(n)==0 and n.text in (None,'')]
 except ET.ParseError:o['xml_well_formed']=False;o['literal_empty_leaf_tags']=None
 try:
  errors=list(schema.iter_errors(xml,use_location_hints=False,allow_empty=False))
  o['xsd_valid']=not errors;o['xsd_errors']=[{'class':type(e).__name__,'path':e.path,'reason':e.reason} for e in errors]
  try:schema.validate(xml,use_location_hints=False,allow_empty=False);o['validate_exception']=None
  except XMLSchemaValidationError as e:o['validate_exception']=type(e).__name__
 except XMLResourceParseError as e:o['xsd_valid']=None;o['xsd_errors']=None;o['validate_exception']=type(e).__name__
 obs.append(o);print(json.dumps(o),flush=True)
by={o['case']:o for o in obs}
assert by['nonempty_reference']['xsd_valid'] and not by['nonempty_reference']['literal_empty_leaf_tags']
assert by['empty_supplier_container']['xsd_valid'] and by['empty_supplier_container']['literal_empty_leaf_tags']==['{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty']
assert by['empty_note_scalar']['xsd_valid'] and by['empty_note_scalar']['literal_empty_leaf_tags']==['{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Note']
assert not by['invalid_date_lexical']['xsd_valid'] and by['invalid_date_lexical']['xml_well_formed']
assert by['malformed_xml']['xsd_valid'] is None and by['malformed_xml']['validate_exception']=='XMLResourceParseError'
assert not denied
result={'observed_at':datetime.now(timezone.utc).isoformat(),'versions':{'python':platform.python_version(),'xmlschema':version('xmlschema'),'elementpath':version('elementpath')},'source_manifest':m,'installed_trusted_meta_schema_allowlist':installed,'schema_resource_reads':resource_reads,'schema_resource_read_set':sorted(set(resource_reads)),'schema_construction_warnings':[str(w.message) for w in construction_warnings],'denied_resource_attempts':denied,'inputs':inputs,'observations':obs,'conclusion':'Two explicit empty-element counterexamples are XSD-valid under the fixed library and official Invoice schema closure, yet conflict with UBL 2.3 section 4.4 IND5. This is not a complete UBL conformance check.','limits':['Only five trusted synthetic examples and one fixed library/dependency combination.','No business/legal/tax/code-list/signature/security assessment, entity attack, real counterpart or third-party interoperability.','The nonempty reference is not claimed fully UBL-conforming. No null/whitespace/general semantic validator is supplied.','No implements or compatibility relation and no IA adoption or ongoing testing obligation follows.']}
OUT.mkdir(parents=True);(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for n,v in inputs.items():(OUT/(n+'.xml')).write_text(v)
print('PASS: five bounded observations; known empty elements distinct from XSD failures and XML parse exception.')
