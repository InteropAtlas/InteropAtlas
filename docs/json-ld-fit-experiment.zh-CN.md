# JSON-LD 对 InteropAtlas 的适配实验

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

这点非常重要：

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

这种方式最忠实于当前 InteropAtlas 数据模型，但在通用 RDF 工具看来，它不是最简洁的：

`JSON-LD → mapsTo → RDF`

直接三元组形式。

## RDF 1.2 带来的重要变化

2026 年的 RDF 1.2 Candidate Recommendation 已引入 triple terms（把三元组作为 RDF term）和 reification（关系/命题实体化）的新模型。

这意味着 InteropAtlas 可以考虑双层导出：

```text
JSON-LD ── mapsTo ──→ RDF
            │
            └─ reifier / annotation
                 ├─ confidence
                 ├─ source
                 ├─ conditions
                 └─ scenario context
```

这样既保留标准 RDF 图中的直接语义边，又可以给该关系附加证据和上下文。

这比旧式“把每条三元组拆成 rdf:subject / rdf:predicate / rdf:object”更接近 InteropAtlas 的 first-class Relation 思路。

不过 RDF 1.2 当前仍处于 Candidate Recommendation 阶段，因此 InteropAtlas 不应立即依赖其作为唯一稳定导出机制。

## 适配优势

1. **全局可解析标识**：稳定对象 ID 可映射为 IRI。
2. **语义明确**：Relation 类型可以映射为 RDF predicate。
3. **外部互操作**：可进入 RDF、Linked Data、SPARQL 和知识图谱生态。
4. **机器友好**：Agent 和外部工具不必只理解 InteropAtlas 私有 YAML 结构。
5. **Web 原生**：JSON-LD 与 Web/HTTP/IRI 体系天然衔接。
6. **Relation 元数据可以保留**：即使不用 RDF 1.2 triple annotation，也可将 Relation 保持为一级资源节点进行无损导出。

## 当前阻力

### 1. 人工编辑体验

JSON-LD 比当前 YAML 更冗长，`@context`、IRI 和嵌套对象会增加认知负担。对于大量社区贡献者，直接把 JSON-LD 作为主要编辑格式可能降低可读性和 Git diff 体验。

### 2. 内部 Relation 模型与通用 RDF 图之间需要映射层

直接将 Relation 导出为资源节点最无损，但图查询者可能更希望看到：

`A → predicate → B`

因此 Engine exporter 最终可能需要同时生成：

- **Canonical relation resource**：完整保留 InteropAtlas Relation 元数据；
- **Semantic edge**：生成便于 RDF/SPARQL 查询的直接 predicate 边；
- 可选 RDF 1.2 reifier / annotation：把两者正式关联起来。

### 3. 双链体验仍需 View / Engine

JSON-LD 能让机器理解“这个值是链接”，但它本身不会自动提供：

- 点击跳转
- Backlinks（反向链接）
- Graph View（图视图）
- Hover Preview（悬浮预览）

这些仍然需要 Reference Resolver、Backlink Indexer 和最终的人类浏览 View。

## 当前结论（第二轮）

JSON-LD 的适配性比第一轮预估更好，但结论仍然是：**不替换 YAML，而是成为高优先级语义交换层。**

当前建议架构：

```text
YAML
  ↓
InteropAtlas Canonical Data Model
  ↓
Engine Graph
  ├─ Linked View / Backlinks
  ├─ direct semantic edges
  └─ canonical Relation resources
          ↓
    RDF-compatible mapping
          ↓
       JSON-LD
```

角色分工：

- YAML：主要人工编辑与 Git 事实源；
- InteropAtlas Data Model：内部权威语义模型；
- RDF：图语义兼容模型与查询生态基础；
- JSON-LD：高优先级交换/发布/Agent 接口格式；
- RDF 1.2 triple terms / reification：很有潜力成为 Relation 元数据的标准映射机制，但在标准成熟前保持实验状态。

## 下一步验证

1. 设计一个 Relation 的“双表示”导出：Relation resource + direct semantic edge。
2. 研究 RDF 1.2 reifier / triple annotation 对 `confidence / evidence / conditions / scenario_context` 的精确映射。
3. 用真实的 3–5 条复杂 Relation 测试。
4. 后续用支持 JSON-LD/RDF 1.2 的库实际做 expand / compact / RDF round-trip。
5. 若往返转换稳定，再将 JSON-LD exporter 纳入 Engine。

## 架构原则

> 概念兼容、实现不绑定。

InteropAtlas 可以兼容 RDF / JSON-LD，而不必把自身内部模型完全绑定到 RDF 或 JSON-LD。
