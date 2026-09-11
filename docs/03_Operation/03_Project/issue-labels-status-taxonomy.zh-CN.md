# Issue Labels / Status Taxonomy（最小标签与状态分类体系）

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-05T18:00:00+08:00
Document Updated At: 2026-09-05T18:00:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Agent — Doubao / MainAgent
  Executor: Agent — Doubao / MainAgent
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 来源：#287 首轮历史议题整理。从 207 个 Open Issue 的真实状态字段中归纳，目标是**最小、无歧义、机器可判定**。

## 1. 设计原则

1. **Status 是生命周期，不是优先级**。一个 Issue 同一时间只有一个 Status。
2. **Label 是正交维度**，不互相替代：Status × Type × Priority × Workstream。
3. **机器可判定优先**：每个 Label 都有明确的进入/退出条件，Hygiene Action 可以自动检查违规。
4. **不发明复杂流水号**：GitHub Issue Number 是唯一稳定身份。
5. **历史 Phase（P1–P6）保留在标题中作为语义上下文**，不作为 Status 或 Label。

## 2. Status Label（生命周期，互斥，必须恰好一个）

```text
status:draft        — 尚未收敛为可执行 Work Item；不得被 Agent 自主提升为 Ready
status:ready        — 前置条件满足，可被认领执行
status:claimed      — 已有人/Agent 认领，但尚未开始实质执行
status:in_progress  — 正在执行
status:blocked      — 外部前置条件不满足；必须在 body 中写明 Blocked By
status:review       — 执行完成，等待独立 Review / Human Gate
status:done         — 已完成并关闭（GitHub state=closed, reason=completed）
status:not_planned  — 不做 / 触发条件不存在 / 已过时（GitHub state=closed, reason=not_planned）
```

### 迁移规则

当前 Issue body 中的 `Status: xxx` 文本字段是过渡状态。逐步迁移为 Label：

| 当前 body 文本 | 迁移到 Label |
|---|---|
| Draft / Future | status:draft |
| Draft / Conditional Future | status:draft (+ type:conditional) |
| Draft / Future Gate | status:draft (+ review-class:high-impact) |
| Draft / Future Operating Umbrella | status:draft (+ type:umbrella) |
| Draft / Deferred | status:draft |
| Draft / Queued | status:ready |
| Draft | status:draft |
| Ready | status:ready |
| Blocked | status:blocked |
| In Progress | status:in_progress |
| Review | status:review |
| 无 Status 字段（旧 P0–P2） | 先判定：已完成→done，仍有效→补 status |

## 3. Type Label（任务类型，互斥，必须恰好一个）

```text
type:task          — 有明确 Deliverable 和 Acceptance 的可执行工作
type:research      — 开放式研究，产出 Research artifact，不直接改 Canonical
type:experiment    — 有假设、有对照组、有结论的压力测试 / Fit Test
type:decision      — 需要做出架构 / 治理 / 方向选择的 Decision Record
type:umbrella      — 组织多个子 Issue 的上层跟踪；优先由 Project View 承担
type:maintenance   — 仓库长期维护（Hygiene / Staleness / CI / Structure）
```

### Umbrella 的特殊规则

- Umbrella Issue 只组织子任务，不自己承担具体 Deliverable；
- 子任务数 ≥ 3 时优先考虑用 GitHub Project View 替代 Umbrella Issue；
- Umbrella 的 Status 由子任务聚合决定，不单独标记 In Progress。

## 4. Priority Label（优先级，互斥，必须恰好一个）

```text
priority:p0  — 阻塞当前主线 / 安全 / 数据完整性
priority:p1  — 当前 Phase 的核心路径
priority:p2  — 重要但不阻塞当前主线
priority:p3  — 改善型 / 低紧急度
```

P1–P6 标题前缀是**历史 Phase 语义**，不是 Priority。新 Issue 不再使用 P0–P6 标题前缀表达优先级，改用 Label。

## 5. Review Class Label（评审等级，可选）

```text
review-class:normal       — 普通技术工作，deterministic evidence 可自检
review-class:high-impact  — 涉及 Scope / Schema / Governance / 不可逆决策，需 Human Gate
```

## 6. Workstream Label（长期维护 Project 的工作流，可选）

对应 #287 定义的六个 Workstream：

```text
workstream:issue_hygiene
workstream:candidate_pool
workstream:docs_staleness
workstream:repo_structure
workstream:provenance
workstream:ci_hygiene
```

普通 P6 建设 Issue 不需要 Workstream Label；只有长期维护类任务使用。

## 7. 最小必填集

每个 Open Issue 必须有：

1. 恰好一个 `status:*` Label
2. 恰好一个 `type:*` Label
3. 恰好一个 `priority:*` Label
4. body 中包含 `Status:` 字段（过渡期间与 Label 并存，后续可移除）

缺少任一项 → Hygiene Action 告警，不自动关闭。

## 8. 不使用的 Label

以下概念**不**建 Label，避免维度膨胀：

- Phase（P1–P6）→ 保留在标题前缀，历史语义
- Task Authority（T0–T3）→ 保留在 body 字段，不适合 Label 过滤
- Assignee → GitHub 原生 Assignee 功能
- Milestone → GitHub Milestone 或 Project
- Component → 由 Issue 标题和 body 表达，不建 component Label（当前仓库规模不需要）
