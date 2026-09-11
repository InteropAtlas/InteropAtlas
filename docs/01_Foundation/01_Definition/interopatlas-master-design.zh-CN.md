# InteropAtlas 总体设计（Master Design）

<!-- InteropAtlas Document Metadata v0
Document Status: active master design
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T18:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：当前有效的总体设计基线（Active Master Design）
>
> 目的：回答 InteropAtlas 是什么、长期要成为怎样的系统、主要系统边界是什么。当前施工状态不在本文维护，以 `PROJECT_STATE.md` 为准。
>
> 项目的价值哲学与派生建设原则由 [`knowledge-philosophy-and-principles.zh-CN.md`](/docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md) 维护；本文不重复建立第二套哲学清单。

[简体中文](interopatlas-master-design.zh-CN.md) | [English](interopatlas-master-design.md)

## 1. InteropAtlas 是什么

InteropAtlas 是一个面向全人类的、开放、机器可读、可追溯、可持续分析与演化的 **互操作方案空间（Interoperability Solution Space）公共知识基础设施**。

它持续连接人类已经用于解决互操作问题的标准、规范、协议、配置规范、接口、格式、成熟先例、方法、指南、框架、实现、工具、服务、组织、能力、需求、场景、关系、事件、证据、来源追踪、评估与开放缺口，以及未来经研究和真实使用证明有必要纳入的其他知识类型。

InteropAtlas 不是单纯的标准目录、网站、知识图谱产品、智能体数据库、个人知识管理软件或推荐系统。这些都可能成为它的组成部分、访问方式或投影，但都不是项目本身。

> **地图优先（Atlas-first）：核心资产是共享、可验证、可演化的知识世界；Human、Agent、API、网站和未来界面都是访问与操作这个世界的方式。**

## 2. 上位哲学与总体设计

InteropAtlas 的核心产品哲学是：

> **知识属于公共共同体。视角属于个人。**  
> **Knowledge belongs to the commons. Perspective belongs to the individual.**

动态命题是：

> **知识流动，创造不息。**  
> **Knowledge travels. Creation continues.**

发现（Discover）、连接（Connect）、传递（Transmit）、转化（Transform）、复用（Reuse）和创造（Create）构成知识流动与回流公共共同体的基本过程。

完整论证见 [`知识哲学与原则`](/docs/01_Foundation/02_Principles/knowledge-philosophy-and-principles.zh-CN.md)。

## 3. 长期系统结构：共享知识 → 个人视角 → 体验

```text
                 公共知识共同体
            （Public Knowledge Commons）
                         │
                 规范知识（Canonical Knowledge）
                         │
                         ↓
              个人知识空间（Personal Knowledge Space）
                         │
          个人状态 / 意图 / 上下文 / 偏好
                         │
                         ↓
              视角 / 选择（Perspective / Selection）
                         │
                         ↓
                  投影（Projection）
                         │
                         ↓
             表达 / 工作空间（Representation / Workspace）
                         │
                    Human / Agent
```

### 3.1 公共知识共同体

公共层回答“人类已经知道什么”：对象是什么、彼此有什么关系、谁发布或维护、什么证据支持某个陈述、什么是事实与评估，以及哪些内容未知、未记录、有争议、过时或已被替代。

公共事实原则上不应因为“谁在看”而改变。身份、证据、来源追踪、关系、生命周期与明确未知边界应保持稳定、可验证和可恢复。

专项设计见 [`公共知识共同体与个人知识空间`](/docs/02_System/01_Knowledge/02_Workspace/public-commons-and-personal-knowledge-space.zh-CN.md)。

### 3.2 个人知识空间

个人层不复制一份私人的规范知识地图，而是在公共知识之上保存或计算个人状态、当前意图、注意力和选择。个性化可以改变注意力、选择、排序和表达，但不能静默改写公共事实；公共基线必须始终可访问。

### 3.3 体验 / 工作空间

```text
规范知识
   ↓
视角 / 选择
   ↓
投影
   ↓
表达 + 操作
   ↓
工作空间
```

- **视角（Perspective）**：现在什么知识值得进入注意力？
- **投影（Projection）**：对已经选中的知识，当前任务需要暴露哪些维度、关系与结构？
- **表达（Representation）**：这些知识应以什么形式出现？
- **工作空间（Workspace）**：在这种认知方式下，主体能够对知识做什么？

具体设计见 [`知识工作空间设计原则`](/docs/02_System/01_Knowledge/02_Workspace/knowledge-workspace-design-principles.zh-CN.md)。

## 4. 稳定知识，流动表达

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

底层知识的身份、证据、来源追踪、关系、生命周期和明确未知边界应尽量保持稳定和可恢复；上层允许根据主体、任务和认知方式形成不同投影与表达。

文字、百科式浏览、时间线、关系图、比较、矩阵、地图、图像、音频、视频、交互解释、模拟、游戏以及面向 Agent 的结构化表达，都可以是同一知识底座的不同表示。任何一种表示都不应成为第二事实源。

## 5. Human 与 Agent 共享同一个知识世界

“Human-first”和“Agent-first”都不是最终定位。最终原则是 **Atlas-first**。

```text
                Canonical Knowledge
                         ↑↓
                    Perspective
                         ↑↓
                     Projection
                         ↑↓
                     Workspace
                    ↙             ↘
                 Human           Agent
```

Human 与 Agent 应尽可能使用同一套规范知识、证据和选择 / 投影边界。差异主要存在于访问方式、表达、操作能力与权限，而不是各自拥有一套事实世界。

Agent 输出、推理和建议不自动等于规范事实。写入公共知识必须经过明确的 **Candidate → Validation → Acceptance / Review** 边界。

## 6. 项目的设计层级

```text
L0  使命 / 哲学
L1  总体设计
L2  架构 / 长期方向
L3  运行与演化模型
L4  当前主线 / 建设重点
L5  契约 / 规范 / Profile
L6  Work Item / Implementation
```

低层工作不能静默改写高层使命；高层原则也不能替代低层可执行契约。

当前主线由 `PROJECT_STATE.md` 表达；具体 Work Item 由 GitHub Issue / PR 表达。总体设计不维护任务树。

## 7. 真实使用与系统演化

InteropAtlas 不是“先把世界收录完，再开始使用”的项目。知识模型和产品必须通过真实查询、真实工作流、真实收录和真实失败持续接受检验。

当现实暴露模型缺口时，默认顺序是：

```text
真实问题 / 查询 / 工作流
        ↓
识别缺口
        ↓
检查成熟先例 / 标准
        ↓
Adopt → Profile → Extend → Invent
        ↓
必要时演化 Canonical Model / Contract
```

真实使用可以塑造知识模型，但不能绕过证据、审查和治理边界。

## 8. 长期路线不是阶段编号或项目版本

InteropAtlas 的长期项目本身、总体路线、Living Documents 和 Owner View 不以连续 `P1 / P2 / P3...` 或 `V1 / V2` 作为规划框架。

历史上的阶段编号和旧版本称呼只是某轮建设过程的历史标签，保留在 Git history、closed Issues 和 Evolution 中，不再定义当前方向。

现行规划关系是：

```text
使命 / 哲学
    ↓
长期能力域
    ↓
当前主线
    ↓
真实 Work Item
```

版本号仍然适用于本来具有版本身份或兼容边界的现实对象和技术制品，例如外部标准版本、协议、Schema、兼容契约、发布制品和历史快照；不要把这种版本身份扩展成项目计划版本号。

## 9. 长期能力域

长期方向包括但不限于：

- Atlas Coverage & Continuous Intake；
- Knowledge Modeling Evolution；
- Knowledge Operation Spaces；
- Human + Agent Shared Operation；
- Personal Knowledge Space；
- Knowledge Lifecycle / Metabolism；
- Match / Discovery / Recommendation；
- Open Ecosystem & Federation。

这些是长期能力域，不是固定阶段。是否进入施工必须由真实问题、Prior Art、真实数据 / 使用证据、风险与可验证性共同决定。

详细路线见 [`InteropAtlas 长期路线图`](/docs/01_Foundation/03_Direction/interopatlas-long-term-roadmap.zh-CN.md)。

## 10. 当前状态边界

总体设计不自动授权长期能力进入当前施工。

当前只应从 `PROJECT_STATE.md` 判断：

- 当前主线是什么；
- 哪些能力正在运行；
- 哪些任务是真正 Ready / In Progress；
- 哪些高影响事项仍需 Owner Gate。

核心原则：**长期方向可以稳定，当前路径必须持续根据真实世界修正。**
