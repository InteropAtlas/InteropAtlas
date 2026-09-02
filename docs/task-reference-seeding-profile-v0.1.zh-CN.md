# InteropAtlas Task Reference Seeding Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Extension Profile
Document Created At: 2026-09-01T12:19:07+08:00
Document Updated At: 2026-09-01T12:19:07+08:00
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

> 状态：Draft / Extension Profile
>
> 关联：`open-collaboration-profile-v0.1.zh-CN.md`
>
> 目的：规定 Task Author 在发布 Human-ready / Agent-ready Work Item 时，如何复用 InteropAtlas 已有的 Standards / Mature Precedents / Methods / Implementations 作为已知起点，同时避免因过度依赖旧参考而产生锚定和过时问题。

## 1. 核心原则

> **Seed known references, still check for better or newer ones.**
>
> **预装已知依据，但仍检查更新、更完整或更合适的依据。**

Seed References 是任务启动资产，不是封闭答案集。

## 2. 规范关键词

本文中的 MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 按 BCP 14 理解。

## 3. 三类任务参考

### A. Read First / Upstream Contracts

表示执行者必须遵守的 InteropAtlas 自身定义、Specification、Schema、Decision 或 Governance Artifact。

例如：

```text
Read First
- docs/interopatlas-definition-and-scope-v0.2.zh-CN.md
- docs/knowledge-object-classification-specification-v0.1.zh-CN.md
```

这类引用是**任务约束**。

### B. Seed References

表示任务作者已经知道且与任务高度相关的外部 Standard / Precedent / Method / Implementation。

优先引用 Atlas Canonical ID：

```text
Seed References
- standard: iso_iec_25589_cd
- standard: iso_iec_5339_2024
- reference_project: w3c_browser_specs
```

必要时 MAY 同时给官方来源 URL。

这类引用是**已知起点**，不是任务约束本身。

### C. Freshness / Completeness Check

表示执行者是否仍需要查找：
- 新版本；
- 新标准；
- superseding artifact；
- 新成熟先例；
- 更适合当前场景的替代方案；
- Atlas 尚未收录的重要对象。

## 4. Requirements

### IA-TRS-001 — 已知高相关 Atlas 对象 SHOULD 预装

当 Task Author 已知 Atlas 中存在与任务高度相关的标准、成熟先例、方法或实现时，Work Item **SHOULD** 将其列入 Seed References。

目的不是减少研究质量，而是避免重复从零发现基础材料。

### IA-TRS-002 — 优先引用 Stable Atlas ID

如果对象已经 Canonicalized，Task **SHOULD** 优先引用稳定 Atlas ID，而不是只复制自然语言名称或搜索结果 URL。

这样后续可支持：
- 自动展开对象摘要；
- 检查 superseded / deprecated；
- 查看关系和替代方案；
- 统计任务依赖了哪些知识对象。

### IA-TRS-003 — Seed Reference MUST NOT 被当作完整答案

Executor **MUST NOT** 因任务作者给出 Seed References 就假定：
- 参考集合完整；
- 参考仍是最新；
- 参考一定是最佳方案；
- 没有其他标准或替代先例。

### IA-TRS-004 — 需要外部研究的任务 SHOULD 做 Freshness Check

对于 standards research、prior-art study、architecture decision、security、AI governance、Human Interface 等会随时间变化的任务，Executor **SHOULD** 在开始实质结论前执行 Freshness / Completeness Check。

### IA-TRS-005 — 新发现 SHOULD 回流 Atlas

如果任务执行过程中发现：
- 新标准；
- 新版本；
- 成熟先例；
- superseding relation；
- Atlas 当前模型无法表达的重要对象；

Executor **SHOULD**：
1. 在当前任务中记录发现；
2. 能准确建模时纳入 Atlas 或创建 intake task；
3. 无法准确建模时登记 Model Gap，而不是忽略。

这形成：

```text
Atlas Seed References
      ↓
Task Research
      ↓
New / Updated References
      ↓
Feed Back to Atlas
      ↓
Better Seed References for future tasks
```

### IA-TRS-006 — Task Author 不需要穷举

Task Author **SHOULD NOT** 为了发布任务而先完成一遍执行者本应完成的完整研究。

任务发布阶段只需要提供：
- 明显关键的已知依据；
- 上位规范；
- 必要风险提示。

这样避免把节省执行者时间变成过度增加任务作者负担。

## 5. 推荐模板

```text
Read First / Upstream Contracts
- IA definition/spec IDs or repository paths

Seed References
- standard: <atlas-id>
- reference_project: <atlas-id>
- method: <atlas-id>        # 等 #15 模型完成后使用
- implementation: <atlas-id>

Freshness Check
- required: yes/no
- check for: new version / superseding standard / alternatives / new precedent
```

## 6. 与 Open Collaboration Profile 的关系

本 Profile 扩展 `IA-OC-003 Agent-ready / Contributor-ready Work Item`。

未来 Open Collaboration Profile 下一版本 SHOULD 把以下字段合并进主 Work Item Contract：

1. Read First / Upstream Contracts；
2. Seed References；
3. Freshness / Completeness Check。

在此之前，本 Extension Profile 与 `open-collaboration-profile-v0.1` 共同构成当前 Task Authoring 规范输入。

## 7. 对 InteropAtlas 的长期价值

Reference Seeding 让 Atlas 不再只是“查询结果数据库”，而开始成为自身协作系统的知识缓存：

```text
第一次研究成本
      ↓
结构化进入 Atlas
      ↓
后续任务直接复用
      ↓
执行者只补新增 / 变化 / 缺口
      ↓
研究边际成本下降
```

这也是 Practice-driven Feedback Loop 在协作层的一个直接应用。
