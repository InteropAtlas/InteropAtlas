# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T12:00:00+08:00
Metadata Backfilled At: 2026-09-02T11:45:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-04T12:00:00+08:00
>
> Purpose: 给新的 Human / Agent 一个短小的“现在在哪、为什么、从哪里继续”入口。它不替代 Issue、PR、Git history 或完整 Roadmap。

## 1. Project in one sentence

InteropAtlas 是一个开放、机器可读、可持续分析的 **Interoperability Solution Space（互操作方案空间）** 知识基础设施，用来连接标准、成熟先例、方法、实现、组织、能力、场景、关系、证据与开放缺口，并服务 Human 与 Agent 的发现、比较、组合、验证和改进。

完整定义：`docs/interopatlas-definition-and-scope-v0.2.zh-CN.md`。

## 2. Core invariants

- `Adopt → Profile → Extend → Invent`；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- Physical Storage ≠ Semantic Classification ≠ Index / View；
- Stable Identity 不能依赖文件路径或显示名称；
- Canonical State ≠ Generated View；
- Search / Compare / Map / Timeline / Wiki 等是 View / Projection / Workspace，不是新的 Canonical Fact 来源；
- Readable Projection ≠ Updatable Projection；
- Agent Output ≠ Canonical Fact；
- Public Knowledge Lifecycle ≠ Personal Attention / Memory Metabolism；
- Human / Agent 共用同一个公共知识底座，但不等于共享无边界写权限；
- Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission；
- 高影响治理、Identity Merge、破坏性迁移和稳定规范升级需要更高授权 / Review Gate。

## 3. Foundation status

```text
Gate A — Repository Structure             ✅ PASS
Gate B — Human Interface                  ✅ PASS
Gate C — Open Collaboration v0.1 Pilot    ✅ PASS
Knowledge Model / Machine Contract         ✅ representative V0 foundation
F4 — Curation / Evidence / Correctness     🟡 parallel quality line
```

此前 Reference Implementation 的 Human Route、Search、Compare、Evidence / Assessment presentation、Local Map 等代表性成果保留为已验证资产，但不自动沿旧页面功能路线扩张。

## 4. P1–P4 status

```text
P1  Design Principles                    ✅ Completed / accepted
P2  Prior-art / standards research       ✅ Completed / #124 closed
P3  Current-state audit                  ✅ Completed / #126 closed
P4  Architecture / Roadmap reset         ✅ Completed / #127 closed
P5  Real-data experiments / intake stress test ← NOW / #128
P6  Implementation + continuous intake   Future / #129
```

## 5. P4 outputs

1. `docs/canonical-contract-v1-architecture-draft.zh-CN.md` ✅
2. `docs/canonical-write-intake-contract-v1-architecture-draft.zh-CN.md` ✅
3. `docs/canonical-migration-architecture-v1-draft.zh-CN.md` ✅
4. `docs/selection-projection-workspace-architecture-v1-draft.zh-CN.md` ✅
5. `docs/human-agent-access-architecture-v1-draft.zh-CN.md` ✅
6. `docs/p1-p6-roadmap-reset-v1-draft.zh-CN.md` ✅

These remain architecture/roadmap drafts. P4 completion does not stable-promote them or authorize destructive migration / broad Canonical writes.

## 6. NOW — P5 Real-data Experiments / Intake Stress Test

Primary umbrella: **#128**。
Mainline index: **#193**。

Critical path:

```text
#137 Experiment Harness / V1-shaped fixtures          ✅ first usable harness / Review
→ #130 Identity / Version / Family-Kind Fit Test      ✅ fit test complete / Review
→ #132 Relation + Evidence/Assertion/Conflict + Lifecycle Fit Test ✅ fit test complete / Review
→ #133 Migration + Workspace + Human/Agent Write-back E2E ✅ representative E2E complete / Review
→ #136 Candidate→Canonical bounded Intake Stress Test ✅ Batch 1 complete / Review
→ #159 Gate Evidence Synthesis ← NOW
→ #134 Contribution-Ready Owner/Governance Gate
```

#136 Batch 1 selected five deliberately diverse candidates and exercised source confirmation, dedup, Candidate Proposal, semantic disposition and dry acceptance/provenance paths. Experimental outcomes:

```text
RFC 9114                 → proceed ordinary intake
Fetch Living Standard    → proceed with lifecycle/freshness boundary
ISO/IEC 27001:2022       → defer semantic model decision
FAPI 2.0 Security Profile→ defer profile/base/framework semantics
BCP 47 / RFC 5646        → duplicate/existing overlap
```

No production Canonical mutation occurred. Batch 1 confirmed `accept / defer / duplicate / reject` must remain separate, and that scalable automation should focus first on preflight rather than semantic acceptance.

Durable gate input: `docs/p5-ordinary-intake-minimal-checklist-v1-draft.zh-CN.md`.

### Resume Here

**Primary next small checkpoint: #159 — synthesize Gate evidence from #137/#130/#132/#133/#136 into a concise PASS / PASS-WITH-BOUNDARIES / FAIL recommendation for #134. Do not ask Owner to decide implementation details. Explicitly separate architecture validity, bounded-intake validity, and production-readiness gaps.**

The synthesis should answer:
- which P4 contracts survived real data without reversal;
- which ordinary M0/M1 intake steps are repeatable;
- which checks can scale as T0/T1 preflight;
- what must still defer/escalate;
- which implementation gaps remain before broad continuous Canonical intake;
- whether #134 should authorize P6 ordinary intake now, authorize with boundaries, or hold.

## 7. When standard intake can scale

- **Now / P5:** Candidate discovery/source confirmation/dedup can scale in parallel through #125/#131/#140–#165. Candidate ≠ Canonical.
- **#136 result:** bounded intake semantics are viable; ordinary preflight is highly parallelizable, but actual Canonical acceptance still requires production validator/review-routing/acceptance-event implementation.
- **After #134 PASS / PASS WITH BOUNDARIES:** broad ordinary M0/M1 continuous Canonical intake may begin in early P6 through #145 → #146, with explicit escalation of ambiguous/high-impact cases.
- M2/M3 identity/destructive/governance/stable changes retain higher gates.

## 8. P5 parallel work

Fast Lane index: **#192**。

Allowed before Contribution-Ready Gate:
- Candidate discovery / source confirmation / dedup；
- evidence-gap discovery；
- relation/lifecycle/identity/migration inventories；
- Workspace current-asset audit；
- machine/graph baseline；
- experiment fixtures；
- continuity/task-readability validation；
- bounded non-destructive research。

Not allowed through fast lane: mass Canonical write, identity merge/split, production Schema migration, stable governance promotion, destructive deletion, unrestricted Agent acceptance.

## 9. P6 preview

P6 umbrella: **#129**; index: **#194**。

First production chain after Gate:

```text
#145 V1 Serialization / Validator minimal production loop
├→ #146 Continuous Intake
├→ #147 Migration Cohort 1
├→ #148 Compare + Evidence Workspace
└→ #149 Agent structured read/query + Candidate Write
```

A likely #134 boundary is that broad ordinary intake may be authorized conceptually but must still begin through #145 production serialization/validator before mass Canonical writes are actually enabled.

## 10. Legacy / parallel work

- #122 — long-term Owner intent anchor: retain；
- #125 — Candidate Pool historical entry / accelerator: retain and activate in parallel；
- #135 / #195 — legacy backlog reclassification / cleanup proposal；
- PR #26 / #24 — Open Collaboration v0.2: retain pending P4.5 reconciliation；
- PR #30 / #15 / #23 — retain as P5 non-normative Fit Test evidence；
- #86 / #138 — Agent continuity validation；
- F4 quality line remains parallel；
- `docs/task-authority-governance-v0.1-draft.zh-CN.md` remains governance input, not stable policy。

Do not mass-close old Issues merely because the roadmap reset exists.

## 11. Owner gates

Ordinary P5 experiments/discovery proceed autonomously. Explicit Owner/Governance decision is required for:
- #134 broad Contribution-Ready activation；
- identity merge/split or destructive migration where authority requires；
- material security/permission governance changes；
- stable specification/governance promotion；
- V1-only writer / Legacy retirement gates；
- material project definition/scope changes。

## 12. Where to read next

```text
AGENTS.md
→ PROJECT_STATE.md
→ #159
→ #134
→ docs/p5-ordinary-intake-minimal-checklist-v1-draft.zh-CN.md
→ #137/#130/#132/#133/#136 evidence as needed
→ docs/p1-p6-roadmap-reset-v1-draft.zh-CN.md
```

## 13. Staleness check

新 Agent 在继续前只需检查 `Verified At` 后 main / #128 / #159 / #134 / #122 是否出现改变主线的新决策，并确认 Research / Task Governance 是否已有更高版本。不要根据 superseded historical phase plan 恢复旧路线。
