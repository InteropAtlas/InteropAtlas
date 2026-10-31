from __future__ import annotations
import argparse
import json
from pathlib import Path

LEVELS = [
    "L0_task_understanding",
    "L1_candidate_grounding",
    "L2_claim_calibration",
    "L3_comparative_reliability",
    "L4_human_external_validity",
]


def validate(data: dict) -> dict:
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version")
    levels = data.get("semantic_validation_levels", {})
    if list(levels) != LEVELS:
        errors.append("validation_level_order_or_membership")
    roles = data.get("roles", {})
    required_roles = {
        "candidate_generation",
        "surface_observation",
        "semantic_association",
        "resource_triage",
        "final_quality_selector",
        "reality_legal_domain_clearance",
        "owner_preference_inference",
        "final_adoption",
    }
    if set(roles) != required_roles:
        errors.append("role_set")
    known_levels = set(LEVELS)
    for name, role in roles.items():
        unknown = set(role.get("required_levels", [])) - known_levels
        if unknown:
            errors.append(f"unknown_levels:{name}:{sorted(unknown)}")
    if roles.get("candidate_generation", {}).get("status") != "conditional_allowed":
        errors.append("generation_must_remain_conditional")
    if roles.get("semantic_association", {}).get("automatic_quality_effect") != "none":
        errors.append("association_must_not_auto_score")
    triage = roles.get("resource_triage", {})
    if triage.get("automatic_drop_allowed") is not False or triage.get("unstable_decision_policy") != "route_to_hold":
        errors.append("triage_must_be_conservative")
    if roles.get("final_quality_selector", {}).get("status") != "not_validated_for_autonomous_use":
        errors.append("final_selector_must_remain_closed")
    if roles.get("final_adoption", {}).get("status") != "owner_only":
        errors.append("final_adoption_owner_only")
    if roles.get("reality_legal_domain_clearance", {}).get("language_model_role") != "summarize supplied evidence only":
        errors.append("reality_clearance_boundary")
    comparison = data.get("method_comparison", {})
    if comparison.get("simple_vs_redesign_winner") != "not_established":
        errors.append("method_winner_must_not_be_invented")
    if comparison.get("default_engineering_choice") != "simple" or comparison.get("redesign_role") != "optional exploration expansion":
        errors.append("current_engineering_choice_changed")
    rules = data.get("global_rules", {})
    expected_false = [
        "task_gate_pass_is_semantic_truth",
        "semantic_quality_ground_truth_exists",
        "new_reviewer_inference_authorized",
        "ia_generation_authorized",
        "paid_calls_authorized",
        "stable_skill_promotion_authorized",
    ]
    for key in expected_false:
        if rules.get(key) is not False:
            errors.append(f"must_be_false:{key}")
    if rules.get("new_names") != 0:
        errors.append("new_names_must_be_zero")
    scope = data.get("evidence_scope", {})
    not_validated = " ".join(scope.get("not_validated_for", []))
    if "30B/MoE" not in not_validated or "all small models" not in not_validated:
        errors.append("scope_must_not_generalize")
    return {"id": data.get("id"), "valid": not errors, "errors": errors, "role_count": len(roles), "level_count": len(levels)}


def main() -> int:
    p = argparse.ArgumentParser();p.add_argument("input", type=Path);p.add_argument("--output", type=Path);a=p.parse_args()
    result = validate(json.loads(a.input.read_text()))
    raw = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if a.output: a.output.write_text(raw)
    else: print(raw, end="")
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
