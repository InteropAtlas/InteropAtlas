# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）。
>
> 当前阶段：**Foundation First（基础先行）**。
>
> 详细阶段定义：`foundation-first-phase-v0.1.zh-CN.md`。

## 当前总体判断

InteropAtlas 当前不把网站、Renderer 或具体 Agent 自动化当作第一优先级，而是先建立能够长期指导实现的基础规范。

Foundation 当前四个工作包：

1. **F1 Repository Structure / Artifact Taxonomy**；
2. **F2 Human Interface Standards Package**；
3. **F3 Open Collaboration / Human–AI Collaboration**；
4. **F4 Curation / Evidence / Machine Correctness**。

其中 Work Package A 已完成 **F1 + F3 的 Draft Profile**。

完成审计：`foundation-work-package-a-completion-audit-2026-09-01.zh-CN.md`。

原则保持不变：
- Interoperability 是问题边界；
- Reuse Before Invent；
- Adopt → Profile → Extend → Invent；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Human ↔ Machine Co-development；
- Practice-driven Feedback；
- graph-native, database-agnostic。

## 已完成的 Foundation Profiles

### Gate A / F1 — Repository Structure：PASS at Draft level

已形成：
- `repository-structure-prior-art-and-options-v0.1.zh-CN.md`；
- `repository-current-to-target-mapping-v0.1.zh-CN.md`；
- `repository-structure-profile-v0.1.zh-CN.md`。

当前决策：

> **Layered Monorepo now, extraction-ready later.**

目标逻辑边界已经明确：
- Canonical Data；
- Schemas / Contracts；
- Engine / Tools / Tests；
- IA-produced Specifications；
- Research / Prior Art / Audits；
- Documentation；
- Governance；
- Experiments；
- Generated Views。

目标采用单一 Canonical Data boundary（候选 `data/`），但当前**尚未执行物理目录迁移**。

迁移必须保持 stable IDs、object / relation / graph semantics 和 `reference_issues = 0` 等不变量。

### Gate C / F3 — Open Collaboration：PASS at Draft level

已形成：
- `human-ai-open-collaboration-prior-art.zh-CN.md`；
- `open-collaboration-route-v0-notes.zh-CN.md`；
- `open-collaboration-profile-v0.1.zh-CN.md`。

当前协作合同已经定义：
- Steward / Planner / Executor / Reviewer / Maintainer / Automation roles；
- Agent-ready / Human-ready Work Item Contract；
- GitHub Issue / Sub-issue / Dependency Task Graph；
- Draft → Ready → Claimed → In Progress → Review → Done 生命周期；
- Lease-style Claim；
- Handoff / Continuity；
- Independent Review / Human authorization；
- Agent contribution transparency；
- AGENTS.md 的职责边界；
- GitHub-native mapping。

目标运行模型：

```text
Vision / Specification
       ↓
Ready Work Items
       ↓
Lease-style Claim
       ↓
Independent Execution
       ↓
Public Artifact / PR
       ↓
Independent Review
       ↓
Maintainer Authorization where required
       ↓
Merge / Done / Handoff
```

当前**尚未实现** CONTRIBUTING 重写、AGENTS.md、templates、Project Fields、CODEOWNERS / Ruleset、Lease automation 或真实任务试运行。

这些属于候选 Work Package B，不自动执行。

## 当前仍未完成的 Foundation

### P0-F2：Human Interface Standards Package

相关：#14、#15。

需要形成至少五个可审计模块：
1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个模块需要：
- 用户任务 / context；
- 上游标准 / Mature Precedent；
- Adopt / Profile / Extend / Invent；
- BCP 14 Requirements；
- 验收 / conformance 方法。

同时 #15 需要用真实 Mature Precedent / Method / Design System 做 Fit Test，形成 Non-normative Knowledge Object Model，再修改 Schema。

### P0-F4：Curation / Evidence / Machine Correctness

相关：#7、#8、#9、#10。

继续需要：
- Curation / Contribution minimum workflow；
- Evidence / Provenance minimum model；
- JSON Schema validation；
- ID / reference / type correctness；
- 保持 `reference_issues = 0`；
- 修复 #7 query scope；
- regression tests。

## Candidate next Work Package — 由 Maintainer 决定

Work Package A 完成后不自动继续。

### Candidate B — Collaboration Implementation Pilot

把 `open-collaboration-profile-v0.1` 映射到 GitHub：
- CONTRIBUTING；
- Issue / PR Templates；
- Issue / Project Fields；
- CODEOWNERS / Rulesets；
- AGENTS.md；
- 2–3 个真实 Ready Task；
- Lease / Handoff / Review 试运行。

### Candidate C — Knowledge Object Model

推进 #15：真实对象 Fit Test → Model Decision → Schema。

### Candidate D — Human Interface Standards Package

推进 #14：形成五个 Human Interface Draft Profiles。

### Candidate F4 — Machine / Curation / Trust

推进 #7/#8/#9/#10。

## Reference Implementation 继续保持 P1

### #17 Object Page Shell

已经完成的 `<main>`、semantic Breadcrumb、Identity Before Exploration 等修正保留，不回滚；等待 Gate B 再继续。

### #13 Browser E2E / Accessibility

等待 Interaction / Accessibility / Conformance Profile 明确测试合同后恢复。

### Website / Global Information Architecture / Visual System

Foundation Gate 后再由规范推导，不先画页面再反推规则。

## Foundation Gate

### Gate A — Repository

**PASS at Draft Profile level.**

### Gate B — Human Interface

**NOT YET PASS.**

### Gate C — Open Collaboration

**PASS at Draft Profile level.**

因此整个 Foundation Gate 仍未通过；当前不恢复网站作为主 P0。

## Prior Art 是持续前置流程

仓库结构、AI 协作、网页设计与数据模型都属于互操作系统设计问题。

所有方向继续遵守：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**
