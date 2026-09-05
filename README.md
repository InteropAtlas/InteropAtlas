# InteropAtlas

[简体中文](README.md) | [English](README.en.md)

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-05T19:00:00+08:00
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

主要知识包括标准 / 规范 / 协议 / Profile / API / Format，方法 / 指南 / Framework，实现 / 工具 / 服务，成熟先例（Prior Art），组织，能力 / 需求 / 场景，关系，证据 / 来源 / Provenance，生命周期 / 事件，以及评估 / Open Gap。

这些知识共同构成这张知识地图，而不是彼此孤立的条目。

> **映射完整方案空间，同时严格保持对象身份与权威性区别。**  
> *Map the solution space, preserve the authority distinction.*

例如，一个成熟开源项目可以是重要的成熟先例，但不会因此被写成“国际标准”；一个正式标准也不会因为实现较少而失去其规范身份。

更完整的收录边界见 [`项目定义与范围`](docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)。

## 你可以怎样使用它？

InteropAtlas 的目标是让人（Human）与智能体（Agent）都能从同一个知识世界中：

**查找 → 浏览 → 理解 → 追踪关系 → 比较方案 → 检查证据 → 发现缺口。**

项目正在把 Canonical Knowledge、持续收录（Intake）、Human / Agent Access 与真实数据使用变成可靠的长期运行能力。不同形式不是不同数据库，而是同一张知识地图面向不同认知任务的不同表达。

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

## 为什么是“互操作方案空间”？

InteropAtlas 关注的不是某一个行业，而是一个跨领域问题：**彼此独立设计的系统怎样协同工作。**

一个现实问题通常不会只靠一份标准解决，而会同时涉及规范、实现、方法、组织、兼容关系和具体场景。因此项目逐步帮助回答：

> **这个互操作问题，人类已经有哪些可用方案？它们之间是什么关系？依据是什么？我应该从哪里继续探索？**

## 产品哲学

> **知识属于公共共同体。视角属于个人。**  
> *Knowledge belongs to the commons. Perspective belongs to the individual.*
>
> **知识流动，创造不息。**  
> *Knowledge travels. Creation continues.*

公共知识跨越边界进入个人视角与具体情境，推动新的创造；新的创造又可以进入公共共同体，成为下一轮流动的基础。

> **保存知识不是终点。知识最终应该帮助新的创造发生。**  
> *Preservation is not the endpoint; knowledge should ultimately enable new creation.*

个性化透明 / 可控 / 可逆、地图优先（Atlas-first）、先有证据再有断言（Evidence before assertion）、先选择再呈现（Selection before presentation）、真实使用塑造本体模型（Real use shapes the ontology）、**采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**等属于产品与建设原则。

完整结构见 [`知识哲学与原则`](docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md)；长期架构见 [`总体设计（Master Design）`](docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)。

## 想参与建设？

**只需要进入 [`PROJECT_STATE.md`](PROJECT_STATE.md)。**

它是 Human 与 Agent 共用的当前建设入口，直接回答三个问题：

1. 我们要去哪里；
2. 我们现在在建设什么；
3. 我可以从哪里参与。

从那里可以继续进入当前适用的 Discussion、Issue、Project、Candidate Pool、Human / Machine 路线或深入文档。你不需要为了参与项目先通读 Master Design、Roadmap、全部 `docs/` 或完整 Issue backlog。

如果你是 Agent，仓库级执行约束另见 [`AGENTS.md`](AGENTS.md)；具体贡献规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 当前状态

InteropAtlas 仍处于早期建设阶段，但已经从纯设计转向真实运行：知识地图持续成长、可运行知识基础设施、Human / Agent 真实使用与反馈正在并行演化。

**实时方向、参与路径与下一步入口统一从 [`PROJECT_STATE.md`](PROJECT_STATE.md) 进入。**

## 许可证

- **软件代码**：Apache License 2.0
- **结构化事实数据**：CC0 1.0 Universal
- **原创文档 / 研究**：CC BY 4.0

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准文本、商标、标志（Logo）和其他材料仍受各自权利与许可证约束。
