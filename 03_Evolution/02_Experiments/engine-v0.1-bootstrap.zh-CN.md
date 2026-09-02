# Engine v0.1 自举实践实验

<!-- InteropAtlas Document Metadata v0
Document Status: 进行中
Document Created At: 2026-08-31T13:32:38+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

状态：进行中

关联：#2、#1

## 实验问题

在真正开始开发 InteropAtlas Engine v0.1 之前，从它的实际建设流程反推：

1. 我们需要哪些互操作能力？
2. 这些能力涉及哪些标准、规范、协议、开放方法和实现？
3. 当前 InteropAtlas 已经覆盖多少？
4. 哪些对象、关系和解释缺失？
5. Atlas 能否在真实工程中有效帮助技术发现与选型？

## 初始流程分解

### A. 数据源与读取

需求：人类可编辑、Git 友好、机器可解析的事实源。

当前候选：
- YAML 1.2.2
- Unicode
- URI
- Git

### B. 数据结构验证

需求：检查对象结构、字段、类型和约束。

当前候选：
- JSON
- JSON Schema 2020-12
- JSON Pointer（待核实/待收录）
- JSON Schema URI / Reference 相关规范（待进一步拆解）

### C. 对象引用与关系图

需求：稳定 ID、对象引用、Relation、Backlinks、图结构。

当前候选：
- URI
- RDF 1.2 Concepts（语义兼容/外部图模型）
- JSON-LD 1.1（交换格式候选）
- SKOS（部分知识组织语义）
- Topic Maps（关系 Scope / Association 等参考）

说明：这些标准不等于 Engine v0.1 必须直接采用；需要区分“实现依赖”和“架构/互操作参考”。

### D. 人类可读页面

需求：中文优先、超链接、可导航的静态阅读层。

当前候选：
- HTML Living Standard
- Unicode
- BCP 47
- URI / URL
- CSS（待核实/待收录）
- ECMAScript（如第一版需要客户端交互，则待核实/待收录）

### E. 文档与解释内容

需求：项目文档、标准解释、可读文本的统一表达。

当前候选：
- CommonMark（待收录）
- GitHub Flavored Markdown / GFM（待核实是否作为平台相关规范收录）
- HTML
- BCP 47

### F. 基础关系图呈现

需求：把对象和 Relation 生成人类可查看的图。

候选待实验：
- SVG（开放 Web 图形标准，待收录）
- Mermaid（开源工具/语法，不应直接等同开放标准，待评估）
- HTML/CSS/JavaScript 图形实现

### G. 版本控制与协作

需求：事实数据、Engine 代码、变更历史、协作。

当前候选：
- Git
- Git protocol v2
- GitHub（平台/实现，不是开放标准）
- Pull Request / Issue（GitHub 平台工作流，需与开放标准区分）

### H. 自动构建与部署

需求：数据变化后自动运行 Engine、生成并部署静态站点。

候选：
- GitHub Actions（专有平台服务/公开工作流格式，不视作独立开放标准）
- GitHub Pages（平台服务）
- HTTP
- HTML
- URI / URL

后续应研究是否存在更开放、可迁移的 CI/CD 和静态托管接口/替代实现，并记录平台依赖。

### I. 元数据

需求：标准化表达时间、版本、许可证、语言、资源标识等。

当前候选：
- BCP 47：语言
- URI：资源标识
- ISO 8601 / RFC 3339：日期时间（待收录）
- SPDX License Identifier / License Expression：许可证表达（待收录）
- Semantic Versioning：Engine 自身版本策略候选（待评估其对象类型和收录价值）

## 第一轮已知覆盖

当前仓库已经具备明显相关的：

- YAML 1.2.2
- JSON RFC 8259
- JSON Schema 2020-12
- HTTP RFC 9110
- URI RFC 3986
- Git protocol v2
- Unicode 17
- BCP 47 / RFC 5646
- HTML Living Standard
- JSON-LD 1.1
- RDF 1.2 Concepts
- RDF 1.2 Turtle
- SKOS
- ISO Topic Maps

第一轮明显缺失/待调查的至少包括：

- CommonMark
- GitHub Flavored Markdown
- JSON Pointer RFC 6901
- RFC 3339 / ISO 8601
- SPDX License Expression / Identifier
- CSS
- SVG
- ECMAScript（是否实际需要取决于 v0.1 交互设计）
- URL Living Standard 与 URI RFC 3986 的边界
- GitHub Actions / Pages / Issues / Pull Requests 等平台对象应该如何建模
- CI/CD 的开放替代与可迁移性

## 初始观察

现有 Atlas 对“数据表示、Web 基础、链接数据”已有一定覆盖，但对一个完整的软件建设/发布流程的覆盖明显不足，尤其是：

- 文档表示；
- 时间与版本元数据；
- 许可证机器表达；
- Web 展示层；
- 构建与部署；
- 平台工作流；
- 实现/产品与开放标准之间的建模。

这已经产生了第一批实践反馈，说明自举机制能够有效暴露 Atlas 的覆盖边界。

## 下一步

1. 对上述待调查项逐一核实官方来源、类型、治理、开放性和关系；
2. 计算更严格的第一轮覆盖评估，避免简单按“名称数量”计算；
3. 收录确定的重要缺项；
4. 建立 Engine v0.1 Scenario / Capability / Relation；
5. 再进入 Engine 实现；
6. 实现过程中持续更新本实验记录。