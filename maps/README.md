# Maps

`maps/` 保存 InteropAtlas 的 Map（地图/视图）定义。

Map 不是第二份事实库，也不是固定分类树。它只声明：

- 从哪些对象作为入口；
- 沿哪些 Relation（关系）展开；
- 允许包含哪些对象类型；
- 哪些对象需要固定显示；
- 如何把结果分组展示。

底层事实仍然来自 `standards/`、`capabilities/`、`organizations/`、`reference-projects/`、`relations/` 等目录。

未来 Engine 可以根据 Map 定义生成 Graph View（图视图）、List View（列表视图）、Table View（表格视图）或 API 结果。

当前采用原则：

> Flat Objects（扁平对象） + Rich Relations（丰富关系） + Dynamic Maps（动态地图）

Map 定义的 Schema：`schemas/map.schema.json`。
