# InteropAtlas 项目建设与实践反馈模型（Project Development & Practice Feedback Model）

<!-- InteropAtlas Document Metadata v0
Document Status: Provisional Methodology / Long-term Core Method
Document Created At: 2026-09-05T14:40:00+08:00
Document Updated At: 2026-09-05T18:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 本文是项目建设方法与实践反馈机制的 Primary Home。它描述 IA 怎样持续建设、学习和反馈，不建立第二套 Roadmap。

## 1. 建设原则

InteropAtlas 默认遵循：

> **Adopt → Profile → Extend → Invent**

创建新的 Relation、Schema、ID 体系、验证机制、版本规则、仓库模板、方法论或规范之前，先检查成熟 Prior Art；能采用就采用，不完全适用就 Profile，仍不足才做最小扩展，只有真实缺口才发明 IA 自有机制。

同时保持：Evidence Before Assertion、Fact ≠ Assessment、Canonical ≠ Generated View、Human 与 Agent 共享同一知识世界、Prefer Reversible Decisions、Record Decisions and Negative Evidence。

## 2. 项目计划采用持续演化，不采用项目级版本路线

InteropAtlas 的项目本身、长期路线、Living Documents 和 Owner View 不以 `V1 / V2` 或连续 `P1 / P2 / P3...` 作为规划骨架。

历史阶段和旧版本称呼只保留在 Git history、closed Issues 和 Evolution 中。当前计划按以下关系组织：

```text
长期使命 / 产品哲学
        ↓
长期能力域
        ↓
当前主线
        ↓
真实 Work Item
```

`PROJECT_STATE.md` 是 Owner 和新 Agent 查看当前主线的首要入口；Issue / PR 承载执行细节。

版本号只在对象本身确实具有版本身份或兼容边界时使用，例如外部标准特定版本、协议、Schema、兼容契约、发布制品或历史快照。不要把它扩展成项目计划版本号。

## 3. 实践反馈环

InteropAtlas 不应只靠抽象设计积累知识。真实项目、真实建设步骤和真实技术选择，应持续作为 Atlas 的使用场景和验证实验；Atlas 中积累的标准、能力、关系与证据又反过来指导真实项目。

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

这不是一次性建设阶段，而是长期运行机制。

## 4. Atlas → Practice / Practice → Atlas

Atlas 应帮助真实项目发现标准、协议、方法与实现，找到替代路线，理解依赖、兼容、Profile 与约束，并为技术选择提供可验证知识。

真实实践应帮助 Atlas 暴露遗漏对象、缺失 Relation、Capability / Scenario / Evidence 模型不足、界面可用性问题、Open Gap、实现缺口和真实兼容性问题。

## 5. Alternative Discovery 是默认步骤

发现第一个满足 Capability 的方案不代表检索结束。应继续检查：

1. 是否存在解决相同或相似 Capability 的其他方案；
2. 它们的标准化性质是否不同；
3. 是否需要 `alternative_to`、`extends`、`profiles`、`compatible_with` 等关系；
4. 各路线优化什么、限制是什么；
5. 未采用候选及原因是否值得保留为实践证据。

SemVer / CalVer 的早期实践说明：找到一个可用方案，不等于已经看见主要方案空间。

## 6. 覆盖与反馈

### Standard Coverage

回答：面对一个 Scenario / Capability，实际需要的重要标准、规范、协议或约定，Atlas 已经收录多少？只有候选集合边界足够明确时才计算百分比。

### Solution-Space Coverage

回答：Atlas 是否呈现主要可行路线，而不是只找到第一个能用的方案？重点检查替代方案、关键关系、适用条件、限制和搜索偏差。

覆盖率本身不是最终目标。真正的问题始终是：

> **当真实项目需要互操作知识时，InteropAtlas 到底能帮助到什么程度？**

## 7. 当前运行原则

每一次 InteropAtlas 自身建设，都尽可能同时完成：

1. **Build** — 完成当前真实建设任务；
2. **Learn** — 发现缺失的标准、关系、能力、方法或工具；
3. **Feed Back** — 把可复用事实、证据、缺口与方法回流 Atlas。

当前主线不通过阶段编号判断，而通过 `PROJECT_STATE.md` + GitHub Ready / In Progress Work Items 判断。

> **InteropAtlas 不只是描述互操作世界，也持续通过真实实践检验自己对这个世界的描述。**
