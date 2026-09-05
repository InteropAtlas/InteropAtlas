# Human + Agent Access Architecture V1（P4.5 Historical Architecture Draft）

> Lifecycle: **Historical / Completed P4 Architecture Artifact**
>
> Original Phase: P4.5 — Human + Agent Access Architecture
>
> Primary Work Item: Issue #127 — completed / closed
>
> Current Role: 保存 P4.5 对 Human / Agent 共享知识、身份、能力、任务权限、Review 与平台权限边界的架构收敛历史。当前贡献身份、任务治理和 Agent onboarding 的具体规则由相应 Living Profiles / Governance Documents 维护；总体 Human + Agent 边界由 Master Design 维护。

## P4.5 accepted architecture synthesis

核心原则：

> **Shared knowledge world does not imply shared authority.**
>
> **Identity ≠ Capability ≠ Task Authority ≠ Review Authority ≠ Platform Permission.**

Human 与 Agent 共享 Canonical identity、Source / Evidence / Assertion / Assessment / Provenance、Relation、Selection / Projection、Candidate → Validation → Review → Acceptance 与 provenance expectations，不维护两套事实世界。

访问能力不能只压成 read/write，而应区分：Discover / Read、Query / Traverse、Compose / Analyze、Candidate Write、Review / Assess、Canonical Accept / Govern。

Human / Agent 可以在 UI / API、context window、navigation、batch processing、automation、tools、claim eligibility 和 review/acceptance authority 上不对称。

## Identity and capability boundary

P4.5 复用 Human | Agent participant class，以及 Initiator、Executor、Reviewer、GitHub / Platform Actor 与必要时 Governance Approver 的角色分离。

Agent system/provider/model/session 可按审计需要分层；模型升级不自动制造新的长期 contributor identity。

> **Authenticated Platform Actor ≠ Proven Actual Executor.**

Credential 是平台执行能力，不自动证明真实 Executor，也不自动授予 Owner / Maintainer authority。

Capability 应按 research、canonical curation、schema / knowledge modeling、relation / graph、runtime / code、documentation、product / UX、governance / collaboration、release / security 等领域表达，而不是把 Human / Agent 排成一个单轴等级。

## Authority dimensions

至少区分 Claim Authority、Execution Authority、Review Authority、Acceptance / Governance Authority 与 Platform Permission。任何一项都不能从另一项自动推断。

P4.5 将 Task Authority Class T0–T3 与 Mutation Impact M0–M3 视为两个独立维度；workflow 由 Participant Identity + Capability Scope + Task Authority + Intended Operation + Mutation Impact + Review Requirement + Platform Permission 共同决定。

## Agent and Human defaults

Agent 默认可读取、查询、研究、收集 Evidence、生成 Candidate / Proposal / Patch、运行 Machine Validation，并在政策允许和真正独立时参与 Review；不能仅凭自身输出自批高影响 identity、destructive migration、stable governance/spec promotion 或把 generated interpretation 直接宣布为 Canonical Fact。

Human 也不能因为是 Human 就绕过 evidence、validation 和 review。特殊 authority 来自明确 Owner / Maintainer / capability / governance authorization。

Self-check 与 Independent Review 分离；CI / Validator 提供 Review Evidence，不自动等于 Reviewer。

## Delegation and least privilege

Delegation 应 bounded / explicit / revocable，并尽可能表达 delegator、delegate、scope、allowed operations、duration / lease、mutation ceiling、review requirement 与 revocation/expiry。

> **Delegation should be bounded, explicit and revocable; credentials should not be treated as delegation policy.**

自动化遵循 least privilege，优先 scoped lease、scoped operation、candidate-write before canonical-accept、reviewable branch/PR、destructive action 前 dry-run 与 explicit high-impact gate。

## Open contribution boundary

长期开放协作至少区分低风险 discovery/research contribution、受约束的 canonical contribution 与受限 architecture/governance work，使第三方 Human / Agent 可以尽早参与资料、Candidate、Evidence 和普通 Patch，而不同时开放底层 Schema / Governance authority。

## Historical P4.5 decisions

P4.5 当时确认：

- Human / Agent 共用同一个 Canonical knowledge world；
- Shared knowledge ≠ shared authority；
- Identity / Capability / Task Authority / Review Authority / Platform Permission 正交；
- access 不只是 read/write；
- GitHub Actor / credential 不等于实际 Executor 或 Owner authority；
- Capability 按领域表达；
- Task Authority 与 Mutation Impact 组合而不互相替代；
- Agent 可研究、读取、查询、生成候选、验证和在授权范围内执行，但不能自授高影响 acceptance authority；
- Human 同样受 evidence/validation/review 约束；
- self-check ≠ independent review；CI/Validator ≠ Reviewer；
- Delegation 必须 bounded / explicit / revocable；
- Workspace collaboration state 不自动成为 Canonical；
- 开放 Intake 可以先开放低风险 Candidate / Evidence / ordinary Patch，而不同时开放 Schema / Governance。

这些边界后来由当前 Master Design、Agent Attribution、Task Authority、Collaboration 与 Onboarding 文档继续承接。