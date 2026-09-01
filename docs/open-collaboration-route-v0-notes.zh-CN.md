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

## 机器可发现性与外部 Agent 参与

这是一个重要的长期方向，但当前只记录，不立即展开实现。

目标不只是让人类在 GitHub 上发现 InteropAtlas，还要让其他 AI / Agent 在执行标准检索、技术调研或互操作相关任务时有机会发现 IA，并明确知道：

- InteropAtlas 是一个开放、可贡献的项目；
- Agent 可以提交发现的问题、缺失标准、改进建议和研究结果；
- 条件允许时，Agent 可以进一步参与 Issue、PR、Review 等正常贡献流程；
- 项目应尽量采用跨 Agent 可识别的公开元数据、说明文件和贡献入口，而不是只对某一种 Agent 产品可见。

长期希望形成：

```text
外部 Agent 执行自己的任务
        ↓
发现 InteropAtlas
        ↓
识别 IA 与当前任务相关
        ↓
读取贡献说明 / Agent instructions
        ↓
提交反馈、Issue、研究结果或 PR
        ↓
进入 IA 正常 Review 流程
```

这个方向暂不等同于“无条件利用外部 Agent 的闲置算力”。权限、授权、身份、滥用防护、质量控制和资源激励都需要后续单独研究。当前只把“可发现 + 可贡献”作为前中期需要保留的重要能力目标。

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
