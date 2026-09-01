# InteropAtlas Documentation

This directory contains InteropAtlas architecture, methodology, governance, research, and design documentation.

## Start here

- [`interopatlas-definition-and-scope-v0.2.zh-CN.md`](interopatlas-definition-and-scope-v0.2.zh-CN.md) — **当前项目定义与收录边界：InteropAtlas 是互操作知识地图，不只收录正式标准。**
- [`knowledge-object-classification-specification-v0.1.zh-CN.md`](knowledge-object-classification-specification-v0.1.zh-CN.md) — **知识对象分类规范草案：区分 Normative Artifact、Mature Precedent、Method、Implementation 等，并规定证据与权威性边界。**
- [`roadmap.zh-CN.md`](roadmap.zh-CN.md) — 当前路线图、优先级与近期执行顺序。
- [`foundation-first-phase-v0.1.zh-CN.md`](foundation-first-phase-v0.1.zh-CN.md) — **当前 Foundation First 阶段：先建立仓库结构、Human Interface 标准包、Human–AI 协作 Profile，再恢复网站实现。**
- [`route-alignment-audit-2026-09-01.zh-CN.md`](route-alignment-audit-2026-09-01.zh-CN.md) — 2026-09-01 多会话 / 仓库路线对齐审计。
- [`five-route-operating-model.zh-CN.md`](five-route-operating-model.zh-CN.md) — 五路线协同模型：Human、Machine、Curation、Trust、Governance；Open Collaboration 当前作为横向协作层。
- [`project-development-principles.zh-CN.md`](project-development-principles.zh-CN.md) — 当前项目建设原则与最小治理规则。
- [`prior-art-and-method-reference.zh-CN.md`](prior-art-and-method-reference.zh-CN.md) — 可持续维护的 Existing Standards & Prior Art / 参考项目与方法索引。

## Foundation work

- **#21 Repository Structure & Artifact Taxonomy** — 仓库结构、文档 / 规范产物类型、生命周期、Community Health 与迁移决策。
  - [`repository-structure-prior-art-and-options-v0.1.zh-CN.md`](repository-structure-prior-art-and-options-v0.1.zh-CN.md) — GitHub / REUSE / W3C / MDN / CNCF / SPDX / Diátaxis 等成熟先例与三种结构候选比较。
  - [`repository-current-to-target-mapping-v0.1.zh-CN.md`](repository-current-to-target-mapping-v0.1.zh-CN.md) — 当前真实仓库逐项映射到 Artifact Taxonomy 与候选 Target Zone，不执行物理迁移。
- **#14 Human Interface Standards Package** — Information Architecture / Presentation / Interaction / Visual / Accessibility-Conformance。
- **#15 Non-normative Knowledge Object Model** — Mature Precedent / Method / Guideline / Heuristic / Framework / Design System 等非规范性知识对象。
- **#19 Open Collaboration / Human–AI Collaboration Profile** — roles、task lifecycle、租赁式认领语义、Review / Handoff / Authorization、GitHub / AGENTS.md 映射。

## Core routes

### Human Route

- [`human-readable-route.zh-CN.md`](human-readable-route.zh-CN.md) — 人类可读路线：Visible → Actionable。
- [`human-interface-specification-v0.1.zh-CN.md`](human-interface-specification-v0.1.zh-CN.md) — Human Interface 综合草案；当前作为 Standards Package 的输入，而不是已完成的基础。
- [`human-interface-standards-baseline.zh-CN.md`](human-interface-standards-baseline.zh-CN.md) — Human Interface 外部标准基线与 Adopt → Profile → Extend → Invent 原则。
- [`human-interface-reference-map.zh-CN.md`](human-interface-reference-map.zh-CN.md) — 将交互、信息架构、视觉、无障碍、图探索、测试等问题映射到标准、方法与参考实现。
- [`human-readable-interaction-baseline.zh-CN.md`](human-readable-interaction-baseline.zh-CN.md) — 暂定交互基线与 Existing Standards & Prior Art。
- [`human-interface-conformance-audit-2026-09-01.zh-CN.md`](human-interface-conformance-audit-2026-09-01.zh-CN.md) — 第一次 IA-HI v0.1 符合性审计；作为反馈材料保留。
- [`object-page-shell-v0.1-plan.zh-CN.md`](object-page-shell-v0.1-plan.zh-CN.md) — Reference Implementation vertical slice；当前等待 Foundation Gate 后继续。

### Machine / Practice

- [`machine-readable-maintainable-route.zh-CN.md`](machine-readable-maintainable-route.zh-CN.md) — 机器可用 / 可维护路线：Loadable → Interoperable。
- [`practice-feedback-loop.zh-CN.md`](practice-feedback-loop.zh-CN.md) — Atlas ↔ Engine 实践驱动反馈机制。

### Open Collaboration / Human + Agent

- [`human-ai-open-collaboration-prior-art.zh-CN.md`](human-ai-open-collaboration-prior-art.zh-CN.md) — Human-Machine Teaming、NIST、Linux Foundation / AGENTS.md、GitHub 等开放协作 Prior Art。
- [`open-collaboration-route-v0-notes.zh-CN.md`](open-collaboration-route-v0-notes.zh-CN.md) — Open Collaboration V0 工作笔记；下一步由 #19 推进为可审计 Profile。

## Architecture and modeling

- [`architecture-v0.1.zh-CN.md`](architecture-v0.1.zh-CN.md) — 当前架构草案，已同步“互操作方案空间”定义。
- [`flat-graph-and-dynamic-maps.zh-CN.md`](flat-graph-and-dynamic-maps.zh-CN.md) — Flat Objects + Rich Relations + Dynamic Maps。
- [`visualization-direction.zh-CN.md`](visualization-direction.zh-CN.md) — 图形化关系呈现方向。
- [`json-ld-fit-experiment.zh-CN.md`](json-ld-fit-experiment.zh-CN.md) — JSON-LD / linked-data 适配实验。

## Project-generated methods and standards

- [`project-generated-methods-standards.zh-CN.md`](project-generated-methods-standards.zh-CN.md) — IA 自身产生的方法、规范、标准与 Skills 的暂定治理方向。
- [`language-policy.zh-CN.md`](language-policy.zh-CN.md) — 语言政策。

## Experiments

- [`experiments/`](experiments/) — Engine、Coverage、开放替代等实践实验记录。
- [`seed-experiment-01.zh-CN.md`](seed-experiment-01.zh-CN.md) — 早期 seed experiment。

## Documentation status

Unless explicitly marked otherwise, current architecture and methodology documents are living / provisional references rather than frozen InteropAtlas standards.

Original prose documentation in this directory is licensed under **CC BY 4.0**, unless explicitly stated otherwise.
