# InteropAtlas Repository Current → Target Mapping v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Migration Dry Run / Updated after Schema colocation decision
Document Created At: 2026-09-01T10:56:49+08:00
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

> 状态：Migration Dry Run / Updated after Schema colocation decision
>
> 关联：#21、#31、#33、#34、#35、#36、#37。
>
> 本文件记录当前仓库如何迁入已经确认的三大主结构。它是迁移计划，不代表已经授权或执行物理搬迁。

## 1. 已确认的目标结构

```text
01_State/
├── 01_Objects/
├── 02_Relations/
└── README.md

02_Runtime/
├── 01_Engine/
├── 02_Tools/
├── 03_Outputs/
└── README.md

03_Evolution/
├── 01_Research/
├── 02_Experiments/
├── 03_Change/
└── README.md
```

三个一级目录分别回答：

- `01_State`：项目当前正式承认什么；
- `02_Runtime`：项目如何运行、处理和产生输出；
- `03_Evolution`：项目如何研究、验证并改变自己。

根目录外部接口继续保留，例如 `.github/`、`docs/`、`LICENSES/`、`README.md`、`CONTRIBUTING.md`、`LICENSE.md`、`AGENTS.md`。

`docs/` 主要承担项目正式规范、治理、说明与长期有效文档；研究过程、实验过程、迁移/路线等演化材料应逐步迁入 `03_Evolution`。

---

## 2. Canonical YAML 迁移

当前 Loader 扫描九个 legacy physical storage locations：

```text
standards/
capabilities/
scenarios/
organizations/
implementations/
reference-projects/
gaps/
relations/
maps/
```

目标不是把这九种分类复制到新目录。

迁移规则是：

```text
如果文档内容表示 Relation
→ 01_State/02_Relations/

其他 Canonical Object
→ 01_State/01_Objects/
```

因此预期的大方向是：

```text
standards/          ┐
capabilities/       │
scenarios/          │
organizations/      │
implementations/    ├──→ 01_State/01_Objects/
reference-projects/ │
gaps/               │
maps/               ┘

relations/ ─────────────→ 01_State/02_Relations/
```

但真实迁移时不能简单依据旧目录名批量分类。最终判断必须使用文件内容。Relation 的判断继续兼容：

- 正式形式：`type: relation`；
- legacy 形式：没有显式 `type`，但具有 `source + relation/predicate/kind + target`。

这能避免重新把文件夹变成知识模型。

`Properties` 不建立独立目录，继续属于 Object 或 Relation 自身。

### 规模风险

`01_Objects/` 未来可能包含数百到数千文件。现阶段可以保持平坦；只有当实际浏览、工具或文件系统性能出现明确问题时，再引入**非语义分片**。例如按稳定 ID 前缀或哈希分片，而不是重新按 Standard / Method / Organization 等类型建目录。

---

## 3. Schema 放置：已确认与数据共置

当前 `schemas/` 有一组机器可读合同，例如：

```text
base-object.schema.json
standard.schema.json
capability.schema.json
implementation.schema.json
organization.schema.json
scenario.schema.json
reference-project.schema.json
open-gap.schema.json
map.schema.json
relation.schema.json
```

目标结构不建立独立 `Schemas/` 二级目录。

已确认的原则是：

```text
Object 的数据说明与机器 Schema
→ 01_State/01_Objects/

Relation 的数据说明与机器 Schema
→ 01_State/02_Relations/
```

也就是说，同一个数据区内：

- `README.md` 给 Human / Agent 解释数据格式；
- `*.schema.json` 给机器执行验证；
- `*.yaml` / `*.yml` 承载正式数据。

Schema 因此不是 State 中与 Objects、Relations 平级的第三种内容，而是它所约束数据的机器可读合同。

### 现有 Schema 的迁移仍需 Dry Run

“放在哪里”已经决定，但现有 Schema 不能仅按文件名机械移动：

- `relation.schema.json` 明确属于 `02_Relations`；
- Object 相关 Schema 原则上属于 `01_Objects`；
- `base-object.schema.json` 与各 type-specific Schema 之间的引用必须检查；
- 是否合并或重构 type-specific Schema 属于 Data Model 改造，不应偷偷混入纯目录迁移。

因此物理迁移时优先保持 Schema 语义和验证能力不变；结构性重构另开工作。

---

## 4. Runtime 迁移

```text
engine/ ─────────→ 02_Runtime/01_Engine/
tools/ ──────────→ 02_Runtime/02_Tools/
```

当前 `engine/` 包括 Loader、Graph Index、Query、Markdown/Site Renderer、Repository Layout 和测试，整体职责与 `01_Engine` 一致，可以作为一个整体迁移候选。

当前 `tools/` 只有 README，迁移风险很低。

### Outputs

当前 Pages 工作流使用：

```text
python engine/render_site.py --output build/site
```

`build/site` 是 CI 生成物并上传到 GitHub Pages，不是 Canonical Source。

因此暂时没有需要从旧仓库搬入 `02_Runtime/03_Outputs/` 的正式内容。未来可以让运行时输出路径落到该区域，但**不等于应该把所有生成文件提交进 Git**。

---

## 5. Evolution 迁移

### Research

以下性质的现有 `docs/` 内容应逐步进入：

```text
03_Evolution/01_Research/
```

包括：

- Prior Art；
- standards/reference intake research；
- Fit Test；
- Audit / Assessment；
- 方案比较；
- 为某个项目决策进行的调查。

例如当前的 human-ai prior art、human-interface reference/audit、repository structure prior-art 等文档属于这一方向。

### Experiments

```text
experiments/*
        ↓
03_Evolution/02_Experiments/
```

当前 `experiments/json-ld/`、`experiments/rdf-1.2/` 是直接候选。

当前 `docs/experiments/` 中的实验报告也应与实验层统一，不再长期形成两个 experiment 区域。

### Change

以下性质的文档应逐步进入：

```text
03_Evolution/03_Change/
```

包括：

- Roadmap；
- Proposal；
- Migration Plan / Dry Run；
- Transition / Deprecation Plan；
- 面向下一状态的实施计划。

本 Mapping 文件本身在正式迁移时也属于 `03_Change`，现在继续留在 `docs/` 只是为了在迁移完成前保持现有文档索引和链接稳定。

---

## 6. `docs/` 最终保留什么

`docs/` 不再承担“所有 Markdown 都往这里放”的角色。

优先保留：

- 项目 Definition / Scope；
- 正式 Architecture；
- 已采用的 Specification / Profile；
- Governance / Policy；
- Collaboration rules；
- Language / Project development principles；
- 其他长期有效、用于解释和规范项目本身的正式文档。

判断方法不是“是不是 Markdown”，而是：

> 它是在解释当前项目规则，还是在记录项目如何演化？

前者留 `docs/`；后者进入 `03_Evolution`。

---

## 7. 根目录外围内容

以下内容继续留在主三目录之外：

```text
.github/
LICENSES/
README.md
CONTRIBUTING.md
LICENSE.md
AGENTS.md
```

理由是它们承担 GitHub、开源协作、法务或项目入口职责，不属于三大项目内容区本体。

---

## 8. 真实迁移前的三个工程准备项

### A. Public Route 与 Physical Source 解耦

当前 Loader 明确保留 `_source` / `_physical_source` 的物理路径，并注明在未来迁移前仍保持当前 generated-view 行为。

如果先移动文件，生成页面或链接可能因为物理路径变化而改变。

所以真实搬 Canonical Data 前，应先定义：

```text
stable object id
        ↓
stable public route
```

而不是：

```text
physical file path
        ↓
public route
```

### B. 现有 Schema 引用与验证迁移

Schema 的目标位置已经决定，但需要确认现有 Schema 之间的 `$ref`、Validator 调用位置以及 CI 路径，确保移动到 Objects / Relations 后验证能力不变。

这一步只解决“安全搬迁”，不顺便重做 Data Model。

### C. CI 路径更新

当前两个 GitHub Actions workflow 都显式监听旧的 `standards/**`、`capabilities/**`、`relations/**`、`schemas/**`、`engine/**` 等路径，并直接运行 `engine/...`。

真实迁移必须在同一个迁移 PR 中同步修改，否则迁移后 CI / Pages 可能不会触发或直接找不到程序。

---

## 9. 迁移验证基线

#32 最后一次完整验证的行为基线：

```text
objects = 112
relations = 107
resolved edges = 161
reference issues = 0
```

同时：

- 4 个 storage/layout regression tests 通过；
- 代表性 Query 语义不变；
- 代表性 Markdown rendering 成功。

物理迁移完成后必须至少保持这些语义基线，或者对任何变化给出明确的数据层原因，不能把“搬目录”变成静默的数据模型改变。

---

## 10. 建议迁移顺序

```text
M1  路径/URL 解耦准备
 ↓
M2  Schema 引用与 Validator 路径 Dry Run
 ↓
M3  Canonical YAML 按内容 Dry Run 分类
 ↓
M4  同一 PR 中移动 State + Runtime + Evolution 文件并更新 CI/文档引用
 ↓
M5  回归验证
 ↓
M6  删除已经为空的 legacy root folders
```

M4 是第一次真正发生大规模物理移动的步骤，需要 Human Maintainer 明确确认后再执行。

---

## 11. 当前结论

两级结构目前可以容纳现有仓库的主要内容，没有发现必须增加第四个主目录或第四个编号二级目录的硬需求。

Schema 的目标位置也已经明确：它跟随所约束的数据，不形成独立 `Schemas/` 区域。

当前真正需要解决的是迁移工程问题：

1. public route 不依赖 physical path；
2. Schema 引用、Validator 与 CI 能随新路径安全切换；
3. 文档链接和生成流程与新路径同时切换。

在这些准备完成前，保留 legacy directories 是有意的兼容状态，不视为结构设计失败。
