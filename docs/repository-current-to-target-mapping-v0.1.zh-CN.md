# InteropAtlas Repository Current → Target Mapping v0.1

> 状态：Migration Simulation（迁移模拟，不执行移动）
>
> 关联：#21；输入：`repository-structure-prior-art-and-options-v0.1.zh-CN.md`

## 1. 目的

把当前真实仓库逐项映射到 Artifact Taxonomy 与候选 Target Zone，验证 Layered Monorepo 是否真的比当前结构更清晰。

本文件**不代表路径已经批准**，也不执行 rename / move。

---

# 2. Root 当前对象

| 当前路径 | Artifact identity | 当前判断 | 候选目标 |
|---|---|---|---|
| `README.md` | Project Entry / Reference | Root 保留 | `/README.md` |
| `CONTRIBUTING.md` | Community / Contribution Guide | Root 保留；内容待 #19/#9 重写 | `/CONTRIBUTING.md` |
| `LICENSE.md` | Licensing Overview | Root 保留 | `/LICENSE.md` |
| `LICENSES/` | Machine-readable License Text Set | 与 REUSE 方向兼容 | `/LICENSES/` |
| `.github/workflows/` | Platform Integration / Automation | 保留在 `.github` | `/.github/workflows/` |
| `tools/` | Implementation / Tooling | 已有独立逻辑区 | `/tools/` |

未来候选 Root / Community Health 文件（尚不创建）：

```text
CODE_OF_CONDUCT.md
SECURITY.md
SUPPORT.md
AGENTS.md            # 仅 #19 Profile 后
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS 或 root CODEOWNERS（按 GitHub 支持位置决定）
```

原则：Root 保持“第一次打开仓库就应该理解的公开入口”，不把内部 Agent 状态、实验文件、生成产物堆到 Root。

---

# 3. Canonical Data

当前 object families：

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

Artifact identity：**Canonical Data Objects**。

候选映射：

```text
current                         candidate
------------------------------------------------
standards/                 →   data/standards/
capabilities/              →   data/capabilities/
implementations/           →   data/implementations/
organizations/             →   data/organizations/
scenarios/                 →   data/scenarios/
reference-projects/        →   data/reference-projects/
gaps/                      →   data/gaps/
relations/                 →   data/relations/
maps/                      →   data/maps/
```

### 为什么这个映射目前合理

- 这些目录都被同一个 loader 作为 Atlas Canonical Data 读取；
- 它们共享 ID / Relation / Graph / Schema contract；
- `data/` 可以成为稳定的 Source-of-Truth boundary；
- 新 object family 不再继续占用 root namespace。

### 但现在不能直接移动

当前 `engine/bootstrap_query.py` 的 `OBJECT_DIRS` 直接假设这些目录位于 root。

CI path filters 也把这些目录逐一硬编码在：
- `.github/workflows/bootstrap-engine-experiment.yml`；
- `.github/workflows/pages.yml`。

因此目标状态应该先变成：

```text
Repository Root
   ↓
DATA_ROOT = root / "data"       # configuration / contract
   ↓
OBJECT_FAMILIES = ...
```

而不是把 `data/` 路径散落写死到更多工具里。

### 迁移兼容要求

D1 若批准，迁移 SHOULD：

1. 先让 loader 可配置 `data_root`；
2. 为 current root paths 与 candidate `data/` path 做 transition test；
3. 更新 CI path filters；
4. 更新所有 README / docs links；
5. 确保 generated human URL 不依赖 source YAML physical path；
6. 迁移前后 Graph object / relation / edge count MUST 不变；
7. reference issues MUST 保持 0。

---

# 4. Schemas / Engine / Tools / Tests

## `schemas/`

Artifact identity：**Schema / Contract**。

当前判断：Root-level `schemas/` 可以继续成立。

原因：
- 它不是 Canonical Facts；
- 它定义 Canonical Facts 的结构合同；
- W3C browser-specs / MDN BCD 等成熟 data repos 也把 schema 作为独立一等区。

候选：`/schemas/` 保留。

## `engine/`

Artifact identity：**Implementation / Deterministic Engine**。

当前判断：Root-level `engine/` 暂时保留。

未来当 Engine 形成独立 release / API contract 后，可评估抽离独立 repo；当前不拆。

## `tools/`

Artifact identity：**Operational Tooling**。

当前只有 README，说明这个 zone 已经存在但尚未真正使用。

候选：保留 `/tools/`，未来放：
- migration tooling；
- curation helpers；
- source checking；
- export tooling；
- repo maintenance scripts。

Engine 与 Tools 边界：
- Engine = Atlas deterministic product capability；
- Tools = repo / contributor operational helpers。

## `tests/`（当前不存在）

当前 tests 分散在 CI 行为与 Engine 脚本自检里。

Candidate B 建议未来出现明确 `/tests/`，但需要再决定：

```text
tests/data/          # canonical data / schema tests
tests/engine/        # deterministic query / graph regression
tests/conformance/   # IA-produced specifications conformance
tests/site/          # Reference Implementation / E2E
```

也可能采用 component-local tests，而只把 cross-cutting conformance tests 放 root `tests/`。

当前只记录，不创建空目录。

---

# 5. `docs/` 当前混合状态

当前 `docs/` 已经同时承载至少 9 种 Artifact identity。

## 5.1 Specification / Profile

### 当前
- `human-interface-specification-v0.1.zh-CN.md`

### 候选

```text
specs/human-interface/v0.1.md
```

或：

```text
specifications/human-interface/v0.1.md
```

当前倾向短名 `specs/`，但**尚未批准命名**。

未来：
- Repository Structure Profile；
- Open Collaboration Profile；
- Curation Profile；
- Evidence Profile；
都应该使用同一种 Artifact zone / lifecycle。

---

## 5.2 Research / Prior Art

### 当前
- `human-ai-open-collaboration-prior-art.zh-CN.md`
- `human-interface-reference-map.zh-CN.md`
- `human-interface-standards-baseline.zh-CN.md`
- `prior-art-and-method-reference.zh-CN.md`
- `repository-structure-prior-art-and-options-v0.1.zh-CN.md`

### 候选

```text
research/prior-art/
research/options/
```

或：

```text
docs/research/
```

当前倾向独立 `research/`，因为它不是用户文档，也不是 Specification。

---

## 5.3 Audit / Assessment Report

### 当前
- `human-interface-conformance-audit-2026-09-01.zh-CN.md`
- `route-alignment-audit-2026-09-01.zh-CN.md`

Artifact identity：**Point-in-time Audit / Assessment**。

候选：

```text
research/audits/
```

或未来独立：

```text
assessments/
```

当前倾向 `research/audits/`，避免在项目尚小时制造新 root namespace。

---

## 5.4 Architecture Reference

### 当前
- `architecture-v0.1.zh-CN.md`
- `flat-graph-and-dynamic-maps.zh-CN.md`
- `json-ld-fit-experiment.zh-CN.md`（部分是实验，不纯 architecture）
- `visualization-direction.zh-CN.md`（更像 Working Direction）

候选：

```text
docs/architecture/
```

这里适合继续属于 Documentation，因为它主要帮助贡献者 / 维护者理解系统结构；如果未来某 architecture 文档出现 BCP 14 implementation contract，再考虑升级为 Specification。

---

## 5.5 Methodology / Guide

### 当前
- `practice-feedback-loop.zh-CN.md`
- `project-development-principles.zh-CN.md`
- `five-route-operating-model.zh-CN.md`
- `human-readable-route.zh-CN.md`
- `machine-readable-maintainable-route.zh-CN.md`

其中身份并不完全相同：
- `practice-feedback-loop` 更像 Methodology；
- `project-development-principles` 介于 Methodology / Governance；
- route documents 介于 Methodology / Roadmap。

候选：

```text
methodology/
```

或：

```text
docs/explanation/
docs/reference/
```

这里需要下一轮判断：**Methodology 是否值得成为 root Artifact zone。**

当前不强行拍板。

---

## 5.6 Governance / Policy

### 当前
- `language-policy.zh-CN.md`
- `project-generated-methods-standards.zh-CN.md`
- `project-development-principles.zh-CN.md`（部分）

候选：

```text
governance/
```

理由：这些文档不是普通知识解释，而是在约束项目自身的持续运行。

未来可能加入：
- governance model；
- maintainer roles；
- decision process；
- specification lifecycle；
- security policy relationship；
- trademark policy。

---

## 5.7 Plan / Roadmap / Working Notes

### 当前
- `roadmap.zh-CN.md`
- `foundation-first-phase-v0.1.zh-CN.md`
- `object-page-shell-v0.1-plan.zh-CN.md`
- `open-collaboration-route-v0-notes.zh-CN.md`

这些是**当前项目状态文档**，生命周期短于 Specification / Architecture Reference。

候选方案：

A. `docs/project/`

```text
docs/project/roadmap.md
docs/project/plans/
docs/project/notes/
```

B. `planning/`

当前倾向 **A**，避免为短生命周期文件增加 root namespace。

---

## 5.8 Experiment Records

当前出现两套位置：

```text
docs/experiments/*.md          # 实验报告
experiments/json-ld/*          # 实验输入 / 实际 artifact
experiments/rdf-1.2/*
```

这是合理现象，但职责应明确：

```text
experiments/<experiment-id>/
  README.md / report.md
  input/
  output/
  fixture/
  prototype/
```

即 Experiment report 与 executable artifact 最终最好聚合到同一个 experiment boundary，而不是一份在 docs、一份在 root experiments。

当前不迁移；记录为 Candidate。

---

# 6. 一个很重要的发现：现有 `docs/experiments/human-ai-collaboration-v0-checklist.zh-CN.md`

该文件实际存在于仓库树中，但之前 `docs/README.md` 曾经把它误写成 root `docs/human-ai-collaboration-v0-checklist.zh-CN.md`，导致链接漂移。

这正说明：

> **当 Artifact identity 与目录职责不清楚时，Navigation Index 很容易与物理路径逐渐失同步。**

未来应：
- 自动检查 internal links；
- 给 Docs / Spec / Research Index 建 CI；
- 尽可能由 metadata / manifest 生成导航，而不是长期手工维护多个目录索引。

---

# 7. Current → Target Zone 总览

```text
CURRENT ROOT

standards/ ───────────────┐
capabilities/             │
implementations/          │
organizations/            │
scenarios/                ├──→ data/
reference-projects/       │
gaps/                     │
relations/                │
maps/ ────────────────────┘

schemas/ ─────────────────────→ schemas/        (keep)
engine/ ──────────────────────→ engine/         (keep now)
tools/ ───────────────────────→ tools/          (keep)
experiments/ ─────────────────→ experiments/    (clarify boundary)

                                   ┌→ specs/
docs/ mixed artifacts ────────────┼→ research/
                                   ├→ docs/architecture + Diátaxis docs
                                   ├→ governance/
                                   └→ docs/project/ plans / roadmap

.github/workflows/ ───────────────→ .github/ platform integration
README / CONTRIBUTING / LICENSE ─→ root public entry contracts
LICENSES/ ────────────────────────→ LICENSES/ (REUSE-compatible direction)
```

---

# 8. 当前最需要解决的命名 / 结构 Decision

下一版 Repository Structure Profile 不应该讨论几十个目录，只需要先定 6 个问题：

### RS-D1 — `data/` 是否成为 Canonical Data Root？

当前推荐：**YES / provisional**。

### RS-D2 — IA-produced Specification 是否离开 `docs/`？

当前推荐：**YES / provisional**。

### RS-D3 — 使用 `specs/` 还是 `specifications/`？

未决。

需要考虑：
- 人类可读性；
- 常见开源惯例；
- 与 `standards/` Canonical Data object family 的概念区分；
- URL / package naming。

### RS-D4 — Research 是否 root-level？

当前推荐：**YES / provisional**，但需验证是否会过度增加 root zones。

### RS-D5 — Methodology / Governance 是否分别 root-level？

未决。

可能最终：

```text
governance/
docs/methodology/
```

而不是两个都 root-level。

### RS-D6 — Experiments 是否把 report + fixture 聚在一个 experiment boundary？

当前推荐：**YES / provisional**。

---

# 9. 迁移风险清单

## Code / Loader
- `engine/bootstrap_query.py::OBJECT_DIRS`；
- 任何按 root relative path 生成 `_source` 的逻辑；
- Renderer / output path 是否错误耦合 source path。

## CI
- Bootstrap Engine workflow path filters；
- Pages workflow path filters；
- future schema / link / conformance checks。

## Documentation
- README links；
- docs index；
- cross-document relative links；
- GitHub Issue 中不可自动更新的历史路径引用。

## External References
- 用户 / Agent 可能已引用 GitHub blob path；
- GitHub history 可追踪 rename，但旧 raw links 未必是稳定 API。

## Licensing
- REUSE / file-level licensing 若后续采用，应在迁移前明确，避免大量文件移动后重复补 metadata。

---

# 10. 下一小步

基于这份映射，下一步可以开始写 **Repository Structure Profile v0.1 Requirements**，但只先写“职责合同”，不写所有具体目录：

1. Root MUST remain a public project entry surface；
2. Canonical Data MUST have one explicit source boundary；
3. Generated Views MUST NOT be competing source of truth；
4. Specification / Research / Governance artifact identity MUST be distinguishable；
5. Agent instructions MUST NOT replace human contribution / governance contracts；
6. path migration MUST preserve Graph semantics and be testable；
7. physical path MUST NOT be the only artifact identity mechanism；
8. repository structure SHOULD remain extraction-ready without premature multi-repo split。

然后再用这些 Requirements 审核 Option B，而不是因为 Option B 看起来整齐就采用。
