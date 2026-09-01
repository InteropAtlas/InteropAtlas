# InteropAtlas Foundation First Phase v0.1

> 状态：Working Plan / 暂定阶段计划
>
> 目的：纠正“基础规范尚未形成，却过早推进具体网站实现”的路线偏移。当前阶段先让知识模型、Human Interface、开放协作、可信收录和机器正确性达到最小可依赖状态，再把 Reference Implementation 恢复为主要实现线。

## 0. 当前 Gate 状态

截至 2026-09-01 当前仓库状态：

- **Gate A — Repository Structure：PASS + physical implementation completed**；
- **Gate B — Human Interface：NOT YET PASS**；
- **Gate C — Open Collaboration：PASS + V0.1 Pilot completed**。

因此整个 Foundation Gate 仍未通过，当前唯一未通过的正式 Gate 是 Human Interface；同时 F4 Machine / Curation / Trust 仍需继续作为基础线补齐。

相关当前文档：

- Repository Structure：[`../../docs/repository-structure-profile-v0.1.zh-CN.md`](../../docs/repository-structure-profile-v0.1.zh-CN.md)
- Human Interface：[`../../docs/human-interface-specification-v0.1.zh-CN.md`](../../docs/human-interface-specification-v0.1.zh-CN.md)
- Open Collaboration：[`../../docs/open-collaboration-profile-v0.1.zh-CN.md`](../../docs/open-collaboration-profile-v0.1.zh-CN.md)
- Work Package A audit：[`../01_Research/foundation-work-package-a-completion-audit-2026-09-01.zh-CN.md`](../01_Research/foundation-work-package-a-completion-audit-2026-09-01.zh-CN.md)
- Work Package B pilot audit：[`../01_Research/work-package-b-pilot-audit-2026-09-01.zh-CN.md`](../01_Research/work-package-b-pilot-audit-2026-09-01.zh-CN.md)

## 1. 当前判断

Foundation First 原则继续成立：

> **先让规则、模型和运行边界足够可靠，再继续扩大具体实现。**

但“基础建设”不再等于继续整理文件夹。

Repository Structure 与 Open Collaboration 已经从“设计阶段”进入实际运行阶段；现在的主要瓶颈变成：

```text
Non-normative Knowledge Object Model
        ↓
Human Interface Standards Package
        ↓
Conformance Gate
        ↓
Reference Implementation
```

同时 Curation / Evidence / Schema correctness / Query correctness 作为 F4 并行推进。

## 2. 四个基础工作包

### F1 — Repository Structure & Artifact Boundaries — COMPLETE

已经形成并实施：

```text
01_State/
02_Runtime/
03_Evolution/
```

State：

```text
01_State/
├── 01_Objects/
└── 02_Relations/
```

Runtime：

```text
02_Runtime/
├── 01_Engine/
├── 02_Tools/
└── 03_Outputs/
```

Evolution：

```text
03_Evolution/
├── 01_Research/
├── 02_Experiments/
└── 03_Change/
```

当前已经完成：

- Storage ≠ Semantics ≠ View 原则落地；
- Canonical State 物理迁移；
- Schema 与 State 共置；
- Runtime 迁移；
- stable public route 与 physical path 解耦；
- Research / Experiments / Change 与 `docs/` 分流；
- CI / 文档路径检查更新。

因此 F1 不再阻塞 #15，也不等待知识对象模型来决定语义文件夹。

### F2 — Human Interface Standards Package — IN PROGRESS / NOT PASS

回答：**IA 面向人的信息应该怎样组织、呈现、交互和验收？**

现有 `IA-HI v0.1` 已经提供综合规范基础，但 Gate B 仍要求至少形成五个可独立审计的 Draft Profile：

1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个模块必须能回答：

- 用户任务 / Context of Use 是什么；
- 采用了哪些正式标准和 Mature Prior Art；
- 属于 Adopt / Profile / Extend / Invent 哪一层；
- BCP 14 Requirements 是什么；
- 如何验证符合性；
- 与其他模块冲突时如何处理。

#### 当前前置瓶颈：#15

Human Interface 已经需要引用大量 Method、Heuristic、Framework、Design System 和 Mature Precedent，但当前数据模型无法自然表达这些对象。

因此当前先推进：

```text
#23 / PR #30 — Batch 1 Fit Test
        ↓
Batch 2 — 累计达到 8–12 个样本
        ↓
候选模型比较
        ↓
#15 Model Decision
        ↓
必要时修改 Schema
        ↓
完成 #14 五个 Draft Profiles
```

这不是因为 #15 决定文件夹，而是因为 #15 决定这些知识对象在 Atlas 中**是什么**。

### F3 — Open Collaboration / Human–AI Collaboration — COMPLETE AT V0.1 PILOT

Draft Profile 已经完成，Work Package B #22 也已经完成真实 GitHub-native Pilot。

已经落地：

- `CONTRIBUTING.md`；
- `AGENTS.md`；
- Work Item Issue Form；
- PR Template；
- Ready / Claim / Lease / Handoff / Review Class；
- 真实任务 #23 / #24 / #25；
- #24 的完整 Pilot；
- Pilot friction / gaps 记录。

当前后续：

- PR #26 v0.2 Draft 保持 high-impact Review Gate；
- #27 Identity friction 保持 Draft；
- Issue Fields / CODEOWNERS / Ruleset / automation 按真实需要再增强；
- 不自动开发 Lease Server / heartbeat。

F3 的这些后续演化不阻塞 F2 / F4。

### F4 — Curation / Evidence / Machine Correctness — IN PROGRESS / NOT PASS

当前 Engine 已经具备：

- deterministic Loader；
- Graph / Backlink Index；
- stable object route；
- canonical storage contract；
- `reference_issues = 0` 的当前基线。

仍需要补齐：

1. JSON Schema 全量 enforcement；
2. #9 Curation / Contribution minimum workflow；
3. #10 Evidence / Provenance / Trust minimum model；
4. #7 query scope correctness；
5. regression tests；
6. legacy Relation `type: relation` cleanup。

F4 与 #15 / #14 并行，不通过增加新网站功能来代替验证。

## 3. Reference Implementation 的定位

当前 GitHub Pages、Renderer、Local Map、Engine Bootstrap 继续保留为：

> **Reference Implementation / Test Bed（参考实现 / 试验场）**

规则：

- 已完成且符合上游规范的实现不回滚；
- #12 / #13 / #16 / #17 暂不作为主 P0；
- 新首页、Search、复杂 Local Map、全图 Explore、视觉品牌化等继续等待 Gate B；
- Human Interface Profile 可以使用现有网站做 conformance evidence，但不能让现有代码反向决定规范。

## 4. Foundation Gate

### Gate A — Repository Structure — PASS

- [x] Repository Structure Profile；
- [x] 三大生命周期区域；
- [x] Canonical State / Runtime 物理迁移；
- [x] storage / semantics / public route 解耦；
- [x] docs / Evolution boundary；
- [x] migration regression baseline。

### Gate B — Human Interface — NOT PASS

- [ ] Information Architecture Draft；
- [ ] Information Presentation Draft；
- [ ] Interaction Draft；
- [ ] Visual Presentation Draft；
- [ ] Accessibility / Conformance Draft；
- [ ] 关键 Requirements 有上游依据；
- [ ] Non-normative HCI Knowledge Object Model 可用；
- [ ] 可以执行一次 Gate B conformance audit。

### Gate C — Open Collaboration — PASS

- [x] Open Collaboration Profile v0.1；
- [x] participant roles / task lifecycle / review / handoff / claim semantics；
- [x] GitHub-native mapping；
- [x] AGENTS.md boundary；
- [x] Collaboration Implementation Pilot；
- [x] friction / gap audit。

## 5. 当前执行顺序

当前不再从多个 Candidate Work Package 中随机选择，而采用下面的主次关系：

```text
P0 主线
#15 / #23 Knowledge Object Model
        ↓
#14 Human Interface Standards Package
        ↓
Gate B Audit
        ↓
Reference Implementation 恢复为 P0

Foundation 并行线
#8 剩余 Schema / Validator correctness
#9 Curation
#10 Evidence / Provenance
#7 Query correctness

后续演化线
PR #26 Open Collaboration v0.2 review
#27 Participant / Agent identity research
```

当前下一小步：**先把 #23 / PR #30 整理到符合新的 Repository Structure / Evolution 边界，再继续 Batch 2。**

## 6. 采用原则

继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

仓库结构、AI 协作、网页设计、知识模型、Evidence 和自动化都属于互操作系统设计问题，因此都应先确认已有标准、成熟先例和方法，再决定 IA-specific 扩展。
