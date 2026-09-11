# InteropAtlas Canonical Contract V1 Architecture — P4.1 Historical Draft

> Lifecycle: **Historical / Superseded by Active V1 Core Architecture**
>
> Original Phase: P4.1 — Canonical Contract V1 Architecture
>
> Primary Work Item: Issue #127
>
> Successor: `docs/architecture.zh-CN.md`
>
> Current Role: 保存 P4.1 阶段 Canonical Contract V1 的架构形成历史。经过后续 P5/P6 延续的核心边界已经提升并吸收到当前 V1 Core Architecture；本文不再作为 Living Architecture 或当前事实源。

## Historical synthesis

P4.1 将 Canonical V1 从“扩张一个万能 Object Schema”的方向收敛为：

> **Stable Canonical Core + explicit composable semantic contracts / profiles**

当时确定并在后续架构中延续的关键边界包括：

- Stable IA identity 与 display name、physical path、Source URL、external identifier 分离；
- Physical Storage ≠ Semantic Classification ≠ View；
- Relation 是一等知识资产，binary relation 不是通用表达上限；
- Source ≠ Evidence ≠ Assertion ≠ Assessment ≠ Provenance；
- Fact ≠ Assessment；
- Canonical State ≠ Generated View；
- Agent Output ≠ Canonical Fact；
- competing assertions、conflicting evidence 与 explicit unknown 可以保留；
- public knowledge lifecycle 与 personal attention / memory lifecycle 分离；
- Legacy compatibility 是迁移基础设施，而不是永久第二模型。

### Identity Contract

P4.1 区分 IA Canonical ID、External Identifier、Locator / Access Address、Human Name / Label，并明确相同名称、URL 或外部 identifier 都不能单独推出 same Canonical Subject。

Version / edition / snapshot / profile 的身份粒度当时有意留给真实数据压力测试，而不是在 P4 全局硬编码。

### Entity / Object Contract

P4.1 提出 Family 与 Kind 的职责分离：Family 保持少量、稳定，用于基础 semantic contract / profile family；Kind 更具体、可扩展，用于检索、约束和专用 Profile。两者都不重新决定物理目录，也不承载 authority / maturity / validity 等其他维度。

### Relation / Association Contract

Simple binary relation 被保留为常见 fast path，同时为 multiple participants、participant roles、qualifiers / context 等 richer association 保留架构空间。

### Knowledge Claim / Evidence Contract

P4.1 明确 Source、Evidence、Assertion、Assessment、Provenance 五类概念不能互相替代，并提出 Canonical acceptance 与 truth 是两个不同问题：接受进入 Canonical 表示通过项目 Intake / Review boundary，不表示不可争议的绝对真理。

### Lifecycle / State Contract

P4.1 拒绝用单一 `status` 表达全部生命周期，区分 Repository Record Lifecycle、Real-world Validity / Applicability、Publication / Version Status、Verification / Freshness、Authority / Confidence / Maturity Assessment、Supersession / Historical State 等正交维度。

### Deferred decisions

当时有意未冻结 final family/kind taxonomy、version identity granularity、richer association promotion criteria、Assertion / Evidence persistence granularity、Context / Scope attachment、lifecycle enums、conflict projection policy 与最终 YAML / JSON serialization。

这些 Not Yet 决策是 P4 Draft 的重要历史意义之一：它记录了项目明确选择“不在证据不足时过早冻结模式”。当前是否已经解决这些问题，应读取现行 Contracts / Profiles / PROJECT_STATE，而不是从本文推断。

## Supersession note

2026-09-05 文档生命周期审计确认：P4.1 已完成其阶段性职责，而原 `docs/architecture.zh-CN.md` 尚未充分吸收后续 V1 架构，导致 Draft 被迫长期承担 Living Architecture 的作用。

本轮已将仍有效的核心边界提升至 `docs/architecture.zh-CN.md`。因此本文进入 `03_Evolution/03_Change/` 保存设计历史，避免形成第二个 Canonical Architecture source。
