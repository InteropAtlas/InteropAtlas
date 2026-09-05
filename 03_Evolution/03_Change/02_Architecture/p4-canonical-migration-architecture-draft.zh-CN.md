# Canonical Migration Architecture V1（P4.3 Historical Architecture Draft）

> Lifecycle: **Historical / Completed P4 Architecture Artifact**
>
> Original Phase: P4.3 — Migration Architecture
>
> Primary Work Item: Issue #127 — completed / closed
>
> Current Role: 保存 P4.3 对 Legacy / V0 → Canonical Contract V1 迁移边界的设计历史；**不再作为 `docs/` 中的当前 Living Architecture 入口。** 当前架构与执行状态应从 Master Design、当前 Canonical contracts、PROJECT_STATE 与后续 P5/P6 工作项读取。
>
> Provenance: 本文件由原 `docs/canonical-migration-architecture-draft.zh-CN.md` 在文档生命周期审计中迁移而来；正文保持原 P4.3 设计内容。

## 1. 目的

InteropAtlas 已明确选择：保留现有知识资产、stable IDs、来源与 provenance 历史，同时建立干净的 Canonical Contract V1，而不是全仓推倒重来，也不是让 V0 与 V1 永久并存。

因此 Migration Architecture 的任务不是“把旧 YAML 改成新 YAML”，而是建立一条可审计、可验证、可分批、可纠错、最终可退役 Legacy compatibility 的语义迁移路径。

核心原则：

> **Migration is a governed semantic transformation, not a bulk text rewrite.**

## 2. Migration boundary

迁移必须区分至少四层：

1. **Knowledge Asset Preservation** — 保留对象、关系、来源、证据、历史贡献等已有知识资产；
2. **Semantic Mapping** — 将 Legacy 字段/类型/关系语义映射到 V1 contract；
3. **Canonical Acceptance** — 映射结果必须经过 P4.2 Write / Intake 的 validation / review / authority gate；
4. **Compatibility Retirement** — Legacy reader/normalizer/alias 只作为过渡能力，并有明确退役条件。

不得把“机器能转换”直接等同于“语义已经正确迁移”。

## 3. Stable identity preservation

### 3.1 默认规则

Legacy Canonical Subject 已有 IA stable ID 时，迁移默认**保留原 ID**。

以下变化本身不得触发 ID 重建：
- 文件路径变化；
- display name / 翻译变化；
- `type/kind` 分类模型变化；
- URL / locator 变化；
- Schema generation 变化；
- binary relation 升级为 richer association representation。

### 3.2 Identity-affecting migration

若迁移发现旧数据实际上混合了多个 subject、重复创建了同一 subject，或 version/work 边界错误，则不得由 migration script 静默修正。

这些情况必须提升为高影响 mutation：
- merge；
- split / unmerge correction；
- canonical redirect / alias；
- identity reassignment；
- destructive removal。

它们需要独立 evidence / rationale / provenance，并按 P4.2 的高影响 review / authority gate 处理。

## 4. Mapping classes

每个 Legacy → V1 映射至少归入以下一种类别：

### A. Lossless structural mapping

语义不变，仅表达结构变化。例：字段重命名、数组/对象结构标准化、明确 namespace 后的 identifier 搬迁。可高度自动化，但仍需 Machine Review。

### B. Normalization mapping

多个 Legacy 表达收敛到同一 V1 semantic slot。需要验证旧字段是否真的语义等价，不能只按字段名批量替换。

### C. Semantic promotion

旧模型中隐含或弱结构化的信息提升为更明确的 V1 语义结构。必须保留原始来源与转换依据。

### D. Ambiguous / review-required mapping

无法仅凭结构确定正确 V1 语义的记录必须进入人工 / 独立 review，不得由批处理猜测。

### E. Identity-affecting mapping

涉及 merge / split / reassignment / destructive removal 的情况单独治理，不与普通 migration batch 混合。

## 5. Batch migration

迁移应采用小批次、可审计、可回滚的方式，而不是一次性全仓重写。每批至少应记录：

- 输入对象 / relation 集合；
- mapping class；
- 使用的 converter / normalizer 版本；
- validation 结果；
- review / authority 结果；
- before / after identity mapping；
- unresolved / ambiguous records；
- regression / graph checks；
- rollback boundary。

批次应优先按风险与语义相似度组织，而不是仅按文件数量平均切片。

## 6. Validation layers

每个 migration batch 至少通过：

1. structural/schema validation；
2. stable identity preservation check；
3. reference / relation resolution；
4. provenance / evidence preservation；
5. semantic review for non-lossless mappings；
6. graph / count / route regression；
7. explicit unknown / conflict preservation where applicable。

机器验证不能替代语义审查，但语义审查也不应替代可自动执行的回归检查。

## 7. Compatibility layer

Legacy compatibility 是迁移基础设施，不是长期产品能力。

允许的过渡机制包括 legacy reader、normalizer、alias、compatibility projection 或明确的 conversion tooling，但必须满足：

- compatibility 不成为第二 Canonical truth；
- 新写入默认面向 V1 contract；
- legacy-only behavior 可被观测和统计；
- 有明确 retirement criteria；
- 不因“兼容方便”无限延长双模型状态。

## 8. Retirement endpoint

Legacy compatibility 只有在至少满足以下条件后才可退役：

- 目标范围内 Canonical assets 已完成 V1 migration / acceptance；
- legacy-only references 已清零或有显式保留理由；
- current runtime / renderer / validation 不再依赖 legacy-only semantics；
- regression baseline 通过；
- rollback / historical recovery 不依赖继续运行 legacy model；
- Maintainer 明确批准 retirement。

退役 legacy compatibility 不等于删除历史。历史数据、mapping evidence 与迁移记录仍应可恢复。

## 9. P5 handoff

P4.3 不冻结所有 migration mapping。以下问题应由真实数据实验验证：

- 不同 Legacy family/kind 的映射是否真的稳定；
- richer relation / association promotion 的真实频率；
- source / evidence / provenance 拆分会产生多少 ambiguous cases；
- 自动转换能够覆盖多少记录；
- 哪些对象需要人工 semantic review；
- batch size 与 review cost 的实际关系；
- compatibility retirement 是否存在未识别依赖。

P5 应以代表性真实数据集测试这些假设，再决定 P6 的迁移实现和批次顺序。

## 10. Historical conclusion

P4.3 的结论是：InteropAtlas 不把 V1 migration 视为文件格式升级，而把它视为**受治理的语义迁移**。Stable identity、evidence/provenance、冲突与未知边界优先于批量转换速度；Legacy compatibility 必须从一开始就拥有 retirement endpoint。
