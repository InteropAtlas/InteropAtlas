# 01_State

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T14:31:59+08:00
Document Updated At: 2026-09-05T15:25:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human Owner — ff6962757
  GitHub Actor: ff6962757
-->

`01_State` 是 InteropAtlas 三个核心一级目录之一。

它的**编号入口只表示当前正式承认的 Canonical State**；尚未正式收入的候选内容和 intake 审核过程不占编号注意力入口。

当前结构：

```text
01_State/
├── 01_Objects/              正式收录的对象
├── 02_Relations/            正式记录的关系
├── inbox/                   未正式进入 Canonical 的 intake 工作区（不编号）
│   ├── candidates/          候选对象
│   └── acceptance-events/   候选审核 / 接受决策的审计记录与合同
└── README.md
```

- `01_Objects/`：存放正式收录的对象；对象类型通过数据字段表达，不通过文件夹分类。
- `02_Relations/`：存放对象之间正式记录的关系。
- `inbox/`：辅助入口，不是第三个 Canonical 类别；其中内容尚未成为正式 State，或属于进入正式 State 的审核 / 决策过程。
- `inbox/candidates/`：Candidate Pool（候选池），用于等待验证、研究、判重、审核与接纳的对象。
- `inbox/acceptance-events/`：记录候选经过审核后被接受、判重、延期、要求身份审查等决定的结构化证据；它不是第二套 Canonical 对象库。
- Properties 不单独建目录，而是作为 Object 或 Relation 自身的数据字段存在。
- Schema 不单独建通用 `Schemas/` 目录；与正式 Object / Relation 直接对应的 Schema 与数据放在一起，intake 专用合同则跟随 `inbox/` 对应流程。

同一个目录内，README 负责给 Human / Agent 解释数据规则，机器可读 Schema 负责自动验证，YAML/YML 文件承载结构化数据。

原则：编号表示主要注意力入口。`01_State` 当前只有两个编号入口：Objects 与 Relations；`inbox/` 是未正式进入 Canonical 的辅助工作区，不占编号位置。