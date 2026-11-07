"""Build bounded snapshot v98 -> v99 after semantic contract and packet validation."""
from __future__ import annotations
import argparse
from pathlib import Path
import re

NEXT="""next_action:
  action: execute_bounded_reference_packet_001_with_independent_mistral_nemo_12b_cpu
  rationale: >-
    v98已冻结五层语义验证合同与小模型角色边界，并冻结SEM-408-REF-PACKET-001四个既有DEV-02候选；常设CI已验证
    packet不含旧排名、方法标签、generator risk或实验provenance元信息。当前4B证据支持“小模型可做探索提案、不可自动做最终质量裁判”。
    下一步不是恢复4B Reviewer，而是在免费GitHub标准CPU上使用不同模型家族的Mistral-Nemo-Instruct-2407 12B Q4_K_M，
    对冻结packet最多执行4个独立参考请求、无重试。该12B输出仅是reference opinion，不是ground truth；运行只用于逐claim校准
    和判断已观察失败是否跨模型/规模持续，不产生新名称、不做现实筛查、不比较Simple vs redesign winner、不恢复IA/G0-G8。
  requires_owner: false_for_bounded_free_reference_calibration_existing_candidates_only

"""
SECTION="""
# v99: semantic contract is frozen before any new reference inference.
semantic_validation_contract:
  id: SEM-408-ROLE-CONTRACT-001
  status: contract_and_reference_packet_validated_reference_execution_authorized_bounded
  primary_issue: 408
  contract:
    document: naming-evidence-pilot/model-aware/semantic-validation-contract/CONTRACT.zh-CN.md
    machine_boundary: naming-evidence-pilot/model-aware/semantic-validation-contract/role-boundary.json
    validator: naming-evidence-pilot/model-aware/semantic-validation-contract/validate.py
    tests: naming-evidence-pilot/model-aware/semantic-validation-contract/test_validate.py
    permanent_ci: .github/workflows/naming-semantic-contract.yml
    latest_ci_run: 34745970452
    latest_ci_result: success
    levels: [L0_task_understanding, L1_candidate_grounding, L2_claim_calibration, L3_comparative_reliability, L4_human_external_validity]
  role_boundary:
    candidate_generation: conditional_allowed
    surface_observation: conditional_allowed
    semantic_association: hypothesis_only
    resource_triage: conditional_allowed_conservative_hold_on_instability
    final_quality_selector: not_validated_for_autonomous_use
    reality_legal_domain_clearance: authoritative_tools_required
    owner_preference_inference: explicit_feedback_or_reversible_hypothesis_only
    final_adoption: owner_only
    tested_scope: 4B_Qwen_and_Gemma_development_evidence_only
    owner_30B_MoE_generalization: not_established
  reference_packet:
    id: SEM-408-REF-PACKET-001
    file: naming-evidence-pilot/model-aware/semantic-validation-contract/reference-packet-001.json
    tests: naming-evidence-pilot/model-aware/semantic-validation-contract/test_packet.py
    cases: [{packet_id: P01, source_id: C001}, {packet_id: P02, source_id: C002}, {packet_id: P03, source_id: C003}, {packet_id: P04, source_id: C006}]
    existing_candidates_only: true
    independent_reference_obtained: false
    quality_ground_truth: null
    model_calls_in_packet_creation: 0
    new_names: 0
  reference_strategy:
    document: naming-evidence-pilot/model-aware/semantic-validation-contract/REFERENCE-STRATEGY.zh-CN.md
    production_policy: cheap_exploration_deterministic_boundaries_periodic_reference_calibration_owner_at_high_value_gates
    strong_or_reference_model_is_pipeline_requirement: false
    reference_opinion_is_ground_truth: false
  bounded_reference_authorization:
    experiment: SEM-408-006
    model_family: Mistral_Nemo
    model_repo: bartowski/Mistral-Nemo-Instruct-2407-GGUF
    model_file: Mistral-Nemo-Instruct-2407-Q4_K_M.gguf
    expected_file_sha256: 7c1a10d202d8788dbe5628dc962254d10654c853cae6aaeca0618f05490d4a46
    execution_location: github_standard_cpu
    packet: SEM-408-REF-PACKET-001
    max_requests: 4
    retries: 0
    paid_api_calls: 0
    new_names: 0
    ia_generation: false
    reality_search: false
    method_winner_inference: false
    semantic_quality_ground_truth: null
    automatic_expansion: false
  current_method_comparison:
    simple_default: true
    redesign_optional: true
    winner: not_established
  stable_skill_changed: false
  stable_promotion: false
"""

def build(text:str)->str:
    if text.count('  snapshot_version: 98\n')!=1: raise ValueError('expected_snapshot_98_once')
    if '\nsemantic_validation_contract:' in text: raise ValueError('v99_section_already_present')
    m=re.search(r'^next_action:\n.*?(?=^stop:\n)',text,re.M|re.S)
    if not m or 'define_semantic_judgment_validation_contract_and_small_model_role_boundary_without_new_inference' not in m.group(0):raise ValueError('unexpected_next_action')
    text=text[:m.start()]+NEXT+text[m.end():]
    text=text.replace('  snapshot_version: 98\n','  snapshot_version: 99\n',1)
    return text.rstrip()+'\n'+SECTION

def main()->int:
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args();a.output.write_text(build(a.input.read_text()));return 0

if __name__=='__main__':raise SystemExit(main())
