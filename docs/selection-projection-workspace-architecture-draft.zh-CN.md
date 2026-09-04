# Selection / Projection / Workspace Architecture V1（Architecture Draft）

> Status: Architecture Draft
>
> Phase: P4.4 — Selection / Projection / Workspace Architecture
>
> Primary Work Item: Issue #127
>
> Upstream: `docs/knowledge-workspace-design-principles.zh-CN.md`, `docs/canonical-contract-v1-architecture-draft.zh-CN.md`
>
> Scope: 定义 Canonical State 如何被选择、投影、组合并进入 Human / Agent Workspace；**本文件不冻结最终 UI、Query DSL、Perspective Schema、ranking algorithm，也不授权 frontend rewrite。**

## 1. 目的

InteropAtlas 的 Canonical Knowledge 必须保持稳定、可追溯、机器可读，但 Human / Agent 面对同一知识时需要不同的选择、结构和表示。

因此 P4.4 的任务不是设计一个“最终网页”，而是建立 Canonical 与 Search / Browse / Compare / Graph / Timeline / Evidence / Agent 等消费表面之间的架构边界。

核心原则：

> **Canonical Knowledge is the shared knowledge state; Selection, Projection and Workspace are task-specific lenses over it.**

## 2. Core flow

```text
Canonical Knowledge
        ↓
Selection / Perspective
        ↓
Selected Knowledge Set
        ↓
Projection
        ↓
Workspace / Representation
        ↓
Interaction / Operation
        ↓
Human / Agent / Human+Agent
```

这是一条语义处理链，不要求每层都成为独立服务、数据库或持久对象。

关键边界：
- Canonical 决定“共享知识状态是什么”；
- Selection 决定“当前哪些知识进入注意范围”；
- Projection 决定“当前暴露哪些维度和结构”；
- Workspace 决定“如何表达并支持当前任务”；
- Interaction 决定“Human / Agent 可以在该 Workspace 中做什么”。

## 3. Selection / Perspective Contract

Selection 回答：**当前任务应该让哪些 Canonical knowledge 进入工作集？**

候选选择信号包括：
- explicit query；
- object family / kind / facet；
- lifecycle / publication / verification state；
- relation type / graph distance；
- time / version / jurisdiction / scope；
- evidence / freshness signal；
- current task / navigation context；
- explicit user-saved criteria；
- explicit grouping / ranking / emphasis rule。

### 3.1 Selection is not truth

一个对象被排除、降权或折叠，不表示它在 Canonical 中不存在、无效或错误。

因此 Selection output 必须被视为 derived working set，而不是 Canonical mutation。

### 3.2 Selection reason should be inspectable

当选择过程可能显著改变 Human / Agent 判断时，应尽可能能够解释：
- 为什么被包含；
- 为什么被排除；
- 使用了哪些 filter / scope；
- 是否存在 ranking / emphasis；
- 是否因 unknown / stale / disputed state 被降级或单独分组。

P4 不要求所有 Selection 都产生完整 explanation trace，但禁止把不可见的选择逻辑伪装成完整知识空间。

### 3.3 Saved / dynamic Perspective remains provisional

P4.4 允许未来存在可保存、可重新计算的 Perspective，但暂不决定 Perspective 是否成为 Canonical first-class object。

若未来持久化，它首先属于 workspace/configuration layer；除非经过独立知识建模决定，否则不得自动成为 world-state Canonical Fact。

## 4. Projection Contract

Projection 回答：**在已选择的知识中，当前任务需要暴露哪些维度、关系和结构？**

例：
- Compare：暴露真正可比的 properties / capabilities / evidence gaps；
- Timeline：暴露 publication / effective / supersession / version relations；
- Graph：暴露 selected relation families / participants / direction / context；
- Evidence：暴露 Assertion / Evidence / Source / Assessment / Provenance；
- Browse：暴露 classification / facets / related objects；
- Agent retrieval：暴露适合当前 query 的 structured facts + evidence pointers。

### 4.1 Projection may be lossy

Projection 可以为了任务效率而省略 Canonical dimensions，但必须满足：
- 不覆盖 richer Canonical state；
- 不把 omitted information 解释为不存在；
- 重要 scope / uncertainty / conflict 不应因简化而被误表示；
- 必要时能回到 richer Canonical / Evidence context。

### 4.2 Projection is typed by task, not physical storage

Projection 不应由文件夹、YAML 布局或 renderer 模板决定语义。相同 Canonical object 可进入多个 Projection。

## 5. Workspace Contract

Workspace = task-oriented representation + operations。

它不只是“页面样式”，而是围绕一个认知/操作任务组织 selection、projection、representation 和 interaction。

P4.4 保留以下 foundational workspace families：
- **Search / Discovery** — 从 query / facets 进入 solution space；
- **Wiki / Browse** — 在未知空间中逐层发现与链接导航；
- **Single Object / Article** — 线性理解一个 Canonical subject；
- **Compare** — 并行检查真正可比较的候选；
- **Graph / Ecosystem** — 检查实体之间的结构关系；
- **Timeline / Evolution** — 检查版本、发布、替代与历史演化；
- **Evidence / Verification** — 检查 assertion、source、evidence、assessment、provenance。

这些是 architecture families，不是 P4 的 frontend implementation backlog。

## 6. Workspace admission rule

不得因为“可以做一个新视图”就建立永久 Workspace。

新 Workspace 至少应满足一项：
- 让一个此前困难的任务明显更容易；
- 暴露其他 Workspace 难以感知的属性、关系或抽象；
- 降低显著认知负担；
- 为验证/比较/演化分析提供独特操作能力；
- 比继续扩展现有 Workspace 更清晰。

P5 应用真实 IA 数据验证 cognitive gain 与 information loss。

## 7. Coordinated workspace state

多个 Workspace 可以共享一部分工作状态，例如：
- current subject；
- selected candidates；
- active filters；
- time range；
- relation scope；
- evidence focus；
- comparison set。

例如 Human 可以从 Search 选出三个候选，进入 Compare，再打开 Graph 查看它们的组织/标准关系，而不必每次重新选择。

但必须区分：

> **Shared Workspace State ≠ Shared Canonical State.**

Workspace state 的改变默认不修改 Canonical knowledge。

## 8. Read path and write path separation

这是 P4.4 的核心安全边界。

### 8.1 Readable Projection

Workspace 可以读取、筛选、排序、聚合、简化、解释 Canonical Knowledge。

### 8.2 Updatable Projection

只有当一个 Workspace 能明确恢复 canonical target、mutation semantics、evidence/provenance 与 validation requirements 时，才可能提供写入操作。

因此：

> **Readable Projection ≠ Updatable Projection.**

以下 View 默认不得直接反写：
- lossy aggregate；
- ranked list；
- inferred cluster；
- graph layout；
- generated summary；
- timeline grouping；
- recommendation；
- Agent narrative。

若 Human / Agent 在这些表面发现需要修改 Canonical 的内容，应转换为 P4.2 定义的 Candidate Assertion / Proposal / Patch / Evidence contribution，再进入统一 Intake Contract。

## 9. Derived state classes

为避免所有非 Canonical 数据混成一类，P4.4 概念上区分：

1. **Ephemeral Query State** — 一次 search/filter/focus；
2. **Workspace State** — 当前比较集、展开项、视图参数；
3. **Saved Perspective / Configuration** — 可重用的明确选择规则；
4. **Generated Projection** — graph/timeline/table/article projection；
5. **Generated Interpretation** — summary/explanation/ranking/recommendation；
6. **Canonical Candidate** — 从 Workspace 操作中明确提交到 Intake pipeline 的候选 mutation。

只有第 6 类进入 Canonical acceptance path；前五类默认不因持久化就变成 Canonical Fact。

## 10. Human and Agent parity / asymmetry

Human 与 Agent 应看到同一个 Canonical knowledge world，但消费方式不同。

Human Workspace 偏向：
- browse；
- read；
- compare；
- inspect；
- verify；
- navigate。

Agent Workspace / machine surface 偏向：
- query；
- traverse；
- filter；
- retrieve evidence；
- compose structured context；
- generate candidate mutations。

Parity：底层 facts / evidence / identity / relation semantics 一致。

Asymmetry：表示、交互、上下文窗口和可执行操作可以不同。

P4.5 将进一步定义 Access / Capability / Authority 边界。

## 11. Unknown, conflict and scope in projections

Projection 不得把 Canonical 中的重要不确定性抹平。

当任务相关时，应能表达：
- unknown；
- not recorded；
- not applicable；
- unverified；
- disputed / competing assertions；
- stale verification；
- scope/context limitation。

Compare 尤其不得把“缺数据”显示成“值为否”；Graph 不得把“未选择显示的 relation”表现成“没有 relation”；Timeline 不得把“未知日期”自动排除后暗示完整时间序列。

## 12. Ranking / personalization boundary

P4.4 不建立 opaque personalization / recommendation architecture。

未来若使用 ranking / recommendation：
- ranking signal 应与 Canonical truth 分离；
- user-specific preference 不进入公共 Canonical truth；
- important ranking criteria 应尽可能 inspectable；
- recommendation 不得覆盖完整候选空间；
- Agent ranking 结果默认属于 Generated Interpretation。

这与 Public Knowledge Lifecycle ≠ Personal Attention / Memory Metabolism 保持一致。

## 13. Cache / index / materialized view boundary

为了性能，未来可以存在：
- search index；
- graph index；
- denormalized read model；
- materialized projection；
- cache。

它们属于 derived infrastructure，不自动成为新的 authority source。

必须满足：
- 能指向或重建自 Canonical source；
- stale state 可检测/刷新；
- rebuild 不改变 Canonical semantics；
- derived store 丢失不应导致 Canonical knowledge 丢失。

## 14. P5 validation matrix

| Question | Representative experiment |
| --- | --- |
| Selection boundary | Search query + facets 是否能解释 inclusion/exclusion |
| Compare projection | 3–5 个真实 standards/methods 是否能形成真正可比维度 |
| Graph projection | 同一对象在不同 relation scope 下是否避免误导 |
| Timeline projection | version/publication/supersession 是否能表达未知日期 |
| Evidence workspace | conflicting assertions 是否可理解且可追源 |
| Coordinated views | Search → Compare → Graph 是否能共享 selection state |
| Loss recoverability | 从简化 projection 能否回到 richer Canonical context |
| Agent retrieval | Agent 是否能获取 structured facts + evidence 而非页面 scraping |
| Write boundary | 从 Workspace correction 是否能形成 Candidate Patch 而非直接改 View |
| Ranking transparency | ranking 存在时是否能区分 ranking 与 truth |

## 15. Not Yet decisions

P4.4 不冻结：
- Perspective 是否一等持久对象；
- Query / Selection DSL；
- Workspace protocol；
- frontend component model；
- exact URL/navigation model；
- saved view storage；
- recommendation algorithm；
- personalization model；
- materialized-view technology；
- Human/Agent shared-session protocol；
- final Workspace catalog。

这些进入 P5 experiments / P6 implementation。

## 16. Settled P4.4 architecture decisions

- Canonical → Selection → Projection → Workspace → Interaction 是主要消费链；
- Selection / Projection 是 derived semantics，不是第二套 truth；
- Workspace 是 task-oriented representation + operations，不只是页面模板；
- Search / Browse / Object / Compare / Graph / Timeline / Evidence 是 foundational workspace families；
- 多 Workspace 可共享 selection/focus state，但 Workspace State ≠ Canonical State；
- Readable Projection ≠ Updatable Projection；
- lossy/aggregate/ranked/generated view 默认不得直接反写 Canonical；
- Workspace 中发现的知识修改必须转换为 P4.2 Candidate/Proposal/Patch/Evidence 并走统一 Intake；
- unknown/conflict/scope 在任务相关时必须保持可见或可恢复；
- ranking/personalization 与 Canonical truth 分离；
- indexes/caches/materialized views 是可重建 derived infrastructure；
- Human 与 Agent 共用一个知识世界，但允许不同 representation / operation surface。

## 17. Next

P4.4 第一轮完成后进入 **P4.5 Human + Agent Access Architecture**：定义 Human / Agent 如何访问同一 Canonical / Workspace world、身份与 capability 如何表达、哪些操作属于 read/query/candidate-write/canonical-acceptance、如何避免 Agent 身份与 GitHub Actor/权限混淆，以及 Human+Agent 协作状态如何保持可追溯。