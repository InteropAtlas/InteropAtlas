# InteropAtlas 项目建设与实践反馈模型（Project Development & Practice Feedback Model）

<!-- InteropAtlas Document Metadata v0
Document Status: Provisional Methodology / Long-term Core Method
Document Created At: 2026-09-05T14:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文是项目建设方法与实践反馈机制的 Primary Home。它合并此前的 `project-development-principles` 与 `practice-feedback-loop`，避免“建设原则”和“反馈环”形成两套平行方法论。

## 1. 建设原则：先复用、再扩展，先证据、再断言

InteropAtlas 的建设默认遵循：

> **Adopt → Profile → Extend → Invent**

创建新的 Relation、Schema、ID 体系、验证机制、版本规则、仓库模板、方法论或规范之前，应先进行 Prior Art Check。优先直接采用成熟方案；不完全适用时 Profile；仍不足时做最小扩展；只有存在真实缺口时才创造 IA 自有方法。新建自有规范时，应记录为什么现有方案不能满足需求。

同时保持以下不变量：

- **Evidence Before Assertion**：重要事实尽可能具有可追踪 Source / Evidence；来源不足时允许 Unknown / Incomplete，而不是强行填值。
- **Fact ≠ Assessment**：可验证事实与场景化判断分离，Engine 不得把动态 Assessment 静默写回稳定事实。
- **Structured Source, Linked View**：Canonical structured data 是事实源；网页、Markdown、列表、地图、关系图和 API 是 View / Projection，不维护竞争性事实数据库。
- **Flat Objects + Rich Relations + Dynamic Maps**：对象不被单一文件夹或唯一 parent 锁死；分类、层级和导航主要由关系、查询和 View 产生。
- **Human ↔ Machine Co-development**：机器能力与人类体验共同演进，共享 Canonical Model，不建设彼此割裂的两套事实世界。
- **Minimum Governance Before Scale**：规模扩大前至少明确 stable ID、Evidence、Relation vocabulary、Schema change、成熟度标签与重大设计依据。
- **Prefer Reversible Decisions**：需求未成熟时优先可迁移、可替换、可回滚的实现，不因一次实验冻结长期模型。
- **Record Decisions and Negative Evidence**：不仅记录采用了什么，也记录研究过什么、为何不采用、什么仍未解决。

项目自产方法的成熟度不应被过早抬高：

```text
Experiment / Note
      ↓
Methodology / Guide
      ↓
Specification
      ↓
Candidate / Profile
      ↓
Standard（仅在真正需要时）
```

Skill 与这条成熟链正交：Skill 可以实现 Methodology 或 Specification，但不能替代其定义。

## 2. 实践反馈环：每次建设同时是一次 Atlas 验证

InteropAtlas 不应只靠抽象设计积累知识。真实项目、真实建设步骤和真实技术选择，应持续作为 Atlas 的使用场景和验证实验；Atlas 中积累的标准、能力、关系与证据又反过来指导真实项目。

核心循环：

```text
真实项目 / 建设步骤
        ↓
Scenario / Capability Need
        ↓
在 Atlas 中检索候选方案
        ↓
Alternative Discovery
        ↓
比较路线、关系、约束与适用条件
        ↓
发现覆盖与模型缺口
        ↓
研究、补充、修正 Atlas
        ↓
真实选择与实现
        ↓
记录采用 / 未采用 / 失败 / 限制 / 结果
        ↓
反哺 Atlas
        ↺
```

这不是一次性 Bootstrap Experiment，而是长期运行机制。

### Atlas → Practice

Atlas 应帮助真实项目：

- 发现标准、协议、方法与实现；
- 发现同类与替代路线；
- 理解依赖、兼容、扩展、Profile 等关系；
- 检查开放性、来源与约束；
- 发现尚未考虑的能力和互操作需求；
- 为技术选型提供可验证、可版本化的知识基础。

### Practice → Atlas

真实实践应帮助 Atlas：

- 暴露尚未收录的重要对象；
- 暴露缺失或错误的 Relation；
- 暴露 Capability / Scenario / Evidence 模型不足；
- 验证分类、解释与界面是否真正有用；
- 发现 Open Gap、实现缺口和桥接缺口；
- 积累采用与淘汰的真实理由；
- 积累失败、限制、兼容性问题与负面证据。

一个大型项目应继续拆成可观察的小场景。例如 Engine 可以拆为读取结构化数据、Schema validation、引用解析、反向链接、Graph 构建、Renderer、语言表达、发布与自动化等步骤；每一步都可以触发一次小型反馈环。

### Alternative Discovery 是默认步骤

发现第一个满足 Capability 的方案不代表检索结束。每次发现候选后，应至少继续检查：

1. 是否存在解决相同或高度相似 Capability 的其他标准、规范、协议、方法或实现；
2. 它们是否属于不同对象性质或标准化程度；
3. 是否需要 `alternative_to`、`extends`、`profiles`、`compatible_with` 等关系；
4. 各路线优化什么、适用于什么、限制是什么；
5. 未采用候选及其淘汰理由是否值得保留为实践证据。

SemVer / CalVer 的早期实践已经证明：找到一个可用方案，并不等于已经看见主要方案空间。

### 不只记录成功

以下内容同样具有长期价值：

- 调研过但未采用的方案及原因；
- 导致淘汰的约束；
- Atlas 当时是否成功发现候选；
- Atlas 是否漏掉重要路线；
- 是否缺少开放实现；
- 是否依赖专有平台；
- 是否出现模型无法表达的关系；
- 实现中的真实兼容性问题；
- 原有判断是否被实践推翻。

## 3. 用覆盖与反馈推动演化，而不是追求漂亮数字

实践反馈至少区分两个核心维度：

### Standard Coverage（标准覆盖率）

回答：面对一个 Scenario / Capability，实际需要的重要标准、规范、协议或约定，Atlas 已经收录了多少？

它主要检查对象层缺项。只有候选集合边界足够明确时才应计算百分比，避免制造虚假的精确度。

### Solution-Space Coverage（方案空间覆盖率）

回答：Atlas 是否呈现了主要可行路线，而不是只找到第一个能用的方案？

它关注：

- 主要替代方案是否被发现；
- 不同标准化性质是否被正确区分；
- 关键关系是否存在；
- 优化目标、适用条件与限制是否足够明确；
- 是否因搜索路径、生态偏好或先入为主漏掉重要路线。

两者的区别可以压缩为：

```text
Standard Coverage
→ 我需要的重要东西，Atlas 里有没有？

Solution-Space Coverage
→ Atlas 有没有让我看到主要有哪些路可以走？
```

Relation Coverage、Explanation Coverage、Decision Coverage、Practice Coverage 等维度可作为进一步的 Coverage Assessment 信号，但覆盖率本身不是最终目标。真正的问题始终是：

> **当真实项目需要互操作知识时，InteropAtlas 到底能帮助到什么程度？**

长期实践历史因此也是 Atlas 的资产，可用于改进分类与数据模型、研究标准选择模式、发现反复出现的互操作缺口、形成参考架构，并为未来比较、推荐和 Gap Analysis 提供依据。

### 当前运行原则

每一次 InteropAtlas 自身建设，都应尽可能同时完成三件事：

1. **Build** — 完成当前真实建设任务；
2. **Learn** — 发现缺失的标准、关系、能力、方法或工具；
3. **Feed Back** — 把可复用的事实、证据、缺口与方法回流到 Atlas / Methodology。

> **InteropAtlas 不只是描述互操作世界，也持续通过真实实践检验自己对这个世界的描述。**
