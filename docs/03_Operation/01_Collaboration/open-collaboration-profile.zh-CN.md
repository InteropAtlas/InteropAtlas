# InteropAtlas Open Collaboration / Human–AI Collaboration Profile v0.2

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification（草案 / 暂定规范）
Document Created At: 2026-09-01T11:35:22+08:00
Document Updated At: 2026-09-05T15:03:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Owner-authorized consolidation
  GitHub Actor: ff6962757
-->

> 状态：Draft / Provisional Specification（草案 / 暂定规范）
>
> 目的：定义 InteropAtlas 中 Human、AI / Agent、Reviewer、Maintainer 与 Automation 如何共享同一公开协作协议，包括任务合同、授权、租约式认领、交接、审核与依据复用。

## 1. 核心原则

- **Human-first, agent-compatible.** 同一公开任务协议允许不同执行者。
- 影响任务执行的稳定上下文进入 Repository Artifact、Issue 或 PR，不依赖私有聊天。
- Task Authority、Review Authority 与 GitHub Permission 是三个不同维度。
- Owner 负责方向、重大风险、权限边界和不可逆决策，不承担日常技术仪式化审批。
- Automation 提供 Evidence，不冒充独立 Reviewer identity。

## 2. Participant Roles

- **Steward / Project Maintainer**：Vision、scope、priority、重大方向与最终治理授权。
- **Task Author / Planner**：把 Goal 转换成 Human-ready / Agent-ready Work Item。
- **Executor / Contributor**：Human 或 Agent，负责执行已认领工作。
- **Reviewer / Overseer**：独立检查 Scope、Evidence、Specification 与语义判断。
- **Maintainer / Approver**：拥有相应 Merge / governance authorization。
- **Automation Infrastructure**：CI、Validator、Renderer、Bot、Scheduler；不是贡献者或 Reviewer 身份。

Executor MUST NOT 把 self-check 描述为 independent review。机器可充分验证的低至中风险任务可以用 executable evidence 完成，不得为了流程伪造 Human/Agent Reviewer。

## 3. Work Item Contract

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

### 3.1 Read First / Upstream Contracts

这是执行者必须遵守的 InteropAtlas 自身 Definition、Specification、Schema、Decision 或 Governance Artifact，属于**任务约束**。

### 3.2 Seed References

当 Task Author 已知 Atlas 中存在高度相关的 Standard、Mature Precedent、Method 或 Implementation 时，Work Item SHOULD 预装为 Seed References，并优先引用 Stable Atlas ID。

Seed References 是已知起点，不是封闭答案集。Executor MUST NOT 因此假定参考集合完整、最新或最佳。

Task Author SHOULD NOT 为了发布任务先替 Executor 完成整套研究；只需要提供明显关键的已知依据、上位规范与风险提示。

### 3.3 Freshness / Completeness Check

Standards research、prior-art、architecture、security、AI governance、Human Interface 等会随时间变化的任务 SHOULD 检查新版本、superseding artifact、新成熟先例和替代方案。

执行中发现新的标准、版本、先例、superseding relation 或 Model Gap 时 SHOULD 回流 Atlas / intake，而不是留在一次性任务上下文中。

## 4. Task Authority

### 4.1 Authority Classes

- **T0 — Open Contribution**：公开可认领的低风险研究、资料补充、测试、局部数据改进。
- **T1 — Trusted / Bounded Contribution**：跨文件一致性、批量数据、非破坏性代码、ordinary Canonical intake 等；需要 bounded scope 与验证路径。
- **T2 — Maintainer Technical Authority**：Canonical 模型、主线架构、核心 runtime/schema、迁移工具、任务系统等。受托 Maintainer / Agent 可在既定方向和安全边界内自主实施。
- **T3 — Owner / Governance Gate**：项目 Definition / Scope、License、Security、治理权限体系、Identity Merge/Split policy、破坏性 migration / major deletion / Legacy retirement、stable governance/specification promotion、formal Release 等重大或不可逆事项。

### 4.2 Delegation rule

T2 不等于逐项 Owner 技术签字；high-impact 标签也不机械等于 Owner review。是否升级取决于实际 mutation / decision 是否进入 T3。

机器可充分验证的 T0–T2 工作 MAY 以 tests、schema、Machine Review、graph、compatibility、CI 作为完成证据。语义判断无法充分机器验证时，优先 independent review 或显式 deferred / uncertain。

一旦执行发现会改变 Owner 已确定的大方向或进入 T3，MUST 停止并升级具体决策。

### 4.3 Capability / Trust Scope

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

## 5. Task Graph 与 Lifecycle

Issue SHOULD 是公开 Work Item 的默认 identity；大的 Work Package SHOULD 使用 parent Issue + Sub-issues，依赖 SHOULD 使用 GitHub-native dependency 表达。Roadmap 负责方向 / milestone；Issue graph 负责可执行任务。

```text
Draft → Ready → Claimed → In Progress → Review → Done
                         ├→ Blocked
                         └→ Handoff
Claimed / In Progress / Blocked / Handoff → Released → Ready
```

Draft 不可被自主当作 Ready。Ready 必须满足 Work Item Contract。

## 6. Lease-style Claim（租约式认领）

排他性执行任务在 `Claimed / In Progress` SHOULD 有一个 Primary Lease Holder。Claim MUST 在公共任务记录中可观察，并表达 holder、claim time、lease expiration/review time、current status。

Lease SHOULD 有限期；续租 SHOULD 伴随 Issue update、commit、Draft artifact、PR、blocker report 或 Handoff 等可观察进展。Lease 到期可以 Released 回 Ready，但已有工作不得丢失。

## 7. Handoff 与 Context Continuity

Agent/Human 退出任务前 SHOULD 留下可恢复的 Handoff：已完成内容、未完成内容、关键判断、证据、branch/PR/artifact、下一步和 blocker。

仓库级启动与中断恢复的完整合同由 [`Agent Onboarding / Context Continuity Profile`](agent-onboarding-context-continuity-profile.zh-CN.md) 负责；Open Collaboration 只规定任务级协作语义。

## 8. Review 与 Merge Boundary

PR SHOULD 对应可解释的 Work Item / bounded scope。Review 检查的不只是 diff，还包括：是否满足 Acceptance Criteria、Evidence 是否充分、Fact / Assessment 是否分离、是否越界。

普通机器可验证任务不强制制造 ceremonial reviewer；高影响语义或 T3 决策必须满足对应授权边界。

## 9. Research tasks

研究型任务继续由 [`Research Governance`](/docs/03_Operation/02_Governance/research-governance.zh-CN.md) 约束 Research Question、Depth、Stop Conditions、Evidence 与 R0–R3 escalation。本 Profile 只提供通用 Work Item / Reference Seeding / Authority 合同。

## 10. Current operational boundary

立即采用：

- 普通知识贡献、Candidate discovery、资料补充和 bounded intake 可以开放并行；
- Canonical Schema / Runtime / Migration 等主线技术工作由受托 Maintainer/Agent 在既定 V1 方向内推进；
- 项目 Definition、Scope、重大 Governance、License、Security、重大权限变化、破坏性 migration/retirement、stable promotion、formal Release 保持 Owner/Governance Gate；
- Owner 不承担自己无法实质验证的 ceremonial technical approval；
- Agent 不确定某决定是否改变大方向时，升级**该决策**，而不是把整个技术任务交回 Owner。

## 11. Primary Home consolidation

本 v0.2 已吸收原 `Task Authority Governance` 与 `Task Reference Seeding Profile` 的长期规则。它们不再作为独立 Living Documents 维护；历史由 Git history 保留。

后续任务协作、授权等级、Reference Seeding 与 Freshness 的规则只在本 Profile 维护一个 Primary Home。