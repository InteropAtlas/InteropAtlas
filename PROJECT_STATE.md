# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-03T18:07:00+08:00
Metadata Backfilled At: 2026-09-02T11:45:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> Status: Living Project Checkpoint（持续更新的项目断点）
>
> Verified At: 2026-09-03T18:07:00+08:00
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
- Private Chat 不是项目状态；
- Human / Agent 必须共享可公开恢复的项目状态；
- 高影响治理、破坏性迁移和稳定规范升级需要 Human Maintainer 明确授权。

## 3. Foundation status

```text
Gate A — Repository Structure             ✅ PASS
Gate B — Human Interface                  ✅ PASS
Gate C — Open Collaboration v0.1 Pilot    ✅ PASS
Knowledge Model / Machine Contract         ✅ representative foundation complete
F4 — Curation / Evidence / Correctness     🟡 parallel quality line
```

此前 Reference Implementation 已落地 Permanent Human Route、Search v0.1、dedicated Compare、Evidence / Assessment presentation、Homepage task entry 等代表性切片。这些成果保留，但不再自动按旧页面功能路线继续扩张。

## 4. Current design baseline

Human Maintainer 已确认 Knowledge Workspace / Perspective 方向为新的项目级设计基线。

当前设计原则：`docs/knowledge-workspace-design-principles-v1.0.zh-CN.md`。

当前 Phase Plan：`03_Evolution/03_Change/knowledge-workspace-phase-plan-v1.0.zh-CN.md`。

核心方向：

```text
Canonical Knowledge
        ↓
Selection / Perspective
        ↓
Projection
        ↓
Representation / Workspace
        ↓
Human / Agent Interaction
```

- **Knowledge is stable; representations are fluid.**
- Wiki / Browse 是长期必需的基础 Workspace，但不是唯一形式；
- 同一 Canonical Knowledge 可以支持 Timeline / Graph / Compare / Article 等不同 Workspace；
- Human 与 Agent 使用同一 Canonical Knowledge，而不是两套事实世界；
- Representation 可以有损，但不能反向覆盖 richer Canonical Knowledge；
- Perspective / Projection / Workspace 仍是待 P2/P5 验证的概念边界，不是稳定 Schema。

## 5. Current phase and resume point

```text
P1  Design Principles                    ✅ Human Maintainer accepted
        ↓
P2  Prior-art / standards research       ← NOW
        ↓
P3  Current-state audit
        ↓
P4  Architecture / Roadmap reset
        ↓
P5  Small real-data experiments
        ↓
P6  Resume implementation
```

### NOW: P2 — Prior-Art Map / Standards & Research Landscape

Primary Work Item: **Issue #124**.

Long-term direction / Owner intent anchor: **Issue #122**.

P2 目标不是堆参考资料，而是形成 `InteropAtlas Prior-Art Map v0.1`，对主要问题分别判断：

`Adopt / Profile / Extend / Invent`。

P2 当前一级研究主题：
- Knowledge Modeling：Topic Maps、RDF / Linked Data / JSON-LD、Property Graph、Hypergraph、N-ary Relation、Identity、Scope / Context、Provenance；
- Selection / Attention：IR / Relevance、Faceted Navigation、Dynamic / Saved / Standing / Continuous Query、Focus+Context、OmniFocus Perspective；
- **Knowledge Lifecycle / Metabolism**：Active / Warm / Cold、freshness / staleness、superseded / deprecated / archive、decay / down-ranking、compaction、deletion、reactivation；
- Projection / Representation：Multiple Coordinated Views、representation transformation、information loss、transformation invariants；
- Productization：Capacities、Tana、Heptabase、Notion、Obsidian Bases、Logseq、Roam、Anytype、OmniFocus 等；
- Human + Agent：共享 Canonical Knowledge、可解释 selection、Agent 操作 Perspective / Workspace。

`Knowledge Metabolism` 目前是研究术语，不是稳定架构。P2 必须特别区分 Validity、Freshness、Usage、Relevance、Historical Value、Authority 与 Lifecycle，避免把它们压缩为一个永久 weight。

## 6. Current stop conditions

在 P2/P3 证据不足前，不自动执行：
- destructive Schema migration；
- 把 Perspective 或 Knowledge Metabolism 设为 mandatory Canonical type；
- 全量 Relation → N-ary / Hypergraph 迁移；
- wholesale frontend / renderer rewrite；
- opaque personalization / recommendation ranking；
- stable Specification promotion；
- 大规模数据删除；
- Ruleset / Branch Protection / Governance Automation。

已有 #118/#119 等旧页面功能工作**不要机械恢复**。P3 应判断其属于 Fits / Temporary View / Premature Constraint / Missing Capability / Research Needed，再决定继续、降级或暂停。

## 7. P3 preloaded audit questions

P3 至少检查：
- Object Identity 是否稳定、可合并、可去重；
- Source / Resource 是否与 Object / Subject 清晰分离；
- Relation 是否被二元边先验限制，是否有真实 facts 需要 participants + roles；
- Scope / Context 是否缺失并已造成语义错误；
- Evidence 与 Provenance 是否混用；
- Generated View 是否可能污染 Canonical State；
- 当前 Search / Compare / Graph / Browse 是否只是 Projection，还是已经偷偷固化数据模型假设；
- 当前 IA 是否默认所有知识永久 active / equal-weight；
- superseded / legacy knowledge 如何降权但保留可恢复性；
- 被综合吸收后的 Research Materials 哪些必须保留、哪些可归档/压缩/淘汰；
- knowledge reactivation 应由 query / context / time / history 中哪些信号触发。

## 8. Recent stable milestones

- #89–#93 lifecycle / provenance historical backfill ✅；
- PR #98 merged；
- #101 / PR #102 Permanent Human Route ✅；
- #103 / PR #104 Search v0.1 ✅；
- #105 / PR #106 First Compare UI ✅；
- #107 / PR #109 Human Route shell ✅；
- #110 / PR #111 Evidence / Assessment Human View ✅；
- #112 / PR #113 Homepage Task Entry v0.1 ✅；
- #114 / PR #115 stable Homepage fragment navigation ✅；
- #116 / PR #117 Resource Page Task Navigation v0.1 ✅；
- #122 Knowledge Workspace / Perspective long-term anchor OPEN；
- #124 P2 Prior-Art Map research OPEN；
- PR #123 Knowledge Workspace Design Principles v1.0 — Human Maintainer accepted, merge/closeout in progress。

## 9. Known open / unrelated work

不要自动吞并：
- PR #26 — Open Collaboration v0.2；
- PR #30 — Fit Test Batch 1；
- Issue #15 — wider Schema / Validator / migration debt；
- Issue #86 — Agent Continuity takeover validation；
- F4 Machine / Curation / Evidence quality line。

## 10. Where to read next

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
Issue #124
→ Issue #122
→ P2 research notes / comments
→ produce Prior-Art Map v0.1
→ P3 Current-State Audit
```

## 11. Staleness check

新 Agent 在继续前必须检查：
1. `Verified At` 之后 main 是否有改变 Phase / main line 的提交；
2. PR #123 是否已合并；
3. #124 是否已有更新的研究顺序 / durable artifact；
4. P2 是否已形成正式 Prior-Art Map 或进入 P3。

不要根据旧 Reference Implementation Phase 的历史 `NOW` 恢复页面功能扩张路线。
