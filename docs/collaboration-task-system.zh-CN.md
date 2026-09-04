# InteropAtlas Collaboration Task System v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Pilot Operational Profile
Document Created At: 2026-09-01T12:42:42+08:00
Document Updated At: 2026-09-04T14:55:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: verification-evidence / Owner-directed governance clarification
  GitHub Actor: ff6962757
-->

> 状态：Pilot Operational Profile
>
> Parent Work Package：#22
>
> 上位规范：`docs/open-collaboration-profile.zh-CN.md`
>
> Context Continuity：`docs/agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`
>
> Research Tasks：`docs/research-governance-v0.1.zh-CN.md`

本文把 Open Collaboration Profile 映射成当前仓库可直接执行的 GitHub 工作协议。它不建立第二套任务数据库；GitHub Issue 仍是 Work Item source of truth。

## 1. Work Item 必备结构

一个任务只有在以下信息足够完整时才能标记为 `Ready`：Objective、Why / Context、Read First、Scope、Non-goals、Deliverables、Evidence Requirements、Acceptance Criteria、Review Class、Dependencies 和 Lease Policy。Research Work Item 另外遵守 `docs/research-governance-v0.1.zh-CN.md`。

## 2. V0 Task Metadata

```text
Status: Ready
Primary Lease Holder: —
Claimed At: —
Lease Until: —
Execution Mode: human | agent | mixed | unassigned
Review Class: normal | high-impact
Parent: #<issue> | —
Blocked By: #<issue> | —
```

未来配置 Project Fields 后，这些字段 SHOULD 迁移到原生 fields；Issue body 可保留可读镜像，但不得形成两个冲突状态源。

## 3. Lifecycle

```text
Draft → Ready → Claimed → In Progress → Review → Done
                         ↘ Blocked
                         ↘ Handoff
Claimed / In Progress / Blocked / Handoff → Released → Ready
Review → Changes Requested → In Progress
```

状态变化必须在 Issue 中公开可观察。

## 4. Claim / Lease

排他任务需要公开 Claim、Primary Lease Holder、Claimed At、Lease Until。Pilot 默认首次 Lease review window 为 72 小时。续租必须伴随可观察进展。长期可恢复信息必须进入 Issue、PR 或 repository artifact。

## 5. Handoff / Continuity

Handoff 至少记录 Completed、Artifacts、Validated、Remaining、Blockers、Recommended next action、current branch/PR/commit。

如果任务改变 Phase、主线 Work Item、Resume Here、Gate 或重大项目方向，SHOULD 同步 `PROJECT_STATE.md`。

新会话在用户只说“继续”时：

```text
AGENTS.md
↓
PROJECT_STATE.md
↓
验证 Project State 新鲜度
↓
检查 Resume Here 对应 Issue / PR
↓
恢复第一项尚未完成的主线工作
```

## 6. Review policy — risk-driven, evidence-first

Review 的目的是真正降低错误风险，不是制造形式上的第二签字。

### 6.1 Mechanically verifiable technical work

当普通技术实现同时满足以下条件时，Executor MAY 基于可重复执行的证据完成任务，而不强制另找 Human/Agent 做 ceremonial independent review：

- 不改变项目定义、V1 方向或 Scope；
- 不扩大 Agent / Contributor 权限或 Canonical acceptance authority；
- 不涉及 identity merge/split、破坏性迁移、重大删除、Legacy retirement、stable promotion、License/Security/Release；
- Acceptance Criteria 可以被 deterministic tests / schema validation / Machine Review / graph checks / compatibility checks / CI 等充分验证；
- 验证实际执行并留下公开证据；
- Executor 明确记录 self-check / evidence，并且不伪造不存在的 Reviewer。

这种情况下，CI / Validator 是 **Verification Evidence**。它仍不是一个 Human/Agent Reviewer，但任务也不因为缺少形式化 Reviewer 而自动阻塞。

### 6.2 Semantic / judgment-heavy work

当正确性无法由机器充分判定，例如语义归类、证据解释、争议事实、identity ambiguity、复杂知识建模，SHOULD 使用与 Executor 不同的 Human 或 Agent 做 independent review；如果没有 Reviewer，可以保留明确 uncertainty / deferred 状态，而不是伪造批准。

### 6.3 Governance / irreversible high-impact work

以下事项仍必须升级，不适用 6.1 fast path：

- Project Definition / Scope / V1 direction；
- Governance authority / permission boundary；
- Identity Merge/Split 的高影响决定；
- destructive migration / major Canonical deletion / Legacy retirement；
- License / Security policy；
- stable Specification / Governance promotion；
- branch protection / ruleset 的重大权限变化；
- formal Release 或其他 materially irreversible decision。

这类事项需要适当的 independent review，并在属于 Owner/Governance Gate 时取得 Human Owner / designated governance authority 的明确授权。

### 6.4 Owner role

Owner 不承担无法实质验证的日常技术签字。Owner 主要决定项目方向、价值取舍、重大风险边界和不可逆治理事项。技术细节应尽可能通过 executable evidence 和 Maintainer/Agent responsibility 解决。

## 7. Pull Request Boundary

改变 Canonical Repository 的完成产物 SHOULD 通过 PR 交付。当前 connector 直接写 main 属于 Bootstrap 过渡；Agent-ready tasks 应逐步优先采用 branch / PR。PR 至少说明 Linked Work Item、Execution Mode、Scope、Evidence、Validation、Remaining work 和 Review Class。

## 8. Agent Transparency

Agent 参与时按 `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md` 区分 Initiator / Executor / Reviewer 与 GitHub Actor。Agent 在开始任务前必须读取 `AGENTS.md`，并按任务模式读取 `PROJECT_STATE.md`、Issue 和相关 Specification；不得假设私人聊天记忆属于公共项目上下文。

具体工具名称 MAY 记录，但流程 MUST NOT 依赖单一厂商。

## 9. Pilot Success Criteria

Task System v0.1 至少需要真实 Research / Modeling、Specification / Design、Code / Repository implementation 三类任务验证。Fresh-session takeover 和 different-agent takeover 继续作为 Project-level Continuity 实测。

试运行 friction 必须记录；只有重复出现且 GitHub 原生机制无法覆盖的 friction，才升级为 automation / protocol gap。
