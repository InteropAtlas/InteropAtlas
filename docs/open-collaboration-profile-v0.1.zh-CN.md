# InteropAtlas Open Collaboration / Human–AI Collaboration Profile v0.1

> 状态：Draft / Provisional Specification（草案 / 暂定规范）
>
> 关联：Issue #19；输入包括 [`03_Evolution/01_Research/human-ai-open-collaboration-prior-art.zh-CN.md`](../03_Evolution/01_Research/human-ai-open-collaboration-prior-art.zh-CN.md) 与 [`03_Evolution/03_Change/open-collaboration-route-v0-notes.zh-CN.md`](../03_Evolution/03_Change/open-collaboration-route-v0-notes.zh-CN.md)。
>
> 目的：定义 InteropAtlas 中 Human、AI / Agent、Reviewer、Maintainer 与 Automation 如何共享同一公开协作协议。本文先定义角色、任务生命周期、租约式认领、交接、审核与授权语义；不在本文发布时创建 Lease Server、AGENTS.md、Issue Template 或 Project automation。

## 1. 规范关键词

本文中的 MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 按 BCP 14（RFC 2119 + RFC 8174）理解。

## 2. 上游依据与依据强度

本 Profile 没有可直接照搬的单一国际标准。它是上位 Human–Machine Teaming 原则、AI oversight 框架、GitHub 原生协作机制和开放 Agent 生态的组合 Profile。

| 上游依据 | 身份 / 状态 | 采用内容 | 依据强度 |
|---|---|---|---|
| ISO/IEC CD 25589 | Committee Draft，制定中 | Human–Machine Teaming 概念、角色关系、设计原则 | 上位标准化工作；**不可冒充已发布国际标准** |
| ISO/IEC 5339:2024 | 已发布 ISO/IEC 标准 | AI application lifecycle / stakeholder engagement 的组织视角 | 正式标准，上位原则 |
| NIST AI RMF 1.0 / Playbook | NIST Framework / guidance | 明确区分 human-AI roles、responsibilities、oversight | 强治理依据 |
| Linux Foundation AAIF / AGENTS.md | 开放基金会成熟先例 | 跨 Agent 的 repository-specific instructions | 开放生态先例 |
| GitHub Issues / Assignees / Sub-issues / Dependencies | 平台原生机制 | 公开任务池、主要执行者、任务图 | 强实现依据 |
| GitHub Issue Fields / Projects | 平台原生机制 | Status、Priority、Date 等结构化任务元数据 | 强实现依据 |
| GitHub Pull Requests / Reviews / CODEOWNERS / Rulesets | 平台原生机制 | 产物交付、独立 Review、合并保护 | 强实现依据 |
| InteropAtlas 自身实践 | 项目证据 | 聊天窗口隐式上下文不可扩展、重复“继续”效率低 | IA-specific evidence |

主要来源：
- ISO/IEC CD 25589: https://www.iso.org/standard/90831.html
- NIST AI RMF Core / Govern 3.2: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST Playbook: https://airc.nist.gov/airmf-resources/playbook/govern/
- AAIF / AGENTS.md: https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- GitHub Issues: https://docs.github.com/en/issues
- GitHub Sub-issues: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues
- GitHub Dependencies: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies
- GitHub Issue Fields: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields
- GitHub PR standardization: https://docs.github.com/en/pull-requests/reference/managing-and-standardizing-pull-requests
- GitHub Rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets

## 3. 核心定位

Open Collaboration 是 InteropAtlas 的 **cross-cutting operating layer（横向协作运行层）**，不是第六条知识系统主路线。

```text
InteropAtlas Public Work
       ↓
GitHub-visible Work Items / Artifacts
       ↓
┌───────────────────────────────────┐
│ Human contributors                │
│ AI / Agent contributors           │
└───────────────────────────────────┘
       ↓
Review / Oversight / Authorization
       ↓
Canonical Repository

Automation Infrastructure
= CI / Validator / Renderer / bot / scheduler
≠ contributor identity
```

原则：

> **Human-first, agent-compatible.**
>
> **同一公开任务协议，允许不同执行者。**

## 4. Participant Roles

角色是“职责”，不等同于账号类型。一个 Human 或 Agent MAY 在不同任务中承担不同角色，但高风险职责组合受到限制。

### 4.1 Steward / Project Maintainer（项目维护者 / 方向负责人）

负责：
- Vision / scope / priority；
- 接受或拒绝重大方向变更；
- Governance / Specification 的最终授权；
- 高风险 Merge / Release 决策。

### 4.2 Task Author / Planner（任务发布者 / 规划者）

负责把 Goal 转换成 Agent/Human 可执行的 Work Item，包括上下文、范围、交付物和验收条件。

### 4.3 Executor / Contributor（执行者 / 贡献者）

Human 或 Agent 都 MAY 承担。负责在 Claim 后完成任务范围内的研究、代码、数据或文档工作。

### 4.4 Reviewer / Overseer（审核者 / 监督者）

负责独立检查：
- 任务是否满足 Specification；
- Evidence 是否充分；
- Fact / Assessment 是否分离；
- 测试是否可信；
- 变更是否超出 Scope。

### 4.5 Maintainer / Approver（批准者）

拥有 Merge / governance authorization 权限。可与 Steward 重合。

### 4.6 Automation Infrastructure（自动化基础设施）

包括 CI、Validator、Renderer、Bots、Scheduler、Stale workflow。

Automation **MUST NOT** 被当作 Reviewer identity；测试通过是 Evidence，不是独立治理批准。

## 5. Role Separation

### IA-OC-001 — 执行与独立审核必须可区分

Executor **MUST NOT** 把自己的 self-check 描述成 independent review。

普通任务 **SHOULD** 至少由另一个 Human 或 Agent 进行 Review；高影响任务 **MUST** 由有相应授权的 Human Maintainer / Approver 最终批准。

### IA-OC-002 — 高影响任务保留 Human authorization

以下变更在 v0.1 **MUST** 有 Human Maintainer 最终授权：
- 项目核心定义 / Scope；
- Governance / Collaboration Profile；
- Canonical Schema 的破坏性变更；
- License / Security policy；
- stable Specification 状态升级；
- main branch protection / ruleset；
- 删除大量 Canonical Data；
- 对外正式 Release。

未来社区成熟后 MAY 重新 Profile。

Basis: NIST AI RMF role differentiation / oversight + current IA trust stage.

## 6. Work Item Contract

一个可被独立 Agent / Human 接手的任务，不应该依赖聊天窗口隐式上下文。

### IA-OC-003 — Agent-ready / Contributor-ready Work Item

标记为 `Ready` 的 Work Item **MUST** 至少包含：

1. **Objective** — 要达到什么结果；
2. **Why / Context** — 为什么需要；
3. **Read First / Upstream Contracts** — 必须读取的定义、Specification、Issue；
4. **Scope** — 允许修改 / 研究什么；
5. **Non-goals** — 明确本任务不做什么；
6. **Deliverables** — 需要提交哪些 Artifact；
7. **Acceptance Criteria** — 什么算完成；
8. **Evidence Requirements** — 哪些判断必须有来源；
9. **Review / Authorization Class** — 谁可以审核 / 批准；
10. **Dependencies / Blockers** — 前置任务。

任务 MAY 包含 Implementation Notes，但 **MUST NOT** 把某个 Agent 的私有提示词当成唯一任务合同。

### IA-OC-004 — 公共上下文优先

影响任务执行的稳定上下文 **SHOULD** 进入 Repository Artifact、Issue 或 PR，而不是只存在于 Chat / private memory。

## 7. Task Graph

### IA-OC-005 — Issue 是默认 Work Item identity

V0.1 **SHOULD** 使用 GitHub Issue 作为公开 Work Item 的默认身份。

大的 Work Package **SHOULD** 使用 parent Issue + Sub-issues 拆分；前置关系 **SHOULD** 使用 GitHub issue dependencies 表达，而不是把依赖关系只写在自然语言 Roadmap 中。

Basis: GitHub native sub-issues / dependencies.

### IA-OC-006 — Roadmap 与 Task Graph 分工

Roadmap 负责方向 / milestone；Issue graph 负责可执行任务。

项目 **MUST NOT** 另建一个只有 Agent 使用、与 GitHub Issues 不同步的 Goal / Task source of truth。

## 8. Task Lifecycle

V0.1 采用以下语义状态：

```text
Draft
  ↓
Ready
  ↓ claim
Claimed
  ↓ first substantive work
In Progress
  ├──→ Blocked
  ├──→ Handoff
  └──→ Review
Review
  ├──→ Changes Requested → In Progress
  └──→ Approved → Done

Claimed / In Progress / Blocked / Handoff
  └──→ Released → Ready
```

### 状态定义

- **Draft**：任务还不够清楚，不可自主领取；
- **Ready**：满足 IA-OC-003，可被认领；
- **Claimed**：任务已由一个主要执行者获得排他性工作权；
- **In Progress**：已有可观察的实质工作；
- **Blocked**：执行者仍持有任务，但存在外部阻塞；
- **Handoff**：当前执行者准备把工作上下文交给其他执行者；
- **Review**：执行产物已提交，等待独立审核；
- **Done**：满足 Acceptance 且获得所需批准；
- **Released**：Claim 失效或主动释放，任务重新回到 Ready。

## 9. Lease-style Claim（租约式认领）

### 9.1 为什么不是永久 Assignee

传统 Assignee 只能说明“现在谁负责”，不能自然表达：
- 是否仍然活跃；
- 多久后可以安全释放；
- Agent 失联时怎样避免任务永久占用；
- 认领是否排他。

因此 IA 在 GitHub Assignee 之上定义**语义租约**。

### IA-OC-007 — 普通执行任务默认单一主 Lease Holder

一个排他性执行任务在 `Claimed / In Progress` 状态 **SHOULD** 有一个 Primary Lease Holder。

多人协作 MAY 有 collaborators，但 **SHOULD** 明确一个主要负责者，避免两个 Agent 无意做同一份工作。

### IA-OC-008 — Claim 必须可观察

Claim **MUST** 在公共任务记录中可观察，并至少包含：
- holder identity；
- claim time；
- lease expiration / review time；
- current status。

### IA-OC-009 — Lease 必须有限期

Agent 或 Human 对排他性任务的 Claim **SHOULD** 是有限期租约，而不是永久所有权。

v0.1 不规定统一时长；不同任务类别 MAY 采用不同 Lease Policy。

### IA-OC-010 — Lease renewal 必须有进展证据

续租 **SHOULD** 伴随至少一种可观察进展：
- Issue update；
- branch / commit；
- Draft artifact；
- PR；
- blocker report；
- Handoff record。

仅“仍在处理”不应无限期占用任务。

### IA-OC-011 — Lease expiration 不等于删除工作

Lease 到期时任务 MAY 被 Released 回 Ready；已有 branch、commit、notes、PR **MUST NOT** 因释放而丢失。

新执行者 **SHOULD** 先读取已有 Handoff / Artifact 再继续。

### 9.2 GitHub-native V0 Mapping

Profile 建议的第一实现：

| 协作语义 | GitHub 原生映射 |
|---|---|
| Task identity | Issue |
| Primary Lease Holder | Assignee |
| Lifecycle | Issue Field / Project Status |
| Lease expiration | Public Date field `Lease Until`（优先）或结构化 Issue metadata fallback |
| Priority | Issue field / label |
| Parent work package | Parent Issue / Sub-issue |
| Dependency | blocked-by / blocking |
| Work product | branch / commit / PR / repository artifact |
| Review | PR Review |
| Ownership routing | CODEOWNERS |
| Required authorization | Ruleset / Required Review |
| Inactivity reminder | GitHub Action / bot（后续实现） |

GitHub 已支持 public issue fields（包括 date-like structured metadata）与 Projects；因此 V0 **SHOULD** 优先 Profile 这些原语，而不是建立独立任务数据库。

## 10. Handoff / Continuity

### IA-OC-012 — Handoff 必须显式记录

Human ↔ Agent、Agent ↔ Agent、Human ↔ Human 交接 **MUST** 使用同一个最小 Handoff Contract。

Handoff 至少包括：
1. 当前任务状态；
2. 已完成内容；
3. 已修改 / 新增 Artifact；
4. 已验证内容；
5. 未完成内容；
6. blockers / open questions；
7. 推荐 next action；
8. 当前 branch / PR / commit（如有）。

### IA-OC-013 — Handoff 不能只存在于聊天摘要

对长期项目有价值的 Handoff **MUST** 进入 Issue、PR 或 repository artifact；Chat summary MAY 作为输入，但不得成为唯一可恢复状态。

## 11. Review / Oversight

### IA-OC-014 — PR 是可合并产物的默认 Review boundary

会改变 Canonical Repository 的工作 **SHOULD** 通过 Pull Request 进入独立 Review，而不是执行者直接把“完成”当作“批准”。

当前 ChatGPT connector 对 main 的直接编辑是 Bootstrap 阶段例外；Open Collaboration 实施后 **SHOULD** 逐渐切换到 branch / PR workflow。

### IA-OC-015 — Review 必须针对上位合同

Reviewer **SHOULD** 根据 Task Acceptance + Upstream Specification / Schema / Evidence requirements 审核，而不是只评价“看起来不错”。

### IA-OC-016 — 自动检查是 Review Evidence，不是 Reviewer

CI、Validator、E2E、link checker 等输出 **SHOULD** 成为 Review Evidence；它们 **MUST NOT** 被描述成独立人类/Agent Review。

### IA-OC-017 — 高风险区域 SHOULD 通过 ownership / ruleset 自动路由

Repository Structure Profile 定义的高风险区域（例如 `01_State` 中的 Schema / Contract、stable specifications、security / licensing，以及其他会影响全项目合同的文件）**SHOULD** 在实施阶段映射到 CODEOWNERS / Required Review / Rulesets。

## 12. AI / Agent Contribution Transparency

### IA-OC-018 — Agent 参与应可追踪，但不绑具体厂商

当主要工作由 Agent 执行时，Work Item / PR **SHOULD** 能识别：
- execution mode: human / agent / mixed；
- responsible human or account（如适用）；
- Agent/tool identity MAY 记录，但不得成为流程兼容的必要条件。

流程 **MUST NOT** 只支持 ChatGPT / Codex / Claude / Copilot 等某一个产品。

### IA-OC-019 — Agent 不得继承未公开的永久项目秘密上下文

Agent-ready task **SHOULD** 假设新的执行者只能读取公开 repository / Issue / permitted connected context。

如果任务必须依赖私人聊天记忆才能正确执行，该任务 **MUST NOT** 标记为 fully Ready。

## 13. AGENTS.md Boundary

### IA-OC-020 — AGENTS.md 的职责受限

未来 `AGENTS.md` **SHOULD** 只保存 Agent 执行仓库工作时需要的 repository-specific instructions，例如：
- read-first files；
- validation commands；
- generated-file policy；
- formatting / test rules；
- forbidden direct edits；
- task / PR protocol pointers。

AGENTS.md **MUST NOT**：
- 重新定义项目 Vision；
- 替代 CONTRIBUTING；
- 隐藏 Human 不可见的治理规则；
- 绑定单一 Agent vendor；
- 成为 Task source of truth。

Basis: AAIF / AGENTS.md role + Human-first principle.

## 14. Task Authoring Profile

为了把用户从“每轮写 Prompt”转变为“发布工作”，Task Authoring SHOULD 使用统一结构。

推荐 Task Template：

```text
Title

Objective
Why / Context

Read First
- Definition / Specification / Issue

Scope
- allowed work

Non-goals
- explicitly excluded work

Deliverables
- artifacts / data / code / report

Evidence Requirements
- official sources / test evidence

Acceptance Criteria
- observable completion conditions

Review Class
- normal / high-impact
- required reviewer / approver

Dependencies
- blocked by / parent

Lease Policy
- exclusive? yes/no
- lease duration / review date
```

这个结构同时适用于 Human 与 Agent；Agent-specific prompt MAY 由执行环境生成，但不是项目合同本体。

## 15. Open Gap：GitHub 原生机制目前缺什么？

当前 Profile 判断 GitHub 原生能力已经足够覆盖 V0 的大部分语义：Issue、Assignee、Fields、Sub-issues、Dependencies、PR、Review、CODEOWNERS、Rulesets。

仍需真实试运行验证的潜在缺口：

1. **自动 Lease expiration / release**：GitHub 原生 Assignee 不会自动过期；
2. **Heartbeat / liveness**：没有通用 Human/Agent heartbeat contract；
3. **跨不同 Agent 平台统一 claim API**；
4. **Agent identity / provenance 的跨平台统一表示**；
5. **自动匹配 Ready Task 与 Agent capability**；
6. **并发任务冲突检测**（两个不同 Issue 修改同一敏感 Artifact）。

这些当前都是 **candidate gaps**，不是开发需求。

只有 2–3 个真实任务试运行后仍反复出现，才进入 `Extend / Invent`。

## 16. V0 Implementation Sequence

本 Profile 完成后，实施 SHOULD 按以下顺序：

```text
1. CONTRIBUTING 重写
2. Issue / PR Task Templates
3. GitHub Project / Issue Fields
4. CODEOWNERS / Required Review / Ruleset
5. AGENTS.md
6. 选择 2–3 个真实任务
7. Human / Agent claim + lease 试运行
8. 记录 friction / gaps
9. 只对真实缺口增加 automation
```

这部分属于下一个 Work Package，不在 Profile A 中执行。

## 17. Conformance Checklist

一个任务被标记为 `Ready` 前：

- [ ] Objective 清楚；
- [ ] Upstream Specification / Read First 明确；
- [ ] Scope / Non-goals 清楚；
- [ ] Deliverables 可观察；
- [ ] Acceptance Criteria 可验证；
- [ ] Evidence 要求明确；
- [ ] Dependencies 已表达；
- [ ] Review / Authorization class 已明确；
- [ ] 不依赖私人聊天记忆才能理解。

一个任务被标记为 `Done` 前：

- [ ] Deliverables 已进入公共 Artifact / PR；
- [ ] Acceptance Criteria 已满足；
- [ ] CI / Validator 等 Evidence 已记录；
- [ ] Independent Review 已完成；
- [ ] 高影响任务已获得 Human Maintainer approval；
- [ ] Handoff / residual work 已进入后续 Issue（如需要）。

## 18. v0.1 结论

InteropAtlas 的目标协作模式从：

```text
Maintainer ↔ Chat assistant
逐轮对话推动仓库
```

转向：

```text
Vision / Specification
       ↓
Agent-ready / Human-ready Work Items
       ↓
Ready Task Pool
       ↓
Lease-style Claim
       ↓
Independent Execution
       ↓
Public Artifact / Pull Request
       ↓
Independent Review / Oversight
       ↓
Maintainer Authorization where required
       ↓
Merge / Done / Handoff
```

核心不是让 Agent 获得特殊工作流，而是让**同一个开放协作协议足够明确，使 Human 和 Agent 都能独立进入并恢复工作。**