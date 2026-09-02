# InteropAtlas Collaboration Task System v0.1

> 状态：Pilot Operational Profile
>
> Parent Work Package：#22
>
> 上位规范：`docs/open-collaboration-profile-v0.1.zh-CN.md`
>
> Context Continuity：`docs/agent-onboarding-context-continuity-profile-v0.1.zh-CN.md`

本文把 Open Collaboration Profile 映射成当前仓库可直接执行的 GitHub 工作协议。它不建立第二套任务数据库；GitHub Issue 仍是 Work Item source of truth。

## 1. Work Item 必备结构

一个任务只有在以下信息足够完整时才能标记为 `Ready`：

1. Objective；
2. Why / Context；
3. Read First / Upstream Contracts；
4. Seed References；
5. Freshness / Completeness Check；
6. Scope；
7. Non-goals；
8. Deliverables；
9. Evidence Requirements；
10. Acceptance Criteria；
11. Review Class；
12. Dependencies / Parent；
13. Lease Policy。

`Seed References` 是已知高价值起点，不是封闭白名单。执行者仍要检查新版本、新标准、新替代方案和 Atlas 漏项。

## 2. V0 Task Metadata

当前仓库还没有配置 GitHub Project custom fields，因此 Pilot 使用 Issue body 中的结构化 metadata block 作为 fallback：

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

未来配置 Project Fields 后，这些字段 SHOULD 迁移到原生 fields；Issue body 可保留为可读镜像，但不得形成两个相互冲突的状态源。

## 3. Lifecycle

Pilot 使用：

```text
Draft → Ready → Claimed → In Progress → Review → Done
                         ↘ Blocked
                         ↘ Handoff
Claimed / In Progress / Blocked / Handoff → Released → Ready
Review → Changes Requested → In Progress
```

状态变化必须在 Issue 中公开可观察。

## 4. Claim / Lease

### 4.1 Claim 成立条件

一个排他任务只有同时满足以下条件才视为被认领：

- GitHub Assignee 指向 Primary Lease Holder 或负责账号；
- Issue 中存在公开 Claim 记录；
- `Claimed At` 与 `Lease Until` 已记录；
- Status 从 `Ready` 变为 `Claimed`。

### 4.2 Pilot 默认 Lease

默认首次 Lease review window：**72 小时**。

Task Author MAY 为明显更长或更短的任务指定不同期限。72 小时不是长期标准，只是 Pilot 参数。

续租必须伴随可观察进展，例如 commit、PR、draft artifact、研究结果、blocker report 或 substantive Issue update。

### 4.3 Claim comment

```text
Claim
Holder: @account / agent identity
Execution mode: human | agent | mixed
Claimed at: YYYY-MM-DD HH:MM TZ
Lease until: YYYY-MM-DD HH:MM TZ
Planned first checkpoint: ...
```

到期且没有有效进展时，任务可以 `Released → Ready`。已有 branch / commit / PR / notes 不得删除。

## 5. Handoff Contract

Handoff 使用同一个公开格式，不区分 Human→Agent、Agent→Agent 或 Human→Human：

```text
Handoff
Status: ...
Completed: ...
Artifacts / commits / PRs: ...
Validated: ...
Remaining: ...
Blockers / open questions: ...
Recommended next action: ...
Current branch / PR / commit: ...
```

长期可恢复信息必须进入 Issue、PR 或 repository artifact，不能只留在聊天窗口。

### 5.1 Context Exhaustion Handoff（上下文耗尽交接）

当 Agent 因上下文窗口、工具 Session、时间或执行环境限制而无法在同一会话继续时，必须把“下一个 Agent 真正需要的状态”写进 Handoff，而不是只在私人 Chat 最后一条消息里总结。

Handoff 至少要让新的 Executor 能回答：

- 已经做了什么；
- 哪些东西实际落到了仓库 / PR；
- 哪些 Validation 已经跑过；
- 哪些仍未完成；
- 当前 branch / PR / commit 在哪里；
- 下一步应该先做什么；
- 是否存在需要 Human 决策的 blocker。

### 5.2 Project-level Continuity（项目级连续性）

Issue / PR Handoff 继续只负责**具体任务**。

如果一次任务同时改变了以下任何项目级状态，SHOULD 同步根 `PROJECT_STATE.md`：

- 当前 Foundation / Phase；
- 当前主线 Work Item；
- `Resume Here` 的下一断点；
- Gate PASS / NOT PASS 状态；
- 高影响 Decision Gate；
- 一个足以改变后来 Agent 方向判断的重大里程碑。

普通局部任务不得为了留痕而频繁改 `PROJECT_STATE.md`。

### 5.3 Fresh-session Resume（新会话恢复）

如果没有明确 assigned Issue，而用户只要求“继续”，Agent SHOULD：

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

不得把私人聊天摘要当作唯一恢复机制。

## 6. Review Classes

### normal

适用于普通研究、数据、文档、非破坏性实现改动。

要求：
- Executor self-check 需要记录；
- SHOULD 有与 Executor 不同的 Human 或 Agent 进行 independent review；
- CI / Validator 是 Evidence，不是 Reviewer；
- 满足 Acceptance 后才进入 Done。

### high-impact

至少包括：
- 项目定义 / Scope；
- Governance / Collaboration Profile；
- Canonical Schema 破坏性变更；
- License / Security policy；
- stable Specification 状态升级；
- main branch protection / ruleset；
- 大规模 Canonical Data 删除；
- 正式 Release。

要求：
- independent review；
- **Human Maintainer 最终授权**；
- 不允许执行 Agent 把自己的 self-review 当成最终批准。

## 7. Pull Request Boundary

改变 Canonical Repository 的完成产物 SHOULD 通过 PR 交付。PR 至少说明：

- Linked Work Item；
- Execution Mode；
- Scope / out-of-scope；
- Evidence / sources；
- Validation performed；
- Remaining work / handoff；
- Review Class。

当前直接写 main 的 connector 工作属于 Bootstrap 过渡；Pilot 的 Agent-ready tasks 应优先采用 branch / PR。

## 8. Agent Transparency

Agent 参与时记录 `Execution Mode`，并按 `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md` 区分 Initiator / Executor / Reviewer 与 GitHub Actor。

Agent 在开始任务前必须读取 Repository `AGENTS.md`，并根据任务模式读取 `PROJECT_STATE.md`、Issue 的 Read First 与相关 Specification；不得假设私人聊天记忆属于项目公共上下文。

具体工具名称 MAY 记录，但流程 MUST NOT 依赖 ChatGPT、Codex、Claude、Copilot、Gemini 或任何单一厂商。

## 9. Pilot Success Criteria

Task System v0.1 只有在至少 3 个不同类型真实任务上可用，才算经过 Pilot：

- 一个 Research / Modeling task；
- 一个 Specification / Design task；
- 一个 Code / Repository implementation task。

试运行中遇到的 friction 必须记录。只有重复出现且 GitHub 原生机制无法覆盖的 friction，才升级为 automation / protocol gap。

Project-level Continuity 另外通过以下实测验证：

- 一个 fresh-session takeover（新会话接管）；
- 一个 different-agent takeover（不同 Agent 接管）。

测试目标不是要求新 Agent 读完所有历史，而是确认其能从仓库状态找到项目价值、当前主线、正确断点和相关任务上下文。
