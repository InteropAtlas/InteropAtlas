# InteropAtlas

[简体中文](README.md) | [English](README.en.md)

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Updated At: 2026-09-24T23:59:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human Owner — ff6962757
  GitHub Actor: ff6962757
-->

**一张关于“人类已经如何解决互操作问题”的开放知识地图。**

现实中的设备、软件、服务、组织和智能体（Agent）经常需要交换数据、能力、控制、身份、时间与语义。人类已经为这些问题创造了大量标准、协议、方法、实现和实践经验，但它们分散在不同组织、行业和技术领域中。

**InteropAtlas 把这些知识连接起来，逐步映射完整的互操作方案空间（Interoperability Solution Space）。**

## 三句话认识 InteropAtlas

### 我们做什么
**研究互操作，并映射人类已经形成的互操作方案空间。**

### 我们怎么做
**持续连接、整理和验证分散在不同领域中的互操作知识，并在 IA 自身上实践互操作。**

标准、协议、方法、实现、案例、关系与证据会被连接到同一张知识地图中；同时，IA 自身也可以用于探索不同视图、表达形式、Human / Agent 接口和机器可读形式之间的转换与协同。

### 这些成果最后去哪
**形成开放、机器可读、持续演化的互操作公共知识基础设施。**

让这些知识能够被 Human 与 Agent 获取、验证、复用、组合和继续扩展。

如果你只是来查知识，不需要先理解这个仓库如何建设。可以把这里理解成一张仍在成长中的“互操作知识地图”。

## 与上层组织的关系

InteropAtlas 是上层组织中的一个具体项目，负责探索 **interoperability / 互操作** 这一问题空间。

它的项目边界不是整个组织的边界：上层组织关注“组织还可以是什么”，而 IA 关注彼此独立的主体、系统与知识表达如何实现互通、对齐与协同。

IA 的研究也会反过来支持组织本身：帮助不同主体更好地连接、理解、协作，并为 Human / Agent、多视图与机器可读表达之间的转换提供基础。

关于 IA 对整个组织意味着什么、以及它与其他未来项目的关系，以 Organization 仓库中的组织级定义为准。

## 什么叫“互操作”？

InteropAtlas 当前用三个**并列、非互斥**的问题维度来理解互操作：

- **互通（Exchange）**：能否建立可用通路并交换信息、请求、能力或控制——**连得上**。
- **对齐（Alignment）**：能否对结构、语义、身份、能力、状态与上下文形成足够一致的解释——**对得上**。
- **协同（Coordination）**：能否在目标、权限、规则、流程与责任约束下组织行动并完成跨边界任务——**办得成**。

这不是新的国际标准分类，也不是严格顺序或协议栈；它是 IA 为跨领域组织互操作问题采用的工作模型。它参考了既有互操作框架中对 technical / syntactic / semantic / organisational / legal / pragmatic 等问题的分层研究。[^interop-model] 更严格的定义、边界与映射见 [`项目定义与范围`](docs/01_Foundation/01_Definition/interopatlas-definition-and-scope.zh-CN.md)。

[^interop-model]: 主要参考：[Interoperable Europe Act / European Interoperability Framework](https://interoperable-europe.ec.europa.eu/Interoperable-Europe-Act-Regulation)；Tolk, Diallo & Turnitsa, [*Applying the Levels of Conceptual Interoperability Model…*](https://digitalcommons.odu.edu/msve_fac_pubs/27/) (2007，LCIM 源于 Tolk & Muguira 2003)。IA 的“互通 / 对齐 / 协同”是对这些既有框架的问题导向综合，不宣称与其分类一一等价。

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

项目当前沿三条方向持续建设：**知识积累、知识视角与访问建设、系统运维与自我进化**。适人化呈现与机器可读访问都建立在同一个 Canonical knowledge world 上；不同呈现与调用方式不是不同数据库，而是同一知识底座的不同访问方式。

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

## 为什么是“互操作方案空间”？

InteropAtlas 关注的不是某一个行业，而是一个跨领域问题：**彼此独立设计的系统怎样协同工作。**

一个现实问题通常不会只靠一份标准解决，而会同时涉及规范、实现、方法、组织、兼容关系和具体场景。因此项目逐步帮助回答：

> **这个互操作问题，人类已经有哪些可用方案？它们之间是什么关系？依据是什么？我应该从哪里继续探索？**

## 建设原则

InteropAtlas 优先把可验证、可追溯、可复用的互操作知识沉淀为公共知识基础设施。个性化透明 / 可控 / 可逆、地图优先（Atlas-first）、先有证据再有断言（Evidence before assertion）、先选择再呈现（Selection before presentation）、真实使用塑造本体模型（Real use shapes the ontology）、**采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**等属于产品与建设原则。

“知识属于公共共同体，视角属于个人”等知识态度不再作为 IA 的核心项目定义；相关讨论可以继续保留在深入文档中，但 README 优先回答 IA 做什么、怎么做、成果最终形成什么。

完整结构见 [`知识哲学与原则`](docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md)；长期架构见 [`总体设计（Master Design）`](docs/01_Foundation/01_Definition/interopatlas-master-design.zh-CN.md)。

## 想参与建设？

**只需要进入 [`PROJECT_STATE.md`](PROJECT_STATE.md)。**

它是 Human 与 Agent 共用的当前建设入口，直接回答三个问题：

1. 我们要去哪里；
2. 我们现在在建设什么；
3. 我可以从哪里参与。

从那里可以继续进入当前 Focus、Inbox、PR、Project、Candidate Pool、Human / Machine 路线或深入文档。Issue 只承载可继续推进的具体任务；研究可以发生在任何任务中，不再单独把 Research 当作一种 Issue 类型。你不需要为了参与项目先通读 Master Design、Roadmap、全部 `docs/` 或完整 Issue backlog。

如果你是 Agent，仓库级执行约束另见 [`AGENTS.md`](AGENTS.md)；具体贡献规则见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 当前状态

InteropAtlas 仍处于早期建设阶段，但已经从纯设计转向真实运行：**知识积累、知识视角与访问建设、系统运维与自我进化**正在并行推进。

**实时方向、参与路径与下一步入口统一从 [`PROJECT_STATE.md`](PROJECT_STATE.md) 进入。**

## 许可证

- **软件代码**：Apache License 2.0
- **结构化事实数据**：CC0 1.0 Universal
- **原创文档 / 研究**：CC BY 4.0

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准文本、商标、标志（Logo）和其他材料仍受各自权利与许可证约束。