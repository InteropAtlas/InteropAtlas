# Repository Data Root Contract v0.1

> 状态：Implementation Preparation / Migration Guardrail
>
> Work Item：#25
>
> 上位规范：`docs/repository-structure-profile-v0.1.zh-CN.md`
>
> 本文只定义“迁移前路径解耦”的实现合同。**没有执行任何 Canonical Data 目录迁移。**

## 1. 为什么现在做

Repository Structure Profile 已接受：

> Layered Monorepo now, extraction-ready later.

并把 `data/` 作为未来 Canonical Data 的候选逻辑边界。

当前真实仓库仍是：

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

原 `engine/bootstrap_query.py` 自己维护了这 9 个目录名。未来如果直接把目录搬进 `data/`，至少会同时影响：

- Loader；
- GraphIndex（通过 Loader）；
- Markdown Renderer（通过 Loader）；
- Site Renderer（通过 Loader）；
- GitHub Actions path triggers；
- 由 source path 派生的 generated page paths。

因此不能把“移动目录”当成普通文件整理。

## 2. 本轮决策

新增 `engine/repository_layout.py`，集中定义：

- `OBJECT_FAMILIES`；
- 当前 `DEFAULT_DATA_ROOT = .`；
- repository root 与 data root 的关系；
- family physical path；
- physical source 与 logical source 的区别。

当前并没有切换默认 Data Root。

```text
DEFAULT_DATA_ROOT = .
```

所以所有 Canonical YAML 仍从现有 root directories 读取。

## 3. Physical Source 与 Logical Source

这是本轮最重要的迁移保护。

当前：

```text
physical: standards/yaml_1.2.2.yaml
logical:  standards/yaml_1.2.2.yaml
```

未来若批准迁移：

```text
physical: data/standards/yaml_1.2.2.yaml
logical:  standards/yaml_1.2.2.yaml
```

Loader 运行时使用：

- `_source` = stable logical source；
- `_physical_source` = actual repository-relative source；
- `_object_family` = logical family。

Renderer 当前已经使用 `_source` 生成 Markdown / HTML 相对路径，因此保持 `_source` 为逻辑路径可以避免未来物理目录迁移自动改变 public object URL。

这实现了 Repository Structure Profile 中的重要 invariant：

> source physical path 的变化不应强制 generated public URL 变化。

## 4. 明确未改变的内容

本轮 MUST NOT 改变：

- Canonical Data 文件的物理位置；
- stable object IDs；
- Schema；
- relation semantics；
- Graph edge semantics；
- 现有 generated page logical paths；
- `reference-projects/` 的最终命名决策。

尤其是 `reference-projects/` 仍受 #15 Non-normative Knowledge Object Model 影响，本轮只把它当作**当前存在的 object family**，不冻结它的长期 ontology 身份。

## 5. 风险分析

### Risk 1 — Loader 漏读 object family

如果集中路径列表遗漏某个现有 family，会直接减少 object / relation count。

控制：
- `OBJECT_FAMILIES` 按当前 9 个 families 原样迁移；
- CI 比较 graph diagnostics；
- object / relation / edge counts 必须保持。

### Risk 2 — 生成 URL 意外改变

若 Renderer 继续直接使用 physical path，则未来 `data/` 前缀会泄漏到 generated path。

控制：
- `_source` 保持 logical source；
- 新增 `_physical_source` 单独提供真实路径；
- regression test 同时模拟 root layout 与 future `data/` layout，要求 `output_path()` 完全相同。

### Risk 3 — 配置允许逃出 repository

若 `data_root` 接受绝对路径或 `../`，可能让 bootstrap Engine 意外加载 repository 外部数据，增加可复现性与安全风险。

控制：
- v0.1 只接受 repository-relative data root；
- absolute path / parent escape 明确拒绝。

### Risk 4 — 误以为 Engine 解耦等于整个仓库解耦

GitHub Actions 的 `paths:` 是 GitHub 平台配置，不能直接 import Python path contract。

控制：
- 本轮不假装消除这个耦合；
- workflow path triggers 继续保留现有 root paths；
- 真正迁移前必须单独修改并验证 Bootstrap / Pages triggers。

## 6. 当前影响范围

本轮代码影响：

```text
engine/repository_layout.py     NEW
engine/bootstrap_query.py       Loader 改用集中合同
engine/graph_index.py           增加可显式传入 data-root 的 diagnostics
engine/test_repository_layout.py NEW regression checks
engine/README.md                记录合同
.github/workflows/bootstrap-engine-experiment.yml
                                只增加 regression check step
```

不修改：

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
schemas/
```

## 7. Baseline

迁移前最近一次完整 Bootstrap Engine Run #89（Canonical Data 最新变化之后）报告：

```text
objects:          112
relations:        107
resolved edges:   161
reference issues: 0
```

代表性 deterministic query：

```text
capability = automated_build_deployment
implementations = forgejo_actions, github_actions
open-source + self-hostable = forgejo_actions
```

PR CI 必须至少保持上述 graph / query semantics。

## 8. Residual Coupling

Step 1 完成后仍然存在：

1. `.github/workflows/bootstrap-engine-experiment.yml` 的 root path filters；
2. `.github/workflows/pages.yml` 的 root path filters；
3. README / docs 中描述当前路径的自然语言引用；
4. 未来 #15 可能改变 `reference-projects` 的 object-family modeling / naming。

其中 1–2 是正式 Migration Dry Run 前的硬前置；3 属于迁移后的 link/docs stabilization；4 是正式目录迁移前需要等待的模型决策。

## 9. Step 1 完成 Gate

只有满足以下条件，#25 才可完成：

- current root layout 仍可完整加载；
- object = 112；
- relation = 107；
- edge = 161；
- reference issues = 0；
- representative query 语义不变；
- current logical generated paths 不变；
- regression test 证明 future `data/` physical prefix 不会自动改变 logical generated path；
- 没有真实移动任何 Canonical Data 文件。

## 10. 下一步不是迁移

#25 完成后仍然**不直接迁移**。

下一阶段按已批准顺序推进 #15，待关键 object-family naming / modeling 稳定后，再进入 Migration Dry Run。Dry Run 应再次向 Maintainer 明确说明：

1. 准备移动哪些路径；
2. 每条路径为什么移动；
3. Loader / CI / URLs / external links 的影响；
4. rollback 方法；
5. 迁移前后不变量。

只有 Maintainer 再次明确批准，才进入真实物理目录迁移。
