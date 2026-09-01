# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）。
>
> 当前阶段：**Foundation First（基础先行）**。
>
> 详细阶段定义：`foundation-first-phase-v0.1.zh-CN.md`。

## 当前总体判断

InteropAtlas 的主方向没有变化，但此前近期执行顺序有一处明显偏移：Human-readable Website / Object Page 的实现推进速度已经超过了底层规范、开放协作机制和仓库结构本身。

因此当前不再把网站重构作为第一 P0，而是先回答三个更基础的问题：

1. **项目自身怎样组织？** — Repository Structure / Artifact Taxonomy；
2. **面向人的信息怎样组织、呈现和交互？** — Human Interface Standards Package；
3. **人类与 AI / Agent 怎样共同建设？** — Open Collaboration / Human–AI Collaboration Profile。

同时继续并行补齐 Canonical Data 的 Curation / Evidence / Validator / Query correctness。

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

## 当前已有但尚未等于“基础完成”

### Human Interface

已有：
- ISO 9241 / WCAG / WAI-ARIA 等 Standards Baseline；
- Prior Art Reference Map；
- `IA-HI Specification v0.1` 综合草案；
- 第一次 requirement-based audit；
- GitHub Pages Reference Implementation。

但仍缺：
- Information Architecture Profile；
- Information Presentation Profile；
- Interaction Profile；
- Visual Presentation Profile；
- Accessibility / Conformance Profile；
- Method / Guideline / Heuristic / Design System 的合适 Atlas 对象模型。

因此：**网站只是 Reference Implementation，不是当前规范来源。**

### Open Collaboration / Human–AI

已有：
- ISO/IEC Human-Machine Teaming / NIST AI RMF Prior Art；
- Linux Foundation AAIF / AGENTS.md 调研；
- GitHub Coding Agents / Issue / PR / Review Prior Art；
- Open Collaboration V0 Working Notes。

但仍缺：
- participant roles；
- task lifecycle；
- claim / lease semantics；
- handoff / continuity；
- review / oversight / authorization；
- GitHub-native mapping；
- AGENTS.md 与 README / CONTRIBUTING 的边界。

因此：**不先做 Agent-only task system，也不先写 AGENTS.md。先形成 Profile。**

### Repository Structure

当前根目录同时放置 Canonical Data 对象目录、docs、schemas、engine、experiments 等；`docs/` 又混合 Specification、Methodology、Research、Plan、Audit、Roadmap 等多种产物身份；`.github/` 当前主要只有 workflows。

当前结构可以工作，但还没有经过“开放标准项目 + 多贡献者 + Agent-compatible”的结构审计。

因此：**不立即搬目录，先形成 Repository Structure & Artifact Taxonomy v0.1。**

## P0 — Foundation First

### P0-F1：Repository Structure & Artifact Taxonomy

相关：#21。

输出：
- 当前仓库结构审计；
- Root / docs / data / specs / methodology / research / experiments / governance / tools / tests 等职责比较；
- Artifact taxonomy 与 lifecycle；
- Community Health / CONTRIBUTING / Issue / PR / CODEOWNERS / AGENTS.md 的目标位置和职责；
- 是否把现有 `standards/`、`capabilities/` 等迁入 `data/` 的 Decision；
- Migration Plan。

Prior Art：GitHub Community Profile / Health Files、OpenSSF、REUSE、Diátaxis / docs-as-code、IETF / W3C / LF 开放规范项目等。

在该 Profile 出来前，不大规模移动仓库目录。

### P0-F2：Human Interface Standards Package

相关：#14、#15。

当前综合 `IA-HI v0.1` 作为输入，不作为“已经完成”。

需要形成至少五个可审计模块：
1. Information Architecture；
2. Information Presentation；
3. Interaction；
4. Visual Presentation；
5. Accessibility / Conformance。

每个模块必须有：
- 用户任务 / context；
- 上游标准 / Prior Art；
- Adopt / Profile / Extend / Invent 判断；
- BCP 14 Requirements；
- 验收 / conformance 方法。

#15 提升为 P0，因为大量设计方法 / Guideline / Design System 不能继续被模糊塞进 `standard` 或 `reference_project`。

### P0-F3：Open Collaboration / Human–AI Collaboration Profile

相关：#19。

需要明确：
- Contributor / Executor / Reviewer / Overseer / Maintainer / Automation roles；
- Available → Claimed → In Progress → Blocked / Handoff → Review → Done；
- “租赁式认领”的语义；
- GitHub Assignee / activity / stale 能表达多少；
- 什么时候才需要 Lease / Heartbeat；
- 执行者与 Reviewer / Approver 的分离；
- Human ↔ Agent / Agent ↔ Agent handoff；
- AGENTS.md 的职责和边界；
- GitHub Issue / PR / Review / CODEOWNERS / Rulesets 的映射。

Profile 出来后，才修改 CONTRIBUTING、创建 AGENTS.md、Issue / PR templates，并用真实任务试运行。

### P0-F4：Curation / Evidence / Machine Correctness

相关：#8、#7、#9、#10。

并行补：
- Curation / Contribution minimum workflow；
- Evidence / Provenance minimum model；
- JSON Schema validation；
- ID / reference / type correctness；
- 保持 `reference_issues = 0`；
- 修复 #7 query scope；
- regression tests。

这条线不依赖继续加网站 UI。

## P1 — Foundation Gate 后的参考实现

### #17 Object Page Shell

已经完成的 `<main>`、semantic Breadcrumb、Identity Before Exploration 等兼容性修正保留，不回滚。

但 #17 暂缓继续扩展，等待 Human Interface Standards Package 达到 Foundation Gate。

### #13 Browser E2E / Accessibility

仍然重要，但应在 Interaction / Accessibility / Conformance Profile 明确测试合同后再恢复为实现 P0。

### Website / Global Information Architecture

Foundation Gate 之后再根据正式 Information Architecture Profile 推导：
- 首页；
- Capability / Domain / Organization / Scenario 入口；
- Search；
- Resource Pages；
- Maps / Explore；
- Comparison / Explanation Views。

不是先画页面再反推规则。

### Visual System / Design Tokens

在信息架构、信息呈现和交互规则稳定后再实现：
- typography；
- spacing；
- semantic color；
- status / relation / evidence encoding；
- light / dark；
- DTCG-compatible Design Tokens。

## P2 — 分析与规模化

在 Foundation 与 Query correctness 稳定后逐步进入：
- Search / Dynamic Maps / path exploration；
- Comparator / Pathfinder；
- Coverage / Gap / Openness analysis；
- Atlas Linter / Atlas Health；
- Agent discoverability / external AI contribution (#18)；
- 多后端 / Federation / RDF / Neo4j 等。

## Foundation Gate

Reference Implementation 恢复为主 P0 前，至少满足：

### Gate A — Repository
- Repository Structure Profile v0.1；
- Artifact taxonomy / lifecycle；
- 目录迁移 Decision；
- Community Health / Collaboration 文件目标结构明确。

### Gate B — Human Interface
- IA / Information Presentation / Interaction / Visual / Accessibility-Conformance 五个 Draft Profile；
- 关键 Requirements 有依据和验收方式；
- 非标准 HCI Prior Art 可正确建模。

### Gate C — Open Collaboration
- Human–AI Collaboration Profile v0.1；
- roles / lifecycle / claim / review / handoff / authorization 明确；
- GitHub-native mapping 明确；
- AGENTS.md 职责边界明确。

Gate 不要求它们已经成为成熟 Standard，只要求**规范足够指导实现，而不是由实现临时决定规范。**

## 当前执行顺序

```text
#21 Repository Structure & Artifact Taxonomy
        ↓
#14 + #15 Human Interface Standards Package
        ↓
#19 Open Collaboration / Human–AI Profile
        ↘
         #8/#7/#9/#10 Machine / Curation / Trust 并行
        ↓
Foundation Gate Review
        ↓
#17 / #13 / Website Reference Implementation resumes
```

允许 F1 / F2 / F3 交叉研究，但当前**不继续新增网站功能，不大规模搬目录，不先实现 Agent-only 协作机制。**

## Prior Art 是持续前置流程

仓库结构、AI 协作、网页设计与数据模型都属于需要互操作的系统设计问题。

因此所有这些方向继续使用同一规则：

> **Reuse Before Invent**
>
> **Adopt → Profile → Extend → Invent**

不是只有 Atlas 收录外部标准时才遵守这条原则；InteropAtlas 自己的建设方式也必须遵守。
