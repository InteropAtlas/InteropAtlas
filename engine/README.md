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

### Source path

Loader 当前保留：

- `_source`：为了保持现有 Renderer / public generated path 行为，当前仍等于 repository-relative physical path；
- `_physical_source`：实际 repository-relative physical path，用于追踪和迁移诊断。

#31 修正删除了 `_object_family`，因为从目录名推断 semantic family 会重新把 ontology 绑回文件系统。

真正执行未来目录迁移之前，必须另外确定 public view / URL 如何与物理 storage path 解耦。**本次修正没有假装这个问题已经解决。**

### 可显式测试其他物理存储位置

CLI 使用可重复的 `--storage-path`：

```bash
python engine/graph_index.py --storage-path standards --storage-path relations
python engine/bootstrap_query.py --storage-path standards --storage-path implementations --capability automated_build_deployment
```

如果不传，使用当前 9 个 legacy storage locations。

将来讨论出新的物理布局后，可以把候选位置传给同一 Loader 做 Migration Dry Run，不需要让目录名承担知识分类语义。

## 当前边界

- 本合同没有决定未来根目录一级目录叫什么；
- 没有决定 Canonical Data 内部应该平铺、分片还是采用其他物理布局；
- GitHub Actions `paths:` 仍然监听当前真实路径，正式迁移时必须一起调整；
- #15 Non-normative Knowledge Object Model 负责对象 `type / kind / roles / relations`，**不负责决定文件夹名字，也不再阻塞物理目录结构讨论。**
