# docs / Evolution Responsibility Boundary Audit — 2026-09-01

> 状态：Audit / Classification Proposal
>
> 关联：Issue #46；三大区域物理迁移 #43 / PR #45。
>
> **本文件只做职责分类，不执行任何文件移动、删除或重命名。**

## 1. 为什么需要这次审计

三大区域迁移完成后，仓库已经有明确的生命周期结构：

```text
01_State      当前正式承认什么
02_Runtime    当前怎样运行
03_Evolution  项目怎样研究、验证和改变自己
```

但 `docs/README.md` 仍把 architecture、methodology、governance、research、design 全部视为 `docs/` 的职责，而 `03_Evolution/README.md` 已明确规定：

- Research / Prior Art / Fit Test / Audit → `01_Research/`
- Prototype / Dry Run / Experiment → `02_Experiments/`
- Proposal / Roadmap / Migration / Transition → `03_Change/`

因此当前真正的问题不是“文档太多”，而是：

> **当前有效的项目合同，与形成这些合同的研究 / 实验 / 变更过程混在了一起。**

这会让 Human / Agent 难以判断一份文档究竟是“现在应该遵守的东西”，还是“当时为什么这样决定的过程材料”。

---

## 2. 建议的稳定边界

### `docs/` — Current Project Contract / Guidance

`docs/` 只保留当前仍承担公开项目接口作用的长期文档：

- 项目 Definition / Scope；
- Architecture；
- Specification / Profile；
- Policy；
- 当前 Operating Model；
- 当前 Method / Process；
- Contributor / Human / Agent 需要长期读取并据此行动的说明。

判断问题：

> **一个新的贡献者今天进入项目，为了正确理解或遵守当前项目，是否应该读这份文件？**

如果答案是“是”，优先留在 `docs/`。

### `03_Evolution/01_Research/` — Why / Evidence

用于保存形成决策之前和之后的证据与分析：

- Prior Art；
- 标准 / 方法 / Reference 调研；
- Audit；
- Fit / Comparison；
- Reference Intake；
- Gap / Conformance / Verification 分析。

判断问题：

> **这份文件主要是在回答‘我们依据什么、发现了什么、验证出了什么？’吗？**

### `03_Evolution/02_Experiments/` — Try / Verify

用于可复现探索：

- Prototype；
- Engine / Coverage 实验；
- Dry Run；
- Fixture / Checklist；
- 格式适配实验；
- 实验结果。

判断问题：

> **这份文件主要是在记录一次可重复尝试或验证吗？**

### `03_Evolution/03_Change/` — Become / Transition

用于项目从当前状态走向下一状态：

- Roadmap；
- Route / Phase plan；
- Proposal；
- Implementation Plan；
- Migration / Transition；
- Future Direction；
- 已被正式产物替代的早期 Working Note。

判断问题：

> **这份文件主要是在回答‘接下来要变成什么、怎样变过去？’吗？**

---

## 3. 全量分类结果

当前 `docs/` 共审计 **45 个文件**（41 个顶层文件 + `docs/experiments/` 下 4 个文件）。建议结果：

```text
保留 docs/                         15
→ 03_Evolution/01_Research/        13
→ 03_Evolution/02_Experiments/      6
→ 03_Evolution/03_Change/          11
-------------------------------------
合计                               45
```

### A. 保留在 `docs/` — 15

| 当前文件 | 建议 | 原因 / 后续 |
|---|---|---|
| `docs/README.md` | KEEP + REWRITE | 继续作为正式文档入口，但应删除“research 也属于 docs”的旧职责描述，并重建链接 |
| `docs/architecture-v0.1.zh-CN.md` | KEEP | 当前架构说明 |
| `docs/collaboration-task-system-v0.1.zh-CN.md` | KEEP | 当前协作运行 Profile / operational contract |
| `docs/five-route-operating-model.zh-CN.md` | KEEP + LINK UPDATE | 当前建设 Operating Model；其 Route 链接在迁移后需更新 |
| `docs/flat-graph-and-dynamic-maps.zh-CN.md` | KEEP | 当前架构 / 建模原则 |
| `docs/human-interface-specification-v0.1.zh-CN.md` | KEEP | IA 自身 Human Interface Specification 草案 |
| `docs/human-readable-interaction-baseline.zh-CN.md` | KEEP | 虽为 provisional，但已经表达当前采用规则，而不仅是外部参考清单 |
| `docs/interopatlas-definition-and-scope-v0.2.zh-CN.md` | KEEP | 项目 Definition / Scope |
| `docs/knowledge-object-classification-specification-v0.1.zh-CN.md` | KEEP | 当前知识对象 Specification 草案 |
| `docs/language-policy.zh-CN.md` | KEEP | 当前语言 Policy |
| `docs/open-collaboration-profile-v0.1.zh-CN.md` | KEEP | 当前 Human–AI / Open Collaboration Profile |
| `docs/practice-feedback-loop.zh-CN.md` | KEEP | 已采用的长期 Atlas ↔ Runtime 实践反馈机制 |
| `docs/project-development-principles.zh-CN.md` | KEEP | 当前项目建设原则 / 最小治理规则 |
| `docs/repository-structure-profile-v0.1.zh-CN.md` | KEEP + UPDATE | 仍包含有效 IA-RS 规范要求，但部分“物理布局仍未决定 / legacy roots”描述已被 PR #45 的现实状态超越 |
| `docs/task-reference-seeding-profile-v0.1.zh-CN.md` | KEEP | 当前 Reference Seeding Extension Profile |

### B. 迁入 `03_Evolution/01_Research/` — 13

| 当前文件 | 建议目标 | 原因 |
|---|---|---|
| `docs/foundation-work-package-a-completion-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Completion Audit |
| `docs/foundation-work-package-a-reference-intake-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Reference Intake Audit |
| `docs/human-ai-open-collaboration-prior-art.zh-CN.md` | `03_Evolution/01_Research/` | Prior Art |
| `docs/human-interface-conformance-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Conformance Audit |
| `docs/human-interface-reference-intake-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Reference Intake Audit |
| `docs/human-interface-reference-map.zh-CN.md` | `03_Evolution/01_Research/` | Living Reference / evidence map，服务后续 Specification |
| `docs/human-interface-standards-baseline.zh-CN.md` | `03_Evolution/01_Research/` | 外部 Standards / Methods baseline，是 IA 规则的输入而非 IA 自身规范 |
| `docs/prior-art-and-method-reference.zh-CN.md` | `03_Evolution/01_Research/` | Prior Art / Method reference index |
| `docs/repository-structure-prior-art-and-options-v0.1.zh-CN.md` | `03_Evolution/01_Research/` | Prior Art 与方案比较 |
| `docs/route-alignment-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Route alignment Audit |
| `docs/work-package-a-reference-intake-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Reference Intake Audit |
| `docs/work-package-a-verification-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Verification / Audit |
| `docs/work-package-b-pilot-audit-2026-09-01.zh-CN.md` | `03_Evolution/01_Research/` | Pilot Audit / feedback evidence |

### C. 迁入 `03_Evolution/02_Experiments/` — 6

| 当前文件 | 建议目标 | 原因 |
|---|---|---|
| `docs/experiments/automated-build-deployment-open-alternative.zh-CN.md` | `03_Evolution/02_Experiments/` | 开放替代实验 |
| `docs/experiments/engine-v0.1-bootstrap.zh-CN.md` | `03_Evolution/02_Experiments/` | Engine bootstrap experiment |
| `docs/experiments/engine-v0.1-coverage-baseline.zh-CN.md` | `03_Evolution/02_Experiments/` | Coverage experiment / baseline result |
| `docs/experiments/human-ai-collaboration-v0-checklist.zh-CN.md` | `03_Evolution/02_Experiments/` | Pilot / experiment checklist |
| `docs/json-ld-fit-experiment.zh-CN.md` | `03_Evolution/02_Experiments/` | JSON-LD Fit Experiment；可与已迁入的 `json-ld/` fixture 共置 |
| `docs/seed-experiment-01.zh-CN.md` | `03_Evolution/02_Experiments/` | 早期 seed experiment |

迁移完成后，旧 `docs/experiments/` 应自然消失，不再建立第二个 Experiments 区。

### D. 迁入 `03_Evolution/03_Change/` — 11

| 当前文件 | 建议目标 | 原因 / 状态 |
|---|---|---|
| `docs/foundation-first-phase-v0.1.zh-CN.md` | `03_Evolution/03_Change/` | Working Phase Plan / Gate plan |
| `docs/human-readable-route.zh-CN.md` | `03_Evolution/03_Change/` | Provisional Route，描述 Human Route 如何继续演化 |
| `docs/machine-readable-maintainable-route.zh-CN.md` | `03_Evolution/03_Change/` | Provisional Route，描述 Machine Route 如何继续演化 |
| `docs/object-page-shell-v0.1-plan.zh-CN.md` | `03_Evolution/03_Change/` | Implementation Plan / vertical slice plan |
| `docs/open-collaboration-route-v0-notes.zh-CN.md` | `03_Evolution/03_Change/` | 早期 Working Notes；其规范角色已被正式 Profile 取代 |
| `docs/project-generated-methods-standards.zh-CN.md` | `03_Evolution/03_Change/` | 明确标注 Future Direction / Provisional Note |
| `docs/repository-current-to-target-mapping-v0.1.zh-CN.md` | `03_Evolution/03_Change/` | Migration Dry Run / mapping；PR #45 后主要成为迁移历史 |
| `docs/repository-data-root-contract-v0.1.zh-CN.md` | `03_Evolution/03_Change/` | 原 Implementation Preparation / Migration Guardrail，且其中 legacy physical paths 已被实际迁移超越 |
| `docs/roadmap.zh-CN.md` | `03_Evolution/03_Change/` | Roadmap 本身属于项目演化 |
| `docs/visualization-direction.zh-CN.md` | `03_Evolution/03_Change/` | 明确标注 Future Direction |
| `docs/work-item-reference-seeding-v0.1.zh-CN.md` | `03_Evolution/03_Change/` | 早期 Draft Addendum，与后来的 `task-reference-seeding-profile-v0.1` 高度重叠；先保留为演化历史，不在本次直接删除 |

---

## 4. 发现的两个重要问题

### 4.1 `docs/` 的职责文字已经与仓库结构冲突

当前 `docs/README.md` 仍声称该目录同时承载 research，而新的 `03_Evolution` 已明确把 Research 作为自身一级职责。

后续迁移必须把 `docs/README.md` 改成更明确的入口：

> **docs = current project contract / guidance**

它可以链接到 Evolution 中的研究和历史，但不应再物理承载全部过程材料。

### 4.2 有些文档不是“搬家”就结束，还需要状态修正

特别是：

- `repository-structure-profile-v0.1.zh-CN.md`：应该继续作为规范文档保留，但需同步 PR #45 后的现实物理结构；
- `repository-data-root-contract-v0.1.zh-CN.md`：当前部分内容描述迁移前 legacy roots，应作为演化 / 迁移历史，不应继续让新贡献者误认为是 current state；
- `work-item-reference-seeding-v0.1.zh-CN.md` 与 `task-reference-seeding-profile-v0.1.zh-CN.md` 存在明显世代 / 重叠关系；本次只分区，不自动删除或合并；
- `foundation-work-package-a-reference-intake-audit...` 与 `work-package-a-reference-intake-audit...` 名称和职责接近，后续可以单独做重复性核验，但本次不去重。

---

## 5. 建议的迁移方式

正式执行时应作为**单独的 docs/Evolution migration PR**，不要与内容重写或规范升级混成一个大项目。

建议顺序：

```text
1. 按本表移动 Research / Experiments / Change 文件
2. 保留文件名，不在同一 PR 顺便重命名
3. 更新所有 Markdown 内部链接
4. 重写 docs/README.md 导航
5. 更新 03_Evolution 三个二级 README 的索引 / 示例
6. 对 KEEP 文档扫描旧路径与旧状态描述
7. 运行 link / path search，确认不存在 docs/experiments 或旧相对链接
8. 不删除疑似重复历史文档；另开去重工作
```

这次迁移不涉及 Canonical State、Engine、Graph 或公共对象 URL，因此不应重新打开 `01_State` / `02_Runtime` 结构问题。

---

## 6. 结论

三大区域结构已经能够自然吸收现有文档，不需要继续增加新的一级或二级目录。

推荐最终职责压缩为：

```text
docs/
    现在应该相信 / 遵守 / 理解什么

03_Evolution/01_Research/
    为什么这样判断

03_Evolution/02_Experiments/
    我们怎样试过 / 验证过

03_Evolution/03_Change/
    接下来怎样改变
```

本审计建议下一步进入独立物理迁移，但在执行前先由 Maintainer 确认这张分类表，尤其是 `docs/` 中 15 个 KEEP 文档与 11 个 Change 文档的边界。