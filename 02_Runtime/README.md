# 02_Runtime

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
