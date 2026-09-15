"""Build bounded snapshot v97 -> v98 after SEM-408-005 gate false negatives."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

NEXT_ACTION="define_semantic_judgment_validation_contract_and_small_model_role_boundary_without_new_inference"
NEXT="""next_action:
  action: define_semantic_judgment_validation_contract_and_small_model_role_boundary_without_new_inference
  rationale: >-
    SEM-408-005按v97计划对既有C002/C006各执行一次确认请求，旧Gate v1均判pass，但事后检查发现C002把synthetic brief元信息
    虚构的/fictional带入候选语义，C006最终reason大段复述task boundary；因此两个pass均为false negative。Gate v2加入任务本地
    context-only provenance与长指令重合检查，永久CI通过，并在不改写原结果的后验重放中把C002/C006均判block；SEM-408-004/C003
    仍保持pass。继续增加prompt/gate规则存在对单一开发任务过拟合风险，故暂停新的Reviewer推理。下一步只基于现有SEM-408-003~005、
    selector稳定性和作者审计证据，冻结“语义判断正确性”验证合同及小模型可承担/不可承担的角色边界，再决定是否需要独立参考模型或
    Owner本地模型参与。该工作不产生新名称，不恢复IA/G0-G8，也不改变Simple vs redesign当前无赢家结论。
  requires_owner: false_for_bounded_method_analysis_no_new_inference_paid_or_ia_generation

"""
SECTION="""
# v98: original gate decisions are preserved; v2 replay records false negatives separately.
semantic_task_gate_revision:
  id: SEM-408-TASK-GATE-002
  status: gate_v2_regression_passed_sem005_false_negatives_confirmed_new_reviewer_inference_paused
  primary_issue: 408
  source_experiment:
    id: SEM-408-005
    run: 34744595667
    job: 103690048899
    source_commit: 57c2a9dbe18a814651542aa448da630815ffba8c
    evidence_commit: 160f376edbf139b32b6f89917b640dc0bfe4b2c1
    artifact: 10314065187
    artifact_sha256: 279143b544d837865818c7ab0743db55ddf63872c41325ad8c970bd1e1bb9fec
    report: naming-evidence-pilot/model-aware/semantic-review-pilot-005/REPORT.zh-CN.md
    requests_dispatched: 2
    retries: 0
    candidates: [{id: C002, name: Diffly}, {id: C006, name: Sublyte}]
    original_gate_version: v1_pre_version_field
    original_gate_results: {C002: pass, C006: pass}
    original_results_mutated: false
    stopped_early: false
    stop_policy_limit: first_request_false_pass_allowed_second_request_within_frozen_max_two
    new_names: 0
    paid_api_calls: 0
    semantic_quality_validated: false
    quality_ground_truth: null
  diagnosed_false_negatives:
    C002:
      classification: context_only_metadata_leaked_into_review
      observation: synthetic brief marker 虚构的/fictional influenced association and fit reasoning
      name_quality_inference: none
    C006:
      classification: instruction_echo_in_review
      observation: final reason substantially copied the task-boundary instructions
      name_quality_inference: none
  gate_v2:
    version: 2.0-experimental
    implementation: naming-evidence-pilot/model-aware/semantic-review-task-gate/gate.py
    fixtures: naming-evidence-pilot/model-aware/semantic-review-task-gate/fixtures.json
    tests: naming-evidence-pilot/model-aware/semantic-review-task-gate/test_gate.py
    permanent_ci_run: 34744993746
    permanent_ci_result: success
    changes:
      - optional task-local context_only_terms for provenance metadata
      - six-token structural overlap check for instruction echo anywhere in review
    replay:
      SEM-408-004_C003: pass
      SEM-408-005_C002: block
      SEM-408-005_C006: block
    replay_semantics: posthoc_task_understanding_assessment_not_mutation_or_name_quality_rescore
    limitations:
      - same-author deterministic gate
      - task-local provenance terms require explicit construction
      - pass does not establish semantic correctness
      - additional rule growth risks development-task overfit
  model_budget_since_v96:
    SEM-408-004_requests: 1
    SEM-408-005_requests: 2
    total_reviewer_requests: 3
    paid_api_calls: 0
    new_names: 0
  current_inference_policy:
    new_reviewer_calls: paused_pending_semantic_validation_contract
    reason: task-understanding qualification_is_not_semantic_accuracy_and_gate_patching_should_not_become_the_method
  method_comparison_effect:
    simple_vs_redesign_winner: not_established
    reviewer_evidence_effect: insufficient_for_quality_comparison
  ia_generation: false
  stable_skill_changed: false
  stable_promotion: false
"""


def build(text:str)->str:
    if text.count("  snapshot_version: 97\n")!=1: raise ValueError("expected_snapshot_97_once")
    if "\nsemantic_task_gate_revision:" in text: raise ValueError("v98_section_already_present")
    match=re.search(r"^next_action:\n.*?(?=^stop:\n)",text,re.M|re.S)
    if not match or "confirm_task_understanding_on_two_distinct_historical_failure_types" not in match.group(0):
        raise ValueError("unexpected_next_action")
    text=text[:match.start()]+NEXT+text[match.end():]
    text=text.replace("  snapshot_version: 97\n","  snapshot_version: 98\n",1)
    return text.rstrip()+"\n"+SECTION


def main()->int:
    p=argparse.ArgumentParser();p.add_argument("input",type=Path);p.add_argument("output",type=Path);a=p.parse_args()
    a.output.write_text(build(a.input.read_text()));return 0

if __name__=="__main__": raise SystemExit(main())
