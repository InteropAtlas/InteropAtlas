# InteropAtlas Master Design v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active master design
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T19:53:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Active Master Design（当前项目上位设计基线）
>
> Purpose: 回答 InteropAtlas **是什么、为什么存在、长期要成为怎样的系统、各层之间是什么关系，以及当前 P1–P6 Foundation Cycle 在长期路线中的位置**。
>
> This document is intentionally above implementation architecture, current phase plans and individual Specifications. It does not replace them.

## 1. InteropAtlas 是什么

InteropAtlas 是一个面向全人类的、开放、机器可读、可追溯、可持续分析与演化的 **Interoperability Solution Space（互操作方案空间）公共知识基础设施**。

它试图持续连接人类已经用于解决互操作问题的：

- Standards / Specifications / Protocols / Profiles / Interfaces / Formats；
- Mature Prior Art / Precedents；
- Methods / Guidelines / Frameworks；
- Implementations / Tools / Services；
- Organizations / Governance actors；
- Capabilities / Needs / Scenarios；
- Relations / Events / Context；
- Evidence / Sources / Provenance；
- Assessments / Open Gaps；
- 以及未来经研究和真实使用证明有必要纳入的其他知识类型。

InteropAtlas 不是单纯的标准目录、网站、知识图谱产品、Agent 数据库、PKM 软件或推荐系统。这些都可能成为它的组成部分、访问方式或投影，但都不是项目本身。

> **Atlas-first：核心资产是共享、可验证、可演化的知识世界；Human、Agent、API、网站和未来界面都是访问与操作这个世界的方式。**

## 2. 四条长期产品哲学

### Knowledge belongs to the commons.

**知识属于公共共同体。**

InteropAtlas 的公共知识层应尽可能成为全人类可访问、可复用、可验证、可扩展的基础设施，而不是某个个人、Agent 或产品的私有事实世界。

### Perspective belongs to the individual.

**视角属于个人。**

完整知识世界可以共享，但不同人的目标、工作、兴趣、背景、已有知识、当前状态和注意力并不相同。个人应该能够拥有自己的动态知识视角，而不需要复制或篡改公共事实。

### Representation should adapt to cognition.

**表达应适应认知。**

知识没有唯一正确的呈现形式。同一份知识可以根据当前的人、任务和认知方式，被表达为文字、Wiki/Browse、Timeline、Graph、Compare、Matrix、Map、图像、音频、视频、交互解释、Simulation、Game 或未来尚未出现的形式。

### Personalization must remain reversible and transparent.

**个性化必须可逆、透明、可检查。**

个性化不能把公共知识世界替换成黑箱信息流。用户应能够理解为什么某些知识被选择、强调或弱化，并能够退出个人化视角、回到公共 Atlas、扩大视野或主动探索当前 Perspective 之外的重要知识。

## 3. 三个世界：Shared → Personal → Experience

InteropAtlas 的长期形态可以用三个相互连接、但必须保持边界的世界理解：

```text
                    InteropAtlas
                         │
        ┌────────────────┴────────────────┐
        │                                 │
  Shared Knowledge World            Public Access
  公共知识世界                       Search / Browse / API
        │                                 │
        └──────── Canonical Knowledge ────┘
                         │
                         ↓
                Personal Knowledge Space
                    个人知识空间
                         │
        User State / Intent / Context / History
        Knowledge State / Interest / Attention
        Representation Preference / Accessibility
                         │
                         ↓
             Perspective / Selection / Ranking
                         │
                         ↓
                    Projection
                         │
                         ↓
                Experience / Workspace
                    体验与操作空间
                         │
      Article / Wiki / Graph / Timeline / Compare
      Image / Video / Simulation / Interactive / Game
                         │
                    Human / Agent
```

### 3.1 Shared Knowledge World

公共层回答的是：

- 人类已经知道什么？
- 某对象是什么？
- 它和其他对象有什么关系？
- 谁发布、维护或实现它？
- 什么证据支持某个陈述？
- 什么是 Fact，什么是 Assessment？
- 哪些信息未知、未记录、有争议、过时或已被替代？

公共事实原则上不应因为“谁在看”而改变。

### 3.2 Personal Knowledge Space

个人层不应复制一份私人 Canonical Atlas，而应建立在公共知识之上的**个人认知窗口、状态与选择层**。

它未来可能考虑：

- 当前任务与目标；
- 当前职业/项目/学习主题；
- 已知与未知；
- 最近使用与长期兴趣；
- 时间与环境上下文；
- 用户主动声明的关注与回避；
- 信息密度偏好；
- 文字、图像、音视频、交互等表达偏好；
- Accessibility 需要；
- 用户愿意投入的时间与深度；
- 需要主动跳出既有兴趣的探索模式。

这些信号属于 Personal Perspective / Personal State，不应被错误提升为公共事实。

### 3.3 Experience / Workspace World

最终呈现不只由知识本身决定，而可能由以下组合共同决定：

```text
Knowledge × Task × Person × Context × Cognitive Preference
                         ↓
                  Representation
                         +
                     Operations
                         ↓
                     Workspace
```

Workspace 因此不是“页面模板”，而是针对认知任务形成的**知识观察与操作空间**。

## 4. 稳定知识，流动表达

> **Knowledge is stable; representations are fluid.**

InteropAtlas 应尽量让底层知识的 Identity、Evidence、Provenance、Relation、Lifecycle 与明确未知边界保持稳定和可恢复，同时允许上层表达持续演化。

```text
Canonical Knowledge
        ↓
Lifecycle / Context signals
        ↓
Perspective / Selection
        ↓
Selected Knowledge
        ↓
Projection
        ↓
Representation / Workspace
        ↓
Interaction
        ↓
Human / Agent
```

这是一套概念边界，不要求每一层都成为独立服务、数据库或 Schema 对象。

### Perspective

回答：**现在什么知识值得进入注意力？**

Perspective 可以是公共查询视角，也可以是个人认知视角。长期必须明确区分至少：

- Knowledge Perspective：针对知识空间本身的条件、Scope、时间、关系、Evidence、Lifecycle 等选择；
- Personal Perspective：针对某个人当前状态、目标、兴趣、知识水平、认知偏好形成的动态选择与强调。

### Projection

回答：**对于已经选中的知识，当前任务需要暴露哪些维度、关系与结构？**

### Representation / Workspace

回答：**这些知识应该怎样被表达，以及用户/Agent 在这里能够做什么？**

Representation 是表达；Workspace 是表达加上与认知任务匹配的操作能力。

## 5. 知识操作空间，而不是固定网站

InteropAtlas 的长期产品不应该是一组被永久固定的页面，而应该是一套共享同一知识底座的 **Knowledge Operation Spaces（知识操作空间）**。

基础 Workspace 家族包括但不限于：

- Wiki / Browse：搜索、分类/Facet 深入、链接导航；
- Single Object / Article：线性理解一个对象；
- Timeline：历史、版本、代际、事件与演化；
- Graph / Ecosystem：关系、组织、标准、实现与生态；
- Compare：可比候选的并行检查；
- Evidence / Verification：来源、Provenance、断言边界、未知状态；
- Outline / Matrix / Map；
- Interactive Explanation / Simulation；
- Audio / Video；
- Game-like representation；
- 未来尚未识别的新型表示。

新 Workspace 不因“看起来新颖”而成立。它应证明自己能够暴露其他 Workspace 难以表达的意义、降低认知负担或提供新的有效操作。

## 6. Human 与 Agent 共享同一个知识世界

Human-first 和 Agent-first 都不是最终定位。最终原则是 **Atlas-first**。

```text
                  Canonical Knowledge
                         ↑↓
                   Perspective
                         ↑↓
                    Projection
                         ↑↓
                     Workspace
                    ↙         ↘
                 Human       Agent
                    ↖         ↗
                 shared state
```

Human 与 Agent 应尽可能使用同一 Canonical Knowledge、Evidence 和明确的选择/投影边界。

Human 可能 Browse / Read / Compare / Verify；Agent 可能 Query / Traverse / Filter / Retrieve Evidence / Compose / Explain / Operate Workspace。

长期目标不是让 Agent 在另一个黑箱里重新生成一套世界，而是让 Human 与 Agent 可以在同一个可解释的知识空间和 Workspace 状态上协作。

Agent 输出、推理和建议仍然不自动等于 Canonical Fact。写入公共知识必须经过明确的 Candidate → Validation → Acceptance / Review 边界。

## 7. Atlas 的成长循环

InteropAtlas 不是“先把世界收录完，再开始使用”的项目。知识模型和产品都应该通过真实使用持续被检验。

长期循环：

```text
KNOW
建立、验证、连接知识
  ↓
USE
Human / Agent 使用 Atlas 解决真实问题
  ↓
DISCOVER
发现知识缺口、模型缺口、错误、过时信息和新方案
  ↓
CONTRIBUTE
研究、验证并把新知识反馈给 Atlas
  ↓
KNOW
```

未来可以进一步发展：

```text
MATCH
问题 ↔ 方案
人 ↔ 知识
人 ↔ 人
组织 ↔ 能力
需求 ↔ 标准 / 实现 / 方法
```

MATCH 不应退化为不透明的商业推荐，而应尽可能基于可解释的知识关系、Context 与用户控制。

## 8. 真实使用塑造 Ontology

InteropAtlas 不应坐在设计阶段试图一次性把世界分类完。

```text
真实问题 / Query / Workflow
        ↓
使用当前 Atlas
        ↓
发现表达或查询缺口
        ↓
检查 Prior Art / Standards
        ↓
确认是否重复出现、是否为真实结构性问题
        ↓
Adopt / Profile / Extend / Invent
        ↓
必要时演化 Canonical Model
```

因此：

> **让真实查询与真实贡献塑造 Ontology，而不是让预设 Ontology 限制现实。**

## 9. Knowledge Metabolism：重要方向，但保持研究边界

公共知识基础设施不能简单复制个人 PKM 的“删除旧笔记”逻辑；一个过时标准在历史设备、法律、兼容性或研究场景下仍可能是唯一正确的信息。

但 IA 同样不能假设所有知识永远处于同一注意力和计算优先级。

需要长期研究：

```text
Collect
→ Understand
→ Integrate
→ Apply
→ Create
→ Distill
→ Down-rank / Archive / Compact / Forget
→ Reactivate when context requires
```

必须区分：

- Validity；
- Freshness / Staleness；
- Usage；
- Relevance；
- Historical Value；
- Authority；
- Lifecycle。

**低当前权重 ≠ 低真实性 ≠ 低历史价值。**

Knowledge Metabolism 当前仍是需要研究和验证的上位方向，不应未经验证直接变成统一 `weight`、自动删除算法或稳定 Schema。

公共知识 Lifecycle 与个人 Attention Lifecycle 也必须分开：公共 Atlas 负责保存可恢复的历史与证据；个人空间负责决定什么现在值得进入某个人的注意力。

## 10. 个性化的边界：反信息茧房是设计问题

Personalization 是长期核心方向，但必须满足：

1. **Public baseline remains available**：任何人都能回到非个人化的公共 Atlas；
2. **Explainability**：重要选择、排序和弱化应尽可能说明依据；
3. **Reversibility**：Personal Perspective 可关闭、切换、重置；
4. **User agency**：用户可以主动定义目标、偏好和探索方式；
5. **Perspective escape**：系统应允许“跳出当前视角”，探索远离既有兴趣但重要的知识；
6. **Fact isolation**：个性化改变注意力和表达，不改变公共事实；
7. **Privacy boundary**：Personal State 不应默认进入公共 Canonical Knowledge；
8. **Interoperability**：未来个人状态、Perspective 与 Workspace 应优先考虑可携带、可导出、可组合，而不是锁死在单一客户端。

## 11. 项目的层级，不要再混淆

InteropAtlas 同时存在不同尺度的设计。它们必须明确分层：

```text
L0  Mission / Philosophy
    为什么存在；服务谁；什么不能轻易改变

L1  Master Design
    Shared / Personal / Experience、Atlas-first、长期产品形态

L2  Architecture
    Canonical / Lifecycle / Perspective / Projection / Workspace / Access

L3  Operating & Evolution Model
    KNOW → USE → DISCOVER → CONTRIBUTE；Adopt → Profile → Extend → Invent

L4  Foundation / Phase Roadmap
    当前 P1 → P6 等有边界的建设周期

L5  Contracts / Specifications / Profiles
    Canonical、Intake、Migration、Human Interface、Agent Access、Collaboration…

L6  Work Items / Implementation
    Issues / PRs / experiments / migrations / intake batches
```

低层工作不能反过来静默改写高层使命。高层原则也不能替代低层可执行 Contract。

## 12. P1–P6 的正确位置

P1–P6 **不是整个 InteropAtlas 的生命周期或最终 Roadmap**。

它是 2026-09-02 Knowledge Workspace / Perspective 方向重大升级之后，为避免直接凭直觉重构项目而启动的第一轮 **V1 Foundation / Architecture Revalidation Cycle**：

```text
早期 InteropAtlas / Reference Implementation model
        ↓
P1  Design Principles
        ↓
P2  Prior-Art / Standards Research
        ↓
P3  Current-State Audit
        ↓
P4  V1 Architecture / Roadmap Reset
        ↓
P5  Real-data Experiments / Stress Tests
        ↓
P6  V1 Implementation + Migration + Continuous Intake
        ↓
V1 becomes an operating foundation
        ↓
长期 Atlas Growth / Workspace / Personalization / Human+Agent evolution
```

P6 完成只意味着新方向获得可信的运行基础，不意味着 InteropAtlas 完成。

## 13. 当前 V1 与长期愿景的关系

当前 V1 应优先完成那些未来很难绕开的基础能力：

- 稳定 Canonical identity / contract；
- Evidence / Provenance / explicit unknown boundaries；
- 安全、可持续的 Intake；
- Legacy → V1 Migration；
- 明确 Selection / Projection 边界的 Human Workspace；
- Human + Agent 共享结构化访问；
- Candidate Write 与 Canonical acceptance 分离；
- 可验证、可回滚、可演化的运行机制。

长期方向——Personal Knowledge Space、动态 Personal Perspective、Representation Transformation、更多 Workspace、Knowledge Metabolism、MATCH、Human+Agent shared workspace——应从现在开始保留架构空间，但不能为了未来想象而过早冻结 Schema。

## 14. 项目研究方法

InteropAtlas 对新问题默认采用：

> **Adopt → Profile → Extend → Invent**

研究不是为了证明当前想法正确，而是同时追求：

- Validation：前人是否已有成熟理论/标准/实践；
- Correction：当前直觉在哪里会失败；
- Cognitive gain：前人研究能否带来此前没有想到的新问题和方向。

推荐研究链：

```text
前人问题
→ 前人方案
→ 为什么这样设计
→ 后来发生了什么
→ 失败 / 局限 / 反例
→ 当年技术条件
→ 2026 条件变化
→ AI / Agent / modern IR / Knowledge Graph 带来的新可能
→ 对 IA 的启发
→ 新研究问题
```

## 15. 信息损失与可恢复性

从现实进入知识系统，再进入个人注意力和具体表达，会连续发生信息损失：

```text
Reality
→ Collection
→ Modeling
→ Selection
→ Projection
→ Representation
→ Perception / Action
```

InteropAtlas 不追求所有 Representation 无损，而追求**任务适配 + 关键语义可恢复**。

Identity、Provenance、Evidence、Scope、Fact/Inference boundary、关键关系与明确未知不应因为生成了更易读的表达而被静默抹除。

## 16. 开放性不仅是许可证

InteropAtlas 的开放性至少包括：

- Open Knowledge：公共知识可复用；
- Open Evidence：结论可追溯；
- Open Access：Human 与 Machine 均可访问；
- Open Contribution：多人、多 Agent 可参与；
- Open Representation：未来可以产生新的 Workspace / Projection；
- Open Evolution：项目可以根据研究和真实使用改变自己；
- Interoperable Personal Space：长期避免把个人 Perspective 锁死在单一软件或服务中。

开放贡献不意味着所有贡献者拥有同等 Canonical authority。Identity、Evidence、Review、Governance 和权限边界仍然必须明确。

## 17. 长期成功标准

InteropAtlas 的成功不应只用“收录了多少标准”衡量。

更重要的问题包括：

- Solution-space coverage 是否持续扩大；
- Evidence / Provenance 是否足够可信；
- Human / Agent 是否能解决真实互操作问题；
- 是否能发现原本看不到的方案、关系和缺口；
- 是否能让贡献重新进入 Atlas，形成正反馈；
- 是否能让同一知识在不同任务中获得合适表达；
- 是否允许个人拥有自己的认知窗口，同时保留完整公共世界；
- 是否能主动抵抗不透明个性化和信息茧房；
- 是否能在不破坏 Canonical truth 的前提下持续产生新的 Workspace；
- 是否能让真实使用反向改进 Ontology、Intake、Selection 与产品设计。

## 18. Read Next

理解项目长期方向时建议按以下顺序：

1. `README.md` — 项目入口；
2. 本文 — Master Design；
3. `docs/knowledge-philosophy-and-principles-v1.0.zh-CN.md` — 哲学与长期不变量；
4. `docs/public-commons-and-personal-knowledge-space-v0.1.zh-CN.md` — 公共知识与个人认知空间；
5. `docs/knowledge-workspace-design-principles-v1.0.zh-CN.md` — Selection / Projection / Workspace 基线；
6. `docs/interopatlas-long-term-roadmap-v1.0.zh-CN.md` — 长期路线与当前 Foundation Cycle；
7. `PROJECT_STATE.md` — 当前施工断点；
8. 当前 Issue / Contract / Specification — 具体工作。

## 19. 设计判断顺序

面对未来重大设计问题，优先问：

1. 这是否仍然服务于 InteropAtlas 的公共知识基础设施使命？
2. 这是公共事实、个人状态、选择规则、投影还是表达？
3. 当前 Human / Agent 的真实任务是什么？
4. 什么知识应该进入注意力？为什么？
5. 哪些维度和关系需要暴露？
6. 什么 Representation / Workspace 最适合当前认知任务？
7. 个性化是否透明、可逆，并允许回到公共世界？
8. 什么信息会丢失？能否恢复？
9. 真实使用是否证明需要改变 Ontology / Contract？
10. 前人是否已经解决过？能否 Adopt / Profile / Extend，而不是 Invent？
