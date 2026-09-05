# InteropAtlas 总体设计（Master Design）

<!-- InteropAtlas Document Metadata v0
Document Status: active master design
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T04:20:00+08:00
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
> 目的：回答 InteropAtlas **是什么、长期要成为怎样的系统、主要系统边界是什么，以及当前基础建设周期在长期路线中的位置**。
>
> 项目的价值哲学与派生建设原则由 [`knowledge-philosophy-and-principles.zh-CN.md`](knowledge-philosophy-and-principles.zh-CN.md) 维护；本文不重复建立第二套哲学清单。具体实现架构、阶段计划和单项规范由下位文档维护。

[简体中文](interopatlas-master-design.zh-CN.md) | [English](interopatlas-master-design.md)

## 1. InteropAtlas 是什么

InteropAtlas 是一个面向全人类的、开放、机器可读、可追溯、可持续分析与演化的**互操作方案空间（Interoperability Solution Space）公共知识基础设施**。

它持续连接人类已经用于解决互操作问题的标准、规范、协议、配置规范、接口、格式、成熟先例、方法、指南、框架、实现、工具、服务、组织、能力、需求、场景、关系、事件、证据、来源追踪、评估与开放缺口，以及未来经研究和真实使用证明有必要纳入的其他知识类型。

InteropAtlas 不是单纯的标准目录、网站、知识图谱产品、智能体数据库、个人知识管理软件或推荐系统。这些都可能成为它的组成部分、访问方式或投影，但都不是项目本身。

> **地图优先（Atlas-first）：核心资产是共享、可验证、可演化的知识世界；人（Human）、智能体（Agent）、API、网站和未来界面都是访问与操作这个世界的方式。**

## 2. 上位哲学与总体设计的关系

InteropAtlas 的核心产品哲学只有一个相互依存的命题：

> **知识属于公共共同体。视角属于个人。**  
> **Knowledge belongs to the commons. Perspective belongs to the individual.**

它的动态命题是：

> **知识流动，创造不息。**  
> **Knowledge travels. Creation continues.**

发现（Discover）、连接（Connect）、传递（Transmit）、转化（Transform）和复用（Reuse）是知识跨越不同边界的典型流动机制；创造（Create）让主体站在已有知识之上产生新的知识、方法、实现、规范或作品，并使新的成果有机会重新进入公共共同体。

完整论证、知识流动模型、知识代谢边界以及产品与建设原则只在 [`知识哲学与原则`](knowledge-philosophy-and-principles.zh-CN.md) 中维护。总体设计只承接这些上位约束，不重新定义它们。

## 3. 长期系统结构：共享知识 → 个人视角 → 体验

InteropAtlas 的长期形态可以用三个相互连接、但必须保持边界的层面理解：

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
                    人 / 智能体
                 （Human / Agent）
```

### 3.1 公共知识共同体

公共层回答“人类已经知道什么”：对象是什么、彼此有什么关系、谁发布或维护、什么证据支持某个陈述、什么是事实与评估，以及哪些内容未知、未记录、有争议、过时或已被替代。

公共事实原则上不应因为“谁在看”而改变。身份、证据、来源追踪、关系、生命周期与明确未知边界应保持稳定、可验证和可恢复。

专项设计见 [`公共知识共同体与个人知识空间`](public-commons-and-personal-knowledge-space.zh-CN.md)。

### 3.2 个人知识空间

个人层不复制一份私人的规范知识地图，而是在公共知识之上保存或计算个人状态、当前意图、注意力和选择。任务、已有知识、兴趣、时间预算、认知 / 媒介偏好、无障碍需要等可以影响个人视角，但不能被静默提升为公共事实。

个性化可以改变注意力、选择、排序和表达；公共基线必须仍然可访问。隐私、反信息茧房、个人注意力生命周期和可携带性等具体要求由专项文档维护。

### 3.3 体验 / 工作空间

最终体验由知识、任务、主体、上下文和认知方式共同决定：

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

- **视角（Perspective）**回答：现在什么知识值得进入注意力？
- **投影（Projection）**回答：对已经选中的知识，当前任务需要暴露哪些维度、关系与结构？
- **表达（Representation）**回答：这些知识应以什么形式出现？
- **工作空间（Workspace）**进一步回答：在这种认知方式下，主体能够对知识做什么？

具体工作空间家族、选择 / 投影边界和设计要求见 [`知识工作空间设计原则`](knowledge-workspace-design-principles.zh-CN.md)。

## 4. 稳定知识，流动表达

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

这不是另一条独立哲学，而是知识流动中“转化（Transform）”机制在系统架构上的直接含义。

InteropAtlas 应尽量让底层知识的身份、证据、来源追踪、关系、生命周期和明确未知边界保持稳定和可恢复，同时允许上层根据主体、任务和认知方式形成不同投影与表达。

文字、百科式浏览、时间线、关系图、比较、矩阵、地图、图像、音频、视频、交互解释、模拟、游戏以及面向智能体的结构化表达，都可以是同一知识底座的不同表示。任何一种表示都不应反过来成为第二事实源。

## 5. 人与智能体共享同一个知识世界

“人类优先（Human-first）”和“智能体优先（Agent-first）”都不是最终定位。最终原则是**地图优先（Atlas-first）**。

```text
                规范知识（Canonical Knowledge）
                         ↑↓
                    视角（Perspective）
                         ↑↓
                    投影（Projection）
                         ↑↓
                  工作空间（Workspace）
                    ↙             ↘
                 人（Human）    智能体（Agent）
```

人与智能体应尽可能使用同一套规范知识、证据和明确的选择 / 投影边界。差异主要存在于访问方式、表达、操作能力与权限，而不是各自拥有一套事实世界。

智能体输出、推理和建议不自动等于规范事实。写入公共知识必须经过明确的**候选 → 验证 → 接受 / 审查（Candidate → Validation → Acceptance / Review）**边界。

## 6. 项目的层级

InteropAtlas 同时存在不同尺度的设计，必须明确分层：

```text
L0  使命 / 哲学（Mission / Philosophy）
    为什么存在；服务谁；什么不能轻易改变

L1  总体设计（Master Design）
    公共知识 / 个人视角 / 体验、地图优先、长期系统边界

L2  架构 / 长期方向（Architecture / Long-term Directions）
    规范知识、生命周期、视角、投影、工作空间、访问、个人空间

L3  运行与演化模型（Operating & Evolution Model）
    项目如何研究、使用、贡献和持续演化

L4  基础建设 / 阶段路线图（Foundation / Phase Roadmap）
    有边界的建设周期与迁移阶段

L5  契约 / 规范 / 配置规范（Contracts / Specifications / Profiles）
    收录、迁移、人类界面、智能体访问、协作、来源追踪等可执行规则

L6  工作项 / 实现（Work Items / Implementation）
    Issue / PR / 实验 / 迁移 / 收录批次
```

低层工作不能静默改写高层使命；高层原则也不能替代低层可执行契约。

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
采用 → 配置 → 扩展 → 发明
        ↓
必要时演化规范模型 / 契约
```

因此，真实使用应能够塑造本体模型，但不能绕过证据、审查和治理边界。具体研究方法、`Adopt → Profile → Extend → Invent` 原则和知识代谢模型由哲学与研究治理文档维护。

## 8. P1–P6 的正确位置

P1–P6 **不是整个 InteropAtlas 的生命周期或最终路线图**。

它是 2026-09-02 知识工作空间 / 视角方向重大升级之后，为避免直接凭直觉重构项目而启动的第一轮 **V1 基础建设 / 架构重新验证周期（V1 Foundation / Architecture Revalidation Cycle）**：

```text
早期 InteropAtlas / 参考实现模型
        ↓
P1  设计原则
        ↓
P2  既有先例 / 标准研究
        ↓
P3  当前状态审计
        ↓
P4  V1 架构 / 路线图重置
        ↓
P5  真实数据实验 / 压力测试
        ↓
P6  V1 实现 + 迁移 + 持续收录
        ↓
V1 成为可运行基础
        ↓
长期知识地图成长 / 工作空间 / 个性化 / 人与智能体演化
```

P6 完成只意味着新方向获得可信的运行基础，不意味着 InteropAtlas 完成。实时状态与恢复点只由 [`PROJECT_STATE.md`](../PROJECT_STATE.md) + GitHub Issue / PR + 更新的 Git 证据维护。

## 9. 当前 V1 与长期愿景

当前 V1 优先建设未来很难绕开的基础能力：稳定规范身份与契约、证据 / 来源追踪 / 明确未知边界、安全持续收录、旧模型迁移、明确 Selection / Projection 边界的人类工作空间、人与智能体共享结构化访问、候选写入与规范接受分离，以及可验证、可回滚、可演化的运行机制。

个人知识空间、动态个人视角、表达转换、更多工作空间、知识代谢、匹配（MATCH）和人与智能体共享工作空间属于长期方向。当前设计应保留架构空间，但不能为了未来想象过早冻结模式（Schema）。

长期阶段关系见 [`InteropAtlas 长期路线图`](interopatlas-long-term-roadmap.zh-CN.md)。

## 10. 信息损失与开放边界

现实进入知识系统，再进入具体表达，会连续发生有意识的信息选择与损失：

```text
现实（Reality）
→ 收集（Collection）
→ 建模（Modeling）
→ 选择（Selection）
→ 投影（Projection）
→ 表达（Representation）
→ 感知 / 行动（Perception / Action）
```

InteropAtlas 不要求所有表达无损，而要求**任务适配 + 关键语义可恢复**。身份、来源追踪、证据、范围、事实 / 推断边界、关键关系和明确未知不应因为生成更易读的表达而被静默抹除。

开放性也不只等于许可证。公共知识、证据、访问、贡献、表达和项目演化都应尽可能开放；长期个人空间还应避免被锁死在单一客户端。开放贡献不意味着所有贡献者拥有同等规范权威，身份、证据、审查、治理和权限边界仍必须明确。

## 11. 长期成功标准

InteropAtlas 的成功不只用“收录了多少标准”衡量。更重要的是：

- 互操作方案空间覆盖率是否持续扩大；
- 证据与来源追踪是否可信；
- 人和智能体是否能解决真实互操作问题；
- 是否能发现原本不可见的方案、关系与缺口；
- 已有知识是否更容易跨越边界并被复用；
- 新的创造是否能够经过验证重新进入公共共同体；
- 同一知识是否能在不同任务中获得合适表达；
- 个人是否拥有自己的认知窗口，同时保留完整公共世界；
- 是否能够抵抗不透明个性化和信息茧房；
- 真实使用是否能够反向改进知识模型、收录和产品设计。

## 12. 文档职责与继续阅读

总体设计故意保持在系统边界层，不继续展开专项规则。相关职责如下：

- [`知识哲学与原则`](knowledge-philosophy-and-principles.zh-CN.md)：价值哲学、知识流动、创造循环与派生建设原则；
- [`公共知识共同体与个人知识空间`](public-commons-and-personal-knowledge-space.zh-CN.md)：公共 / 个人边界、个人状态、个性化、隐私、反信息茧房与个人空间互操作；
- [`知识工作空间设计原则`](knowledge-workspace-design-principles.zh-CN.md)：Selection / Projection / Representation / Workspace；
- [`长期路线图`](interopatlas-long-term-roadmap.zh-CN.md)：长期阶段关系与当前基础建设周期；
- [`项目状态`](../PROJECT_STATE.md)：唯一的项目级实时施工断点；
- 当前 Issue / Contract / Specification：具体可执行工作。

面对重大设计问题，先判断它属于哪一层，再读取对应的正式文档；不要通过复制上位内容到多个文件来“确保不丢失”。Git 历史与 Evolution 保存演化过程，Living Documents 保存当前有效设计。
