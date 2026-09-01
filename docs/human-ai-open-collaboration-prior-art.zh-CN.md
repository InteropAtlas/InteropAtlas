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

### ISO/IEC Human-Machine Teaming 系列

当前最直接的三项工作都由 ISO/IEC JTC 1/SC 42 推进，但仍处于制定阶段：

- ISO/IEC CD 25589 — Framework for human-machine teaming：建立 Human-Machine Teaming 的概念、术语、关系描述、技术特征和设计原则；
- ISO/IEC AWI 25880 — Organizational implementation of human-machine teaming：面向组织实际实施 Human-Machine Teaming；
- ISO/IEC CD TR 42109 — Use cases of human-machine teaming：收集和整理 Human-Machine Teaming 用例。

对 IA 的意义：这组标准适合作为“人和 Agent 如何组成团队”的上位依据，但目前不能直接提供 GitHub Issue 领取、Lease、PR Review 等仓库级机制。尤其 ISO/IEC 25880 值得持续跟踪，因为 IA 真正需要解决的是“一个开放组织怎样把人和 Agent 放进同一协作流程”。

## 已发布的支撑标准 / 框架

### ISO/IEC 5339:2024 + NIST AI RMF

ISO/IEC 5339 强调 AI 应用生命周期中的 stakeholder engagement 和多方沟通；NIST AI RMF 则更具体地要求区分 human-AI configuration 中的角色、责任、沟通和 human oversight，并区分使用 AI 的人和监督 AI 的人。

对 IA 的直接启示是：执行者、Reviewer / Overseer、治理者应明确区分。项目不能只从 Agent 开发者视角设计协作流程，也不应默认让同一 Agent 同时拥有执行、审核和最终授权。

## Linux Foundation：Agent 开源协作正在快速形成

2025 年 Linux Foundation 成立 Agentic AI Foundation（AAIF），以中立、开放治理方式推动 Agentic AI 的开放协议、工具和实践。首批项目包括 MCP、goose 和 AGENTS.md。

其中 **AGENTS.md** 与 IA 特别相关：它提供一个面向 Coding Agent 的、可由仓库自己维护的开放说明格式，相当于“给 Agent 的 README”。这证明“让仓库自己保存 Agent 工作规则，并由不同 Agent 共同读取”已经开始形成跨工具的开放约定，而不是 IA 独有想法。

2026 年 Linux Foundation TODO Group 又成立了 **Agentic AI to Empower OSPOs Working Group**，专门研究 Agent 如何进入开源项目管理、合规、开发者体验和上游协作。这一工作组虽然还没有形成正式国际标准，但它和 IA 的“人 + Agent 共建开源项目”问题高度重合，应作为持续 Prior Art 来源。

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

因此 IA 后续更合适的路线不是从零发明 Human-AI Teaming 理论，而是：

```text
ISO / NIST 上位原则
        +
Linux Foundation / AGENTS.md 的开放 Agent 生态
        +
GitHub / 开源社区现实实践
        ↓
IA Open Collaboration Profile
```

## 对 IA V0 的暂定约束

在进一步研究完成前，只保留以下轻量方向：

1. AI / Agent 属于协作参与者，不属于项目本体，也不等同于自动化基础设施；
2. 人和 Agent 尽量共享 GitHub Issues / PR / Review 这套公开协作流程；
3. 普通任务默认一个主执行者，避免重复劳动；Review / Oversight 与执行角色分离；
4. 仓库规则优先采用开放、跨 Agent 可读的形式，优先研究 AGENTS.md，而不是绑定单一 Agent 产品；
5. Lease、Heartbeat、Agent 自动选任务等属于后续实现机制，不先写成项目根本结构；
6. 持续跟踪 ISO/IEC 25589 / 25880、AAIF 和 TODO Group 的演进，再调整 IA Profile。

## 重点来源

- ISO/IEC 25589: https://www.iso.org/standard/90831.html
- ISO/IEC 25880: https://www.iso.org/standard/91833.html
- ISO/IEC TR 42109: https://www.iso.org/standard/88243.html
- ISO/IEC 5339: https://www.iso.org/standard/81120.html
- NIST AI RMF: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- Agentic AI Foundation: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- AGENTS.md: https://github.com/agentsmd/agents.md
- Linux Foundation TODO Group Agentic AI WG: https://www.linuxfoundation.org/blog/todo-group-launches-new-working-group-on-agentic-ai-to-empower-open-source-program-offices
- GitHub Coding Agents: https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents

## 后续 Prior Art

下一轮优先研究开源项目已有的任务分配、stale / reassignment、review / CODEOWNERS 等机制，判断 GitHub Issues / Projects 本身能否成为 IA 统一的人机任务池；同时继续观察 AAIF / TODO Group 是否开始形成更明确的人机协作治理规范。
