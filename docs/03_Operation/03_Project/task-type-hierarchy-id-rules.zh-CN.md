# Task Type / Hierarchy / ID Rules（任务类型、层级与标识规范）

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-05T18:00:00+08:00
Document Updated At: 2026-09-05T18:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 来源：#287 历史议题整理与 Owner 对当前任务可读性的修正。

## 1. 核心结论

**GitHub Issue Number 是唯一稳定的 Work Item 身份。** 不建立与 `#number` 并行的项目阶段号或自定义流水号。

因此，新任务标题默认不再添加 `P1 / P2 / P6`、`PH-*`、`IA-TASK-*`、`V1-*` 等项目级前缀。标题直接描述工作本身。

历史 Issue 中已有的阶段前缀可以留在历史记录中；它们不再定义当前路线，也不应出现在 Owner 的主线视图里。

## 2. Owner View 与执行层分离

Owner 默认只需要看到：

```text
长期目标
  ↓
当前主线
  ↓
当前真正需要决策或推进的工作
```

实现层可以继续使用 Issue Number、Status、Type、Priority、Parent、Blocked By、Task Authority 等元数据，但这些内部标识不应机械地堆到 Owner-facing 汇报中。

除非 Human Owner 正在讨论某个具体 Issue，否则汇报优先使用自然语言任务名，Issue Number 作为次级引用。

## 3. 任务类型

| 类型 | 含义 | 主要载体 |
|---|---|---|
| **Task** | 有明确 Deliverable + Acceptance 的可执行工作 | Issue |
| **Research** | 有边界的调查，产出可复用研究结果 | Issue + `03_Evolution/01_Research/`（达到长期价值门槛时） |
| **Experiment** | 有假设、条件和观察结果的实验 | Issue + `03_Evolution/02_Experiments/`（达到长期价值门槛时） |
| **Decision** | 需要明确选择并留下长期依据的事项 | Issue + `03_Evolution/03_Decisions/`（达到长期价值门槛时） |
| **Umbrella** | 临时组织多个 Work Item 的上层任务 | Issue；规模增长后优先 Project View |
| **Maintenance** | 有边界的维护批次 | Issue；长期责任由 Project / Automation 承担 |
| **Candidate** | 待收录知识对象 | Candidate Pool；不是 Work Item，不建一对象一 Issue |

`Phase` 不再作为现行 Work Item 类型或标题前缀。历史 `P1–P6` 只解释过去某轮工作何时发生，不参与当前任务身份。

## 4. 层级规则

- Parent Issue 是执行组织关系，不是项目方向本身；
- 一个 Issue 最多一个 Parent；
- Parent 关闭时，子 Issue 应关闭、迁移或解除依赖；
- 默认避免超过 Parent → Child 两层；
- 大型 Umbrella 优先转为 GitHub Project / View，不建立深层 Issue 树；
- Project 是组织和投影视图，不保存只能在那里找到的执行真相。

## 5. ID 与引用

- Issue：`#123`
- 跨仓库 Issue：`owner/repo#123`
- PR：使用 GitHub 原生编号
- Commit：SHA / URL

不使用：

- `P1 / P2 / P6` 作为新任务身份或标题前缀；
- `PH-xxx`；
- `IA-TASK-xxx`；
- `V1-* / V2-*` 作为项目计划任务体系；
- 依赖重排的 `1.1 / 1.2 / 2.3` 子任务流水号。

## 6. Issue 最小元数据

```text
Status: draft | ready | claimed | in_progress | blocked | review
Type: task | research | experiment | decision | umbrella | maintenance
Priority: p0 | p1 | p2 | p3
Parent: #123 (可选)
Blocked By: #123 / 描述 (仅 blocked 时必填)
Task Authority: T0 | T1 | T2 | T3 (高影响任务必填)
Review Class: normal | high-impact
```

这些字段服务 Agent 与维护者执行，不要求在 Owner-facing 汇报里逐项呈现。

## 7. 新建 Issue 的最小模板

```text
## Operational Metadata
Status: draft
Type: task
Priority: p2
Parent: #123 (如适用)
Blocked By: —
Task Authority: T1
Review Class: normal

## Objective
（一句话说明要做什么）

## Scope
（包含什么 / 不包含什么）

## Acceptance Criteria
- [ ] 可验证的完成条件
```

标题示例优先使用：

```text
Continuous Intake：扩大普通候选收录并验证真实摩擦
Agent Structured Access：建立有边界的查询与 Candidate Write
Relation Lifecycle Migration：迁移并验证关系生命周期数据
```

而不是：

```text
P6 V1 Continuous Intake
P6 Agent Access Slice 1
PH-07 V2 Migration
```

## 8. 项目版本边界

项目路线、Living Documents 和 Owner View 不使用 `V1 / V2` 作为规划结构。

版本号仍可以存在于真正具有版本身份的现实对象或技术制品中，例如某一版外部标准、协议、Schema、兼容契约、发布制品和历史快照。不要把“版本身份”与“项目计划版本号”混为一谈。

## 9. 与 AGENTS.md 的对齐

- `Draft → Ready → Claimed → In Progress → Review → Done` 不变；
- Draft 不得被 Agent 自动视为 Ready；
- 高影响事项仍需 Human Owner / Governance Gate；
- GitHub Issue Number 是 Work Item 身份；
- Owner 主线由 `PROJECT_STATE.md` 表达，不由阶段前缀、Project 字段或 Issue 树替代。
