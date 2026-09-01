# InteropAtlas Repository Structure Profile v0.1

> 状态：Draft / Provisional Specification（已应用 #31 Corrigendum）
>
> 关联：Issue #21、#31。
>
> 本 Profile 定义仓库的职责边界、Artifact identity 与迁移约束。它**不再把知识对象分类映射成文件夹分类**，也不在本文发布时自动执行目录迁移。

## 1. 核心修正

早期 v0.1 一方面规定“Artifact / object identity 不得依赖目录”，另一方面又把未来 Canonical Data 画成：

```text
data/
  standards/
  capabilities/
  implementations/
  organizations/
  scenarios/
  reference-projects/
  relations/
  gaps/
  maps/
```

这两个设计存在内在矛盾。

#31 后采用以下原则：

> **物理存储 ≠ 知识分类 ≠ 索引 / 视图。**

- 物理目录只解决文件怎样存、怎样被工具找到、怎样维护；
- 对象是什么，由对象自身 `id / type / kind / roles / fields` 等数据合同表达；
- 对象之间怎样分类、归组和连接，由引用、Relation、Graph、Index、Map、Query 表达；
- 一个对象可以同时出现在多个动态分类 / 视图中，而无需复制文件；
- Standard、Method、Design System、Mature Precedent、Implementation 等**不需要因为语义类别不同而住在不同文件夹**。

因此，旧的 `data/<object-family>/` 目标树 **WITHDRAWN / SUPERSEDED**。它不再是已接受迁移目标。

## 2. 仍然有效的上位依据

本 Profile 继续采用以下成熟约束与先例：

- GitHub Community Health / Issue & PR Templates：平台原生公共项目入口；
- GitHub CODEOWNERS / Rulesets / Required Review：ownership / review 原语；
- REUSE Specification 3.3：`LICENSES/` 等许可证布局约束；
- OpenSSF Best Practices / Scorecard：安全、Review、CI、维护实践；
- W3C browser-specs / MDN BCD / CNCF Landscape / SPDX License List：Data、Schema、Tooling、Generated Output 分工；
- Diátaxis / Docs as Code：面向人的文档组织和版本化工作流；
- InteropAtlas 自身实践：当前路径耦合、Graph / Renderer / Loader 的真实迁移风险。

但这些来源**没有要求** InteropAtlas 必须按 ontology 类别建立物理目录。

## 3. 核心决策

### RS-D1 — 当前采用 Layered Monorepo

**Decision: ACCEPTED.**

InteropAtlas 当前继续保持单仓。Canonical Data、Schema、Engine、Validator、Renderer、项目规范与研究仍处于高频共同演化阶段，现在拆成多个仓库会增加协作成本。

### RS-D2 — Storage 与 Semantics 必须解耦

**Decision: ACCEPTED.**

Canonical Data 的物理路径 **MUST NOT** 决定对象的知识身份。

目录名 **MUST NOT** 被 Loader、Validator、GraphIndex 或其他核心工具当作判断 `standard`、`relation`、`method`、`implementation` 等语义类型的依据。

语义分类 **MUST** 来自机器可读对象数据与引用 / Graph contract。

### RS-D3 — Canonical Data 需要明确的存储边界，但名字与内部布局未决定

**Decision: RESPONSIBILITY ACCEPTED; PHYSICAL LAYOUT REOPENED.**

Canonical Facts 应具有可发现、可配置、可验证的物理存储边界。

但是以下问题全部重新进入讨论：

- 根目录是否使用 `data/`、其他名字，或其他结构；
- Canonical Data 内部是否完全平铺；
- 是否因文件数量、维护、分片、性能等**技术原因**建立子目录；
- Relations / Maps 是否需要独立物理区。

这些决定**不得从旧 object-family 目录自动继承**。

### RS-D4 — Artifact identity 必须可区分，物理一级目录另行讨论

**Decision: LOGICAL DISTINCTION ACCEPTED; ROOT PLACEMENT REOPENED.**

以下 Artifact identity 仍然必须可区分：

- Canonical Data Object；
- Schema / Contract；
- IA-produced Specification / Profile；
- Research / Prior Art / Fit Test / Audit；
- Architecture / User Documentation；
- Governance Policy；
- Experiment；
- Implementation / Tooling；
- Generated Artifact / View。

但“逻辑上必须区分”**不等于**“每一种都必须成为 root 一级目录”。

`specs/`、`research/`、`governance/`、`docs/`、`tests/` 等旧目标位置从现在起视为 **candidate / pending discussion**，不是自动批准的最终 root tree。

### RS-D5 — Generated Site / Export 永不成为第二事实源

**Decision: ACCEPTED.**

Generated HTML、Markdown、JSON/RDF export、indexes 等必须能够从 Canonical Facts / Contracts 再生成，不得成为竞争事实源。

### RS-D6 — AGENTS.md 是 Agent Instructions，不是项目本体

**Decision: ACCEPTED.**

AGENTS.md 不得替代 README、CONTRIBUTING、Governance 或领域 Specification。

## 4. Artifact Taxonomy

| Artifact Class | 主要职责 | Canonical Fact? |
|---|---|---:|
| Canonical Data Object | 对现实互操作知识对象的结构化事实 | 是 |
| Schema / Contract | 定义数据和接口允许的结构 | 否 |
| Specification / Profile | IA 自产的规范要求 | 否 |
| Research / Prior Art / Fit Test | 调研、方案比较、证据汇总 | 否 |
| Architecture / Documentation | 帮助理解、使用、贡献项目 | 否 |
| Governance Policy | 角色、授权、生命周期、治理约束 | 否 |
| Experiment | 可复现探索、fixture、prototype、结果 | 否 |
| Implementation / Tool | Engine、Validator、Renderer、CLI、维护工具 | 否 |
| Generated Artifact / View | 网站、export、报告、动态索引 | 否 |

### Artifact identity invariant

Artifact identity **MUST NOT** 只依赖目录位置。

同样，Canonical Data 内部的知识分类 **MUST NOT** 只依赖目录位置。

## 5. 三层结构模型

以后讨论仓库结构时，必须把三个问题分开：

```text
A. Physical Storage
   文件实际放在哪里？

B. Semantic Model
   对象是什么？type / kind / role / relation 是什么？

C. Projection / Navigation
   用户或 Agent 想按什么维度看？有哪些 Index / Map / Query？
```

例如一个 GOV.UK Design System 对象可以只有一个物理文件，但通过 Graph 同时出现在：

- Design System；
- Human Interface reference；
- Accessibility precedent；
- Government service precedent；
- Pattern library related view。

不需要为了这些视图复制文件，也不需要五个文件夹。

## 6. Normative Requirements

### IA-RS-001 — Root 是公开项目入口

Root **MUST** 优先服务第一次进入仓库的人类贡献者和通用工具；**MUST NOT** 演化成 Agent 私有状态或临时工作文件集合。

### IA-RS-002 — Canonical Storage 必须可发现和可配置

Loader / CI / Tooling **SHOULD** 通过明确的 repository storage contract 获取 Canonical Data 当前物理位置。

当前存在多个 root 目录，只能被视为 **legacy physical storage locations**，不得解释成未来 ontology layout。

### IA-RS-003 — 目录不得定义知识分类

一个对象的 `type / kind / roles` **MUST NOT** 由其所在目录推断。

Relation **MUST** 因对象数据声明 `type: relation` 而成为 Relation，而不是因为它位于 `relations/`。

### IA-RS-004 — 分类与索引使用数据和引用

面向 Standard、Method、Organization、Capability、Design System、成熟先例、某个主题或某个能力的分类 / 索引 **SHOULD** 由对象字段、稳定 ID、Relation、Graph、Index、Map 或 Query 生成。

### IA-RS-005 — Data / Schema / Implementation 职责必须可区分

Canonical Facts、Schema/Contract 与 Engine/Tooling **MUST** 保持职责清楚；具体是否分别成为 root 一级目录，由下一轮 Repository Layout Decision 决定。

### IA-RS-006 — Source of Truth 与 Generated Projection 必须分离

Generated artifacts **MUST NOT** 与 Canonical Facts 竞争事实源身份。

### IA-RS-007 — Specification / Research 身份必须清楚

带 BCP 14 Requirements 的 IA Specification / Profile **MUST** 与 Prior Art、Options、Fit Test、Audit 等 Research Artifact 可区分；具体文件夹位置尚未冻结。

### IA-RS-008 — Community Health 使用平台原生位置

GitHub 能原生识别的 Community Health / Issue / PR 文件 **SHOULD** 使用 GitHub 支持的位置和格式。

### IA-RS-009 — License layout 优先兼容 REUSE

若项目采用 REUSE 3.3，`LICENSES/` 等受规范约束的位置继续遵守 REUSE；这属于外部格式 / 工具约束，而不是 IA 知识分类。

### IA-RS-010 — 迁移必须保持语义不变量

任何 Canonical storage migration 至少保持：

- object count 不因移动改变；
- relation count 不变；
- resolved graph edge count 不变；
- `reference_issues = 0`；
- stable object IDs 不变；
- 对象 `type / kind / relations` 不因文件位置改变；
- public generated URL 不应被物理 source path 无意改变。

### IA-RS-011 — 路径合同只表达物理位置

Path / storage contract **MUST NOT** 同时充当 ontology registry。

### IA-RS-012 — Internal links 与索引必须可验证

迁移后的 internal links、generated routes、navigation indexes **SHOULD** 可自动检查。

### IA-RS-013 — Monorepo 保持 extraction-ready

通过明确职责和接口边界保持未来可抽离，但不提前拆仓。

### IA-RS-014 — 不为分类制造目录

项目 **MUST NOT** 仅为了让 taxonomy 看起来完整而创建 Standard / Method / Precedent / Design System 等物理目录。

如果未来创建物理子目录，必须说明它解决的是规模、所有权、性能、生命周期、工具约束或其他实际工程问题，而不是“这个对象属于某个类别”。

## 7. 对 #15 的边界修正

#15 Non-normative Knowledge Object Model 继续回答：

- 对象 `type / kind / roles / relations` 如何表达；
- Method、Guideline、Design System、Precedent 等怎样保持现实身份；
- Fact、Evidence、Assessment 怎样分离。

#15 **不再负责决定**：

- `reference-projects/` 将来叫什么文件夹；
- 是否建立 `methods/`、`precedents/` 等目录；
- root 一级目录如何组织。

因此 #15 **不再是 Repository Physical Layout Discussion 的阻塞项**。

## 8. 修正后的迁移阶段

### Phase M0 — Principles / Contracts

已完成或进行中：

- Artifact identity；
- Storage ≠ Semantics ≠ View；
- Open Collaboration boundary；
- 迁移语义不变量。

### Phase M1 — Storage path decoupling

#25 已完成第一轮；#31 修正其语义：

- 集中记录**当前物理 storage locations**；
- Loader 从对象内容判断语义，而不是从目录判断；
- 可以对任意候选物理 storage path 做 Dry Run；
- 不预设未来必须保留 object-family 子目录。

### Phase M2 — Root / First-level Layout Decision

**下一阶段。**

从 root 一级目录开始重新讨论：

- 哪些目录因为平台 / 许可证标准必须存在；
- 哪些职责值得成为一级目录；
- 哪些可以合并；
- Canonical Data 的一级 storage zone 是否存在、叫什么；
- 不先讨论 Standard / Method 等语义子目录。

### Phase M3 — Migration Dry Run

在一级目录与 storage layout 经 Maintainer 明确批准后，生成完整 current → target move table、CI / links / Renderer / Loader 影响和 rollback plan。

### Phase M4 — Physical Migration

只有 Maintainer 再次明确批准后执行真实移动。

## 9. 当前明确未决定

以下全部 **OPEN / 待讨论**：

- `data/` 是否是最终一级目录名；
- Canonical Data 是否位于一个一级目录；
- Canonical Data 内部是否平铺或技术分片；
- `relations` 是否单独物理存放；
- `specs/` / `research/` / `governance/` / `docs/` 是否分别作为一级目录；
- `tests/` 是 root-level 还是 component-local；
- experiments / examples / tools 的最终层级。

这正是下一轮“从根目录一级目录开始”的讨论范围。

## 10. v0.1 修正结论

```text
文件夹：负责存储和工程边界
数据字段 / ID / Relation：负责知识身份与连接
Graph / Index / Map / Query：负责分类、索引与视图
```

**不要再让目录树承担知识图谱本来应该承担的工作。**
