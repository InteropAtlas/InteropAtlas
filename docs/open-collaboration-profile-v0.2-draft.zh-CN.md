# InteropAtlas Open Collaboration / Human–AI Collaboration Profile v0.2 Draft

> 状态：Draft / Provisional Specification
>
> Parent：#19；Work Package B：#22；Pilot Task：#24
>
> v0.2 目的：保持 v0.1 的 Human-first / agent-compatible 协作合同，同时把 Task Reference Seeding 正式合并进 Work Item Contract，并根据 2026-09 GitHub Issue Fields 现状修正 operational mapping。

## 1. 规范关键词

MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 按 BCP 14（RFC 2119 + RFC 8174）理解。

## 2. 核心定位

Open Collaboration 是 InteropAtlas 的 cross-cutting operating layer，不是独立知识主路线。

```text
Vision / Specifications
        ↓
Public GitHub Work Items
        ↓
Human / Agent Executors
        ↓
Public Artifact / Pull Request
        ↓
Independent Review / Oversight
        ↓
Human Maintainer Authorization where required
        ↓
Merge / Done / Handoff
```

原则：

> **Human-first, agent-compatible.**
>
> **同一公开任务协议，允许不同执行者。**
>
> **Project state MUST be recoverable without private chat memory.**

## 3. 上游依据

本 Profile 是组合 Profile，不声称存在一个可直接照搬的单一国际标准。

主要依据：
- ISO/IEC CD 25589 — Human–Machine Teaming，仍处于制定阶段；
- ISO/IEC 5339:2024 — AI application lifecycle / stakeholder engagement；
- NIST AI RMF — human-AI roles / responsibilities / oversight；
- Linux Foundation AAIF / AGENTS.md — repository-specific Agent instructions 的开放生态先例；
- GitHub Issues / Assignees / Sub-issues / Dependencies / Issue Fields / Pull Requests / Reviews / CODEOWNERS / Rulesets。

GitHub Issue Fields 在 2026-07 已对组织进入 Generally Available。它们是 organization-level typed metadata，可用于 single-select / text / number / date 等结构化字段，并可进入 Projects。当前 GitHub 文档同时明确：Issue Fields 不能直接由 Issue Template 预填，需通过 Issue sidebar、Project、API 或 Actions 设置。因此 IA 的 V0 Pilot 可以使用结构化 Issue-body metadata 作为 bootstrap fallback，但长期 SHOULD 迁移到 public Issue Fields。

## 4. Participant Roles

角色是职责，不等于账号类型。

- **Steward / Project Maintainer**：Vision、Scope、priority、重大治理与 release 决策；
- **Task Author / Planner**：把 Goal 转成可独立执行的 Work Item；
- **Executor / Contributor**：Human 或 Agent，负责 Claim 后的实际工作；
- **Reviewer / Overseer**：独立检查 Specification、Evidence、Scope、Validation；
- **Maintainer / Approver**：拥有最终 merge / governance authorization；
- **Automation Infrastructure**：CI、Validator、Renderer、Bot、Scheduler，不是 Reviewer identity。

### IA-OC-001 — Executor 与 independent reviewer 必须可区分

Executor **MUST NOT** 把 self-check 描述为 independent review。

普通任务 **SHOULD** 有不同 Human / Agent Review；高影响任务 **MUST** 有 Human Maintainer 最终授权。

### IA-OC-002 — 高影响任务保留 Human authorization

至少包括：
- 项目核心 Definition / Scope；
- Governance / Collaboration Profile；
- Canonical Schema 破坏性变更；
- License / Security policy；
- stable Specification 状态升级；
- main branch protection / ruleset；
- 大规模 Canonical Data 删除；
- 正式 Release。

## 5. Work Item Contract

### IA-OC-003 — Ready Work Item MUST 同时包含任务合同与参考上下文

标记为 `Ready` 的 Work Item **MUST** 至少包含：

1. **Objective** — 目标结果；
2. **Why / Context** — 为什么需要；
3. **Read First / Upstream Contracts** — 必须遵守的 Definition / Specification / Schema / Issue；
4. **Seed References** — Task Author 已知的高价值 Atlas objects / Standards / Mature Precedents / Methods / Implementations，优先 stable ID；
5. **Freshness / Completeness Check** — 执行者必须重新检查新版本、superseding artifacts、新标准、替代方案、成熟先例与 Atlas 漏项；
6. **Scope**；
7. **Non-goals**；
8. **Deliverables**；
9. **Evidence Requirements**；
10. **Acceptance Criteria**；
11. **Review / Authorization Class**；
12. **Dependencies / Blockers**；
13. **Lease Policy**。

`Seed References` **MUST NOT** 被当成封闭答案集。执行中发现的新对象 SHOULD 回流 Atlas；当前模型无法准确表达时 SHOULD 创建 Intake / Model Gap，而不是强塞错误类型。

Task-specific Agent prompt MAY 由执行环境生成，但 **MUST NOT** 成为唯一 Work Item contract。

### IA-OC-004 — 公共上下文优先

影响执行的稳定上下文 **SHOULD** 进入 Issue、PR 或 repository artifact。任务若必须依赖私人聊天历史才能正确开始，**MUST NOT** 标为 fully Ready。

## 6. Task Graph

### IA-OC-005 — GitHub Issue 是默认 Work Item identity

V0.2 **SHOULD** 使用 GitHub Issue 作为公开 Work Item identity。大型 Work Package SHOULD 使用 Parent / Sub-issues；依赖 SHOULD 使用 GitHub dependencies 或同等公开映射。

### IA-OC-006 — Roadmap 与 Task Graph 分工

Roadmap 负责方向；Issue graph 负责可执行工作。项目 **MUST NOT** 建立与 GitHub Issues 不同步的 Agent-only Task source of truth。

## 7. Lifecycle

```text
Draft → Ready → Claimed → In Progress → Review → Done
                         ↘ Blocked
                         ↘ Handoff
Claimed / In Progress / Blocked / Handoff → Released → Ready
Review → Changes Requested → In Progress
```

- Draft：合同不足，不能自主领取；
- Ready：满足 IA-OC-003；
- Claimed：Primary Lease Holder 已公开获得主要执行权；
- In Progress：已有可观察 substantive work；
- Blocked：仍持有任务但有外部阻塞；
- Handoff：准备交接；
- Review：产物已公开交付等待独立审核；
- Done：Acceptance + required authorization 均完成；
- Released：Claim 解除，任务回 Ready。

## 8. Lease-style Claim

### IA-OC-007 — 普通排他任务 SHOULD 有一个 Primary Lease Holder

Collaborators MAY 存在，但主要执行责任必须可识别。

### IA-OC-008 — Claim MUST 可公开观察

至少记录：
- holder / responsible account；
- claim time；
- lease expiration / review time；
- current status；
- execution mode。

### IA-OC-009 — Claim SHOULD 是有限期 Lease

Profile 不规定永久统一时长。`docs/collaboration-task-system-v0.1.zh-CN.md` 的 72 小时只是 Pilot 初始 review window，不是规范常量。

### IA-OC-010 — Renewal SHOULD 有进展证据

Issue update、commit、PR、draft artifact、research result、blocker report 等均可；单纯“仍在处理”不应无限续租。

### IA-OC-011 — Lease expiration MUST NOT 删除已有工作

Released 后，branch / commit / PR / notes 保留；下一执行者 SHOULD 先读取已有 Handoff / Artifact。

## 9. GitHub-native Metadata Mapping

优先目标：

| IA semantic | Preferred GitHub mapping |
|---|---|
| Task identity | Issue |
| Primary Lease Holder | Assignee |
| Status | public Issue Field: `Status` |
| Lease expiration | public Issue Field: `Lease Until` (date) |
| Execution Mode | public Issue Field: `Execution Mode` |
| Review Class | public Issue Field: `Review Class` |
| Priority | Issue Field / existing project policy |
| Parent | Parent Issue / Sub-issue |
| Dependency | blocked-by / blocking |
| Work product | branch / commit / PR / repository artifact |
| Review | PR Review |
| Ownership routing | CODEOWNERS |
| Required authorization | Ruleset / Required Review |

当前 Pilot 尚未配置 organization-level Issue Fields，因此 MAY 使用 Issue body metadata block：

```text
Status: Ready
Primary Lease Holder: —
Claimed At: —
Lease Until: —
Execution Mode: unassigned
Review Class: normal | high-impact
Parent: #issue | —
Blocked By: #issue | —
```

一旦 Issue Fields 配置完成，Status / Lease / Execution Mode / Review Class SHOULD 以 Issue Fields 为 canonical structured state，Issue body 不应维护冲突副本。

**GitHub platform fact：**Issue Fields 当前不能由 Issue Template 直接预填；如需自动设置，SHOULD 使用 API / GitHub Actions，而不是因此创建独立 Task DB。

## 10. Handoff / Continuity

### IA-OC-012 — Handoff MUST 显式记录

最小合同：
1. current status；
2. completed；
3. artifacts / commits / PRs；
4. validated；
5. remaining；
6. blockers / open questions；
7. recommended next action；
8. current branch / PR / commit。

### IA-OC-013 — Handoff MUST NOT 只存在于 Chat summary

Chat MAY 提供输入，但长期可恢复状态必须进入 Issue / PR / repository artifact。

## 11. Review / Oversight

### IA-OC-014 — PR SHOULD 是可合并产物的 Review boundary

Bootstrap 阶段的直接 main 编辑是过渡例外；Agent-ready task Pilot SHOULD 采用 branch / PR。

### IA-OC-015 — Review SHOULD 针对上位合同

Reviewer 应检查 Acceptance、Specification / Schema、Evidence requirements，而不是只判断“看起来不错”。

### IA-OC-016 — Automation 是 Evidence，不是 Reviewer

CI、Validator、E2E、link checker 的通过结果 **MUST NOT** 被描述为 independent review。

### IA-OC-017 — 高风险区域 SHOULD 使用 ownership / ruleset 路由

Schema、Governance、stable Specification、Security / Licensing 等 SHOULD 逐步映射到 CODEOWNERS / Required Review / Rulesets。

## 12. AI / Agent Transparency

### IA-OC-018 — Agent 参与 SHOULD 可追踪但 vendor-neutral

Work Item / PR SHOULD 记录 execution mode：human / agent / mixed。具体 Agent / tool MAY 记录，但流程 **MUST NOT** 依赖单一厂商。

### IA-OC-019 — Agent MUST NOT 依赖未公开永久上下文

Agent-ready task SHOULD 假设新执行者只有 repository、Issue 与获准连接上下文。

## 13. AGENTS.md Boundary

### IA-OC-020 — AGENTS.md 只承载 repository-specific Agent instructions

可以包括：read-first files、validation commands、generated-file policy、formatting / test rules、forbidden direct edits、task / PR protocol pointers。

AGENTS.md **MUST NOT**：
- 重定义 Vision；
- 替代 CONTRIBUTING / Governance / Specifications；
- 隐藏 Human 不可见规则；
- 绑定单一 Agent vendor；
- 成为 Task source of truth。

## 14. Operational Profile Boundary

`docs/collaboration-task-system-v0.1.zh-CN.md` 是本 Profile 的 **Pilot Operational Profile**：它选择暂定 72h Lease review window、Issue-body metadata fallback、Claim / Handoff comment format 等实现参数。

Operational Profile MAY 调整 Pilot 参数，但 **MUST NOT** 无声重写本规范 Requirements。重复出现的 friction 才能推动 Extend / Invent。

## 15. Conformance

Ready 前：
- [ ] IA-OC-003 全部字段足够；
- [ ] 不依赖 private chat；
- [ ] Review Class 明确；
- [ ] Lease Policy 明确。

Done 前：
- [ ] Deliverables 已公共化；
- [ ] Acceptance 满足；
- [ ] Evidence / CI 已记录；
- [ ] independent review 已完成到所需级别；
- [ ] high-impact 已 Human Maintainer approval；
- [ ] residual work 已 Handoff / follow-up。

## 16. v0.1 → v0.2 Draft Change Log

1. `IA-OC-003` 正式吸收 Task Reference Seeding：Read First + Seed References + Freshness / Completeness Check；
2. Work Item Contract 从 10 项扩展为 13 项，加入 Lease Policy；
3. 根据 GitHub 2026-07 Issue Fields GA 更新 metadata mapping；
4. 明确 Issue Fields 无法由 Issue Template 直接预填这一平台事实，并保留 API / Actions 路径；
5. 明确 `collaboration-task-system-v0.1` 是 Operational Profile，不是独立治理 source of truth；
6. 明确 72h 是 Pilot 参数，不进入长期 normative requirement；
7. 其余 IA-OC-001…020 的核心语义保持与 v0.1 兼容。

## 17. Draft Authorization Status

本文件由 Agent execution 形成，Review Class = `high-impact`。

它 **不能自动替代 v0.1**。至少需要：
- independent review；
- Human Maintainer final authorization。

在获得批准前，`open-collaboration-profile-v0.1.zh-CN.md` 仍是当前已接受的 Draft/Profile 基线；本文件用于 Work Package B Pilot 与后续 revision review。

## 18. 官方平台参考

- GitHub Issue Fields GA (2026-07-02): https://github.blog/changelog/2026-07-02-issue-fields-are-now-generally-available/
- GitHub Managing Issue Fields: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields-in-your-organization
- GitHub Adding and Managing Issue Fields: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields
- GitHub About Issue Fields in Projects: https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-issue-fields
