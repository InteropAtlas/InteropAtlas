# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）。用于回答“现在最重要的事情是什么、为什么要做、哪些方向已经提出但尚未实现”。具体执行任务继续放在 GitHub Issues。
>
> 最近路线对齐审计：`route-alignment-audit-2026-09-01.zh-CN.md`。

## 当前总体判断

InteropAtlas **不需要项目级转向**。核心目标、三层架构和五路线模型仍然成立，但项目实际阶段已经比旧 Roadmap 更靠前。

仍然成立的核心原则：

- Interoperability（互操作性）是问题边界；
- Facts → Rules / Engine → Assessments；
- Reuse Before Invent；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Human ↔ Machine Co-development；
- Practice-driven Feedback；
- graph-native, database-agnostic。

当前整体仍采用五路线协同模型：

1. Human Route（人类可读）；
2. Machine Route（机器可用 / 可维护）；
3. Curation / Contribution Route（收录与贡献）；
4. Evidence / Provenance / Trust Route（证据、溯源与可信）；
5. Governance / Standardization Route（治理与标准化）。

Open Collaboration（开放协作）当前是横向 operating layer，补强“谁做、如何接手、如何 Review / Oversight”，**不是第六条主路线**。

## 当前已经跨过的阶段

### Human Route

已经不再只是：

`YAML → Renderer → HTML → Pages`

而是开始形成：

```text
External Standards / Prior Art
        ↓
Human Interface Baseline
        ↓
IA-HI Specification v0.1
        ↓
Requirement-based Audit
        ↓
Vertical Slice
        ↓
Browser / Accessibility Acceptance
```

当前已有：
- GitHub Pages 静态站点；
- Capability / Standard / Implementation 资源页；
- Graph-driven relations / backlinks；
- Human Interface Standards Baseline；
- Human Interface Specification v0.1；
- 第一次 68-Requirement Conformance Audit；
- Object Page Shell v0.1 实施计划。

### Machine Route

Reference Resolver / Graphable 已经形成可用最小版本。

已验证的阶段性 Graph health（`d8e62cc`）：
- 90 objects；
- 82 explicit relations；
- 126 resolved edges；
- `reference_issues: []`。

因此 Machine 当前最重要的问题已经从“有没有 Graph”转成：
- Validator 是否足够正式和可信；
- Schema / type correctness 是否进入 CI；
- Query 是否有正确作用域；
- 回归测试能否阻止错误结果重新出现。

已知 #7 `alternative_to` query scope bug 仍未解决，在依赖 Query 做 Comparator / Pathfinder / Open Gap / Coverage 前必须修复。

## P0 — 当前主闭环

### P0-H1：Object Page Shell v0.1

相关：#17、#16、#14。

目标不是“换一套视觉皮肤”，而是先稳定一个 Canonical Object 如何成为人类知识页面。

第一轮只做：
- `<main>` semantic page shell；
- semantic Breadcrumb + `aria-current`；
- H1 / Summary / Core Context 在 Explore 之前；
- Local Map 降为关系探索辅助区；
- 关系摘要、Local Map、详细边列表明确职责并减少重复；
- Human View 不把 `implementation`、`exchange`、`validate` 等机器枚举作为主要用户标签；
- 保持 Link / Button 原生语义与 Progressive Enhancement。

明确不在这一轮做：
- 完整首页重构；
- 品牌视觉；
- React / Vue；
- Cytoscape / Sigma / D3；
- 完整 Search；
- 全图 Explore；
- 冻结 typography / spacing / color 数值。

### P0-H2：真实 Browser / Accessibility Acceptance

相关：#13。

原则：

> `build success != interaction acceptance success`

需要建立最小真实浏览器 E2E，至少覆盖：
- 对象 Link 真正导航；
- `以此为地图中心` 只改变 Local Map；
- Filter 行为与状态；
- Keyboard；
- JS disabled fallback；
- 深色模式；
- 后续 URL / History state。

Accessibility 自动检查逐步与 WCAG / ACT-style rules 对接；静态源码检查不能冒充完整无障碍验收。

### P0-M1：Validator / Machine correctness

相关：#8。

Graph / Backlink 已有最小实现，#8 的重点应继续收敛到：
- JSON Schema validation；
- required fields；
- ID uniqueness；
- object / reference type consistency；
- Error / Warning / Notice / Unknown 等结构化 Validation Report；
- regression tests；
- 保持 `reference_issues = 0` 作为 CI invariant。

### P0-M2：修复 Query correctness

相关：#7。

`alternative_to` 查询目前仍会混入当前 Capability 作用域之外的关系。

在任何 Analysis 能力依赖 Engine Query 前：
1. 修复 capability / implementation scope；
2. 正确返回 `forgejo_actions → alternative_to → github_actions`；
3. 不混入 URL / URI、SemVer / CalVer 等无关关系；
4. 增加最小 regression test。

### P0-G：轻量 Specification Loop

Governance / Standardization 不再只是抽象原则，但仍不建设重型标准组织。

当前允许并鼓励：

```text
Prior Art
  ↓
Draft / Provisional Specification
  ↓
BCP 14 Requirement IDs
  ↓
Conformance Audit
  ↓
Implementation Slice
  ↓
Practice Feedback / Revision
```

`IA-HI v0.1` 继续保持 Draft / Provisional Specification，不升级为正式 Standard。

## P1 — P0 第一轮稳定后

### Global Information Architecture

Human Interface 的下一阶段不是先做视觉，而是从真实用户任务建立全局信息架构。

至少围绕：
- Identify；
- Find；
- Understand；
- Relate；
- Compare；
- Verify；
- Explore。

再反推：
- 首页入口；
- Capability / Domain / Organization / Scenario；
- Search；
- Maps / Explore；
- Standard / Implementation indexes。

Breadcrumb、侧栏和分类只是 View，不代表底层唯一知识树。

### Curation / Contribution Route

相关：#9。

建立最小可重复流程：

```text
候选发现 → Prior Art → 对象识别 → 建模 → Evidence → Relations → Validate → Review → Merge → Monitor
```

优先明确：收录门槛、Source / Evidence、去重、版本更新、Relation 新增条件、Agent / Human Review 边界。

### Evidence / Provenance / Trust Route

相关：#10。

从简单 `sources:` 逐步走向：

`Fact / Claim → Evidence → Source → version / retrieved_at / context → review`

优先从真实事实类型扩展，不一次性设计完整 provenance ontology。

### Non-standard Reference Object Model

相关：#15。

Human Interface Prior Art 已证明：Method、Guideline、Heuristic、Framework、Design System、Research Result 不能全部塞进 `standard`。

用少量真实对象反推最小模型，不为了 taxonomy 完整性提前制造复杂 ontology。

### Open Collaboration V0

相关：#19。

Open Collaboration 当前横向服务 Curation / Governance，不新建 Agent-only 仓库结构。

V0 先复用 GitHub：
- Issues；
- Assignee；
- Projects / Fields；
- Sub-issues / Dependencies；
- Pull Request / Review；
- CODEOWNERS / Required Review；
- activity / stale。

用 2–3 个真实 Issue 验证：
- 人或 Agent 如何找到任务；
- 如何避免重复执行；
- 执行与 Review 如何分离；
- GitHub 原生机制哪里确实不足。

在真实缺口出现前，不建设独立 Lease / Heartbeat / Scheduler。

### Explanation / Comparison

相关：#3、#4。

对象页继续偏 Reference；标准族、方案空间、历史演化、为什么、如何比较逐步形成 Explanation / Guide / Comparison View。

### Visual Profile / Design Tokens

在 Object Page Shell 与 Global IA 稳定后再进入：
- typography；
- spacing；
- semantic color；
- focus / state；
- relation visual coding；
- light / dark equivalence；
- DTCG-compatible design tokens。

## P2 — 中期能力

### Mappable / Explorable

- Dynamic Maps；
- Search；
- 多维过滤；
- 子图探索；
- 路径视图；
- 可分享 / 可恢复的 Explore state。

复杂图渲染必须先做 Prior Art Check；成熟库能解决时不自己重复实现布局、pan / zoom、hit testing、WebGL 渲染等基础设施。

### Analyzable

在 Query correctness 可信后逐步进入：
- Pathfinder；
- Comparator；
- Coverage Analyzer；
- Gap Analyzer；
- Dependency Audit；
- Openness Analyzer；
- Constraint Evaluator。

### Atlas Health / Maintainability

- broken references；
- orphan objects；
- stale sources / versions；
- missing evidence；
- duplicate candidates；
- relation conflicts；
- schema drift；
- human-readable coverage；
- relation coverage。

逐步形成 Atlas Linter / Atlas Health。

### Agent Discoverability / External AI Contribution

相关：#18。

研究 AGENTS.md、开放 metadata、机器可发现贡献入口等，但不把外部 Agent 当成未经授权的计算资源，也不绑定单一 Agent 产品。

## P3 — 长期技术与生态方向

### 多后端 / Federation

相关：#6。

- JSON / JSON-LD / RDF / CSV / Graph export；
- API / Agent interface；
- Property Graph / RDF backend；
- Neo4j / SPARQL 等可选运行时；
- Map of Maps / federated catalogs；
- graph-native, database-agnostic。

### IA 自产正式标准治理

相关：#11。

继续研究 stable ID、version / date / URL 分离、lifecycle、repo boundary、conformance tests 和 governance。

当前仍不：
- 规定“一个标准一个仓库”；
- 冻结 IA 标准编号体系；
- 建设重型委员会；
- 把 Draft Specification 自动升级成 Standard。

## Prior Art 是持续流程

Prior Art 不是一次性研究阶段，而是每个新能力点的前置流程。

当前来源已从早期 Wikidata / OSM / FAIR / W3C / IETF 扩展到：
- ISO 9241 Human-system Interaction；
- WCAG / WAI-ARIA / APG；
- ACT；
- Apple HIG / Material / USWDS / GOV.UK；
- Human-Machine Teaming；
- NIST AI RMF；
- Linux Foundation AAIF / AGENTS.md；
- GitHub 原生协作机制。

采用顺序继续是：

> **Adopt → Profile → Extend → Invent**

## 当前执行顺序

### Human lane

1. **#17 Object Page Shell v0.1**；
2. **#13 Browser E2E + Accessibility acceptance**；
3. 按 #16 重新审计第一轮实现；
4. Global Information Architecture；
5. Visual Profile / Design Tokens。

### Machine lane（并行）

1. 保持 Graph / Resolver clean；
2. 补正式 Validator / schema correctness；
3. 修复 #7 query scope + regression test；
4. 建立可信 Query API；
5. 再进入 Analysis。

### Collaboration lane（P1，不抢占 P0）

1. #19 使用 GitHub-native workflow；
2. 用 2–3 个真实 Issue 实践；
3. 记录缺口；
4. 只有真实缺口存在时才研究 IA-specific Lease / Scheduler。

## 待办管理方式

- `docs/roadmap.zh-CN.md`：总体阶段、优先级和主路线；
- GitHub Issues：可执行任务与验收条件；
- Sub-issues / Dependencies / Projects：任务图与协作状态；
- YAML / Schemas / Relations：事实与模型；
- Engine：确定性验证、解析、查询与分析；
- Renderer / Site：Human-readable Projection；
- Methodology / Specification docs：方法、要求和符合性基线。

原则：

> **不转向，更新阶段定义；不扩大战线，收紧当前 P0。**
