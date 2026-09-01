# InteropAtlas Engine — Bootstrap Harness

这是 InteropAtlas Engine 的**临时最小可执行实验区**。

当前目标不是确定 Engine 最终仓库结构，而是尽快把人工走查升级为可重复执行的机器实验。

当 Engine 独立仓库建立后，这里的代码可以迁移过去。

## v0.0.1 目标

1. Loader：读取 Atlas 的 YAML 对象；
2. Index：按 `id` 建立对象索引；
3. Query：按 Capability 查找 Implementation；
4. Filter：筛选 `open_source` / `self_hostable`；
5. Relation lookup：查找 `alternative_to`；
6. 输出机器可重复的实验结果。

原则：Engine 只做确定性读取、查询与计算，不把 Atlas 变成推理模型。

## Canonical Storage Contract

`engine/repository_layout.py` 只负责一个问题：

> **Canonical YAML 现在物理存在哪里？**

它不负责回答：

> **这个对象在知识模型里属于什么类别？**

当前仓库历史上把 Canonical YAML 分散在：

```text
standards/
capabilities/
scenarios/
organizations/
implementations/
reference-projects/
gaps/
relations/
maps/
```

这些名称在 Engine 中被记录为 `CURRENT_CANONICAL_STORAGE_PATHS`，意思只是“当前需要扫描的物理位置”。

**它们不是未来必须保留的 object-family 目录，也不是 ontology。**

未来完全可以出现这样的物理结构：

```text
<某个尚未决定的 canonical storage zone>/
  a.yaml
  b.yaml
  nested/c.yaml
```

Standard、Method、Design System、Capability、Relation 等语义身份由 YAML 内容、Schema、引用和 Graph 决定，而不是由文件夹决定。

### Loader 如何判断对象身份

目标模型中 Relation 应显式写：

```yaml
type: relation
```

但当前数据里仍有少量历史 Relation 没有这个字段。为保持兼容，Loader 也会根据文档自身是否具有：

```text
source + relation/predicate/kind + target
```

来识别这类旧 Relation。

关键点是：**这两种判断都来自文件内容，不来自 `relations/` 这个目录名。**

所以同一个物理目录里可以混合不同 `type` 的对象，回归测试会验证这一点。后续应把旧 Relation 独立清理为显式 `type: relation`，但不在本次目录原则修正里顺便修改 Canonical Data。

### Logical source 与 physical source

Loader 现在明确区分两个概念：

- `_source`：稳定的逻辑 / 公开路径来源，由文档稳定 `id` 生成；
- `_physical_source`：真实 repository-relative 文件路径，仅用于读取、追踪和迁移诊断。

Object 的逻辑路径统一为：

```text
objects/<stable-id>.yaml
```

Renderer 继续从 `_source` 派生 Markdown / HTML，因此公开对象页面稳定为：

```text
/objects/<stable-id>.html
```

例如：

```text
objects/sample_standard.yaml
→ objects/sample_standard.md
→ /objects/sample_standard.html
```

即使同一个源文件从：

```text
standards/sample.yaml
```

移动到：

```text
01_State/01_Objects/renamed.yaml
```

只要 `id: sample_standard` 不变，公开页面地址也不变。

Relation 当前同样得到稳定逻辑路径：

```text
relations/<stable-id>.yaml
```

但目前 Renderer 尚不生成 Relation 独立页面。

#31 修正删除了 `_object_family`，因为从目录名推断 semantic family 会重新把 ontology 绑回文件系统。现在公开页面路径也已经与物理 storage path 解耦。

### 可显式测试其他物理存储位置

CLI 使用可重复的 `--storage-path`：

```bash
python engine/graph_index.py --storage-path standards --storage-path relations
python engine/bootstrap_query.py --storage-path standards --storage-path implementations --capability automated_build_deployment
```

如果不传，使用当前 9 个 legacy storage locations。

将来迁入新的物理布局后，可以把候选位置传给同一 Loader 做 Migration Dry Run，不需要让目录名承担知识分类语义，也不会改变对象公开 URL。

## 当前边界

- Canonical Data 尚未发生物理迁移；
- GitHub Actions `paths:` 仍然监听当前真实路径，正式迁移时必须一起调整；
- Schema 目标位置已经确定，但 Schema enforcement 与 legacy data cleanup 仍是独立工作；
- #15 Non-normative Knowledge Object Model 负责对象 `type / kind / roles / relations`，**不负责决定文件夹名字，也不再阻塞物理目录结构讨论。**
