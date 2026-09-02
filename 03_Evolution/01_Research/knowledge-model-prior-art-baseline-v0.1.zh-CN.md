# Knowledge Model Prior Art Baseline v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Research / Prior Art Baseline
Document Created At: 2026-09-01T17:56:34+08:00
Document Updated At: 2026-09-01T17:56:34+08:00
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

> 状态：Research / Prior Art Baseline
>
> Work Item：#53
>
> Parent：#15 Non-normative Knowledge Object Model
>
> 下游：#52 Fit Test Batch 2

## 1. 目的

在继续扩大真实对象 Fit Test 之前，先检查术语学、知识组织、元数据、知识图谱、来源追踪、数据目录与图约束领域已经存在的成熟标准和先例。

目标不是从这些模型里选一个整套复制，而是回答：

```text
哪些原则可以直接 Adopt？
哪些需要形成 InteropAtlas Profile？
哪些现有方案确实没有覆盖，才需要 Extend / Invent？
```

这一步防止 #15 演化成“凭直觉设计自己的万能分类法”。

---

## 2. 当前 Atlas Intake 状态

### 已存在

- `skos_reference` — W3C SKOS Reference，已经位于 `01_State/01_Objects/`。

### 本次可直接进入 Canonical State 的明确规范对象

- ISO 704:2022；
- ISO 25964-1:2011（当前仍为已发布版本，但第二版已进入 FDIS）；
- ISO 25964-2:2013；
- W3C PROV-O；
- DCMI Metadata Terms；
- ISO 15836-2:2019；
- W3C DCAT 3；
- ISO 21127:2023；
- W3C SHACL 2017 Recommendation。

### 暂不强塞当前 Canonical type 的 Modeling Intake

以下对象非常重要，但当前 `reference_project` 可能再次把现实身份与“IA 为什么引用它”混在一起，因此先作为 Prior Art 研究对象，不为了收录数量强塞：

- Wikibase / Wikidata Data Model；
- Schema.org type/property model；
- CIDOC CRM 社区维护模型 / 网站（ISO 21127 已作为正式标准对象收录）；
- SHACL 1.2 Working Draft family（记录演化状态，不冒充 Recommendation）。

---

# 3. Prior Art Map

## 3.1 ISO 704:2022 — 对象、概念、定义、名称必须区分

官方身份：International Standard。

核心启发：ISO 704 明确讨论：

```text
object
  ↓ conceptualization
concept
  ↓ definition
定义
  ↓ designation
名称 / 术语
```

对 #15 的直接意义：

- 现实中的 GOV.UK Design System 是一个对象；
- `Design System` 是我们描述其概念身份的方式；
- 某个中文/英文标签是 designation；
- “成熟先例”不能因为是一个好用的标签，就自动变成它的现实身份。

### 初步判断

**ADOPT PRINCIPLE.**

InteropAtlas 应明确区分 Reality Identity、Conceptual Classification 和 Human-readable Designation。

---

## 3.2 W3C SKOS — 分类体系本身也是图

官方身份：W3C Recommendation；Atlas 已收录为 `skos_reference`。

SKOS 提供 Concept、ConceptScheme 以及 broader / narrower / related 等知识组织关系。

对 #15 的直接意义：

- 分类不必对应物理文件夹；
- 一个对象可以通过不同 Concept Scheme 被多维组织；
- “属于 Human Interface Reference”“属于 Design System”“属于 Government Service”可以是不同视图，不要求复制对象。

### 初步判断

**ADOPT CONCEPT / VIEW SEPARATION；PROFILE MAPPING LATER.**

不建议把全部 Atlas Object 直接退化成 SKOS Concept，但 SKOS 很适合为分类、主题与 vocabulary mapping 提供上游模型。

---

## 3.3 ISO 25964 — Vocabulary 与 Vocabulary Mapping

### Part 1

ISO 25964-1:2011 当前仍是已发布 International Standard，ISO 已明确第二版进入 FDIS 阶段并预计替代 2011 版。

它提供 thesaurus 开发、维护、数据模型与交换方面的成熟实践。

### Part 2

ISO 25964-2:2013 专门处理 thesauri 与其他 vocabulary 之间的互操作和 mapping。

对 #15 的意义：

```text
IA internal concept / kind
        ↕ mapping
external vocabulary / taxonomy
```

可以成为正式问题，而不是把外部分类硬复制进 IA 自己的 `type`。

### 初步判断

**ADOPT MAPPING PRINCIPLE；PROFILE EXTERNAL VOCABULARY ALIGNMENT.**

---

## 3.4 Wikibase / Wikidata Data Model — Entity 与 Statement 分离

官方身份：成熟开放知识基础设施的数据模型先例，不在本研究中把它称为 Formal Standard。

其重要结构包括：

```text
Entity / Item
    ↓
Statement
    ├─ Property / Value
    ├─ Qualifier
    ├─ Reference
    └─ Rank
```

对 Batch 1 最重要的启发：

```text
对象本身
≠
关于对象的陈述
≠
陈述上下文
≠
陈述来源
≠
对陈述的排序 / 评价
```

这与 Batch 1 已经形成的：

```text
what it is
≠ why Atlas references it
≠ how Atlas assesses it
```

高度相容。

### 初步判断

**ADOPT SEPARATION PRINCIPLE；DO NOT COPY FULL WIKIBASE MODEL YET.**

InteropAtlas 可以学习 Statement / Reference / Qualifier 分层，但是否需要完整 statement-level reification，需要由 Evidence / Provenance 工作与真实查询场景共同决定。

---

## 3.5 W3C PROV-O — 来源链、Agent、Role 不应压成一个字段

官方身份：W3C Recommendation。

PROV-O 用 Entity、Activity、Agent 等概念表达 provenance，并提供 attribution、association、derivation 等关系。

对 Batch 1 暴露出的 attribution 问题非常直接：

```text
creator
maintainer
publisher
governing organization
contributor
```

不应该全部压成一个 `organization`。

### 初步判断

**ADOPT ROLE-AWARE PROVENANCE PRINCIPLE；PROFILE MINIMUM ATTRIBUTION MODEL.**

不要求 IA 立刻实现完整 PROV 图，但至少不要设计一个未来无法映射到角色化 provenance 的扁平字段模型。

---

## 3.6 DCMI Metadata Terms / ISO 15836-2 — 宽资源模型 + 可复用属性 + Application Profile

DCMI Metadata Terms 是 DCMI Recommendation；ISO 15836-2:2019 将其主要 Properties 与 Classes 国际标准化。

特别值得 IA 学习的是：

- `type` 描述资源性质 / genre；
- creator、contributor、publisher 等是不同属性；
- DCMI 不限制“resource”只能是什么；
- ISO 15836-2 明确指出这些 terms 通常在 Application Profile 中按本地 / 社区需求约束。

对 #15 的意义：

> 不一定需要先发明一个极其封闭的万能 ontology；可以采用稳定宽语义 + IA Profile 逐步收紧。

### 初步判断

**ADOPT METADATA ROLE SEPARATION；PROFILE IA APPLICATION MODEL.**

---

## 3.7 Schema.org — 宽上位类型 + 丰富 Properties

官方身份：大规模 Web structured-data vocabulary / 成熟先例；本研究不把 Schema.org 本身误标为 Formal Standard。

典型模式：

```text
Thing
  ↓
CreativeWork
  ↓
更具体 subtype

同时通过大量 properties 表达：
author / creator / contributor / publisher / hasPart / isPartOf / ...
```

对 Candidate A / C 的意义：

- 现实大型 vocabulary 并不要求每个细小概念都成为顶层类别；
- stable upper types + properties 是经过大规模实践的可行方向；
- 但 Schema.org 本身的 Web markup 目标与 IA 不同，不能照抄其 taxonomy。

### 初步判断

**ADOPT DESIGN PATTERN；PROFILE, NOT COPY.**

---

## 3.8 W3C DCAT 3 — Dataset / DataService / Catalog / Resource 的身份分离

官方身份：W3C Recommendation，2024-08-22。

DCAT 为 Web 数据目录互操作提供标准 RDF vocabulary，并区分至少：

```text
Catalog
Cataloged Resource
Dataset
DataService
Distribution
```

它还主动复用 Dublin Core、FOAF、SPDX 等既有 vocabulary，而不是重新创造所有术语。

对 #52 中 MDN Browser Compat Data 的意义：

- “一个 GitHub 项目维护着数据”不等于“数据本身的主要现实身份就是 Project”；
- Dataset、Project、Service、Catalog 可以是不同现实 artifact，需要按现实身份与引用需求决定是否拆对象。

### 初步判断

**ADOPT RESOURCE-SEPARATION + VOCABULARY-REUSE PRINCIPLE.**

---

## 3.9 CIDOC CRM / ISO 21127:2023 — 高层语义整合，而不是目录分类

ISO 21127:2023 是已发布国际标准，来源于长期 CIDOC CRM 实践。

它解决的是异构来源的信息交换与语义集成，而不是要求所有数据库采用同一物理结构。

对 IA 的价值主要是架构先例：

> 用稳定的高层语义和关系做 integration layer，而不是把所有现实对象压成一棵目录树。

### 初步判断

**ADOPT SEMANTIC-INTEGRATION PRINCIPLE；DO NOT COPY DOMAIN ONTOLOGY.**

文化遗产领域的具体 classes 不属于 IA 的直接 solution-space taxonomy。

---

## 3.10 W3C SHACL — “对象模型是什么”与“机器怎样验证”分开

稳定基线：2017 W3C Recommendation。

SHACL 用 Shape 表达 RDF graph constraints，并生成 validation results。

2026 年 W3C 正在推进 SHACL 1.2，但截至本研究时间，SHACL 1.2 Core 仍为 Working Draft。

这给 IA 一个很重要的边界：

```text
Conceptual / Semantic Model
        ≠
Validation Contract
```

JSON Schema、SHACL 或其他 validator 可以负责“数据有没有按合同写对”，但不应该反过来因为现有 Schema 写起来方便，就决定现实世界里的对象是什么。

### 初步判断

**ADOPT MODEL / VALIDATION SEPARATION.**

当前 IA 继续使用 JSON Schema 并不与学习 SHACL 冲突；SHACL 更适合作为 graph-native validation 的成熟参照。

---

# 4. Prior Art 原则 → 当前 IA 问题

| 当前问题 | 最相关 Prior Art | 当前判断 |
|---|---|---|
| Reality object 与分类概念混淆 | ISO 704 | Adopt 分离原则 |
| 分类被误做成文件夹树 | SKOS / ISO 25964 | Adopt graph / scheme / mapping 思路 |
| 对象与关于对象的 claim 混淆 | Wikibase | Adopt entity / statement / reference 分层思想 |
| creator / maintainer / publisher 混成 organization | PROV-O + DCMI | Profile role-aware attribution |
| 顶层 type 可能无限膨胀 | Schema.org + DCMI | 优先稳定上位类 + properties / kinds |
| Dataset / Project / Service 混成一个对象 | DCAT | Adopt resource identity separation |
| 异构模型如何共同工作 | CIDOC CRM / ISO 21127 | Adopt semantic integration layer 思路 |
| Schema 方便性反向决定 ontology | SHACL + ISO 704 | 强制区分 semantic model 与 validation contract |
| 外部分类怎么和 IA 对接 | ISO 25964 + SKOS | Profile vocabulary mappings |
| 成熟 / 推荐如何表达 | Wikibase references/rank + PROV/Evidence 思路 | 继续作为 Assessment + Evidence，不作为裸 identity |

---

# 5. 对 Batch 1 候选模型的影响

## Candidate A — 每个概念一个顶层 type

Prior Art 后评价进一步下降。

ISO 704、SKOS、Schema.org、DCMI 都说明：概念身份、分类层级、属性与角色可以分层表达，没有必要让所有细粒度概念都成为最上层互斥 type。

**当前：不推荐。**

## Candidate B — 一个通用 practice/reference 容纳全部非规范知识

仍然过宽。

DCAT 与 PROV/DCMI 进一步说明：不同现实 artifact 对 version、attribution、service/data、maintenance 的需求确实不同，不能只靠一个 `kind` 字段掩盖所有差异。

**当前：不推荐作为单一万能容器。**

## Candidate C — 少量稳定主要身份 + kind / roles / relations / evidence

Prior Art 整体上继续支持这个方向，但需要一个重要修正：

> 不应只讨论“type + kind”，还必须把 **Statements / Attribution / Evidence / Assessment** 的层次一起考虑。

因此下一版工作假设更接近：

```text
Stable Reality Identity
      ↓
Kind / Roles / Relations
      ↓
Claims / Statements
      ↓
Evidence / Provenance
      ↓
Assessment
      ↓
Views / Classification Schemes
```

这仍不是最终 Model Decision。

---

# 6. Adopt → Profile → Extend → Invent 初判

### Adopt

当前已有充分成熟依据，可直接采用的原则：

1. object / concept / designation 分离；
2. storage 与 classification 分离；
3. entity 与 statement / reference 分离；
4. creator / contributor / publisher / role-aware attribution 分离；
5. dataset / catalog / service 等现实 resource identity 可以拆分；
6. semantic model 与 validation contract 分离；
7. vocabulary mapping 是显式关系问题，而不是复制 taxonomy。

### Profile

需要形成 IA-specific Profile 的部分：

1. IA 到底需要哪些稳定主要 object identities；
2. `kind / roles / relations` 的最小 vocabulary；
3. attribution 最小合同；
4. Evidence / Assessment 最小合同；
5. IA internal concepts 与 SKOS / external vocabularies 怎样映射。

### Extend

只有 Batch 2 验证后，若成熟模型无法自然表达 IA 的特定需求，才定义扩展字段或新 relation。

### Invent

目前**没有证据支持发明一套完全独立的新 ontology / provenance / classification framework**。

---

# 7. 对 #52 的直接要求

Batch 2 不再只问“当前 Schema 装不装得下”。

每个样本还必须问：

```text
这个问题是否已经被上述成熟模型解决？
能不能直接 Adopt？
是否只需要 IA Profile？
真正的 gap 在哪里？
```

特别关注：

- Docs as Code：去中心化 Practice identity；
- MDN BCD：对照 DCAT Dataset / Resource；
- GitHub Community Health：Convention / governance mechanism；
- NIST AI RMF：Framework 与 quasi-normative artifact；
- Munzner Nested Model：research-derived model；
- USWDS：Design System umbrella 与 implementation / guidance artifact。

---

# 8. 当前结论

Prior Art Check 已经把 #15 的目标进一步收窄：

> #15 不应该创造“一个负责给世界万物判类别的万能分类模型”。
>
> 它应该定义 **InteropAtlas 为了准确记录现实互操作方案空间所需要的最小知识表示合同**，并尽可能映射到成熟的 terminology、knowledge organization、metadata、provenance 与 validation 标准。

因此下一步是用 #52 的六个真实对象验证这个 Prior Art-informed working model，而不是继续扩大抽象 taxonomy。
