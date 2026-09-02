# 实践驱动的双向成长反馈环

<!-- InteropAtlas Document Metadata v0
Document Status: 长期核心方法（持续演化）
Document Created At: 2026-08-31T13:32:18+08:00
Document Updated At: 2026-08-31T14:53:04+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

状态：长期核心方法（持续演化）

## 目的

InteropAtlas 不应只通过抽象设计积累标准数据。真实项目、真实建设步骤和真实技术选择，应持续作为 Atlas 的使用场景和验证实验；与此同时，Atlas 中积累的标准、能力、关系和评估结果又应反过来指导这些项目的设计与实现。

因此，InteropAtlas 与使用它的项目之间应建立长期的双向驱动关系。

## 核心反馈环

```text
真实项目 / 建设步骤
        ↓
Scenario（场景）
        ↓
Capability Need（能力需求）
        ↓
在 InteropAtlas 中检索
        ↓
发现候选标准 / 规范 / 协议 / 实现
        ↓
Alternative Discovery（替代方案发现）
        ↓
比较同能力下的候选、关系与适用条件
        ↓
覆盖情况与缺口
        ↓
研究、补充、修正 InteropAtlas
        ↓
进行真实技术选择与实现
        ↓
记录实践结果、问题与选择理由
        ↓
反哺 InteropAtlas
        ↓
下一轮场景与实践
```

这不是一次性的 Bootstrap Experiment（自举实验），而是长期机制。

## 双向驱动

### Atlas → Practice

InteropAtlas 应帮助真实项目：

- 发现可能采用的标准和协议；
- 发现同类与替代方案；
- 理解标准之间的关系；
- 检查开放性和依赖；
- 发现尚未考虑的能力与互操作需求；
- 为技术选型提供可验证、可版本化的知识基础。

### Practice → Atlas

真实项目应帮助 InteropAtlas：

- 暴露尚未收录的重要标准；
- 暴露缺失或错误的 Relation；
- 暴露 Capability / Scenario 模型不足；
- 验证分类和解释是否真正有用；
- 发现 Open Gap、实现缺口和桥接缺口；
- 积累技术选择的真实理由；
- 积累失败、限制、替代和实践证据。

## Alternative Discovery（替代方案发现）

发现一个能够满足 Capability 的标准或方案，并不意味着检索结束。

每次发现候选后，应至少再执行一次替代方案发现：

1. 检查是否存在解决相同或高度相似 Capability 的其他标准、规范、协议、约定或实现；
2. 区分它们的对象性质和标准化程度，不能因为解决相似问题就强行归为同一种 Standard；
3. 建立 `alternative_to`、`extends`、`profiles`、`compatible_with` 等适当关系；
4. 记录各候选优化的目标、适用条件、限制和选择理由；
5. 如果最终未采用某候选，也保留“研究过但未采用”的实践证据。

第一次 Engine v0.1 版本表达实验提供了一个具体反馈：最初从 `version_expression` 能力发现并收录了 SemVer，但没有立即发现 CalVer。后续追问才暴露 CalVer 这条以时间和发布节奏为主要语义的替代路线。因此，替代方案发现被正式加入长期反馈流程。

## 每个步骤都可以成为场景

一个项目不应只被记录为一个巨大的 Scenario。项目内部的实际步骤也可以成为更小的场景或实验单元。

例如构建 InteropAtlas Engine v0.1 可以继续拆分为：

- 读取人类可编辑结构化数据；
- 校验数据结构；
- 解析对象引用；
- 计算反向链接；
- 构建关系图；
- 生成 HTML；
- 表达语言信息；
- 发布静态网站；
- 自动化构建与部署；
- 表达许可证、版本、日期时间等元数据。

每一个步骤都可以触发一次“需求 → Atlas → 实践 → 反馈”的小循环。

## 不只记录成功

实践数据的价值不应只来自最终采用的标准。以下信息同样重要：

- 调研过但没有采用的标准；
- 为什么没有采用；
- 哪些约束导致方案淘汰；
- Atlas 当时是否成功发现了候选；
- Atlas 是否漏掉重要候选；
- 标准本身是否缺少开放实现；
- 是否需要专有平台或闭源组件；
- 标准之间是否存在无法表达的关系；
- 实现过程中出现了哪些实际兼容性问题；
- 原先的判断后来是否被实践推翻。

这些负反馈与失败数据是 Atlas 演化的重要证据。

## 覆盖率作为反馈指标，而不是目标本身

覆盖评估不能只回答“有没有收录某个标准”。至少应区分以下两个核心维度：

### Standard Coverage（标准覆盖率）

回答：

> 面对一个 Scenario / Capability，实际需要的重要标准、规范、协议或约定，InteropAtlas 已经收录了多少？

它主要衡量 Atlas 的对象层是否存在明显缺项。

例如一个场景实际涉及 10 个重要标准，而 Atlas 在实践开始前已有 7 个，则可以记录对象层面的标准覆盖情况。具体百分比只有在候选集合边界足够明确时才应计算，不能制造虚假的精确度。

### Solution-Space Coverage（方案空间覆盖率）

回答：

> 面对一个 Capability，InteropAtlas 是否发现并呈现了主要可行路线，而不是只找到第一个能用的方案？

它关注的不只是对象数量，还包括：

- 主要替代方案是否被发现；
- 不同标准化性质的方案是否被正确区分；
- 候选之间的重要关系是否存在；
- 各方案优化目标、适用条件和限制是否足够明确；
- 是否存在因搜索路径、生态偏好或先入为主而漏掉的重要路线。

因此，“已经收录一个可用标准”不能自动视为方案空间覆盖完成。

Engine v0.1 的版本表达实践就是第一个例子：仅收录 SemVer 时，`version_expression` 已经具有一个可用方案，因此 Standard Coverage 并非零；但由于 CalVer 这一主要替代路线尚未被发现，Solution-Space Coverage 仍明显不足。

这两个指标互补：

```text
Standard Coverage
  → 我需要的重要东西，Atlas 里有没有？

Solution-Space Coverage
  → Atlas 有没有让我看到主要有哪些路可以走？
```

对于一个真实场景，还可以继续记录：

- 实际需要研究的标准数量；
- 开始实践前 Atlas 已收录数量；
- 实践中新增数量；
- 已存在但关系不完整的数量；
- Atlas 成功帮助发现的候选数量；
- Atlas 漏掉、最终由外部研究发现的候选数量。

此前提出的 Relation Coverage、Explanation Coverage、Decision Coverage、Practice Coverage 等维度仍然有效；Standard Coverage 与 Solution-Space Coverage 用来进一步区分“对象是否存在”和“方案空间是否被充分探索”。这些维度后续可逐渐形成正式的 Coverage Assessment（覆盖评估）模型。

覆盖率的目的不是追求漂亮数字，而是回答：

> 当一个真实项目需要标准知识时，InteropAtlas 到底能帮助到什么程度？

随着项目成熟，同类型真实场景的初始覆盖率、方案发现完整度和决策支持质量应逐渐提高。

## 实践记录的长期价值

当 InteropAtlas 达到较高可用程度时，持续的自举和外部实践会自然形成一批历史实验数据。这些数据可以用于：

- 验证 Atlas 的实际价值；
- 改进分类与数据模型；
- 研究标准选择模式；
- 发现反复出现的互操作缺口；
- 分析开放标准生态的薄弱位置；
- 形成参考架构和标准组合；
- 为未来 Engine 的推荐、比较和 Gap Analysis 提供实践依据。

因此，实践历史本身应逐渐成为 InteropAtlas 的一种重要资产。

## 当前第一个正式实践

**InteropAtlas Engine v0.1** 作为第一批正式的自举实践场景。

第一阶段先进行：

1. 将 Engine v0.1 拆成实际场景与能力需求；
2. 从这些需求发现可能涉及的标准、规范、协议、开放方法和实现；
3. 对发现的候选执行 Alternative Discovery；
4. 与当前 Atlas 数据比较；
5. 记录 Standard Coverage 与 Solution-Space Coverage，并逐步补充其他覆盖维度；
6. 收录重要缺项并建立关系；
7. 开始 Engine 实现；
8. 开发过程中继续发现并补充；
9. 记录采用、未采用、失败、限制和选择理由；
10. 用实际结果再次检查 Atlas 的有效性。

## 原则

> InteropAtlas 不只是描述互操作世界，也要持续通过真实实践检验自己对这个世界的描述。

> Atlas 与 Practice 相互驱动成长；每一次建设都同时是一次使用、验证和数据积累。