# Adaptive Naming v0.3.3 Regression Review — 2026-09-11

Purpose: verify that the live #411 Fit Test has not reintroduced previously fixed control defects. This is a behavioral regression review, not a naming-quality benchmark and not a restart of G0–G8.

## Summary

- `exercised_pass`: 13
- `not_triggered_but_contract_present`: 3
- `fail`: 0

The current live run supports freezing **v0.3.3 as the Fit-Test baseline** unless a new architecture/control defect appears. Naming search may continue without further Skill changes.

## Cases

| Case | Status | Live evidence / observation |
| --- | --- | --- |
| REG-001 search-path delegation | exercised_pass | v36 false Owner boundary was reclassified; subsequent route changes were autonomous. |
| REG-002 constraint provenance | exercised_pass | word-count remains a Controller search variable; no Agent-authored brief is treated as Owner provenance. |
| REG-003 isolation honesty | exercised_pass | generation remains `best_effort_same_context`; no false fresh-context claim. |
| REG-004 value flattening | exercised_pass | Mission / Value Model retains actors, agency relations, transformations and feedback structure. |
| REG-005 value-proxy collapse | exercised_pass | plurality/multiplicity is not treated as a substitute for individual agency; value targets remain separated. |
| REG-006 name overloading | exercised_pass | semantic grounding is secondary; the bare name is not required to encode the whole mission loop. |
| REG-007 scheduler monoculture | exercised_pass | portfolio moved across direct lexical, territory, grounded coinage, short coinage and longer proper-name architectures. |
| REG-008 rescue underuse | exercised_pass | reality-failed strong prototypes were explicitly audited for Rescue; no branch opened because low-distortion rescue would not solve the conflict or the base was also weak. |
| REG-009 rescue overfit | not_triggered_but_contract_present | no Rescue branch has opened, so overfit behavior has not been exercised live. |
| REG-010 evaluator anchoring | not_triggered_but_contract_present | no Owner-ready shortlist exists; Decision Hygiene remains correctly deferred. |
| REG-011 progressive disclosure | exercised_pass | Territory Research and Reality Screening were activated by specific triggers; Temporal/Validation/Activation modules stayed inactive. |
| REG-012 territory research trigger | exercised_pass | RND-054 material starvation triggered Territory Research before another equivalent generation batch. |
| REG-013 criteria role separation | exercised_pass | `.org` remains a finalist gate, recoverability/distinctiveness are optimization targets, Owner resonance is preference, formal TM clearance remains observed/deferred. |
| REG-014 territory vs generation | exercised_pass | after material starvation was partially resolved, weak outputs caused method/architecture changes rather than repeated Territory Research. |
| REG-015 Owner final choice | not_triggered_but_contract_present | no 2–3 finalist set exists; Controller has not fabricated final Owner resonance. |
| REG-016 reality-screen false negative | exercised_pass | N078–N080 feasibility claims were retracted, same-batch survivors rechecked, intrinsic quality preserved, Reality Screening Contract adopted. |

## Baseline decision

No new control-level defect appeared in the latest live microcycles. Therefore:

1. keep Skill version at **v0.3.3**;
2. stop architecture expansion by default;
3. only reopen Skill design if a new repeatable control failure is observed;
4. continue #411 primarily as a naming-search problem;
5. keep PR #416 Draft until the real naming task reaches a sufficiently stable outcome or Owner explicitly requests merge/review-state change.
