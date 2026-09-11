# InteropAtlas 知识工作空间设计原则 v1.0（Knowledge Workspace Design Principles）

<!-- InteropAtlas Document Metadata v0
Document Status: active design principles
Document Created At: 2026-09-02T21:11:00+08:00
Document Updated At: 2026-09-04T22:50:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 状态：当前有效的设计原则（Active Design Principles），用于约束当前产品与知识空间方向。
>
> 上游意图：GitHub Issue #122 —— 知识工作空间 / 视角（Knowledge Workspace / Perspective）路线。
>
> 版本说明：v1.0 相对于此前的参考实现（Reference Implementation）产品模型代表一次重大项目设计转向。本文是重要设计基线，但其中的视角 / 投影 / 工作空间（Perspective / Projection / Workspace）术语，在后续研究和实验完成前仍属于暂定概念。
>
> 本文建立设计原则，而不是最终的人类界面（UI）、模式（Schema）、工作空间目录或实现契约。

## 1. 目的

InteropAtlas 仍然是开放、机器可读、可追溯的互操作知识基础设施。它的目的不是成为通用笔记应用，也不是把某一种网站布局变成知识的最终形态。

随着规范知识（Canonical Knowledge）不断结构化，项目应该允许针对不同认知任务，对同一份底层知识进行不同的选择、投影、表达和操作。

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

这把仓库已有的不变量 `规范状态 ≠ 生成视图（Canonical State ≠ Generated View）` 从工程边界进一步扩展为产品设计原则。

## 2. 稳定知识，流动表达（Stable Knowledge, Fluid Representations）

共享规范知识层应在适当情况下保存：稳定对象 / 身份（Objects / Identities）、关系（Relations）、属性（Properties）、证据 / 来源（Evidence / Sources）、来源追踪（Provenance）、生命周期（Lifecycle）、明确的未知 / 未记录边界（explicit unknown / not-recorded），以及模型能够准确表达的上下文 / 范围（Context / Scope）。

生成页面、时间线、关系图、比较、智能体回答和其他表达**不得（MUST NOT）**静默成为相互竞争的事实来源。有损表达**不得（MUST NOT）**仅仅因为更容易阅读，就覆盖信息更丰富的规范知识。

## 3. 先选择，再呈现（Selection Before Presentation）

好的呈现无法修复根本错误的知识选择。

```text
规范知识（Canonical Knowledge）
        ↓
视角 / 选择（Perspective / Selection）
        ↓
已选知识（Selected Knowledge）
        ↓
投影（Projection）
        ↓
表达 / 工作空间（Representation / Workspace）
        ↓
交互（Interaction）
        ↓
人 / 智能体（Human / Agent）
```

这是一套概念模型，不要求建立彼此独立的服务、数据库或模式（Schema）对象。

### 视角（Perspective）

回答：**现在什么知识应该进入注意力？**

未来可能使用显式过滤、分面 / 分类（Facets / Categories）、时间、生命周期 / 状态、当前任务 / 查询、导航上下文、关系距离、证据 / 新鲜度信号、保存的兴趣、分组 / 聚合，以及语义明确且可审计的排序或强调规则。

视角比一次性的人类界面过滤器（UI Filter）更宽。未来的视角可能被保存，并随着时间或规范知识变化而持续重新求值。选择也不必是二元的：上下文可以被强调、弱化、分组、折叠或作为背景保留。

### 投影（Projection）

回答：**在已经选中的知识中，当前任务需要暴露哪些维度、关系或结构？**

例如：历史分析需要发布时间 / 生命周期；生态分析需要组织 / 关系；比较（Compare）需要可比较属性；验证需要证据 / 来源追踪（Evidence / Provenance）；浏览（Browse）需要层级 / 分类。

视角 / 投影（Perspective / Projection）的边界仍属暂定，在正式形成模式（Schema）或运行时契约之前必须经过实验验证。

### 表达 / 工作空间（Representation / Workspace）

表达（Representation）是已选择、已投影知识的具体呈现。工作空间（Workspace）则是在表达基础上加入与其认知任务相匹配的操作能力。因此，呈现与操作彼此关联。

## 4. 多种工作空间（Multiple Workspaces）

InteropAtlas **不得（MUST NOT）**为所有知识规定唯一最终表达形式。

基础 / 预期的工作空间家族包括：
- **百科式浏览（Wiki / Browse）** —— 搜索、分类 / 分面深入，以及在陌生知识空间中的链接导航；
- **单对象 / 文章（Single Object / Article）** —— 线性理解一个对象；
- **时间线（Timeline）** —— 历史演化、版本、代际与事件；
- **关系图 / 生态图（Graph / Ecosystem）** —— 标准、组织、实现、方法、能力及其他实体之间的关系；
- **比较（Compare）** —— 并行检查真正具有可比性的候选方案；
- **证据 / 验证（Evidence / Verification）** —— 检查来源、来源追踪、断言边界和未知状态。

未来的工作空间还可能包括大纲（Outline）、矩阵（Matrix）、地图（Map）、交互解释、模拟（Simulation）、音频 / 视频表达、游戏式表达，或目前尚未识别的形式。这些只是开放可能性，不是实现承诺。

## 5. 百科式浏览是基础，但不是唯一方式（Wiki / Browse Is Foundational, Not Exclusive）

类似 Wikipedia 的浏览体验，是长期必须具备的人类工作空间（Human Workspace），因为它为进入陌生知识提供了一条熟悉路径：

```text
搜索已知对象
        或
浏览领域
    ↓
子领域 / 分面 / 分类
    ↓
对象
    ↓
相关对象
```

语义分类**不得（MUST NOT）**被压缩成单一物理文件夹树。一个对象可以通过多种分类和关系到达。浏览是知识地图（Atlas）上的一种投影，而不是本体模型（Ontology）本身，也不是唯一的导航模型。

## 6. 多视图必须有认知依据（Multiple Views Require Cognitive Justification）

按照多重协调视图（Multiple Coordinated Views）研究的思路，只有当新的工作空间能够暴露其他工作空间隐藏的意义、与其他视图形成互补、分解困难任务，或实质性降低认知负担时，它才值得存在。

增加一个长期工作空间之前，至少应回答以下一个问题：
- 什么任务因此成为可能，或明显变得更容易？
- 哪些属性、关系或抽象因此变得可感知？
- 降低了什么认知负担？
- 为什么扩展已有工作空间不能更好地解决问题？

在有价值的情况下，多个工作空间应共享选择 / 焦点状态，而不是表现为彼此无关的副本。

## 7. 人与智能体共享同一个知识世界（Human and Agent Share One Knowledge World）

人类界面与机器 / 智能体界面**必须（MUST）**使用同一份规范知识，而不是建立彼此分离的事实世界。访问方式可以不同：人可能进行浏览 / 阅读 / 比较 / 验证（Browse / Read / Compare / Verify）；智能体可能进行查询 / 遍历 / 过滤 / 检索证据 / 组合 / 解释（Query / Traverse / Filter / Retrieve Evidence / Compose / Explain）。

长期方向是让人和智能体（Human + Agent）在同一份视角 / 工作空间状态上协作。智能体生成的叙述或推断**不得（MUST NOT）**静默成为规范事实（Canonical Fact）。

## 8. 信息损失与可恢复性（Information Loss and Recoverability）

收集、建模、选择、投影、表达以及人的感知都会造成信息损失。InteropAtlas 不假定所有表达都是无损的；针对具体任务的表达可以有意省略信息。

应保护可恢复性：
- 尽可能保存来源追踪和来源身份（Provenance / Source Identity）；
- 让规范知识独立于具体投影保存；
- 保存足够上下文，以理解断言的边界；
- 绝不允许有损表达覆盖更丰富的规范状态；
- 在实际可行时，让重要排除项、未知项和选择原因可检查。

> **表达可以有意有损；规范知识与来源追踪应尽可能保持可恢复。**  
> *Representations may be deliberately lossy; Canonical Knowledge and Provenance should remain as recoverable as reasonably possible.*

保真度本身不是价值的唯一尺度；表达质量取决于它所服务的任务。

## 9. 渐进披露与信息气味（Progressive Disclosure and Information Scent）

存在许多可能的工作空间，并不意味着界面需要同时提供大量选择。

InteropAtlas 应从少量、容易理解的入口开始，随着用户意图变得清晰再逐步暴露选择；标签应该让人能够预判下一步操作，而不是暴露内部术语；首页也不应试图表达完整的本体模型或工作空间目录。

此前的 `3 → 3 → 3` 直觉只是一种控制展开规模的启发式规则，不是固定规则。未来顶层入口仍可能只有“搜索 + 浏览 + 智能体（Search + Browse + Agent）”，而更丰富的工作空间只在真正有意义时出现。

## 10. 架构应允许实验（Architecture Should Permit Experimentation）

```text
交互：人 / 智能体 / 人+智能体
（Interaction: Human / Agent / Human+Agent）
        ↑
工作空间 / 表达（Workspace / Representation）
        ↑
投影（Projection）
        ↑
视角 / 选择（Perspective / Selection）
        ↑
规范知识（Canonical Knowledge）
```

下层应足够稳定，使上层表达可以持续演化，而不需要复制或破坏规范知识。优先进行小规模实验，而不是过早建立通用抽象。

## 11. 当前原则与研究假设（Current Principles vs Research Hypotheses）

### 当前设计原则

1. IA 仍然是互操作知识基础设施，而不是通用笔记应用；
2. 规范知识与生成表达保持分离；
3. 同一知识可以支持多个工作空间；
4. 百科式浏览（Wiki / Browse）是必须且基础的，但不是唯一形式；
5. 选择 / 视角（Selection / Perspective）在概念上先于呈现（Presentation）；
6. 人与智能体共享同一份规范知识；
7. 表达可以有损，但来源追踪和规范知识的可恢复性仍然重要；
8. 新工作空间必须有任务 / 认知依据；
9. 渐进披露用于防止工作空间多样性演变成界面杂乱；
10. 在这些概念经过真实 IA 数据验证之前，不进行重大模式（Schema）变更。

### 研究假设——不是契约（Research Hypotheses — Not Contracts）

开放问题包括：
- 视角（Perspective）是否成为持久化的一等对象；
- 视角 / 投影 / 工作空间的精确边界；
- 是否需要通用工作空间协议（Workspace Protocol）；
- 动态 / 连续的视角求值；
- 个性化 / 排序 / 推荐的治理；
- 范围 / 上下文（Scope / Context）如何进入规范模型；
- 智能体可以修改多少工作空间状态；
- 哪些额外工作空间家族值得获得长期地位；
- 通用表达转换（Representation Transformation）能否被安全抽象；
- 如何评价信息损失、认知增益和选择质量。

这些问题**不得（MUST NOT）**被静默当作已经确定的架构。

## 12. 已确定的项目路线（Agreed Project Path）

```text
阶段 1（P1） 建立设计原则
        ↓
阶段 2（P2） 系统研究成熟先例与标准
        ↓
阶段 3（P3） 按新原则审计当前 InteropAtlas
        ↓
阶段 4（P4） 重绘架构与项目路线图
        ↓
阶段 5（P5） 运行小规模真实数据实验
        ↓
阶段 6（P6） 根据已验证结论恢复实现
```

P2 必须研究更广泛的问题，而不只是视角（Perspective）：信息检索 / 相关性 / 分面导航（Information Retrieval / Relevance / Faceted Navigation）；动态与连续查询（Dynamic / Continuous Queries）；焦点 + 上下文（Focus+Context）；多重协调视图 / 可视分析（Multiple Coordinated Views / Visual Analytics）；主题地图（Topic Maps）、RDF / 关联数据（Linked Data）、超文本（Hypertext）、知识图谱（Knowledge Graphs）、Web Annotation，以及相关的现代产品先例。

P3 在改变现有能力之前，应审计当前对象（Objects）、关系（Relations）、证据（Evidence）、生命周期（Lifecycle）、能力 / 分类（Capability / Classification）、搜索（Search）、浏览（Browse）、比较（Compare）、局部地图 / 关系图（Local Map / Graph）、人类路径 / 渲染器（Human Route / Renderer）和机器查询界面。

P4 按知识（Knowledge）、选择（Selection）、投影（Projection）、工作空间（Workspace）、机器 / 智能体（Machine / Agent）和评估（Evaluation）重新组织未来工作。

P5 使用范围明确的真实 IA 数据，以少量视角和表达形式进行实验，观察每种形式揭示了什么、隐藏了什么、扭曲了什么，以及让什么任务变得更容易。

## 13. 近期非目标（Near-term Non-goals）

- 不把 IA 变成通用个人知识管理 / 笔记应用（PKM / Note Application）；
- 现在不设计所有可能的工作空间；
- 不为了新奇而建设 3D / VR / 游戏界面；
- 实验之前不抽象通用转换引擎；
- 不建立隐藏的智能体项目事实（Agent Project Truth）；
- 默认不引入不透明的个性化 / 推荐；
- 在原则阶段不进行破坏性模式（Schema）迁移；
- 不丢弃现有搜索 / 比较 / 人类路径（Search / Compare / Human Route）工作，而是在 P3 中审计它们。

## 14. 成熟先例研究锚点（Prior-art Anchors）

Issue #122 继续作为以下方向的研究锚点：多重协调视图（Multiple Coordinated Views）、鱼眼 / 焦点+上下文 / 概览+细节（Fisheye / Focus+Context / Overview+Detail）、动态查询 / 可视信息检索（Dynamic Queries / Visual Information Seeking）、持续 / 连续查询（Standing / Continuous Queries）、ISO/IEC 13250 主题地图（Topic Maps）、W3C Web Annotation、JSON-LD / 关联数据（Linked Data）、OmniFocus 自定义视角（Custom Perspectives），以及现代多视图知识 / 数据库产品。

这些只是种子参考，不是白名单。P2 应按照：

> **采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**

主动寻找更多成熟标准与既有先例。

## 15. 决策规则（Decision Rule）

面对未来设计问题，依次询问：
1. 当前正在执行什么认知 / 互操作任务？
2. 什么知识应该进入注意力？
3. 需要哪些维度和关系？
4. 哪种表达最有利于理解 / 操作？
5. 什么信息 / 上下文会丢失？
6. 底层规范知识和证据能否恢复？
7. 在 IA 发明新机制之前，是否已有成熟先例能够解决这个问题？
