# InteropAtlas 总体设计 v1.0（Master Design）

<!-- InteropAtlas Document Metadata v0
Document Status: active master design
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T22:20:00+08:00
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
> 目的：回答 InteropAtlas **是什么、为什么存在、长期要成为怎样的系统、各层之间是什么关系，以及当前 P1–P6 基础建设周期（Foundation Cycle）在长期路线中的位置**。
>
> 本文位于具体实现架构、当前阶段计划和单项规范（Specification）之上，但不取代这些更具体的文档。

[简体中文](interopatlas-master-design.zh-CN.md) | [English](interopatlas-master-design.md)

## 1. InteropAtlas 是什么

InteropAtlas 是一个面向全人类的、开放、机器可读、可追溯、可持续分析与演化的**互操作方案空间（Interoperability Solution Space）公共知识基础设施**。

它试图持续连接人类已经用于解决互操作问题的：

- **标准 / 规范 / 协议 / 配置规范 / 接口 / 格式（Standards / Specifications / Protocols / Profiles / Interfaces / Formats）**；
- **成熟先例（Mature Prior Art / Precedents）**；
- **方法 / 指南 / 框架（Methods / Guidelines / Frameworks）**；
- **实现 / 工具 / 服务（Implementations / Tools / Services）**；
- **组织 / 治理主体（Organizations / Governance Actors）**；
- **能力 / 需求 / 场景（Capabilities / Needs / Scenarios）**；
- **关系 / 事件 / 上下文（Relations / Events / Context）**；
- **证据 / 来源 / 来源追踪（Evidence / Sources / Provenance）**；
- **评估 / 开放缺口（Assessments / Open Gaps）**；
- 以及未来经研究和真实使用证明有必要纳入的其他知识类型。

InteropAtlas 不是单纯的标准目录、网站、知识图谱产品、智能体（Agent）数据库、个人知识管理（PKM）软件或推荐系统。这些都可能成为它的组成部分、访问方式或投影，但都不是项目本身。

> **地图优先（Atlas-first）：核心资产是共享、可验证、可演化的知识世界；人（Human）、智能体（Agent）、API、网站和未来界面都是访问与操作这个世界的方式。**

## 2. 四条长期产品哲学

### 知识属于公共共同体（Knowledge belongs to the commons）

InteropAtlas 的公共知识层应尽可能成为全人类可访问、可复用、可验证、可扩展的基础设施，而不是某个个人、智能体或产品的私有事实世界。

### 视角属于个人（Perspective belongs to the individual）

完整知识世界可以共享，但不同人的目标、工作、兴趣、背景、已有知识、当前状态和注意力并不相同。个人应该能够拥有自己的动态知识视角（Perspective），而不需要复制或篡改公共事实。

### 表达应适应认知（Representation should adapt to cognition）

知识没有唯一正确的呈现形式。同一份知识可以根据当前的人、任务和认知方式，被表达为文字、百科式浏览（Wiki / Browse）、时间线（Timeline）、关系图（Graph）、比较（Compare）、矩阵（Matrix）、地图（Map）、图像、音频、视频、交互解释、模拟（Simulation）、游戏（Game）或未来尚未出现的形式。

### 个性化必须可逆、透明、可检查（Personalization must remain reversible and transparent）

个性化不能把公共知识世界替换成黑箱信息流。用户应能够理解为什么某些知识被选择、强调或弱化，并能够退出个人视角、回到公共知识地图（Public Atlas）、扩大视野或主动探索当前视角之外的重要知识。

## 3. 三个世界：共享 → 个人 → 体验（Shared → Personal → Experience）

InteropAtlas 的长期形态可以用三个相互连接、但必须保持边界的世界理解：

```text
                    InteropAtlas
                         │
        ┌────────────────┴────────────────┐
        │                                 │
    共享知识世界                        公共访问
（Shared Knowledge World）       搜索 / 浏览 / API
        │                                 │
        └────── 规范知识（Canonical Knowledge）──────┘
                         │
                         ↓
              个人知识空间（Personal Knowledge Space）
                         │
       用户状态 / 意图 / 上下文 / 历史
       知识状态 / 兴趣 / 注意力
       表达偏好 / 无障碍需求
                         │
                         ↓
            视角 / 选择 / 排序
      （Perspective / Selection / Ranking）
                         │
                         ↓
                投影（Projection）
                         │
                         ↓
              体验 / 工作空间（Workspace）
                         │
       文章 / 百科 / 关系图 / 时间线 / 比较
       图像 / 视频 / 模拟 / 交互 / 游戏
                         │
                  人 / 智能体
              （Human / Agent）
```

### 3.1 共享知识世界（Shared Knowledge World）

公共层回答的是：

- 人类已经知道什么？
- 某对象是什么？
- 它和其他对象有什么关系？
- 谁发布、维护或实现它？
- 什么证据支持某个陈述？
- 什么是事实（Fact），什么是评估（Assessment）？
- 哪些信息未知、未记录、有争议、过时或已被替代？

公共事实原则上不应因为“谁在看”而改变。

### 3.2 个人知识空间（Personal Knowledge Space）

个人层不应复制一份私人的规范知识地图（Canonical Atlas），而应建立在公共知识之上的**个人认知窗口、状态与选择层**。

它未来可能考虑：

- 当前任务与目标；
- 当前职业 / 项目 / 学习主题；
- 已知与未知；
- 最近使用与长期兴趣；
- 时间与环境上下文；
- 用户主动声明的关注与回避；
- 信息密度偏好；
- 文字、图像、音视频、交互等表达偏好；
- 无障碍（Accessibility）需要；
- 用户愿意投入的时间与深度；
- 需要主动跳出既有兴趣的探索模式。

这些信号属于个人视角 / 个人状态（Personal Perspective / Personal State），不应被错误提升为公共事实。

### 3.3 体验 / 工作空间（Experience / Workspace）

最终呈现不只由知识本身决定，而可能由以下组合共同决定：

```text
知识 × 任务 × 人 × 上下文 × 认知偏好
（Knowledge × Task × Person × Context × Cognitive Preference）
                         ↓
                  表达（Representation）
                         +
                    操作（Operations）
                         ↓
                  工作空间（Workspace）
```

工作空间因此不是“页面模板”，而是针对认知任务形成的**知识观察与操作空间**。

## 4. 稳定知识，流动表达

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

InteropAtlas 应尽量让底层知识的身份（Identity）、证据（Evidence）、来源追踪（Provenance）、关系（Relation）、生命周期（Lifecycle）与明确未知边界保持稳定和可恢复，同时允许上层表达持续演化。

```text
规范知识（Canonical Knowledge）
        ↓
生命周期 / 上下文信号（Lifecycle / Context Signals）
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

这是一套概念边界，不要求每一层都成为独立服务、数据库或模式（Schema）对象。

### 视角（Perspective）

回答：**现在什么知识值得进入注意力？**

视角可以是公共查询视角，也可以是个人认知视角。长期必须明确区分至少：

- **知识视角（Knowledge Perspective）**：根据知识空间本身的条件、范围（Scope）、时间、关系、证据、生命周期等进行选择；
- **个人视角（Personal Perspective）**：根据某个人当前状态、目标、兴趣、知识水平、认知偏好形成动态选择与强调。

### 投影（Projection）

回答：**对于已经选中的知识，当前任务需要暴露哪些维度、关系与结构？**

### 表达 / 工作空间（Representation / Workspace）

回答：**这些知识应该怎样被表达，以及用户 / 智能体在这里能够做什么？**

表达（Representation）决定知识以什么形式出现；工作空间（Workspace）则在表达之外，还提供与认知任务匹配的操作能力。

## 5. 知识操作空间，而不是固定网站

InteropAtlas 的长期产品不应该是一组被永久固定的页面，而应该是一套共享同一知识底座的**知识操作空间（Knowledge Operation Spaces）**。

基础工作空间家族包括但不限于：

- **百科式浏览（Wiki / Browse）**：搜索、分类 / 分面（Facet）深入、链接导航；
- **单对象 / 文章（Single Object / Article）**：线性理解一个对象；
- **时间线（Timeline）**：历史、版本、代际、事件与演化；
- **关系图 / 生态图（Graph / Ecosystem）**：关系、组织、标准、实现与生态；
- **比较（Compare）**：可比候选的并行检查；
- **证据 / 验证（Evidence / Verification）**：来源、来源追踪（Provenance）、断言边界、未知状态；
- **大纲 / 矩阵 / 地图（Outline / Matrix / Map）**；
- **交互解释 / 模拟（Interactive Explanation / Simulation）**；
- **音频 / 视频（Audio / Video）**；
- **游戏式表达（Game-like Representation）**；
- 未来尚未识别的新型表达。

新的工作空间不因“看起来新颖”而成立。它应证明自己能够暴露其他工作空间难以表达的意义、降低认知负担或提供新的有效操作。

## 6. 人与智能体共享同一个知识世界（Human + Agent）

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
                    ↖             ↗
                    共享状态（Shared State）
```

人与智能体应尽可能使用同一套规范知识（Canonical Knowledge）、证据（Evidence）和明确的选择 / 投影边界。

人可能进行浏览、阅读、比较、验证（Browse / Read / Compare / Verify）；智能体可能进行查询、关系遍历、过滤、检索证据、组合、解释和操作工作空间（Query / Traverse / Filter / Retrieve Evidence / Compose / Explain / Operate Workspace）。

长期目标不是让智能体在另一个黑箱里重新生成一套世界，而是让人与智能体可以在同一个可解释的知识空间和工作空间状态上协作。

智能体输出、推理和建议仍然不自动等于规范事实（Canonical Fact）。写入公共知识必须经过明确的**候选 → 验证 → 接受 / 审查（Candidate → Validation → Acceptance / Review）**边界。

## 7. 知识地图的成长循环

InteropAtlas 不是“先把世界收录完，再开始使用”的项目。知识模型和产品都应该通过真实使用持续被检验。

长期循环：

```text
知晓（KNOW）
建立、验证、连接知识
  ↓
使用（USE）
人 / 智能体使用知识地图解决真实问题
  ↓
发现（DISCOVER）
发现知识缺口、模型缺口、错误、过时信息和新方案
  ↓
贡献（CONTRIBUTE）
研究、验证并把新知识反馈给知识地图
  ↓
知晓（KNOW）
```

未来可以进一步发展：

```text
匹配（MATCH）
问题 ↔ 方案
人 ↔ 知识
人 ↔ 人
组织 ↔ 能力
需求 ↔ 标准 / 实现 / 方法
```

匹配（MATCH）不应退化为不透明的商业推荐，而应尽可能基于可解释的知识关系、上下文（Context）与用户控制。

## 8. 真实使用塑造本体模型（Ontology）

InteropAtlas 不应坐在设计阶段试图一次性把世界分类完。

```text
真实问题 / 查询 / 工作流（Query / Workflow）
        ↓
使用当前知识地图
        ↓
发现表达或查询缺口
        ↓
检查成熟先例 / 标准（Prior Art / Standards）
        ↓
确认是否重复出现、是否为真实结构性问题
        ↓
采用 / 配置 / 扩展 / 发明（Adopt / Profile / Extend / Invent）
        ↓
必要时演化规范模型（Canonical Model）
```

因此：

> **让真实查询与真实贡献塑造本体模型（Ontology），而不是让预设本体模型限制现实。**

## 9. 知识代谢（Knowledge Metabolism）：重要方向，但保持研究边界

公共知识基础设施不能简单复制个人知识管理（PKM）的“删除旧笔记”逻辑；一个过时标准在历史设备、法律、兼容性或研究场景下仍可能是唯一正确的信息。

但 IA 同样不能假设所有知识永远处于同一注意力和计算优先级。

需要长期研究：

```text
收集（Collect）
→ 理解（Understand）
→ 整合（Integrate）
→ 应用（Apply）
→ 创造（Create）
→ 提炼（Distill）
→ 降权 / 归档 / 压缩 / 遗忘（Down-rank / Archive / Compact / Forget）
→ 在上下文需要时重新激活（Reactivate when context requires）
```

必须区分：

- 有效性（Validity）；
- 新鲜度 / 陈旧度（Freshness / Staleness）；
- 使用情况（Usage）；
- 相关性（Relevance）；
- 历史价值（Historical Value）；
- 权威性（Authority）；
- 生命周期（Lifecycle）。

**低当前权重 ≠ 低真实性 ≠ 低历史价值。**

知识代谢当前仍是需要研究和验证的上位方向，不应未经验证直接变成统一 `weight`、自动删除算法或稳定模式（Schema）。

公共知识生命周期（Lifecycle）与个人注意力生命周期（Attention Lifecycle）也必须分开：公共知识地图负责保存可恢复的历史与证据；个人空间负责决定什么现在值得进入某个人的注意力。

## 10. 个性化的边界：反信息茧房是设计问题

个性化（Personalization）是长期核心方向，但必须满足：

1. **始终保留公共基线（Public baseline remains available）**：任何人都能回到非个人化的公共知识地图；
2. **可解释（Explainability）**：重要选择、排序和弱化应尽可能说明依据；
3. **可逆（Reversibility）**：个人视角（Personal Perspective）可关闭、切换、重置；
4. **用户自主权（User agency）**：用户可以主动定义目标、偏好和探索方式；
5. **跳出当前视角（Perspective escape）**：系统应允许用户探索远离既有兴趣但重要的知识；
6. **事实隔离（Fact isolation）**：个性化改变注意力和表达，不改变公共事实；
7. **隐私边界（Privacy boundary）**：个人状态（Personal State）不应默认进入公共规范知识（Canonical Knowledge）；
8. **互操作性（Interoperability）**：未来个人状态、视角与工作空间应优先考虑可携带、可导出、可组合，而不是锁死在单一客户端。

## 11. 项目的层级，不要再混淆

InteropAtlas 同时存在不同尺度的设计。它们必须明确分层：

```text
L0  使命 / 哲学（Mission / Philosophy）
    为什么存在；服务谁；什么不能轻易改变

L1  总体设计（Master Design）
    共享 / 个人 / 体验、地图优先、长期产品形态

L2  架构（Architecture）
    规范知识 / 生命周期 / 视角 / 投影 / 工作空间 / 访问

L3  运行与演化模型（Operating & Evolution Model）
    知晓 → 使用 → 发现 → 贡献（KNOW → USE → DISCOVER → CONTRIBUTE）
    采用 → 配置 → 扩展 → 发明（Adopt → Profile → Extend → Invent）

L4  基础建设 / 阶段路线图（Foundation / Phase Roadmap）
    当前 P1 → P6 等有边界的建设周期

L5  契约 / 规范 / 配置规范（Contracts / Specifications / Profiles）
    规范知识、收录、迁移、人类界面、智能体访问、协作……

L6  工作项 / 实现（Work Items / Implementation）
    Issue / PR / 实验 / 迁移 / 收录批次
```

低层工作不能反过来静默改写高层使命。高层原则也不能替代低层可执行契约（Contract）。

## 12. P1–P6 的正确位置

P1–P6 **不是整个 InteropAtlas 的生命周期或最终路线图（Roadmap）**。

它是 2026-09-02 知识工作空间 / 视角（Knowledge Workspace / Perspective）方向重大升级之后，为避免直接凭直觉重构项目而启动的第一轮 **V1 基础建设 / 架构重新验证周期（V1 Foundation / Architecture Revalidation Cycle）**：

```text
早期 InteropAtlas / 参考实现模型（Reference Implementation Model）
        ↓
P1  设计原则（Design Principles）
        ↓
P2  既有先例 / 标准研究（Prior-Art / Standards Research）
        ↓
P3  当前状态审计（Current-State Audit）
        ↓
P4  V1 架构 / 路线图重置（Architecture / Roadmap Reset）
        ↓
P5  真实数据实验 / 压力测试（Real-data Experiments / Stress Tests）
        ↓
P6  V1 实现 + 迁移 + 持续收录（Implementation + Migration + Continuous Intake）
        ↓
V1 成为可运行基础（Operating Foundation）
        ↓
长期知识地图成长 / 工作空间 / 个性化 / 人与智能体演化
```

P6 完成只意味着新方向获得可信的运行基础，不意味着 InteropAtlas 完成。

## 13. 当前 V1 与长期愿景的关系

当前 V1 应优先完成那些未来很难绕开的基础能力：

- 稳定的规范身份 / 契约（Canonical Identity / Contract）；
- 证据 / 来源追踪 / 明确未知边界（Evidence / Provenance / Explicit Unknown Boundaries）；
- 安全、可持续的收录（Intake）；
- 旧模型 → V1 迁移（Legacy → V1 Migration）；
- 明确选择 / 投影（Selection / Projection）边界的人类工作空间（Human Workspace）；
- 人与智能体（Human + Agent）共享结构化访问；
- 候选写入（Candidate Write）与规范接受（Canonical Acceptance）分离；
- 可验证、可回滚、可演化的运行机制。

长期方向——个人知识空间（Personal Knowledge Space）、动态个人视角（Personal Perspective）、表达转换（Representation Transformation）、更多工作空间（Workspace）、知识代谢（Knowledge Metabolism）、匹配（MATCH）、人与智能体共享工作空间（Human + Agent Shared Workspace）——应从现在开始保留架构空间，但不能为了未来想象而过早冻结模式（Schema）。

## 14. 项目研究方法

InteropAtlas 对新问题默认采用：

> **采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**

研究不是为了证明当前想法正确，而是同时追求：

- **验证（Validation）**：前人是否已有成熟理论 / 标准 / 实践；
- **纠偏（Correction）**：当前直觉在哪里会失败；
- **认知增量（Cognitive Gain）**：前人研究能否带来此前没有想到的新问题和方向。

推荐研究链：

```text
前人问题
→ 前人方案
→ 为什么这样设计
→ 后来发生了什么
→ 失败 / 局限 / 反例
→ 当年技术条件
→ 2026 年条件变化
→ AI / 智能体 / 现代信息检索 / 知识图谱
  （AI / Agent / Modern IR / Knowledge Graph）带来的新可能
→ 对 IA 的启发
→ 新研究问题
```

## 15. 信息损失与可恢复性

从现实进入知识系统，再进入个人注意力和具体表达，会连续发生信息损失：

```text
现实（Reality）
→ 收集（Collection）
→ 建模（Modeling）
→ 选择（Selection）
→ 投影（Projection）
→ 表达（Representation）
→ 感知 / 行动（Perception / Action）
```

InteropAtlas 不追求所有表达（Representation）无损，而追求**任务适配 + 关键语义可恢复**。

身份（Identity）、来源追踪（Provenance）、证据（Evidence）、范围（Scope）、事实 / 推断边界（Fact / Inference Boundary）、关键关系与明确未知，不应因为生成了更易读的表达而被静默抹除。

## 16. 开放性不仅是许可证

InteropAtlas 的开放性至少包括：

- **开放知识（Open Knowledge）**：公共知识可复用；
- **开放证据（Open Evidence）**：结论可追溯；
- **开放访问（Open Access）**：人和机器均可访问；
- **开放贡献（Open Contribution）**：多人、多智能体可参与；
- **开放表达（Open Representation）**：未来可以产生新的工作空间 / 投影；
- **开放演化（Open Evolution）**：项目可以根据研究和真实使用改变自己；
- **可互操作的个人空间（Interoperable Personal Space）**：长期避免把个人视角锁死在单一软件或服务中。

开放贡献不意味着所有贡献者拥有同等规范权威（Canonical Authority）。身份（Identity）、证据（Evidence）、审查（Review）、治理（Governance）和权限边界仍然必须明确。

## 17. 长期成功标准

InteropAtlas 的成功不应只用“收录了多少标准”衡量。

更重要的问题包括：

- 方案空间覆盖率（Solution-space Coverage）是否持续扩大；
- 证据 / 来源追踪（Evidence / Provenance）是否足够可信；
- 人 / 智能体是否能解决真实互操作问题；
- 是否能发现原本看不到的方案、关系和缺口；
- 是否能让贡献重新进入知识地图，形成正反馈；
- 是否能让同一知识在不同任务中获得合适表达；
- 是否允许个人拥有自己的认知窗口，同时保留完整公共世界；
- 是否能主动抵抗不透明个性化和信息茧房；
- 是否能在不破坏规范事实（Canonical Truth）的前提下持续产生新的工作空间；
- 是否能让真实使用反向改进本体模型（Ontology）、收录（Intake）、选择（Selection）与产品设计。

## 18. 接下来读什么（Read Next）

理解项目长期方向时建议按以下顺序：

1. [`README.md`](../README.md) — 项目入口；
2. 本文 — 总体设计（Master Design）；
3. [`知识哲学与原则`](knowledge-philosophy-and-principles.zh-CN.md) — 哲学与长期不变量；
4. [`公共共同体与个人知识空间`](public-commons-and-personal-knowledge-space.zh-CN.md) — 公共知识与个人认知空间；
5. [`知识工作空间设计原则`](knowledge-workspace-design-principles.zh-CN.md) — 选择 / 投影 / 工作空间基线；
6. [`长期路线图`](interopatlas-long-term-roadmap.zh-CN.md) — 长期路线与当前基础建设周期；
7. [`项目状态（PROJECT_STATE.md）`](../PROJECT_STATE.md) — 当前施工断点；
8. 当前 Issue / 契约（Contract）/ 规范（Specification）— 具体工作。

## 19. 设计判断顺序

面对未来重大设计问题，优先问：

1. 这是否仍然服务于 InteropAtlas 的公共知识基础设施使命？
2. 这是公共事实、个人状态、选择规则、投影还是表达？
3. 当前人 / 智能体的真实任务是什么？
4. 什么知识应该进入注意力？为什么？
5. 哪些维度和关系需要暴露？
6. 什么表达形式 / 工作空间（Representation / Workspace）最适合当前认知任务？
7. 个性化是否透明、可逆，并允许回到公共世界？
8. 什么信息会丢失？能否恢复？
9. 真实使用是否证明需要改变本体模型 / 契约（Ontology / Contract）？
10. 前人是否已经解决过？能否采用 / 配置 / 扩展（Adopt / Profile / Extend），而不是发明（Invent）？
