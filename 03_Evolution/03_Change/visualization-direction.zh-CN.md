# 图形化关系呈现方向

<!-- InteropAtlas Document Metadata v0
Document Status: Future Direction（后续方向），当前不冻结技术方案。
Document Created At: 2026-08-30T19:10:31+08:00
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

> 状态：Future Direction（后续方向），当前不冻结技术方案。

InteropAtlas 的核心数据天然具有图结构：标准、能力、组织、实现、场景、参考项目和未来的评估结果都是节点，`uses`（使用）、`provides`（提供）、`depends_on`（依赖）、`alternative_to`（替代）、`bridges_to`（桥接）等是边。

因此后期采用 Graph Visualization（图形化关系呈现）是自然方向，而且很可能比纯列表更适合探索复杂互操作关系。

但“图形化界面”不应该成为事实源。当前原则是：

```text
YAML / 数据库中的结构化事实
          ↓
       Engine
          ↓
查询 / 筛选 / 路径搜索 / 评估
          ↓
图形化视图、列表视图、表格视图、API
```

也就是说，图只是 View（视图）之一。用户未来可能按照领域、能力、层级、开放程度、组织、时间、场景等条件筛选，再把筛选结果渲染成图。

暂时不决定底层一定使用图数据库还是关系数据库，也不决定使用哪种前端图库。v0.1 只要求数据中的对象和关系足够明确，使未来可以生成图。

## 当前需要提前保证的事情

1. 每个对象有稳定 ID；
2. Relation（关系）是一等对象，而不是埋在自然语言里；
3. 关系具有明确类型；
4. 关系可以附带场景、能力、条件、证据和置信度；
5. 图形化展示与底层存储解耦。

如果这些基础保持稳定，未来无论使用图数据库、关系数据库还是静态生成，都可以构建图形化关系界面。
