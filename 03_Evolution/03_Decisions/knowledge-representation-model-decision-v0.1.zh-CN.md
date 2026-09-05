# InteropAtlas Minimum Knowledge Representation Contract v0.1 — Model Decision Draft

<!-- InteropAtlas Document Metadata v0
Document Status: **Revised Draft / High-impact Decision — NOT ADOPTED**
Document Created At: 2026-09-01T18:49:47+08:00
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

> 状态：**Revised Draft / High-impact Decision — NOT ADOPTED**
>
> Work Item：#58
>
> Parent：#15
>
> 目的：基于既有标准、成熟数据语言技术栈、10 个真实对象 Fit Test，以及对初稿的 Decision Stress Test，收敛 InteropAtlas v0 的最小知识表示合同。
>
> 本文件仍然只是决策草案。它不修改 Schema、不迁移数据、不改变物理目录；只有 Maintainer 明确批准后，才能进入正式规范与实现阶段。

## 0. Revision Note

初稿提出 6 个顶层 Reality Identity Families：

```text
artifact
practice
system
agent
capability
scenario
```

随后对当前 Canonical Schema、现有对象和边界案例进行压力测试，发现这个集合仍混合了不同抽象层级：

- `artifact / system / agent` 更像稳定身份形态；
- `practice` 对 Method 很自然，但对 Capability / Scenario / Conceptual Model 过窄；
- `capability / scenario` 非常重要，但更适合作为 InteropAtlas 的强类型概念 Profile，而不是与 Artifact / System 平级的上位本体类别。

因此本修订稿将 D1 收敛为 **4 个 Core Identity Families**：

```text
concept
artifact
system
agent
```

并明确：

```text
capability / scenario / method / framework / principle ...
→ concept family 下的 kind / strong profile
```

完整压力测试记录见：

`../01_Research/knowledge-representation-decision-stress-test-v0.1.zh-CN.md`

---

# 1. Decision Context

InteropAtlas 当前真正需要定义的，不是一张不断扩大的对象分类表，而是一套足够小、可演化、可投影的知识语言语义骨架。

前置研究已经覆盖：

- ISO 704：object / concept / definition / designation 分离；
- W3C SKOS、ISO 25964：Concept Scheme、关系和 vocabulary mapping；
- Wikibase / Wikidata：Entity / Statement / Qualifier / Reference / Rank；
- W3C PROV-O、DCMI：Agent、Role、Attribution、creator / contributor / publisher 分离；
- W3C DCAT：Dataset / Distribution / DataService / Catalog 等资源身份分离；
- CIDOC CRM / ISO 21127：异构知识的高层语义整合；
- SHACL / JSON Schema：语义模型与机器验证合同分离；
- SQL、RDF、Wikibase、Property Graph / GQL：数据模型、约束、查询、投影的完整技术栈比较；
- 10 个真实对象 Fit Test：Diátaxis、Card Sorting、Nielsen 10 Heuristics、GOV.UK Design System、Docs as Code、MDN Browser Compat Data、GitHub Community Health、NIST AI RMF 1.0、Munzner Nested Model、USWDS；
- 当前 Canonical Schema 反向压力测试：Standard、Reference Project、Implementation、Organization、Capability、Scenario、Relation、Open Gap、Map。

这些证据已经足够做 v0 Model Decision。

除非本修订稿仍暴露一个会改变模型结构的明确二选一问题，不再开启无边界 Batch 3。

---

# 2. Decision Summary

本 Draft 提议 InteropAtlas v0 使用以下逻辑骨架：

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

核心原则：

> **对象是什么，不等于 Atlas 为什么引用它，也不等于 Atlas 如何评价它。**

> **先确定 stable ID 到底指向什么，再选择 family；不得仅根据名称做分类。**

> **语义模型决定知识怎样被准确表达；Schema、YAML、数据库和查询语言只是它的实现、验证或投影。**

---

# 3. Rejected Alternatives

## A. 每个现实名词一个顶层 `type`

例如：

```text
method
framework
heuristic
guideline
design_system
dataset
publication
capability
scenario
convention
...
```

**Reject.**

原因：

- 10 个样本已经证明现实对象经常具有多个角色；
- taxonomy 会快速膨胀；
- type 变更会持续制造 Schema / Query / migration 成本；
- 很多差异应由 kind、Profile、role、relation、authority 或 lifecycle 表达。

## B. 一个万能 `reference` / `practice` / `reference_project`

**Reject.**

原因：

- `reference` 描述 Atlas 为什么引用对象，不是 reality identity；
- Card Sorting、BCD、USWDS、AI RMF 1.0 的现实生命周期完全不同；
- 当前 `reference_project` 已经实际把 Method、Guidance、Design System、Convention 等强行 Project 化。

## C. 初稿 6-family 模型

```text
artifact / practice / system / agent / capability / scenario
```

**Superseded by this revision.**

原因：

- 顶层类别不够正交；
- `practice` 无法自然覆盖所有抽象 Concept；
- Capability / Scenario 应保留专业结构，但不必因此占用顶层 identity family。

## D. 直接复制完整 Wikibase

**Reject for v0.**

Statement / Qualifier / Reference 分层值得采用，但当前 Atlas 不需要把所有简单字段一次性改造成 Statement records。

## E. 强制 RDF / OWL 作为 Canonical Storage

**Reject for v0.**

RDF 是重要语义参考和未来投影目标，但 YAML 仍适合当前 Human / Agent authoring。

## F. 直接采用某个 Property Graph / SQL Schema

**Reject.**

工程存储和查询能力不能反向决定现实语义。

## G. Query-language-first

**Reject.**

当前不发明 IA Query Language。查询必须建立在稳定语义合同之上。

---

# 4. D1 — Core Identity Families

## Decision

v0 提议只定义 **4 个 Core Identity Families**：

```text
concept
artifact
system
agent
```

它们回答的是：

> **这个 stable ID 主要指向哪一种存在 / 身份形态？**

它们不是完整 taxonomy，也不是目录分类。

## 4.1 Identity Target Rule

在选择 family 之前，维护者 **MUST** 先回答：

> **这个 stable ID 实际指向什么？**

不得先看到名称，再从 taxonomy 中挑一个“看起来最像”的 type。

同一个名称可能同时让人联想到：

- 抽象概念；
- 官方发布物；
- 持续维护系统；
- 责任主体。

只有当这些现实身份具有独立查询、版本、生命周期、Evidence 或 attribution 价值时，才拆成多个对象。

### Apple HIG 示例

如果 stable ID 指 Apple 持续发布维护的完整 HIG guidance resource：

```text
type: artifact
kind: guidance_document
```

如果另有一个 ID 指某个独立设计原则概念：

```text
type: concept
kind: principle
```

### NIST AI RMF 示例

```text
AI RMF framework family
→ concept / framework

AI RMF 1.0 publication
→ artifact / publication
```

### Munzner Nested Model 示例

```text
Nested Model
→ concept / conceptual_model

2009 paper
→ artifact / publication
```

### MDN BCD 示例

```text
maintained project
→ system / data_project

dataset
→ artifact / dataset

distribution
→ artifact / distribution
```

---

## 4.2 Concept

**定义：** 不依赖某个单一物理、运行或发布实例才能成立的抽象知识对象、能力、方法、模型、规则概念或情境描述。

候选 kinds / profiles：

```text
capability
scenario
need
constraint
method
methodology
framework
conceptual_model
guideline
principle
heuristic_set
practice
approach
convention
workflow_pattern
architecture_pattern
...
```

典型：

- Card Sorting；
- Docs as Code；
- Diátaxis 方法；
- Nielsen Heuristics；
- Munzner Nested Model；
- AI RMF framework family；
- InteropAtlas Capability；
- InteropAtlas Scenario。

### Strong Concept Profiles

某些 Concept 对 InteropAtlas 特别重要，需要强结构 Profile，而不是只用自由 `kind`。

#### Capability Profile

现有结构原则保留：

```text
category
layers
domains
parent_capabilities
constraints
```

逻辑身份变成：

```text
type: concept
kind: capability
profile: capability
```

具体机器字段是否显式使用 `profile`，后续 Schema 设计决定。

#### Scenario Profile

现有结构原则保留：

```text
actors
requires
environment
success criteria
```

逻辑身份：

```text
type: concept
kind: scenario
profile: scenario
```

所以“上位 family 收敛”并不意味着抹掉 IA 的专业对象结构。

---

## 4.3 Artifact

**定义：** 可以被独立引用、发布、保存、版本化、分发或获取的信息 / 数据产物。

候选 kinds：

```text
standard
specification
protocol
profile
interface_specification
publication
guidance_document
dataset
distribution
schema
format
report
release
reference_architecture
catalog_artifact
...
```

重要：

- Artifact 不等于 Formal Standard；
- authority / normative status 是单独维度；
- 同一个 living Concept 或 System 可以产生多个 Artifact；
- 独立 version / edition 在确有查询价值时可拥有独立 Artifact identity。

典型：

- ISO/W3C 具体标准版本；
- NIST AI RMF 1.0；
- Munzner 2009 paper；
- MDN BCD Dataset；
- npm Distribution；
- Apple HIG 官方 guidance resource。

---

## 4.4 System

**定义：** 具有独立工程、产品、运行或维护生命周期的具体系统、实现、服务、设备或项目资源集合。

候选 kinds：

```text
software
library
tool
service
platform
hardware
firmware
design_system
data_project
knowledge_base
registry
catalog_system
platform_mechanism
governance_system
...
```

典型：

- GitHub Actions；
- Forgejo Actions；
- GOV.UK Design System；
- USWDS；
- MDN BCD maintained project；
- GitHub Community Health platform mechanism（当 ID 指实际产品机制）。

### System / Artifact split

```text
software / library product identity
→ system

release / binary / package / distribution
→ artifact（当需要独立 identity）
```

不得仅因为某个 System “有版本”就自动为每一个版本创建对象；拆分仍遵守 D9 的独立 identity / lifecycle 规则。

---

## 4.5 Agent

**定义：** 能够承担 creator、author、maintainer、publisher、issuer、governor、contributor、assertor、assessor 等责任角色的独立行动主体。

候选 kinds：

```text
person
organization
project_team
community
software_agent
...
```

当前 Organization 自然映射：

```text
type: agent
kind: organization
```

### Agent / System overlap rule

软件 Agent 可能同时具有“软件产品”和“行动主体”的特征。

v0 使用 Identity Target Rule 避免双重 primary family：

- 如果 ID 指软件产品 / runtime / implementation → `system`；
- 只有当现实中存在一个需要被独立归因、授权、签名、声明或追踪的 actor identity 时，才建立独立 `agent`；
- 两者通过 relation 连接。

因此未来可能存在：

```text
Agent actor identity A
  agent / software_agent

Agent runtime/product X
  system / software
```

只有有真实查询 / provenance 价值时才拆。

---

## 4.6 Not Core Identity Families

以下概念不作为 4 个 Core Family 的平级分类：

```text
Relation / Statement
Evidence / Source
Assessment / Gap Finding
Map / View / Index
Reference / Precedent role
Maturity / Recommendation
```

它们属于 Statement、Evidence、Assessment、View 或 Role 层。

### Future extension slot: Activity / Event

PROV-O 等成熟模型表明，未来测试、认证、采用、发布、迁移等 Activity / Event 可能需要第一等 stable identity。

当前 Atlas 尚没有足够需求证明必须马上增加第五个 Core Family。

因此 v0 **MUST NOT** 预先加入 `activity/event`；但也 **MUST NOT** 用当前设计阻断未来 evidence-driven extension。

---

# 5. D2 — `type` vs `kind` vs `profile` vs `roles` vs `authority`

## Decision

### `type`

`type` 表达 Core Identity Family：

```text
concept
artifact
system
agent
```

要求：

- 数量极少；
- 变化慢；
- 不因新领域名词扩张；
- 不表达成熟度、推荐度、权威性或 Atlas 使用角色。

### `kind`

`kind` 表达 family 内更具体的现实 / 概念身份。

示例：

```text
type: concept
kind: heuristic_set
```

```text
type: artifact
kind: dataset
```

```text
type: system
kind: design_system
```

```text
type: agent
kind: organization
```

`kind` 比 `type` 更可扩展，但 **MUST** 使用受控 vocabulary / 明确定义，不能成为无约束 tag 池。

### Strong Profile

当某类对象需要明显更强的结构合同，而 `kind` 本身不足以表达机器约束时，允许定义 Profile。

典型：

```text
Capability Profile
Scenario Profile
Standard / Normative Artifact Profile
Implementation/System Profile
```

Profile 的作用是：

> 在共享 Core Identity Family 的同时，添加领域专用的结构和 validation contract。

Profile **MUST NOT** 被解释为物理目录。

### `roles`

Roles 表达对象在某个上下文中的非排他性用途，例如：

```text
human_interface_reference
compatibility_evidence_source
reference_implementation
interoperability_precedent
```

Role **MUST NOT** 替代 identity。

例如：

```text
precedent
reference
```

通常是 Atlas role；

```text
mature
recommended
```

通常是 Assessment。

### `authority` / normative status

Formal Standard、Official Guidance、Community Specification、Research Publication、Vendor Documentation 等权威性质是单独维度。

例如两个对象都可以是：

```text
type: artifact
```

但：

```text
kind: standard
authority: formal_standard
```

与：

```text
kind: guidance_document
authority: vendor_guidance
```

语义完全不同。

精确 vocabulary 后续由 Standard / Authority Profile 决定。

---

# 6. D3 — Object Property vs Statement / Claim

## Decision

InteropAtlas 在概念上 **MUST** 区分：

```text
Object Property
≠
Statement / Claim
```

## 6.1 可以保持 compact Object Property 的信息

满足以下大部分条件时可以保持简单属性：

1. 主要用于 identity / discoverability；
2. 对 identity target 相对稳定；
3. 通常只有一个 canonical value；
4. 不需要时间 / 版本 / scope 才有意义；
5. 不预期存在多来源冲突；
6. 不需要独立 Evidence lifecycle。

典型：

```text
stable id
primary name
official name
core family
kind
canonical official URL
stable external identifier
```

如果对象已经是独立 versioned Artifact，那么该 Artifact 自己的 edition/version/date 也 MAY 保持 compact property。

## 6.2 应升级为 Statement 的信息

出现任一高影响条件时，**SHOULD** 视为 Statement：

- 会随时间 / 版本变化；
- 依赖 scenario / capability / jurisdiction / environment / audience；
- 需要 condition / test method / measurement method 才准确；
- 多个来源可能给不同值；
- 需要 statement-specific Evidence；
- 需要明确谁在声称；
- 是兼容、支持、采用、推荐、成熟、适用等可争议命题；
- 关系本身需要 qualifier。

典型：

```text
Browser X 从 Version Y 开始支持 Feature Z
Site A 采用 USWDS 的 Code 层
AI RMF 当前处于修订状态
Object X 是成熟先例
System A 与 Artifact B 兼容
```

---

# 7. D4 — Statement v0 Boundary

## Decision

v0 **正式定义 Statement 的逻辑合同，但不把所有字段立即物理化成 Statement records。**

### Logical Statement

一条 Statement 至少具有：

```text
subject
predicate
value / object
value_state
qualifiers / context
provenance / evidence
assertor / assessor（适用时）
```

Relation 是 Statement 的重要特例：

```text
source   = subject
relation = predicate
target   = object value
```

## 7.1 v0 physical strategy

1. 简单稳定信息继续允许 compact Object properties；
2. 当前显式 Relation records 继续作为第一类 relationship statements；
3. Relation Schema 后续应增加 statement-level evidence / qualifier，而不是另建一套冲突的关系系统；
4. 高风险、动态、多来源、可冲突的非关系事实可以逐步升级为 explicit Statement；
5. v0 **MUST NOT** 要求一次性把所有现有 YAML 字段变成 Statements。

## 7.2 Promotion rule

Compact property → Explicit Statement 必须保持：

- Object stable ID 不变；
- 原语义不变；
- 只是获得独立 statement identity、context、provenance / evidence。

---

# 8. D5 — Context / Qualifier

## Decision

v0 不复制 Wikibase 全部 qualifier 机制，但正式保留以下通用语义维度。

### Temporal

```text
as_of
valid_from
valid_to
```

### Version

```text
version_context
edition_context
release_context
```

### Scope / Applicability

```text
scenario
capability
jurisdiction
environment
audience / target
```

### Condition / Variant

例如：

```text
flag required
partial implementation
prefix required
specific configuration
adoption level
```

### Method / Basis

例如：

```text
measurement method
test method
classification basis
```

## Boundary

Qualifier 修改的是 **Statement 的含义**。

以下不属于 Qualifier：

- `retrieved_at` → Evidence metadata；
- reviewer identity → provenance / review；
- maturity score → Assessment value。

当前 Relation 中的 `capability_context` / `scenario_context` 是这一模型的早期兼容形式。

---

# 9. D6 — Evidence / Provenance

## Decision

至少区分两层来源。

## 9.1 Object Identity Source

用于证明：

```text
这个 identity target 确实存在
官方名称是什么
官方入口在哪里
谁创建 / 发布 / 维护
```

当前 Object `sources` 可继续作为简单实现。

## 9.2 Statement Evidence

用于证明一条具体 Claim：

```text
谁说的
来源在哪里
支持的是哪条 Statement
何时获取
针对哪个版本 / 范围
必要时引用哪个具体片段
```

Statement Evidence **MUST NOT** 因为“同属一个 Object”就自动推广为该对象全部 Claim 的证据。

## 9.3 Attribution roles

模型必须允许区分至少：

```text
creator
author
maintainer
publisher
issuer
governing body
contributor
assertor
assessor
```

稳定且可复用的责任主体 SHOULD 通过 `agent` identity 引用，而不是长期塞在一个模糊 `organization` 字段中。

这些语义应尽量映射 PROV-O / DCMI。

---

# 10. D7 — Fact vs Assessment

## Decision

## 10.1 Factual Claim

描述某来源对现实状态的可追溯陈述，例如：

```text
发布日期
官方版本
maintainer
license
documented deployment
documented support
release history
specification access status
```

“Fact”在 Atlas 中仍然是一条可追溯 Claim，不代表它脱离来源变成绝对真理。

## 10.2 Assessment

具有评价性的 Statement，例如：

```text
mature
recommended
suitable
authoritative
insufficient
vendor-neutral
high confidence
best practice
```

Assessment 最少需要：

```text
subject
assessment kind / value
assessor
basis / criteria
evidence
as_of / context（动态评价时）
```

## 10.3 Current-schema implication

当前 Standard Schema 中：

```text
maturity
vendor_neutrality
```

已经表现出 Fact / Assessment 混合风险。

后续迁移不应机械删除这些字段，而应逐字段判断：

- 是否是来源明确的 factual status；
- 是否是 IA Assessment；
- 是否需要 as_of / criteria / Evidence。

当前 Relation `confidence` 也需要同样审计：

> 它是谁的 confidence？基于什么？是在评价 Statement 还是描述来源？

---

# 11. D8 — Missing / Unknown / Explicit None

## Decision

InteropAtlas 在语义层 **MUST** 区分至少四种状态：

### Known value

已有具体值，包括合法 boolean `false`。

### Unknown value

明确知道这个属性 / 问题有意义，但具体值未知。

### Explicit none

明确知道不存在该值或该关系。

### Not recorded / missing

Atlas 当前没有记录。

## Normative invariant

> 字段缺失 **MUST NOT** 自动解释为 unknown、none 或 false。

v0 不冻结 YAML sentinel 语法。后续 Schema 可采用 `value_state` 或其他方式，但不能让一个通用 `null` 同时表达所有状态。

MDN BCD 已经证明这种区分是实际工程需求，而非理论附加项。

---

# 12. D9 — Concept Family / Versioned Artifact / System / Distribution / Part

## Decision

现实对象只有在拥有独立 identity / lifecycle 时才拆分；但不能为了 Schema 方便，把现实中已独立的对象压成一个 umbrella free-text object。

## 12.1 Split rule

以下任一条件成立时，SHOULD 考虑独立对象：

- 有独立官方 ID / URL；
- 有自己的版本 / 发布时间；
- 有不同 license / status / authority；
- 有独立 Evidence；
- 会被独立查询 / 引用；
- 有自己的 lifecycle / maintainer；
- 与 umbrella identity 的关系本身有显著语义价值。

## 12.2 Common relations to profile later

候选：

```text
version_of / has_version
part_of / has_part
distribution_of
maintained_by
published_by
introduced_by
canonical_source
implements
realizes
```

精确 Relation vocabulary 后续单独 Profile；本 Decision 只确定边界。

## Example A — NIST AI RMF

```text
AI RMF
  type: concept
  kind: framework

AI RMF 1.0
  type: artifact
  kind: publication
  authority: official_guidance

AI RMF 1.0 --version_of / realizes--> AI RMF
```

“截至 2026 正在修订”是关于 living Concept 当前生命周期的一条时效 Statement，不改变 AI RMF 1.0 的历史 identity。

## Example B — MDN BCD

```text
BCD maintained project
  type: system
  kind: data_project

BCD dataset
  type: artifact
  kind: dataset

@mdn/browser-compat-data package/distribution
  type: artifact
  kind: distribution
```

不要求每个 npm release 都成为对象；是否拆分取决于独立查询 / Evidence 需求。

## Example C — Munzner Nested Model

```text
Nested Model
  type: concept
  kind: conceptual_model

2009 paper
  type: artifact
  kind: publication

Nested Model --introduced_by / canonical_source--> 2009 paper
```

Concept ≠ Publication。

## Example D — USWDS

```text
USWDS
  type: system
  kind: design_system
```

Principles、Guidance、Components、Code、Releases、Accessibility Test Results 只有在现实中需要独立 identity / lifecycle / evidence 时才拆。

采用关系可带 qualifier：

```text
Site A --adopts--> USWDS
adoption_level = principles | guidance | code
```

所以“采用 USWDS”不能永远只是无上下文 boolean。

## Example E — AGENTS.md

先应用 Identity Target Rule：

- 如果 ID 指 canonical open format / published specification → `artifact`；
- 如果另有需求表示抽象 repository instruction convention → `concept`；
- 只有当两者都具有独立查询价值时才拆对象。

---

# 13. D10 — Model / Validation / Serialization / Query Boundary

## Decision

以下成为 v0 核心不变量。

## Semantic Model ≠ Validation Contract

知识表示规范定义“什么意思”；JSON Schema / future SHACL 定义“机器怎样检查”。

Schema **MUST NOT** 因实现方便反向决定 reality identity。

## Semantic Identity ≠ Serialization

YAML 是当前 authoring format，不是 ontology。

字段顺序、嵌套方式、目录位置 **MUST NOT** 承担 identity。

## Semantic Identity ≠ Physical Path

继续遵守：

> **Physical Storage ≠ Semantic Classification ≠ Index / View**

## Canonical Authoring ≠ Query Projection

模型 SHOULD 保持未来可投影到：

```text
current Python Engine
RDF / SPARQL
Property Graph / GQL
relational views / SQL
JSON-LD
```

v0 不要求立即实现这些投影。

## graph-native, database-agnostic

正式解释为：

> **关系、引用和 Statement 是第一等语义；底层存储与查询产品可以替换。**

这不意味着拒绝 Schema / vocabulary，而意味着不把具体数据库实现提升为语义真相。

---

# 14. Proposed Normative Invariants

如果本 Decision 获批准，下列规则 SHOULD 被提升为正式 Knowledge Representation Requirements。

1. Stable ID **MUST NOT** 依赖显示名称、翻译、目录或文件路径。
2. 选择 `type` 前 **MUST** 明确 stable ID 的 Identity Target。
3. Core Identity Family **MUST** 限制在少量稳定上位类别；不得因新领域名词随意增加。
4. Reality identity **MUST NOT** 由 Atlas reference / precedent role 决定。
5. `type` **MUST NOT** 表达 maturity、recommendation、authority 或 Assessment。
6. `kind` **MUST NOT** 成为无定义自由标签池。
7. Strong Profile **MUST NOT** 被实现为语义物理目录。
8. 同一现实 identity **MUST NOT** 仅为 taxonomy 方便而复制。
9. 独立现实 Artifact / System / Agent **SHOULD NOT** 为 Schema 方便被压成 umbrella free text。
10. Object Source 与 Statement Evidence **MUST** 可区分。
11. Statement-specific Evidence **MUST NOT** 自动推广为整个 Object 的证据。
12. Fact 与 Assessment **MUST** 可区分。
13. 字段缺失 **MUST NOT** 自动解释为 false / none / unknown。
14. 动态、版本化、条件化 Claim **SHOULD** 具有 Statement / Context 升级路径。
15. Relation **SHOULD** 与通用 Statement 模型语义兼容，而不是形成两个互斥关系系统。
16. Validation **MUST** 服务语义合同，而不是反向定义语义。
17. Query / Renderer / current Engine **MUST NOT** 反向扭曲 Canonical semantics。
18. Breaking semantic change **MUST** 有 migration rationale，并优先保持 stable ID。
19. External vocabulary mapping **SHOULD** 通过明确 mapping / external ID 表达，不依赖名称字符串猜测。
20. v0 **MUST NOT** 预先增加没有现实需求支撑的顶层 family。

---

# 15. What v0 Implements Now vs Reserves for Later

## 15.1 获批后立即进入下一阶段设计

1. 4 个 Core Identity Families；
2. `type / kind / profile / roles / authority` 职责分离；
3. Identity Target Rule；
4. Capability / Scenario Strong Concept Profiles；
5. Object / Statement 语义边界；
6. Object Source / Statement Evidence 边界；
7. Fact / Assessment 边界；
8. missing / unknown / explicit none 语义；
9. Relation 作为 Statement 特例的统一方向；
10. Concept / versioned Artifact / System / Distribution / Part 拆分规则；
11. Agent / System identity split rule；
12. legacy → v0 compatibility migration strategy。

## 15.2 未来预留，但 v0 不全面实现

1. explicit Statement IDs；
2. statement-level temporal validity；
3. 多来源冲突 Claims；
4. richer qualifier vocabulary；
5. full PROV graph；
6. external SKOS / Wikidata / Schema.org mappings；
7. RDF / JSON-LD export；
8. GQL / SQL projection；
9. richer inference / entailment；
10. graph canonicalization / signing；
11. Activity / Event core family（只有真实需求出现后再决策）。

## 15.3 当前明确不要做

1. 不发明 IA Query Language；
2. 不实现完整 OWL ontology；
3. 不把全部字段改造成 Wikibase-style Statements；
4. 不强制 RDF 作为 Canonical storage；
5. 不选定 Neo4j / PostgreSQL / triple store；
6. 不为了未来百万对象规模提前做 distributed storage；
7. 不建立几十个顶层 object types；
8. 不创建新的语义物理目录；
9. 不为了“模型完美”继续无边界 Fit Test。

---

# 16. Impact on Current Canonical Model

## `standard`

长期逻辑映射：

```text
legacy type: standard
→ type: artifact
→ kind: standard / specification / protocol / profile / ...
→ authority / normative status 单独表达
```

Stable ID 保持。

当前 `maturity`、`vendor_neutrality` 等字段要逐项审计 Fact / Assessment 边界。

## `reference_project`

这是最大迁移区，**禁止批量一刀切**。

逐对象应用 Identity Target Rule，可能映射：

```text
concept
artifact
system
```

Apple HIG、AGENTS.md 等已经证明 current `reference_project: other` 是临时容器，不是长期 identity model。

## `implementation`

大部分自然映射：

```text
type: system
kind: software / library / service / hardware / ...
```

独立 release / package / distribution 可在需要时拆成 Artifact。

## `organization`

长期映射：

```text
type: agent
kind: organization
```

但当前 `organization_kind: open_source_project` 必须逐对象判断：它究竟是治理主体（Agent）还是工程项目（System）。

## `capability`

语义上：

```text
type: concept
kind: capability
Capability Profile
```

现有 category / layers / parent_capabilities / constraints 等专业结构保留。

## `scenario`

语义上：

```text
type: concept
kind: scenario
Scenario Profile
```

现有 actors / requires / environment / success criteria 保留。

## `relation`

不删除。

长期明确为 relationship Statement，并逐步补：

```text
qualifier/context
evidence/provenance
assertor
assessment/confidence semantics
```

当前 `capability_context` / `scenario_context` 可兼容迁移。

## `open_gap`

当前对象同时混有：

```text
Gap Finding
priority Assessment
workflow status
impact / insufficiency judgment
closure criteria
```

本 Decision 不强行把它塞入 4 family。

后续 Trust / Curation Profile 需要决定：

- Gap Case 是否具有独立 identity；
- priority / insufficiency 是否变为 Assessment；
- tracking status 是否属于 workflow metadata。

## `map`

继续作为 View / Projection，不属于 4 个 Core Identity Families。

---

# 17. Impact on Schema / Engine / Curation / Human Interface

## Schema

获批后的下一阶段才设计：

- 4-family discriminator；
- kind vocabulary；
- Strong Profiles；
- authority / roles；
- Statement / Evidence 可升级结构；
- Relation Schema objectRef 不再永久硬编码 legacy type 枚举；
- missing semantics；
- legacy compatibility layer。

本 Decision PR 不执行任何 Schema 修改。

## Engine

Engine 继续基于 stable ID / semantic fields 工作，不依赖物理目录。

迁移阶段 SHOULD dual-read legacy type 与 v0 family/kind mapping，保证：

```text
Graph
Backlinks
Representative Queries
Stable public URLs
```

不中断。

## Curation

新对象收录逻辑应演进为：

```text
Identify candidate
↓
Define Identity Target
↓
Choose Core Family
↓
Choose kind / Strong Profile
↓
Record identity sources
↓
Add roles / relations
↓
Promote contextual claims to Statements where needed
↓
Attach Evidence
↓
Add Assessment separately
```

## Human Interface

页面未来至少要在信息层区分：

```text
Identity
Kind / Profile
Roles
Facts / Statements
Context
Evidence
Assessment
```

不能把 YAML 字段平铺直接当最终信息架构。

## Query

未来查询针对稳定语义：

```text
family
kind/profile
role
relation/statement
context
assessment
```

而不是 legacy 文件路径或某版 Schema 的偶然布局。

---

# 18. Migration Strategy Proposal

如果本 Decision 获批准，实施 SHOULD 分阶段。

## Phase 0 — Decision approval

只确认语义合同。

## Phase 1 — Schema / Compatibility Design

- 设计 v0 machine contracts；
- 定义 legacy → v0 mapping；
- 设计 Engine dual-read；
- 不迁移全部数据。

## Phase 2 — Representative Migration Pilot

选择：

- 10 个已研究 Fit Test 对象；
- 少量现有 Standard；
- 少量 Implementation；
- Organization；
- Capability / Scenario；
- Relations；
- Apple HIG / AGENTS.md 这类 boundary objects。

验证：

```text
stable IDs
identity targets
graph edges
representative queries
Renderer
human readability
evidence semantics
legacy compatibility
```

## Phase 3 — Canonical Data Migration

分批迁移 legacy objects，每批保持回归基线。

## Phase 4 — Enforcement

Schema / Validator / CI 才开始正式拒绝旧写法。

## Phase 5 — Projection

按真实需求增加 JSON-LD / RDF / Property Graph / SQL projection，而不是为了技术完整性提前实现。

---

# 19. Explicit Open Questions

以下问题仍开放，但目前都不要求增加大规模 Prior Art / Batch 3：

1. `kind` vocabulary 是全局表还是按 family 分组管理；
2. Strong Profile 的机器字段是否显式叫 `profile`；
3. authority / normative status 最小 vocabulary；
4. explicit Statement 的最终 YAML 语法和物理存储方式；
5. Relation 与通用 Statement 是同一 Schema 的 Profile，还是共享基础合同的两个 Schema；
6. explicit `value_state` 的机器编码；
7. version Artifact 的创建阈值是否需要按 family 增加更具体规则；
8. external identifiers / SKOS mappings 第一阶段覆盖哪些系统；
9. Assessment vocabulary 与 confidence model 由 #10 Trust Route 如何细化；
10. Activity / Event 在什么现实阈值下升级为第五个 Core Family。

如果其中某个问题被证明会推翻 D1–D10，才允许新增最多 1–2 个定向样本。

---

# 20. Decision Outcome Proposed

本 Revised Draft 提议接受：

> **InteropAtlas v0 不建立万能分类树，而建立一个最小、可演化、可投影的知识表示合同。**

核心结构为：

```text
4 Core Identity Families
concept / artifact / system / agent

+ Identity Target Rule
+ kind / Strong Profile / roles / authority 分层
+ Object / Statement 分离
+ Context / Qualifier
+ Evidence / Provenance
+ Fact / Assessment 分离
+ Missing semantics
+ Concept / Artifact / System / Agent identity split rules
+ Validation / Serialization / Query 解耦
```

这套模型故意比现实 taxonomy 小得多。

它不是为了“现在就把每件事建模得最复杂”，而是为了确保 InteropAtlas 从当前百级对象扩展到千级、万级时，不会因为早期把 reality identity、来源、评价、版本和数据库实现混在一起而被迫推翻全部 Canonical Data。

## Approval boundary

**本文件当前仍是 Draft。**

在 Maintainer 明确批准前：

- 不更新正式 Knowledge Object Specification；
- 不修改 JSON Schema；
- 不迁移现有 Canonical Data；
- 不关闭 #15；
- 不把本模型描述为已采用规范；
- 不把 PR #59 转为可合并状态。
