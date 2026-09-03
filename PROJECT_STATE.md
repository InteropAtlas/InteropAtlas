# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-04T05:49:28+08:00
Metadata Backfilled At: 2026-09-02T11:45:00+08:00
Metadata Provenance: mixed
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
> Verified At: 2026-09-04T05:49:28+08:00
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

P3 认为值得保留：
- Canonical knowledge content / stable IDs / sources / provenance history；
- Relation 作为一等知识资产；
- semantic normalization / migration layer；
- Machine Review / Graph checks / CI skeleton；
- Generated View ≠ Canonical boundary；
- Human-first, agent-compatible collaboration；
- Search / Compare / Local Graph 已验证的交互原则。

P3 认为需要 P4 重建或补齐：
- Canonical Contract V1；
- external identifier semantics；
- Lifecycle dimensions；
- Source / Evidence / Assertion / Assessment / Provenance 边界；
- binary Relation 的通用上限与 richer participants / roles 能力；
- Candidate Assertion / Proposal / Patch → Review → Canonical mutation 写入边界；
- Human Workspace / Product information architecture；
- Legacy compatibility 的明确退役终点。

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

P4 的任务不是立即迁移数据或重写前端，而是把 P1/P2 原则与 P3 真实审计结果合并成一套明确的 V1 架构和新的执行路线。

Long-term Owner intent anchor: **Issue #122**。

P3 factual input: **Issue #126 final synthesis**。

### P4 recommended design order

1. **Canonical Contract V1**
   - Identity / external identifiers；
   - Object family / kind hierarchy；
   - Relation / participants / roles boundary；
   - Evidence / Assertion / Assessment / Provenance；
   - Lifecycle dimensions。

2. **Canonical Write / Intake Contract**
   - Candidate Assertion / Proposal / Patch；
   - Evidence requirements；
   - review / authority gates；
   - competing assertions / conflict preservation。

3. **Migration Architecture**
   - Legacy → V1 mapping；
   - stable ID preservation；
   - compatibility retirement plan；
   - batch migration / validation strategy。

4. **Selection / Projection / Workspace Architecture**
   - Search / Browse / Compare / Graph / Evidence / Timeline；
   - explicit scope / filter / selection reasons；
   - readable projection vs updatable projection。

5. **Human + Agent Access Architecture**
   - shared Canonical substrate；
   - different interaction surfaces；
   - no hidden Agent truth；
   - no unrestricted write equivalence。

6. **Roadmap Reset**
   - classify old #118/#119 and earlier implementation work；
   - determine what moves to P5 experiments vs P6 implementation。

### Resume Here

Continue **Issue #127 / P4.1 Canonical Contract V1 architecture**.

Checkpoint A has established five semantic contract surfaces: Identity; Entity/Object; Relation/Association; Knowledge Claim/Evidence; Lifecycle/State. It also recorded the current architectural direction of a stable Canonical Core plus explicit composable semantic contracts/profiles rather than continuing to grow one universal Object schema.

Next small checkpoint: **Identity Contract + Object family / kind boundary**. Define identity levels, external-identifier and merge boundaries, then the minimal responsibilities of family/kind classification. Do not write the final field-level Schema yet and do not migrate data.

## 6. P4 guardrails

P4 不应自动执行：
- destructive Schema migration；
- 全量 Canonical data rewrite；
- 全量 Relation → N-ary / Hypergraph migration；
- wholesale frontend / renderer rewrite；
- opaque personalization / recommendation ranking；
- stable Specification promotion；
- 大规模删除；
- complex permission / governance automation。

P4 首先做 Architecture / Decision / Roadmap。需要真实数据验证的设计进入 P5，而不是在 P4 直接固化。

## 7. Recent stable milestones

- #89–#93 lifecycle / provenance historical backfill ✅；
- PR #123 Knowledge Workspace Design Principles v1.0 merged / Human Maintainer accepted ✅；
- Research Governance v0.1 established ✅；
- #124 P2 Prior-Art / Standards Research completed ✅；
- Standards Candidate Pool v0.1 established ✅；
- #126 P3 Current-State Audit completed ✅；
- P3 conclusion: **V1 architecture + asset migration, not whole-project rewrite** ✅；
- #127 P4 Primary Work Item established; Canonical Contract V1 architecture Checkpoint A recorded ✅。

## 8. Known open / parallel work

不要自动吞并：
- #122 — Knowledge Workspace / Perspective long-term anchor；
- #125 — Candidate Pool 历史入口 / acceleration work item；
- PR #26 — Open Collaboration v0.2；
- PR #30 — Fit Test Batch 1；
- Issue #15 — wider Schema / Validator / migration debt；
- Issue #86 — Agent Continuity takeover validation；
- F4 Machine / Curation / Evidence quality line；
- `docs/task-authority-governance-v0.1-draft.zh-CN.md` — P4 governance input, not yet stable policy。

## 9. Where to read next

第一次理解项目：

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ docs/interopatlas-definition-and-scope-v0.2.zh-CN.md
→ docs/knowledge-workspace-design-principles-v1.0.zh-CN.md
→ 03_Evolution/03_Change/knowledge-workspace-phase-plan-v1.0.zh-CN.md
```

继续当前主线：

```text
Issue #122 Owner intent
→ Issue #124 final P2 synthesis
→ Issue #126 final P3 synthesis
→ Issue #127 P4 Primary Work Item
→ P4.1 Canonical Contract V1 architecture
→ Canonical Write / Intake Contract
→ Migration Architecture
→ Workspace / Human+Agent Architecture
→ Roadmap Reset
```

## 10. Staleness check

新 Agent 在继续前必须检查：
1. `Verified At` 之后 main 是否有改变 Phase / main line 的提交；
2. #127 是否有新的 architecture checkpoint / decision artifact；
3. #122 是否有新的 Human Owner 意图；
4. #126 后是否出现改变 P3 结论的新证据；
5. Research Governance / Task Governance 是否已有更高版本。

不要根据旧 Reference Implementation Phase、旧 P2/P3 `NOW` 或 #118/#119 自动恢复页面功能扩张路线。
