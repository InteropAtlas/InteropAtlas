# Human + Agent Access Architecture V1（Architecture Draft）

> Status: Architecture Draft
>
> Phase: P4.5 — Human + Agent Access Architecture
>
> Primary Work Item: Issue #127
>
> Upstream: Canonical Contract V1, Write / Intake Contract, Selection / Projection / Workspace Architecture, Agent Attribution Profile, Task Authority Governance draft
>
> Scope: 定义 Human / Agent 如何访问同一知识与 Workspace world，以及 Identity / Capability / Authority / Platform Permission 的边界。**本文件不建立最终权限系统、不配置 GitHub Ruleset/CODEOWNERS、不授予新的治理权限。**

## 1. 目的

InteropAtlas 需要同时服务 Human 与 Agent。两者应共享同一个 Canonical knowledge world，但不能因为“都能读取/生成内容”就被视为拥有相同身份、能力或 Canonical acceptance authority。

核心原则：

> **Shared knowledge world does not imply shared authority.**

以及：

> **Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission.**

## 2. Access layers

P4.5 将访问能力概念上分为六层：

1. **Discover / Read** — 浏览、读取 Canonical / Projection / Evidence；
2. **Query / Traverse** — 搜索、筛选、图遍历、结构化检索；
3. **Compose / Analyze** — 比较、总结、推理、生成 Workspace interpretation；
4. **Candidate Write** — 提交 Candidate Assertion / Proposal / Patch / Evidence；
5. **Review / Assess** — 独立检查候选 mutation、evidence、semantic mapping；
6. **Canonical Accept / Govern** — 接受高影响 mutation、稳定规范、治理/身份/破坏性变更。

这些层不是单一“读/写权限”可以完整表达的。

## 3. Human / Agent common contract

Human 与 Agent 共享：
- Canonical identity semantics；
- Source / Evidence / Assertion / Assessment / Provenance boundaries；
- Relation semantics；
- Selection / Projection rules；
- Candidate → Validation → Review → Acceptance intake path；
- provenance / contribution traceability expectations。

不得维护一套“Human truth”和另一套“Agent truth”。

## 4. Human / Agent asymmetry

允许并且预期存在差异：
- UI vs structured query/API/tool surface；
- context window；
- navigation style；
- batch processing ability；
- automation frequency；
- available tools；
- claim eligibility；
- review/acceptance authority。

因此“接口不同”不意味着“知识不同”，“同一知识”也不意味着“权限相同”。

## 5. Identity model

Access Architecture 复用贡献身份模型：
- Participant Class: Human | Agent；
- Initiator；
- Executor；
- Reviewer；
- GitHub Actor / Platform Actor 独立记录；
- high-impact 时另有 Governance Approver。

### 5.1 Agent identity

Agent system/provider/model/session 应按需要分层：
- stable Agent System identity；
- Provider；
- Model/version when relevant；
- Session/Run when audit requires。

模型升级不应自动制造新的长期 contributor identity。

### 5.2 Credential is not identity

Human 的 GitHub token、Agent 使用的 connector credential、GitHub App/Bot 身份都是平台执行凭据，不自动证明实际 Executor。

因此：

> **Authenticated Platform Actor ≠ Proven Actual Executor.**

## 6. Capability model

Capability 回答：**该参与者/系统实际能够可靠执行什么类型的操作？**

候选 capability domains：
- research / prior-art；
- canonical data curation；
- schema / knowledge modeling；
- relation / graph；
- runtime / code；
- documentation；
- product / UX；
- governance / collaboration；
- release / security。

Capability 应按领域表达，而不是把 Human/Agent 排成单一高低等级。

Capability 可以来自：
- maintainer authorization；
- team membership；
- verified contribution history；
- tool/runtime capability declaration；
- bounded task-specific authorization。

P4 不冻结最终 registry 或自动认证机制。

## 7. Authority dimensions

至少区分：

### Claim Authority
谁可以开始某个 Work Item。

### Execution Authority
谁被允许实际执行某类 mutation/operation。

### Review Authority
谁可以作为 independent reviewer 对某类工作给出有效 review。

### Acceptance / Governance Authority
谁可以让候选变化进入 Canonical/stable/governance state。

### Platform Permission
谁在 GitHub/API/infra 技术上拥有 push/merge/write/admin credential。

任何一项都不得从另一项自动推断。

例如：拥有 GitHub Write 权限的 Agent 不因此获得 Schema acceptance authority；Human Owner 的账号被 Agent connector 使用时，也不能把 Agent execution 自动记录成人类亲自执行。

## 8. Task Authority + Mutation Impact composition

P4.5 不替代已有两个维度：
- Task Authority Class T0–T3：谁可 Claim / 开始；
- Mutation Impact M0–M3：变化本身影响多大。

Access decision 应组合考虑：

```text
Participant Identity
+ Capability Scope
+ Task Authority / Claim Eligibility
+ Intended Operation
+ Mutation Impact
+ Review Requirement
+ Platform Permission
= Allowed workflow path
```

这不是一个简单 role number。

## 9. Default Agent authority

Agent 默认可以：
- Discover / Read / Query / Traverse；
- 收集来源与 Evidence；
- 生成 Candidate Assertion / Proposal / Patch；
- 运行 Machine Validation；
- 在政策允许且与 Executor 独立时执行 Agent Review；
- 报告 uncertainty / conflict / missing evidence；
- 在明确授权任务范围内执行普通 repository operation。

Agent 默认不可以仅凭自身输出：
- 宣布高影响 Identity merge/split 已获接受；
- 自行批准 destructive migration / mass deletion；
- 把 architecture draft 提升为 stable governance/spec；
- 自己执行并自己构成 independent review；
- 把 generated interpretation 直接宣布为 Canonical Fact；
- 因持有 Human credential 而继承 Human Owner authority。

## 10. Human authority is also governed

Human input 也不自动绕过知识治理。

普通 Human contributor 的事实性贡献仍应遵守：
- evidence/provenance；
- structural validation；
- semantic review when required；
- Task Authority / Review Class；
- high-impact gate。

Human 的特殊角色主要来自明确的 Owner / Maintainer / capability / governance authorization，而不是“因为是人类所以天然正确”。

## 11. Independent review

Independent Review 必须与 self-check 区分。

有效独立 review 的基本条件：
- Reviewer 不是同一 execution instance 的自我确认；
- 能访问足够的 source/evidence/diff/context；
- 对该领域具有所需 capability；
- review 结果可追溯。

不同 Agent instance 是否足够“独立”，需要 P5/P6 根据 provider/model/context sharing 风险进一步验证；P4 不把“换一个会话”自动视为强独立性。

Machine Validator / CI 提供 Review Evidence，不自动等同 Reviewer。

## 12. Human + Agent collaboration patterns

架构至少支持：

```text
Human Initiator → Agent Executor → Human Reviewer
Human Initiator → Agent A Executor → Agent B Reviewer → Human high-impact approval
Agent discovers gap → Candidate Work Item → Maintainer claim approval → Agent execution
Human curation → Agent validation → Human/Agent independent review
Agent research → Human judgment → Agent patch execution
```

重点不是固定流程，而是每一步的实际角色、authority 与 provenance 可区分。

## 13. Workspace collaboration state

Human 与 Agent 可以共享：
- selected subjects；
- comparison set；
- active filters；
- unresolved questions；
- evidence focus；
- candidate patches；
- review comments。

但共享 Workspace State 不等于共享身份，也不自动产生 Canonical mutation。

Agent 对 Workspace 的总结、排序、标记、建议默认属于 derived/generated state；只有明确转换为 Candidate / Patch 后才进入 Intake。

## 14. Delegation boundary

未来 Human 可以把 bounded authority 委托给 Agent，例如：
- 在某个 T0/T1 Work Item lease 内编辑；
- 对某个 family 执行 M0/M1 evidence/data patch；
- 运行特定 migration dry-run；
- 执行指定 validator/renderer operation。

委托应尽可能表达：
- delegator；
- delegate Agent；
- scope；
- allowed operations；
- duration / lease；
- mutation ceiling；
- review requirement；
- revocation/expiry。

原则：

> **Delegation should be bounded, explicit and revocable; credentials should not be treated as delegation policy.**

## 15. Least privilege and safe automation

自动化应获得完成任务所需的最小权限。

优先：
- scoped task lease；
- scoped repository/path operation；
- candidate-write before canonical-accept；
- branch/PR for reviewable changes；
- dry-run before destructive/structural action；
- explicit high-impact gate。

避免：
- 因方便给 Agent 永久 admin；
- 用同一 credential 隐藏多个实际 Executor；
- 让 bot/Agent 自动扩大自身 capability；
- 用平台权限替代项目治理。

## 16. Public contributor access

长期开放协作需要至少三条清晰入口：
- **Open discovery/research contribution**：低风险资料、Candidate Pool、evidence gap；
- **Bounded canonical contribution**：符合明确 profile/validation 的普通知识 patch；
- **Restricted architecture/governance work**：需要 Maintainer/Owner authorization。

这使“更多 Human / Agent 尽早参与标准收入”成为可能，同时不要求先开放底层 Schema/治理权限。

## 17. Failure / revocation / correction

Access Architecture 必须允许：
- lease expiry；
- capability/authorization revoke；
- rejected candidate；
- reviewer conflict-of-interest correction；
- mistaken Agent attribution correction；
- credential compromise 后撤销平台权限但保留历史 provenance；
- accepted mutation 的后续 correction/supersession。

撤销当前权限不得抹除历史贡献身份。

## 18. P5 validation matrix

| Question | Representative experiment |
| --- | --- |
| Agent candidate write | Agent 收录一个标准是否能只生成 Candidate/Patch 而非直接 truth |
| Attribution | Agent 用 Human GitHub Actor 写入时是否仍能正确记录 Executor |
| Capability scope | Research-capable Agent 是否会被阻止自行修改 Schema authority |
| Independent review | Agent A → Agent B review 是否能识别共享上下文/模型带来的独立性风险 |
| Delegation | 一个限定 M0/M1 的 task lease 是否足以完成批量 evidence intake |
| Workspace handoff | Human selection → Agent analysis → Human review 是否保持同一 task context |
| High-impact gate | Identity merge / destructive migration 是否无法由 executing Agent 自批 |
| Public intake | T0/T1 标准候选收录是否能让第三方 Human/Agent 安全参与 |

## 19. Not Yet decisions

P4.5 不冻结：
- final T0–T3 names；
- Agent capability registry；
- Maintainer registry；
- Agent authentication protocol；
- GitHub App vs bot vs user account strategy；
- CODEOWNERS / Ruleset configuration；
- cryptographic Agent identity；
- automatic trust scoring；
- cross-provider Agent independence threshold；
- exact delegation serialization；
- permission bot implementation。

## 20. Settled P4.5 architecture decisions

- Human / Agent 共用同一个 Canonical knowledge world；
- Shared knowledge ≠ shared authority；
- Identity / Capability / Task Authority / Review Authority / Platform Permission 必须正交；
- access 不只分 read/write，而分 Discover/Read、Query/Traverse、Compose/Analyze、Candidate Write、Review/Assess、Canonical Accept/Govern；
- GitHub Actor / credential 不等于实际 Executor 或 Owner authority；
- Capability 按领域而不是单轴人员等级表达；
- T0–T3 Task Authority 与 M0–M3 Mutation Impact 组合使用而不互相替代；
- Agent 默认可以研究、读取、查询、生成候选、验证和在授权范围内执行，但不能自授高影响 acceptance authority；
- Human 贡献同样受 evidence/validation/review 约束；
- self-check ≠ independent review；CI/Validator ≠ Reviewer；
- Delegation 必须 bounded / explicit / revocable；
- Workspace collaboration state 不自动成为 Canonical；
- 开放标准收入可以优先开放低风险 Candidate/Evidence/普通 Patch 路径，而不必同时开放 Schema/Governance；
- P4 不提前建设复杂权限自动化，P5/P6 再用真实协作验证。

## 21. Next

P4.5 第一轮完成后进入 **P4.6 Roadmap Reset**：把 P4.1–P4.5 的架构结论转换为 P5 real-data experiments / intake stress tests 与 P6 implementation 的可执行路线，并明确哪些并行旧任务保留、重排、迁移、暂停或退役。