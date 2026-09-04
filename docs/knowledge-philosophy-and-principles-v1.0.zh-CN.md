# InteropAtlas 知识哲学与原则 v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-05T01:22:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文保存 InteropAtlas 最不应该因为某个页面、模式（Schema）、智能体（Agent）或阶段计划而丢失的产品哲学。具体架构以总体设计（Master Design）和各 V1 契约（Contract）为准。
>
> 这些原则并非被假定为凭空发明。其知识共同体（Knowledge Commons）、Memex / 超文本（Hypertext）、自适应超媒体（Adaptive Hypermedia）、多重表达（Multiple Representation）、可解释 / 可控个性化（Explainable / Controllable Personalization）等思想来源，以及 IA 对这些思想的继承与重新组合关系，见 [`InteropAtlas 思想谱系与产品哲学扩展阅读`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)。

## 1. 知识属于公共共同体（Knowledge belongs to the commons）

InteropAtlas 首先服务于全人类，而不是某个单独用户、组织、智能体（Agent）或客户端。

公共知识世界应尽可能开放、可追溯、机器可读、可复用、可长期演化。任何个性化（Personalization）都建立在这个公共世界之上，而不是取代它。

### 为什么：把创造能力留给真正尚未解决的问题

这条原则背后还有一个更深的动机：**人类的注意力与创造能力是有限的（Human attention and creative capacity are scarce）。**

如果一个问题已经被前人解决，但已有知识因为分散、封闭、不可发现、不可理解或不可复用而无法被后来者利用，人类就会不断把有限的创造性注意力重新投入已经解决过的问题。

InteropAtlas 希望减少这种由知识不可见与不可复用造成的重复发明，把更多创造力释放给真正尚未解决的问题。

```text
人类的创造能力是有限的
（Human creative capacity is scarce）
            ↓
已有知识应该尽可能可发现、可理解、可复用
（Knowledge should remain discoverable and reusable）
            ↓
知识属于公共共同体
（Knowledge belongs to the commons）
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

## 2. 视角属于个人（Perspective belongs to the individual）

公共事实可以共享，注意力不能被统一规定。

不同人的工作、目标、知识背景、兴趣、生活状态、时间预算和认知方式不同。系统应允许每个人形成自己的视角（Perspective），并允许视角随状态变化。

个人视角（Personal Perspective）是对公共知识的选择、强调和组织，不是用私人事实覆盖公共事实。

## 3. 表达应适应认知（Representation should adapt to cognition）

> **知识相对稳定，表达可以流动。**  
> *Knowledge is stable; representations are fluid.*

同一知识可以被表达为文字、图像、百科式浏览（Wiki）、时间线（Timeline）、关系图（Graph）、比较（Compare）、音频、视频、交互、模拟（Simulation）或游戏（Game）。不存在一种对所有人、所有任务都最好的表达形式（Representation）。

文字可以是高压缩、高可检索的默认媒介，但 InteropAtlas 应坚持**文字优先，而非只有文字（text-first, not text-only）**：当关键语义无法被文字充分表达，或其他媒介对当前认知任务明显更有效时，应允许更合适的形式。

## 4. 个性化必须可逆、透明、可检查（Personalization must remain reversible and transparent）

个性化不是“猜你喜欢”。

系统应尽可能让用户知道：

- 为什么某条知识出现；
- 为什么某条知识被弱化；
- 当前使用了什么视角 / 上下文（Perspective / Context）；
- 如何关闭或改变这些规则；
- 如何回到公共知识地图（Public Atlas）；
- 如何主动探索当前兴趣之外的知识。

信息茧房不是一个可以留到产品末期再处理的副作用，而是个人知识空间（Personal Knowledge Space）的设计约束。

## 5. 地图优先，而不是人类优先或智能体优先（Atlas-first, not Human-first or Agent-first）

人（Human）和智能体（Agent）都是知识世界的参与者和访问者。

项目不能为了人类界面（Human UI）建立一套事实，又为了智能体建立另一套事实。它们应共享规范知识（Canonical Knowledge）、证据（Evidence）、来源追踪（Provenance）和明确的未知边界，只在访问、选择、投影、表达与权限上不同。

## 6. 知识是为了创造，而不只是保存（Knowledge is for creation, not preservation alone）

> **我们把知识开放出来，最终不是为了保存知识，而是为了创造。**  
> *We open knowledge not merely to preserve it, but ultimately to enable creation.*

保存（Preservation）非常重要，但它是手段和基础，而不是终点。知识真正进入公共共同体之后，应能够被后来者发现、理解、验证、使用、组合和继续推进，使他们不必反复重新解决已经解决的问题，并能把有限的创造性注意力投入真正仍然未知、未解决、未被创造的空间。

因此知识的价值不仅在于被保存，还在于被：

```text
发现
→ 理解
→ 使用
→ 传播
→ 组合
→ 验证
→ 创造
→ 产生新知识
→ 重新进入知识地图
```

这个循环意味着：**保存知识服务于继续创造；开放知识服务于让更多人能够站在已有知识之上继续创造。**

因此 InteropAtlas 不应成为无限堆积材料的仓库。它要尽可能让已有知识成为下一次创造的基础。

## 7. 知识应该流动（Knowledge should flow）

长期研究知识代谢（Knowledge Metabolism）：

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

但公共知识基础设施中的“遗忘”必须谨慎。**已废弃（Deprecated）≠ 没有价值，已被取代（Superseded）≠ 错误。** 历史知识可能在特定上下文（Context）下重新成为最相关的知识。

公共知识生命周期（Lifecycle）与个人注意力生命周期（Attention Lifecycle）必须区分。

## 8. 先选择，再呈现（Selection before presentation）

一个漂亮界面无法修复错误的知识选择。

在问“页面怎么设计”之前，先问：

1. 当前任务是什么？
2. 什么知识应该进入注意力？
3. 哪些维度与关系需要暴露？
4. 哪种表达形式（Representation）最合适？
5. 用户 / 智能体需要执行什么操作？

## 9. 工作空间是知识操作空间（Workspace is a knowledge operation space）

工作空间（Workspace）不只是一个视图（View）。

表达形式（Representation）决定“看到什么样子”，工作空间还决定“在这种认知方式下能够做什么”。因此时间线（Timeline）、关系图（Graph）、比较（Compare）、证据（Evidence）、模拟（Simulation）等形式的价值，来自它们支持不同的认知任务和操作。

## 10. 先有证据，再有断言（Evidence before assertion）

InteropAtlas 应尽可能把以下层次保持可区分：

- 现实（Reality）；
- 来源（Source）；
- 证据（Evidence）；
- 事实（Fact）；
- 推断（Inference）；
- 评估（Assessment）；
- 建议（Recommendation）。

智能体输出（Agent Output）和生成视图（Generated View）不会因为读起来流畅就自动成为规范事实（Canonical Fact）。

## 11. 可恢复性优先于虚假的完整性（Recoverability over false completeness）

知识进入系统并不断被选择、投影和表达时会发生信息损失。

允许有损表达（Representation），但不允许为了方便显示而静默破坏更丰富的规范知识（Canonical Knowledge）、证据（Evidence）、来源追踪（Provenance）、范围（Scope）和身份（Identity）。

明确的 `unknown` / `not_recorded` 比伪造完整性更好。

## 12. 真实使用塑造本体模型（Real use shapes the ontology）

InteropAtlas 不应先设计一个理论上完美的世界模型，再要求现实服从它。

真实查询（Query）、真实工作流、真实收录（Intake）和真实失败应该持续暴露模型缺口。只有当问题被证明确实存在，并经过既有先例 / 标准（Prior Art / Standards）检查后，才决定是否改变模型。

## 13. 采用 → 配置 → 扩展 → 发明（Adopt → Profile → Extend → Invent）

不要因为一个问题“看起来新”就自己发明。

优先寻找几十年来已经存在的标准、理论、协议、知识模型、交互研究和成熟产品实践。研究既用于验证，也用于纠偏和获得认知增量。

**这条原则同样约束 InteropAtlas 自己。** 当 IA 设计规范模式（Canonical Schema）、关系（Relation）、API、智能体访问（Agent Access）、人类界面（Human Interface）、治理、协作机制、数据格式、个人视角（Personal Perspective）或新的规范（Specification）时，必须优先调查和采用现有标准与成熟先例；只有它们经过真实场景验证仍无法满足需求时，才依次考虑配置（Profile）、扩展（Extend），最后才发明（Invent）。

IA 不应一边绘制人类的互操作方案空间，一边因为不了解既有先例（Prior Art）而制造新的互操作孤岛。

## 14. 映射已解决空间，暴露未解决空间（Map the solved space, expose the unsolved space）

InteropAtlas 的目的不止是描述已经存在的标准。

完整映射标准（Standards）、成熟先例（Prior Art）、方法（Methods）、实现（Implementations）、组织（Organizations）、能力（Capabilities）、场景（Scenarios）与证据（Evidence）的一个重要结果，是让“已经解决”与“仍未解决”之间的边界逐渐可见。

当某个真实互操作需求：

- 没有成熟标准（Standard）；
- 只有少量、彼此割裂或封闭的成熟先例（Prior Art）；
- 存在多个互不兼容的实现；
- 现有方案具有明显的开放性 / 可携带性 / 互操作性（Openness / Portability / Interoperability）缺口；
- 或已有标准无法覆盖反复出现的真实场景；

IA 应能够把它识别为可研究的**开放缺口（Open Gap）/ 标准化缺口（Standardization Gap）/ 开放性缺口（Openness Gap）**，而不是把“没有找到答案”静默处理为搜索失败。

理想的长期循环是：

```text
映射现有互操作方案空间
（Map the existing Solution Space）
        ↓
发现真实互操作需求
（Find a real interoperability need）
        ↓
是否已有成熟且足够开放的方案？
（Is there a mature, sufficiently open solution?）
        ↓
有则尽可能采用、复用并连接
（Adopt / reuse / connect）
        ↓
没有则检查成熟先例与竞争方案
（Examine Prior Art and competing approaches）
        ↓
验证真实缺口
（Verify the real gap）
        ↓
足够时采用配置或扩展
（Profile / Extend）
        ↓
只有必要时才自行发明
（Invent only when necessary）
        ↓
形成新的共享知识 / 实现 / 规范
        ↓
重新进入知识地图
```

因此 IA 可以帮助推动更开放、更成熟、更可复用的共同方案，但它不应成为一个为了“制定标准”而不断制造 IA 自有标准的组织。

> **标准化是经过验证的缺口可能产生的结果，而不是知识地图的默认产物。**  
> *Standardization is a possible consequence of a verified gap, not the default output of the Atlas.*

## 15. 开放不等于没有权威边界（Open does not mean authority-free）

开放贡献不等于任何输入自动成为公共事实。

开放系统仍然需要：

- 身份（Identity）；
- 来源追踪（Provenance）；
- 证据（Evidence）；
- 审查（Review）；
- 生命周期（Lifecycle）；
- 治理（Governance）；
- 权限边界（Permission boundaries）。

智能体、人类、组织的平台权限也不等于知识权威。

## 16. 互操作也应适用于 InteropAtlas 自身（Interoperability should apply to InteropAtlas itself）

一个研究互操作的项目，应尽可能让自己的：

- 规范数据（Canonical data）；
- API / 智能体访问（Agent access）；
- 个人视角（Personal Perspective）；
- 工作空间状态（Workspace state）；
- 导出数据（exports）；
- 贡献记录（contribution records）；

保持可携带、可解释、可组合，并保留替换具体实现的空间。

长期个人知识空间（Personal Knowledge Space）尤其不应天然锁死在某个客户端、账号或推荐模型中。

## 17. 项目本身也是知识表达实验（The project is also an experiment in knowledge expression）

InteropAtlas 不只是“收录互操作知识”。它也可以成为一个真实实验场：研究结构化知识怎样被选择、投影、转换和表达，人（Human）与智能体（Agent）如何共同操作复杂知识空间，以及几十年前因技术条件受限的知识组织思想在智能体时代能否获得新的生命。

这不意味着 IA 要变成通用个人知识管理系统（PKM）。研究必须始终服务于真实的 InteropAtlas 使用和可验证的知识任务。

## 18. 延伸阅读：思想谱系（Intellectual Lineage）

如果希望继续追踪这些原则“从哪里来”，以及 IA 对前人思想究竟是采用（Adopt）、配置（Profile）、扩展（Extend）、综合（Synthesize）还是仍处于开放研究（Open Research），请继续阅读：

- [`InteropAtlas 思想谱系与产品哲学扩展阅读 v0.1`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)

这份扩展阅读应随着既有先例研究（Prior-Art Research）持续修正。发现更早或更成熟的前人工作，应被视为 IA 获得了更准确的知识，而不是削弱项目价值。