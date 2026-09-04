# InteropAtlas 知识哲学与原则 v2.0

<!-- InteropAtlas Document Metadata v0
Document Status: active philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T02:30:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文保存 InteropAtlas 最不应该因为某个页面、模式（Schema）、智能体（Agent）或阶段计划而丢失的产品哲学，并将“产品哲学”与由其派生的“产品与建设原则”明确分层。具体架构以总体设计（Master Design）和各 V1 契约（Contract）为准。
>
> 这些思想并非被假定为凭空发明。其知识共同体（Knowledge Commons）、Memex / 超文本（Hypertext）、自适应超媒体（Adaptive Hypermedia）、多重表达（Multiple Representation）、可解释 / 可控个性化（Explainable / Controllable Personalization）等思想来源，以及 IA 对这些思想的继承与重新组合关系，见 [`InteropAtlas 思想谱系与产品哲学扩展阅读`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)。

---

# 第一部分：产品哲学（Product Philosophy）

## 核心哲学：知识属于公共共同体，视角属于个人

> **知识属于公共共同体。视角属于个人。**  
> **Knowledge belongs to the commons. Perspective belongs to the individual.**

这不是两条彼此独立的口号，而是同一个产品哲学的两个相互依存的方面。

**知识世界（Knowledge World）具有公共性。** 人类已经形成的事实、证据、关系、标准、规范、方法、实现、成熟先例（Prior Art）与历史，应尽可能成为开放、可发现、可追溯、机器可读、可验证、可复用、可长期演化的公共知识基础设施。InteropAtlas 首先服务于这个共同世界，而不是为某个单独用户、组织、智能体（Agent）或客户端建立一套私有事实世界。

**知识视角（Perspective）具有个人性。** 公共事实可以共享，但注意力、目标、背景知识、兴趣、任务、时间预算和认知方式不能被统一规定。不同的人和智能体可以从同一个公共知识世界中选择、强调、组织和投影不同的部分。个人视角不是用私人事实覆盖公共事实，而是从共同世界形成适合当前主体和情境的观察窗口。

因此，InteropAtlas 不在“公共”与“个人”之间做折中，而是明确区分：**公共的应该公共，个人的应该个人。** 公共知识越完整、开放和可复用，个人越有条件形成真正属于自己的视角；个人对知识的使用与创造，也可以反过来扩充公共知识世界。

### 为什么：把创造能力留给真正尚未解决的问题

这套哲学背后有一个更深的动机：**人类的注意力与创造能力是有限的（Human attention and creative capacity are scarce）。**

如果一个问题已经被前人解决，但已有知识因为分散、封闭、不可发现、不可理解或不可复用而无法被后来者利用，人类就会不断把有限的创造性注意力重新投入已经解决过的问题。

InteropAtlas 希望降低已有知识的发现、理解、验证、连接和复用成本，让更多创造力进入真正尚未解决的问题。

```text
人类的创造能力是有限的
（Human creative capacity is scarce）
            ↓
已有知识应该尽可能可发现、可理解、可复用
（Knowledge should remain discoverable and reusable）
            ↓
看清人类已经解决了什么
（Map what humanity already knows）
            ↓
暴露真正尚未解决的问题
（Expose the real open gaps）
            ↓
把创造力投入真正仍需创造之处
（Create where creation is still needed）
```

这是一项价值方向，而不是关于所有知识产权制度、商业模式或创新行为的普遍因果定律。InteropAtlas 不要求所有实现、组织或创作者放弃私有权利，也不把专有方案（Proprietary）自动等同于低价值；它关注的是尽可能降低人类已有互操作知识的发现、理解、验证和复用成本，并如实记录不同方案的开放性（Openness）、权威性（Authority）、许可证（License）、可携带性（Portability）与互操作性（Interoperability）边界。

## 核心哲学的动态展开：知识流动模型（Knowledge Flow Model）

如果“知识属于公共共同体，视角属于个人”描述的是知识世界的静态关系，那么知识流动模型描述的就是同一哲学在时间与使用过程中的动态展开。

> **知识不应该只是被保存。知识应该流动。**  
> **Knowledge should flow.**

InteropAtlas 将这种流动概括为六个彼此连接、最终闭环的动作：

```text
发现（Discover）
      ↓
连接（Connect）
      ↓
传递（Transmit）
      ↓
转化（Transform）
      ↓
复用（Reuse）
      ↓
创造（Create）
      ↓
新的知识进入公共共同体（Commons）
      ↺
```

这不是一条要求所有知识严格依次通过六个步骤的流水线，而是一张知识运动的概念地图。六个动作可以并行、往返、跳跃，也可以由个人、共同体、组织、软件或智能体完成。它们表达的是知识从公共世界进入具体视角、被理解和使用、产生新创造，再重新进入公共世界的整体循环。

### 发现（Discover）——让已有知识重新可见

发现回答：**人类已经知道什么？**

很多重复发明并不是因为知识从未存在，而是因为已有知识无法被后来者找到。InteropAtlas 应让标准、成熟先例、方法、实现、证据、历史与开放缺口尽可能可发现，并坚持 Prior Art First：在创造之前，先确认人类是否已经解决过相同或相近的问题。

### 连接（Connect）——让知识从条目变成世界

连接回答：**我们已经知道的东西之间是什么关系？**

孤立的一千个标准页面仍然是一千座知识孤岛。InteropAtlas 应连接标准、问题、能力、场景、实现、组织、证据、替代方案、依赖关系与历史演化，使知识从目录逐渐形成 Atlas。

发现与连接的重心更靠近公共知识世界（Commons）：它们帮助人类看清已经存在的知识及其结构。

### 传递（Transmit）——让知识跨越主体、系统与时间

传递让知识能够跨越人与人、组织与组织、系统与系统、文化与文化以及世代与世代。

保存（Preservation）在这里具有重要价值，但保存不是终点；保存是知识能够跨越时间继续被发现、理解和使用的条件之一。

### 转化（Transform）——让知识跨越表达与认知边界

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

同一份规范知识（Canonical Knowledge）可以根据不同主体、任务和认知方式，被投影为文字、图像、百科式浏览（Wiki / Browse）、单对象文章（Article）、时间线（Timeline）、关系图（Graph）、比较（Compare）、音频、视频、交互解释、模拟（Simulation）、游戏（Game）或面向智能体（Agent）的结构化表达。

因此，转化不是简单的格式转换，也不意味着不同媒介各自维护一套事实。更理想的方向是：

```text
Canonical Knowledge
        ↓
Perspective / Context
        ↓
Projection
        ↓
Representation
Article / Graph / Image / Audio / Video / Simulation / Game / Agent / ...
```

**表达应适应认知（Representation should adapt to cognition）** 是这一能力的重要要求：不存在一种对所有人、所有任务都最好的表达形式。文字可以是高压缩、高可检索的默认媒介，但 InteropAtlas 应坚持**文字优先，而非只有文字（text-first, not text-only）**。

传递与转化共同构成公共知识世界与具体个人视角之间的重要桥梁：前者让意义跨越主体、系统和时间，后者让意义跨越媒介、形式和认知方式。

### 复用（Reuse）——让已有知识成为后来工作的基础

知识不应该只能被阅读、引用和保存。它还应该能够被采用、组合、配置、实现、扩展并进入新的任务。

复用意味着后来者能够站在已有成果之上，而不是因为知识不可用而重新从零开始。它与 InteropAtlas 的建设方法 **Adopt → Profile → Extend → Invent** 直接相连。

### 创造（Create）——把知识继续推向未知空间

> **保存知识不是终点。知识最终应该帮助新的创造发生。**  
> *Preservation is not the endpoint; knowledge should ultimately enable new creation.*

我们把知识开放出来，最终不是为了无限保存知识，而是为了让更多人能够站在已有知识之上继续创造。

创造可以产生新的知识、方法、实现、规范、标准、作品、经验或新的问题。它们经过证据、来源追踪和治理后，又可以重新进入公共知识世界，成为下一轮发现、连接、传递、转化、复用与创造的基础。

因此，知识流动模型最终不是从 Commons 单向走向 Individual，而是：

```text
COMMONS
   ↓
Discover + Connect
   ↓
Transmit + Transform
   ↓
Reuse + Create
   ↓
INDIVIDUAL / CONCRETE CONTEXT
   ↓
New Knowledge / New Creation
   ↓
COMMONS
   ↺
```

这里的“偏公共”与“偏个人”描述的是重心，而不是所有权边界。个人同样可以发现和连接知识，共同体同样可以复用和创造。真正重要的是：**公共知识为个人视角和创造提供基础，个人与具体情境中的创造又能够反过来扩充公共知识。**

### 与知识代谢（Knowledge Metabolism）的区别

知识流动模型描述“知识如何跨越边界并进入下一次创造”；知识代谢描述知识在长期生命周期中如何被摄取、应用、提炼、衰减和重新激活。二者相关，但不是同一个模型。

长期继续研究知识代谢：

```text
收集（Collect）
→ 理解（Understand）
→ 整合（Integrate）
→ 应用（Apply）
→ 创造（Create）
→ 提炼（Distill）
→ 归档 / 压缩 / 遗忘（Archive / Compact / Forget）
→ 重新激活（Reactivate）
```

公共知识基础设施中的“遗忘”必须谨慎。**已废弃（Deprecated）≠ 没有价值，已被取代（Superseded）≠ 错误。** 历史知识可能在特定上下文（Context）下重新成为最相关的知识。公共知识生命周期（Lifecycle）与个人注意力生命周期（Attention Lifecycle）必须区分。

---

# 第二部分：产品与建设原则（Product & Construction Principles）

以下内容不再与核心产品哲学并列。它们回答的是：为了让上述哲学和知识流动真正成立，InteropAtlas 在产品、知识、架构和项目建设中必须遵守什么。

## 1. 个性化必须透明、可控、可逆（Personalization must be transparent, controllable, and reversible）

个性化不是“猜你喜欢”。个人视角不能篡改公共事实，也不能成为不可解释的信息黑箱。

系统应尽可能让用户知道为什么某条知识出现或被弱化、当前使用了什么视角 / 上下文（Perspective / Context）、如何改变或关闭这些规则、如何回到公共知识地图（Public Atlas），以及如何主动探索当前兴趣之外的知识。

信息茧房不是一个可以留到产品末期再处理的副作用，而是个人知识空间（Personal Knowledge Space）的设计约束。

## 2. 地图优先，而不是人类优先或智能体优先（Atlas-first, not Human-first or Agent-first）

人（Human）和智能体（Agent）都是知识世界的参与者和访问者。

项目不能为了人类界面（Human UI）建立一套事实，又为了智能体建立另一套事实。它们应共享规范知识（Canonical Knowledge）、证据（Evidence）、来源追踪（Provenance）和明确的未知边界，只在访问、选择、投影、表达与权限上不同。

## 3. 先选择，再呈现（Selection before presentation）

一个漂亮界面无法修复错误的知识选择。

在问“页面怎么设计”之前，先问：当前任务是什么；什么知识应该进入注意力；哪些维度与关系需要暴露；哪种表达形式（Representation）最合适；用户 / 智能体需要执行什么操作。

## 4. 工作空间是知识操作空间（Workspace is a knowledge operation space）

工作空间（Workspace）不只是一个视图（View）。表达形式（Representation）决定“看到什么样子”，工作空间还决定“在这种认知方式下能够做什么”。时间线、关系图、比较、证据、模拟等形式的价值，来自它们支持不同的认知任务和操作。

## 5. 先有证据，再有断言（Evidence before assertion）

InteropAtlas 应尽可能保持现实（Reality）、来源（Source）、证据（Evidence）、事实（Fact）、推断（Inference）、评估（Assessment）与建议（Recommendation）可区分。

智能体输出（Agent Output）和生成视图（Generated View）不会因为读起来流畅就自动成为规范事实（Canonical Fact）。

## 6. 可恢复性优先于虚假的完整性（Recoverability over false completeness）

知识在选择、投影和表达时可以发生有意识的信息损失，但不允许为了方便显示而静默破坏更丰富的规范知识（Canonical Knowledge）、证据、来源追踪、范围（Scope）和身份（Identity）。明确的 `unknown` / `not_recorded` 比伪造完整性更好。

## 7. 真实使用塑造本体模型（Real use shapes the ontology）

InteropAtlas 不应先设计一个理论上完美的世界模型，再要求现实服从它。真实查询、真实工作流、真实收录（Intake）和真实失败应该持续暴露模型缺口。只有当问题被证明确实存在，并经过既有先例 / 标准（Prior Art / Standards）检查后，才决定是否改变模型。

## 8. 采用 → 配置 → 扩展 → 发明（Adopt → Profile → Extend → Invent）

不要因为一个问题“看起来新”就自己发明。

优先寻找已经存在的标准、理论、协议、知识模型、交互研究和成熟产品实践。研究既用于验证，也用于纠偏和获得认知增量。

**这条原则同样约束 InteropAtlas 自己。** 当 IA 设计规范模式（Canonical Schema）、关系（Relation）、API、智能体访问（Agent Access）、人类界面（Human Interface）、治理、协作机制、数据格式、个人视角（Personal Perspective）或新的规范（Specification）时，必须优先调查和采用现有标准与成熟先例；只有它们经过真实场景验证仍无法满足需求时，才依次考虑配置（Profile）、扩展（Extend），最后才发明（Invent）。

IA 不应一边绘制人类的互操作方案空间，一边因为不了解既有先例（Prior Art）而制造新的互操作孤岛。

## 9. 映射已解决空间，暴露未解决空间（Map the solved space, expose the unsolved space）

InteropAtlas 的目的不止是描述已经存在的标准。完整映射标准、成熟先例、方法、实现、组织、能力、场景与证据的一个重要结果，是让“已经解决”与“仍未解决”之间的边界逐渐可见。

当真实互操作需求缺乏成熟标准、只有割裂或封闭的成熟先例、存在多个互不兼容的实现，或现有方案存在明显的开放性 / 可携带性 / 互操作性缺口时，IA 应把它识别为可研究的开放缺口（Open Gap），而不是立即宣布需要创造一项 IA 标准。

```text
Map existing Solution Space
        ↓
Identify interoperability need
        ↓
Mature open standard exists?
   ├─ yes → promote / adopt / connect
   └─ no
        ↓
Mature prior art exists?
        ↓
Compare / validate / distill
        ↓
Confirm real Open Gap
        ↓
Only when necessary → Specification / Standard
        ↓
Back into the Atlas
```

**发现 Gap ≠ 马上制定 IA 标准。**

---

## 一句话总结

InteropAtlas 的产品哲学可以压缩为一个对立统一的核心命题：

> **知识属于公共共同体，视角属于个人。**

它的动态展开是一个持续循环：

> **发现 → 连接 → 传递 → 转化 → 复用 → 创造 → 公共共同体 ↺**

而本文件第二部分的原则，则负责约束 InteropAtlas 如何在现实建设中不偏离这套哲学。
