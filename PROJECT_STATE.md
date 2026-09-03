# InteropAtlas Project State

<!-- InteropAtlas Document Metadata v0
Document Status: Living Project Checkpoint（持续更新的项目断点）
Document Created At: 2026-09-02T10:43:23+08:00
Document Updated At: 2026-09-03T21:38:00+08:00
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
> Verified At: 2026-09-03T21:38:00+08:00
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

此前 Reference Implementation 的 Permanent Human Route、Search、Compare、Evidence / Assessment presentation、Homepage task entry 等代表性成果保留，但不自动沿旧页面功能路线扩张。

## 4. Design baseline after P2

P1 Knowledge Workspace / Perspective 设计方向已通过 P2 prior-art / standards validation，没有发现需要推翻 P1 的重大错误。

当前上层方向仍为：

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

P2 对其增加以下边界：

- Perspective 仍是上位研究概念，不能提前把 filter / query / continuous reevaluation / ranking / recommendation / manual curation 压成单一机制；
- Public Knowledge Lifecycle 关注 Validity / Freshness / Authority / Supersession / Archive / Historical Value / Retention / Reactivation；个人使用频率、注意力衰减、项目激活属于个人层；
- Identity / Merge 比普通 Relation 更高风险、更保守；
- Statement / Provenance 与 Relation / participants + roles 是不同层；
- View 能正确生成，不代表能安全反向修改 Canonical；
- Agent inference / artifact 默认不是公共事实；
- 产品层可以默认简单，但必须能解释当前 scope / selection，并可下钻到 source / evidence / relations / history。

P2 完整研究记录与总收口：**Issue #124（Completed）**。

## 5. Current phase and resume point

```text
P1  Design Principles                    ✅ Completed / accepted
        ↓
P2  Prior-art / standards research       ✅ Completed / #124 closed
        ↓
P3  Current-state audit                  ← NOW
        ↓
P4  Architecture / Roadmap reset
        ↓
P5  Real-data experiments / intake stress test
        ↓
P6  Implementation + continuous intake
```

### NOW: P3 — Current-State Audit

P3 的任务不是继续做泛研究，也不是马上重写 Schema / UI，而是拿 P2 已验证和修正的认知，对**当前真实 InteropAtlas**做结构化体检，为 P4 Architecture / Roadmap Reset 提供事实依据。

Long-term Owner intent anchor: **Issue #122**。

P2 research record / P3 input: **Issue #124**，尤其最终 P2 总收口评论。

Standards Candidate Pool 已建立：`03_Evolution/01_Research/standards-candidate-pool-v0.1.zh-CN.md`。候选池可在 P3 并行增长，但当前不批量污染 Canonical Knowledge。

## 6. P3 required audit scope

### Identity / Canonical Model
- Object ID、external identifier、Source URL 是否混淆；
- merge / dedup 是否过度激进；
- binary Relation 是否已经造成角色 / 多参与者语义损失；
- Context / Scope / qualifier 是否缺失并造成真实错误。

### Evidence / State / Lifecycle
- Validity、Freshness、Authority、last-updated 是否混用；
- 是否能表达 old-but-valid、new-but-low-confidence、superseded-but-historically-important；
- archive / invalidated / superseded / deleted 是否区分；
- Fact / Assessment / generated output 是否混淆。

### Selection / Perspective
- Search / Compare / Graph / Browse 是否存在隐藏的 selection / ranking；
- saved view / Perspective 是否 explainable / replayable；
- manual curation、query、ranking、personalization 是否混为一种状态。

### Projection / Representation
- Article / Compare / Graph 是否只是派生 View，还是偷偷维护第二事实源；
- Renderer / generated content 是否反向污染 Canonical；
- 是否存在“改 View = 改底层”的隐含路径；
- transformation provenance / known loss 是否可追踪。

### Human + Agent / Collaboration
- Agent output 是否可能直接成为 Fact；
- proposal / task artifact / workspace state / canonical artifact 是否区分；
- 多 Agent 冲突是否可保留和审计；
- executor / reviewer / authority / delegation 是否清楚；
- high-impact mutation 是否有更高 gate。

### Product / Human Route
- 页面是否围绕 raw Schema 而不是用户任务；
- View 是否过度增殖；
- 当前 scope / filter / hidden information 是否可见；
- 是否能从简化表示下钻到 source / evidence / relations / history。

## 7. Current stop conditions

在 P3/P4 形成明确结论前，不自动执行：
- destructive Schema migration；
- 把 Perspective / Knowledge Metabolism 设为 mandatory Canonical type；
- 全量 Relation → N-ary / Hypergraph 迁移；
- wholesale frontend / renderer rewrite；
- opaque personalization / recommendation ranking；
- stable Specification promotion；
- 大规模数据删除；
- Ruleset / Branch Protection / Governance Automation。

已有 #118/#119 等旧页面功能工作**不要机械恢复**。P3 应判断其属于 Fits / Temporary View / Premature Constraint / Missing Capability / Research Needed，再决定继续、降级或暂停。

## 8. Recent stable milestones

- #89–#93 lifecycle / provenance historical backfill ✅；
- PR #123 Knowledge Workspace Design Principles v1.0 merged / Human Maintainer accepted ✅；
- Research Governance v0.1 established ✅；
- #124 P2 Prior-Art / Standards Research completed ✅；
- P2 结论：无 P1 重大设计错误；形成 R2 边界修正并进入 P3 ✅；
- Standards Candidate Pool v0.1 established ✅。

## 9. Known open / unrelated work

不要自动吞并：
- #122 — Knowledge Workspace / Perspective long-term anchor；
- #125 — Candidate Pool 历史入口 / acceleration work item；
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
Issue #124 final P2 synthesis
→ Issue #122
→ audit current Canonical Objects / Relations / Evidence / Runtime / Human Route / Agent path
→ classify findings
→ produce P3 Current-State Audit
→ P4 Architecture / Roadmap Reset
```

## 11. Staleness check

新 Agent 在继续前必须检查：
1. `Verified At` 之后 main 是否有改变 Phase / main line 的提交；
2. 是否已经存在新的 P3 Primary Work Item / audit artifact；
3. #122 是否有新的 Human Owner 意图；
4. Research Governance / Task Governance 是否已有更高版本。

不要根据旧 Reference Implementation Phase 或已完成的 P2 `NOW` 恢复页面功能扩张路线。
