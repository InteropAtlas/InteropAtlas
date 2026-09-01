# Schema Migration Dry Run — 2026-09-01

> 状态：Dry Run / No physical migration

## 1. 目标位置

已确认：Schema 不建立独立 `Schemas/` 二级目录，而是与其约束的数据共置。

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

`schemas/README.md` 不作为一个独立 Schema 区继续迁移；其中“YAML 使用 JSON Schema 做机器验证、Schema 属于机器可读合同”的有效说明应合并进 `01_State/01_Objects/README.md` 与 `01_State/02_Relations/README.md`。

## 2. 引用检查

现有各 Object type-specific Schema 都以相对引用继承：

```json
{"$ref": "base-object.schema.json"}
```

因为它们未来与 `base-object.schema.json` 同处 `01_Objects/`，这些引用在搬迁后仍然有效，不需要修改。

`relation.schema.json` 也引用：

```json
{"$ref": "base-object.schema.json"}
```

但它未来位于 `02_Relations/`，因此这是当前 Schema 搬迁中唯一明确会因目录变化而断开的跨目录引用。

最小迁移修复：

```json
{"$ref": "../01_Objects/base-object.schema.json"}
```

这只修复物理位置，不改变 Relation 数据模型。

## 3. `$id` 不随物理目录改动

当前 Schema 使用类似：

```text
https://interopatlas.org/schemas/standard.schema.json
https://interopatlas.org/schemas/relation.schema.json
```

作为 JSON Schema `$id`。

本次目录迁移不应因为 GitHub 文件位置变化就自动改这些逻辑标识。`$id` 与 repository physical path 分离，和对象公开 URL 与物理路径分离采用同一原则。

如果未来要正式提供可解析的 Schema 公共 URL，应另行决定，不与本次目录搬迁混做。

## 4. 不在本次迁移中做的事情

- 不启用全量 Schema enforcement；
- 不清洗 legacy Relation；
- 不合并或重做 type-specific Schema；
- 不改变字段、枚举或 required 规则；
- 不改变 Schema `$id`。

原因：当前部分历史 Relation 尚不满足现有 Relation Schema；若同时启用强制验证，会把“搬目录”变成 Data Model / 数据清洗项目。

## 5. 迁移时的最小操作

```text
1. 将 9 个 Object Schema 移入 01_State/01_Objects/
2. 将 relation.schema.json 移入 01_State/02_Relations/
3. 将 relation.schema.json 的 base-object $ref 改为 ../01_Objects/base-object.schema.json
4. 将 schemas/README.md 中仍有效的说明合并到两个 State README
5. 删除空的 schemas/ legacy root
6. 同步更新 CI 的 schemas/** 路径监听
```

完成后必须保持现有 Engine / Graph 行为基线不变。

## 6. 结论

Schema 物理迁移没有发现新的结构性阻塞点。

真正迁移时只有一个已知的 Schema 路径修复：`relation.schema.json → base-object.schema.json` 的跨目录 `$ref`。其余 Object Schema 与 Base Object 共置，因此现有相对引用可以原样保留。
