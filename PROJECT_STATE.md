# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T09:11:00+08:00
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
> Verified At: 2026-09-04T09:11:00+08:00
>
> Purpose: 给新的 Human / Agent 一个短小的“现在在哪、为什么、从哪里继续”入口。它不替代 Issue、PR、Git history 或完整 Phase Plan。

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
- Readable Projection ≠ Updatable Projection；有损 / 筛选 / 聚合 View 默认不能直接反写 Canonical；
- Agent Output ≠ Canonical Fact；Agent 默认产生 Candidate Assertion / Proposal / Patch / Evidence；
- Public Knowledge Lifecycle ≠ Personal Attention / Memory Metabolism；
- Human / Agent 共用同一个公共知识底座，但不等于共享无边界写权限；
- Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission；
- 高影响治理、Identity Merge、破坏性迁移和稳定规范升级需要更高授权 / Review Gate。

## 3. Foundation status

```text
Gate A — Repository Structure             ✅ PASS
Gate B — Human Interface                  ✅ PASS
Gate C — Open Collaboration v0.1 Pilot    ✅ PASS
Knowledge Model / Machine Contract         ✅ representative foundation complete
F4 — Curation / Evidence / Correctness     🟡 parallel quality line
```

此前 Reference Implementation 的 Human Route、Search、Compare、Evidence / Assessment presentation、Local Map 等代表性成果保留为已验证资产，但不自动沿旧页面功能路线扩张。

## 4. P1–P3 settled direction

P1 设计原则已接受；P2 prior-art / standards research 没有发现需要推翻 P1 的重大错误；P3 Current-State Audit 已在 **Issue #126（Completed）** 收口。

P3 的正式结论：

> **不推倒重写整个 InteropAtlas，也不继续在 V0 上无限打补丁。保留知识资产、仓库历史、协作体系、迁移基础设施和 Runtime 骨架；P4 建立干净的 Canonical Contract V1 与新的 Workspace / Product Architecture，再逐步迁移。**

完整审计与 Keep / Refactor / Migrate / Rewrite / Retire Matrix：**Issue #126 final synthesis**。

## 5. Current phase and resume point

```text
P1  Design Principles                    ✅ Completed / accepted
        ↓
P2  Prior-art / standards research       ✅ Completed / #124 closed
        ↓
P3  Current-state audit                  ✅ Completed / #126 closed
        ↓
P4  Architecture / Roadmap reset         ← NOW / #127
        ↓
P5  Real-data experiments / intake stress test
        ↓
P6  Implementation + continuous intake
```

### NOW: P4 — Architecture / Roadmap Reset

Primary Work Item: **Issue #127 — P4 Architecture / Roadmap Reset: Canonical Contract V1 → Intake → Migration → Workspace**。

### P4 design order / status

1. **Canonical Contract V1** — `docs/canonical-contract-v1-architecture-draft.zh-CN.md` ✅ draft
2. **Canonical Write / Intake Contract** — `docs/canonical-write-intake-contract-v1-architecture-draft.zh-CN.md` ✅ draft
3. **Migration Architecture** — `docs/canonical-migration-architecture-v1-draft.zh-CN.md` ✅ draft
4. **Selection / Projection / Workspace Architecture** — `docs/selection-projection-workspace-architecture-v1-draft.zh-CN.md` ✅ draft
5. **Human + Agent Access Architecture** — `docs/human-agent-access-architecture-v1-draft.zh-CN.md` ✅ draft
6. **Roadmap Reset** ← NEXT

### Resume Here

Continue **Issue #127 / P4.6 Roadmap Reset**.

P4.5 settled direction:
- Human / Agent share one Canonical knowledge world, but shared knowledge does not imply shared authority;
- access separates Discover/Read, Query/Traverse, Compose/Analyze, Candidate Write, Review/Assess, Canonical Accept/Govern;
- Identity, Capability, Task Authority, Review Authority and Platform Permission are orthogonal;
- GitHub Actor / credential is not actual Executor identity or Owner authority;
- capability is domain-scoped rather than a single contributor level;
- T0–T3 Task Authority and M0–M3 Mutation Impact compose without replacing each other;
- Agent can research/query/generate candidates/validate within authorization, but cannot self-approve high-impact identity/destructive/stable-governance mutations;
- Human contribution also follows evidence/validation/review requirements;
- self-check is not independent review; CI/Validator supplies review evidence but is not automatically a Reviewer;
- delegation should be bounded, explicit and revocable;
- public Human/Agent participation can expand first through Candidate/Evidence/bounded ordinary Patch paths without opening Schema/Governance authority.

Next small checkpoint: convert P4.1–P4.5 into an executable P5 real-data experiment/intake stress-test plan and P6 implementation order; reconcile existing parallel Issues/PRs into keep/resequence/migrate/pause/retire buckets without automatically absorbing or closing them.

## 6. P4 guardrails

P4 不应自动执行 destructive Schema migration、全量 Canonical rewrite、全量 Relation rich-model migration、frontend rewrite、opaque personalization、stable spec promotion、大规模删除或 complex permission automation。

## 7. Recent stable milestones

- #89–#93 lifecycle / provenance historical backfill ✅；
- PR #123 Knowledge Workspace Design Principles v1.0 merged / Human Maintainer accepted ✅；
- Research Governance v0.1 established ✅；
- #124 P2 Prior-Art / Standards Research completed ✅；
- Standards Candidate Pool v0.1 established ✅；
- #126 P3 Current-State Audit completed ✅；
- #127 P4 Primary Work Item established ✅；
- P4.1 Canonical Contract V1 architecture draft ✅；
- P4.2 Canonical Write / Intake architecture draft ✅；
- P4.3 Canonical Migration architecture draft ✅；
- P4.4 Selection / Projection / Workspace architecture draft ✅；
- P4.5 Human + Agent Access architecture draft ✅。

## 8. Known open / parallel work

Do not automatically absorb/close before P4.6 reconciliation:
- #122 — Knowledge Workspace / Perspective long-term anchor；
- #125 — Candidate Pool historical entry / acceleration work item；
- PR #26 — Open Collaboration v0.2；
- PR #30 — Fit Test Batch 1；
- Issue #15 — wider Schema / Validator / migration debt；
- Issue #86 — Agent Continuity takeover validation；
- F4 Machine / Curation / Evidence quality line；
- `docs/task-authority-governance-v0.1-draft.zh-CN.md` — governance input, not yet stable policy。

## 9. Where to read next

```text
Issue #127
→ docs/canonical-contract-v1-architecture-draft.zh-CN.md
→ docs/canonical-write-intake-contract-v1-architecture-draft.zh-CN.md
→ docs/canonical-migration-architecture-v1-draft.zh-CN.md
→ docs/selection-projection-workspace-architecture-v1-draft.zh-CN.md
→ docs/human-agent-access-architecture-v1-draft.zh-CN.md
→ P4.6 Roadmap Reset
```

## 10. Staleness check

新 Agent 在继续前必须检查 `Verified At` 后 main / #127 / #122 是否出现改变主线的新决策，并确认 Research / Task Governance 是否已有更高版本。不要根据旧 Reference Implementation Phase 恢复页面功能扩张路线。
