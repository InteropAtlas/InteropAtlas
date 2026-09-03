# Canonical Migration Architecture V1（Architecture Draft）

> Status: Architecture Draft
>
> Phase: P4.3 — Migration Architecture
>
> Primary Work Item: Issue #127
>
> Scope: 定义 Legacy / V0 → Canonical Contract V1 的迁移架构；**本文件不执行任何数据迁移，不冻结最终 Schema，也不授权破坏性变更。**

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

语义不变，仅表达结构变化。

例：字段重命名、数组/对象结构标准化、明确 namespace 后的 identifier 搬迁。

可高度自动化，但仍需 Machine Review。

### B. Normalization mapping

多个 Legacy 表达收敛到同一 V1 semantic slot。

例：`website` / `official_url` / locator-like fields 的角色归一；旧 `type` 与 `kind` 两代模型向 family/kind contract 收敛。

需要验证旧字段是否真的语义等价，不能只按字段名批量替换。

### C. Semantic promotion

旧数据中隐含或压缩的知识，需要升级为显式 V1 construct。

例：
- 一个模糊 `status` 拆成 publication / validity / verification / repository lifecycle 等不同维度；
- binary edge 在必要时升级为 identified relation / participants + roles + qualifiers；
- 某属性因存在独立 evidence/conflict/review 需求而提升为 Assertion。

默认需要更强语义审查。

### D. Ambiguous / unresolved mapping

无法从现有 Legacy 数据可靠决定 V1 表达。

必须保留为：
- unknown；
- not recorded；
- unverified；
- disputed / competing；
- migration decision pending；

而不是猜测、补默认值或伪造确定性。

### E. Identity / destructive transformation

涉及 merge、split、删除、ID 重定向、重大语义重解释等高影响变化。

不得作为普通批量迁移执行。

## 5. Unknown, conflict and information loss

迁移不得通过“清洗”消除真实的不确定性。

### 5.1 Unknown preservation

Legacy 缺失值必须先判断其含义，而不是统一转成 `null`：
- unknown；
- not recorded；
- not applicable；
- unverified。

最终词汇由 P5 real-data validation 决定。

### 5.2 Conflict preservation

若 Legacy 中存在相互冲突的来源、字段值或关系：
- 不以“最后写入值”自动获胜；
- 不因迁移方便而删除 minority/older assertion；
- 能识别时转成 competing Assertions + Evidence / Assessment；
- 无法可靠拆解时标记为 unresolved migration case，进入人工/独立 Agent review。

### 5.3 Loss report

任何有损迁移都必须能产生显式 loss / ambiguity report，说明：
- 哪些信息无法映射；
- 哪些语义被降级；
- 哪些需要后续补证；
- 哪些需要 Owner / Maintainer 决策。

## 6. Batch migration unit

不得全仓一次性迁移。

推荐最小批次按“可独立验证的 semantic cohort”组织，而不是机械按文件数量切片。例如：
- 同一 object family/kind；
- 同一 relation type；
- 同一 Legacy schema generation；
- 同一明确 mapping rule；
- 一组代表性 edge cases。

每批必须能够单独：
1. inventory；
2. map；
3. dry-run；
4. validate；
5. review；
6. accept/reject；
7. record provenance；
8. rollback/correct。

P5 应先用代表性真实数据做 pressure test，再决定批次规模。

## 7. Migration pipeline

建议的 V1 migration pipeline：

```text
Legacy Inventory
→ Semantic Classification
→ Mapping Plan + Mapping Class
→ Dry-run Transformation
→ Structural / Schema Validation
→ Relation Compatibility + Graph Checks
→ Semantic Diff / Loss & Ambiguity Report
→ Independent Review
→ Authority Gate when required
→ Canonical Acceptance
→ Provenance Record
→ Post-migration Verification
→ Legacy Compatibility Retirement Check
```

其中任何一步失败，都不应把部分结果静默写入 Canonical。

## 8. Validation contract

每个 migration batch 至少需要四类验证：

### 8.1 Structural validation
- serialization 可解析；
- V1 contract/schema compatibility；
- required identity/reference constraints；
- no accidental field loss。

### 8.2 Relation / graph validation
- endpoints / participants 可解析；
- stable ID references preserved；
- no unintended dangling references；
- graph topology change 可解释；
- binary → rich relation upgrade 不应被误判为 real-world relation change。

### 8.3 Semantic validation
- mapping rule 与 Legacy 实际含义一致；
- `status/maturity/source/url/type/kind` 等历史漂移没有被机械归一；
- unknown/conflict preserved；
- generated/default values 不伪装成 sourced facts。

### 8.4 Provenance validation
- migration batch 可追溯；
- mapping rule/version 可追溯；
- executor/reviewer 可追溯；
- accepted canonical mutation 与原 Legacy record 可关联。

## 9. Rollback and correction

Git revert 只是最低层恢复机制，不等于完整 semantic rollback。

Migration Architecture 必须支持：
- batch-level rollback；
- correction without losing original provenance；
- identity merge 的 redirect / split correction path；
- migration rule versioning；
- failed/partial migration 的明确状态；
- re-run 时避免重复生成或重复接受同一 mutation。

原则：

> **A migration mistake must remain diagnosable after it is corrected.**

## 10. Legacy compatibility layer

Legacy compatibility 是临时桥梁，不是永久架构。

可以存在：
- reader compatibility；
- normalizer / adapter；
- field alias；
- V0 → V1 projection；
- migration diagnostics。

但不得形成：
- 两套都能长期直接写 Canonical 的双写模型；
- 新功能继续依赖 V0-only semantics；
- 为保持旧格式而污染 V1 contract；
- 无截止条件的 compatibility debt。

### Retirement endpoint

Legacy compatibility 只有在以下条件满足后才可退役：
1. scope 内 Legacy assets 已完成 inventory；
2. 已迁移或被显式分类为 retained exception；
3. stable IDs / references 已验证；
4. Machine Review / Graph checks 对 V1 路径通过；
5. no active canonical writer depends on Legacy contract；
6. unresolved ambiguity 已有公开 backlog / exception record；
7. retirement change 通过相应 Maintainer / authority review。

退役不等于删除历史。Git history、migration provenance、必要的 archival fixtures 应继续保留。

## 11. Interaction with P4.2 Write / Intake

Migration 不建立第二条 Canonical 写入通道。

Migration 产生的 transformation 应被视为 Proposal / Patch / Candidate canonical mutation，进入同一 Write / Intake governance：

```text
Migration transformation
→ Candidate Patch / Assertions
→ Validation
→ Semantic Review
→ Authority Gate when required
→ Accepted Canonical Mutation
```

因此：
- migration automation 可以执行 transformation；
- automation 不自动拥有 acceptance authority；
- identity/destructive migration 必须升级 review；
- GitHub merge permission 不等于 semantic acceptance authority。

## 12. P5 validation matrix

以下内容在 P4 不冻结，进入 P5 用真实数据验证：

| Question | Representative pressure test |
| --- | --- |
| family/kind mapping | Capability / Organization 两代 typing |
| locator/source mapping | `official_url` / `website` / `sources[].url` |
| lifecycle split | legacy `status` / `maturity` |
| version identity | RFC / ISO edition / W3C living or versioned standards |
| relation promotion | simple binary vs participant-role relation |
| assertion promotion | conflicting or independently evidenced property |
| unknown semantics | missing vs unknown vs not applicable |
| conflict preservation | contradictory source claims |
| ID preservation | rename / classification change / file relocation |
| merge/split gate | duplicate candidate / false equivalence correction |

## 13. Not Yet Schema / implementation decisions

本文件明确不决定：
- migration manifest 的最终 serialization；
- mapping rule DSL；
- V1 schema filenames / folder layout；
- exact unknown-state enums；
- exact lifecycle enums；
- relation instance ID serialization；
- automated confidence thresholds；
- batch size；
- CI job names；
- Legacy compatibility 的具体代码删除日期。

这些应在 P5 真实数据实验与 P6 implementation 中决定。

## 14. Settled P4.3 architecture decisions

P4.3 第一轮架构边界确认：

- 迁移是 governed semantic transformation，不是 bulk rewrite；
- 已有 IA stable ID 默认跨 Schema generation 保留；
- taxonomy / path / display-name 变化不构成 identity migration；
- mapping 分为 lossless、normalization、semantic promotion、ambiguous、identity/destructive 等不同风险等级；
- unknown/conflict 必须保留，不得由 migration 猜测消除；
- migration 采用小批次、dry-run、semantic diff、Machine Review、Graph check、独立 review；
- migration 不绕过 P4.2 Write / Intake Contract；
- rollback/correction 必须保留 provenance；
- Legacy compatibility 是临时桥梁，必须有 retirement endpoint；
- P4 只设计 migration architecture，P5 才做代表性真实数据 pressure test，P6 才进入系统化 implementation/migration。

## 15. Next

P4.3 完成第一轮后，进入 **P4.4 Selection / Projection / Workspace Architecture**：定义 Canonical State 如何被 Search / Compare / Map / Timeline / Wiki / task workspace 等读取、筛选、组合和呈现，同时继续保持 `Canonical ≠ Projection` 与 `Readable Projection ≠ Updatable Projection`。