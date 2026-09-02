# Engine v0.1 第一轮覆盖基线

<!-- InteropAtlas Document Metadata v0
Document Status: 初步基线，不作为最终统计
Document Created At: 2026-08-31T13:34:21+08:00
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

状态：初步基线，不作为最终统计

## 统计目的

这份基线用于回答：在开始 Engine v0.1 自举实践时，InteropAtlas 对真实建设所需标准知识已经覆盖到什么程度？

它不是为了追求高覆盖率，而是为了记录实践开始时的真实状态，方便后续比较 Atlas 是否通过实践成长。

## 第一轮候选集合

按当前计划，已经确认或高度相关的标准/规范包括：

### 实践开始前已收录

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

### 本轮实践直接暴露并新增

- JSON Pointer / RFC 6901
- RFC 3339 Internet Timestamps
- CommonMark 0.31.2
- GitHub Flavored Markdown 0.29
- SPDX License Expressions 3.0.1
- WHATWG URL Living Standard
- CSS Snapshot 2025
- SVG 2

### 仍待决定是否实际进入 v0.1 技术栈或 Atlas

- ECMAScript / ECMA-262
- ISO 8601 本体（RFC 3339 已作为互联网时间戳配置文件收录）
- Semantic Versioning
- Mermaid
- GitHub Actions
- GitHub Pages
- GitHub Issues / Pull Requests 的平台工作流模型
- 更开放的 CI/CD 与代码托管替代方案

## 为什么暂时不报一个简单百分比

如果直接用“已收录名称数 / 候选名称数”，会产生虚假的精确度：

1. 有些标准只是架构参考，并不是 Engine 实现依赖；
2. 有些对象是标准，有些是平台、实现或工具；
3. 一个标准被收录不代表 Capability、Relation、Evidence 和解释已经完整；
4. “覆盖”至少应区分存在、关系完整、解释完整、可用于选型等层次。

因此下一步应把 Coverage Assessment 拆成至少几个层级：

- Object Coverage：对象是否存在；
- Relation Coverage：关键关系是否存在；
- Explanation Coverage：是否达到人类可理解程度；
- Decision Coverage：是否足以支持真实选型；
- Practice Coverage：是否已经有实践反馈。

## 第一轮反馈

本次自举在尚未编写 Engine 代码之前，就已经发现了多个明显缺项，说明“Practice → Atlas”反馈环已经开始产生价值。

同时，现有仓库已经能够直接提供 YAML、JSON、JSON Schema、HTTP、URI、Git、Unicode、BCP 47、HTML 等基础知识对象，说明早期积累并非无效。

后续每完成一个 Engine 小步骤，应继续更新覆盖情况，而不是只在项目结束时做一次总结。