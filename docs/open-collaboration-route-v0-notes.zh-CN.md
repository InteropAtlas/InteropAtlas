# InteropAtlas Open Collaboration Route v0 — Notes

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

## 当前上位依据

- ISO/IEC CD 25589：Human-Machine Teaming framework；
- ISO/IEC AWI 25880：组织实施 Human-Machine Teaming；
- ISO/IEC CD TR 42109：Human-Machine Teaming use cases；
- ISO/IEC 5339:2024：stakeholder engagement；
- NIST AI RMF：human-AI roles / responsibilities / oversight；
- GitHub Coding Agents：Issue → Agent → PR → Human Review 的现实实现。

详细见 `human-ai-open-collaboration-prior-art.zh-CN.md`。

## 当前暂定原则

- Human-first, agent-compatible；
- 人和 Agent 尽量使用同一公开协作流程；
- 执行、Review、最终授权不要默认集中在同一 Agent；
- 普通任务避免多个执行者重复工作；
- Agent 特有的 Lease / Heartbeat 是实现细节，不应改变普通贡献者对项目的理解；
- Roadmap 保持项目方向，Issues 保持可执行任务，不另造 Agent-only Goal / Task 系统。
