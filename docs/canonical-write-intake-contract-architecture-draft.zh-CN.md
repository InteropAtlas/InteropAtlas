# InteropAtlas Canonical Write / Intake Contract V1 — Architecture Draft

<!-- InteropAtlas Document Metadata v0
Document Status: Architecture Draft
Document Created At: 2026-09-04T06:18:00+08:00
Metadata Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> Status: Architecture Draft — P4.2
>
> Primary Work Item: Issue #127
>
> Upstream: `docs/canonical-contract-v1-architecture-draft.zh-CN.md`
>
> Purpose: 定义 Candidate / Proposal / Patch / Evidence 如何经过 validation、review 与 authority gate 进入 Canonical substrate。本文定义语义与治理边界，不实现权限自动化，不执行数据迁移。

## 1. Core pipeline

Canonical write path 采用：

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

核心原则：**write capability ≠ canonical acceptance authority**。

Human、Agent、自动工具都可以产生输入；是否成为 Canonical knowledge 由 mutation class、evidence、validation、review 与 authority 决定，而不是由“谁有 GitHub 写权限”单独决定。

## 2. Intake artifact classes

### 2.1 Candidate Assertion

提出一个尚未被 Canonical 接受的知识陈述。可以来自 Human、Agent、importer、research task 或外部数据源。

Candidate Assertion SHOULD 能携带：
- subject / proposition intent；
- supporting or contradicting evidence；
- source/context/scope；
- proposer/executor provenance；
- uncertainty / unresolved conflict where known。

Candidate 不因来源权威、Agent confidence 高或已写入 branch/Issue 而自动升级为 Fact。

### 2.2 Proposal

提出结构、分类、关系、解释或治理层面的候选改变，但不必已经表示成精确 patch。

适合：
- 新 Object / Relation 建议；
- identity equivalence candidate；
- taxonomy/profile extension；
- lifecycle interpretation；
- architecture/governance change。

### 2.3 Patch

对已存在 Canonical artifact 的具体候选 mutation。Patch 是“建议如何改”，不是“改动已经获得语义批准”。

### 2.4 Evidence contribution

可以只增加或改进 Evidence，而不立即改变现有 Assertion。新 Evidence 与现有 Canonical conclusion 冲突时，默认先保留冲突并触发 review/revalidation，而不是静默覆盖旧事实。

## 3. Mutation classes

Gate 强度由 **mutation semantics / impact** 决定，不只由文件大小或提交行数决定。

### M0 — Additive evidence / metadata

示例：
- 增加来源；
- 增加 evidence locator；
- 补 provenance；
- 非语义性的 metadata correction。

默认风险较低，但仍必须通过 structural validation；不能借 M0 偷渡事实变化。

### M1 — Ordinary canonical knowledge mutation

示例：
- 新增经过支持的普通 Assertion；
- 修正一般事实；
- 新增普通 binary Relation；
- 更新已核实的 publication/version facts。

需要 evidence-aware semantic review；是否必须独立 reviewer 由 operational profile 决定，但 Agent self-confidence 不构成 review。

### M2 — Structural / semantic mutation

示例：
- 新 Object family/kind/profile；
- richer association / role semantics；
- 改变某类事实的解释边界；
- 跨对象的大范围语义重分类；
- 影响 validator/migration contract 的非破坏性模型改变。

需要 independent review，并应由相应 capability scope 的 Maintainer 批准。

### M3 — High-impact identity / destructive / governance mutation

示例：
- confirmed identity merge / split；
- destructive schema migration；
- 大规模删除；
- Canonical ID retirement without safe redirect；
- project definition/scope/governance/security/license/release 等高影响改变。

必须进入 Human Maintainer / Owner / Governance gate；不能由执行 Agent 自批。

M0–M3 是 P4 architecture vocabulary，不直接替代现有 Task Authority T0–T3 或 Review Class。前者描述 **mutation impact**，后者描述 **谁能 Claim / 谁能 Review**；后续可建立映射，但不能压成一个维度。

## 4. Gate responsibilities

### 4.1 Structural & Machine Validation

机器层负责回答“结构上是否可接受”，例如：
- schema/profile compatibility；
- required identity/reference resolution；
- relation endpoint integrity；
- syntax / controlled vocabulary / invariant checks；
- migration compatibility / graph checks where applicable。

Machine PASS 只证明可解析/满足规则，不证明事实真实、证据充分或治理上可接受。

### 4.2 Semantic Review

语义 Review 负责回答：
- Assertion 是否准确表达 Evidence；
- Source/Evidence 是否相关且足够；
- Fact 与 Assessment 是否混淆；
- Context/Scope 是否遗漏导致误导；
- conflict 是否被正确保留；
- identity/version/relation semantics 是否合理；
- mutation class 是否被低估。

Reviewer 应与 Executor 的角色可区分。对于 normal low-risk work，可由另一个 Human 或 Agent 做 independent review；高影响工作最终授权不能由 Agent self-review 代替。

### 4.3 Authority Gate

Authority Gate 不重复做全部 semantic review，而回答：**即使内容合理，这类改变是否有权进入 Canonical / stable project contract？**

它与 GitHub merge permission 分离。

当前保守映射：
- M0/M1：按现有 operational profile 执行；
- M2：Maintainer capability-scope approval；
- M3：Human Maintainer / Owner / Governance 明确批准，具体依据 Task Authority Governance 与 stable policy 演进。

## 5. Evidence policy

默认原则：**Evidence Before Assertion**。

但“不存在公开来源”本身有时是研究结果，因此 V1 不采用机械的“每个字段必须有 URL”规则。允许的 evidence exception 必须显式可辨，例如：
- direct repository observation；
- reproducible machine observation/test；
- project-owned governance decision；
- explicitly marked hypothesis / unresolved candidate；
- absence finding with documented search scope。

Exception 不是免除 provenance；反而更需要说明“依据是什么、如何得到”。

Assessment 必须能追踪其事实输入、评价主体或方法，不能把评分/成熟度直接伪装成外部事实。

## 6. Conflict handling

发现冲突时，默认流程不是“最后写入者覆盖”：

```text
new evidence/assertion
→ detect conflict
→ preserve competing state
→ review context/scope/version/authority
→ accept one, retain both with qualification, supersede, or escalate
```

允许的结果包括：
- 两个 Assertion 在不同 scope/context 下都成立；
- 一个 Assertion supersede 另一个，但历史仍保留；
- Evidence 不足，保持 unresolved；
- 旧 Assertion 被 invalidated/corrected，但 provenance/history 保留；
- 冲突升级到更高 authority gate。

Canonical substrate 的目标是保存可审计知识状态，而不是制造表面上的单一答案。

## 7. Human + Agent write boundary

Human 与 Agent 使用同一个 intake contract，但不因此获得相同的无边界 authority。

### Agent default

Agent 默认可以：
- research / collect sources；
- generate Candidate Assertion / Proposal / Patch；
- run validation；
- perform independent review when policy allows and it不是自身执行产物的最终高影响批准；
- report uncertainty/conflict。

Agent 默认不能仅凭自身输出：
- 宣告高影响 identity merge；
- 执行 destructive migration；
- 将 architecture/governance draft 提升为 stable specification；
- 把生成内容自动视为 Canonical Fact。

### Human boundary

Human 也不因“是人”自动绕过 evidence/validation。Owner/Maintainer authority 解决的是治理授权，不替代事实证据。

## 8. Acceptance event and provenance

Accepted Canonical Mutation 必须能够追踪：
- candidate/proposal/patch 来源；
- executor；
- evidence basis；
- validation result；
- reviewer；
- approver when required；
- accepted mutation / commit / PR；
- acceptance time；
- later correction / supersession path。

完整 event history 继续由 Git/GitHub 承担，不在 Canonical record 内复制完整 change log。Canonical 只保留查询和再验证所需的最小 provenance projection。

## 9. Rejection is not deletion

未接受的 Candidate / Proposal 不应自动被当成垃圾删除。对有研究价值、冲突价值或未来复核价值的输入，可以保留在 Issue/PR/research artifact/candidate pool 中。

这使 rejected / deferred / unresolved 与 false / invalid 明确分离。

## 10. P5 validation items

P4.2 暂不冻结：
- M0–M3 的最终名称和所有映射表；
- 每类 mutation 的最小 Evidence 数量；
- 哪些 M1 必须 independent review；
- assertion-level review 的最终序列化；
- automated confidence threshold；
- conflict detection 的实现算法；
- Agent capability/identity 的技术认证方式；
- GitHub Project fields / bot / ruleset automation。

P5 应用真实 intake 样本验证 gate 是否过重或过松，尤其覆盖：普通标准新增、版本状态更新、冲突来源、relation 新增、identity duplicate candidate、Agent-generated patch。

## 11. Handoff to P4.3 — Migration Architecture

P4.3 必须在不改变上述 write boundary 的前提下回答：
- Legacy record 如何映射成 V1 Candidate / migration patch；
- stable IA IDs 如何保留；
- 无法确定的字段如何进入 unknown/conflict 而不是猜值；
- migration batch 如何经过 machine validation + semantic review；
- Legacy compatibility 何时、以什么条件退役；
- migration rollback / correction 如何保留 provenance。
