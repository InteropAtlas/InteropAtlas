# JSON-LD 对 InteropAtlas 的适配实验

<!-- InteropAtlas Document Metadata v0
Document Status: 探索性记录，未冻结架构。
Document Created At: 2026-08-30T22:06:53+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

状态：探索性记录，未冻结架构。

## 目标

评估 JSON-LD 是否适合作为 InteropAtlas 的主要事实存储格式、内部语义模型、交换格式或导出格式。

## 当前数据模型观察

InteropAtlas 当前事实源使用 YAML，并通过稳定对象 ID、typed reference（带类型引用）和 first-class Relation（一级关系对象）表达知识。

典型 Relation 不只是简单的 A → B：

```yaml
source: {type: standard, id: json_schema_2020_12}
relation: compatible_with
target: {type: standard, id: example_standard}
confidence: 0.8
scenario_context: [example_scenario]
conditions_zh: 某些条件下兼容
sources:
  - url: https://example.org/
```

关系自身可以拥有证据、置信度、条件、场景上下文和未来可能的时间属性。

## 与 RDF / JSON-LD 的对应

最基础的 InteropAtlas Relation：

`source → relation → target`

与 RDF 的：

`subject → predicate → object`

高度相似，因此 RDF 很适合作为 InteropAtlas 的语义图兼容目标。

JSON-LD 则提供一种基于 JSON 的 Linked Data / RDF 序列化方式。InteropAtlas 对象可以较自然地映射为 JSON-LD 的 `@id`、`@type` 和 IRI 属性。

## 第一轮真实映射实验

已新增：

- `experiments/json-ld/interopatlas-context-v0.1.jsonld`
- `experiments/json-ld/sample-json-ld-maps-to-rdf.jsonld`

实验使用真实对象：

- `json_ld_1.1`
- `rdf_1.2_concepts`
- `graph_representation`
- `json_ld_maps_to_rdf`

第一轮结果：**InteropAtlas 当前对象模型可以无损地序列化进 JSON-LD**，包括 Relation 自身的 `confidence`、`conditions_*`、`capability_context` 和 `sources`。

但这种最直接映射的含义是：InteropAtlas Relation 被表达成一个独立 RDF resource（资源节点），其 `source / relationType / target` 是该节点的属性，而不是直接把它压缩成一个裸 RDF triple。

```text
InteropAtlas Relation object
        ↓
rel:json_ld_maps_to_rdf
  ├─ source → JSON-LD
  ├─ relationType → maps_to
  ├─ target → RDF
  ├─ confidence → 1.0
  └─ evidence → ...
```

这种方式最忠实于当前 InteropAtlas 数据模型，但通用 RDF 查询通常更希望直接看到：

`JSON-LD → mapsTo → RDF`

## 第二轮：RDF 1.2 的重要变化

RDF 1.2 引入 triple terms 和新的 reification 模型。reifier 可以指向一个 triple term，并作为普通 RDF resource 继续承载来源、置信度、条件等描述。

这意味着 InteropAtlas 可以采用双层导出：

```text
JSON-LD ── mapsTo ──→ RDF
            │
            └─ reifier / annotation
                 ├─ confidence
                 ├─ source
                 ├─ conditions
                 └─ scenario context
```

这比 RDF 1.1 时代常见的 `rdf:subject / rdf:predicate / rdf:object` 旧式 reification 更贴近 InteropAtlas 的 first-class Relation。

## 第三轮：真实 RDF 1.2 reifier 实验

新增：

- `standards/rdf-1.2-turtle.yaml`
- `experiments/rdf-1.2/relation-annotation-example.ttl`

使用 RDF 1.2 Turtle annotation syntax 对真实关系：

`json_ld_1.1 → maps_to → rdf_1.2_concepts`

进行表示。实验模式：

```turtle
std:json_ld_1.1 ia:mapsTo std:rdf_1.2_concepts
  ~ rel:json_ld_maps_to_rdf {|
      ia:confidence "1.0"^^xsd:decimal ;
      ia:capabilityContext cap:graph_representation ;
      ia:conditions "..."@en ;
      ia:evidenceSource <https://www.w3.org/TR/json-ld11/>
  |} .
```

验证结果：**RDF 1.2 的“直接语义边 + 显式 reifier + annotation”与 InteropAtlas Relation 模型高度匹配。**

对应关系非常自然：

- `source` → triple subject
- `relation` → RDF predicate
- `target` → triple object
- Relation `id` → reifier IRI
- `confidence` → reifier property
- `conditions_*` → reifier property
- `sources` / evidence → reifier property
- `scenario_context` / `capability_context` → reifier property

而且 RDF 1.2 明确允许同一个 proposition 有多个 reifier，也允许一个 reifier 与多个 proposition 关联。这对 InteropAtlas 未来表达“不同来源对同一个兼容性关系有不同评估”非常有价值。

## 一个重要限制：JSON-LD 1.1 ≠ RDF 1.2 全量语法

第三轮同时发现：**JSON-LD 1.1 本身早于 RDF 1.2 triple terms，并没有 RDF 1.2 triple term / annotation 的原生 JSON-LD 表面语法。**

因此目前不能简单假设：

`RDF 1.2 graph ↔ JSON-LD 1.1`

可以对新 triple-term 结构完全无损往返。

当前最稳妥的 JSON-LD 导出仍然是把 InteropAtlas Relation 保持为普通资源节点：

```text
rel:X
├─ source → A
├─ relationType → mapsTo
├─ target → B
├─ confidence → ...
└─ evidence → ...
```

这可以被 JSON-LD 1.1 无损表达。

因此未来 Engine 可能需要同时支持两种 RDF-facing representation：

### Compatibility representation

使用普通 Relation resource，兼容 JSON-LD 1.1 和传统 RDF 工具。

### Native RDF 1.2 representation

生成 direct semantic edge + RDF 1.2 reifier / annotation，面向 RDF 1.2 / SPARQL 1.2 工具。

两者都从同一个 InteropAtlas Canonical Relation 生成，不作为两份事实源维护。

## 当前判断（第三轮）

现在可以更明确地区分四层：

```text
YAML
↓
InteropAtlas Canonical Data Model
↓
Engine
├─ Linked View / Backlinks
├─ JSON-LD 1.1 compatibility export
└─ RDF 1.2 native graph export
      ├─ direct semantic edge
      └─ reifier / annotation metadata
```

角色分工：

- **YAML**：人工编辑、Git diff、事实源；
- **InteropAtlas Data Model**：内部权威模型；
- **RDF 1.2**：目前最匹配 InteropAtlas Relation 语义的外部图模型；
- **RDF 1.2 Turtle**：验证 relation annotation 的直接实验语法；
- **JSON-LD 1.1**：仍是很有价值的 Web / Agent / API 交换格式，但不能视为 RDF 1.2 新特性的完整序列化；
- **JSON-LD Relation resource representation**：当前最稳妥的无损兼容出口。

## 下一步验证

1. 选择 3–5 条不同性质的 Relation：`provides`、`compatible_with`、`inspired_by`、带 scenario context 的关系。
2. 测试“同一个语义边拥有多个来源/评估”的 multiple reifier 模型。
3. 研究 SPARQL 1.2 是否能自然查询 InteropAtlas Relation metadata。
4. 研究 SHACL 1.2 是否可以验证 Relation reifier 的结构约束。
5. 后续才进入真实 library round-trip 测试。

## 架构原则

> 概念兼容、实现不绑定。

InteropAtlas 应利用 RDF / JSON-LD 的成熟生态，但内部模型仍以 InteropAtlas 自身需求为准。
