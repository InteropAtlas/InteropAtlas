# InteropAtlas 人机开放协作 Prior Art 调研

> 状态：Research Note。用于为 InteropAtlas 后续 Open Collaboration Profile 提供依据，不代表已经冻结协作规范。

## 当前问题

InteropAtlas 未来需要允许人类贡献者与 AI / Agent 共同建设同一开放仓库。核心问题不是“如何运行一个 Agent”，而是：

- 人类与 Agent 在协作系统中分别是什么角色；
- 一个任务如何被分配、接手、交接和释放；
- 谁负责 Review / Oversight；
- 如何避免多个 Agent 或人与 Agent 重复劳动；
- 哪些决策必须保留人工授权；
- 如何让同一套贡献流程同时对人和 Agent 成立。

## 直接相关的标准化工作

### ISO/IEC CD 25589 — Framework for human-machine teaming

当前状态：Committee Draft，仍在制定中。

公开范围显示，该文件正在建立 Human-Machine Teaming 的概念、术语、人与机器之间的关系描述、技术特征和设计原则，并基于 ISO/IEC 5339 给出 AI 应用在人机团队中的开发和应用指导。

对 IA 的意义：适合作为“人和 Agent 如何被视为同一团队成员”的上位概念来源，但不能直接提供 GitHub Issue 领取、Lease 等仓库机制。

### ISO/IEC AWI 25880 — Organizational implementation of human-machine teaming

当前状态：Approved Work Item，处于早期制定阶段。

目标是规定并指导组织如何在 AI 系统实际运行中实施 Human-Machine Teaming。

对 IA 的意义：未来最值得持续跟踪，因为 IA 真正需要解决的是“一个开放组织怎样把人和 Agent 放进同一协作流程”。

### ISO/IEC CD TR 42109 — Use cases of human-machine teaming

当前状态：Committee Draft Technical Report。

作用是积累和整理 Human-Machine Teaming 实际用例。

对 IA 的意义：适合用于验证 IA 自己的人机协作场景是否属于已有模式，避免只从软件 Agent 场景推导一般规则。

## 已发布的支撑标准 / 框架

### ISO/IEC 5339:2024 — Guidance for AI applications

强调 AI 应用生命周期中的 stakeholder engagement、多方沟通以及 make / use / impact 等不同视角。

对 IA 的启示：项目不能只从 Agent 开发者视角设计协作系统；维护者、普通贡献者、Reviewer、最终使用者等都应被视为不同 stakeholder。

### NIST AI RMF

NIST AI RMF 已明确要求：

- 区分 human-AI configuration 中不同角色和责任；
- 明确沟通关系；
- 定义 human oversight；
- 持续记录、评估人机配置及其结果；
- 区分使用 AI 的人和监督 AI 的人。

对 IA 的启示：执行者、Reviewer / Overseer、治理者应是不同角色。默认不应让同一 Agent 同时拥有执行、审核和最终授权。

## 可观察的现实实现：GitHub Coding Agents

GitHub 当前已经允许把 Issue 分配给 Coding Agent。Agent 完成任务后创建 Pull Request，并请求人工 Review；人可以继续通过 PR 评论要求 Agent 修改。

它不是国际标准，但非常接近 IA 的实际工作环境，因此适合作为 Reference Implementation / Operational Prior Art。

## 当前空白

目前没有发现已经成熟发布、可以直接规定以下流程的国际标准：

```text
开放仓库
  ↓
人类 + Agent 共享任务池
  ↓
任务领取 / 分配
  ↓
防重复 / Lease / Heartbeat
  ↓
工作与交接
  ↓
Review
  ↓
Merge / Release
```

因此 IA 后续更合适的方式不是从零发明 Human-AI Teaming 理论，而是：

```text
ISO / NIST 上位原则
        +
GitHub / 开源社区现实实践
        ↓
IA Open Collaboration Profile
```

## 对 IA V0 的暂定约束

在进一步研究完成前，只保留以下轻量方向：

1. AI / Agent 属于协作参与者，不属于项目本体，也不等同于自动化基础设施；
2. 人和 Agent 尽量共享 GitHub Issues / PR / Review 这套公开协作流程；
3. 普通任务默认一个主执行者，避免重复劳动；
4. Review / Oversight 与执行角色分离；
5. Lease、Heartbeat、Agent 自动选任务等属于后续实现机制，不先写成项目根本结构；
6. 等 ISO/IEC 25589、25880 等继续成熟后再调整 IA Profile。

## 后续 Prior Art

下一轮优先继续研究：

- 开源社区现有任务领取、stale / reassignment、review / CODEOWNERS 等成熟实践；
- GitHub Projects / Issues 是否足以承载统一的人机任务池；
- GitHub Coding Agents 的实际权限与任务生命周期；
- 是否存在 Linux Foundation、OpenSSF、CHAOSS 等针对 AI 参与开源协作的新规范或治理实践；
- Human-Machine Teaming 标准后续版本变化。
