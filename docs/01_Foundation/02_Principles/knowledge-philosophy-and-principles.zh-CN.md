# InteropAtlas 知识哲学与原则 v2.1

<!-- InteropAtlas Document Metadata v0
Document Status: active philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T03:50:00+08:00
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

**人类的注意力与创造能力是有限的（Human attention and creative capacity are scarce）。** 如果一个问题已经被前人解决，但已有知识因为分散、封闭、不可发现、不可理解或不可复用而无法被后来者利用，人类就会不断把有限的创造性注意力重新投入已经解决过的问题。

InteropAtlas 希望降低已有知识的发现、理解、验证、连接和复用成本，让更多创造力进入真正尚未解决的问题：

```text
Map what humanity already knows
        ↓
Expose the real open gaps
        ↓
Create where creation is still needed
```

这是一项价值方向，而不是关于所有知识产权制度、商业模式或创新行为的普遍因果定律。InteropAtlas 不要求所有实现、组织或创作者放弃私有权利，也不把专有方案（Proprietary）自动等同于低价值；它关注的是降低人类已有互操作知识的发现、理解、验证和复用成本，并如实记录不同方案的开放性、权威性、许可证、可携带性与互操作性边界。

## 核心哲学的动态命题：知识流动，创造不息

如果“知识属于公共共同体，视角属于个人”描述的是知识世界的**结构**，那么它的动态命题描述的就是这个世界如何持续运动：

> **知识流动，创造不息。**  
> **Knowledge travels. Creation continues.**

最底层不需要六个同级阶段。这里真正需要区分的是两个基本运动：

1. **流动（Flow）**：让已经存在的知识跨越边界；
2. **创造（Create）**：让主体站在已有知识之上，跨越已知本身的边界，产生原本不存在的东西。

```text
Knowledge Commons
      ↓
     FLOW
      ↓
Individual / Perspective / Context
      ↓
    CREATE
      ↓
New Knowledge / New Creation
      ↓
Knowledge Commons
      ↺
```

因此，公共共同体（Commons）与个人（Individual）不是两个竞争的终点。公共知识为个人提供可以继承、理解和复用的基础；个人与具体情境中的创造，又可以反过来扩充公共知识。循环不断继续。

### 流动（Flow）：让已有知识跨越边界

知识流动不是单一动作，也不是固定流水线。此前使用的“发现 → 连接 → 传递 → 转化 → 复用”仍然重要，但它们不再被定义为五个必须依次发生的一级阶段，而是**知识跨越不同边界的典型机制**：

- **发现（Discover）**：跨越可见性的边界，让原本不可见或未知的已有知识重新进入注意力；
- **连接（Connect）**：跨越知识孤岛的边界，让对象、关系、证据、组织、场景和历史形成知识世界；
- **传递（Transmit）**：跨越人与人、组织、系统、文化和时代的边界；
- **转化（Transform）**：跨越语言、媒介、表达形式和认知方式的边界；
- **复用（Reuse）**：跨越使用情境的边界，让已有知识进入新的任务、组合、实现和扩展。

这组机制是开放的，而不是封闭枚举。未来如果发现其他重要的知识跨界机制，可以继续补充，而不需要改变模型的顶层结构。

其中，**转化（Transform）**包含一个重要判断：

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

同一份规范知识（Canonical Knowledge）可以根据不同主体、任务和认知方式，被投影为文字、图像、百科式浏览（Wiki / Browse）、文章（Article）、时间线（Timeline）、关系图（Graph）、比较（Compare）、音频、视频、交互解释、模拟（Simulation）、游戏（Game）或面向智能体（Agent）的结构化表达。

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

**表达应适应认知（Representation should adapt to cognition）** 是转化能力的重要要求。InteropAtlas 坚持**文字优先，而非只有文字（text-first, not text-only）**。

### 创造（Create）：跨越已知的边界

创造与前述机制存在一个根本差异：发现、连接、传递、转化和复用主要处理**已经存在的知识**；创造则面向**尚不存在的东西**。

> **保存知识不是终点。知识最终应该帮助新的创造发生。**  
> *Preservation is not the endpoint; knowledge should ultimately enable new creation.*

创造可以产生新的知识、方法、实现、规范、标准、作品、经验或新的问题。它们经过证据、来源追踪和治理后，又可以进入公共知识世界，成为下一轮知识流动与创造的基础。

因此，InteropAtlas 所追求的不是一个静态知识仓库，而是一个持续循环：

```text
已有知识 → 流动 → 个体 / 情境 → 创造 → 新知识 → 公共共同体 ↺
```

### 与知识代谢（Knowledge Metabolism）的区别

知识流动描述“已有知识如何跨越边界并进入下一次创造”；知识代谢描述知识在长期生命周期中如何被摄取、应用、提炼、衰减和重新激活。二者相关，但不是同一个模型。

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

公共知识基础设施中的“遗忘”必须谨慎。**已废弃（Deprecated）≠ 没有价值，已被取代（Superseded）≠ 错误。** 公共知识生命周期（Lifecycle）与个人注意力生命周期（Attention Lifecycle）必须区分。

---

# 第二部分：产品与建设原则（Product & Construction Principles）

以下内容不与核心产品哲学并列。它们回答的是：为了让上述哲学、知识流动和创造循环真正成立，InteropAtlas 在产品、知识、架构和项目建设中必须遵守什么。

## 1. 个性化必须透明、可控、可逆（Personalization must be transparent, controllable, and reversible）

个人视角不能篡改公共事实，也不能成为不可解释的信息黑箱。系统应尽可能让用户知道为什么某条知识出现或被弱化、当前使用了什么视角 / 上下文、如何改变或关闭这些规则，以及如何回到公共知识地图。

## 2. 地图优先，而不是人类优先或智能体优先（Atlas-first, not Human-first or Agent-first）

人（Human）和智能体（Agent）都是知识世界的参与者和访问者。它们应共享规范知识（Canonical Knowledge）、证据（Evidence）、来源追踪（Provenance）和明确的未知边界，只在访问、选择、投影、表达与权限上不同。

## 3. 先选择，再呈现（Selection before presentation）

一个漂亮界面无法修复错误的知识选择。在问“页面怎么设计”之前，先问当前任务是什么、什么知识应该进入注意力、哪些维度与关系需要暴露、哪种表达形式最合适。

## 4. 工作空间是知识操作空间（Workspace is a knowledge operation space）

工作空间（Workspace）不只是一个视图。表达形式决定“看到什么样子”，工作空间还决定“在这种认知方式下能够做什么”。

## 5. 先有证据，再有断言（Evidence before assertion）

InteropAtlas 应尽可能保持现实、来源、证据、事实、推断、评估与建议可区分。智能体输出和生成视图不会因为读起来流畅就自动成为规范事实。

## 6. 可恢复性优先于虚假的完整性（Recoverability over false completeness）

知识在选择、投影和表达时可以发生有意识的信息损失，但不允许为了方便显示而静默破坏更丰富的规范知识、证据、来源追踪、范围和身份。明确的 `unknown` / `not_recorded` 比伪造完整性更好。

## 7. 真实使用塑造本体模型（Real use shapes the ontology）

InteropAtlas 不应先设计一个理论上完美的世界模型，再要求现实服从它。真实查询、真实工作流、真实收录和真实失败应该持续暴露模型缺口。

## 8. 采用 → 配置 → 扩展 → 发明（Adopt → Profile → Extend → Invent）

优先寻找已经存在的标准、理论、协议、知识模型、交互研究和成熟产品实践。只有既有标准和成熟先例经过真实场景验证仍无法满足需求时，才依次考虑配置、扩展，最后才发明。

**这条原则同样约束 InteropAtlas 自己。** IA 不应一边绘制人类的互操作方案空间，一边因为不了解既有先例（Prior Art）而制造新的互操作孤岛。

## 9. 映射已解决空间，暴露未解决空间（Map the solved space, expose the unsolved space）

完整映射标准、成熟先例、方法、实现、组织、能力、场景与证据的一个重要结果，是让“已经解决”与“仍未解决”之间的边界逐渐可见。

**发现 Gap ≠ 马上制定 IA 标准。** 应先确认成熟开放标准与成熟先例是否存在，比较、验证并提炼之后，只有确认真实 Open Gap 且确有必要时，才进入新的 Specification / Standard。

---

## 一句话总结

InteropAtlas 的产品哲学由一组静态与动态命题共同表达：

> **知识属于公共共同体，视角属于个人。**  
> **知识流动，创造不息。**

前一句描述知识世界的结构；后一句描述它的运动。已有知识通过发现、连接、传递、转化、复用等方式跨越边界，进入个人视角与具体情境，推动新的创造；新的创造又可以进入公共共同体，成为下一轮流动的基础。

本文件第二部分的原则，则负责约束 InteropAtlas 如何在现实建设中不偏离这套哲学。