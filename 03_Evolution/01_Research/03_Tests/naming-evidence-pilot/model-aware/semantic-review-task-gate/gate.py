"""Deterministic task-understanding gate for naming semantic-review outputs.

This gate does NOT judge whether a candidate name is good, whether a reviewer agrees
with another reviewer, or whether advance/hold/stop is correct. It only detects
whether the response demonstrates enough task-level understanding to be eligible
for later semantic evidence use.

Outcomes:
- pass: no task-understanding stop condition observed.
- review: no decisive task-layer failure, but a weak/over-literal pattern remains.
- block: explicit task/object confusion, instruction leakage into candidate evidence,
  circular candidate grounding, or missing candidate grounding.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

BLOCK = "block"
REVIEW = "review"
PASS = "pass"

INSTRUCTION_LEAK = re.compile(
    r"\b(frozen brief|output[_ -]?contract|review dimensions?|task instructions?|candidate id|"
    r"validation (?:process|procedure)|the phrase ['\"]?validation)\b",
    re.I,
)

PRODUCT_BURDEN = [
    re.compile(r"\bit[’']?s a name, not a tool\b", re.I),
    re.compile(r"\blacks? inherent product features?\b", re.I),
    re.compile(r"\b(?:candidate )?name\b.{0,80}\blacks? (?:a |an )?(?:defined )?(?:product )?function\b", re.I),
    re.compile(r"\b(?:candidate )?name\b.{0,80}\b(?:offers?|provides?) no inherent (?:analytical|functional|product) value\b", re.I),
    re.compile(r"\bno inherent (?:analytical|functional|product) value\b", re.I),
]

OVER_LITERAL = [
    re.compile(r"\bdoes not directly (?:address|describe|encode|state|express)\b", re.I),
    re.compile(r"\bdoesn't directly (?:address|describe|encode|state|express)\b", re.I),
    re.compile(r"\bdoes not inherently (?:describe|encode|state|express)\b", re.I),
]

CIRCULAR = [
    re.compile(r"\bcontains the (?:word|exact candidate name)\b", re.I),
    re.compile(r"\bcontains the word\b", re.I),
]


def _strings(review: dict) -> dict[str, list[str]]:
    return {
        "observable_form": [str(v) for v in review.get("observable_form", [])],
        "associations": [str(v) for v in review.get("association_hypotheses", [])],
        "pronunciation": [str(review.get("pronunciation_uncertainty", {}).get("reason", ""))],
        "brief_fit": [str(review.get("brief_fit", {}).get("reason", ""))],
        "reason": [str(review.get("reason", ""))],
    }


def _normalized(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", value.casefold())).strip()


def evaluate(candidate_name: str, review: dict) -> dict:
    """Return task-understanding disposition with explicit machine reasons."""
    sections = _strings(review)
    findings: list[dict] = []

    observable_text = "\n".join(sections["observable_form"])
    evidence_text = "\n".join(sections["observable_form"] + sections["associations"])
    judgment_text = "\n".join(sections["brief_fit"] + sections["reason"])

    if candidate_name.casefold() not in observable_text.casefold():
        findings.append({"severity": BLOCK, "code": "candidate_not_grounded_in_observable"})

    for text in sections["observable_form"] + sections["associations"]:
        match = INSTRUCTION_LEAK.search(text)
        if match:
            findings.append({"severity": BLOCK, "code": "instruction_or_brief_treated_as_candidate_evidence", "excerpt": match.group(0)})
            break

    for pattern in PRODUCT_BURDEN:
        match = pattern.search(judgment_text)
        if match:
            findings.append({"severity": BLOCK, "code": "name_burdened_with_product_function", "excerpt": match.group(0)})
            break

    circular = None
    for pattern in CIRCULAR:
        circular = pattern.search("\n".join(sections["observable_form"] + sections["reason"]))
        if circular:
            findings.append({"severity": BLOCK, "code": "circular_candidate_grounding", "excerpt": circular.group(0)})
            break

    # Repeating an observation verbatim as the final rationale is a circularity signal
    # only when it is candidate-identification rather than a substantive comparison.
    final_reason = _normalized(sections["reason"][0])
    normalized_observations = {_normalized(v) for v in sections["observable_form"]}
    if final_reason and final_reason in normalized_observations and len(final_reason.split()) <= 12:
        if not any(f["code"] == "circular_candidate_grounding" for f in findings):
            findings.append({"severity": BLOCK, "code": "short_observation_reused_as_final_reason"})

    for pattern in OVER_LITERAL:
        match = pattern.search(judgment_text)
        if match:
            findings.append({"severity": REVIEW, "code": "possible_literal_function_encoding_assumption", "excerpt": match.group(0)})
            break

    # Generic value claims are not decisive task misunderstanding, but they are not
    # enough to qualify a reviewer by themselves.
    generic_claims = re.compile(r"\b(memorable|brand recognition|clear purpose|good fit|bad fit)\b", re.I)
    if generic_claims.search("\n".join(sections["reason"])) and not findings:
        findings.append({"severity": REVIEW, "code": "generic_unanchored_final_rationale"})

    severity = PASS
    if any(f["severity"] == BLOCK for f in findings):
        severity = BLOCK
    elif any(f["severity"] == REVIEW for f in findings):
        severity = REVIEW

    return {
        "candidate": candidate_name,
        "task_understanding": severity,
        "eligible_for_semantic_evidence": severity == PASS,
        "findings": findings,
        "scope": "task_understanding_only_not_name_quality_or_disposition_correctness",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON object with candidate/name and review")
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    candidate = data.get("candidate") or data.get("name")
    if not isinstance(candidate, str) or not isinstance(data.get("review"), dict):
        raise SystemExit("input must contain candidate/name and review object")
    print(json.dumps(evaluate(candidate, data["review"]), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
