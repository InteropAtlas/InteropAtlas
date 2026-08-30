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

示意：

```json
{
  "@context": {
    "ia": "https://interopatlas.org/vocab/",
    "provides": {"@id": "ia:provides", "@type": "@id"}
  },
  "@id": "https://interopatlas.org/standard/json_schema_2020_12",
  "@type": "ia:Standard",
  "provides": "https://interopatlas.org/capability/schema_validation"
}
```

## 适配优势

1. **全局可解析标识**：稳定对象 ID 可映射为 IRI。
2. **语义明确**：Relation 类型可以映射为 RDF predicate。
3. **外部互操作**：可进入 RDF、Linked Data、SPARQL 和知识图谱生态。
4. **机器友好**：Agent 和外部工具不必只理解 InteropAtlas 私有 YAML 结构。
5. **Web 原生**：JSON-LD 与 Web/HTTP/IRI 体系天然衔接。

## 当前阻力

### 1. 人工编辑体验

JSON-LD 比当前 YAML 更冗长，`@context`、IRI 和嵌套对象会增加认知负担。对于大量社区贡献者，直接把 JSON-LD 作为主要编辑格式可能降低可读性和 Git diff 体验。

### 2. Relation 自身的元数据

InteropAtlas 将 Relation 视为一级对象，而标准 RDF 三元组本身没有天然承载 confidence、conditions、evidence、scenario_context 等关系元数据的位置。

RDF 可以通过 reification、named graphs 或 RDF-star 等机制处理，但会显著增加模型复杂度。InteropAtlas 不应为了追求 RDF 纯度而削弱自身关系模型。

### 3. 双链体验仍需 View / Engine

JSON-LD 能让机器理解“这个值是链接”，但它本身不会自动提供：

- 点击跳转
- Backlinks（反向链接）
- Graph View（图视图）
- Hover Preview（悬浮预览）

这些仍然需要 Reference Resolver、Backlink Indexer 和最终的人类浏览 View。

## 当前结论

暂不建议用 JSON-LD 替换 YAML 作为主要人工事实源。

当前更合理的分工是：

```text
YAML
  ↓
InteropAtlas Data Model
  ↓
Engine Graph
  ↓
RDF-compatible semantic mapping
  ↓
JSON-LD export / interchange
```

因此当前优先级判断为：

- YAML：主要人工编辑与 Git 事实源
- InteropAtlas Data Model：内部权威语义模型
- RDF：图语义兼容模型与理论基础
- JSON-LD：高优先级交换/导出格式候选

## 下一步实验

1. 为 InteropAtlas 定义最小 JSON-LD `@context` 草案。
2. 选择 3–5 个已有对象和 Relation 做无损导出实验。
3. 检查 Relation 元数据如何映射而不丢失信息。
4. 测试 JSON-LD → RDF → JSON-LD round-trip（往返转换）。
5. 如果转换稳定，再考虑把 JSON-LD exporter 纳入 Engine。

## 架构原则

> 概念兼容、实现不绑定。

InteropAtlas 可以兼容 RDF / JSON-LD，而不必把自身内部模型完全绑定到 RDF 或 JSON-LD。
