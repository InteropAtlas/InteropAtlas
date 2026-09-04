# InteropAtlas Knowledge Philosophy & Principles v1.0

<!-- InteropAtlas Document Metadata v0
Document Status: active philosophy baseline
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T21:00:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文保存 InteropAtlas 最不应该因为某个页面、Schema、Agent 或阶段计划而丢失的产品哲学。具体架构以 Master Design 和各 V1 Contract 为准。
>
> 这些原则并非被假定为凭空发明。其 Knowledge Commons、Memex / Hypertext、Adaptive Hypermedia、Multiple Representation、Explainable / Controllable Personalization 等思想来源与 IA 的继承/重新组合关系，见 [`InteropAtlas 思想谱系与产品哲学扩展阅读`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)。

## 1. Knowledge belongs to the commons

InteropAtlas 首先服务于全人类，而不是某个单独用户、组织、Agent 或客户端。

公共知识世界应尽可能开放、可追溯、机器可读、可复用、可长期演化。任何 Personalization 都建立在这个公共世界之上，而不是取代它。

## 2. Perspective belongs to the individual

公共事实可以共享，注意力不能被统一规定。

不同人的工作、目标、知识背景、兴趣、生活状态、时间预算和认知方式不同。系统应允许每个人形成自己的 Perspective，并允许 Perspective 随状态变化。

Personal Perspective 是对公共知识的选择、强调和组织，不是私人事实覆盖公共事实。

## 3. Representation should adapt to cognition

> **Knowledge is stable; representations are fluid.**

同一知识可以被表达为文字、图像、Wiki、Timeline、Graph、Compare、音频、视频、交互、Simulation 或 Game。不存在一种对所有人、所有任务都最好的 Representation。

文字可以是高压缩、高可检索的默认媒介，但 InteropAtlas 应坚持 **text-first, not text-only**：当关键语义无法被文字充分表达，或其他媒介对当前认知任务明显更有效时，应允许更合适的形式。

## 4. Personalization must remain reversible and transparent

个性化不是“猜你喜欢”。

系统应尽可能让用户知道：

- 为什么某条知识出现；
- 为什么某条知识被弱化；
- 当前使用了什么 Perspective / Context；
- 如何关闭或改变这些规则；
- 如何回到 Public Atlas；
- 如何主动探索当前兴趣之外的知识。

信息茧房不是一个可以留到产品末期再处理的副作用，而是 Personal Knowledge Space 的设计约束。

## 5. Atlas-first, not Human-first or Agent-first

Human 和 Agent 都是知识世界的参与者和访问者。

项目不能为了 Human UI 建立一套事实，又为了 Agent 建立另一套事实。它们应共享 Canonical Knowledge、Evidence、Provenance 和明确的未知边界，只在访问、选择、投影、表达与权限上不同。

## 6. Knowledge is for use, not accumulation alone

知识的价值不仅在于被保存，还在于被：

```text
发现
→ 理解
→ 使用
→ 传播
→ 组合
→ 验证
→ 产生新知识
→ 重新进入 Atlas
```

因此 InteropAtlas 不应成为无限堆积材料的仓库。

## 7. Knowledge should flow

长期研究 Knowledge Metabolism：

```text
Collect
→ Understand
→ Integrate
→ Apply
→ Create
→ Distill
→ Archive / Compact / Forget
→ Reactivate
```

但公共知识基础设施中的“遗忘”必须谨慎。Deprecated ≠ Worthless，Superseded ≠ False。历史知识可能在特定 Context 下重新成为最相关的知识。

公共知识 Lifecycle 与个人 Attention Lifecycle 必须区分。

## 8. Selection before presentation

一个漂亮界面无法修复错误的知识选择。

在问“页面怎么设计”之前，先问：

1. 当前任务是什么？
2. 什么知识应该进入注意力？
3. 哪些维度与关系需要暴露？
4. 哪种 Representation 最合适？
5. 用户/Agent 需要执行什么操作？

## 9. Workspace is a knowledge operation space

Workspace 不是单纯 View。

Representation 决定“看到什么样子”，Workspace 还决定“在这种认知方式下能够做什么”。因此 Timeline、Graph、Compare、Evidence、Simulation 等的价值来自它们支持不同的认知任务和操作。

## 10. Evidence before assertion

InteropAtlas 应尽可能把：

- Reality；
- Source；
- Evidence；
- Fact；
- Inference；
- Assessment；
- Recommendation；

保持可区分。

Agent 输出和 Generated View 不因为读起来流畅就成为 Canonical Fact。

## 11. Recoverability over false completeness

知识进入系统并不断被选择、投影和表达时会发生信息损失。

允许有损 Representation，但不允许为了方便显示而静默破坏更丰富的 Canonical Knowledge、Evidence、Provenance、Scope 和 Identity。

明确的 `unknown` / `not_recorded` 比伪造完整性更好。

## 12. Real use shapes the ontology

InteropAtlas 不应先设计一个理论上完美的世界模型，再要求现实服从它。

真实 Query、真实工作流、真实 Intake 和真实失败应该持续暴露模型缺口。只有当问题被证明确实存在，并经过 Prior Art / Standards 检查后，才决定是否改变模型。

## 13. Adopt → Profile → Extend → Invent

不要因为一个问题“看起来新”就自己发明。

优先寻找几十年来已经存在的标准、理论、协议、知识模型、交互研究和成熟产品实践。研究既用于验证，也用于纠偏和获得认知增量。

**这条原则同样约束 InteropAtlas 自己。** 当 IA 设计 Canonical Schema、Relation、API、Agent access、Human Interface、治理、协作机制、数据格式、Personal Perspective 或新的 Specification 时，必须优先调查和采用现有标准与成熟先例；只有它们经过真实场景验证仍无法满足需求时，才依次考虑 Profile、Extend，最后才 Invent。

IA 不应一边绘制人类的互操作方案空间，一边因为不了解 Prior Art 而制造新的互操作孤岛。

## 14. Open does not mean authority-free

开放贡献不等于任何输入自动成为公共事实。

开放系统仍然需要：

- Identity；
- Provenance；
- Evidence；
- Review；
- Lifecycle；
- Governance；
- Permission boundaries。

Agent、Human、Organization 的平台权限也不等于知识权威。

## 15. Interoperability should apply to InteropAtlas itself

一个研究互操作的项目，应尽可能让自己的：

- Canonical data；
- API / Agent access；
- Personal Perspective；
- Workspace state；
- exports；
- contribution records；

保持可携带、可解释、可组合、可替换实现的空间。

长期 Personal Knowledge Space 尤其不应天然锁死在某个客户端、账号或推荐模型中。

## 16. The project is also an experiment in knowledge expression

InteropAtlas 不只是“收录互操作知识”。它也可以成为一个真实实验场：研究结构化知识怎样被选择、投影、转换和表达，Human 与 Agent 如何共同操作复杂知识空间，以及几十年前因技术条件受限的知识组织思想在 Agent 时代能否获得新的生命。

这不意味着 IA 要变成通用 PKM。研究必须始终服务于真实 InteropAtlas 使用和可验证的知识任务。

## 17. Further reading: Intellectual Lineage

如果希望继续追踪这些原则“从哪里来”，以及 IA 对前人思想究竟是 Adopt、Profile、Extend、Synthesize 还是仍处于 Open Research，请继续阅读：

- [`InteropAtlas 思想谱系与产品哲学扩展阅读 v0.1`](interopatlas-intellectual-lineage-v0.1.zh-CN.md)

这份扩展阅读应随着 Prior-Art Research 持续修正。发现更早或更成熟的前人工作，应被视为 IA 获得了更准确的知识，而不是削弱项目价值。
