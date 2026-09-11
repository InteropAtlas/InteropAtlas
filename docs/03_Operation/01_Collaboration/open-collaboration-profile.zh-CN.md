# InteropAtlas Open Collaboration / Human–AI Collaboration Profile v0.3

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification（草案 / 暂定规范）
Document Created At: 2026-09-01T11:35:22+08:00
Document Updated At: 2026-09-05T17:10:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：Draft / Provisional Specification（草案 / 暂定规范）
>
> 目的：定义 InteropAtlas 中 Human、AI / Agent、Reviewer、Maintainer 与 Automation 如何共享同一公开协作协议，包括 GitHub 原生协作层、任务合同、授权、租约式认领、交接、审核与依据复用。

## 1. 核心原则

- **Human-first, agent-compatible.** 同一公开任务协议允许不同执行者。
- 影响任务执行的稳定上下文进入 Repository Artifact、Issue、Discussion、Project 或 PR，不依赖私有聊天。
- Task Authority、Review Authority 与 GitHub Permission 是三个不同维度。
- Owner 负责方向、重大风险、权限边界和不可逆决策，不承担日常技术仪式化审批。
- Automation 提供 Evidence，不冒充独立 Reviewer identity。
- **GitHub 原生协作能力优先于在 Repository 中重新造工作管理结构。**

## 2. GitHub 原生协作层（GitHub-native Collaboration Layer）

InteropAtlas 把 GitHub 不只视为代码托管平台，也视为公开项目的协作运行层。Repository 与 GitHub 原生协作面承担不同职责：

```text
开放探索 / 社区问题
→ Discussions

明确可执行工作
→ Issues

多个 Work Item 的组织、状态、优先级与进度视图
→ Projects

实际变更、交付与 Review
→ Branch / Pull Request

自动验证、构建与例行操作
→ Actions

安全、依赖、代码与供应链质量控制
→ Security / Code Quality capabilities

Human / Agent 执行
→ 共享上述同一公开任务与权限体系

长期有效结果
→ Repository: State / Runtime / Evolution / docs
```

### 2.1 Discussions — 开放问题与形成共识

Discussion 适合尚未收敛为明确 Work Item 的开放问题、方向探索、社区问答、方案讨论和经验交流。

当 Discussion 已经形成明确 Objective、Scope、Deliverables 与 Acceptance Criteria 时，SHOULD 转化或引用到 Issue；不要让长期可执行任务只存在于开放讨论中。

重要长期结论如果成为项目正式规则、架构或 durable rationale，仍应进入对应 Repository Primary Home；Discussion 本身保留讨论过程，不成为第二套规范事实源。

### 2.2 Issues — Work Item 的默认身份

Issue 是公开 Activity / Task / bounded Research / Maintenance Work Item 的默认 identity。

小活动不会因为存在就创建 Repository 文件夹；多日研究也不会仅因为被称作 Project 就获得仓库项目目录。是否进入 Repository 取决于最终 Durable Output，而不是工作持续时间。

### 2.3 Projects — 工作组合与进度视图

GitHub Projects 负责多个 Issue / PR 的组织、状态、优先级、负责人、依赖与阶段视图。

Project **不是第二套 Work Item 数据源**：Issue / PR 保持任务与交付 identity，Project 只组织和投影视图。

长期 Roadmap / project direction 仍由正式 Living Documents 负责；实时施工状态由 Project + Issue / PR 负责，避免把实时任务表复制进 Repository 文档。

### 2.4 Pull Requests — 变更与交付边界

PR 负责把一个 bounded Work Item 变成可审查的实际变更。重大长期决策可以由 PR 引用 Evolution Decision / Living Specification，但 PR 本身不替代正式 Primary Home。

### 2.5 Actions — Automation / Verification Infrastructure

Actions 负责 CI、Validator、Machine Review、link / schema / graph checks、生成任务与其他可机械执行流程。

Action PASS 是 Verification Evidence，不是 semantic review、Owner approval 或独立 Reviewer identity。

### 2.6 Security / Quality — 技术强制与风险控制层

Repository security、dependency、code scanning、secret protection、ruleset / branch protections 等能力属于技术强制层。

它们 SHOULD 随真实风险逐步启用，用于防止秘密泄露、依赖风险、代码缺陷、供应链问题和越权变更；但不得把平台技术权限等同于 Task Authority 或 Review Authority。

### 2.7 Wiki — 可选解释层，不是第二事实源

Wiki MAY 用于面向社区的教程、FAQ、导览和非规范性解释，但 SHOULD NOT 复制 `docs/`、Canonical State 或其他 Primary Home 的完整正式内容。

若启用 Wiki 作为长期入口，必须清楚声明规范与事实 Source of Truth 位于 Repository 对应 Primary Home，并尽量链接而不是复制。

### 2.8 Agent — Executor，不是独立治理层

GitHub 或其他平台提供的 Agent 能力，本质上属于 Executor / Automation capability，而不是第五种治理 authority。

Agent 仍必须遵守同一 Work Item Contract、Task Authority、Review Boundary、Canonical intake 与 Owner / Governance Gate；不得因为平台提供“Agent”入口就获得额外语义权限。

## 3. Participant Roles

- **Steward / Project Maintainer**：Vision、scope、priority、重大方向与最终治理授权。
- **Task Author / Planner**：把 Goal 转换成 Human-ready / Agent-ready Work Item。
- **Executor / Contributor**：Human 或 Agent，负责执行已认领工作。
- **Reviewer / Overseer**：独立检查 Scope、Evidence、Specification 与语义判断。
- **Maintainer / Approver**：拥有相应 Merge / governance authorization。
- **Automation Infrastructure**：CI、Validator、Renderer、Bot、Scheduler；不是贡献者或 Reviewer 身份。

Executor MUST NOT 把 self-check 描述为 independent review。机器可充分验证的低至中风险任务可以用 executable evidence 完成，不得为了流程伪造 Human/Agent Reviewer。

## 4. Work Item Contract

标记为 `Ready` 的 Work Item MUST 至少表达：

```text
Objective
Why / Context
Read First / Upstream Contracts
Scope
Non-goals
Deliverables
Acceptance Criteria
Evidence Requirements
Seed References（已知时）
Freshness / Completeness Check（适用时）
Task Authority Class
Eligible Executors / Required Capability（需要限制时）
Review / Authorization Class
Dependencies / Blockers
```

### 4.1 Read First / Upstream Contracts

这是执行者必须遵守的 InteropAtlas 自身 Definition、Specification、Schema、Decision 或 Governance Artifact，属于**任务约束**。

### 4.2 Seed References

当 Task Author 已知 Atlas 中存在高度相关的 Standard、Mature Precedent、Method 或 Implementation 时，Work Item SHOULD 预装为 Seed References，并优先引用 Stable Atlas ID。

Seed References 是已知起点，不是封闭答案集。Executor MUST NOT 因此假定参考集合完整、最新或最佳。

Task Author SHOULD NOT 为了发布任务先替 Executor 完成整套研究；只需要提供明显关键的已知依据、上位规范与风险提示。

### 4.3 Freshness / Completeness Check

Standards research、prior-art、architecture、security、AI governance、Human Interface 等会随时间变化的任务 SHOULD 检查新版本、superseding artifact、新成熟先例和替代方案。

执行中发现新的标准、版本、先例、superseding relation 或 Model Gap 时 SHOULD 回流 Atlas / intake，而不是留在一次性任务上下文中。

## 5. Task Authority

### 5.1 Authority Classes

- **T0 — Open Contribution**：公开可认领的低风险研究、资料补充、测试、局部数据改进。
- **T1 — Trusted / Bounded Contribution**：跨文件一致性、批量数据、非破坏性代码、ordinary Canonical intake 等；需要 bounded scope 与验证路径。
- **T2 — Maintainer Technical Authority**：Canonical 模型、主线架构、核心 runtime/schema、迁移工具、任务系统等。受托 Maintainer / Agent 可在既定方向和安全边界内自主实施。
- **T3 — Owner / Governance Gate**：项目 Definition / Scope、License、Security、治理权限体系、Identity Merge/Split policy、破坏性 migration / major deletion / Legacy retirement、stable governance/specification promotion、formal Release 等重大或不可逆事项。

### 5.2 Delegation rule

T2 不等于逐项 Owner 技术签字；high-impact 标签也不机械等于 Owner review。是否升级取决于实际 mutation / decision 是否进入 T3。

机器可充分验证的 T0–T2 工作 MAY 以 tests、schema、Machine Review、graph、compatibility、CI 作为完成证据。语义判断无法充分机器验证时，优先 independent review 或显式 deferred / uncertain。

一旦执行发现会改变 Owner 已确定的大方向或进入 T3，MUST 停止并升级具体决策。

### 5.3 Capability / Trust Scope

授权按能力域理解，而不是单轴人员等级，例如：Research/Prior-art、Canonical Data、Schema/Knowledge Modeling、Runtime/Code、Documentation、Product/UX、Governance/Collaboration、Release/Security。

一个执行者在某领域具备技术能力，不自动获得另一个领域的治理权限。

需要时 Work Item SHOULD 表达：

```text
Task Authority Class: T0 | T1 | T2 | T3
Eligible Executors: public | trusted-contributors | team:<name> | maintainers | owner-approved
Required Capability: research | schema | data | runtime | governance | ...
Claim Approval: none | maintainer | owner
Review Class: normal | high-impact
```

T3 必须 Owner/Governance 授权。T2 在明确受托且没有跨越 T3 边界时，不要求逐项 Owner Claim Approval。

GitHub roles、Teams、CODEOWNERS、branch protection 和 rulesets 是技术强制层，不等同于任务语义；只按真实协作摩擦逐步增加，不提前构建复杂权限系统。

## 6. Task Graph 与 Lifecycle

Issue SHOULD 是公开 Work Item 的默认 identity；大的 Work Package SHOULD 使用 parent Issue + Sub-issues，依赖 SHOULD 使用 GitHub-native dependency 表达。GitHub Project 负责跨 Work Item 的实时组织与投影视图；长期 Roadmap 负责方向，不复制实时任务状态。

```text
Draft → Ready → Claimed → In Progress → Review → Done
                         ├→ Blocked
                         └→ Handoff
Claimed / In Progress / Blocked / Handoff → Released → Ready
```

Draft 不可被自主当作 Ready。Ready 必须满足 Work Item Contract。

## 7. Lease-style Claim（租约式认领）

排他性执行任务在 `Claimed / In Progress` SHOULD 有一个 Primary Lease Holder。Claim MUST 在公共任务记录中可观察，并表达 holder、claim time、lease expiration/review time、current status。

Lease SHOULD 有限期；续租 SHOULD 伴随 Issue update、commit、Draft artifact、PR、blocker report 或 Handoff 等可观察进展。Lease 到期可以 Released 回 Ready，但已有工作不得丢失。

## 8. Handoff 与 Context Continuity

Agent/Human 退出任务前 SHOULD 留下可恢复的 Handoff：已完成内容、未完成内容、关键判断、证据、branch/PR/artifact、下一步和 blocker。

仓库级启动与中断恢复的完整合同由 [`Agent Onboarding / Context Continuity Profile`](agent-onboarding-context-continuity-profile.zh-CN.md) 负责；Open Collaboration 只规定任务级协作语义。

## 9. Review 与 Merge Boundary

PR SHOULD 对应可解释的 Work Item / bounded scope。Review 检查的不只是 diff，还包括：是否满足 Acceptance Criteria、Evidence 是否充分、Fact / Assessment 是否分离、是否越界。

普通机器可验证任务不强制制造 ceremonial reviewer；高影响语义或 T3 决策必须满足对应授权边界。

## 10. Research tasks

研究型任务继续由 [`Research Governance`](/docs/03_Operation/02_Governance/research-governance.zh-CN.md) 约束 Research Question、Depth、Stop Conditions、Evidence 与 R0–R3 escalation。本 Profile 只提供通用 Work Item / Reference Seeding / Authority 合同。

## 11. Current operational boundary

立即采用：

- 普通知识贡献、Candidate discovery、资料补充和 bounded intake 可以开放并行；
- Canonical Schema / Runtime / Migration 等主线技术工作由受托 Maintainer/Agent 在既定 V1 方向内推进；
- 项目 Definition、Scope、重大 Governance、License、Security、重大权限变化、破坏性 migration/retirement、stable promotion、formal Release 保持 Owner/Governance Gate；
- Owner 不承担自己无法实质验证的 ceremonial technical approval；
- Agent 不确定某决定是否改变大方向时，升级**该决策**，而不是把整个技术任务交回 Owner；
- 新的开放讨论优先进入 Discussions（启用后）；明确工作进入 Issues；跨任务实时组织进入 Projects；不要为这些工作状态在 Repository 复制第二套目录或清单。

## 12. Primary Home consolidation

本 v0.3 继续以单一 Profile 维护 Open Collaboration、Task Authority、Reference Seeding 与 GitHub-native collaboration surface 的长期规则。

平台具体 UI、字段、自动化和安全开关可以随 GitHub 能力演化，但上述职责边界不因 UI 名称变化而分裂出第二套项目状态。