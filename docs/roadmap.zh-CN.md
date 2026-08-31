# InteropAtlas 当前路线图

> 状态：Living Roadmap（持续更新路线图）。用于回答“现在最重要的事情是什么、为什么要做、哪些方向已经提出但尚未实现”。具体执行任务继续放在 GitHub Issues。

## 当前总体判断

InteropAtlas 已完成第一轮从“仓库里的结构化事实”到“人可以打开的网页”的闭环：

```text
YAML Facts
   ↓
Loader / Renderer
   ↓
Static HTML
   ↓
GitHub Pages
   ↓
人可以浏览
```

因此 **Visible（看得到）已经基本成立**。当前最明显的问题不再是“看不到”，而是：页面缺乏结构、对象解释不足、导航弱、关系不能可靠展开，机器基础层仍是 bootstrap 状态。

当前整体采用五路线协同模型：

1. Human Route（人类可读）；
2. Machine Route（机器可用 / 可维护）；
3. Curation / Contribution Route（收录与贡献）；
4. Evidence / Provenance / Trust Route（证据、溯源与可信）；
5. Governance / Standardization Route（治理与标准化）。

详见 `five-route-operating-model.zh-CN.md`。

## P0 — 当前最近的主闭环

近期不平均推进所有方向，而是先建立下面这一组互相驱动的能力：

```text
Human:
Readable + Navigable + Connected
                ↕
Machine:
Validator + Reference Resolver + Graph/Backlink Index
                ↕
Trust / Curation:
Minimum Evidence + Prior Art + 收录规则
```

### P0-A：Readable / Navigable / Connected

目标：让网站从“对象列表”逐步变成真正可理解、可导航的 Atlas。

当前已完成：
- Markdown / HTML Renderer；
- Capability / Standard / Implementation 三类对象页；
- GitHub Pages 自动部署；
- 自动/手动深色模式；
- 最小 Capability → Implementation backlink 实验。

下一步：
- 把单个对象页从字段转写升级为结构化知识页面；
- 首页和导航从对象类型列表升级为能力优先、多入口结构；
- 对象页显示可信的正向关系和反向关系；
- Renderer 不再自行临时承担长期 Graph / Resolver 职责。

相关：Issue #1、#2、#3、#8。

### P0-B：Engine 基础层

当前最需要补齐的机器基础：

1. Validator；
2. Reference Resolver；
3. Graph / Backlink Index。

原因：一旦 Human Route 进入 Connected（看关系），机器路线的 Graphable / Resolvable 就开始成为直接阻塞项。

相关：Issue #1、#8。

### P0-C：最小建设规范

在继续快速扩充对象前，先遵守一组轻量规则，而不是建设重型治理体系：

- Reuse Before Invent；
- Evidence Before Assertion；
- Fact 与 Assessment 分离；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Practice-driven Feedback；
- 新方法先标 Note / Methodology / Specification，不轻易称 Standard。

详见 `project-development-principles.zh-CN.md`。

## P1 — 第一轮闭环稳定后

### Curation / Contribution Route

建立最小、可重复执行的收录流程：

```text
候选发现 → Prior Art / 来源调查 → 对象识别 → 建模 → Evidence → Relations → Validate → Review → Merge → 更新监控
```

需要逐步明确：收录门槛、最小 Evidence、重复对象、版本更新、贡献者如何操作。

### Evidence / Provenance / Trust Route

从简单 `sources:` 字段逐步发展到可追踪的 Claim / Evidence / Source / Context / Time / Review 模型。

优先从真实痛点扩展，不一次性设计完整 provenance ontology。

### Queryable / Analysis 前置修复

在开始依赖 Engine 做比较、路径、Open Gap、Coverage 之前：
- 修复 Issue #7 的 `alternative_to` 查询作用域；
- 建立可信基础查询 API；
- 增加最小回归测试。

### 统一解释层与标准族指南

对象页负责 Reference；方案空间、标准族、历史演化和“为什么”逐步形成 Explanation / Guide，而不是无限扩张详情页。

相关：Issue #3、#4。

## P2 — 中期能力

### Mappable / Explorable

- Dynamic Maps；
- 搜索；
- 多维过滤；
- 子图探索；
- 基础图形化关系视图；
- 路径视图。

### Analyzable

- Pathfinder；
- Coverage Analyzer；
- Gap Analyzer；
- Comparator；
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
- human-readable coverage；
- relation coverage。

逐步形成 Atlas Linter 和 Atlas Health。

## P3 — 长期技术与生态方向

### 多后端 / Federation

- JSON / JSON-LD / RDF / CSV / Graph export；
- API / Agent interface；
- Property Graph / RDF backend；
- Neo4j / SPARQL 等可选运行时；
- Map of Maps / federated catalogs；
- graph-native, database-agnostic。

相关：Issue #6。

### IA 自产规范与标准化

项目建设过程中可能产生 Methodology、Specification、Profile、Skill，未来才可能出现正式 Standard。

当前只研究：
- stable ID；
- version / date / URL 分离；
- lifecycle；
- repo boundary；
- conformance test；
- governance；
- 如何重新被主 Atlas 作为普通标准收录。

不在当前阶段规定“每个标准一个仓库”或固定 `IA-YYYYMMDD-XXX` 编号。

详见 `project-generated-methods-standards.zh-CN.md`。

## Prior Art 是持续流程，不是一次调研

以后每进入一个新能力点，都优先参考已有成熟项目，而不是一次性把所有标准组织研究完。

当前参考池见 `prior-art-and-method-reference.zh-CN.md`，包括：
- Wikidata；
- OpenStreetMap；
- FAIR；
- W3C DCAT；
- W3C SHACL；
- Diátaxis；
- IETF；
- W3C Process；
- Software Heritage / SWHID。

## 当前建议执行顺序

### 立即

1. 用当前 GitHub Pages 继续验证真实阅读体验；
2. 补 Validator + Resolver + Graph/Backlink 的最小可信基础；
3. 同时改善 Readable + Navigable + Connected；
4. 每次增加新数据 / 新机制前遵循最小 Prior Art 与 Evidence 规则。

### 紧随其后

5. 把收录流程和 Evidence 模型从隐性做法变成可重复流程；
6. 修复关系查询作用域并建立基础 Query API；
7. 在真实对象族上试做 Explanation / Comparison / Map。

### 暂不急做

8. 重型标准治理组织；
9. 每个自产标准独立仓库；
10. 固定 IA 标准编号体系；
11. 提前绑定 Neo4j / RDF Store；
12. 一次性设计完整网站和完整 ontology。

## 待办管理方式

- `docs/roadmap.zh-CN.md`：总体优先级与阶段；
- GitHub Issues：可执行任务、验收条件、阻塞关系；
- YAML / Schemas / Relations：事实与模型；
- Engine：确定性解析、查询与分析；
- Renderer / Site：人类可读 Projection；
- Methodology docs：项目建设方法和暂定规范。

原则：**先建立最小闭环，再让真实使用决定下一轮结构扩展。**
