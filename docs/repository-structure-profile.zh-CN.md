# InteropAtlas Repository Structure Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Provisional Specification
Document Created At: 2026-09-01T11:34:09+08:00
Document Updated At: 2026-09-05T04:20:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：Draft / Provisional Specification
>
> 本 Profile 定义 InteropAtlas 当前仓库的职责边界、Artifact identity、物理结构原则、文档生命周期与迁移不变量。

## 1. 核心原则

> **物理存储 ≠ 知识分类 ≠ 索引 / 视图。**

物理目录只解决文件怎样存、怎样被工具找到和怎样维护；对象是什么由对象自身数据合同表达；分类、连接和视图由引用、Relation、Graph、Index、Map、Query 表达。

因此，旧的按 Standard / Method / Organization 等语义类别划分物理目录的方式视为 **WITHDRAWN / SUPERSEDED（已撤回 / 已被取代）**。

## 2. 当前仓库的一级职责边界

当前正式结构：

```text
01_State/       项目当前正式承认的 Canonical State
02_Runtime/     项目怎样运行、验证和使用 State
03_Evolution/   项目怎样研究、实验、决策并改变自己

docs/           当前仍需理解或遵守的 Living Documents
.github/        GitHub 平台原生协作 / 自动化
LICENSES/       外部许可证布局
root files      README / CONTRIBUTING / AGENTS / PROJECT_STATE 等公共入口
```

`01_State`、`02_Runtime`、`03_Evolution` 是项目本体的三个生命周期区域；外围目录存在于平台、许可证、治理或公开入口需要，不构成第四个知识区域。

## 3. 已接受的结构决策

### RS-D1 — 单仓结构

**ACCEPTED.** 当前保持 Monorepo。State、Runtime、规范文档与 Evolution 仍处于高频共同演化阶段，提前拆仓只会增加同步成本。

### RS-D2 — Storage 与 Semantics 解耦

**ACCEPTED.** Canonical Data 的物理路径 **MUST NOT** 决定知识身份或语义类型。语义分类 **MUST** 来自机器可读对象数据、稳定 ID、引用与 Graph contract。

### RS-D3 — Canonical State 边界

**ACCEPTED AND IMPLEMENTED.**

```text
01_State/
├── 01_Objects/
├── 02_Relations/
└── README.md
```

未来如需分片，应优先采用稳定 ID、哈希或其他非语义分片，不恢复 ontology 文件夹。

### RS-D4 — Runtime / Evolution 边界

**ACCEPTED AND IMPLEMENTED.**

```text
02_Runtime/
├── 01_Engine/
├── 02_Tools/
└── 03_Outputs/

03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

### RS-D5 — Generated View 永不成为第二事实源

**ACCEPTED.** Generated HTML、Markdown、JSON/RDF export、index、report 等必须能够从 Canonical State / Contracts / Runtime 重新生成。

### RS-D6 — Public Route 与 Physical Source 分离

**ACCEPTED AND IMPLEMENTED.** 稳定对象 ID / public route 不依赖物理文件位置。移动或重命名文件不得无意改变对象身份。

### RS-D7 — `docs/` 与 Evolution 分离

**ACCEPTED.** `docs/` 只保存今天进入项目仍需理解或遵守的 Definition、Master Design、Architecture、Specification、Profile、Policy、Operating Model 与长期规则。

过程材料进入：

```text
03_Evolution/01_Research/      为什么这样判断：Prior Art / Research / Audit / Verification
03_Evolution/02_Experiments/   怎样试过：Prototype / Experiment / Dry Run / Result
03_Evolution/03_Change/        怎样改变：Proposal / Phase Plan / Migration / Transition / Historical Decision
```

### RS-D8 — AGENTS.md 是 Router，不是项目本体

**ACCEPTED.** `AGENTS.md` 指导 Agent 如何进入和参与项目，但不得替代 README、Master Design、CONTRIBUTING、Governance 或 Specification。

### RS-D9 — Living Documents 必须保持单一职责

**ACCEPTED.** 同一长期概念的完整定义 **SHOULD** 有一个明确的主要维护位置（Primary Home）。其他 Living Documents 可以摘要并链接，但 **SHOULD NOT** 复制完整论证、完整规则表或另一套平行定义。

典型职责：

```text
Philosophy          为什么；价值方向；最高层原则
Master Design       系统长期是什么；主要边界和层之间怎样组合
Architecture        关键系统结构与职责
Long-term Direction 某一长期子系统的专项设计
Roadmap             先后关系、阶段与 Gate
Specification       可执行的规范要求
Profile             针对特定场景的规范化选择 / 约束
PROJECT_STATE       现在在哪里、从哪里继续
Issue / PR           当前工作项与交付状态
Evolution           研究、实验、提案、迁移与历史过程
```

### RS-D10 — Living Document 与历史制品必须分离

**ACCEPTED.** 一个文件若不再描述当前有效设计，但仍具有独立的设计历史、决策、研究或迁移价值，**SHOULD** 进入对应的 `03_Evolution` 区域并明确 Historical / Superseded / Completed 状态，而不是继续与 Living Documents 平铺，也不应仅为整洁而删除。

真正临时、重复且没有独立历史价值的文件可以删除；具有重要设计历史的删除属于高影响清理，应确认替代关系和 Git 可恢复性。

### RS-D11 — Living Document 路径稳定

**ACCEPTED.** 持续维护的正式文档路径 **SHOULD** 稳定，文件名通常不携带内容版本号。版本历史由 Git commit / tag / release / provenance 保存。

只有协议、Schema、标准身份、兼容契约、不可变历史制品或版本号本身具有语义时，文件名才保留版本号。

### RS-D12 — Draft 是状态，不是位置

**ACCEPTED.** `draft` 可以出现在 Living Document 的状态中，只要该文档仍是当前正在形成的规范 / 架构入口；但已经完成、被取代或仅用于某一阶段施工的 Draft **MUST NOT** 因文件名带 `draft` 就永久留在 `docs/`。

判断依据是**当前职责和生命周期**，不是文件名。

## 4. Artifact Taxonomy

| Artifact Class | 主要职责 | 默认位置 | Canonical Fact? |
|---|---|---|---:|
| Canonical Data Object | 对现实知识对象的结构化事实 | `01_State/01_Objects/` | 是 |
| Canonical Relation | 对象之间的结构化关系 | `01_State/02_Relations/` | 是 |
| Schema / State Contract | 定义 Canonical 数据结构 | 与 State 共置 | 否 |
| Philosophy / Master Design | 当前最高层方向 | `docs/` | 否 |
| Architecture / Long-term Direction | 当前系统 / 专项长期结构 | `docs/` | 否 |
| Specification / Profile / Policy | 当前可执行规则 | `docs/` | 否 |
| Operating Model | 当前仍有效的运行 / 演化机制 | `docs/` | 否 |
| Research / Prior Art / Audit | 调研、比较、证据、验证 | `03_Evolution/01_Research/` | 否 |
| Experiment | 可复现探索、fixture、prototype、结果 | `03_Evolution/02_Experiments/` | 否 |
| Change Artifact | Roadmap 历史、Proposal、Phase Plan、Migration、Transition | `03_Evolution/03_Change/` | 否 |
| Implementation / Tool | Engine、Validator、Renderer、CLI、维护工具 | `02_Runtime/` | 否 |
| Generated Artifact / View | 网站、export、报告、动态索引 | `02_Runtime/03_Outputs/` 或 CI artifact | 否 |

目录表达当前工程 / 生命周期职责；Artifact 的语义身份仍由内容、标识、状态和关系决定。

## 5. 文档去重规则

### IA-RS-DOC-001 — 一个概念一个主要维护位置

当前正式文档 **MUST** 明确谁拥有某一概念的完整定义。引用者可以保留理解上下文所需的最小摘要，但不得为了“保险”复制整段设计。

### IA-RS-DOC-002 — 上位文档不承担下位细节

Philosophy 不维护具体架构；Master Design 不维护专项规则；Roadmap 不维护实时施工细节；`PROJECT_STATE.md` 不承担完整 Roadmap；Specification 不重新解释整个项目使命。

### IA-RS-DOC-003 — 下位文档不得重新定义上位概念

下位文档可以把上位原则操作化，但若发现上位定义不足，应回到主要维护位置修改，而不是在下位文件中创建一个更完整、但不同的版本。

### IA-RS-DOC-004 — 摘要必须指向 Primary Home

当一个概念因上下文必须重复出现时，摘要 **SHOULD** 指向其主要维护文档，使读者知道哪里是完整定义。

### IA-RS-DOC-005 — Current / Process / History 三态分离

文档维护时必须先判断：

```text
CURRENT   今天仍需理解 / 遵守 → docs/
PROCESS   正在研究 / 实验 / 迁移 → 03_Evolution 对应区域
HISTORY   已完成 / 被取代但值得保存 → 03_Evolution + lifecycle marker
```

不要通过创建更多 checkpoint 文档解决上下文连续性。实时状态进入 `PROJECT_STATE.md` / Issue / PR；长期设计进入既有 Durable Artifact；历史过程由 Git 与 Evolution 保存。

### IA-RS-DOC-006 — Promotion / Supersession 必须闭环

当 Research / Experiment / Change 结论被接受为当前设计时：

1. 更新对应 Living Document；
2. 在过程制品中记录 accepted / completed / superseded 状态或指向结果；
3. 更新必要索引；
4. 不让过程文件继续冒充当前规范。

当一个 Living Document 被替代时，应明确 successor；若只是局部内容被吸收，则将剩余独立价值重新判断为 Living / Evolution / 删除。

### IA-RS-DOC-007 — 文档数量不是安全性

设计连续性来自稳定 Primary Home、明确引用、Git history、Evolution 和项目状态，而不是在多个文件中保存相同文本。重复越多，长期漂移风险越高。

## 6. 三个必须分开的结构问题

以后讨论结构时必须区分：

```text
A. Physical Storage
   文件实际放在哪里？

B. Semantic Model
   对象是什么？type / kind / role / relation 是什么？

C. Projection / Navigation
   用户或 Agent 想按什么维度看？有哪些 Index / Map / Query？
```

一个对象可以通过 Graph 同时出现在多个分类和视图中，不需要复制文件，也不需要为了这些视图建立多个语义文件夹。

## 7. 其他规范要求

- Canonical State、Runtime 与 Evolution **MUST** 保持职责清楚。
- Specification / Profile 与 Research / Audit **MUST** 可区分。
- GitHub 能原生识别的 Community Health、Issue、PR、Workflow 文件 **SHOULD** 使用平台原生位置。
- Path / storage contract **MUST NOT** 同时充当 ontology registry。
- Internal links、generated routes、navigation indexes **SHOULD** 可自动检查。
- Monorepo **SHOULD** 保持 extraction-ready，但 **MUST NOT** 为未来可能拆仓提前制造不必要复杂度。
- 新物理目录必须解决规模、所有权、性能、生命周期、工具约束或其他真实工程问题，而不是仅为了分类。

## 8. Canonical 迁移不变量

任何 Canonical storage migration 至少保持：

- object / relation count 不因移动无意改变；
- resolved graph edge count 不因移动无意改变；
- `reference_issues = 0`；
- stable object IDs 不变；
- 对象语义不因文件位置改变；
- public URL 不被 physical source path 无意改变。

## 9. 当前结构维护检查表

新增或修改文档前至少检查：

1. 这是 Current、Process 还是 History？
2. 它属于哪一设计层？
3. 是否已经有 Primary Home？
4. 是应该修改已有 Durable Artifact，还是确实需要新文件？
5. 是否重复了其他文档的完整定义？
6. 如果是 Draft，它仍是当前入口，还是已经成为阶段历史？
7. 如果被替代，successor 和生命周期状态是否明确？
8. 索引、AGENTS / PROJECT_STATE 的阅读路径是否仍然正确？
9. 中文 / 英文并行文档的同步状态是否需要更新？

## 10. 当前结论

```text
文件夹：负责存储、生命周期和工程边界
数据字段 / ID / Relation：负责知识身份与连接
Graph / Index / Map / Query：负责分类、索引与视图
Living Documents：保存当前有效设计
Evolution：保存研究、实验、变更与有价值的历史过程
Git / Issue / PR：保存事件与实时协作证据
```

**不要再让目录树承担知识图谱的工作，也不要让重复文档承担版本控制和设计历史的工作。**
