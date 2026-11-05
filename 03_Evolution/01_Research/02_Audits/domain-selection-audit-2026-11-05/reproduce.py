#!/usr/bin/env python3
"""One-shot audit of existing IA records at a fixed historical baseline.

Read-only and stdout-only. This is a research recipe, not a Runtime API,
maintenance rule, coverage denominator, or replacement inventory snapshot.
Requires the baseline checkout's already available Engine dependencies.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import collections
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
BASELINE = '8c53fd278a595c7918833363cf63473fa46f3a61'
BASE_URL = f'https://github.com/InteropAtlas/InteropAtlas/blob/{BASELINE}/'
FIELDS = ('version', 'capabilities', 'description_zh', 'description_en',
          'scope_notes_zh', 'scope_notes_en', 'last_verified_at',
          'last_verified_by', 'sources', 'notes_zh')
INTAKE_SHA256 = 'd93e9e94d478707c26936fdcfcc201fdcc6bf0162e58a6083e46e443aeb98185'


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def link(path):
    return BASE_URL + path


def current_record_audit(root):
    from bootstrap_query import load_atlas, index_objects
    from intake_coverage_audit import documents, unique, PLAN
    from kind_registry import has_profile, load_kind_registry
    from workspace_projection import project_evidence, project_field

    objects, relations = load_atlas(root)
    index = index_objects(objects)
    registry = load_kind_registry()

    def located(directory, key):
        docs, paths = [], {}
        for path in sorted((root / directory).rglob('*')):
            if path.suffix not in {'.yaml', '.yml'}:
                continue
            for record in documents(path):
                docs.append(record)
                if record.get(key) in paths:
                    raise AssertionError(f'Duplicate {key}: {record.get(key)}')
                paths[record[key]] = path.relative_to(root).as_posix()
        return unique(docs, key), paths

    candidates, candidate_paths = located('01_State/Inbox/candidates', 'candidate_id')
    events, event_paths = located('01_State/Inbox/acceptance-events', 'event_id')
    accepted, targets = {}, {}
    for event in events.values():
        if event['decision'] != 'accepted':
            continue
        cid, oid = event['candidate_id'], event['accepted_canonical_id']
        assert cid not in accepted and oid not in targets
        assert cid in candidates and oid in index
        assert candidates[cid]['identity_resolution']['state'] == 'duplicate'
        assert candidates[cid]['identity_resolution']['matched_canonical_ids'] == [oid]
        provenance = index[oid]['intake_provenance']
        assert provenance['candidate_id'] == cid
        assert provenance['acceptance_event_id'] == event['event_id']
        accepted[cid], targets[oid] = event, cid

    plan = documents(root / PLAN)[0]
    assert plan['status'] == 'draft' and plan['semantics'] == 'editorial_navigation_only'
    category_ids = [c['id'] for c in plan['categories']]
    assert len(set(category_ids)) == len(category_ids)
    route_counts, domain_counts = Counter(), {c: Counter() for c in category_ids}
    resolved, seen_refs, target_routes = set(), set(), defaultdict(list)
    unresolved, candidate_nav = [], []
    for membership in plan['memberships']:
        category = membership['category_id']
        surface, rid = membership['ref']['surface'], membership['ref']['id']
        key = (category, surface, rid)
        assert category in domain_counts and key not in seen_refs
        seen_refs.add(key)
        if surface == 'canonical':
            assert rid in index
            oid, route = rid, 'canonical_direct'
        elif surface == 'candidate':
            assert rid in candidates
            if rid in accepted:
                oid, route = accepted[rid]['accepted_canonical_id'], 'accepted_candidate'
                candidate_nav.append(rid)
            else:
                oid, route = None, 'unresolved_candidate'
                unresolved.append({'category_id': category, 'candidate_id': rid,
                    'identity_state': candidates[rid]['identity_resolution']['state'],
                    'source': link(candidate_paths[rid]),
                    'decision': 'Preserve the recorded hold; no acceptance or identity repair inferred.'})
        else:
            raise AssertionError(f'Unknown surface: {surface}')
        route_counts[route] += 1
        domain_counts[category][route] += 1
        if oid:
            resolved.add(oid)
            target_routes[(category, oid)].append((surface, rid))

    duplicate_targets = [{'category_id': c, 'canonical_id': oid, 'routes': routes}
                         for (c, oid), routes in sorted(target_routes.items()) if len(routes) > 1]
    missing_accepted_targets = sorted(set(targets) - resolved)
    aliases = []
    for cid, event in sorted(accepted.items()):
        oid = event['accepted_canonical_id']
        if cid != oid:
            aliases.append({'candidate_id': cid, 'canonical_id': oid,
                'event_id': event['event_id'], 'event_source': link(event_paths[event['event_id']]),
                'candidate_navigation_link_count': candidate_nav.count(cid),
                'canonical_navigation_categories': sorted({c for c, target in target_routes if target == oid})})
    duplicate_only = []
    for cid, candidate in sorted(candidates.items()):
        identity = candidate['identity_resolution']
        if identity['state'] == 'duplicate' and cid not in accepted:
            duplicate_only.append({'candidate_id': cid, 'matched_canonical_ids': identity['matched_canonical_ids'],
                'source': link(candidate_paths[cid]), 'accepted_event_recorded': False,
                'navigated_target_ids': sorted(set(identity['matched_canonical_ids']) & resolved),
                'decision': 'Retain duplicate identity resolution; do not manufacture an acceptance.'})

    selected = [index[oid] for oid in sorted(resolved)]
    implementations = [r for r in selected if has_profile(r, 'implementation', registry)]
    no_sources = [r for r in selected if project_evidence(r)['evidence_state'] == 'not_recorded']
    for record in selected:
        for field in FIELDS:
            projected = project_field(record, field)
            assert projected['value'] == record.get(field)
            assert projected['state'] == ('not_recorded' if record.get(field) is None else 'recorded')
            assert projected['recoverable_from'] == {'canonical_object_id': record['id'], 'canonical_field': field}
    role_exceptions = [{'id': r['id'], 'record_type': r['type'], 'kind': r.get('kind'),
                        'source': link(r['_physical_source'])} for r in no_sources]
    implementation_counts = {
        'records': len(implementations),
        'sources_recorded': sum(project_evidence(r)['evidence_state'] == 'recorded' for r in implementations),
        'description_zh_recorded_nonempty': sum(bool(r.get('description_zh')) for r in implementations),
        'capabilities_not_recorded': sum(project_field(r, 'capabilities')['state'] == 'not_recorded' for r in implementations),
        'notes_zh_only_assessment_not_recorded': sum(project_evidence(r)['assessment']['state'] == 'not_recorded' for r in implementations),
        'scope_notes_zh_recorded_nonempty': sum(bool(r.get('scope_notes_zh')) for r in implementations),
    }
    # These expectations describe this exact baseline, not future acceptance gates.
    assert route_counts == {'canonical_direct': 267, 'accepted_candidate': 26, 'unresolved_candidate': 8}
    assert len(resolved) == 271 and len(accepted) == 163 and len(aliases) == 8
    assert not missing_accepted_targets and not duplicate_targets
    assert all(a['candidate_navigation_link_count'] == 0 for a in aliases)
    assert all(x['identity_state'] == 'identity_risk' for x in unresolved)
    assert Counter(r['type'] for r in no_sources) == {'capability': 21, 'scenario': 1}
    assert implementation_counts == {'records': 73, 'sources_recorded': 73,
        'description_zh_recorded_nonempty': 73, 'capabilities_not_recorded': 44,
        'notes_zh_only_assessment_not_recorded': 73, 'scope_notes_zh_recorded_nonempty': 51}
    return {
        'input_scope': 'All memberships in the existing editorial navigation; not a universe-of-technology denominator.',
        'counts': {'categories': len(category_ids), 'memberships': len(seen_refs),
            'resolved_memberships': sum(route_counts[k] for k in ['canonical_direct', 'accepted_candidate']),
            'resolved_unique_canonical_targets': len(resolved),
            'accepted_events_with_current_links_checked': len(accepted),
            'routes': dict(sorted(route_counts.items()))},
        'per_category_routes': {c: dict(sorted(counts.items())) for c, counts in domain_counts.items()},
        'missing_accepted_navigation_targets': missing_accepted_targets,
        'duplicate_category_resolved_targets': duplicate_targets,
        'accepted_candidate_target_aliases': aliases,
        'alias_boundary': 'Eight aliases are acceptance-chain facts, not eight failed candidate-navigation links; current routes are reported separately.',
        'duplicate_candidates_without_acceptance': duplicate_only,
        'unresolved_navigation_references': unresolved,
        'sources_not_recorded': {'count': len(no_sources),
            'roles': dict(sorted(Counter(r['type'] for r in no_sources).items())),
            'records': role_exceptions,
            'decision': 'These are recorded capabilities and an IA-authored scenario, not absent standards or implementation evidence. No automatic source backfill.'},
        'navigated_implementation_profiles': implementation_counts,
        'field_recovery': {'fields': list(FIELDS), 'field_projections_checked': len(selected) * len(FIELDS),
            'checks': ['raw value preserved', 'missing/null state preserved', 'object ID and field recovery preserved'],
            'result': 'PASS',
            'evidence_boundary': 'project_field attaches record-level sources, not field-specific substantiation. Value recovery does not prove the value or the sufficiency of its evidence.'},
        'current_link_boundary': 'Current candidate/event/object links checked here. Frozen Git pre-materialization verification is separate.',
    }


def _json(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),default=str)

def _state(record,field):
    return {'present':field in record,'value':record.get(field),'state':('absent' if field not in record else 'null' if record[field] is None else 'empty_list' if record[field]==[] else 'recorded')}

def implementation_audit(root, include_full_context=False):
    root=Path(root).resolve()
    sys.path.insert(0,str(root/'02_Runtime/01_Engine'))
    from bootstrap_query import load_atlas,index_objects,implementations_for_capability
    from relation_model import normalize_relation
    from graph_index import GraphIndex
    from kind_registry import has_profile,load_kind_registry
    from workspace_projection import select_by_capability
    objects,relations=load_atlas(root);index=index_objects(objects);registry=load_kind_registry()
    graph=GraphIndex(index,relations)
    rel_by_id={r['id']:r for r in relations}
    impl=[r for r in relations if normalize_relation(r).predicate=='implements']
    sources={normalize_relation(r).source_id for r in impl}
    impl_sources={sid for sid in sources if has_profile(index[sid],'implementation',registry)}
    def recovery(record,fields):
        return {'id':record['id'],'logical_source':record['_source'],'physical_source':record['_physical_source'],'canonical_fields':fields}
    def detail(rid):
        r=rel_by_id[rid];d=normalize_relation(r);s=index[d.source_id];t=index[d.target_id]
        return {'relation_id':rid,'source_id':d.source_id,'target_id':d.target_id,
          'relation_recovery':recovery(r,['source','relation','target','context','capability_context','scenario_context','conditions_zh','conditions_en','evidence','sources']),
          'source_recovery':recovery(s,['type','kind','version','versions','maturity','capabilities','scope_notes_zh','scope_notes_en','description_zh','description_en','sources']),
          'target_recovery':recovery(t,['type','kind','version','versions','maturity','capabilities','scope_notes_zh','scope_notes_en','description_zh','description_en','sources']),
          'source_type_kind':{'type':s.get('type'),'kind':s.get('kind')},
          'source_has_existing_implementation_profile':has_profile(s,'implementation',registry),
          'raw_source_capabilities':_state(s,'capabilities'),'raw_target_capabilities':_state(t,'capabilities'),
          'raw_relation_context':_state(r,'context'),'raw_legacy_capability_context':_state(r,'capability_context'),
          'normalized_context':d.context,'normalized_context_sha256':hashlib.sha256(_json(d.context).encode()).hexdigest(),
          'raw_relation_evidence':_state(r,'evidence'),
          'raw_relation_sources':_state(r,'sources'),
          'normalized_relation_evidence_count':len(d.evidence),
          'source_sources_state':_state(s,'sources')['state'], 'source_source_urls':[x.get('url') for x in s.get('sources') or [] if isinstance(x,dict)],
          'target_sources_state':_state(t,'sources')['state'], 'target_source_urls':[x.get('url') for x in t.get('sources') or [] if isinstance(x,dict)]}
    def compare(target,capability,representative,reason):
        assert capability in (index[target].get('capabilities') or [])
        edge_ids=sorted(e.relation_id for e in graph.backlinks(target) if e.origin=='relation' and e.kind=='implements')
        edge_sources=sorted({normalize_relation(rel_by_id[rid]).source_id for rid in edge_ids})
        cli=sorted(o['id'] for o in implementations_for_capability(objects,capability))
        workspace=sorted(select_by_capability(capability,index)['selected_ids'])
        context=sorted(normalize_relation(r).relation_id for r in graph.relation_objects_for_capability(capability) if normalize_relation(r).predicate=='implements')
        return {'target_id':target,'capability_id':capability,'comparison_basis':'Capability is literally recorded on the target; not inferred membership for any source.',
           'explicit_implements_relation_ids':edge_ids,'explicit_implements_source_ids':edge_sources,
           'cli_implementation_ids':cli,'workspace_explicit_membership_ids':workspace,'context_scoped_implements_relation_ids':context,
           'explicit_sources_not_in_cli':sorted(set(edge_sources)-set(cli)),
           'cli_sources_without_this_explicit_edge':sorted(set(cli)-set(edge_sources)),
           'reason':reason,'representative_bounded_relation':detail(representative)}
    examples=[
      compare('cbor_rfc8949','data_serialization','tinycbor_implements_cbor_uint','Direct capability selection misses TinyCBOR and selects sources whose recorded implements targets are different. An absent edge is not evidence of unsupported functionality; TinyCBOR retains its one-uint static slice and complete caller/platform restrictions.'),
      compare('http3_rfc9114','web_resource_transfer','aioquic_implements_http3_rfc9114','The target has web_resource_transfer, but its recorded implementing source aioquic has no capability field. h11/httpx annotations do not establish RFC9114 implementation or substitute for this bounded H3Connection edge.'),
      compare('git_protocol_v2','version_control','git_software_implements_git_v2_ls_refs','Git has a bounded ls-refs edge but no capability field. The version_control selector returns Dulwich instead; this neither removes Git evidence nor establishes a Dulwich implements edge.'),
      compare('json_schema_2020_12','schema_validation','python_jsonschema_implements_json_schema_2020_12','The capability groups JSON Schema, SHACL and object-only XML-schema material, while the exact target has one recorded edge. Matching the capability does not identify the standard or erase opt-in format/dependency limits.'),
      compare('commonmark_0_31_2','document_representation','cmark_implements_commonmark_0_31_2','Document representation selects cmark, cmark-gfm and html5lib, but the explicit CommonMark edge is cmark only and excludes GFM. Sharing the annotation does not establish equivalent parser/extension behavior.'),
      compare('rdf_1.2_concepts','graph_representation','rdf_turtle_implements_rdf_model','The existing implements source is a standard/format, not an implementation-profile object. CLI and workspace differ intentionally in profile filtering. The raw evidence field is absent and normalized evidence is empty, but the relation has legacy sources and both endpoints have sources; preserve those field roles rather than relabeling or claiming evidence is wholly absent.')]
    context_omissions=[]
    for r in impl:
        d=normalize_relation(r);s=index[d.source_id]
        caps=s.get('capabilities') or []
        if caps and not d.context.get('capabilities'):
            context_omissions.append({'relation_id':d.relation_id,'source_id':d.source_id,'target_id':d.target_id,
              'raw_source_capabilities':_state(s,'capabilities'),'raw_relation_context':_state(r,'context'),
              'raw_legacy_capability_context':_state(r,'capability_context'),
              'relation_recovery':recovery(r,['context','capability_context','evidence','sources']),
              'source_recovery':recovery(s,['capabilities','sources']),
              'evidence_urls':[e.get('url') for e in d.evidence],
              'meaning':'Object membership does not supply relation-context membership; the relation remains retrievable by its explicit source/target edge.'})
    summary={
      'denominator':f'All {len(impl)} explicit implements records loaded only from current configured canonical storage at the supplied base; not all real implementations, not coverage completeness, not supportability or conformance.',
      'canonical_objects':len(objects),'canonical_relations':len(relations),'explicit_implements_records':len(impl),'distinct_source_objects':len(sources),
      'implementation_profile_records':sum(has_profile(index[normalize_relation(r).source_id],'implementation',registry) for r in impl),
      'distinct_implementation_profile_source_objects':len(impl_sources),
      'source_capability_field_state_by_edge':dict(collections.Counter(_state(index[normalize_relation(r).source_id],'capabilities')['state'] for r in impl)),
      'source_capability_field_state_by_distinct_source':dict(collections.Counter(_state(index[sid],'capabilities')['state'] for sid in sources)),
      'edge_evidence_field_states':dict(collections.Counter(_state(r,'evidence')['state'] for r in impl)),
      'edge_legacy_sources_field_states':dict(collections.Counter(_state(r,'sources')['state'] for r in impl)),
      'normalized_context_with_capabilities':sum(bool(normalize_relation(r).context.get('capabilities')) for r in impl),
      'object_annotation_without_relation_context_examples':len(context_omissions),
      'all_explicit_edges_resolved':all(any(e.relation_id==r['id'] for e in graph.edges) for r in impl),
      'graph_reference_issue_count':len(graph.issues)}
    result = {'scope':'One-shot exception-focused read-only audit; no new ontology, API, capability backfill, UI/display or maintenance process.',
      'summary':summary,
      'selector_contracts':[
       {'entry':'bootstrap_query.implementations_for_capability','selects':'existing implementation profile AND direct source capabilities membership','does_not':'traverse implements, inherit target capabilities, or return relation scope'},
       {'entry':'workspace_projection.select_by_capability','selects':'direct capability membership, without implementation-profile filtering','does_not':'infer equivalence or consult relation context'},
       {'entry':'GraphIndex.relation_objects_for_capability','selects':'normalized relation.context.capabilities membership only','does_not':'inherit object or target capability annotations'},
       {'entry':'GraphIndex.backlinks(target_id) filtered origin=relation/kind=implements','selects':'exact explicitly recorded edges to target','does_not':'assert implementation profile, whole-standard conformance or capability membership; join relation_id to original record and normalize_relation for complete context/evidence'}],
      'counterexamples':examples,'object_annotation_without_relation_context':context_omissions,
      'interpretation_boundaries':['Absent capabilities means not recorded in that field, not incapable or unsupported.','An absent implements edge does not prove nonimplementation.','Whole implementation object identity does not broaden a bounded relation.','Relation evidence, legacy relation sources, and endpoint object sources are distinct roles; normalize_relation only carries evidence.','Counts describe only this finite traversal; no coverage percentage or priority ranking follows.','Existing runtime checks here do not execute or revalidate upstream libraries.','The RDF implements row is observed historical graph data, not a new semantic approval; separate provides or maps_to evidence does not validate it.','Source/target scope, version and source-list recovery preserves existing context, not field-specific proof or freshly verified publication status.'],
      'proposed_next_deliverable':'Integrate these finite counterexamples and the reproducible existing-function recipe into the current broad evidence report. Retain exact IDs, raw field states, complete relation context or its verified canonical recovery path, and source URLs. No capability backfill, new query API, classification change, inventory snapshot or UI/display work is needed to demonstrate noninterchangeability.'}

    if not include_full_context:
        for item in result['counterexamples']:
            d=item['representative_bounded_relation']
            d['normalized_context_recovery']={'relation_id':d['relation_id'],'physical_source':d['relation_recovery']['physical_source'],'read':'Resolve exact relation by id and call existing normalize_relation; use complete context, not a bare edge.'}
            del d['normalized_context']
            d['raw_relation_context'].pop('value',None)
            evidence=d['raw_relation_evidence'].pop('value',None)
            d['raw_relation_evidence']['count']=len(evidence or [])
            d['relation_evidence_urls']=[item.get('url') for item in evidence or [] if isinstance(item,dict)]
            legacy_sources=d['raw_relation_sources'].pop('value',None)
            d['raw_relation_sources']['count']=len(legacy_sources or [])
            d['legacy_relation_source_urls']=[item.get('url') for item in legacy_sources or [] if isinstance(item,dict)]
            for key in ('source_source_urls','target_source_urls'):
                urls=d[key]
                d[key+'_count']=len(urls)
                d[key+'_examples']=urls[:1]
                del d[key]
        for d in result['object_annotation_without_relation_context']:
            d['raw_relation_context'].pop('value',None)
    assert summary['explicit_implements_records'] == 47
    assert summary['distinct_source_objects'] == 44
    assert summary['distinct_implementation_profile_source_objects'] == 43
    assert summary['implementation_profile_records'] == 46
    assert summary['source_capability_field_state_by_edge'] == {'absent': 26, 'recorded': 21}
    assert summary['edge_evidence_field_states'] == {'recorded': 46, 'absent': 1}
    assert summary['edge_legacy_sources_field_states'] == {'absent': 46, 'recorded': 1}
    assert summary['all_explicit_edges_resolved'] and summary['graph_reference_issue_count'] == 0
    assert len(context_omissions) == 3
    return result


def intake_receipt(path):
    if path is None:
        return {'status': 'NOT_RUN_BY_THIS_RECIPE',
                'command': 'PYTHONDONTWRITEBYTECODE=1 python 02_Runtime/01_Engine/intake_coverage_audit.py --root . > intake-audit.json'}
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    assert digest == INTAKE_SHA256
    result = json.loads(raw)
    assert result['outcome'] == 'PASS / STRUCTURAL AND REFERENCE CHECKS ONLY'
    assert len(result['pre_materialization_routes']) == 163
    return {'status': 'VERIFIED_SEPARATE_RUN_RECEIPT', 'sha256': digest, 'bytes': len(raw),
        'outcome': result['outcome'], 'totals': result['totals'], 'plan': result['plan'],
        'frozen_pre_materialization_routes': len(result['pre_materialization_routes']),
        'boundary': 'Separately executed existing intake audit at this baseline; not semantic acceptance or proof of reviewer independence.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--intake-result', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    assert git(root, 'rev-parse', 'HEAD') == BASELINE
    assert not git(root, 'status', '--porcelain', '--untracked-files=no')
    # The loaders consume local YAML and Python paths, including ignored/untracked inputs.
    untracked = git(root, 'ls-files', '--others', '--', '01_State', '02_Runtime/01_Engine').splitlines()
    unsafe = [p for p in untracked if not (Path(p).parent == Path('02_Runtime/01_Engine/__pycache__') and Path(p).suffix == '.pyc')]
    assert not unsafe, f'Untracked consumed-area inputs: {unsafe}'
    sys.path.insert(0, str(root / '02_Runtime/01_Engine'))
    result = {'baseline': BASELINE, 'mode': 'one-shot read-only research audit',
        'boundaries': ['No Canonical, Runtime, taxonomy, relationship semantics, or maintenance contract changes.',
            'No full inventory values exported; summaries and decision-relevant exceptions only.',
            'No upstream installation, execution, network request, date refresh, or publication.',
            'No retry or replacement of the uncertain historical snapshot publication; all existing holds remain.',
            'Annotation absence, missing source fields, and negative technical evidence are distinct.'],
        'navigation_and_fields': current_record_audit(root),
        'relation_and_capability_selection': implementation_audit(root),
        'separate_intake_audit_receipt': intake_receipt(args.intake_result)}
    result['relation_and_capability_selection'].pop('proposed_next_deliverable', None)
    # Give compact recovery records exact immutable repository URLs.
    def add_recovery_links(value):
        if isinstance(value, dict):
            if 'physical_source' in value:
                value['pinned_source'] = link(value['physical_source'])
            for child in list(value.values()):
                add_recovery_links(child)
        elif isinstance(value, list):
            for child in value:
                add_recovery_links(child)
    add_recovery_links(result)
    result['decisions'] = [
        {'decision': 'Retain current navigation, the eight identity holds, and duplicate-only BCP47. No missing accepted navigation target was found.',
         'sources': [link('01_State/Inbox/relations/intake-coverage-20260913.yaml'), link('02_Runtime/01_Engine/intake_coverage_audit.py#L154-L245')]},
        {'decision': 'For an exact standard target, recover its explicit implements edges, complete raw/normalized context and evidence, and any legacy relation.sources separately from endpoint sources. Capability selectors answer different questions and are not substitutes; no normalizer or relation semantic change is proposed.',
         'sources': [link('02_Runtime/01_Engine/bootstrap_query.py#L100-L109'), link('02_Runtime/01_Engine/workspace_projection.py#L45-L64'), link('02_Runtime/01_Engine/graph_index.py')]},
        {'decision': 'Do not turn the 22 role-qualified sources absences or the 73 notes_zh-only assessment absences into automatic repair work. Read the original role, description, scope and source fields.',
         'sources': [link('02_Runtime/01_Engine/workspace_projection.py#L67-L117'), link('01_State/01_Objects/interopatlas-fact-source.yaml'), link('01_State/01_Objects/data_serialization.yaml')]},
        {'decision': 'Do not infer verification history from absence of a literal last_verified_at field, or substitute accessed/Git/research dates. This recipe checks field recovery, not historical or external freshness.',
         'sources': [link('docs/02_System/01_Knowledge/03_Provenance/provenance-traceability-profile.zh-CN.md')]},
        {'decision': 'No automatic capability backfill, edge semantic change, new query contract or coverage-complete claim follows from this audit.',
         'sources': [link('02_Runtime/01_Engine/workspace_projection.py#L45-L64'), link('PROJECT_STATE.md')]},
    ]
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True, default=str))


if __name__ == '__main__':
    main()
