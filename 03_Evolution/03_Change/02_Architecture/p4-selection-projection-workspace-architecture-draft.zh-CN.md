# Selection / Projection / Workspace Architecture V1（P4.4 Historical Architecture Draft）

> Lifecycle: **Historical / Completed P4 Architecture Artifact**
>
> Original Phase: P4.4 — Selection / Projection / Workspace Architecture
>
> Primary Work Item: Issue #127 — completed / closed
>
> Current Role: 保存 P4.4 将 Canonical → Selection → Projection → Workspace → Interaction 收敛为架构边界的历史。当前设计原则以 `docs/knowledge-workspace-design-principles.zh-CN.md` 为 Primary Home，总体边界以 Master Design 为准。
>
> Historical note: 原文中的 P5/P6 handoff、Not Yet 与“Next P4.5”属于阶段施工上下文，不再作为当前路线。

## P4.4 accepted architecture synthesis

P4.4 建立的核心处理链为：

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

关键边界：Canonical 决定共享知识状态；Selection 决定当前哪些知识进入注意范围；Projection 决定当前暴露哪些维度和结构；Workspace 组织任务导向的表达与操作；Interaction 决定主体能够做什么。

### Selection / Perspective

Selection 是 derived working set，不是 truth。对象被排除、降权或折叠，不表示它在 Canonical 中不存在、无效或错误。当选择显著影响判断时，应尽可能能检查 inclusion/exclusion、filter/scope、ranking/emphasis 与 unknown/stale/disputed 处理理由。

### Projection

Projection 可以为了任务效率有损，但不得覆盖 richer Canonical state，不得把 omitted information 解释为不存在，并应在必要时允许回到更完整的 Canonical / Evidence context。Projection 按任务定义，而不是由物理存储或 renderer 模板决定。

### Workspace

Workspace 被定义为 **task-oriented representation + operations**，而不仅是页面样式。P4.4 保留 Search / Discovery、Wiki / Browse、Single Object / Article、Compare、Graph / Ecosystem、Timeline / Evolution、Evidence / Verification 等 foundational families，但这些不是永久冻结的最终目录。

多个 Workspace 可以共享 current subject、comparison set、filters、time range、relation scope、evidence focus 等工作状态，但：

> **Shared Workspace State ≠ Shared Canonical State.**

### Read / write boundary

P4.4 的关键安全边界：

> **Readable Projection ≠ Updatable Projection.**

lossy aggregate、ranked list、inferred cluster、graph layout、generated summary、timeline grouping、recommendation、Agent narrative 等默认不得直接反写 Canonical。需要修改知识时，应转换为 Candidate Assertion / Proposal / Patch / Evidence contribution 并进入统一 Intake。

### Derived state

P4.4 概念上区分 Ephemeral Query State、Workspace State、Saved Perspective / Configuration、Generated Projection、Generated Interpretation 与 Canonical Candidate。只有明确进入 Intake 的 Canonical Candidate 才进入 Canonical acceptance path。

### Human / Agent

Human 与 Agent 共用一个 Canonical knowledge world，底层 facts / evidence / identity / relation semantics 一致；表示、交互、上下文窗口和操作表面允许不同。

### Unknown / conflict / scope

Projection 不得把 unknown、not recorded、not applicable、unverified、disputed、stale verification 或 scope/context limitation 在任务相关时静默抹平。Compare 不应把缺数据表示成否；Graph 不应把未显示关系表示成没有关系；Timeline 不应因未知日期被省略而暗示时间序列完整。

### Ranking / personalization

ranking / recommendation 与 Canonical truth 分离；user-specific preference 不进入公共 Canonical truth；重要 ranking criteria 应尽可能 inspectable；recommendation 不覆盖完整候选空间。

### Derived infrastructure

search index、graph index、denormalized read model、materialized projection、cache 都属于 derived infrastructure，必须可指向或重建自 Canonical source，不能成为第二 authority source。

## Historical P4.4 decisions

P4.4 当时确认：

- Canonical → Selection → Projection → Workspace → Interaction 是主要消费链；
- Selection / Projection 是 derived semantics，不是第二套 truth；
- Workspace 是 task-oriented representation + operations；
- 多 Workspace 可共享 selection/focus state，但 Workspace State ≠ Canonical State；
- Readable Projection ≠ Updatable Projection；
- lossy/aggregate/ranked/generated view 默认不得直接反写 Canonical；
- unknown/conflict/scope 在任务相关时必须保持可见或可恢复；
- ranking/personalization 与 Canonical truth 分离；
- indexes/caches/materialized views 是可重建 derived infrastructure；
- Human 与 Agent 共用一个知识世界，但允许不同 representation / operation surface。

这些结论后来由当前 Knowledge Workspace Design Principles、Master Design 及实现/实验继续承接。