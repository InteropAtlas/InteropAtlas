"""REAL-408-002 reuses the frozen REAL-408-001 transport and adds only the
shared fail-closed lossless format boundary. The original model bytes remain in
calls/*/output.txt; normalized bytes and transformation audits are separate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
sys.path.insert(0,str(HOME))
import protocol as p
import format_adapter as f

BASE_RUN=HOME/'real-pilot/run.py'
source=BASE_RUN.read_text(encoding='utf-8')
require_id=source.count('REAL-408-001')
if require_id < 5:
    raise RuntimeError('unexpected_REAL_408_001_runner_identity')
source_sha=hashlib.sha256(source.encode()).hexdigest()
source=source.replace('REAL-408-001','REAL-408-002')
source=source.replace("BASE = 'e5d538964e15db5f84d2c73296a5d033b9e2f68f'","BASE = 'ff8e422bf52f614403926a1547f835903f35dae1'")
ns={'__name__':'real408002_derived','__file__':str(BASE_RUN)}
exec(compile(source,str(BASE_RUN)+'[REAL-408-002-derived]','exec'),ns)
BaseBackend=ns['Backend']

class NormalizingBackend(BaseBackend):
    def __call__(self, root, plan, step, task, role, limit):
        raw, execution_ref, execution_kind=super().__call__(root,plan,step,task,role,limit)
        question=json.loads(task['question'])
        normalized,audit=f.normalize(raw,question)
        call=root/'calls'/step
        audit.update(experiment_id='REAL-408-002',step=step,
                     original_model_output_sha256=p.digest(raw),
                     normalized_bytes_used_by_workflow=bool(audit['changed']))
        audit_path=call/'format-normalization.json'
        if audit_path.exists():
            if p.read(audit_path)!=audit: raise ValueError('normalization_audit_changed')
        else:
            p.write_new(audit_path,audit)
        if audit['changed']:
            target=call/'normalized-output.txt'
            if target.exists():
                if target.read_bytes()!=normalized: raise ValueError('normalized_output_changed')
            else:
                with target.open('xb') as stream: stream.write(normalized)
        return normalized,execution_ref,execution_kind

ns['Backend']=NormalizingBackend

def setup(output:Path,runtime:Path):
    ns['setup'](output,runtime)
    identity=p.read(output/'identity.json')
    identity.update(experiment_id='REAL-408-002',derived_transport_runner_sha256=source_sha,
                    format_adapter_sha256=p.digest((HOME/'format_adapter.py').read_bytes()),
                    normalization='representation_only_fail_closed_raw_bytes_preserved')
    (output/'identity.json').write_bytes(p.canonical(identity))
    plan=p.read(output/'preregistered-plan.json')
    plan.update(experiment_id='REAL-408-002',prior_experiment='REAL-408-001',
                only_method_change='shared_lossless_format_adapter',
                old_failures_not_rescored=True,
                normalization_rules=['wrap complete exact-contract proposal array in candidates object',
                                     'remove review name only when exact ID-name pair matches supplied input'],
                unsafe_shape_policy='preserve raw and block; no semantic repair')
    (output/'preregistered-plan.json').write_bytes(p.canonical(plan))


def execute(output:Path):
    ns['execute'](output)
    summary=p.read(output/'summary.json')
    summary['experiment_id']='REAL-408-002'
    summary['normalization_layer']='format_adapter.py representation_only'
    summary['comparison_to_REAL_408_001']='new_run_only_no_retroactive_rescore'
    (output/'summary.json').write_bytes(p.canonical(summary))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['setup','execute'])
    parser.add_argument('--output',type=Path,required=True);parser.add_argument('--runtime',type=Path)
    args=parser.parse_args()
    if args.command=='setup': setup(args.output,args.runtime)
    else: execute(args.output)
