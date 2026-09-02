# 01_State

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T14:31:59+08:00
Document Updated At: 2026-09-01T15:23:52+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

`01_State` 是 InteropAtlas 三个核心一级目录之一。

它表示 InteropAtlas **当前时刻正式承认的静态图状态**。

当前二级结构：

```text
01_State/
├── 01_Objects/
├── 02_Relations/
└── README.md
```

- `01_Objects/`：存放正式收录的对象；对象类型通过数据字段表达，不通过文件夹分类。
- `02_Relations/`：存放对象之间正式记录的关系。
- Properties 不单独建目录，而是作为 Object 或 Relation 自身的数据字段存在。
- Schema 不单独建 `Schemas/` 目录，而是与其约束的数据放在一起：Object Schema 放入 `01_Objects/`，Relation Schema 放入 `02_Relations/`。

同一个目录内，README 负责给 Human / Agent 解释数据规则，机器可读 Schema 负责自动验证，YAML/YML 文件承载正式数据。

原则：这里的内容可以变化，但任一时刻都应代表项目当前有效状态，而不是临时研究、实验过程或生成产物。
