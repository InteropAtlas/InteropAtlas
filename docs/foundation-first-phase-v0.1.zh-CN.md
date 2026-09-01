# InteropAtlas Foundation First Phase v0.1

> 状态：Working Plan / 暂定阶段计划
>
> 目的：纠正“基础规范尚未形成，却过早推进具体网站实现”的路线偏移。当前阶段先定义项目怎样组织知识、怎样设计人类界面、怎样让人类与 AI / Agent 协作、怎样组织仓库与贡献流程；Reference Implementation（网站、自动化交互等）在这些基础达到最小可用后再继续。

## 0. 当前 Gate 状态

截至 2026-09-01：

- **Gate A — Repository Structure：PASS at Draft Profile level**；
- **Gate B — Human Interface：NOT YET PASS**；
- **Gate C — Open Collaboration：PASS at Draft Profile level**。

Work Package A 完成审计见：`foundation-work-package-a-completion-audit-2026-09-01.zh-CN.md`。

Gate A 的上位产物：`repository-structure-profile-v0.1.zh-CN.md`。

Gate C 的上位产物：`open-collaboration-profile-v0.1.zh-CN.md`。

整个 Foundation Gate 仍未通过，因为 Human Interface Standards Package 与 Non-normative Knowledge Object Model 仍未完成。

## 1. 当前判断

InteropAtlas 已经有可工作的数据、Graph、Renderer 和 GitHub Pages，也已经形成若干 Human Interface 与 Open Collaboration 研究材料。

当前 Foundation First 原则继续成立：

> **先建立规范与项目运行结构，再继续实现。**

经过 Work Package A，Repository Structure 与 Open Collaboration 已经从 Research / Working Notes 进入 Draft Profile 阶段；Human Interface 与 Machine / Curation / Trust 仍需要继续补齐。

## 2. 当前四个基础工作包

### F1 — Repository Structure & Artifact Taxonomy — Draft Profile COMPLETE

已形成：
- Prior Art / Options；
- Current → Target Mapping；
- Artifact Taxonomy；
- Repository Structure Profile v0.1；
- Migration Plan；
- Community Health target set。

当前决策：

> **Layered Monorepo now, extraction-ready later.**

逻辑目标包括 Canonical Data、Schemas、Engine、Tests、Tools、Specifications、Research、Docs、Governance、Experiments 等明确 Zone。

当前不大规模移动目录；物理迁移属于后续 implementation。

### F2 — Human Interface Standards Package — IN PROGRESS / NOT PASS

先回答：**IA 面向人的信息到底应该怎样组织、传递和交互？**

当前 `IA-HI v0.1` 保留为综合草案，但下一阶段需要把它拆成可审计的模块或 Profile：

1. Information Architecture Profile；
2. Information Presentation Profile；
3. Interaction Profile；
4. Visual Presentation Profile；
5. Accessibility / Conformance Profile。

每个模块必须记录：
- 用户任务；
- 上游标准与 Existing Standards & Prior Art；
- Adopt / Profile / Extend / Invent；
- BCP 14 Requirements；
- 可验证验收方法。

同时 #15 需要建立 Non-normative Knowledge Object Model，使 Method / Guideline / Design System / Mature Precedent 可以被正确收录。

在这套 Package 达到最小 Draft coverage 之前，不继续增加网站功能。

### F3 — Open Collaboration / Human–AI Collaboration — Draft Profile COMPLETE

已形成 `open-collaboration-profile-v0.1.zh-CN.md`，定义：

- Participant Roles；
- Agent-ready / Human-ready Work Item Contract；
- Issue / Sub-issue / Dependency Task Graph；
- Draft → Ready → Claimed → In Progress → Review → Done 生命周期；
- Lease-style Claim；
- Handoff / Continuity；
- Review / Oversight / Authorization；
- Agent contribution transparency；
- AGENTS.md boundary；
- GitHub-native mapping；
- candidate gaps 与 implementation sequence。

下一阶段若选择 Collaboration Implementation Pilot，再把 Profile 投影到 GitHub Issues / Projects / PR / Review / AGENTS.md。

### F4 — Curation / Evidence / Machine Correctness — NOT PASS

Canonical Data 的可信建设还需要并行补：

- Curation / Contribution minimum workflow；
- Evidence / Provenance minimum model；
- Validator / Schema correctness；
- Query correctness + regression tests；
- Reference / relation integrity。

这条线继续并行，但不把新网站功能作为验证它们的唯一方式。

## 3. Reference Implementation 的定位

当前 GitHub Pages、Renderer、Local Map、Engine Bootstrap 都保留，但角色是：

> **Reference Implementation / Test Bed（参考实现 / 试验场）**

它们用于验证 Specification 是否可实现、是否存在缺口，不负责反向定义 Specification。

因此：
- 已完成且符合上游规范的语义修正无需回滚；
- #17 Object Page Shell 暂停继续扩展；
- #13 Browser E2E 保留，但在 Interaction / Conformance Profile 更清楚后继续；
- 新 UI、首页重构、Local Map 功能、Visual Tokens 实现暂缓。

## 4. Foundation Gate

只有满足以下最小条件后，Human-readable Website 才恢复为 P0 实现工作。

### Gate A — Repository Structure — PASS

- [x] Repository Structure Profile v0.1；
- [x] Artifact taxonomy / lifecycle；
- [x] 目录迁移 Decision；
- [x] CONTRIBUTING / Community Health target structure。

### Gate B — Human Interface — NOT PASS

- [ ] Information Architecture Draft；
- [ ] Information Presentation Draft；
- [ ] Interaction Draft；
- [ ] Visual Presentation Draft；
- [ ] Accessibility / Conformance Draft；
- [ ] 各模块有上游依据与最小 Requirement IDs；
- [ ] Non-normative HCI knowledge object model 可用。

### Gate C — Open Collaboration — PASS

- [x] Open Collaboration Profile v0.1；
- [x] participant roles / task lifecycle / review / handoff / claim semantics；
- [x] GitHub-native mapping；
- [x] AGENTS.md 的职责与边界。

Gate 不要求这些文档已经成为成熟 Standard，但要求它们已经足够指导实现，而不是由实现反向临时决定规则。

## 5. 当前执行顺序

Work Package A 完成后不自动进入 Collaboration Implementation。

当前可由 Maintainer 选择：

```text
Candidate B — Collaboration Implementation Pilot
Candidate C — #15 Knowledge Object Model
Candidate D — #14 Human Interface Standards Package
Candidate F4 — #7/#8/#9/#10 Machine / Curation / Trust
```

物理仓库迁移仍不应先于对应 implementation work package。

## 6. 采用原则

继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

仓库结构、AI 协作、网页设计与数据模型都属于互操作问题，因此同样必须先研究成熟方案，而不是把它们当成“项目内部随便约定的小事”。
