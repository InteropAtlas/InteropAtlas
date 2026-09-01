# InteropAtlas Engine — Bootstrap Harness

这里是 InteropAtlas 当前的最小可执行 Engine，负责确定性读取、索引、查询、图构建、验证辅助与人类可读视图生成。

## 当前 Canonical Storage

Engine 默认读取两个物理位置：

```text
01_State/01_Objects/
01_State/02_Relations/
```

这两个目录只是当前的物理存储边界，不承担 ontology 分类。Standard、Capability、Organization、Implementation、Reference Project、Map 等对象身份继续由 YAML 内容决定；Relation 也由文档内容识别，而不是因为文件位于某个目录。

### Relation 兼容

目标形式使用：

```yaml
type: relation
```

部分历史 Relation 仍缺少显式 `type`。Loader 暂时兼容具有：

```text
source + relation/predicate/kind + target
```

的历史结构。该兼容规则仍然只看内容，不看文件夹。

## Logical source 与 physical source

Loader 区分：

- `_source`：由稳定 `id` 生成的逻辑/公开路径来源；
- `_physical_source`：真实 repository-relative 文件位置，用于读取、追踪与迁移诊断。

Object 的公开逻辑路径：

```text
objects/<stable-id>.yaml
→ /objects/<stable-id>.html
```

因此移动或重命名 State 中的 YAML，不会改变公开页面地址，只要对象 `id` 不变。

## 运行

从仓库根目录执行：

```bash
python 02_Runtime/01_Engine/graph_index.py --root .
python 02_Runtime/01_Engine/bootstrap_query.py --root . --capability automated_build_deployment
python 02_Runtime/01_Engine/render_site.py --root . --output build/site
```

需要测试其他存储位置时，CLI 仍可重复传入 `--storage-path`。

## 当前边界

- Schema 已与 State 数据共置，但尚未启用全量 Schema enforcement；
- legacy Relation cleanup 是独立工作，不与目录迁移绑定；
- Engine 不把目录名解释成对象语义；
- GitHub Actions 与 Pages 使用 `02_Runtime/01_Engine/` 作为当前执行路径。
