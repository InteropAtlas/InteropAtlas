# InteropAtlas

<!-- InteropAtlas Document Metadata v0
Document Status: active
Document Created At: 2026-08-30T17:49:18+08:00
Document Updated At: 2026-09-04T21:45:00+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

**An open knowledge atlas of how humanity has already solved interoperability problems.**  
**一张关于“人类已经如何解决互操作问题”的开放知识地图。**

Devices, software, services, organizations, and Agents constantly need to exchange data, capabilities, control, identity, time, and semantics. Humanity has already created a vast body of standards, protocols, methods, implementations, and practical experience for these problems, but that knowledge is scattered across organizations, industries, and technical domains.

现实中的设备、软件、服务、组织和 Agent 经常需要交换数据、能力、控制、身份、时间与语义。人类已经为这些问题创造了大量标准、协议、方法、实现和实践经验，但它们分散在不同组织、行业和技术领域中。

**InteropAtlas connects this knowledge and progressively maps the complete Interoperability Solution Space.**  
**InteropAtlas 把这些知识连接起来，逐步映射完整的互操作方案空间（Interoperability Solution Space）。**

If you are here simply to find knowledge, you do not need to understand how the repository itself is built. Think of it as a growing atlas of interoperability knowledge.

如果你只是来查知识，不需要先理解这个仓库如何建设。可以把这里理解成一个仍在成长中的“互操作知识 Atlas”。

## What knowledge is here? / 这里有什么知识？

InteropAtlas is not merely a standards directory. It aims to connect an interoperability solution from “what is the specification?” all the way to “who maintains it, how is it implemented, what problem does it solve, what alternatives exist, where is the evidence, and what is still missing?”

InteropAtlas 不只是标准目录。它希望把一个互操作方案从“规范是什么”一直连接到“谁在维护、怎样实现、解决什么问题、有哪些替代方案、证据在哪里、还缺什么”。

Core knowledge includes / 主要知识包括：

- **Standards / Specifications / Protocols / Profiles / APIs / Formats — 标准 / 规范 / 协议 / Profile / API / Format** — normative artifacts that formally define ways to interoperate / 正式定义互操作方式的规范性成果；
- **Methods / Guidelines / Frameworks — 方法 / 指南 / Framework** — ways to design, analyze, validate, govern, or maintain interoperable systems / 如何设计、分析、验证、治理或维护互操作系统；
- **Implementations / Tools / Services — 实现 / 工具 / 服务** — concrete real-world implementations of standards and methods / 标准和方法在现实世界中的具体实现；
- **Prior Art — 既有先例** — long-running projects, architectures, and practices worth learning from / 已经长期运行、值得借鉴的项目、架构和实践模式；
- **Organizations — 组织** — standards bodies, maintainers, governance actors, and related institutions / 标准组织、维护者、治理主体和相关机构；
- **Capabilities / Needs / Scenarios — 能力 / 需求 / 场景** — what an interoperability problem actually needs to solve / 一个互操作问题到底需要解决什么；
- **Relations — 关系** — adoption, implementation, alternatives, dependencies, compatibility, extensions, evolution, and other connections / 采用、实现、替代、依赖、兼容、扩展、演化等知识之间的连接；
- **Evidence / Source / Provenance — 证据 / 来源 / 来源追踪** — where a fact comes from and what supports it / 一个事实从哪里来、依据是什么；
- **Lifecycle / Events — 生命周期 / 事件** — publication, revision, deprecation, replacement, and historical evolution / 发布、修订、废弃、替代和历史演化；
- **Assessment / Open Gap — 评估 / 开放缺口** — comparison, coverage, and unresolved problems in explicit contexts / 在明确场景下的比较、覆盖情况和仍未解决的问题。

Together, these form the Atlas rather than a collection of isolated entries.

这些知识共同构成 Atlas，而不是彼此孤立的条目。

> **Map the solution space, preserve the authority distinction.**  
> **映射完整方案空间，同时严格保持对象身份与权威性区别。**

For example, a mature open-source project can be important Prior Art without being misrepresented as an “international standard”; a formal standard does not lose its normative identity merely because it has few implementations.

例如，一个成熟开源项目可以是重要的既有先例（Prior Art），但不会因此被写成“国际标准”；一个正式标准也不会因为实现较少而失去其规范身份。

For the full inclusion boundary, see [`Definition & Scope / 项目定义与范围`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md).

## How can you use it? / 你可以怎样使用它？

InteropAtlas aims to let both Humans and Agents operate over the same knowledge world to:

InteropAtlas 的目标是让 Human 与 Agent 都能从同一个知识世界中：

**Find → Browse → Understand → Trace relations → Compare solutions → Inspect evidence → Discover gaps.**  
**查找 → 浏览 → 理解 → 追踪关系 → 比较方案 → 检查证据 → 发现缺口。**

The project is still building its V1 foundation, so not every knowledge entry point or Workspace exists yet. Over time, the same knowledge base can support Wiki / Browse, Single Object / Article, Timeline, Graph / Ecosystem, Compare, Evidence / Verification, and structured Agent / API access.

当前项目仍在建设 V1 基础设施，并不是所有知识入口和知识工作空间（Workspace）都已经完成。长期会从同一份知识底座提供不同的访问方式，例如 Wiki / Browse、Single Object / Article、Timeline、Graph / Ecosystem、Compare、Evidence / Verification，以及结构化的 Agent / API 访问。

These are not separate databases. They are different representations of the same Atlas for different cognitive tasks.

不同形式不是不同数据库，而是同一 Atlas 面向不同认知任务的表达。

> **Knowledge is stable; representations are fluid.**  
> **知识相对稳定，表达可以流动。**

## Why an “Interoperability Solution Space”? / 为什么是“互操作方案空间”？

InteropAtlas is not limited to a single industry. It focuses on a cross-domain question: **how can independently designed systems work together?**

InteropAtlas 关注的不是某一个行业，而是一个跨领域问题：**彼此独立设计的系统怎样协同工作。**

This problem appears in communications, data representation, video and audio, time synchronization, identity, security, discovery, semantics, Agents, control, automation, and many other domains. A real problem is rarely solved by one standard alone; it often involves specifications, implementations, methods, organizations, compatibility relations, and concrete scenarios together.

这可能发生在通信、数据表达、视频与音频、时间同步、身份、安全、发现、语义、Agent、控制与自动化等领域。一个现实问题通常也不会只靠一份标准解决，而会同时涉及规范、实现、方法、组织、兼容关系和具体场景。

So IA does not merely ask “what standards exist?” It progressively helps answer:

因此 IA 的目标不是回答“有哪些标准”，而是逐步帮助回答：

> **What solutions has humanity already developed for this interoperability problem? How are they related? What is the evidence? Where should I explore next?**  
> **这个互操作问题，人类已经有哪些可用方案？它们之间是什么关系？依据是什么？我应该从哪里继续探索？**

## Product philosophy / 产品哲学

InteropAtlas follows a small set of long-term principles:

InteropAtlas 的长期设计遵循几条简单原则：

> **Knowledge belongs to the commons.**  
> **知识属于公共共同体。**
>
> **Perspective belongs to the individual.**  
> **视角属于个人。**
>
> **Representation should adapt to cognition.**  
> **表达应适应认知。**
>
> **Personalization must remain reversible and transparent.**  
> **个性化必须可逆、透明、可检查。**

And one principle runs through both knowledge construction and product design:

以及一条贯穿知识建设和产品设计的原则：

> **Adopt → Profile → Extend → Invent**
>
> **Prefer understanding and reusing existing standards and mature prior art; invent only when a real gap remains.**  
> **优先理解和复用已有标准与成熟先例；只有真实缺口仍然存在时才自行发明。**

The full meaning of these principles, together with Atlas-first, Knowledge Workspace, Human + Agent, Personal Knowledge Space, and long-term directions, is documented in [`Master Design`](docs/interopatlas-master-design-v1.0.zh-CN.md) and [`Knowledge Philosophy`](docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md). Ordinary knowledge users do not need to read them first.

这些原则的完整含义，以及 Atlas-first、知识工作空间（Knowledge Workspace）、Human + Agent、个人知识空间（Personal Knowledge Space）和长期方向，都放在 [`Master Design`](docs/interopatlas-master-design-v1.0.zh-CN.md) 与 [`Knowledge Philosophy`](docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md) 中。它们不要求普通知识使用者先阅读。

## Want to go further? / 想进一步参与？

Different goals have different entry points; you do not need to read the entire repository from the beginning.

不同目的有不同入口，不需要从头读完整个仓库。

| Goal / 你想做什么 | Start here / 从哪里开始 |
| --- | --- |
| Understand what IA includes / 了解 IA 收录什么 | [`Definition & Scope / 项目定义与范围`](docs/interopatlas-definition-and-scope-v0.2.zh-CN.md) |
| Understand long-term design and philosophy / 理解项目长期设计与哲学 | [`Master Design`](docs/interopatlas-master-design-v1.0.zh-CN.md) |
| See the current build state / 查看当前建设到哪里 | [`PROJECT_STATE.md`](PROJECT_STATE.md) |
| Human maintenance / contribution / Human 参与维护与贡献 | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Agent onboarding / maintenance / Agent 接手或维护项目 | [`AGENTS.md`](AGENTS.md) |
| Find specifications, profiles, architecture, and policies / 查找规范、Profile、架构和政策 | [`docs/README.md`](docs/README.md) |
| Review research, experiments, and change history / 查看研究、实验和变更过程 | [`03_Evolution/`](03_Evolution/) |

Repository structure, P1–P6, the current P6 implementation route, Migration, Intake, Governance, and similar project-maintenance material belong to the second layer of context and are intentionally not expanded on the homepage.

项目维护结构、P1–P6、当前 P6 施工路线、Repository Structure、Migration、Intake、Governance 等内容属于第二层维护上下文，不在首页展开。

## Current status / 当前状态

InteropAtlas is still at an early stage. The current priority is to establish a reliable foundation for V1 Canonical Knowledge, continuous Intake, Human / Agent Access, and real-data use—not to claim complete coverage of the interoperability world.

InteropAtlas 仍处于早期建设阶段。当前重点是让 V1 规范知识（Canonical Knowledge）、持续收录（Intake）、Human / Agent Access 和真实数据使用形成可靠基础，而不是宣称已经覆盖完整的互操作世界。

For the live project checkpoint and next work, see [`PROJECT_STATE.md`](PROJECT_STATE.md).

实时项目断点与下一步工作以 [`PROJECT_STATE.md`](PROJECT_STATE.md) 为准。

## License / 许可证

- Software code / 软件代码: Apache License 2.0
- Structured factual data / 结构化事实数据: CC0 1.0 Universal
- Original documentation / research / 原创文档与研究: CC BY 4.0

See [`LICENSE.md`](LICENSE.md) for the complete boundary. Third-party standards text, trademarks, logos, and other materials remain subject to their respective rights and licenses.

完整边界见 [`LICENSE.md`](LICENSE.md)。第三方标准文本、商标、Logo 和其他材料仍受各自权利与许可证约束。
