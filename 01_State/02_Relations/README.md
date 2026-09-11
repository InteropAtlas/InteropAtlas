# 02_Relations

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T14:44:37+08:00
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

这里存放 InteropAtlas 当前正式记录的**关系**。

关系连接对象并描述它们之间的语义联系。关系本身也可以携带属性，因此不单独建立 `Properties/` 目录。

关系的数据规则也与关系放在一起：

- `README.md`：给 Human / Agent 阅读的数据格式说明；
- `*.schema.json`：需要机器执行的数据验证合同；
- `*.yaml` / `*.yml`：正式关系数据。

因此不再建立独立的 `Schemas/` 二级目录。

关系的身份由文件内容决定，而不是由它位于本目录这一事实决定；本目录只是当前选定的物理存储边界。
