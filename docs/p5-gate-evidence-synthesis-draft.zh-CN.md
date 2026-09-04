# P5 Gate Evidence Synthesis v1 — Draft

> Status: P5 Gate Evidence Draft
>
> Work Item: #159
>
> Checked At: 2026-09-04
>
> Recommended #134 decision: **PASS WITH BOUNDARIES**

## 1. Executive conclusion

P5 representative experiments did **not** find a reason to reverse the P4 Canonical / Intake / Migration / Projection / Human+Agent architecture.

The evidence is strong enough to say:

- the semantic architecture is valid enough to enter P6 implementation；
- bounded Candidate→Intake semantics are viable；
- ordinary M0/M1 preflight can scale to many Human/Agent contributors；
- broad continuous **production Canonical acceptance is not yet implementation-ready today** because production V1 serialization/validator, review routing, acceptance-event implementation, durable Candidate carrier and full repository-level validation are still incomplete。

Therefore the recommended #134 decision is:

> **PASS WITH BOUNDARIES** — authorize P6 implementation and preparation for broad ordinary M0/M1 intake, while keeping actual mass Canonical writes behind the P6 production implementation gates. Candidate discovery and preflight may scale immediately. Ambiguous/high-impact cases continue to defer/escalate.

This is not a HOLD: the remaining gaps are implementation/operational boundaries, not evidence of an architecture failure.

## 2. Architecture validity

### #130 — Identity / Version / Family-Kind

**Result: PASS / no architecture reversal.**

Real publication models tested included immutable RFCs, editioned ISO/IEC standards, W3C Recommendations, Living Standards, final-with-errata specifications and profiles.

Confirmed boundaries:

- IA stable identity is independent of URL/title/publisher identifier；
- publisher identifiers require namespaces；
- locator role and identity are different；
- higher version does not automatically mean supersedes；
- publication revision does not always imply a new Canonical subject；
- Family/Kind is orthogonal to identity；
- Profile semantics cannot be safely modeled as taxonomy alone in all cases。

Remaining questions such as exact work-vs-edition serialization are isolated and can defer individual candidates.

### #132 — Relation / Evidence / Conflict / Lifecycle

**Result: PASS / no architecture reversal.**

Confirmed:

- binary Relation remains valid as a fast path；
- rich Association is needed only when participant roles/structure demand it；
- qualifier/context complexity alone does not require N-ary promotion；
- Source / Evidence / Assertion / Assessment / Provenance must remain distinguishable；
- conflict/unverified/unknown states must be explicit；
- lifecycle is multidimensional, not one universal `status`。

Critical real-data finding: a machine predicate can be more certain than Human-readable notes. Therefore V1 needs a way to preserve approximation/semantic-gap states rather than silently expose an approximate predicate as exact fact.

### #133 — Migration / Projection / Workspace / Write-back

**Result: PASS / no architecture reversal.**

A/B/C/D Legacy mapping classes were exercised through V1-shaped dry-run state, Compare/Evidence/Timeline/Graph projections and a correction→Candidate Patch loop.

Confirmed:

- stable IDs are preserved by default；
- ambiguous migration is allowed to stop as unresolved；
- Projection may be lossy, but omission ≠ Canonical absence；
- Readable Projection ≠ Updatable Projection；
- Agent generated interpretation remains derived state；
- corrections discovered in Workspace must return through Candidate Write/Intake；
- GitHub Actor and actual Agent Executor remain distinct；
- self-check is not independent review。

No second hidden write path is needed.

## 3. Bounded-intake validity

### #136 Batch 1

**Result: PASS at experiment/contract level.**

Five deliberately diverse candidates produced four distinct intake outcomes:

| Candidate | Outcome |
| --- | --- |
| RFC 9114 | proceed ordinary intake |
| Fetch Living Standard | proceed with lifecycle/freshness boundary |
| ISO/IEC 27001:2022 | defer semantic model decision |
| FAPI 2.0 Security Profile | defer profile/base/framework decision |
| BCP 47 / RFC 5646 | duplicate/existing overlap |

Confirmed:

- `accept / defer / duplicate / reject` must remain distinct；
- hard cases can defer without blocking unrelated ordinary intake；
- duplicate detection is a normal successful intake disposition；
- Candidate state can carry provenance and review state without masquerading as Canonical；
- dry acceptance/rollback can be represented without performing a production mutation；
- preflight is a strong automation target；
- semantic acceptance remains review-driven。

## 4. What can scale now as T0/T1

The following can be broadly parallelized before broad Canonical acceptance is enabled:

1. Candidate discovery；
2. official first-party source confirmation；
3. publisher/title/known identifier capture；
4. external identifier normalization；
5. Candidate + Canonical dedup preflight；
6. source checked-at capture；
7. publication-pattern flagging (immutable / editioned / living / profile / other)；
8. obvious uncertainty recording；
9. evidence-gap discovery；
10. provenance carrier creation；
11. obvious duplicate routing；
12. machine-readable fixture/preflight generation；
13. automatic flagging of edition/profile/amendment/identity-risk patterns for semantic review。

These activities produce Candidate / Evidence / Preflight state, not accepted Canonical fact.

## 5. What must remain semantic-review gated

Independent semantic review remains required for actual ordinary Canonical acceptance, especially for:

- work/family vs edition/version identity；
- merge/split/equivalence；
- Profile/base/framework relation minimum；
- relation assertions with scope/context；
- classification that could create false precision；
- evidence sufficiency for nontrivial claims；
- conflict/unknown interpretation；
- mutation-impact classification when semantics change materially。

Agent self-review cannot substitute for independent review.

## 6. Automatic defer / higher-gate triggers

Ordinary intake must automatically stop/escalate when it encounters:

- identity merge/split/equivalence；
- composite identity that cannot be represented without guessing；
- edition/work ambiguity that changes subject identity；
- Profile semantics that would be flattened without required relations；
- approximate predicate known to misstate semantics；
- required rich Association/participant roles；
- authoritative source conflict；
- insufficient evidence for a claimed fact；
- destructive replacement/retirement；
- production contract/schema extension；
- M2/M3 mutation；
- security/permission governance or stable specification promotion。

These triggers are not failures of ordinary intake; they are routing conditions.

## 7. Production-readiness gaps

These are the main reasons the recommendation is **PASS WITH BOUNDARIES**, not unconditional PASS:

### Gap A — production V1 serialization / validator

P5 fixtures validate architecture/experiment envelopes, not a final production Canonical representation. #145 remains necessary before mass production writes.

### Gap B — full repository machine/relation/graph validation

The current execution environment did not provide reliable fresh checkout-level Machine Review / Graph execution for all new P5 experiment artifacts. No false production PASS is claimed.

### Gap C — review routing / independence

The semantic requirement is clear, but a concrete production route for assigning/recording an independent Reviewer still needs implementation and operational proof.

### Gap D — acceptance event implementation

P5 tested an acceptance-event shape, but production code/data paths that write accepted Canonical state with reviewer/authority provenance are not yet implemented.

### Gap E — normalized dedup mechanism

Repository search is sufficient for preflight examples but not a scalable definitive negative dedup guarantee. Identifier/alias indexing needs a production path as scale grows.

### Gap F — Candidate Pool carrier

Discovery Issues exist, but durable Candidate records are not yet materially populated at scale. A consumable Candidate carrier is needed for continuous intake throughput.

These gaps are P6 implementation work. None currently requires reopening P4 architecture.

## 8. Recommended #134 authorization

### Authorize

If Owner/Governance accepts **PASS WITH BOUNDARIES**, authorize:

- P5 architecture/contract direction as sufficient to enter P6 implementation；
- #145 production V1 serialization/validator slice；
- #146 continuous ordinary intake implementation after #145 minimum gate is usable；
- #147 bounded migration cohort；
- #148 Compare + Evidence Workspace slice；
- #149 Agent structured read/query + Candidate Write slice；
- continued large-scale Candidate discovery / source confirmation / dedup；
- broad Human/Agent participation in T0/T1 preflight tasks；
- ordinary M0/M1 intake only once production machine checks + independent review + acceptance-event path are active。

### Do not authorize

#134 should **not** authorize:

- mass direct Canonical writes immediately on the current P5 fixture model；
- unrestricted Agent acceptance；
- identity merge/split automation；
- M2/M3 automatic acceptance；
- destructive migration / Legacy retirement；
- stable promotion of all P4 drafts by implication；
- bypassing independent review because the GitHub Actor is the Owner；
- treating Candidate count as Canonical coverage。

## 9. Gate matrix

| Gate question | Evidence | Result |
| --- | --- | --- |
| Canonical identity/version model survives real standards | #130 | PASS |
| Relation common/rich paths survive real data | #132 | PASS |
| Evidence/conflict/lifecycle semantics survive real data | #132 | PASS |
| Migration ambiguity can be preserved safely | #133 | PASS |
| Projection/workspace does not corrupt Canonical | #133 | PASS |
| Agent output/write-back remains gated | #133 | PASS |
| Candidate→Intake decisions are repeatable | #136 | PASS WITH BOUNDARIES |
| T0/T1 preflight can scale | #136 + minimal checklist | PASS |
| Production V1 validator is ready | P5 evidence | NOT YET — P6 #145 |
| Independent review routing is operational | P5 evidence | NOT YET — implementation gap |
| Broad production Canonical intake can start immediately | P5 evidence | NO |
| P6 implementation can start | combined evidence | YES |

## 10. Final recommendation

**Recommended #134 decision: PASS WITH BOUNDARIES.**

Interpretation:

> InteropAtlas is contribution-ready at the Candidate/preflight and architecture-to-implementation level. It is not yet safe to switch on unrestricted or mass production Canonical intake. Owner approval should release the P6 implementation chain that makes ordinary M0/M1 intake production-ready, while preserving defer/escalate gates for ambiguous and high-impact cases.

This preserves speed without pretending that experiment fixtures are already production infrastructure.
