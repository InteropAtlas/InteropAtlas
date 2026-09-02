# InteropAtlas Open Collaboration Route v0 — Notes

<!-- InteropAtlas Document Metadata v0
Document Status: Working Notes。用于把“人类 + Agent 共同建设 IA”从 Agent 工程问题重新放回开放协作问题中；不代表已经形成正式路线或规范。
Document Created At: 2026-09-01T09:41:39+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：Working Notes。用于把“人类 + Agent 共同建设 IA”从 Agent 工程问题重新放回开放协作问题中；不代表已经形成正式路线或规范。

## 核心定位

InteropAtlas 首先是开放的标准地图项目。人类贡献者与 AI / Agent 都属于协作参与者；CI、Renderer、测试、部署、调度等属于自动化基础设施。

```text
InteropAtlas
   ↓
开放协作系统
   ├── Human contributors
   └── AI / Agent contributors

Automation infrastructure
   └── 为上述参与者提供执行、测试、部署或调度能力
```

## 与现有五路线的关系

Open Collaboration 当前不单独替换五路线，而是重点补强 Curation / Contribution Route 与 Governance / Standardization Route 的“谁来做、如何协作、如何监督”部分。

## V0 只解决的最小问题

```text
Issue / Task
   ↓
Available
   ↓
一个主要执行者接手
   ↓
Work
   ↓
Pull Request
   ↓
独立 Review / Oversight
   ↓
Merge / Done
```

V0 暂不实现完整 Lease、Heartbeat、Agent 自动目标生成和多 Agent 讨论。

## 优先复用 GitHub 原生机制

当前 GitHub 已经提供足够多的协作原语，可以先验证 V0，而不急于开发 IA 自有任务系统：

- Issue：统一任务对象；
- Assignee：表示当前主要执行者，人类与支持的 Coding Agent 都可进入这一流程；
- Issue Fields / Projects：记录 Priority、Status、Area 等结构化状态；
- Sub-issues / Dependencies：拆分大任务并表达 blocked-by / blocking；
- Pull Request + Review：工作成果与独立审核；
- CODEOWNERS / Required Review：按领域自动请求有责任的 Reviewer；
- stale workflow：可用于提醒长期无进展任务，未来再根据真人 / Agent 形成不同释放策略。

因此 V0 的“租约式认领”暂时不需要实现独立 Lease 服务。第一阶段先把 `Assignee + Status + activity / stale` 当作近似机制，用真实协作验证哪些地方确实缺能力。

## 当前上位依据

- ISO/IEC CD 25589：Human-Machine Teaming framework；
- ISO/IEC AWI 25880：组织实施 Human-Machine Teaming；
- ISO/IEC CD TR 42109：Human-Machine Teaming use cases；
- ISO/IEC 5339:2024：stakeholder engagement；
- NIST AI RMF：human-AI roles / responsibilities / oversight；
- Linux Foundation AAIF / AGENTS.md：开放、跨 Agent 的仓库工作说明；
- GitHub Coding Agents：Issue → Agent → PR → Human Review 的现实实现。

详细见 `human-ai-open-collaboration-prior-art.zh-CN.md`。

## 当前暂定原则

- Human-first, agent-compatible；
- 人和 Agent 尽量使用同一公开协作流程；
- 执行、Review、最终授权不要默认集中在同一 Agent；
- 普通任务避免多个执行者重复工作；
- Agent 特有的 Lease / Heartbeat 是实现细节，不应改变普通贡献者对项目的理解；
- Roadmap 保持项目方向，Issues 保持可执行任务，不另造 Agent-only Goal / Task 系统；
- 先复用 GitHub 已有机制，只有真实实践证明不足时才新增 IA 自有协调能力。
