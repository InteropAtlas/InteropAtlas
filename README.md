# InteropAtlas

[简体中文](README.md) | [English](README.en.md)

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:49:18+08:00
Document Updated At: 2026-09-04T22:04:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

**一张关于“人类已经如何解决互操作问题”的开放知识地图。**

现实中的设备、软件、服务、组织和智能体（Agent）经常需要交换数据、能力、控制、身份、时间与语义。人类已经为这些问题创造了大量标准、协议、方法、实现和实践经验，但它们分散在不同组织、行业和技术领域中。

**InteropAtlas 把这些知识连接起来，逐步映射完整的互操作方案空间（Interoperability Solution Space）。**

如果你只是来查知识，不需要先理解这个仓库如何建设。可以把这里理解成一张仍在成长中的“互操作知识地图”。

## 这里有什么知识？

InteropAtlas 不只是标准目录。它希望把一个互操作方案从“规范是什么”一直连接到“谁在维护、怎样实现、解决什么问题、有哪些替代方案、证据在哪里、还缺什么”。

主要知识包括：

- **标准 / 规范 / 协议 / 配置规范（Profile）/ API / 格式（Format）** — 正式定义互操作方式的规范性成果（Normative Artifacts）；
- **方法 / 指南 / 框架（Framework）** — 如何设计、分析、验证、治理或维护互操作系统；
- **实现 / 工具 / 服务** — 标准和方法在现实世界中的具体实现；
- **成熟先例（Prior Art）** — 已经长期运行、值得借鉴的项目、架构和实践模式；
- **组织** — 标准组织、维护者、治理主体和相关机构；
- **能力 / 需求 / 场景** — 一个互操作问题到底需要解决什么；
- **关系** — 采用、实现、替代、依赖、兼容、扩展、演化等知识之间的连接；
- **证据 / 来源 / 来源追踪（Evidence / Source / Provenance）** — 一个事实从哪里来、依据是什么；
- **生命周期 / 事件（Lifecycle / Events）** — 发布、修订、废弃、替代和历史演化；
- **评估 / 开放缺口（Assessment / Open Gap）** — 在明确场景下的比较、覆盖情况和仍未解决的问题。

这些知识共同构成这张知识地图，而不是彼此孤立的条目。

> **映射完整方案空间，同时严格保持对象身份与权威性区别。**  
> *Map the solution space, preserve the authority distinction.*

例如，一个成熟开源项目可以是重要的成熟先例（Prior Art），但不会因此被写成“国际标准”；一个正式标准也不会因为实现较少而失去其规范身份。

更完整的收录边界见 [`项目定义与范围`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md)。

## 你可以怎样使用它？

InteropAtlas 的目标是让人（Human）与智能体（Agent）都能从同一个知识世界中：

**查找 → 浏览 → 理解 → 追踪关系 → 比较方案 → 检查证据 → 发现缺口。**

当前项目仍在建设 V1 基础设施，并不是所有知识入口和知识工作空间（Workspace）都已经完成。长期会从同一份知识底座提供不同的访问方式，例如百科式浏览（Wiki / Browse）、单对象文章（Single Object / Article）、时间线（Timeline）、关系图 / 生态图（Graph / Ecosystem）、比较（Compare）、证据 / 验证（Evidence / Verification），以及面向智能体（Agent）和 API 的结构化访问。

不同形式不是不同数据库，而是同一张知识地图面向不同认知任务的不同表达。

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

## 为什么是“互操作方案空间”？

InteropAtlas 关注的不是某一个行业，而是一个跨领域问题：**彼此独立设计的系统怎样协同工作。**

这可能发生在通信、数据表达、视频与音频、时间同步、身份、安全、发现、语义、智能体（Agent）、控制与自动化等领域。一个现实问题通常也不会只靠一份标准解决，而会同时涉及规范、实现、方法、组织、兼容关系和具体场景。

因此，InteropAtlas 的目标不是回答“有哪些标准”，而是逐步帮助回答：

> **这个互操作问题，人类已经有哪些可用方案？它们之间是什么关系？依据是什么？我应该从哪里继续探索？**

## 产品哲学

InteropAtlas 的长期设计遵循几条简单原则：

> **知识属于公共共同体。**  
> *Knowledge belongs to the commons.*
>
> **视角属于个人。**  
> *Perspective belongs to the individual.*
>
> **表达应适应认知。**  
> *Representation should adapt to cognition.*
>
> **个性化必须可逆、透明、可检查。**  
> *Personalization must remain reversible and transparent.*

以及一条贯穿知识建设和产品设计的原则：

> **采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**
>
> 优先理解和复用已有标准与成熟先例；只有真实缺口仍然存在时才自行发明。

这些原则的完整含义，以及地图优先（Atlas-first）、知识工作空间（Knowledge Workspace）、人与智能体协作（Human + Agent）、个人知识空间等长期方向，都放在 [`总体设计（Master Design）`](docs/interopatlas-master-design-v1.0.zh-CN.md) 与 [`知识哲学（Knowledge Philosophy）`](docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md) 中。普通知识使用者不需要先阅读这些文档。

## 想进一步参与？

不同目的有不同入口，不需要从头读完整个仓库：

| 你想做什么 | 从哪里开始 |
| --- | --- |
| 了解 InteropAtlas 收录什么 | [`项目定义与范围`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md) |
| 理解项目长期设计与哲学 | [`总体设计（Master Design）`](docs/interopatlas-master-design-v1.0.zh-CN.md) |
| 查看当前建设到哪里 | [`项目状态（PROJECT_STATE.md）`](PROJECT_STATE.md) |
| 作为人类维护者参与贡献 | [`贡献指南（CONTRIBUTING.md）`](CONTRIBUTING.md) |
| 让智能体接手或维护项目 | [`智能体指南（AGENTS.md）`](AGENTS.md) |
| 查找规范、配置规范（Profile）、架构和政策 | [`文档索引（docs/README.md）`](docs/README.md) |
| 查看研究、实验和变更过程 | [`演化记录（03_Evolution/）`](03_Evolution/) |

项目维护结构、P1–P6、当前 P6 施工路线、仓库结构（Repository Structure）、迁移（Migration）、收录（Intake）、治理（Governance）等内容属于第二层维护上下文，不在首页展开。

## 当前状态

InteropAtlas 仍处于早期建设阶段。当前重点是让 V1 规范知识（Canonical Knowledge）、持续收录（Intake）、人与智能体访问（Human / Agent Access）和真实数据使用形成可靠基础，而不是宣称已经覆盖完整的互操作世界。

实时项目断点与下一步工作以 [`项目状态（PROJECT_STATE.md）`](PROJECT_STATE.md) 为准。

## 许可证

- **软件代码**：Apache License 2.0
- **结构化事实数据**：CC0 1.0 Universal
- **原创文档 / 研究**：CC BY 4.0

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准文本、商标、标志（Logo）和其他材料仍受各自权利与许可证约束。
