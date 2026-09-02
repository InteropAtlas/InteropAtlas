# InteropAtlas Repository Structure Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification
Document Created At: 2026-09-01T11:34:09+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

> 状态：Draft / Provisional Specification
>
> 关联：Issue #21、#31、#43、#46、#48；物理迁移 PR #45。
>
> 本 Profile 定义 InteropAtlas 当前仓库的职责边界、Artifact identity、物理结构原则与迁移不变量。

## 1. 核心原则

InteropAtlas 曾经按知识对象类别把 Canonical Data 分散到 `standards/`、`capabilities/`、`organizations/`、`implementations/`、`relations/` 等根目录。

该方式会让物理目录逐渐承担 ontology（知识分类模型）的职责。

当前正式采用：

> **物理存储 ≠ 知识分类 ≠ 索引 / 视图。**

- 物理目录只解决文件怎样存、怎样被工具找到、怎样维护；
- 对象是什么，由对象自身 `id / type / kind / roles / fields` 等数据合同表达；
- 对象之间怎样分类、归组和连接，由引用、Relation、Graph、Index、Map、Query 表达；
- 一个对象可以同时出现在多个动态分类 / 视图中，而无需复制文件；
- Standard、Method、Design System、Mature Precedent、Implementation 等不因为语义类别不同而自动获得不同文件夹。

因此，旧的 `data/<object-family>/` 目标和旧 root object-family 目录均视为 **WITHDRAWN / SUPERSEDED（已撤回 / 已被取代）**。

## 2. 上位依据

本 Profile 继续参考：

- GitHub Community Health / Issue & PR Templates：平台原生公共项目入口；
- GitHub CODEOWNERS / Rulesets / Required Review：ownership / review 原语；
- REUSE Specification：`LICENSES/` 等许可证布局约束；
- OpenSSF Best Practices / Scorecard：安全、Review、CI、维护实践；
- W3C browser-specs / MDN BCD / CNCF Landscape / SPDX License List：Data、Schema、Tooling、Generated Output 分工；
- Diátaxis / Docs as Code：面向人的文档组织和版本化工作流；
- InteropAtlas 自身迁移实践：Loader、Renderer、Graph、CI、public route 与 physical path 的真实解耦经验。

这些依据支持清晰的工程边界，但不要求 InteropAtlas 按 ontology 类别建立物理目录。

## 3. 当前已接受的核心决策

### RS-D1 — 继续采用单仓结构

**Decision: ACCEPTED.**

InteropAtlas 当前保持一个主仓库。Canonical State、Runtime、规范文档与 Evolution 材料仍处于高频共同演化阶段，现在拆成多个仓库会增加协作和同步成本。

### RS-D2 — Storage 与 Semantics 必须解耦

**Decision: ACCEPTED.**

Canonical Data 的物理路径 **MUST NOT** 决定对象的知识身份。

目录名 **MUST NOT** 被 Loader、Validator、Graph Index 或其他核心工具当作判断 `standard`、`relation`、`method`、`implementation` 等语义类型的依据。

语义分类 **MUST** 来自机器可读对象数据、稳定 ID、引用与 Graph contract。

### RS-D3 — Canonical State 的物理边界已经确定

**Decision: ACCEPTED AND IMPLEMENTED.**

当前 State：

```text
01_State/
├── 01_Objects/
├── 02_Relations/
└── README.md
```

- `01_Objects/`：Canonical Objects；不同对象类型平级存放；
- `02_Relations/`：Canonical Relations；
- Properties 属于 Object / Relation 自身，不建立独立目录；
- Object Schema 与 Objects 共置；Relation Schema 与 Relations 共置；
- Schema 的 `$id / $ref` 是逻辑身份，不要求复制 Git 物理目录结构。

未来如果因规模、性能或维护需要分片，应优先采用稳定 ID、哈希或其他**非语义分片**，而不是恢复 Standard / Method / Organization 等分类目录。

### RS-D4 — 三大生命周期一级目录已经确定

**Decision: ACCEPTED AND IMPLEMENTED.**

当前仓库的三个核心一级目录：

```text
01_State/
02_Runtime/
03_Evolution/
```

分别回答：

- `01_State`：项目当前正式承认什么；
- `02_Runtime`：项目当前怎样运行和使用 State；
- `03_Evolution`：项目怎样研究、验证、决策并改变自己。

当前 Runtime：

```text
02_Runtime/
├── 01_Engine/
├── 02_Tools/
├── 03_Outputs/
└── README.md
```

当前 Evolution：

```text
03_Evolution/
├── 01_Research/
├── 02_Experiments/
├── 03_Change/
└── README.md
```

平台、开源和项目入口文件继续位于三大区域之外，例如：

```text
.github/
docs/
LICENSES/
README.md
CONTRIBUTING.md
LICENSE.md
AGENTS.md
```

这些外围内容存在是因为 GitHub、许可证、公开项目入口或治理需要，而不是因为它们构成第四个项目本体区域。

### RS-D5 — Generated Site / Export 永不成为第二事实源

**Decision: ACCEPTED.**

Generated HTML、Markdown、JSON/RDF export、index、report 等必须能够从 Canonical State / Contracts / Runtime 重新生成，不得成为与 Canonical State 竞争的第二事实源。

`02_Runtime/03_Outputs/` 是生成产物的逻辑职责区域，不代表所有生成文件都应该提交 Git。

### RS-D6 — Public Route 与 Physical Source 分离

**Decision: ACCEPTED AND IMPLEMENTED.**

对象公开地址由稳定 ID 决定：

```text
/objects/<stable-id>.html
```

Loader 区分：

- `_source`：稳定逻辑 / public route source；
- `_physical_source`：真实 repository-relative 文件路径。

移动或重命名 YAML 不应改变对象公开 URL，只要稳定 `id` 不变。

### RS-D7 — `docs/` 与 Evolution 的职责分离

**Decision: ACCEPTED.**

`docs/` 保存当前需要被理解或遵守的项目 Definition、Architecture、Specification、Profile、Policy、Operating Model 与长期规则。

过程材料进入：

```text
03_Evolution/01_Research/      为什么这样判断
03_Evolution/02_Experiments/   怎样试过 / 验证过
03_Evolution/03_Change/        接下来怎样改变
```

### RS-D8 — AGENTS.md 是 Agent Instructions，不是项目本体

**Decision: ACCEPTED.**

`AGENTS.md` 可以指导 Agent 如何参与仓库，但不得替代 README、CONTRIBUTING、Governance、Specification 或其他正式项目文档。

## 4. Artifact Taxonomy

| Artifact Class | 主要职责 | 当前典型位置 | Canonical Fact? |
|---|---|---|---:|
| Canonical Data Object | 对现实互操作知识对象的结构化事实 | `01_State/01_Objects/` | 是 |
| Canonical Relation | 对象之间的结构化关系 | `01_State/02_Relations/` | 是 |
| Schema / Contract | 定义数据允许的结构 | 与 Objects / Relations 共置 | 否 |
| Specification / Profile | IA 自产的当前规范要求 | `docs/` | 否 |
| Research / Prior Art / Audit | 调研、比较、证据、验证 | `03_Evolution/01_Research/` | 否 |
| Architecture / Documentation | 帮助理解、使用、贡献项目 | `docs/` | 否 |
| Governance / Policy | 角色、授权、生命周期、治理约束 | root / `docs/` | 否 |
| Experiment | 可复现探索、fixture、prototype、结果 | `03_Evolution/02_Experiments/` | 否 |
| Change Artifact | Roadmap、Proposal、Migration、Transition | `03_Evolution/03_Change/` | 否 |
| Implementation / Tool | Engine、Validator、Renderer、CLI、维护工具 | `02_Runtime/` | 否 |
| Generated Artifact / View | 网站、export、报告、动态索引 | `02_Runtime/03_Outputs/` 或 CI artifact | 否 |

### Artifact identity invariant

Artifact identity **MUST NOT** 只依赖目录位置。

目录表达当前工程 / 生命周期职责；对象的语义身份仍由数据、标识和关系决定。

## 5. 三个必须分开的结构问题

以后讨论结构时必须区分：

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

不需要为了这些视图复制文件，也不需要建立五个语义文件夹。

## 6. Normative Requirements

### IA-RS-001 — Root 是公开项目入口

Root **MUST** 优先服务第一次进入仓库的人类贡献者、Agent 与通用工具；**MUST NOT** 演化成 Agent 私有状态或临时工作文件集合。

### IA-RS-002 — Canonical Storage 必须可发现和可配置

Loader / CI / Tooling **SHOULD** 通过明确的 repository storage contract 获取 Canonical State 当前物理位置。

当前默认 storage contract 指向：

```text
01_State/01_Objects/
01_State/02_Relations/
```

工具不得通过遍历整个仓库的全部 YAML 来猜测 Canonical State。

### IA-RS-003 — 目录不得定义知识分类

一个对象的 `type / kind / roles` **MUST NOT** 由其所在目录推断。

Canonical Relation 的目标模型 **SHOULD** 显式声明 `type: relation`。当前 Loader **MAY** 为兼容少量历史数据，根据文档自身的 `source + relation/predicate/kind + target` 结构识别旧 Relation，但 **MUST NOT** 根据它是否位于 `02_Relations/` 来判断。

该兼容只是历史数据技术债，不改变“语义来自对象内容而不是目录”的原则。

### IA-RS-004 — 分类与索引使用数据和引用

面向 Standard、Method、Organization、Capability、Design System、Mature Precedent、主题或能力的分类 / 索引 **SHOULD** 由对象字段、稳定 ID、Relation、Graph、Index、Map 或 Query 生成。

### IA-RS-005 — State / Runtime / Evolution 职责必须清楚

Canonical State、运行实现与演化过程 **MUST** 保持职责清楚：

- State 不存放临时研究和实验；
- Runtime 不成为事实源；
- Evolution 不冒充当前 Canonical State 或当前正式运行源码。

### IA-RS-006 — Source of Truth 与 Generated Projection 必须分离

Generated artifacts **MUST NOT** 与 Canonical State 竞争事实源身份。

### IA-RS-007 — Specification / Research 身份必须清楚

带 BCP 14 Requirements 的当前 IA Specification / Profile **MUST** 与 Prior Art、Options、Fit Test、Audit 等 Research Artifact 可区分。

当前默认边界为：Specification / Profile → `docs/`；Research → `03_Evolution/01_Research/`。

### IA-RS-008 — Community Health 使用平台原生位置

GitHub 能原生识别的 Community Health、Issue、PR、Workflow 等文件 **SHOULD** 使用 GitHub 支持的位置和格式。

### IA-RS-009 — License layout 优先兼容外部规范

若项目采用 REUSE 等外部规范，`LICENSES/` 等受规范约束的位置继续遵守其要求；这属于工具 / 法务互操作约束，而不是 IA 知识分类。

### IA-RS-010 — 迁移必须保持语义不变量

任何 Canonical storage migration 至少保持：

- object count 不因移动改变；
- relation count 不因移动改变；
- resolved graph edge count 不因移动改变；
- `reference_issues = 0`；
- stable object IDs 不变；
- 对象 `type / kind / relations` 不因文件位置改变；
- public URL 不被 physical source path 无意改变。

PR #45 的三大区域迁移以 `112 objects / 107 relations / 161 edges / 0 reference issues` 作为迁移基线并保持通过。

### IA-RS-011 — 路径合同只表达物理位置

Path / storage contract **MUST NOT** 同时充当 ontology registry。

### IA-RS-012 — Internal links 与索引必须可验证

迁移后的 internal links、generated routes、navigation indexes **SHOULD** 可自动检查。

仓库当前通过 Markdown link CI 检查本地文档链接，并通过 Engine regression / site build 检查 State 与 public route。

### IA-RS-013 — Monorepo 保持 extraction-ready

各区域 **SHOULD** 通过明确职责和接口边界保持未来可抽离能力，但 **MUST NOT** 为未来可能发生的拆仓提前制造当前不必要的复杂度。

### IA-RS-014 — 不为分类制造目录

项目 **MUST NOT** 仅为了让 taxonomy 看起来完整而创建 Standard / Method / Precedent / Design System 等物理目录。

如果未来创建新的物理子目录，必须说明它解决的是规模、所有权、性能、生命周期、工具约束或其他实际工程问题，而不是“这个对象属于某个类别”。

## 7. 与 Non-normative Knowledge Object Model 的边界

Non-normative Knowledge Object Model 继续回答：

- 对象 `type / kind / roles / relations` 如何表达；
- Method、Guideline、Design System、Precedent 等怎样保持现实身份；
- Fact、Evidence、Assessment 怎样分离。

它不负责决定：

- 是否创建 `methods/`、`precedents/` 等目录；
- root 一级目录如何组织；
- 某种知识类别应该住在哪个文件夹。

因此 Knowledge Object Model 与 Repository Physical Layout 是两个不同问题。

## 8. 已完成的结构迁移阶段

### M0 — Principles / Contracts

完成：

- Artifact identity；
- Storage ≠ Semantics ≠ View；
- 迁移语义不变量。

### M1 — Storage path decoupling

完成：

- Loader 的 physical storage contract 集中化；
- Loader 从对象内容判断语义；
- public route 与 physical path 解耦；
- 任意候选 storage path 可用于 Dry Run。

### M2 — Root / Second-level Layout Decision

完成：

```text
01_State/
02_Runtime/
03_Evolution/
```

及各自已经确认的二级结构。

### M3 — Migration Dry Run

完成：

- current → target mapping；
- Schema placement / reference review；
- public route review；
- CI / Loader / Renderer 影响分析；
- regression baseline。

相关历史材料位于 [`03_Evolution/03_Change/`](../03_Evolution/03_Change/)。

### M4 — Physical Migration

已由 PR #45 完成并通过回归验证。

### M5 — Documentation / Evolution Boundary

当前执行：将 Research、Experiments 与 Change 历史从 `docs/` 迁入 `03_Evolution`，让 `docs/` 收敛为当前项目文档入口。

## 9. 仍然开放的问题

以下问题仍可根据真实规模与实践重新评估：

- `01_Objects/` 文件量增长后是否需要非语义分片；
- Relation 历史数据何时全部显式补齐 `type: relation`；
- Schema enforcement 如何接入 CI；
- `02_Runtime/03_Outputs/` 中哪些生成产物应该版本化；
- tests 最终采用 component-local 还是更独立的技术布局；
- 未来是否有充分理由从 Monorepo 抽离某一组件。

这些开放问题**不重新打开已经接受的“目录不得定义知识分类”原则**。

## 10. v0.1 当前结论

```text
文件夹：负责存储、生命周期和工程边界
数据字段 / ID / Relation：负责知识身份与连接
Graph / Index / Map / Query：负责分类、索引与视图
```

**不要再让目录树承担知识图谱本来应该承担的工作。**
