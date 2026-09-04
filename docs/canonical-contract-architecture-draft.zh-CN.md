# InteropAtlas Canonical Contract V1 Architecture — Draft

<!-- InteropAtlas Document Metadata v0
Document Status: Architecture Draft
Document Created At: 2026-09-04T06:12:00+08:00
Metadata Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Human review
  GitHub Actor: ff6962757
-->

> Status: Architecture Draft — P4.1
>
> Primary Work Item: Issue #127
>
> Purpose: 固化 P4.1 已收敛的 Canonical Contract V1 语义边界，作为 P4.2 Write / Intake Contract 与 P5 real-data validation 的架构输入。本文不是最终字段级 Schema，也不授权数据迁移。

## 1. Architecture stance

InteropAtlas V1 采用：

> **Stable Canonical Core + explicit composable semantic contracts / profiles**

而不是继续扩张一个承担所有语义的万能 Object Schema。

这里的“分层”首先是语义职责分离，不预设最终必须拆成多少文件、JSON Schema、服务或数据库表。

核心不变量：
- Stable IA identity 独立于 display name、physical path、Source URL、external identifier；
- Physical Storage ≠ Semantic Classification ≠ View；
- Relation 是一等知识资产；
- binary relation 是常见 fast path，但不是 V1 的通用上限；
- Source ≠ Evidence ≠ Assertion ≠ Assessment ≠ Provenance；
- Fact ≠ Assessment；
- Canonical State ≠ Generated View；
- Agent Output ≠ Canonical Fact；
- conflict / competing assertions 可以被保留；
- public knowledge lifecycle ≠ personal attention / memory metabolism；
- Legacy compatibility 是迁移基础设施，必须存在 retirement endpoint。

## 2. Five semantic contract surfaces

### 2.1 Identity Contract

回答：**这个 Canonical Subject / Record 是谁？**

V1 至少在概念上区分：

1. **IA Canonical ID** — InteropAtlas 控制的稳定内部身份，用于引用、relation endpoint 与 migration continuity。
2. **External Identifier** — 外部 authority / namespace 授予的 identifier，是 identity resolution evidence/key，不自动替代 IA ID。
3. **Locator / Access Address** — URL、文件路径、下载入口等；回答“在哪里访问”，不回答“它是谁”。
4. **Human Name / Label** — 官方名称、简称、译名、历史名称等；允许多值、语言和时间变化，不承担唯一身份。

Identity resolution 原则：same identifier / URL / name 都不能单独推出 same Canonical Subject。

Version / edition / snapshot / profile 是否形成独立 Canonical Subject 不采用全局硬编码规则。V1 必须能表达 work/family 与 version/edition 的身份关系，具体 granularity 由 P5 使用 RFC、ISO、W3C、living standard、API/profile 等真实样本压力测试。

Identity mutation 必须区分：duplicate candidate、suspected equivalence、confirmed merge、alias/redirect、predecessor/successor、supersedes/replaces、split/unmerge correction。

Canonical merge 属高影响 mutation：必须有 evidence/rationale、保留旧 ID 可解析性、保留 provenance/decision trail，并使用高于普通 patch 的 review/authority gate。

### 2.2 Entity / Object Contract

回答：**这是哪类可独立识别的知识对象？**

V1 使用两层职责：
- **Family**：少量、稳定，用于决定基础 semantic contract / profile family；
- **Kind**：更具体、可扩展的 domain classification，用于检索、约束和专用 profile。

Family / kind 不重新决定物理目录结构，也不承载 publication status、authority、maturity、validity 等评价或生命周期语义。

当前不冻结完整 taxonomy。P5 需要验证：
- family 的最小充分集合；
- kind 是否允许多值 / secondary roles；
- Standard / Method / Organization / Capability / Implementation / Scenario 等真实对象如何归类；
- 某些跨角色对象是否应由 kind + relation/capability 表达，而不是复制对象。

### 2.3 Relation / Association Contract

回答：**哪些参与者以什么语义发生联系？**

V1 保留 simple binary relation 作为最常见表达，但通用架构不能假定所有关系永远只有 subject/object 两个无角色端点。

必须为 richer association 留出边界：relation instance 可在需要时拥有多个 participants、participant roles、qualifiers/context。

Relation/association semantics 与 statement/provenance semantics 分离：参与者不是 evidence，provenance actor 也不是默认 relation participant。

哪些 relation 需要 richer association 不在 P4 全局枚举；由 P5 真实数据验证后决定。

## 3. Knowledge Claim / Evidence Contract

回答：**InteropAtlas 在断言什么、依据是什么、如何形成当前知识状态？**

### 3.1 Five distinct concepts

- **Source**：可定位的信息来源或来源实体。
- **Evidence**：某个 Source 中被实际用于支持、反驳或限定某个知识判断的可追踪依据。
- **Assertion**：关于某个 subject / relation / proposition 的可判断陈述。
- **Assessment**：基于事实与证据形成的评价、评分、置信判断、成熟度判断或解释。
- **Provenance**：记录知识资产或变更由谁、何时、通过什么过程产生、转换、审核、接受。

这些概念可以相互引用，但不能互相替代。

### 3.2 Canonical knowledge does not require one forced truth at intake

V1 必须能够保留：
- competing assertions；
- conflicting evidence；
- unresolved / unknown state；
- later correction / supersession；
- assertion-specific evidence/provenance where needed。

“没有值”不能同时表示 unknown、not applicable、not yet researched、withheld、conflicting、not verified。具体 serialization 留给后续 contract/schema design，但语义上必须可区分。

### 3.3 Canonical acceptance and truth are different questions

一个 Assertion 被接受进入 Canonical substrate，表示它通过了项目定义的 intake/review boundary；不意味着 InteropAtlas 宣称它是不可争议的绝对真理。

Canonical 可以包含“存在争议”“来源 A 如此断言”“当前证据不足”等经过审查、可追踪的知识状态。

Agent generation 默认是 Candidate Assertion / Proposal / Patch / Evidence，不因写入仓库或由高能力模型生成就自动成为 Canonical Fact。

### 3.4 P5 validation items

P4 不冻结：
- Assertion 是否在所有情况下都成为独立持久 artifact；
- record-level / assertion-level / relation-level evidence 的最小充分粒度；
- Context / Scope 的具体 attachment points；
- competing assertions 的默认 projection/query policy。

## 4. Lifecycle / State Contract

回答：**记录本身、现实对象、发布制度、验证状态与评价分别处于什么状态？**

V1 不采用单一 `status` 字段或单一线性状态机承担全部生命周期语义。采用多个正交维度，使诸如“已被新版取代，但仍大量部署，而且刚刚核验过”的状态可以同时成立。

至少概念上区分：

1. **Repository Record Lifecycle** — draft / candidate / accepted / archived / deleted-like repository handling。
2. **Real-world Validity / Applicability** — 当前是否有效、适用，以及适用 scope/time/context。
3. **Publication / Version Status** — draft、candidate、published、recommendation、withdrawn 等由外部制度定义的发布状态；不得与项目内部 record lifecycle 混用。
4. **Verification / Freshness State** — 何时核验、核验了什么、依据何在；“旧”不自动等于“错”。
5. **Authority / Confidence / Maturity Assessment** — 属于 Assessment，不冒充事实 lifecycle；必须可追踪依据与评价主体。
6. **Supersession / Historical State** — superseded、replaced、historically important、legacy-but-deployed 等关系/状态；superseded 不自动等于 invalid 或 deleted。

时间戳与状态语义也必须分开：created/updated/verified/published/effective/retired 等时间不是一个通用 `last_updated` 可以完整表达的。

## 5. Cross-contract rules

### 5.1 Classification is not lifecycle

`family/kind` 说明“是什么”，不说明“是否成熟、有效、官方、最新”。

### 5.2 Identity is not equivalence

外部 identifier、相同名称、相同 URL、same-as candidate 与 confirmed canonical merge 必须分开。

### 5.3 Evidence is not provenance

Evidence 支持知识判断；Provenance 解释知识资产/变更如何形成。一个来源可以同时参与两者，但职责不同。

### 5.4 Supersession is not deletion

被替代的知识仍可能具有历史、兼容性、部署或解释价值。

### 5.5 Canonical is not a generated projection

Search、Compare、Graph、Article、Timeline、Workspace 等可以选择、聚合和呈现 Canonical knowledge，但不得因为 projection 方便就反向改变 Canonical semantics。

## 6. What P4.1 settles vs defers

### Settled architecture boundaries

- stable IA identity / external identifier / locator / name 分离；
- governed identity resolution / merge；
- family / kind 职责分离，不绑定物理路径；
- binary common relation + richer association extension boundary；
- Source / Evidence / Assertion / Assessment / Provenance 分离；
- competing/conflicting/unknown knowledge state 可保留；
- multi-dimensional lifecycle/state；
- Candidate/Agent output 与 accepted Canonical state 分离。

### Deferred to P5 real-data validation or later P4 serialization design

- final family/kind taxonomy and enums；
- version identity granularity；
- richer association promotion criteria；
- Assertion persistence/granularity；
- Evidence granularity；
- Context/Scope attachment model；
- lifecycle enums and combination constraints；
- default conflict projection/query behavior；
- YAML/JSON serialization, physical file layout and final field names。

## 7. Handoff to P4.2 — Canonical Write / Intake Contract

P4.2 应基于本文建立以下 mutation pipeline 的架构边界：

`Candidate Assertion / Proposal / Patch + Evidence → validation → independent review / authority gate → Canonical mutation`

P4.2 至少需要回答：
- 哪些输入可以直接进入 candidate layer；
- evidence minimum 与 evidence exceptions 如何表达；
- machine validation、semantic review、authority approval 分别负责什么；
- conflict 是 reject、preserve 还是 escalate；
- identity merge、destructive change、supersession 等高影响 mutation 如何升级 gate；
- Human 与 Agent 如何共享 intake contract，但不共享无边界写权限；
- accepted mutation 如何保留 provenance 与可回滚/纠错路径。

P4.2 仍属于 Architecture / Decision 阶段，不自动执行 V1 migration。
