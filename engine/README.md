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
