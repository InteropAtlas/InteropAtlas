# Data Language Stack Comparison v0.1

> 状态：Research / Prior Art Comparison
>
> Work Item：#55
>
> Parent：#15 Knowledge Object Model
>
> 目的：在 InteropAtlas 进入 Model Decision 前，比较成熟的数据语言 / 知识表示体系，提炼真正稳定的共同设计，而不是选择某个数据库产品或照搬某套 ontology。

## 1. 研究问题

InteropAtlas 当前需要定义的不是一张简单分类表，而是一套**最小知识表示合同**。它至少要让 Human / Agent / Engine 对以下问题有共同理解：

```text
一个对象是谁？
它是什么？
有哪些属性和角色？
它与什么有关系？
关于它有哪些陈述？
一条陈述在什么条件下成立？
这条陈述来自哪里？
事实、未知、无值、冲突和评价怎样区分？
机器怎样验证？
查询语言以后怎样稳定地建立在这些语义之上？
```

本研究不寻找“一套直接复制的答案”，而是观察不同成熟体系在长期实践后都不得不解决哪些问题。

---

# 2. 本次比较的四个主体系

## A. Relational Model + SQL

主要参考：

- ISO/IEC 9075-1:2023 SQL/Framework — https://www.iso.org/standard/76583.html
- ISO/IEC 9075-2:2023 SQL/Foundation — https://www.iso.org/standard/76584.html
- ISO/IEC 9075-11:2023 SQL/Schemata — https://www.iso.org/standard/76586.html
- ISO/IEC 9075-16:2023 SQL/PGQ — https://www.iso.org/standard/79473.html

SQL 标准本身就不是一个单文件语法规范，而是把概念框架、基础语言、Schema 信息、扩展等分层。Part 11 明确负责描述 SQL-data 的结构和 integrity constraints；Part 16 又把 Property Graph Queries 引入 SQL 体系。

## B. RDF / Semantic Web Stack

主要参考：

- RDF 1.2 Concepts — https://www.w3.org/TR/rdf12-concepts/
- RDF 1.2 Schema — https://www.w3.org/TR/rdf12-schema/
- OWL 2 — https://www.w3.org/TR/owl2-overview/
- SKOS — https://www.w3.org/TR/skos-reference/
- SHACL 2017 / SHACL 1.2 draft — https://www.w3.org/TR/shacl/ / https://www.w3.org/TR/shacl12-core/
- SPARQL 1.1 / SPARQL 1.2 draft — https://www.w3.org/TR/sparql11-query/ / https://www.w3.org/TR/sparql12-query/
- JSON-LD 1.1 — https://www.w3.org/TR/json-ld11/

RDF 特别强调：**RDF 是抽象数据模型，不等于 Turtle、JSON-LD、RDF/XML 等任何一种序列化格式。**

## C. Wikibase / Wikidata Data Model

主要参考：

- Wikibase Data Model — https://www.mediawiki.org/wiki/Wikibase/DataModel
- Wikibase Data Model Primer — https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer
- Wikidata Data Model — https://www.wikidata.org/wiki/Wikidata:Data_model

它是本研究中最重要的“真实大规模开放知识库”案例。

## D. Property Graph + GQL

主要参考：

- ISO/IEC 39075:2024 GQL — https://www.iso.org/standard/76120.html
- ISO/IEC 9075-16:2023 SQL/PGQ — https://www.iso.org/standard/79473.html

GQL 已经成为独立国际标准，定义 Property Graph 的数据结构和创建、访问、查询、维护等基本操作。SQL/PGQ 则说明关系模型和 Property Graph 并不是必须互斥的两个世界。

---

# 3. 第一层比较：基本数据单位

| 体系 | 最基本单位 | 世界观 |
|---|---|---|
| Relational / SQL | Table / Row / Column | 数据组织成关系与受约束的记录集合 |
| RDF | Triple / Graph / Dataset | 世界由 subject-predicate-object 陈述组成 |
| Wikibase | Entity + Statement | 对象和“关于对象的陈述”明确分离 |
| Property Graph / GQL | Graph elements + properties | 对象和关系都是图中的第一等工程元素 |

## 对 IA 的启发

四套体系虽然结构不同，但都不会把“文件”当作知识本体。

因此 IA 当前继续使用 YAML 没有问题，但必须保持：

> **YAML 是序列化 / authoring format，不是知识模型本身。**

这个原则应成为正式模型不变量。

---

# 4. 稳定身份：系统做大以后最先遇到的问题

## SQL

SQL 常通过 key / primary key / unique constraint 在表内维护身份和唯一性；身份与显示名称分离。

## RDF

全球可引用资源通常使用 IRI。RDF 强调同一 IRI 在图中指向同一资源语义，序列化前缀只是缩写，不属于抽象数据模型。

## Wikibase

Item / Property 使用稳定的机器 ID（Q / P），同时维护多语言 label、description、alias。名字可以改，ID 不应跟着改。

## Property Graph

具体系统实现 identity 的方式不同，但查询模型依然需要稳定引用图元素；应用层不应把可变 display label 当成唯一 identity。

## 对 IA 的结论

**立即 Adopt：**

```text
stable id
≠ display name
≠ translated label
≠ physical file path
≠ public navigation path
```

这一点 IA 已经部分实现，应继续强化。

未来规模扩大后最危险的债务之一，就是让名称、文件名或目录路径承担 identity。

---

# 5. Type、Kind、Property、Relation：不要全部塞进“类型”

## SQL 的教训

关系模型倾向先定义结构和字段，再通过 column data type、constraints、foreign key 等表达不同规则。并不是每多一个业务语义就创建一种全新的数据库语言类型。

## RDF / OWL / SKOS

RDF 本身非常小；更丰富的 class / property semantics 由 RDFS、OWL、SKOS 等 vocabulary 逐层增加。

这形成一种重要架构：

```text
minimal graph model
      ↓
vocabulary / ontology
      ↓
application profile
```

而不是让基础数据模型知道全世界所有类别。

## Wikibase

Item 和 Property 是非常稳定的上层实体种类；具体“human、standard、design system、method”等知识分类主要通过 Property / Statement 表达，而不是为每种现实类别增加新的 Wikibase Entity type。

## Property Graph

Property Graph 工程上通常通过 labels / types / properties / edge types 组织语义，同样说明“对象类型”只是语义的一部分。

## 对 IA 的结论

这四套体系共同支持 Batch 1 当前方向：

> **少量稳定上位 identity family + kind / roles / relations / properties**

而不是：

```text
method type
framework type
heuristic type
design_system type
precedent type
...
```

无限膨胀。

---

# 6. 最重要的新问题：Statement 必须成为独立设计对象

这是本轮研究对 #15 最大的修正。

早期 IA 很容易把知识理解成：

```text
Object
  fields...
```

但 Wikibase 和 RDF 1.2 都说明，系统做大后不能只管理“对象”，还要管理：

> **关于对象的一条具体陈述。**

## Wikibase

Wikibase 的 Statement 不是单纯 property-value，而是：

```text
Statement
├─ subject
├─ main value / claim
├─ qualifiers
├─ references
└─ rank
```

Qualifier 是 Statement 意义的一部分，可表示：

- 何时成立；
- 采用什么测量方法；
- 在什么范围成立；
- 某关系中的具体角色。

Reference 则回答这条 Claim 来自哪里。

Rank 又是对多个 Statement 进行粗粒度选择的机制。

## RDF 1.2

2026 年 RDF 1.2 Candidate Recommendation 引入 triple terms / reification。

它允许：

```text
先引用一个 proposition
        ↓
再为它创建 reifier
        ↓
给这个 reifier 挂来源、时间、上下文、信念、事件等信息
```

而且被引用的 proposition **不一定必须被断言为事实**。

这意味着可以表达：

- 某来源声称 A 与 B 兼容；
- 另一来源不同意；
- IA 当前没有把其中任何一个直接升级为 canonical fact；
- 同一个 proposition 可以存在多个不同来源 / 上下文的 reifier。

## 对 IA 的结论

**Statement / Claim 应从“未来也许需要”提升为模型中的明确保留层。**

但当前体量仍小，不一定马上把所有简单字段改造成独立 Statement 文件。

推荐分两步：

```text
现在：
Object / Relation 模型必须保证未来可以升级到 statement-level provenance

未来有真实需求时：
把高风险 / 多来源 / 有时间上下文 / 可冲突的信息升级为 explicit Statement
```

不能设计一个会阻止未来升级的扁平 Schema。

---

# 7. Evidence / Provenance：来源应该挂在哪里？

四套体系中，真正复杂的知识系统都会区分：

```text
对象的来源
vs
某条具体陈述的来源
```

例如：

```text
GOV.UK Design System 的官方网站
```

可以作为 Object identity source。

但：

```text
“GOV.UK Design System 被 500 个服务采用”
```

需要的是**这条 Statement 自己的 Evidence**。

Wikibase Reference、PROV-O、RDF reification 都支持这种方向。

## 对 IA 的结论

当前 `sources` 字段可以继续服务简单对象，但正式模型必须区分至少两层：

```text
Object Source / Identity Source
Statement Evidence / Provenance
```

以后不应该把所有 Evidence 都无差别挂在对象根节点。

---

# 8. Unknown、No Value、Missing：一个经常被低估的问题

## SQL

SQL 使用 NULL 处理缺失 / 未知信息，但长期实践也说明 NULL 语义很容易给查询和约束带来复杂性。

## RDF

RDF 的开放世界假设意味着：

> 图里没有一条信息，通常不能直接推出“它不存在”。

缺失不是否定。

## Wikibase

Wikibase 更进一步明确区分：

```text
missing
= 目前没有记录

unknown value
= 我们知道有值，但不知道具体是什么

no value
= 明确知道不存在这样的值
```

这是一个非常值得 IA Adopt 的设计。

## 对 IA 的结论

未来不能用：

```yaml
field: null
```

同时表达所有情况。

至少在语义层必须保留：

```text
not recorded
unknown
explicit none
known value
```

当前不要求立刻给全部字段增加四态，但模型必须禁止把“字段不存在”自动解释成否定事实。

---

# 9. Semantic Model 与 Validation Contract 必须分开

这是 SQL、RDF/SHACL、JSON Schema 都共同说明的设计。

## SQL

SQL 的 conceptual framework、data language 和 information / definition schema 是分层规范。

## RDF

RDF 定义数据模型；RDFS / OWL 定义更多语义；SHACL 用于约束验证。

尤其重要的是：

> RDF / OWL 的语义推理与 SHACL 的 closed-world-like validation 不是同一件事。

## JSON Schema

JSON Schema 当前 Draft 2020-12 本身也拆为 Core 与 Validation。

## 对 IA 的结论

继续正式采用：

```text
Knowledge Model
“什么意思”
        ≠
Schema / Validator
“结构是否合法”
```

因此 #15 先做语义 Model Decision，再决定如何修改 JSON Schema 是正确顺序。

---

# 10. Query Language 是下游，不应该反向绑死模型

## SQL

SQL Query 建立在 SQL data model 上。

## SPARQL

SPARQL 明确定义为对 RDF graph / dataset 的查询语言。2026 年 SPARQL 1.2 仍在 Working Draft；稳定 Recommendation 仍是 1.1。

## GQL

ISO/IEC 39075:2024 定义 Property Graph 的查询与管理语言。

## Wikidata

Wikidata 内部采用 Wikibase model，对外可以投影成 RDF 并使用 SPARQL 查询。

这个案例对 IA 特别重要：

> **内部 authoring / canonical model 与查询 projection 不必完全相同。**

## 对 IA 的结论

InteropAtlas 现在**不应该发明 IA Query Language**。

应该保证最小知识合同未来至少能够：

```text
→ 投影成 RDF / SPARQL
→ 投影成 Property Graph / GQL-like query
→ 投影成 relational views / SQL
→ 被当前 Python Engine 查询
```

因此继续坚持：

> graph-native, database-agnostic

但这里的 database-agnostic 不是“什么都不设计”，而是**语义合同稳定、存储和查询技术可替换**。

---

# 11. Relational 与 Graph 正在收敛，而不是互相淘汰

一个值得提前注意的长期趋势：

- SQL/PGQ 已在 ISO/IEC 9075-16:2023 中成为 SQL 标准的一部分；
- GQL 2024 又独立成为 Property Graph 国际标准。

这说明未来 IA 不应押注：

```text
“关系数据库已经过时”
```

或：

```text
“所有东西最终必须 RDF 化”
```

更合理的是保持可投影性。

对 IA 来说：

```text
Canonical semantic contract
        ↓
不同技术 projection
```

比“选择唯一数据库哲学”更稳健。

---

# 12. Serialization 必须与 Model 解耦

RDF 生态非常明确地证明：

```text
同一个 abstract data model
可以有 Turtle / TriG / N-Triples / JSON-LD / RDF/XML 等不同 serialization
```

JSON-LD 1.1 的定位就是“JSON-based serialization for Linked Data”，不是另一个独立世界模型。

## 对 IA 的结论

现在选择 YAML 是合理的 Human/Agent authoring 决策，但正式语义不能依赖：

- YAML 特定层级；
- 文件嵌套；
- 某个目录；
- 字段顺序。

未来如果需要 JSON-LD / RDF export，应该是 projection / mapping，而不是重新建一套 facts。

---

# 13. 外部 Vocabulary / Federation：不要自己定义全世界

SKOS、ISO 25964、RDF、JSON-LD 共同提供一个长期重要经验：

> 一个知识系统不必把所有外部概念复制成自己的内部 taxonomy。

InteropAtlas 未来更合理的是：

```text
IA stable internal identity / semantics
        ↓ mappings
Wikidata / SKOS vocab / Schema.org / domain ontology / external IDs
```

当前体量不需要马上做完整 vocabulary federation，但至少要预留：

- external identifier；
- equivalent / close / broader / narrower mapping；
- mapping provenance。

避免未来通过名称字符串做脆弱匹配。

---

# 14. Schema / Vocabulary Evolution：现在就要避免的长期坑

四类成熟体系都经历了版本演化。

IA 当前最应该避免的是把第一版 Schema 当成不可变 ontology。

建议未来正式区分：

```text
Object identity version
≠ factual state version
≠ vocabulary/schema version
≠ source version
```

并坚持：

1. stable ID 尽量不随 Schema 版本变化；
2. 新字段优先 additive；
3. breaking semantic changes 必须有 migration rationale；
4. deprecated term 不等于立即删除历史事实；
5. 查询层以后应该尽量通过稳定语义名，而不是物理 YAML 路径。

当前无需建立复杂 migration framework，但模型规范应该写下这些不变量。

---

# 15. 规模扩大后最可能遇到的 8 类问题

这部分是本研究最值得提前规划、但不要求现在全部实现的内容。

## 15.1 Predicate / Relation vocabulary explosion

不同贡献者创建：

```text
supports
provides
provides_capability
enables
offers
```

最后语义几乎相同但查询无法统一。

**现在就要做：** Relation vocabulary 有稳定定义和 review。

## 15.2 Object type explosion

每遇到一个现实名词就新增 type。

**现在就要做：** 少量 stable family + kind / role。

## 15.3 Evidence 挂错层

Object sources 与 Statement evidence 混在一起。

**现在要预留；不必全面实现。**

## 15.4 Conflicting claims

不同权威来源给不同版本、兼容性、成熟度判断。

**未来需要：** explicit Statement + source/context，不允许后写覆盖前写。

## 15.5 Unknown / None / Missing 混淆

导致错误查询和错误推理。

**现在语义规范必须区分。**

## 15.6 Schema evolution 把 ID / query 打碎

**现在就要禁止：** 语义 identity 绑定物理 Schema 路径。

## 15.7 External vocabulary drift

外部 ID / taxonomy 改动后映射失效。

**未来预留：** mapping source/version。

## 15.8 Query implementation leak

为了当前 Python Engine 好写，反过来扭曲语义模型。

**现在就要禁止。**

---

# 16. 四套体系共同出现的“稳定核心”

这张表比选择某个技术栈更重要。

| 稳定能力 | SQL | RDF | Wikibase | Property Graph | IA 建议 |
|---|---:|---:|---:|---:|---|
| Stable identity | ✓ | ✓ | ✓ | ✓ | 现在必须 |
| Types / classes | ✓ | ✓ | ✓ | ✓ | 现在必须，但保持少量稳定层 |
| Properties / values | ✓ | ✓ | ✓ | ✓ | 现在必须 |
| Explicit relations | ✓ | ✓ | ✓ | ✓ | 现在必须 |
| Constraints | ✓ | SHACL / OWL distinction | property constraints | schema / implementation | 现在需要基本层 |
| Statement context | 需额外表/结构 | RDF 1.2 reification | qualifier | edge / reified node pattern | 现在预留 |
| Provenance / evidence | 需额外 schema | PROV / reification | references | app model | 现在预留并分层 |
| Unknown / no-value semantics | NULL 等 | open world / vocabulary | explicit somevalue/novalue | app model | 语义上现在必须区分 |
| Query language | SQL | SPARQL | SPARQL projection | GQL | 暂不自创 |
| External mapping | join / ETL | IRI / vocab / SKOS | external IDs | app-level | 未来预留 |
| Serialization independence | 中 | 很强 | JSON + RDF projection | DB-specific | IA 必须坚持 |

---

# 17. InteropAtlas 最小知识表示合同：v0 工作假设

经过 Prior Art + 本轮 stack comparison，目前最值得带入 #52 的模型不再只是：

```text
Type + Kind + Roles
```

而应该扩大成以下分层：

```text
1. Identity
   stable id / names / external ids

2. Reality Classification
   stable family / kind

3. Object Properties
   对象自身相对稳定的描述

4. Roles / Relations
   对象在不同上下文中的角色与连接

5. Statement / Claim Layer
   对对象或关系的具体陈述

6. Context / Qualifier
   时间、范围、方法、版本、条件

7. Evidence / Provenance
   谁说的、哪里来的、何时获取

8. Assessment
   IA 或来源做出的评价，与事实分开

9. Validation Contract
   JSON Schema / future graph validation

10. Projection / View / Query
    Engine / RDF / Property Graph / SQL 等下游
```

这不是说 v0 要马上实现十套目录或十种文件。

它是**逻辑层次**。

物理实现仍然可以非常简单。

---

# 18. 现在就需要 / 未来预留 / 当前不要做

## 现在就需要

1. Stable ID 与显示名称彻底分离；
2. 少量稳定 family + kind / roles；
3. Relation vocabulary 的语义一致性；
4. Fact / Assessment 分离；
5. Object Source 与 Statement Evidence 概念分离；
6. missing / unknown / explicit none 的语义区分；
7. semantic model ≠ JSON Schema；
8. serialization / physical path ≠ semantic identity；
9. 任何设计不得阻止未来 Statement / Qualifier / Provenance 升级。

## 未来预留，但当前不全面实现

1. explicit Statement ID；
2. qualifier / temporal validity；
3. conflicting claims；
4. statement-level references；
5. external vocabulary mapping；
6. RDF / JSON-LD export；
7. Property Graph / GQL projection；
8. graph canonicalization / signing（如未来需要可信发布 / DID / content-addressing）；
9. richer inference / entailment。

## 当前不要做

1. 不发明 IA Query Language；
2. 不实现完整 OWL ontology；
3. 不把全部字段改造成 Wikibase-style Statement；
4. 不强制 RDF 作为 Canonical storage；
5. 不选定 Neo4j / PostgreSQL / triple store；
6. 不为了未来百万对象规模提前做复杂分片 / distributed DB；
7. 不建立几十个顶层 object type。

---

# 19. 对 #52 Batch 2 的具体修改建议

Batch 2 六个对象除了原 Fit Test 字段，应新增四个检查维度：

```text
A. Identity vs Statement
哪些信息属于对象本身，哪些其实是一条可变陈述？

B. Context
这条信息是否需要时间 / 版本 / 方法 / 适用范围？

C. Evidence granularity
来源应该挂对象还是挂 Statement？

D. Missing semantics
不存在、未知、尚未收录是否可能被混淆？
```

这样 Batch 2 才是在验证“数据语言”，而不只是验证分类表。

---

# 20. 当前 Model Decision 方向

本研究目前**不支持**把 InteropAtlas 直接建成 SQL schema、完整 RDF ontology、Wikibase clone 或纯 Property Graph schema。

更适合当前规模的方向是：

> **保持轻量 YAML Canonical authoring + graph-native semantic contract；吸收 Wikibase 的 Statement / Evidence 分层、RDF 的 model/serialization 分离与 reification 能力、SQL 的约束纪律、GQL / Property Graph 的工程图查询思想。**

也就是说：

```text
InteropAtlas 不复制某一种语言，
而是借鉴这些语言长期演化后都证明必要的“语义骨架”。
```

当前最重要的不是语言功能最多，而是：

> **v0 足够小，但未来不会因为现在的设计失误而被迫推翻所有 Canonical Data。**

---

# 21. 结论

经过四套主体系比较，#15 的目标进一步明确：

> **InteropAtlas Knowledge Model 应是一套最小、可演化、可投影的数据语言语义合同。**

它当前不负责定义最终查询语法，也不负责选择数据库。

它必须先稳定以下边界：

```text
Identity
Reality Classification
Property / Relation
Statement
Context
Evidence / Provenance
Assessment
Validation
Projection / Query
```

其中前四层需要在 v0 Model Decision 中直接解决；Statement / Context / Evidence 必须至少做明确的升级预留；查询语言和数据库选择继续留在下游。

下一步应使用 #52 的 6 个真实对象，对这套 Prior Art-informed working model 做最后一轮主要压力测试，再进入 #15 Model Decision。
