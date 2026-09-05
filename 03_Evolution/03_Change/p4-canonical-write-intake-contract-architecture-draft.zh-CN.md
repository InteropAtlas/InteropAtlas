# Canonical Write / Intake Contract V1 — P4.2 Historical Architecture Draft

> Lifecycle: **Historical / Superseded by Active V1 Core Architecture and current governance profiles**
>
> Original Phase: P4.2 — Canonical Write / Intake Contract
>
> Primary Work Item: Issue #127
>
> Successor: `docs/architecture.zh-CN.md` + current Intake / Governance / Collaboration profiles
>
> Current Role: 保存 Candidate → Validation → Review → Acceptance 写入边界的形成历史；不再作为 `docs/` 中的当前 Living Contract。

## Historical synthesis

P4.2 的核心结论是：

> **write capability ≠ canonical acceptance authority**

它将 Canonical 写入从“谁有 GitHub 写权限谁就能改事实”重构为受治理的知识接受路径：

```text
Observation / Source / Existing Record
        ↓
Candidate / Proposal / Patch + Evidence
        ↓
Structural & Machine Validation
        ↓
Semantic Review
        ↓
Authority Gate (when required)
        ↓
Accepted Canonical Mutation
        ↓
Provenance + Revalidation / Correction Path
```

### Intake artifact classes

P4.2 区分 Candidate Assertion、Proposal、Patch 与 Evidence contribution。候选内容不会因为来自 Human、Agent、权威来源、branch 或高模型置信度就自动成为 Canonical Fact。

### Mutation impact

P4.2 用 M0–M3 作为阶段性架构 vocabulary，区分 additive evidence / metadata、ordinary knowledge mutation、structural / semantic mutation 与 high-impact identity / destructive / governance mutation。

它同时明确：Mutation Impact 描述“变化有多大”，Task Authority / Review Class 描述“谁能 Claim / Review / Approve”，二者不能压成同一个维度。当前名称和具体映射应读取现行 Governance / Collaboration Profiles。

### Validation / Review / Authority

Machine Validation 负责结构、Schema/Profile compatibility、reference resolution、relation integrity 与可自动检查的不变量；Machine PASS 不证明事实真实。

Semantic Review 检查 Assertion 是否准确表达 Evidence、Scope / Context 是否充分、Fact 与 Assessment 是否混淆、conflict 是否保留、identity/version/relation semantics 是否合理，以及 mutation impact 是否被低估。

Authority Gate 回答某类改变是否有权进入 Canonical / stable project contract，而不是重复做全部语义审查。

### Evidence policy

默认采用 **Evidence Before Assertion**，但不机械要求每个字段必须有 URL。Direct repository observation、reproducible machine observation/test、project-owned governance decision、明确 hypothesis / unresolved candidate，以及有搜索范围记录的 absence finding 都可能形成有效 Evidence 路径；例外仍需 Provenance。

### Conflict handling

新证据与现有 Canonical conclusion 冲突时，默认不是最后写入覆盖，而是保留 competing state、检查 context / scope / version / authority，再决定接受一个、限定两者、supersede、保持 unresolved 或升级治理。

### Human + Agent boundary

Human 与 Agent 使用同一个 Intake Contract，但不因此拥有相同无边界 authority。Agent 可以研究、收集 Evidence、生成 Candidate / Proposal / Patch、运行 Validation，并在政策允许时进行独立 Review；执行 Agent 不能仅凭自身输出批准高影响 identity / destructive / governance mutation。

Human 也不能因为“是人”而绕过 Evidence 与 Validation。Owner / Maintainer authority 是治理授权，不替代事实依据。

### Acceptance provenance

Accepted Canonical Mutation 应能够追踪 candidate/proposal/patch 来源、executor、evidence basis、validation、reviewer、必要 approver、accepted mutation / commit / PR、acceptance time 与后续 correction / supersession path。完整 event history 仍由 Git/GitHub 承担，不复制进每条 Canonical record。

## Supersession note

2026-09-05 文档生命周期审计确认，P4.2 的长期有效边界已经成为 V1 Core Architecture 与当前 Governance / Collaboration 体系的一部分。继续将阶段 Draft 放在 `docs/` 会制造第二套 Intake 定义。

因此，本轮将其核心架构提升至 `docs/architecture.zh-CN.md`，阶段性 vocabulary、Not Yet 决策和形成过程保存在本文中。具体当前可执行规则应读取现行 Profile / Governance，而不是从 P4.2 Historical Draft 推断。
