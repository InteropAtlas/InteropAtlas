# InteropAtlas Minimum Knowledge Representation Contract v0.1 — Maintainer Approval Record

<!-- InteropAtlas Document Metadata v0
Document Status: **APPROVED / ADOPTED**
Document Created At: 2026-09-01T19:40:59+08:00
Document Updated At: 2026-09-01T19:40:59+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：**APPROVED / ADOPTED**
>
> 日期：2026-09-01
>
> Work Item：#58
>
> Decision PR：#59
>
> Approved revision commit：`18b062b6193a7f7ff0636c700ecf5edebf1da437`

## 决策

Maintainer 已明确批准 PR #59 中经 Decision Stress Test 修订后的 **InteropAtlas Minimum Knowledge Representation Contract v0.1**。

本批准针对以下核心语义模型：

```text
Stable Identity
↓
Core Identity Family
↓
Kind / Strong Profile
↓
Object Properties
↓
Roles / Relations
↓
Statement / Claim
↓
Context / Qualifier
↓
Evidence / Provenance
↓
Assessment
↓
Validation Contract
↓
Projection / View / Query
```

### Adopted Core Identity Families

v0 采用 4 个 Core Identity Families：

```text
concept
artifact
system
agent
```

`capability` 与 `scenario` 保留为强类型 Concept Profiles；Method、Framework、Principle、Conceptual Model 等同样通过 `concept` family 下的 `kind` / Profile 表达。

### Adopted Identity Target Rule

在选择 family 前，必须先明确 stable ID 实际指向的现实或概念身份。不得仅根据对象名称进行分类。

### Adopted boundaries

本批准同时接受决策稿中 D1–D10 的主要边界：

- `type` / `kind` / Strong Profile / roles / authority 分离；
- Object Property 与 Statement / Claim 分离；
- v0 定义 Statement 逻辑合同，但不要求全部字段立即 Statement 化；
- Context / Qualifier、Evidence / Provenance、Fact / Assessment 分层；
- known / unknown / explicit none / not recorded 语义区分；
- Concept / versioned Artifact / System / Distribution / Part 的 identity split rule；
- Agent / System identity split rule；
- Semantic Model、Validation、Serialization、Physical Storage、Query Projection 相互解耦；
- graph-native、database-agnostic；
- Activity / Event 仅作为未来 evidence-driven extension slot，不在 v0 预先增加第五个 Core Family。

## 采纳边界

本批准意味着：

1. PR #59 中的修订模型可以合并并作为后续设计的正式上游原则；
2. #58 可以在合并后关闭为 completed；
3. 后续 Schema、Compatibility Layer、Engine dual-read、Representative Migration Pilot 应以此模型为依据。

本批准 **不等于** 立即批准以下实施动作：

- 不在本次 Decision PR 中修改 JSON Schema；
- 不在本次 Decision PR 中迁移 Canonical Data；
- 不在本次 Decision PR 中修改 Engine；
- 不在本次 Decision PR 中进行全量 legacy type 替换；
- 不改变物理目录结构；
- 不选择数据库或发明 IA Query Language。

这些属于下一阶段单独的 Schema / Compatibility Design 与 Migration Pilot。

## Historical note

`knowledge-representation-model-decision-v0.1.zh-CN.md` 保留其被审阅时的 Revised Draft / High-impact 状态文本，作为决策形成过程的历史记录；本文件是对该特定修订版本的正式采纳记录，避免在批准后重写已审阅的 Decision Draft 内容。
