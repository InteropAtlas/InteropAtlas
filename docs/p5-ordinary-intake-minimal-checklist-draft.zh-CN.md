# P5 Ordinary Intake Minimal Checklist v1 — Draft

> Status: P5 Gate Evidence Draft
>
> Inputs: #136 Batch 1, P4.2 Write/Intake, P4.5 Human+Agent Access
>
> Purpose: 把首批真实 Candidate 压力测试转成 ordinary M0/M1 intake 的最小可重复决策表。本文不是 stable governance policy，也不授权 broad Canonical intake。

## 1. Principle

Ordinary intake 不要求“所有语义都已最终建模”，但必须满足：

> **已知事实足够明确；关键不确定性不被隐藏；高风险语义能自动 defer/escalate；Candidate / Review / Acceptance 边界可追溯。**

目标不是让机器自动接受所有对象，而是让大量低风险 preflight 与普通知识收入可以被安全并行化。

## 2. Intake stages

```text
Candidate Discovery
→ Source Confirmation
→ Identifier / Dedup Preflight
→ Candidate Proposal
→ Machine Checks
→ Semantic Review
→ Defer / Reject / Duplicate / Accept Decision
→ Authority Gate when required
→ Canonical Acceptance Event
→ Revalidation / Correction
```

## 3. T0/T1 preflight — scalable before broad Canonical intake

可由 Human / Agent 大规模执行：

- [ ] official first-party source identified；
- [ ] title / publisher / known identifier captured；
- [ ] source checked-at recorded separately from verification time；
- [ ] normalized external identifier extracted where available；
- [ ] basic Candidate + Canonical dedup search performed；
- [ ] possible duplicate / existing overlap explicitly recorded；
- [ ] publication pattern flagged: immutable / editioned / living / profile / other；
- [ ] obvious uncertainty recorded instead of guessed；
- [ ] Initiator / Executor / GitHub Actor provenance slots preserved；
- [ ] output remains Candidate, not Canonical Fact。

These tasks can scale independently of final acceptance authority.

## 4. Mandatory machine checks before ordinary acceptance

Minimum machine gate SHOULD cover:

- parse / schema-envelope validity；
- required identity/source fields；
- normalized identifier syntax；
- reference resolution where references are asserted；
- duplicate candidate warnings；
- relation endpoint integrity for submitted relations；
- controlled vocabulary/invariant checks where contract is already settled；
- provenance carrier completeness；
- explicit Candidate state vs Canonical state；
- no hidden direct-write path from generated/projection state。

Machine PASS does not establish factual truth or semantic adequacy.

## 5. Independent semantic review — mandatory conditions

Independent semantic review is required before actual ordinary Canonical acceptance when any knowledge assertion is added or changed. Reviewer checks at minimum:

- [ ] official source actually supports the proposed subject/fact；
- [ ] identity is not being inferred solely from URL/title；
- [ ] known identifier/alias collision has been reasonably checked；
- [ ] family/kind/classification does not invent false precision；
- [ ] relation assertions preserve scope/context；
- [ ] unknown / unverified / disputed state is not flattened；
- [ ] publication lifecycle is separate from IA verification/record lifecycle；
- [ ] evidence/provenance are recoverable；
- [ ] mutation impact has not been underestimated。

Agent executor self-review may satisfy a self-check step but does not count as independent review.

## 6. Automatic defer / escalate triggers

The intake path MUST stop ordinary acceptance and route to `defer` or higher review when any of the following appears:

### Identity / publication
- possible merge/split/equivalence；
- work/family vs edition/version boundary materially changes Canonical subject identity；
- composite identity cannot be represented without guessing；
- title/URL similarity is the main identity evidence。

### Relation / semantics
- Profile/base/framework meaning would be lost without unresolved relation modeling；
- Legacy/available predicate is known to be only an approximation；
- ≥3 participants or participant roles are required to preserve meaning；
- relation vocabulary extension is necessary for truthful representation。

### Evidence / conflict
- authoritative sources materially conflict；
- evidence is insufficient for a proposed assertion；
- assessment is being confused with fact；
- scope/context cannot be represented without misleading simplification。

### Lifecycle / migration
- amendment/errata/supersession semantics alter identity or historical meaning；
- destructive replacement, deletion or retirement is implied；
- production contract/schema extension is required。

### Governance
- M2/M3 mutation；
- stable specification/governance promotion；
- security/permission model change。

`defer` means “valid Candidate waiting for bounded decision”, not reject.

## 7. Ordinary M0/M1 contribution-ready conditions

A future #134 PASS / PASS WITH BOUNDARIES can authorize broad ordinary intake only if the operational implementation can reliably enforce:

1. Candidate/Canonical separation；
2. first-party source + provenance capture；
3. normalized identifier/dedup preflight；
4. minimum machine validation；
5. independent semantic review；
6. explicit `accept / defer / duplicate / reject` outcomes；
7. automatic escalation of identity/model/high-impact cases；
8. acceptance event with reviewer/approver provenance；
9. correction/revalidation path preserving history；
10. no Agent credential or GitHub permission bypasses semantic/authority gates。

## 8. Batch 1 evidence mapping

| Rule | Real sample evidence |
| --- | --- |
| simple immutable publication can proceed | RFC 9114 |
| living subject can proceed if clocks stay separate | Fetch Living Standard |
| edition/work ambiguity must defer | ISO/IEC 27001:2022 |
| Profile semantics can force defer | FAPI 2.0 Security Profile |
| duplicate is normal intake disposition | BCP 47 / RFC 5646 |

This five-sample batch is intentionally high-diversity and is not a throughput benchmark.

## 9. Remaining gaps before Gate synthesis

The architecture direction is stable enough for #159 evidence synthesis, but production readiness still depends on implementation evidence for:

- normalized Candidate/Canonical dedup mechanism；
- production V1 serialization + validator slice；
- concrete review routing / reviewer independence；
- machine relation/reference/graph checks on the production representation；
- explicit ordinary acceptance event implementation；
- Candidate Pool carrier that is actually populated and consumable at scale。

These gaps should become Gate boundaries, not reasons to reopen broad architecture research.
