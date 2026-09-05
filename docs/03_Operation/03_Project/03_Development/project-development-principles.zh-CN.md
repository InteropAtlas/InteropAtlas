# InteropAtlas 项目建设原则（暂定规范）

<!-- InteropAtlas Document Metadata v0
Document Status: Provisional Methodology（暂定方法论）。这些规则用于约束近期建设行为，但还不是正式 InteropAtlas Standard。
Document Created At: 2026-08-31T19:36:02+08:00
Document Updated At: 2026-08-31T19:36:02+08:00
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

> 状态：Provisional Methodology（暂定方法论）。这些规则用于约束近期建设行为，但还不是正式 InteropAtlas Standard。

## 1. Reuse Before Invent（先复用，后创造）

创建新的 Relation、Schema、ID 体系、验证机制、版本规则、仓库模板、方法论或规范之前，先做 Prior Art Check。

优先顺序：

```text
直接采用成熟方案
    ↓ 不适用
采用其概念 / Profile
    ↓ 不足
组合多个成熟方案
    ↓ 不足
对现有方案做最小扩展
    ↓ 仍存在真实缺口
创建 IA 自有方法 / 规范
```

新建自有规范时，应记录为什么现有方案不能满足需求。

## 2. Evidence Before Assertion（先证据，后断言）

进入 Facts 层的重要事实应尽可能存在可追踪 Source / Evidence。

- 不因为一个结论“看起来正确”就把它作为稳定事实；
- 动态、争议、开放性、兼容性、版本状态等事实尤其需要来源；
- 来源不足时可以记录 Unknown / Incomplete，而不是强行填值。

## 3. Fact ≠ Assessment（事实与评估分离）

Fact：可从来源验证的事实。

Assessment：在给定规则、场景、约束和时间下计算或判断得到的结果。

例如：
- `open_source: true` 可以是 Fact；
- “是某场景下最佳开放替代方案”是 Assessment。

Engine 不应把动态判断偷偷写回稳定事实。

## 4. Structured Source, Linked View（结构化事实源，链接化视图）

YAML / Canonical Data 保持单一事实源；网页、Markdown、列表、表格、地图、关系图和 API 均为自动生成或可重新计算的 View / Projection。

不得为了网页方便而维护第二份互相竞争的事实数据库。

## 5. Flat Objects + Rich Relations + Dynamic Maps

底层对象尽量扁平，关系尽量丰富；分类、层级和导航主要由关系、查询和 Map/View 产生。

- 不要求对象只有一个 parent；
- 同一对象可以同时出现在多个 Map；
- Map 是视图，不是底层唯一真相；
- Relation vocabulary 需要治理，不能无限自由扩散。

## 6. Human ↔ Machine Co-development（人机路线共同演进）

不要分别建设“机器系统”和“人类网站”。

- 人类体验暴露缺失的机器能力；
- Engine 新能力应考虑如何转换成人类可见价值；
- Renderer 不应长期承担 Resolver / Graph / Analysis 的职责；
- Machine API 和 Human View 应尽量来自同一 Canonical Model。

## 7. Practice-driven Feedback（实践驱动反馈）

真实建设与真实问题优先于抽象完整性。

```text
真实场景
  ↓
发现能力 / 数据 / 关系缺口
  ↓
研究成熟方案
  ↓
扩充 Atlas / Engine / Methodology
  ↓
再次实践
```

允许前期模型演进，不因追求一次性完美而停止实践。

## 8. Minimum Governance Before Scale（扩张前建立最小治理）

项目早期不建立重型标准组织，但在规模扩大前至少明确：

- stable ID 原则；
- version / date / URL 不混同；
- Evidence / Source 最小要求；
- Relation vocabulary 的新增条件；
- Schema change 如何记录；
- 自产 Methodology / Specification 的成熟度标签；
- 重大设计为什么采用 / 不采用既有方案。

## 9. Standardization Ladder（不要过早称为标准）

暂定成熟链：

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

Skill 与这条链正交。Skill 可以实现 Methodology 或 Specification，但不能替代其定义。

## 10. Prefer Reversible Decisions（优先可逆决策）

在需求尚未成熟时，优先选择后续容易迁移的实现：

- graph-native，但 database-agnostic；
- YAML 作为当前 source，不阻断 JSON-LD / RDF / API 输出；
- Renderer 可替换；
- Engine 与网站解耦；
- 不因一次实验冻结整个数据模型。

## 11. Record Decisions and Negative Evidence（记录决定，也记录为什么不选）

重要方法不仅记录“最终用了什么”，也应逐步记录：

- 调研过什么；
- 为什么不采用；
- 哪些限制是暂时的；
- 哪些问题尚未解决。

这样可以减少未来重复调查和重复犯错。

## 当前不是正式标准的原因

本文件目前只作为 IA 自身开发方法论。等这些原则经过更多实际项目、更多贡献者和可验证实践后，再判断是否有必要形成独立 Specification / Standard。
