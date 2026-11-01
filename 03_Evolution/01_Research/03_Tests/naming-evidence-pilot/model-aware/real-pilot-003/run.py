"""REAL-408-003 is an evidence-persistence rerun of REAL-408-002.

Method, prompts, task, model, seeds, budgets, format adapter and evaluation rules
are unchanged. Only experiment identity and persistence metadata differ.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
sys.path.insert(0,str(HOME))
import protocol as p

BASE_RUN=HOME/'real-pilot-002/run.py'
source=BASE_RUN.read_text(encoding='utf-8')
if source.count('REAL-408-002') < 5:
    raise RuntimeError('unexpected_REAL_408_002_runner_identity')
source_sha=hashlib.sha256(source.encode()).hexdigest()
source=source.replace('REAL-408-002','REAL-408-003')
ns={'__name__':'real408003_derived','__file__':str(BASE_RUN)}
exec(compile(source,str(BASE_RUN)+'[REAL-408-003-derived]','exec'),ns)


def setup(output:Path,runtime:Path):
    ns['setup'](output,runtime)
    identity=p.read(output/'identity.json')
    identity.update(experiment_id='REAL-408-003',derived_from_REAL_408_002_sha256=source_sha,
                    execution_change_only='evidence_persistence_strategy_outside_model_workflow')
    (output/'identity.json').write_bytes(p.canonical(identity))
    plan=p.read(output/'preregistered-plan.json')
    plan.update(experiment_id='REAL-408-003',prior_experiment='REAL-408-002',
                rerun_reason='REAL-408-002 model execution finished but complete workdir was not persisted after optimistic concurrency blocked final branch write',
                method_prompt_task_model_seed_budget_format_adapter='identical_to_REAL_408_002',
                old_REAL_408_002_not_rescored=True,
                only_execution_change='final evidence commit rebases on verified current descendant head with second optimistic concurrency check')
    (output/'preregistered-plan.json').write_bytes(p.canonical(plan))


def execute(output:Path):
    ns['execute'](output)
    summary=p.read(output/'summary.json')
    summary['experiment_id']='REAL-408-003'
    summary['comparison_to_REAL_408_002']='new_calls_only_same_method_conditions_not_rescore'
    summary['execution_change_only']='evidence_persistence_strategy'
    (output/'summary.json').write_bytes(p.canonical(summary))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['setup','execute'])
    parser.add_argument('--output',type=Path,required=True);parser.add_argument('--runtime',type=Path)
    args=parser.parse_args()
    if args.command=='setup': setup(args.output,args.runtime)
    else: execute(args.output)
