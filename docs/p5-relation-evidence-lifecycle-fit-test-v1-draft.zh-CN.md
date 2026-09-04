# P5 Relation + Evidence / Assertion / Conflict + Lifecycle Fit Test v1 — Draft

> Status: P5 Research / Fit Test Draft
>
> Work Item: #132
>
> Checked At: 2026-09-04
>
> Scope: 小批量真实场景压力测试；不修改生产 Relation Schema，不执行全量迁移，不 stable-promote P4 drafts。

## 1. First checkpoint

本轮先不发明新的生产字段，而是用现有 IA Relations + #130 的真实标准样本，判断 P4.1 的关系、证据和生命周期边界是否足够。

核心问题不是“Relation YAML 应该长什么样”，而是先判断真实世界至少需要哪些不同语义层。

## 2. Scenario matrix

| Scenario | Existing / real case | What is being tested | Initial result |
| --- | --- | --- | --- |
| S1 simple binary | `engine_v0_1_bootstrap uses semantic_versioning_2_0_0` | source-predicate-target 是否足够 | yes: binary fast path 足够；notes/provenance 可附加但不改变参与者结构 |
| S2 qualified binary | Apple HIG `provides` web accessibility | relation 带 capability context + scope conditions | binary endpoints 仍足够，但 assertion 需要 qualifier/context；不能把条件压进 predicate 名称 |
| S3 relation vocabulary mismatch | RFC 3339 vs ISO 8601 | V0 只有 `extends`，但记录自身说明更准确语义是 `profile_of` | relation type 不足会造成语义损失；应保留 unresolved semantic mismatch，而不是把近似 predicate 当事实 |
| S4 composite / participant roles | BCP 14 + RFC 2119 + RFC 8174 | 多个 publication 共同参与一个 maintained practice | 简单 `A -> version -> B` 不足；需要能表达 participant role / composition semantics 的 rich association 或显式关系组 |
| S5 same participants, different occurrence semantics | publication/work pairs | 同一对对象可同时存在 `updates`, `part_of`, `profile_of`, `supersedes` 等不同事实 | participant set 不能作为 relation identity；predicate/context/occurrence 必须参与区分 |
| S6 evidence-supported stable fact | Apple HIG `governed_by` Apple | 官方来源直接支持低争议关系 | compact relation + source evidence 可作为 fast path；Source 仍不等于 Assertion 本身 |
| S7 evidence gap / provisional assertion | RFC 3339 `extends` ISO 8601 approximation | 已知当前 predicate 只是近似 | 必须能表示 unverified/provisional/semantic-gap，而不是只有 confidence 数字 |
| S8 historical / supersession lifecycle | ISO/IEC 27001:2013 vs 2022 | publication status、supersession、IA record lifecycle 是否正交 | superseded publication 不等于删除/archived IA record；历史对象仍应可查询 |
| S9 source freshness vs IA verification | HTML Living Standard / Apple HIG / A2A current pages | upstream mutable revision 与 IA `last_verified_at` | 两种时间必须分离；网页更新不自动等于 IA record update，IA verification 也不定义 publisher status |
| S10 conflicting assertion | generic conflicting-source case seeded from P4 contract | 同一 subject/predicate 出现 support/refute 或 incompatible assertions | 不能 last-writer-wins；冲突应保留为并存 Assertions + Evidence/Assessment，Canonical 可记录 disputed state |

## 3. Binary fast path boundary

第一批真实 V0 Relations 说明，简单二元边仍然有价值。例如 Engine `uses` SemVer，以及 Apple HIG `governed_by` Apple，都可以自然表达为：

`subject -> predicate -> object`

但 binary fast path 的成立条件应该是：

1. 两个 endpoint 足以定义参与者结构；
2. predicate 的语义无需 participant roles 才能理解；
3. qualifier/context 即使存在，也只是限定 assertion，不改变“谁以什么角色参与”；
4. 不需要把多个 relation occurrence 合并成一个复杂事件/组合结构。

因此 V1 不应为了“语义纯洁”把所有边都强制对象化成重型 Association。

## 4. Promotion to rich association

出现以下任一压力时，应允许从 binary fast path promotion：

- 三个或更多参与者共同定义事实；
- participant role 是事实语义的一部分；
- relation occurrence 自身需要稳定引用；
- 多个 qualifier/context 共同决定事实含义；
- 需要把一组参与关系作为一个组合事实评审；
- 简单 predicate 会把 composition/profile/amendment/errata 等语义压扁。

BCP 14 是当前最强的 promotion candidate：把 RFC 2119 和 RFC 8174 当作 `versions[]` 会损失“多个独立 publication 共同构成 maintained BCP”的结构。

## 5. Relation occurrence ≠ Assertion ≠ Evidence

真实 V0 数据里已经存在把这些层揉在一起的迹象：

- relation record 表示一个关系 occurrence；
- `sources[]` 给出来源；
- `confidence` 给出某种评估；
- `notes` / `conditions` 又携带 assertion 限定与语义 caveat。

P5 暂时确认 P4 的分离方向：

- **Relation / Association**：参与者和关系结构；
- **Assertion**：IA 对某个关系/属性事实提出的可评审陈述；
- **Source**：信息来源载体；
- **Evidence**：Source 中实际支持或反驳 Assertion 的证据；
- **Assessment**：对 Assertion/Evidence 的可信度、争议、验证状态等判断；
- **Provenance**：该记录/判断如何进入 IA、由谁执行/审查、何时发生。

这些概念可以在低争议 fast path 中压缩存储，但语义上不能等同。

## 6. Concrete problem found: approximate predicates can masquerade as facts

现有 `rfc3339_profiles_iso8601` relation 使用：

`RFC 3339 --extends--> ISO 8601`

但它自己的 `notes_zh` 已明确写明：RFC 3339 自称 ISO 8601 的 Internet profile，而当前 relation vocabulary 因没有 `profile_of`，才暂时用 `extends` 近似。

这是 #132 第一个非常具体的 V0 风险：

> 当 vocabulary 不够精确时，机器只看到 `extends`，却看不到“这是近似表达”的语义等级。

因此 V1 至少需要保证：

- exact assertion 与 approximation/provisional mapping 可区分；
- vocabulary gap 不应通过一个看似确定的 predicate 被静默隐藏；
- 后续 vocabulary 增强时可以纠正语义，而不丢失原始来源和审查历史。

这不等于现在立即新增生产 `profile_of` relation type；P5 只记录压力并验证 contract。

## 7. Lifecycle orthogonality

第一批场景继续支持“无万能 status”原则。至少需要概念上区分：

- IA repository record lifecycle；
- publisher publication lifecycle；
- applicability/adoption lifecycle；
- supersession/historical relation state；
- verification freshness；
- assertion dispute/verification state。

例如一个 2013 edition 可以同时：publisher 层面 withdrawn/superseded、IA 层面仍 active/readable、历史研究层面仍 applicable to legacy systems、verification 层面 recently verified。

这些状态不能被一个 `status: deprecated` 压扁。

## 8. First-checkpoint conclusions

目前没有发现需要推翻 P4.1 的问题，反而出现了一个明确的生产迁移风险：**V0 relation vocabulary 不足时，近似 predicate 可能被机器误读为精确 Canonical fact。**

P4.1 下列方向通过第一轮真实压力测试：

- binary Relation 保留 fast path；
- rich Association 按复杂度 promotion，而非默认重型化；
- relation occurrence 与 Assertion / Evidence / Assessment / Provenance 分离；
- conflict 不使用 last-writer-wins；
- unknown / provisional / disputed 不能压成 confidence 数字；
- lifecycle 多维正交。

## 9. Next checkpoint

下一步只补两类证据，不扩大范围：

1. 从现有 Relations 中再找一个真正需要 qualifier/context 的案例，确认它是否仍可保持 binary fast path；
2. 为 conflicting assertion + evidence gap 做最小实验表示，验证 Source/Evidence/Assertion/Assessment 分层是否会过度复杂。

如果这两类通过，就可以收束 #132，而不是继续无限增加 relation types。
