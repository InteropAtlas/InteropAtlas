# InteropAtlas Information Presentation Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft / Gate B Module**
Document Created At: 2026-09-02T07:39:56+08:00
Document Updated At: 2026-09-02T10:51:11+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> 状态：**Draft / Gate B Module**
>
> Package: [`human-interface-profiles.zh-CN.md`](human-interface-profiles.zh-CN.md)

## 1. 目标

本 Profile 约束的是：

> **用户抵达一个 InteropAtlas View 后，信息以什么顺序、粒度和表达形式被理解。**

Human View 不是 YAML 的漂亮打印版。Renderer 可以重组信息，但不能改变 Canonical Facts / Statements 的含义。

---

## 2. 主要用户任务

- Identify — 快速知道“这是什么”；
- Understand — 知道它解决什么问题 / 提供什么能力；
- Relate — 理解重要关系与上下文；
- Compare — 看到可比较维度而不是字段噪声；
- Verify — 找到来源、Evidence 与 provenance；
- Explore — 从正文自然进入关系探索。

---

## 3. 上游依据

### Normative / high-authority

- ISO 9241-112:2025 — 信息呈现、可辨识、可理解、组织原则；
- ISO 9241-125:2017 — 视觉信息呈现；
- ISO 9241-110:2020 — self-descriptiveness / task suitability；
- HTML Living Standard — 文档结构与语义；
- WCAG 2.2 — headings、labels、link purpose、reflow 等。

### Mature methods / reference practice

- progressive disclosure；
- content hierarchy；
- GOV.UK / USWDS 的公共信息呈现方法；
- Diátaxis 作为内容职责分离参考；
- 信息可视化方法用于 table / graph / relation view 的选择。

---

## 4. 默认 Object Resource Page 信息顺序

当数据存在时，SHOULD 优先遵守：

```text
Identity / Name
一句话 Summary
↓
Why / Capability / Context
↓
Key Facts
↓
Important Relationships
↓
Evidence / Sources / Provenance
↓
Exploration / Map / Extended Relations
↓
Machine View / Raw Data
```

这不是要求所有对象页字段完全一致，而是定义用户认知顺序。

---

## 5. Requirements

### `IA-HI-IP-001` — Summary Before Detail

对象页 SHOULD 先提供摘要和关键事实，再让复杂关系、Evidence 和机器字段进入阅读流。

- 用户任务：Identify / Understand
- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-112 / 125
- Conformance：`Static + Human`
- 验收：首个主要内容区是否能在不操作 Graph 的情况下回答“这是什么 / 为什么重要”。

### `IA-HI-IP-002` — Do Not Mirror YAML Literally

Human View MUST NOT 只是按 YAML 字段顺序转写。

- 用户任务：Understand
- 采用方式：**IA-specific Profile**
- 上游：ISO 9241-112 + IA Knowledge Model
- Conformance：`Static + Review`
- 验收：页面区块按用户信息职责组织；物理字段顺序变化不能成为页面结构变化的唯一原因。

### `IA-HI-IP-003` — Detectable Hierarchy

主身份、摘要、关键事实、辅助信息、元数据和探索区域 SHOULD 具有可察觉层级。

- 用户任务：Identify / Scan / Understand
- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-112 / 125
- Conformance：`Static + Visual + Accessibility`
- 验收：heading structure、grouping、视觉权重和阅读顺序一致，不仅靠字体大小制造层级。

### `IA-HI-IP-004` — Concision With Access to Detail

主阅读流 SHOULD 克制内部字段和重复信息，但 MUST 保留完整来源、Evidence 和机器信息的可发现路径。

- 用户任务：Understand / Verify
- 采用方式：**Profile**
- 上游：ISO 9241-112；progressive disclosure
- Conformance：`Static + Human`

### `IA-HI-IP-005` — Unambiguous Human Labels

主要标签 MUST 使用可理解的人类名称；内部 ID、枚举和值不能直接替代主要 Human Label。

- 用户任务：Identify / Relate
- 采用方式：**Profile**
- 上游：ISO 9241-110 self-descriptiveness；ISO 9241-112
- Conformance：`Static + Review`
- 验收：扫描首页 / Resource Page / Map，不应无解释出现 `implementation`、`exchange` 等机器值作为主标签。

### `IA-HI-IP-006` — Progressive Disclosure

长 Evidence、机器字段和大规模关系列表 MAY 渐进披露，但必须保持可发现，并满足 Interaction / Accessibility 合同。

- 用户任务：Understand / Verify
- 采用方式：**Profile**
- 上游：mature interaction pattern
- Conformance：`Static + Browser + Accessibility`

### `IA-HI-IP-007` — Source Visibility

可验证事实页面 MUST 提供来源入口；来源不应压过主阅读流，也不得难以发现。

- 用户任务：Verify
- 采用方式：**Profile**
- 上游：IA Evidence principle + public knowledge infrastructure goal
- Conformance：`Static + Data + Human`

### `IA-HI-IP-008` — Compare Preserves Semantic Class and Missing Meaning

**用户任务：** Compare / Verify。

Compare presentation MUST 对齐共享、可解释的比较维度，并 MUST 保留 Fact / Relation / Statement / Assessment 的语义类别。缺失值 MUST NOT 被默认为 `false` 或 `none`；至少需要区分明确 false、unknown、not recorded / absent 与 not applicable。

Compare MUST NOT 通过隐藏总分、默认 winner 或无依据的推荐把多个事实压缩成新的 Assessment。

- 采用方式：**Profile + IA-specific extension**
- 上游：ISO 9241-112 information discriminability / understandability；Knowledge Model missing semantics and Fact / Assessment boundary
- Conformance：`Static + Data + Human + Accessibility`
- 验收：按 [`human-interface-minimal-compare-contract.zh-CN.md`](human-interface-minimal-compare-contract.zh-CN.md) 检查代表候选能否在保留上下文、缺失语义和来源边界的前提下形成可扫描差异。

---

## 6. 表达形式选择

### Text

适合：解释身份、范围、上下文、限制、理由。

### List

适合：少量同类项目、Requirements、Sources、Relations。

### Table

适合：多个对象共享清楚比较维度时。不得为了“看起来结构化”把长叙述塞入宽表格。

用于 Compare 时，Table 只是可选投影：必须保持维度与候选值关联、缺失值语义和语义类别；窄屏 / 辅助技术场景下如果宽表破坏这些关系，应使用 stacked comparison 或其他等价结构。

### Graph / Map

适合：关系结构本身是用户问题时。Graph 不应在用户还没理解中心对象前抢占首要视觉权重。

Graph 不适合替代属性维度比较，也不得把 `alternative_to` 的连线视觉误读成 compatibility / equivalence。

### Machine View

适合：贡献者 / Agent / 高级用户验证原始结构；不是普通阅读的默认主要界面。

---

## 7. Relationship Presentation

关系 View MUST 保留至少这些语义：

- 方向；
- predicate / relation kind；
- target/source identity；
- Relation 与普通字段引用的来源差异（如果语义不同）；
- Context / Evidence（当该关系需要时）。

同一事实如果已经以明确正文或列表表达，Graph SHOULD 避免无信息增量的重复。

在 Compare View 中，Relation MAY 成为比较上下文或维度，但 MUST 保留原 predicate，不能因页面标题是“Compare”就转换为 compatibility、equivalence 或 recommendation。

---

## 8. 当前实现证据

第一次 Audit 已发现：

- `h1/h2/h3` 结构基本正确；
- 页面已有 Summary；
- Relations 已部分按语义分组；
- 但 Local Map 曾过早进入主阅读流；
- 一跳邻居 / 直接关系 / Local Map 存在重复；
- 内部机器标签曾泄漏到 Human View；
- 部分对象缺少来源入口。

后续 Renderer 已有改进，但 Gate B 仍需要用本 Profile 重新审计，而不能直接沿用早期 PASS/FAIL 数字。

---

## 9. 当前 Gap

### `HI-IP-GAP-001` — Key Facts contract

不同 Strong Profile 的“关键事实”尚未有最小 Human Presentation contract。例如 Capability、Normative Artifact、Implementation、Organization 应各自先显示哪些字段，需要在不重新设计 Knowledge Model 的前提下定义。

### `HI-IP-GAP-002` — Evidence presentation

Knowledge Model 已明确 Evidence / Assessment 边界，但 Human Interface 尚未定义：事实来源、Statement Evidence、Assessment basis 在页面上怎样区分。

### `HI-IP-GAP-003` — Compare presentation

**Gate B minimum：closed by #94 contract。**

最小语义合同已经规定共享维度、Missing Semantics、Fact / Relation / Assessment boundary、No Hidden Ranking，以及 Table / stacked projection 的基本职责。

**Remaining P1：** 最终 Compare UI pattern、并排卡片 / 表格切换、多候选密度、响应式产品体验与交互细节。

### `HI-IP-GAP-004` — Density measurement

目前只有方向性规则，没有可重复的密度 / 扫描评价方法。Gate B 应至少定义 task-based human review，而不是拍一个固定“每页最多多少区块”的数字。

---

## 10. 与其他 Profile 的依赖

- Information Architecture 决定 View 的职责和入口；
- Interaction 决定 disclosure、filter、tabs/details 等行为；
- Visual Presentation 决定层级如何被感知；
- Accessibility / Conformance 验证 heading、reading order、labels、reflow 和辅助技术体验。
