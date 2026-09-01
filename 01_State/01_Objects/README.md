# 01_Objects

这里存放 InteropAtlas 当前正式收录的**对象**。

对象类型不通过文件夹区分。Standard、Organization、Capability、Implementation、Method、Design System、Gap 等可以平级存放；对象是什么，由文件自身的数据字段决定。

属性直接属于对象本身，不单独建立 `Properties/` 目录。

对象的数据规则也与对象放在一起：

- `README.md`：给 Human / Agent 阅读的数据格式说明；
- `*.schema.json`：需要机器执行的数据验证合同；
- `*.yaml` / `*.yml`：正式对象数据。

因此不再建立独立的 `Schemas/` 二级目录。现有历史 Schema 在真正迁移前仍需逐项判断哪些属于 Object、哪些需要重构或合并。
