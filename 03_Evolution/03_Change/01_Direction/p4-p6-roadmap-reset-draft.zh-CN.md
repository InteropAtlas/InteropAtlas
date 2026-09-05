# InteropAtlas P1–P6 Roadmap Reset v1 — Historical P4.6 Draft

> Lifecycle: **Historical / Completed P4.6 Change Artifact**
>
> Original Role: P4.6 Roadmap Reset after P1–P4
>
> Successors: `docs/interopatlas-long-term-roadmap.zh-CN.md` for durable long-term phase relationships; `PROJECT_STATE.md` + current GitHub Issues / PRs for execution state.
>
> Current Role: 保存 2026-09-04 从 P4 架构形成阶段进入 P5/P6 的路线重置历史。本文中的 `NEXT`、Issue critical path、Fast Lane、Gate 与 P6 task ordering 是当时施工状态，不再具有当前路线 authority。

## Historical context

这份 Roadmap Reset 的核心作用，是在 InteropAtlas 从早期 Reference Implementation 功能路线转向 Canonical Contract + Intake + Migration + Workspace + Human/Agent Access 后，重新安排 P5 真实数据实验与 P6 实现顺序。

当时形成的核心判断包括：

> **Candidate discovery 可以立即规模化；bounded Canonical intake 在 P5 小批启动；broad ordinary Canonical intake 只在真实实验通过 Gate 后规模化。**

它明确避免两个极端：一是等待所有架构、迁移和前端完成后才开始收录；二是在 Contract 未经真实数据验证前直接 mass ingest。

## Historical phase map

当时的阶段状态为：

```text
P1 Design Principles                         Completed
P2 Prior-art / Standards Research            Completed
P3 Current-State Audit                       Completed
P4 Architecture / Roadmap Reset              Closing
P5 Real-data Experiments / Intake Stress     NEXT
P6 V1 Implementation + Continuous Intake     Future
```

此状态现已过期。当前长期路线图已经记录 P4 完成、P5 主线完成并进入 P6；实时状态必须读取 `PROJECT_STATE.md`。

## P5 execution model formed here

P5 被设计成真实数据实验 / Intake Stress Test，而不是继续纯理论架构设计。主要目标包括：

- Identity / Version / Family-Kind fit；
- Relation + Evidence / Assertion / Conflict + Lifecycle fit；
- Migration + Workspace + Human/Agent write-back E2E；
- bounded Candidate → Canonical Intake stress test；
- Contribution-Ready Gate。

同时开放 Candidate discovery、source confirmation、dedup、Evidence gap、relation/lifecycle/identity ambiguity inventory、migration mapping、Workspace audit、validator/graph baseline 等非破坏性 Fast Lanes。

## Intake scaling model formed here

Roadmap Reset 将“什么时候可以快速收入标准”拆成三层：

1. **Candidate discovery** — 可以立即并行；
2. **bounded Canonical intake** — 在 P5 用小批真实候选验证；
3. **broad continuous Canonical intake** — Gate 通过后进入 early P6 并逐步扩大。

这个分层思想仍可能被现行运行模型继承，但具体 Issue 编号、batch 数量和 Gate 状态属于历史施工上下文，应读取当前文档与 Issue。

## P6 implementation direction formed here

当时的 P6 第一轮方向包括：

- V1 serialization / validator minimal production loop；
- Continuous Intake；
- Migration Cohort；
- Compare + Evidence Workspace；
- Agent structured read/query + Candidate Write；
- 后续 intake scaling、migration retirement、workspace expansion、quality / coverage loops。

Roadmap 明确 P6 不是项目终点，而是进入长期持续运营基础。

## Authority / stop conditions

当时已经明确：普通 bounded research、Candidate discovery、fixtures、inventory 和 machine audits 可以自主推进；identity merge/split、destructive mutation、stable specification/governance promotion、broad intake activation、permission/security material change 与 Legacy retirement 必须进入更高 authority boundary。

## Supersession note

2026-09-05 文档生命周期审计确认，本文件已经完成 P4.6 的阶段性施工职责。继续放在 `docs/` 会与长期路线图和 `PROJECT_STATE.md` 形成三个并列的路线 authority，并保留大量已经过期的 `NEXT` / Issue 编号 / Gate 状态。

因此将其归档到 `03_Evolution/03_Change/`。长期方向由 `docs/interopatlas-long-term-roadmap.zh-CN.md` 维护；当前执行断点只由 `PROJECT_STATE.md` + GitHub Issue / PR 维护。
