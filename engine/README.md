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

## Repository Data Root Contract

`engine/repository_layout.py` 是当前 Engine 对 Canonical Data 物理位置的集中合同。

当前状态：

```text
repository root
├── standards/
├── capabilities/
├── scenarios/
├── organizations/
├── implementations/
├── reference-projects/
├── gaps/
├── relations/
└── maps/
```

因此当前 `DEFAULT_DATA_ROOT = .`。

未来若批准迁移，可测试：

```text
repository root
└── data/
    ├── standards/
    ├── capabilities/
    └── ...
```

而不需要让每个 Engine 模块重新维护一份 object-family 路径列表。

### 两种 source path

Loader 为对象增加内部运行时元数据：

- `_source`：逻辑 source path，例如 `standards/yaml_1.2.2.yaml`；生成视图使用这一稳定路径；
- `_physical_source`：真实 repository-relative 位置；当前与 `_source` 相同，未来迁移后可能是 `data/standards/yaml_1.2.2.yaml`；
- `_object_family`：逻辑 object family。

这样做是为了满足 Repository Structure Profile 的迁移不变量：**物理位置变化不应自动改变公开生成 URL。**

### 可显式测试候选 Data Root

Bootstrap / Graph diagnostics 支持 repository-relative `--data-root`：

```bash
python engine/graph_index.py --data-root .
python engine/bootstrap_query.py --data-root . --capability automated_build_deployment
```

未来 Migration Dry Run 可以在候选 `data/` 布局准备好后使用 `--data-root data` 验证，而不先修改默认合同。

### 当前边界

本合同只集中 **Engine runtime 的 Canonical Data path knowledge**。

GitHub Actions 的 `paths:` trigger 仍需要声明物理 repository paths；当前两个 workflows 仍列出 root object-family paths。这是已知 residual coupling，真正目录迁移前必须单独更新和验证，不能因为 Engine 已解耦就认为 CI 已迁移。
