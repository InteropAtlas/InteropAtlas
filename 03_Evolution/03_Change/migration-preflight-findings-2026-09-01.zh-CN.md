# Repository Migration Preflight Findings — 2026-09-01

> 状态：Preflight / No physical migration

本文记录三层目录正式迁移前的实际代码与数据检查结果。它不授权移动现有文件。

## 1. Schema：当前是“合同草案”，还不是自动执行的验证系统

当前 `engine/requirements.txt` 只有 PyYAML 与 Markdown，没有 JSON Schema Validator 依赖；现有 GitHub Actions 也没有执行 Schema Validation。

因此当前 `schemas/*.schema.json` 虽然表达机器可读合同，但它们尚未成为 CI 的强制质量门。

这带来两个结论：

1. 物理移动 Schema 本身目前不会直接破坏一个正在运行的 Validator，因为当前没有这样的 Validator；
2. 不能把“现有 Schema 文件存在”误认为“当前全部 Canonical Data 已经通过 Schema 验证”。

### 现有 Schema 引用

Object type-specific Schema（例如 `standard.schema.json`）通过相对引用：

```json
{"$ref": "base-object.schema.json"}
```

继承 `base-object.schema.json`。

`relation.schema.json` 也通过同样方式引用 `base-object.schema.json`。

如果未来：

```text
base-object.schema.json → 01_State/01_Objects/
relation.schema.json    → 01_State/02_Relations/
```

则 Relation Schema 的相对 `$ref` 需要同步调整，或改成稳定的 Schema identifier / resolver 机制。

### Schema 与真实数据存在历史差异

部分较新的 Relation 已具有：

```text
id + type: relation + name_zh/name_en + source + relation + target
```

但仓库仍存在 legacy Relation，仅有：

```text
id + source + relation + target
```

缺少当前 `relation.schema.json` 继承自 Base Object 后要求的 `type`、`name_zh`、`name_en`。

Engine 已通过内容兼容规则支持这些 legacy Relation，因此现阶段不能突然把现有 Relation Schema 作为全量强制门，否则会把“目录迁移”意外变成“历史数据清洗”。

结论：

> Schema 的目标位置已经决定，但 Schema enforcement 与 legacy data cleanup 应作为后续独立工作，不和物理目录迁移捆绑。

---

## 2. Public Route：当前确实依赖物理文件路径

当前 Loader 为文档写入：

```text
_source = repository-relative physical source path
_physical_source = repository-relative physical source path
```

`render_markdown.py` 的 `output_path()` 直接读取 `_source`，把 `.yaml` 改成 `.md`；对象之间的链接也基于这个输出路径计算。

因此当前逻辑实际上是：

```text
物理文件在哪里
      ↓
生成页面在哪里
      ↓
对象之间的网页链接怎么写
```

这正是物理迁移前必须拆开的耦合。

### 推荐目标

Public Route 应由稳定对象身份决定，而不是由知识分类文件夹或物理存储决定。

候选方向：

```text
A. /objects/<stable-id>.html
B. /id/<stable-id>.html
C. /<type>/<stable-id>.html
```

其中 A/B 对未来最稳定，因为即使对象分类/type 调整，URL 也无需变化；C 对人更直观，但仍把语义类型写入 URL。

当前建议优先 A：

```text
/objects/<stable-id>.html
```

理由：

- stable ID 已经是 Atlas identity 核心；
- 不依赖物理目录；
- 不依赖可变化的 type 分类；
- Human / Agent 都容易构造；
- 后续可以给旧 URL 做 redirect/compatibility，而不是永久绑住旧目录。

此 URL 方案会影响公共页面地址，因此在实现前保留 Human Maintainer 决策门。

---

## 3. CI：迁移时需要同步切换，但不是结构设计问题

当前 GitHub Actions 仍监听旧的：

```text
standards/**
capabilities/**
implementations/**
organizations/**
scenarios/**
reference-projects/**
gaps/**
relations/**
maps/**
schemas/**
engine/**
```

并直接运行 `engine/...`。

当真正迁移时，应在同一个迁移 PR 中同步改为新路径，例如：

```text
01_State/**
02_Runtime/**
03_Evolution/**   # 只在确实需要触发相关检查时加入
```

以及：

```text
02_Runtime/01_Engine/...
```

这一步不需要改变三层结构本身，只需要避免迁移后 CI 不触发或找不到程序。

---

## 4. 当前迁移门状态

```text
Schema physical placement       已决定
Schema enforcement              后续独立工作
Legacy Relation cleanup         后续独立工作
Public Route decoupling         待 URL 决策
CI path migration               可在物理迁移时同步完成
Physical migration              尚未授权
```

因此下一项真正需要 Maintainer 决策的是：

> InteropAtlas 对象的稳定公共 URL 是否采用 `/objects/<stable-id>.html` 这一类与物理路径完全无关的形式。
