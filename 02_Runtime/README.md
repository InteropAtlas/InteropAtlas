# 02_Runtime

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-09-01T14:31:59+08:00
Document Updated At: 2026-09-01T14:47:53+08:00
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

`02_Runtime` 是 InteropAtlas 三个核心一级目录之一。

它承载让项目**运行、处理、验证、转换、生成和导出**的内容。

当前二级结构：

```text
02_Runtime/
├── 01_Engine/
├── 02_Tools/
├── 03_Outputs/
└── README.md
```

- `01_Engine/`：核心运行代码；
- `02_Tools/`：Human / Agent / CI 使用的辅助维护与操作工具；
- `03_Outputs/`：由 Runtime 生成的网站、导出、索引和其他产物。

原则：Source 与 Generated Artifact 必须保持边界。哪些 Outputs 需要提交进 Git、哪些只在 CI / 部署中生成，后续单独确定。
