"""Build the bounded snapshot v96 -> v97 reviewer-qualification transition."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

NEXT_ACTION = "confirm_task_understanding_on_two_distinct_historical_failure_types"

NEXT = """next_action:
  action: confirm_task_understanding_on_two_distinct_historical_failure_types
  rationale: >-
    SEM-408-TASK-GATE-001已建立确定性任务理解门槛，历史SEM-408-003六项重放为5 block / 1 review / 0 pass。
    SEM-408-004随后只对既有C003/Linetap执行一次真实canary，在明确identity-label与产品实现边界后得到task_gate=pass；
    这说明包装修复值得继续，但单一样本不足以证明泛化。下一步只用既有C002与C006，分别覆盖历史instruction leakage与
    circular grounding失败类型；每项独立、无重试、无新名称，任一非pass即停止扩大。即使全部pass也只进入语义正确性研究，
    不构成名称质量真值、方法胜负或稳定晋升。
  requires_owner: false_for_bounded_existing_candidate_method_research_no_paid_or_ia_generation

"""

SECTION = """
# v97: task-understanding qualification is distinct from semantic-quality validity.
semantic_task_understanding_validation:
  id: SEM-408-TASK-QUAL-001
  status: deterministic_gate_validated_single_real_canary_passed_confirmation_pending
  primary_issue: 408
  gate:
    implementation: naming-evidence-pilot/model-aware/semantic-review-task-gate/gate.py
    fixtures: naming-evidence-pilot/model-aware/semantic-review-task-gate/fixtures.json
    tests: naming-evidence-pilot/model-aware/semantic-review-task-gate/test_gate.py
    report: naming-evidence-pilot/model-aware/semantic-review-task-gate/REPORT.zh-CN.md
    ci_run: 34744133574
    ci_artifact: 10312508886
    historical_sem003_replay: {block: 5, review: 1, pass: 0, semantic_evidence_eligible: 0}
    scope: task_understanding_only_not_name_quality_or_disposition_correctness
    same_author_rule_based_gate: true
  canary:
    experiment: SEM-408-004
    candidate: {id: C003, name: Linetap, source: existing_DEV-02_only}
    run: 34744282097
    job: 103689175084
    evidence_commit: 6659c3ac5b3e19affa5fe556d9362a025dd6ad1b
    artifact: 10313663077
    artifact_sha256: b109baee713b7b7601fa06da53877fbfdd6bfd633de486256563202f2cf6eb79
    requests_dispatched: 1
    retries: 0
    task_gate: pass
    gate_findings: []
    semantic_evidence_eligible: true
    semantic_quality_validated: false
    quality_ground_truth: null
    input_tokens: 540
    output_tokens: 213
    inference_seconds: 31.01624691500001
    report: naming-evidence-pilot/model-aware/semantic-review-pilot-004/REPORT.zh-CN.md
  interpretation:
    - single_canary_pass_supports_continuing_task_packaging_validation_not_reviewer_quality
    - no_qwen_gemma_quality_winner_or_method_winner_inferred
    - association_hypotheses_remain_unverified_even_when_task_gate_passes
  confirmation_plan:
    candidates: [C002, C006]
    historical_failure_types: [instruction_or_brief_leakage, circular_candidate_grounding]
    max_requests: 2
    retries: 0
    stop_on_first_nonpass: true
    new_names: 0
    paid_api_calls: 0
    automatic_expansion_after_pass: false
  new_model_calls_this_revision: 1
  new_names: 0
  paid_api_calls: 0
  ia_generation: false
  stable_skill_changed: false
  stable_promotion: false
"""


def build(text: str) -> str:
    if text.count("  snapshot_version: 96\n") != 1:
        raise ValueError("expected_snapshot_96_once")
    if "\nsemantic_task_understanding_validation:" in text:
        raise ValueError("v97_section_already_present")
    match = re.search(r"^next_action:\n.*?(?=^stop:\n)", text, re.M | re.S)
    if not match or "qualify_independent_reviewer_task_understanding_before_further_inference" not in match.group(0):
        raise ValueError("unexpected_next_action")
    text = text[:match.start()] + NEXT + text[match.end():]
    text = text.replace("  snapshot_version: 96\n", "  snapshot_version: 97\n", 1)
    return text.rstrip() + "\n" + SECTION


def main() -> int:
    parser=argparse.ArgumentParser();parser.add_argument("input",type=Path);parser.add_argument("output",type=Path)
    args=parser.parse_args();args.output.write_text(build(args.input.read_text()))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
