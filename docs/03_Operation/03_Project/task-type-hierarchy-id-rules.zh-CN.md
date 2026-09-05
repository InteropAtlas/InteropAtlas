# Task Type / Hierarchy / ID Rules（任务类型、层级与标识规范）

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

> 来源：#287 首轮历史议题整理。从 207 个 Open Issue 的真实样本中归纳任务类型、层级关系和标识规则。

## 1. 核心结论

**GitHub Issue Number 是唯一稳定的 Work Item 身份。** 不建立与 #number 并行的自定义流水号（如 IA-TASK-001、P6-INT-03 等）。

理由：
- Issue Number 由平台保证唯一、不可变、可引用；
- 自定义流水号需要额外维护映射，且与 Issue Number 形成第二事实源；
- 跨 Issue 引用使用 `#123` 即可，人类和 Agent 都能解析。

## 2. 概念区分

从真实样本中识别出以下容易混淆的概念：

| 概念 | 是什么 | 不是什么 | 载体 |
|---|---|---|---|
| **Phase** | 项目历史阶段（P1–P6），表达"什么时候定义的" | 不是优先级，不是任务层级 | 标题前缀（历史保留） |
| **Workstream** | 长期维护的工作领域（Hygiene / CI / Docs 等） | 不是具体任务，不是 Phase | GitHub Project 字段 / Label |
| **Task** | 有 Deliverable + Acceptance 的可执行工作 | 不是研究，不是决策 | Issue (type:task) |
| **Research** | 开放式调查，产出 Research artifact | 不直接改 Canonical，不设 Acceptance checklist | Issue (type:research) + `03_Evolution/01_Research/` |
| **Experiment** | 有假设的压力测试 / Fit Test | 不是普通 Task，有明确对照组 | Issue (type:experiment) + `03_Evolution/02_Experiments/` |
| **Decision** | 需要做出选择的架构/治理事项 | 不是讨论，必须有结论 | Issue (type:decision) + `03_Evolution/03_Decisions/` |
| **Umbrella** | 组织多个子 Issue 的上层跟踪 | 不自己承担 Deliverable | Issue (type:umbrella) 或 Project View |
| **Maintenance** | 仓库长期维护的周期性工作 | 不是一次性建设任务 | Issue (type:maintenance) |
| **Candidate** | 待收录的知识对象 | 不是 Work Item，不建 Issue | Candidate Pool / Project |

## 3. 层级规则

### 3.1 Parent / Sub-issue 层级

- Parent Issue 是**执行组织层级**，不是语义分类；
- 一个 Issue 最多有一个 Parent；
- Parent 关闭时，子 Issue 必须全部关闭或重新指定 Parent；
- 嵌套不超过 2 层（Parent → Child），避免深层树；
- Umbrella 类型的 Parent 优先用 Project View 替代。

### 3.2 当前仓库的真实层级样本

```text
#129 P6 V1 Implementation (Umbrella, 47 children)
  ├── #146 Continuous Intake (Umbrella, 17 children, In Progress)
  │    ├── #167 Intake Parallelism Pilot (Task)
  │    ├── #253 Candidate Discovery Automation (Task, Conditional)
  │    └── ...
  ├── #149 Agent Access Slice 1 (Task, Draft)
  ├── #176 Lifecycle Migration Cohort 1 (Task, Draft)
  └── ...
#369 Long-term Operations (Umbrella, 7 children, Draft)
  ├── #374 Workspace Feedback Loop (Research, Draft)
  ├── #375 Architecture Fitness Loop (Research, Draft)
  └── ...
```

### 3.3 层级反模式（从样本中识别）

1. **Parent 已关闭但子 Issue 仍 Open** → Hygiene Action 可检测
2. **Umbrella 嵌套 Umbrella** → 应扁平化，用 Project View 替代
3. **一个 Issue 同时被多个 Parent 引用** → 应只保留一个 Parent
4. **Task 作为 Parent 组织其他 Task** → 应改为 Umbrella 类型或 Project

## 4. ID 与引用规则

### 4.1 Issue 内引用

- 跨 Issue 引用：`#123`
- 跨仓库引用：`owner/repo#123`
- PR 引用：`#123`（PR 与 Issue 共享编号空间）
- Commit 引用：`@sha` 或完整 URL

### 4.2 Body 中的结构化字段

每个 Issue body 顶部应包含（过渡期间保留文本字段，长期可被 Label + Project 字段替代）：

```text
Status: draft | ready | claimed | in_progress | blocked | review
Type: task | research | experiment | decision | umbrella | maintenance
Priority: p0 | p1 | p2 | p3
Parent: #123 (可选)
Blocked By: #123 / 描述 (仅 blocked 时必填)
Task Authority: T0 | T1 | T2 | T3 (高影响任务必填)
Review Class: normal | high-impact
```

### 4.3 不使用的 ID 方案

以下方案在样本中出现过但被否决：

- **PH-xxx（Phase-based ID）**：与 Issue Number 重复，且 Phase 结束后 ID 失去意义
- **IA-TASK-xxx**：需要维护映射表，跨引用不直观
- **子任务编号（1.1, 1.2）**：在 Issue 标题中使用时，重排后编号失效

## 5. 新建 Issue 的最小模板

```text
## Operational Metadata
Status: draft
Type: task
Priority: p2
Parent: #123 (如适用)
Blocked By: — (仅 blocked 时填写)
Task Authority: T1
Review Class: normal

## Objective
（一句话说明要做什么）

## Scope
（包含什么 / 不包含什么）

## Acceptance Criteria
- [ ] 可验证的完成条件
```

## 6. 与 AGENTS.md 的对齐

- `Draft → Ready → Claimed → In Progress → Review → Done` 流程不变；
- `Draft 不得被 Agent 自主当作 Ready` 不变；
- 高影响事项需 Human Owner / Governance Gate 不变；
- 本规范只增加 Type / Priority / Workstream 的正交 Label，不改变现有权限模型。
