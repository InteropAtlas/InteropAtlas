# Schema Migration Dry Run — 2026-09-01

> 状态：Physical placement executed in migration PR; Schema enforcement remains separate

## 1. 目标位置

Schema 不建立独立 `Schemas/` 二级目录，而是与其约束的数据共置：

```text
01_State/01_Objects/
├── base-object.schema.json
├── capability.schema.json
├── implementation.schema.json
├── map.schema.json
├── open-gap.schema.json
├── organization.schema.json
├── reference-project.schema.json
├── scenario.schema.json
└── standard.schema.json

01_State/02_Relations/
└── relation.schema.json
```

## 2. `$id` 与物理位置解耦

各 Schema 已经具有逻辑 `$id`，例如：

```text
https://interopatlas.org/schemas/base-object.schema.json
https://interopatlas.org/schemas/relation.schema.json
```

因此 JSON Schema 中相对 `$ref` 的语义基准是 Schema URI，而不是 GitHub 文件夹位置。

现有：

```json
{"$ref": "base-object.schema.json"}
```

在逻辑上表示同一 Schema namespace 下的：

```text
https://interopatlas.org/schemas/base-object.schema.json
```

所以即使 `relation.schema.json` 与 `base-object.schema.json` 在仓库中分别位于 Relations 与 Objects，**本次物理迁移也不应把 `$ref` 改成 `../01_Objects/...`**。那样会错误地改变逻辑 URI。

这进一步确认同一原则：

> Schema identity / reference ≠ repository physical path.

未来启用 Schema Validator 时，应通过 `$id` / registry / resolver 将逻辑 Schema identity 映射到仓库中的真实文件，而不是要求 Schema URI 模仿 Git 目录结构。

## 3. 不在本次迁移中做的事情

- 不启用全量 Schema enforcement；
- 不清洗 legacy Relation；
- 不合并或重做 type-specific Schema；
- 不改变字段、枚举或 required 规则；
- 不改变 Schema `$id`。

当前部分历史 Relation 尚不满足现有 Relation Schema，因此 Schema enforcement 与 legacy data cleanup 仍应作为独立工作。

## 4. 实际物理迁移

```text
1. 9 个 Object Schema → 01_State/01_Objects/
2. relation.schema.json → 01_State/02_Relations/
3. Schema `$id` 与 `$ref` 的逻辑 URI 保持不变
4. legacy schemas/ 根目录删除
5. CI 路径监听切换到 01_State/**
```

## 5. 结论

Schema 已可以跟数据共置，而不要求其逻辑 identity 跟随文件系统变化。

这与 InteropAtlas 对 Object public route 的处理一致：**稳定身份负责引用，物理路径只负责存储。**
