# Work Package B — Collaboration Implementation Pilot Audit — 2026-09-01

> 状态：Point-in-time Pilot Audit
>
> Parent：#22
>
> 目的：检查 Work Package B 是否已经把 Open Collaboration Profile 从“文档定义”转换成真实、可发布、可认领、可交接、可 Review 的 GitHub-native Task System。

## 1. 结论

**PASS — Collaboration Implementation Pilot v0.1 已达到 Work Package B 的原始完成标志。**

B 的目标不是把所有未来治理自动化一次做完，而是让项目第一次真正能够：

```text
Direction / Work Package
        ↓
Public Ready Tasks
        ↓
Human / Agent Claim + Lease
        ↓
Independent execution
        ↓
Branch / PR / Artifact
        ↓
Review / Handoff
```

这条链路现在已经可以实际运行。

## 2. 已实现的公开协作层

### CONTRIBUTING

`CONTRIBUTING.md` 已从“数据贡献原则”扩展为完整公开任务工作流：
- 找 Ready Work Item；
- Lease-style Claim；
- Read First / Seed References / Freshness Check；
- Blocked / Released / Handoff；
- PR / Review；
- normal / high-impact Review Class；
- Human / Agent 共用协议；
- Done Gate。

### AGENTS.md

新增 root `AGENTS.md`：
- vendor-neutral；
- 只保存 repository-specific Agent instructions；
- 指向 Issue / CONTRIBUTING / Specifications；
- 明确 private chat 不是 Project state；
- 提供 validation commands；
- 不替代 README / Governance / Task source of truth。

这符合 Repository Structure Profile 与 Open Collaboration Profile 对 AGENTS.md 的边界要求。

### Issue Work Item Form

新增：

`.github/ISSUE_TEMPLATE/work-item.yml`

已表达：
- Status；
- Objective / Context；
- Read First；
- Seed References；
- Freshness / Completeness Check；
- Scope / Non-goals；
- Deliverables；
- Evidence；
- Acceptance；
- Execution Mode；
- Review Class；
- Parent / Dependencies；
- Lease Policy；
- Ready Contract checks。

### PR Template

新增：

`.github/PULL_REQUEST_TEMPLATE.md`

已表达：
- linked Work Item；
- execution mode；
- scope；
- evidence；
- validation；
- freshness check；
- review class；
- handoff / remaining work；
- self-check。

### Operational Profile

新增：

`docs/collaboration-task-system-v0.1.zh-CN.md`

明确 Pilot 状态、Issue-body metadata fallback、72h 初始 Lease review window、Claim / Handoff format、Review Classes 与 PR boundary。

72h 仅是 Pilot 参数，不是长期规范常量。

## 3. 第一批真实 Ready Tasks

已经发布三个不同类型的 Foundation Work Items：

### #23 — Research / Modeling

`#15 Fit Test Batch 1：Method / Heuristic / Design System 对象建模`

验证任务系统能否承载真实对象研究、官方 Evidence、Model Gap 与 Non-goals。

### #24 — Specification / Governance

`Open Collaboration v0.2 Draft：合并 Task Reference Seeding`

Review Class：high-impact。

该任务已实际运行：

```text
Ready
  ↓ Claim
In Progress
  ↓ dedicated branch
PR #26
  ↓ Handoff
Review
```

因此 B 并不是只创建了模板，而已经验证 Claim、Lease、Execution Mode、branch / PR、Handoff 和 high-impact Review Gate。

### #25 — Code / Repository Contract

`Repository Data Root Contract：迁移前路径集中化预备`

验证任务系统能否承载具有明确 migration invariants、tests、Non-goals 和 graph-health evidence 的实现任务。

## 4. Pilot #24 的真实结果

Executor：ChatGPT agent，通过 linked GitHub account `ff6962757` 执行。

公开记录已包含：
- Claim；
- `Execution Mode: agent`；
- Claim time；
- Lease Until；
- dedicated branch；
- commit；
- PR #26；
- Handoff；
- Review status。

产物：

`docs/open-collaboration-profile-v0.2-draft.zh-CN.md`

它把 Task Reference Seeding 正式合并进 IA-OC-003，并根据当前 GitHub Issue Fields 状态更新 metadata mapping。

该 PR 没有被自动合并，原因不是执行失败，而是任务本身是 `high-impact`：按照 Profile，它需要 independent review + Human Maintainer authorization。这说明 Review Gate 实际生效。

## 5. Pilot 发现的真实 friction / gaps

### B-GAP-001 — Shared GitHub account collapses role identity

当前 Agent 通过 Maintainer 的同一个 GitHub user account 写入仓库。

结果：
- Issue / commit / PR 的 GitHub author identity 都是 `ff6962757`；
- Issue 可以在正文中说明 `Execution Mode: agent`；
- 但 GitHub 原生 author / reviewer identity **无法证明**“Agent Executor”和“Human Maintainer Reviewer”是两个独立角色；
- 同账号也无法形成强平台级 independent-review audit trail。

这不是理论问题，而是 #24 Pilot 真实暴露的治理缺口。

候选解决方向需要后续比较：
- 独立 Agent / bot identity；
- GitHub App / bot attribution；
- Human approval artifact 与 execution identity 分层；
- 外部可验证 Agent provenance。

本轮 **不立即规定‘每个 Agent 必须注册独立 GitHub 账号’**，因为 identity / authorization / cost / security 需要单独 Profile。

### B-GAP-002 — Issue Fields 已 GA，但 Issue Template 不能直接预填

2026-07 GitHub Issue Fields 已对组织 GA，可以提供 typed organization-level metadata，并支持 date / single-select 等字段。

这非常适合：
- Status；
- Lease Until；
- Execution Mode；
- Review Class。

但当前 GitHub 官方文档说明 Issue Fields 不能由 Issue Template 直接预填，只能通过 sidebar、Projects、API 或 Actions 设置。

因此当前 Pilot 使用 Issue-body metadata 是合理 bootstrap fallback；长期 SHOULD 配置 public Issue Fields，并避免 body / field 双重 source of truth。

### B-GAP-003 — 当前仓库没有 Ruleset

审计时 repository rulesets 返回空集合。

因此：
- high-impact Review 目前主要依赖协议约束；
- 尚没有平台级 Required Review / protected-main enforcement。

Profile 已明确 main ruleset 属于 high-impact governance change，需要 Human Maintainer authorization。本 Work Package 不应由执行 Agent 自行开启。

### B-GAP-004 — Lease expiration 尚未自动执行

72h Lease 可以人工记录和释放，但没有 bot / Action 自动检查。

目前只有一个完整 Claim lifecycle 样本，尚无证据证明 stale lease 是重复 friction。

决策：**暂不开发 Lease automation。**

先继续真实任务；只有 stale / abandoned claim 重复出现，才实施提醒 / release automation。

## 6. Automation Decision

当前不建立 Lease Server、Heartbeat 或 Agent-only task DB。

优先级：

```text
更多真实任务
   ↓
观察重复 friction
   ↓
优先使用 GitHub Issue Fields / Actions / Rulesets
   ↓
GitHub 原生机制仍不足
   ↓
才 Extend / Invent
```

Issue Fields 配置是最值得的下一层原生增强，但需要 organization-level configuration；Ruleset 则需要 Human Maintainer governance authorization。

## 7. B Completion Checklist

- [x] CONTRIBUTING 表达 find → claim → work → PR → review → done / handoff；
- [x] AGENTS.md vendor-neutral 且不成为隐藏 Task source of truth；
- [x] Issue Work Item Form 表达 IA-OC-003 + Reference Seeding；
- [x] PR Template 表达 execution / evidence / validation / handoff / review；
- [x] Lifecycle / Lease / Handoff / Review Class 有 operational mapping；
- [x] 3 个不同类型 Foundation Ready Tasks 已发布；
- [x] 至少一个真实任务完成 Ready → Claim → In Progress → PR → Review / Handoff；
- [x] Pilot friction / gaps 已记录；
- [x] 没有在证据不足时提前开发复杂 automation。

## 8. Work Package B 最终状态

**B 可以关闭为 completed。**

这不意味着 #23 / #24 / #25 都已经 Done；它意味着“公开任务系统的第一版已经建立并通过真实 Pilot”。

接下来项目可以从：

```text
用户 → Chat → 一步一步说继续
```

转向：

```text
Maintainer → 定义方向 / 优先级
               ↓
           Ready Task Pool
               ↓
        Human / Agent leases
               ↓
        PR / Review / Handoff
```

下一阶段应该让 #23 / #25 等任务由不同执行者继续运行，并用真实摩擦决定是否增加 Issue Fields automation、identity profile、CODEOWNERS / Rulesets 与 stale lease automation。

## 9. 官方 GitHub Freshness Sources

- Issue Fields GA: https://github.blog/changelog/2026-07-02-issue-fields-are-now-generally-available/
- Managing issue fields: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-fields-in-your-organization
- Adding and managing issue fields: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-and-managing-issue-fields
