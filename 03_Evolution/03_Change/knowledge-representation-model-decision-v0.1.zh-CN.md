# InteropAtlas Minimum Knowledge Representation Contract v0.1 — Model Decision Draft

> 状态：**Draft / High-impact Decision — NOT ADOPTED**
>
> Work Item：#58
>
> Parent：#15
>
> 目的：基于既有标准、成熟数据语言技术栈和 10 个真实对象 Fit Test，收敛 InteropAtlas v0 的最小知识表示合同。
>
> 本文件是决策草案，不修改 Schema、不迁移数据、不改变物理目录；只有 Maintainer 明确批准后，才能进入规范与实现阶段。

## 1. Decision Context

InteropAtlas 已经确认一个关键事实：当前问题不是“再补几个对象类型”，而是要定义一套足够小、可演化、可投影的知识语言语义骨架。

前置研究包括：

- ISO 704：object / concept / definition / designation 分离；
- W3C SKOS、ISO 25964：Concept Scheme、关系与 vocabulary mapping；
- Wikibase / Wikidata：Entity / Statement / Qualifier / Reference / Rank；
- W3C PROV-O、DCMI：Agent、Role、Attribution、creator / contributor / publisher 分离；
- W3C DCAT：Dataset / Distribution / DataService / Catalog 等资源身份分离；
- CIDOC CRM / ISO 21127：异构知识的高层语义整合；
- SHACL / JSON Schema：语义模型与机器验证合同分离；
- SQL、RDF、Wikibase、Property Graph / GQL：数据模型、约束、查询、投影的完整技术栈比较；
- 10 个真实对象 Fit Test：Diátaxis、Card Sorting、Nielsen 10 Heuristics、GOV.UK Design System、Docs as Code、MDN Browser Compat Data、GitHub Community Health、NIST AI RMF 1.0、Munzner Nested Model、USWDS。

研究已经足够进入 Model Decision；除非本草案暴露一个会改变模型结构的明确二选一问题，不再开启无边界 Batch 3。

---

# 2. Decision Summary

本 Draft 提议 InteropAtlas v0 采用以下逻辑骨架：

```text
Identity
↓
Reality Family / Kind
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

> **语义模型决定知识怎样被准确表达；Schema、YAML、数据库和查询语言只是它的实现或投影。**

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
convention
...
```

**Reject.**

原因：

- 10 个样本已经证明同一对象经常同时具有多个现实角色；
- taxonomy 会快速膨胀；
- type 变更会制造持续 Schema / Query / migration 成本；
- 很多差异应由 `kind`、role、relation、authority 或 lifecycle 表达，而不是顶层 family。

## B. 一个万能 `reference` / `practice` / `reference_project`

**Reject.**

原因：

- Card Sorting、MDN BCD、USWDS、AI RMF 1.0 的生命周期和来源结构完全不同；
- `reference` 描述的是 Atlas 使用角色，不是 reality identity；
- 当前 `reference_project` 已经证明会把 Method、Design System、Dataset、Convention 强行 Project 化。

## C. 直接复制完整 Wikibase

**Reject for v0.**

Statement / Qualifier / Reference 分层值得吸收，但当前 Atlas 体量不需要把所有简单字段都改造成第一等 Statement。

## D. 强制 RDF / OWL 作为 Canonical Storage

**Reject for v0.**

RDF 是重要投影目标和语义参考，但当前 Human / Agent authoring 的轻量 YAML 路线仍然有效。Canonical serialization 不应反向决定 ontology。

## E. 直接采用纯 Property Graph / 某个图数据库 Schema

**Reject.**

GQL / Property Graph 是重要查询和工程投影，但不能让具体数据库能力决定 IA 的现实语义。

## F. Query-language-first

**Reject.**

当前不发明 IA Query Language。查询语言必须建立在稳定语义合同之上，而不是反过来约束语义。

---

# 4. D1 — Stable Reality Identity Families

## Decision

v0 提议采用 **6 个稳定 Reality Identity Families**。它们是逻辑 family；最终 YAML 字段名和 Schema 名称在后续 Implementation Decision 中确定。

### 4.1 Artifact

**定义：** 可以被独立引用、发布、版本化、分发或保存的信息 / 数据产物。

候选 `kind`：

```text
standard
specification
protocol
profile
publication
dataset
distribution
schema
catalog
report
release
reference_architecture
...
```

重要：

- `Artifact` 不等于“正式标准”；
- Normative / official / community / private authority 是单独维度；
- NIST AI RMF 1.0、某篇论文、某个 Dataset、某一版 Specification 都可属于 Artifact family。

### 4.2 Practice

**定义：** 以概念、方法、原则、框架或实践形式存在，可被学习、采用或应用，但不依赖某个单一运行实例才能成立的知识对象。

候选 `kind`：

```text
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
...
```

典型：

- Card Sorting；
- Docs as Code；
- Diátaxis；
- Nielsen Heuristics；
- Munzner Nested Model；
- AI RMF 作为持续演化的 framework family（其具体 1.0 publication 另作为 Artifact）。

### 4.3 System

**定义：** 具有持续维护、运行、组织或产品生命周期的具体系统 / 资源集合；可包含组件、代码、数据、规则或服务。

候选 `kind`：

```text
software
service
platform
hardware
design_system
data_project
knowledge_base
registry
catalog_system
governance_mechanism
platform_mechanism
...
```

典型：

- USWDS；
- GOV.UK Design System；
- GitHub Community Health platform mechanism；
- MDN BCD maintained project；
- 当前大量 Implementation。

### 4.4 Agent

**定义：** 对创建、发布、维护、治理、贡献、决策或执行承担角色的行动主体。

候选 `kind`：

```text
person
organization
project_team
software_agent
...
```

v0 主要解决当前 `organization` 过窄，无法自然表达 creator / author / person 等 attribution 问题。

### 4.5 Capability

**定义：** 系统、Artifact、Practice 或 Agent 可以提供、要求、支持或实现的抽象能力。

当前 `capability` 概念继续成立。

### 4.6 Scenario

**定义：** 描述需求、参与者、上下文、约束和目标组合的使用 / 互操作情境。

当前 `scenario` 概念继续成立；未来 Need / Constraint 可通过 kind / relation / statement 进一步表达。

## Supporting layers that are NOT Reality Families

以下内容不作为上述 6 个 reality family 的平级分类：

- Relation / Statement：关于对象或对象之间的陈述；
- Evidence / Source：支持某个 identity 或 statement 的来源；
- Assessment / Gap：评价 / 发现，不等于对象现实身份；
- Map / View / Index：投影，不属于 Canonical reality identity；
- “Reference / Precedent”：通常是 Atlas role 或 Assessment，不是 reality family。

---

# 5. D2 — `type` vs `kind` vs `roles`

## Decision

### `type`

`type` **SHOULD** 最终承担稳定 Reality Family 的机器身份。

要求：

- 数量少；
- 变化慢；
- 不因某个新领域名词就扩张；
- 不表达成熟度、推荐度、权威性或 Atlas 使用角色。

### `kind`

`kind` 用于表达 family 内更具体的 reality identity。

例如：

```text
type: practice
kind: heuristic_set
```

或：

```text
type: artifact
kind: dataset
```

`kind` 可以比 `type` 更可扩展，但仍需要受控 vocabulary 与定义。

### `roles`

`roles` 表达对象在某个上下文中的非排他性作用。

例如：

```text
human_interface_reference
compatibility_evidence_source
reference_implementation
interoperability_precedent
```

Role **MUST NOT** 替代现实身份。

例如：

```text
mature_precedent
```

不应成为 `type`；“mature”是 Assessment，“precedent/reference”通常是 Atlas role。

## Authority is separate

Formal Standard、Official Guidance、Community Specification、Private Documentation 等权威 / 规范状态 **MUST NOT** 通过 Reality Family 猜测。

一个 `artifact` 可以是：

```text
formal_standard
official_guidance
community_specification
research_publication
vendor_documentation
...
```

具体 authority vocabulary 在后续 Profile 中确定。

---

# 6. D3 — Object Property vs Statement / Claim

## Decision

InteropAtlas 必须在概念上区分：

```text
Object Property
≠
Statement / Claim
```

### 允许保持为简单 Object Property 的信息

满足以下大部分条件时，可保留 compact property：

1. 主要用于 identity / discoverability；
2. 对对象本身相对稳定；
3. 通常只有一个 Canonical value；
4. 不需要独立时间 / 版本 / scope 才有意义；
5. 不预期存在多个互相冲突的来源值；
6. 不需要独立 Evidence lifecycle。

典型：

```text
stable id
primary name
official name
kind
canonical official URL
stable external identifier
```

某些 immutable version facts，例如“这个具体 Artifact 的版本号 / 发布日”，也 MAY 作为 property 保存，只要该 Artifact 已经是独立 versioned identity。

### 必须概念升级为 Statement 的信息

出现任一高影响条件时，**SHOULD** 视为 Statement：

- 会随时间 / 版本变化；
- 依赖 scope / scenario / capability / jurisdiction / environment；
- 需要 condition / method 才准确；
- 多个来源可能给不同值；
- 需要 statement-specific Evidence；
- 需要明确谁在声称；
- 是兼容、支持、采用、推荐、成熟、适用等可争议命题；
- 关系本身需要 qualifier。

典型：

```text
Browser X 从 Version Y 开始支持 Feature Z
Project A 采用 USWDS 的 Code 层
AI RMF 当前处于修订状态
Object X 是成熟先例
Implementation A 与 Standard B 兼容
```

---

# 7. D4 — Statement v0 Boundary

## Decision

v0 **正式定义 Statement 的逻辑合同，但不把所有字段立即物理化成 Statement records。**

这是为了同时满足正确性和当前体量控制。

### Logical Statement

一条 Statement 至少具有以下概念组成：

```text
subject
predicate
value / object
value_state
qualifiers / context
provenance / evidence
assertor / assessor（适用时）
```

其中 Relation 是 Statement 的一个重要特例：

```text
source  = subject
relation = predicate
target  = object value
```

### v0 physical strategy

1. 简单稳定信息继续允许使用 compact Object properties；
2. 当前显式 Relation record 继续作为第一类 relationship statement；
3. Relation Schema 后续应能够增加 statement-level evidence / qualifier，而不是另建一套互不兼容关系系统；
4. 高风险、动态、多来源、可冲突的非关系事实，未来可以升级为 explicit Statement；
5. **不要求 v0 把所有现有 YAML 字段一次性转换成 Statement 文件。**

### Promotion rule

Compact property → Explicit Statement 必须保持语义可升级：

> 同一对象 ID 不变；只是原先 compact assertion 获得独立 context / evidence / statement identity。

---

# 8. D5 — Context / Qualifier

## Decision

v0 不复制 Wikibase 全部 qualifier 机制，但正式保留以下通用语义维度：

### Temporal

```text
as_of
valid_from
valid_to
```

### Version

```text
version_context
edition / release context
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
requires flag
partial implementation
prefix required
specific configuration
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

以下不是 Qualifier：

- `retrieved_at`：属于 Evidence metadata；
- reviewer identity：属于 provenance / review；
- maturity score：属于 Assessment value。

当前 Relation 中已有的 `capability_context` / `scenario_context` 可视为这一模型的早期特例。

---

# 9. D6 — Evidence / Provenance

## Decision

至少区分两层来源：

### 9.1 Object Identity Source

用于证明：

```text
这个对象确实存在
官方名称是什么
官方入口在哪里
谁发布 / 维护
```

当前 Object `sources` 可以继续承担这一层的简单实现。

### 9.2 Statement Evidence

用于证明某一条具体命题：

```text
谁说的
来源在哪里
何时获取
支持的是哪一条 Statement
必要时引用哪一段 / 哪个版本
```

Statement Evidence **MUST NOT** 因为“同属一个对象”就自动推广为对象全部 Claim 的证据。

## Attribution roles

模型至少必须可区分：

```text
creator
author
maintainer
publisher
issuer
governing body
contributor
```

这些角色可映射 PROV-O / DCMI；具体 Relation vocabulary 在实施阶段确定。

稳定且可复用的责任主体 SHOULD 作为 `agent` identity 引用，而不是永久塞进一个 `organization` 字符串。

---

# 10. D7 — Fact vs Assessment

## Decision

### Fact / Factual Claim

描述来源声称的现实状态，例如：

- 发布日期；
- 官方版本；
- documented support；
- documented deployment；
- maintainer；
- license；
- release history。

“Fact”在 Atlas 中仍然是可追溯 Claim，不意味着它脱离来源成为哲学上的绝对真理。

### Assessment

带评价性质的 Statement，例如：

```text
mature
recommended
suitable
authoritative
insufficient
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

## Consequence

- `mature: true` 不应成为无证据 identity property；
- `Mature Precedent` 更适合作为“reference role + evidence-backed maturity assessment”的组合；
- 当前 Relation `confidence` 长期应被审计：它是某来源的 confidence、IA 的 Assessment，还是算法输出，不能保持语义模糊。

---

# 11. D8 — Missing / Unknown / Explicit None

## Decision

InteropAtlas v0 在语义层必须区分至少四种状态：

### 1. Known value

已有具体值，包括合法的 boolean `false`。

### 2. Unknown value

明确知道这个问题 / 属性有意义，但当前具体值未知。

### 3. Explicit none

明确知道不存在该值或该关系。

### 4. Not recorded / missing

Atlas 当前没有记录；**不能推出 unknown、none 或 false。**

## Normative invariant

> 字段缺失 **MUST NOT** 自动解释为否定事实。

v0 本 Decision 不冻结 YAML sentinel 语法。后续 Schema 可以采用 `value_state` 或其他明确表示，但不能继续依赖一个通用 `null` 同时表达所有语义。

---

# 12. D9 — Family / Versioned Artifact / Implementation / Distribution

## Decision

现实对象只有在确实拥有独立 identity / lifecycle 时才拆分；但不能为了简化 Schema 把现实中已独立的 Artifact 压成同一个对象。

## Split rule

以下任一条件成立时，SHOULD 考虑独立对象：

- 有独立稳定官方 ID / URL；
- 有自己的版本 / 发布时间；
- 有不同 license / status / authority；
- 有独立 Evidence；
- 会被独立查询 / 引用；
- 有自己的 lifecycle / maintainer；
- 与 umbrella object 的关系本身有语义价值。

## Common relations to profile later

```text
version_of / has_version
part_of / has_part
distribution_of
maintained_by
published_by
introduced_by
canonical_source
implements
```

精确 Relation vocabulary 后续单独 Profile；本 Decision 先确定语义边界。

## Example A — NIST AI RMF

```text
AI RMF
  type: practice
  kind: framework

AI RMF 1.0
  type: artifact
  kind: publication / framework_artifact
  authority: official_guidance

AI RMF 1.0 --version_of--> AI RMF
```

“2026 正在修订”是关于 family 当前生命周期的 Statement，不改写 AI RMF 1.0 的历史 identity。

## Example B — MDN Browser Compat Data

```text
BCD maintained project
  type: system
  kind: data_project

BCD dataset
  type: artifact
  kind: dataset

@mdn/browser-compat-data package / release
  type: artifact
  kind: distribution
```

是否每个 package release 都成为独立对象取决于查询 / Evidence 需要；但 Project、Dataset、Distribution 三种 identity 不应被语义上视为同义。

## Example C — Munzner Nested Model

```text
Nested Model
  type: practice
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

Principles、Guidance、Components、Code、Release、Accessibility Test Result 只有在现实中需要独立 identity / lifecycle / evidence 时才拆对象。

一个采用 Statement 可以具有 qualifier：

```text
Site A --adopts--> USWDS
qualifier: adoption_level = principles | guidance | code
```

因此“采用 USWDS”不是永远只能是一个无上下文 boolean。

---

# 13. D10 — Model / Validation / Serialization / Query Boundary

## Decision

以下边界成为 v0 核心不变量。

### Semantic Model ≠ Validation Contract

知识表示规范决定“什么意思”；JSON Schema / future SHACL 决定“机器怎样检查”。

Schema **MUST NOT** 因为当前实现方便就反向决定现实对象身份。

### Semantic Identity ≠ Serialization

YAML 是当前 authoring format，不是 ontology。

字段顺序、文件嵌套、物理目录 **MUST NOT** 承担对象本体身份。

### Semantic Identity ≠ Physical Path

继续遵守：

> **Physical Storage ≠ Semantic Classification ≠ Index / View**

### Canonical Authoring ≠ Query Projection

InteropAtlas SHOULD 保持未来可投影到：

```text
current Python Engine
RDF / SPARQL
Property Graph / GQL
relational views / SQL
JSON-LD
```

但 v0 不要求立即实现全部投影。

### graph-native, database-agnostic

该原则正式解释为：

> 关系和引用是第一等语义；底层存储和查询产品可以替换。

而不是“拒绝设计稳定 Schema / vocabulary”。

---

# 14. Normative Invariants Proposed for v0

如果本 Decision 获批准，下列规则 SHOULD 被提升为正式规范 Requirement：

1. Stable ID **MUST NOT** 依赖显示名称、翻译、目录或文件路径。
2. Reality identity **MUST NOT** 由 Atlas reference role 决定。
3. `type` **MUST NOT** 用于成熟度、推荐度、权威性或其他 Assessment。
4. `kind` **MUST NOT** 被用作无定义自由标签池。
5. 同一现实对象 **MUST NOT** 仅为 taxonomy 方便而复制。
6. 独立现实 Artifact **SHOULD NOT** 为 Schema 方便被压成 umbrella free text。
7. Statement-specific Evidence **MUST NOT** 自动推广为整个 Object 的证据。
8. Fact 与 Assessment **MUST** 可区分。
9. 字段缺失 **MUST NOT** 自动解释为 false / none。
10. 动态、版本化、条件化 Claim **SHOULD** 具有 Statement / Context 升级路径。
11. Validation implementation **MUST** 服务语义合同，而不是反向定义语义。
12. Query / Renderer / current Engine implementation **MUST NOT** 反向扭曲 Canonical semantics。
13. Breaking semantic change **MUST** 有 migration rationale，并优先保持 stable ID。
14. External vocabulary mapping **SHOULD** 通过明确 mapping / external ID 表达，不依赖名称字符串猜测。

---

# 15. What v0 Implements Now vs Reserves for Later

## v0 应立即进入下一阶段设计

1. 6 个 stable Reality Families；
2. `type / kind / roles / authority` 职责分离；
3. Object / Statement 语义边界；
4. Object Source / Statement Evidence 边界；
5. Fact / Assessment 边界；
6. missing / unknown / explicit none 语义；
7. Relation 作为 Statement 特例的统一方向；
8. family / versioned artifact / part / distribution 的拆分规则；
9. Relation vocabulary review 机制；
10. legacy model → v0 model 的兼容迁移策略。

## 未来预留，但 v0 不全面物理实现

1. explicit Statement IDs；
2. statement-level temporal validity；
3. 多来源冲突 Claim；
4. richer qualifier vocabulary；
5. full PROV graph；
6. external SKOS / Wikidata / Schema.org mapping profile；
7. RDF / JSON-LD export；
8. GQL / SQL projection；
9. richer inference / entailment；
10. graph canonicalization / signing。

## 当前明确不要做

1. 不发明 IA Query Language；
2. 不实现完整 OWL ontology；
3. 不把全部字段改造成 Wikibase-style Statement；
4. 不强制 RDF 作为 Canonical storage；
5. 不选定 Neo4j / PostgreSQL / triple store；
6. 不为了未来百万对象规模提前做 distributed storage；
7. 不建立几十个顶层 object type；
8. 不创建新的语义物理目录。

---

# 16. Impact on Current Repository

## Current `standard`

长期语义目标：

```text
legacy type: standard
→ type: artifact
→ kind: standard / specification / protocol / profile / ...
→ authority: formal_standard / formal_specification / ...
```

Stable ID 保持。

## Current `reference_project`

这是最大迁移区。

应按现实身份逐个映射到：

```text
artifact
practice
system
```

而不是批量把所有记录换成另一个万能 type。

## Current `implementation`

长期映射到：

```text
type: system
kind: software / service / platform / hardware / implementation / ...
```

Stable ID 保持；现有 implementation query 可通过兼容映射过渡。

## Current `organization`

长期映射到：

```text
type: agent
kind: organization
```

并为 person / project_team / software_agent 留出空间。

## Current `capability` / `scenario`

概念基本保留，主要补 Relation / Statement / Evidence contract。

## Current `relation`

不删除。

长期把它明确成 relationship Statement，并增加：

- qualifier / context；
- evidence / provenance；
- value-state / assertion metadata（如需要）；
- relation vocabulary governance。

当前 `capability_context` / `scenario_context` 可兼容迁移。

## Current `open_gap`

长期应审计为：

- Gap Case / Finding；
- Assessment / Claim；
- 或独立 Artifact（如果它本身是正式报告）。

不在本 Decision 强制迁移。

## Current `map`

继续作为 View / Projection，不作为 Reality Family。

---

# 17. Impact on Schema / Engine / Curation / Human Interface

## Schema

下一阶段应设计，但本 PR 不执行：

- 新 family schemas 或统一 family discriminator；
- legacy type compatibility；
- authority / roles / kind vocabulary；
- Statement / evidence 可升级结构；
- Relation Schema 不再硬编码无法扩展的全部 object type；
- 明确 missing semantics。

## Engine

Engine 必须继续通过 stable ID / semantic fields 处理对象，而不是依赖物理目录。

迁移阶段应 dual-read legacy / v0 type mapping，保证 Graph baseline 不因 Schema 重构瞬间失效。

## Curation

新对象收录顺序应改为：

```text
Identify reality object
↓
Choose family / kind
↓
Record identity sources
↓
Add roles / relations
↓
Promote contextual facts to Statements where needed
↓
Attach Evidence
↓
Add Assessment separately
```

## Human Interface

页面未来至少应视觉 / 信息上区分：

```text
Identity
Role
Facts
Statements / Context
Evidence
Assessment
```

不能继续把 YAML 字段平铺当作信息架构。

## Query

未来查询应针对稳定语义：

```text
family / kind / role / relation / statement / assessment
```

而不是 `reference_project` 目录、物理路径或某一版 Schema 的偶然字段布局。

---

# 18. Migration Strategy Proposal

本 Decision 若获批准，后续实施 SHOULD 分阶段，不做 big-bang migration。

### Phase 0 — Decision approval

只确认语义合同。

### Phase 1 — Schema / Compatibility Design

- 定义 v0 machine schema；
- 定义 legacy → v0 mapping；
- Engine 支持 dual-read；
- 不迁移全量数据。

### Phase 2 — Representative Migration Pilot

选 10 个已研究样本 + 少量现有 Standard / Implementation / Relation 做 migration pilot。

验证：

- stable IDs；
- graph edges；
- representative queries；
- Renderer；
- human readability；
- evidence semantics。

### Phase 3 — Canonical Data Migration

分批迁移 legacy objects；每批有回归基线。

### Phase 4 — Enforcement

Schema / Validator / CI 才开始正式拒绝旧写法。

### Phase 5 — Projection

按真实需求增加 JSON-LD / RDF / Property Graph / SQL projections，而不是为了技术完整性提前实现。

---

# 19. Explicit Open Questions

以下问题仍开放，但它们不阻止 v0 核心语义决策：

1. `agent` 是否在第一版 Schema 就支持 `person` / `software_agent`，还是先只迁移 `organization`；
2. `kind` vocabulary 是单一全局表还是按 family 分表；
3. authority / normative status 最小 vocabulary 的精确值；
4. explicit Statement 的最终 YAML 语法与物理存储方式；
5. Relation 与通用 Statement 是继承关系还是同一 Schema 的两种 profile；
6. explicit `value_state` 的具体机器编码；
7. version object 的创建阈值是否需要按对象 family 增加更具体规则；
8. external identifiers / SKOS mappings 第一阶段收录哪些系统；
9. Assessment vocabulary 与 confidence model 应由 #10 Trust Route 进一步定义。

如果其中某一个问题被证明会推翻 D1–D10，才允许增加最多 1–2 个定向样本；否则进入实现设计。

---

# 20. Decision Outcome Proposed

本 Draft 提议接受：

> **InteropAtlas v0 不建立一棵万能分类树，而建立一个最小、可演化、可投影的知识表示合同。**

其核心是：

```text
6 个稳定 Reality Families
+ kind / roles / authority 分层
+ Object / Statement 分离
+ Context / Qualifier
+ Evidence / Provenance
+ Fact / Assessment 分离
+ Missing semantics
+ Family / Version / Part identity rules
+ Validation / Serialization / Query 解耦
```

这套模型故意保持比现实 taxonomy 小得多。

它的目标不是一次描述世界所有细节，而是确保 InteropAtlas 未来从 100 个对象扩展到 1,000、10,000 甚至更多对象时，不会因为早期把现实身份、来源、评价和数据库实现混在一起而被迫推翻全部 Canonical Data。

## Approval boundary

**本文件当前仅为 Draft。**

在 Maintainer 明确批准前：

- 不更新正式 Knowledge Object Specification；
- 不修改 JSON Schema；
- 不迁移现有 Canonical Data；
- 不关闭 #15；
- 不把本模型描述为已采用规范。
