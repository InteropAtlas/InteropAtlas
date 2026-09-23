# GitHub Issue 运行治理：先例与 IA 采用方案

Updated: 2026-09-23

## 目的

InteropAtlas 的 Open Issue 已经达到数百规模。目标不是消灭 Issue，而是降低认知负担：让 Human / Agent 能快速区分“正在研究什么、正在执行什么、未来储备什么、为什么现在不能做”。

## 外部先例

### GitHub 官方

GitHub 将 Issue 用于计划、讨论和跟踪工作；Projects 用于把 Issue / PR 投影为 table、board、roadmap，并通过自定义字段、过滤、排序、分组和自动化管理 backlog 与 roadmap。

参考：
- https://docs.github.com/en/issues
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects

### Kubernetes

Kubernetes 的 triage 将“是否有效 / 是否需要更多信息”“优先级”“生命周期”分开管理。其优先级包括 critical-urgent、important-soon、important-longterm、backlog、awaiting-more-evidence，并使用 stale / frozen 等生命周期机制。

参考：
- https://kubernetes.io/docs/contribute/review/for-approvers/
- https://kubernetes.io/docs/contribute/participate/issue-wrangler/

对 IA 的启发：**一个 Issue 当前处于什么工作形态、主要属于哪个能力域、何时值得投入注意力，是三个核心维度；等待原因只在确实存在时附加。**

### Rust

Rust triage 明确区分 waiting-on-review、waiting-on-author、blocked，并周期性检查长期等待项。

参考：
- https://forge.rust-lang.org/release/triage-procedure.html

对 IA 的启发：**“没有在做”不等于“不重要”；应明确它在等什么。**

## IA 当前采用的最小模型

### 1. Lifecycle

- `lifecycle:research` — 问题仍在探索、比较、形成假设或方法。
- `lifecycle:active` — 已有明确 Work Unit / deliverable / acceptance boundary，当前激活。
- `lifecycle:backlog` — 有价值但当前未激活；包括 Future / Draft / Deferred / Blocked 等储备。

Open Issue 不等于 Active Work。

### 2. Area

- `area:knowledge` — Canonical knowledge、identity、relation、evidence、provenance、schema、validation、coverage 等。
- `area:interface` — Human / Agent access、search、compare、workspace、projection、API、representation、interchange 等。
- `area:operations` — intake、review、governance、continuity、automation、security、maintenance、quality loop、adaptation 等。

跨域 Issue 先选择 Primary Area，必要时再记录 Secondary。

### 3. Priority

- `priority:now`
- `priority:soon`
- `priority:long-term`
- `priority:someday`

Priority 与 Lifecycle 正交。

### Waiting Condition（可选）

Waiting 不是第四个必填维度，而是只在 Issue 当前确实存在明确等待条件时附加：

- `waiting:prerequisite`
- `waiting:evidence`
- `waiting:scale`
- `waiting:owner`

没有明确等待条件时，不添加任何 `waiting:*` 标签；`waiting:none` 不再使用。

因此 IA 的最小模型是：**Lifecycle × Area × Priority + 可选 Waiting Condition**。

## 生命周期

```text
Research Issue
   ↓ 形成明确交付边界
Work / Active Issue
   ↓ 形成稳定成果
Repository

Project = 对 Issue / PR 的组织与投影，不是第二事实源。
```

## Project 建议视图

- Current — Lifecycle = Active
- Research — Lifecycle = Research
- Near-term — Priority = Now / Soon
- Waiting — 存在任意 `waiting:*` 标签
- Knowledge — Area = Knowledge
- Interface — Area = Interface
- Operations — Area = Operations

Issue Labels 是 Metadata 的唯一事实源；Project 只基于 Labels 做过滤、分组和展示，不维护重复的 Metadata 真值。

## 自动化边界

机器适合：检查缺失 / 冲突 metadata、Active 长期无更新、stale lease / Blocked 条件，并根据已审核的审计文件同步 Lifecycle。

机器不应：仅因长时间无更新就判断 Issue 没价值、自动把 Backlog 激活、自动把 Research 判定为已收敛、自动关闭需要语义判断的 Issue。

## 当前事实源

- Issue：具体研究 / 工作上下文。
- PROJECT_STATE.md：当前项目导航和激活边界。
- GitHub Project：多 Issue 投影视图。
- Repository：稳定成果。
- `03_Evolution/issue-classification-audit-state.md`：2026-09-23 首轮全量分类审计及可恢复维护记录。
