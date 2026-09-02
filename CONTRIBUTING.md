# 为 InteropAtlas 贡献

InteropAtlas 当前处于 Pre-Alpha。项目采用 **Human-first, agent-compatible** 的公开协作方式：Human 与 AI / Agent 使用同一套 GitHub Work Item、Lease、Handoff 和 Review 协议，不建立只给 Agent 使用的隐藏任务系统。

核心协作规范：
- `docs/open-collaboration-profile-v0.1.zh-CN.md`
- `docs/collaboration-task-system-v0.1.zh-CN.md`
- `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`

## 1. 基本原则

- 能使用权威一手来源时，优先使用一手来源。
- 明确区分标准、协议、规范、方法、实现、组织、项目和产品。
- Fact 与 Assessment 分离；关系与判断需要可追踪 Evidence。
- 除非再发布权利清晰，否则不要复制第三方规范全文。
- 优先提交较小、可独立 Review 的变更。
- 稳定任务上下文必须进入 Issue / PR / repository artifact，不能只留在聊天窗口。
- GitHub Actor 不是实际 Contributor / Executor 的可靠替代；贡献角色必须能单独表达。

## 2. 从哪里开始：找 Ready Work Item

可自主执行的任务应使用 GitHub Issue，并明确标记：

```text
Status: Ready
Primary Lease Holder: —
Claimed At: —
Lease Until: —
Execution Mode: unassigned
Review Class: normal | high-impact
```

`Ready` 任务必须已经包含 Objective、Context、Read First、Seed References、Freshness Check、Scope、Non-goals、Deliverables、Evidence、Acceptance、Review Class、Dependencies 和 Lease Policy。

如果这些信息不足，请先把任务保持为 `Draft`，不要靠私人聊天补齐后直接执行。

## 3. 认领任务：Lease-style Claim

普通排他任务默认只有一个 Primary Lease Holder。

认领时：

1. 将负责账号设为 Assignee；
2. 在 Issue 中留下公开 Claim comment；
3. 记录 `Claimed At`、`Lease Until`、Execution Mode；
4. 将 Status 改为 `Claimed`；
5. 开始实质工作后改为 `In Progress`。

Pilot 默认首次 Lease review window 为 **72 小时**，Task Author 可明确覆盖。

Claim comment：

```text
Claim
Holder: @account / agent identity
Execution mode: human | agent | mixed
Claimed at: YYYY-MM-DD HH:MM TZ
Lease until: YYYY-MM-DD HH:MM TZ
Planned first checkpoint: ...
```

续租应伴随可观察进展：commit、PR、draft artifact、研究结果、blocker report 或 substantive Issue update。Lease 到期不删除已有工作；任务可 Released 回 Ready，由下一位执行者继续。

## 4. 执行过程中

执行者必须遵守 Issue 的 Scope / Non-goals 和上位 Specification。

研究或标准相关任务使用：

### Read First / Upstream Contracts
必须遵守的 IA Definition / Specification / Schema / Issue。

### Seed References
Task Author 已知并已进入 Atlas 的高价值 Standard / Mature Precedent / Method / Implementation。优先引用 stable Atlas ID。

### Freshness / Completeness Check
执行者仍需检查：新版本、superseding artifact、新标准、新替代方案、新成熟先例和 Atlas 漏项。

Seed References 是共享起点，不是封闭答案集。新发现应进入 Atlas，或创建明确 Intake / Model Gap follow-up。

## 5. Blocked / Released / Handoff

阻塞时不要静默占用任务。将 Status 设为 `Blocked` 并公开说明 blocker。

需要交接时使用：

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

Human→Agent、Agent→Agent、Human→Human 使用同一格式。

## 6. Pull Request、Contribution Identity 与 Review

改变 Canonical Repository 的完成产物应优先通过 PR 进入 Review。

PR 至少说明：
- Linked Work Item；
- Execution Mode；
- Contribution Identity；
- Scope / out-of-scope；
- Evidence / sources；
- Validation performed；
- Remaining work / handoff；
- Review Class。

### Contribution Identity

对 Agent 执行、Human/Agent mixed、或 GitHub Actor 与实际执行者不一致的工作，PR SHOULD 分开记录：

```text
Initiator — 谁决定启动这项工作
Executor — 谁实际完成实质贡献
Reviewer — 谁独立审核
Approver — 谁进行最终治理授权
GitHub Actor — 哪个 GitHub 账号 / App 执行平台动作
```

Human / Agent 是参与者类别；Initiator / Executor / Reviewer / Approver 是贡献角色；GitHub Actor 是平台 Provenance。三者不能混成一个“作者”。

当 Agent 使用 Human 的 GitHub Account、Connector、Token 或其他授权凭据写入仓库时，MUST 明确记录实际 Executor 与 GitHub Actor 的区别。

Agent 不需要为了 Attribution 被强制注册独立 GitHub 账号。完整定义见 `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`。

Executor 的 self-check 不等于 independent review。CI / Validator / E2E 是 Review Evidence，不是 Reviewer。

### normal

普通数据、研究、文档和非破坏性实现任务。SHOULD 由不同于 Executor 的 Human 或 Agent 独立 Review。

### high-impact

项目定义 / Scope、Governance / Collaboration、破坏性 Schema、License / Security、stable Specification 升级、main protection / ruleset、大规模数据删除、正式 Release 等变更，必须有 **Human Maintainer 最终授权**。

## 7. Done 条件

任务关闭为 Done 前确认：

- Deliverables 已进入公开 Artifact / PR；
- Acceptance Criteria 已满足；
- 所需 Evidence / tests 已记录；
- Contribution Identity 已在适用场景中记录；
- 所需 independent review 已完成；
- high-impact 任务已有 Human Maintainer approval；
- residual work 已形成 Handoff 或 follow-up Issue。

## 8. AI / Agent 贡献

Agent 可以作为 Initiator、Executor 或 Reviewer，但流程不绑定任何厂商。当前高影响治理授权仍由 Human Maintainer 承担。

Agent 开始任务前应读取：
1. 当前 Issue；
2. `AGENTS.md`；
3. Issue 的 Read First / Upstream Contracts；
4. 与修改区域相关的 Specification / Schema。

Agent 不应假设私人 Chat 历史是公共项目状态。主要由 Agent 执行的任务 / PR 应记录 `Execution Mode: agent` 或 `mixed`，并记录实际 Agent identity；不能仅因为 GitHub 页面显示 Human Account 就把该 Human 记作 Executor。

## 9. 数据、时间与语言规则

项目采用“中文优先、英文机器标识、中英双语知识字段”。

- `id`、字段名、枚举值、关系类型、路径、Schema 和 API 标识使用英文。
- 中文是当前主文档和主要解释语言。
- 名称、描述、定义等知识字段尽可能同时提供 `*_zh` 与 `*_en`。
- 官方名称、标准编号、组织名、协议名保留正式原文。
- 翻译不确定时保留原文并标记译名。

完整规则见 `docs/language-policy.zh-CN.md`。

### Canonical Record lifecycle time

现实世界对象的发布时间 / 创建时间 / 生效时间，与 InteropAtlas 记录自己的生命周期不是同一个事实：

```text
artifact publication date / entity creation date
≠
InteropAtlas record creation / update time
```

V0 Schema 提供：

```yaml
record_created_at: 2026-09-02T08:30:00+08:00
record_updated_at: 2026-09-02T09:10:00+08:00
```

- `record_created_at`：该 Canonical Record 首次进入 InteropAtlas 的时间；
- `record_updated_at`：该 Record 最近一次实质更新的时间；
- 使用 RFC 3339 / ISO 8601，并带明确时区；
- Git 历史仍是逐次修改的权威事件日志；显式字段是便于查询和显示的当前生命周期元数据；
- 新建或实质修改的 v0 Record SHOULD 维护这两个字段；
- 当前不要求一次性回填全部 Legacy Data。

当前结构化事实源主要使用人类可编辑 YAML，并由 Schema / Engine / CI 验证。生成的 HTML、Markdown、JSON/RDF 等视图不是第二事实源。

## 10. 许可证

提交贡献即表示同意按照 `LICENSE.md` 中与目标内容对应的许可证提供贡献：

- 软件及功能性 Schema：Apache-2.0；
- 原创结构化事实数据：CC0-1.0；
- 原创文字文档与研究内容：CC BY 4.0。

不要提交无权再发布的第三方材料；如果第三方材料允许收录，应保留必要归属与许可证信息。
