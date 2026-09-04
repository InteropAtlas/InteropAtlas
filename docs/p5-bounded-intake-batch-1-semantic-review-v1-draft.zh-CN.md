# P5 Bounded Intake Batch 1 — Semantic Review v1 Draft

> Status: P5 Intake Stress Test Draft
>
> Work Item: #136
>
> Checked At: 2026-09-04
>
> Scope: experiment-level semantic review only. `accept` below means “fit to proceed as an ordinary Candidate through the intake contract”, not “write to production Canonical now”.

## 1. Review question

For the first five-item batch, answer three questions per candidate:

1. Is the candidate identity/evidence shape sufficiently clear to proceed through ordinary intake?
2. Is there an unresolved semantic decision that should defer Canonical acceptance rather than be guessed?
3. Which checks are safely automatable, and which require independent semantic review?

## 2. Experimental dispositions

| Candidate | Experiment disposition | Why | Production Canonical mutation |
| --- | --- | --- | --- |
| RFC 9114 — HTTP/3 | **ACCEPT TO ORDINARY INTAKE** | immutable RFC identity is clear; publisher identifier and official source are straightforward; unresolved relation minimum is non-blocking | not authorized |
| ISO/IEC 27001:2022 | **DEFER CANONICAL DECISION** | source and edition identity are clear, but work-vs-edition boundary and amendment representation are still architecture-sensitive | not authorized |
| Fetch Living Standard | **ACCEPT TO ORDINARY INTAKE WITH BOUNDARY** | stable subject/title + official living locator are enough; must explicitly separate upstream revision freshness from IA verification/record lifecycle | not authorized |
| FAPI 2.0 Security Profile | **DEFER CANONICAL DECISION** | candidate identity is clear, but profile/base/framework relation semantics could affect model shape and minimum relation assertions | not authorized |
| BCP 47 / RFC 5646 | **DUPLICATE / EXISTING OVERLAP** | current IA already has `bcp47_rfc5646`; creating a new subject would be wrong | not authorized |

No candidate is rejected as out-of-scope or invalid in this batch. One is stopped as duplicate, two can proceed through ordinary intake, and two are deferred at the semantic gate.

## 3. Candidate-by-candidate review

### C1 — RFC 9114 / HTTP/3

**Decision:** ACCEPT TO ORDINARY INTAKE.

Why:
- exact publisher identifier available (`RFC 9114`);
- official source is first-party RFC Editor;
- immutable publication model means current locator/version semantics are low ambiguity;
- no merge/split is implied;
- optional relations to QUIC / HTTP semantics can be added later without blocking subject admission if minimum relation policy permits zero/limited relations at first intake.

Required independent review before actual Canonical acceptance:
- verify title/status/source facts;
- verify no normalized identifier/alias collision;
- verify proposed classification is not over-specific;
- verify any relation assertion added in the same mutation.

### C2 — ISO/IEC 27001:2022

**Decision:** DEFER CANONICAL DECISION.

Why:
- publisher designation and edition facts are clear enough for a Candidate;
- however, this exact sample is intentionally one of the cases where P5 has not frozen whether `ISO/IEC 27001` work/family and `ISO/IEC 27001:2022` edition should be separate Canonical subjects;
- Amendment 1:2024 also pressures whether amendments are first-class publication artifacts, qualified relations, or embedded lifecycle/publication data.

A script must not resolve this by filename/title convention. The correct result is `deferred_pending_semantic_model_decision`, not rejection and not guessed acceptance.

### C3 — Fetch Living Standard

**Decision:** ACCEPT TO ORDINARY INTAKE WITH BOUNDARY.

Why:
- the stable subject is the WHATWG Fetch Living Standard;
- continuously changing text does not require a new IA subject per upstream revision;
- a current official locator can identify the publication surface;
- the critical condition is preserving separate clocks:
  - upstream source `last updated`;
  - IA source checked/accessed time;
  - IA `last_verified_at`;
  - IA record lifecycle timestamps.

The candidate can proceed because this boundary is already settled architecturally; exact production serialization remains provisional.

### C4 — FAPI 2.0 Security Profile

**Decision:** DEFER CANONICAL DECISION.

Why:
- title, publisher, final status and official source are clear;
- it is a genuine profile specification, not merely a marketing page;
- however, intake cannot yet safely decide whether the minimum accepted representation requires explicit `profiles` / `part_of_framework` relations and whether the broader FAPI 2.0 framework must already exist as a subject;
- accepting a taxonomy-only representation could lose the very semantics P4/P5 said must not be flattened.

Therefore the candidate remains valid and source-confirmed but waits on a bounded semantic decision. This is not a reason to block unrelated RFC/WHATWG intake.

### C5 — BCP 47 / RFC 5646

**Decision:** DUPLICATE / EXISTING OVERLAP.

Why:
- current IA object `bcp47_rfc5646` already represents the same candidate space;
- a new-object path is stopped before Canonical mutation;
- if the candidate carries better evidence or newer verification, it may become a future Evidence Contribution / Patch against the existing subject, but that is a different mutation intent.

This confirms dedup is an intake outcome, not an error condition.

## 4. Automation boundary

### Safe to automate or heavily assist

1. official URL host / first-party source checks;
2. extraction/normalization of known publisher identifiers (`rfc:9114`, ISO designation, OpenID spec slug);
3. exact and normalized identifier lookup against Candidate + Canonical indexes;
4. deterministic detection of known existing overlap when identifier match is strong;
5. fixture/schema syntax checks;
6. source presence / required-field completeness;
7. provenance carrier creation (Initiator / Executor / GitHub Actor slots);
8. routing obvious duplicate candidates away from new-subject creation;
9. flagging living-standard sources for separate freshness fields;
10. flagging profile/edition/amendment patterns for semantic review.

### Requires independent semantic review

1. work/family vs edition/version identity boundary;
2. merge/split/equivalence judgment;
3. whether a Profile requires one or more explicit base/framework relations for a minimally valid Canonical representation;
4. whether an unresolved relation can be deferred without misleading the object;
5. classification/family/kind choices when current taxonomy is provisional;
6. evidence sufficiency for nontrivial assertions;
7. conflict/scope interpretation;
8. mutation impact class when a seemingly ordinary intake changes model semantics.

### Requires higher authority when triggered

- confirmed identity merge/split;
- destructive replacement/retirement;
- production Schema/contract extension;
- stable governance/spec promotion.

## 5. Batch metrics

For this five-item experiment:

- total candidates: 5;
- proceed through ordinary intake: 2;
- semantic defer: 2;
- duplicate/existing overlap: 1;
- reject/out-of-scope: 0;
- production Canonical writes: 0;
- identity merge/split decisions: 0;
- candidates with at least one unresolved semantic field: 4/5;
- cases where automation can confidently determine the final intake disposition without semantic review: 1/5 (the known duplicate control);
- cases where automation can perform most preflight work but independent review still matters: 4/5.

The high unresolved rate is expected because the batch was intentionally selected for behavioral diversity, not because ordinary intake is necessarily this ambiguous at scale.

## 6. Important findings

### Finding A — `accept`, `defer`, `duplicate`, and `reject` must remain separate

A Candidate can be valid and valuable while still being deferred. Collapsing `defer` into `reject` would destroy useful backlog; collapsing it into `accept` would force guessed semantics.

### Finding B — intake should be partially non-blocking

ISO edition semantics and FAPI profile semantics can defer independently while RFC 9114 and Fetch continue. One novel modeling case must not freeze unrelated ordinary intake.

### Finding C — the first scalable automation target is preflight, not acceptance

Source confirmation, identifier normalization, duplicate search, completeness checks and routing are strong automation candidates. Final semantic acceptance remains evidence/review driven.

### Finding D — ordinary intake needs a minimal-admission rule

The batch exposed a practical P6 question: how much relation/classification detail is required before an otherwise clear subject may enter Canonical? The rule should be minimal enough not to block simple RFC/living-standard intake, but strong enough not to flatten Profile semantics. This should be resolved from #136 evidence before broad intake launch, not by adding fields ad hoc per candidate.

## 7. Dry acceptance path

The two proceed cases were carried through an experiment-only acceptance event shape in:

`03_Evolution/04_Experiments/v1_contract_fixtures/intake-batch1-dry-acceptance.fixture.yaml`

The dry path is:

```text
Candidate Proposal
→ experiment structural validation state
→ executor semantic self-review
→ mutation-impact hypothesis (M1)
→ independent review still pending
→ authority gate not executed
→ simulated acceptance event
→ rollback/correction path
```

Both simulated events deliberately keep:

- `accepted_canonical_id: null`；
- `accepted_at: null`；
- `reviewer: null`；
- `state: simulated_only`。

This prevents experiment data from masquerading as an accepted Canonical mutation.

Rollback semantics are also explicit: before acceptance, discard/revise the Candidate; after a future real acceptance, corrections must be represented as a new Candidate preserving history rather than deleting or rewriting provenance.

## 8. Gate evidence from Batch 1

Batch 1 now demonstrates that a bounded intake can:

- stop a duplicate before new-object creation；
- allow simple candidates to continue while independently deferring harder semantic cases；
- keep `defer` distinct from `reject`；
- keep structural validation distinct from semantic review；
- keep executor self-review distinct from independent review；
- represent acceptance/provenance without actually mutating Canonical；
- preserve rollback/correction semantics；
- identify preflight as the strongest near-term automation surface。

The remaining blocking question for broad ordinary intake is not “can every candidate be fully modeled automatically?” It is narrower: **what is the minimal safe admission contract for ordinary M0/M1 knowledge, and which semantic patterns must automatically defer/escalate?**

## 9. Next checkpoint

Translate Batch 1 findings into a minimal ordinary-intake checklist / decision table suitable for #159/#134 evidence synthesis. Do not build production automation yet. The checklist should separate:

- T0/T1 preflight tasks that can scale now；
- mandatory machine checks；
- mandatory independent semantic review conditions；
- automatic defer/escalate triggers；
- conditions that would make ordinary M0/M1 intake contribution-ready after #134。
