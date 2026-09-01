# InteropAtlas Repository Current → Target Mapping v0.1

> 状态：Migration Inventory / Corrected by #31
>
> 关联：#21、#31。
>
> 本文件记录“现在有什么”和“迁移时要处理什么”。旧版按 object family 一一映射到 `data/<family>/` 的方案已撤回。

## 1. 修正摘要

旧版曾建议：

```text
standards/          → data/standards/
capabilities/       → data/capabilities/
implementations/    → data/implementations/
...
```

#31 后该映射 **WITHDRAWN**。

原因很简单：

> 当前文件夹只是历史形成的物理存储位置，不应该继续被当成未来知识分类结构。

未来 Standard、Method、Design System、Capability、Organization、Relation 等对象是否共享一个物理目录、是否技术分片，应该按存储和工程需要决定；对象分类由数据字段、引用、Graph / Index / Map 决定。

---

## 2. 当前 Root Inventory

当前仓库大致包含以下 root 内容：

```text
README.md
CONTRIBUTING.md
LICENSE.md
LICENSES/
.github/

standards/
capabilities/
implementations/
organizations/
scenarios/
reference-projects/
gaps/
relations/
maps/

schemas/
engine/
tools/
experiments/
docs/
```

其中：

- README / CONTRIBUTING / LICENSE：公共项目入口 / 法务；
- `.github/`：GitHub 平台集成；
- 9 个知识对象目录：当前 Canonical YAML 的 **legacy physical storage shards**；
- `schemas/`：数据合同；
- `engine/`：确定性读取、Graph、Query、Renderer；
- `tools/`：维护工具候选区；
- `experiments/`：实验 artifact；
- `docs/`：当前混合承载 Specification、Research、Architecture、Plan、Governance 等多种文档身份。

这只是现状，不是目标结构。

---

## 3. Canonical Data：只记录 Current，不预设 Target

当前 Canonical YAML 分布在：

```text
standards/
capabilities/
implementations/
organizations/
scenarios/
reference-projects/
gaps/
relations/
maps/
```

正确的解释是：

```text
current physical storage shards
```

而不是：

```text
future ontology folders
```

因此当前 → 未来的映射现在只能写成：

```text
current 9 storage locations
          ↓
[future canonical storage layout — OPEN]
```

不能提前写成九个同名子目录。

### 已知迁移要求

无论未来 physical layout 最终是什么，迁移都必须：

1. Loader 能显式知道要扫描哪些物理位置；
2. Loader 根据对象内容判断 `type`，不能根据目录判断；
3. stable IDs 保持不变；
4. object / relation / Graph semantics 保持不变；
5. CI path filters 同步更新；
6. README / docs / generated routes / links 检查；
7. public URL 不被 source path 无意改写；
8. 可 rollback。

---

## 4. 当前 9 个目录是否还叫 object families？

在“当前数据”层面，它们历史上大致对应已有 Schema type，因此可以描述为 legacy family-oriented layout。

但从 #31 开始：

> **目录名本身不具有知识模型权威性。**

例如一个 YAML 放在名为 `anything/` 的目录中，只要它的数据声明：

```yaml
type: relation
```

Loader 就应按 Relation 处理。

反过来，一个文件仅仅位于 `relations/`，不能因此自动获得 Relation identity。

---

## 5. 其他 Artifact 的 Current Inventory

### `schemas/`

当前身份：Schema / Contract。

是否继续作为 root 一级目录：**待下一轮讨论**。

### `engine/`

当前身份：Implementation / Deterministic Engine。

是否继续作为 root 一级目录：**待下一轮讨论**。

### `tools/`

当前身份：Repository operational tooling。

是否保留、并入其他区或继续 root-level：**待讨论**。

### `experiments/`

当前身份：Experiment fixtures / prototypes / records 的一部分。

当前还有 `docs/experiments/`，说明 experiment report 与 executable artifact 边界尚未统一。最终层级：**待讨论**。

### `docs/`

当前混合至少包括：

- Specification / Profile；
- Research / Prior Art；
- Audit / Assessment；
- Architecture；
- Methodology / Guide；
- Governance / Policy；
- Roadmap / Plan / Working Notes；
- Experiment report。

这些 Artifact identity 需要区分，但**现在不再自动推导出** `specs/`、`research/`、`governance/` 等必须成为 root 一级目录。

下一轮应先讨论 root 一级目录数量与职责，再决定它们怎样落盘。

---

## 6. Current → Target 图（修正版）

```text
CURRENT

9 个 Canonical YAML root dirs ──────┐
                                     │
                                     ├──→ [Canonical Storage — OPEN]
                                     │     不按 ontology 自动拆目录
                                     │
                                     └──→ 分类由 type / kind / relations / Graph 完成

schemas/ ───────────────────────────→ [root placement OPEN]
engine/ ────────────────────────────→ [root placement OPEN]
tools/ ─────────────────────────────→ [root placement OPEN]
experiments/ ───────────────────────→ [root placement OPEN]

docs/ mixed artifacts ─────────────→ 先按 Artifact identity 理清
                                     再讨论物理一级目录

.github/ ───────────────────────────→ 受 GitHub 平台位置约束的内容继续遵守平台
LICENSES/ ──────────────────────────→ 若采用 REUSE，继续遵守 REUSE 约束
```

---

## 7. #15 与目录迁移的关系（修正）

旧版路线曾把 #15 Non-normative Knowledge Object Model 当成 `reference-projects/` 未来文件夹命名的前置条件。

这一依赖现在撤销。

#15 负责：

```text
type / kind / roles / relations / evidence / assessment
```

Repository Structure 负责：

```text
physical storage / artifact zones / tooling boundary
```

因此两条路线可以并行。

---

## 8. 现有迁移风险仍然有效

### Loader / Engine

- 当前扫描位置仍需集中管理；
- Renderer 仍会使用 `_source` 参与 generated path；
- 真实迁移前必须明确 public route 与 physical source 的关系。

### CI

Bootstrap / Pages workflow 仍然把当前真实路径写在 `paths:` 中。

### Documentation

- README links；
- docs index；
- cross-document relative links；
- 历史 Issue / PR 中的 blob path。

### External references

外部可能已经链接当前 GitHub 文件路径。真实 move 前必须评估。

### Licensing

受 REUSE 或其他实际标准约束的位置不能因为“统一目录”而随意移动。

---

## 9. 下一步

本 Mapping 到此不再给出完整 Target Tree。

下一步从 **Root 一级目录** 重新讨论，按以下顺序：

1. 哪些位置是 GitHub / REUSE 等外部机制强约束；
2. 哪些 Artifact responsibilities 必须一眼可区分；
3. 哪些职责值得成为一级目录，哪些可以合并；
4. Canonical Data 是否需要一个一级 storage zone、叫什么；
5. 最后才讨论一级目录内部怎样物理组织。

在这些决定明确之前，不再创建新的“目标目录树”。
