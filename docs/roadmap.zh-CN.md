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

Visible（看得到）已经基本成立。Human Interface Prior Art、IA-HI v0.1 和第一次符合性审计也已经把“凭感觉继续堆页面”推进到了“按规范做小 vertical slice”的阶段。

当前整体继续采用五路线协同模型：

1. Human Route（人类可读）；
2. Machine Route（机器可用 / 可维护）；
3. Curation / Contribution Route（收录与贡献）；
4. Evidence / Provenance / Trust Route（证据、溯源与可信）；
5. Governance / Standardization Route（治理与标准化）。

开放协作不是新的 Atlas 数据路线，而是横跨 Curation / Contribution 与 Governance 的参与机制：人类贡献者和 AI / Agent 都可以成为协作参与者，自动化基础设施只负责 CI、测试、部署、调度等执行能力。

详见 `five-route-operating-model.zh-CN.md`、`open-collaboration-route-v0-notes.zh-CN.md`。

## P0 — 当前最近的主闭环

当前不平均推进所有方向，而是先跑通这一组互相驱动的能力：

```text
Human:
Object Page Shell + Browser Acceptance + Connected View
                ↕
Machine:
Validator + Reference Resolver + Graph/Backlink Index
                ↕
Standards / Trust:
IA-HI Requirements + Minimum Evidence + Prior Art
```

### P0-A：按 IA-HI v0.1 做第一个真实 Vertical Slice

Human Interface 标准基线、IA-HI v0.1 和第一次 Conformance Audit 已经形成。当前第一优先不是重写整站，而是完成 Issue #17 的 Object Page Shell v0.1：

- Capability / Standard / Implementation 三类对象页共用稳定的信息职责；
- 先修 Web 语义、信息层级和重复关系展示；
- Local Map 回到关系探索辅助角色；
- 不在这一轮冻结完整视觉系统或引入大型前端框架。

随后立刻用 Issue #13 的真实浏览器 E2E 验证代表页，避免再次出现“build success = interaction success”的误判。

相关：#13、#14、#16、#17。

### P0-B：Engine 基础层并行补齐

当前机器基础继续由 Issue #8 推进：

1. Validator；
2. Reference Resolver；
3. Graph / Backlink Index。

Human Route 越依赖真实关系、backlink 和 Connected View，这一层越成为直接基础。Renderer 不应长期自己扫描并重新计算第二套关系事实。

相关：#1、#2、#8、#12。

### P0-C：最小建设规范继续作为护栏

继续遵守：

- Reuse Before Invent；
- Evidence Before Assertion；
- Fact 与 Assessment 分离；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Practice-driven Feedback；
- 新方法先标 Note / Methodology / Specification，不轻易称 Standard。

Human Interface 设计同样遵守 `Adopt → Profile → Extend → Invent`，不再无依据地堆交互和视觉规则。

详见 `project-development-principles.zh-CN.md`。

## P1 — 第一轮 P0 闭环稳定后

### Curation / Contribution + Evidence

Issue #9 与 #10 应尽量使用同一批真实对象共同验证，而不是分别做纯理论设计：

```text
候选发现 → Prior Art → 对象识别 → 建模 → Evidence → Relations → Validate → Review → Merge
```

同时通过真实 HCI / Design Prior Art 样本推进 #15 的非标准参考对象模型，避免把 Method / Guideline / Framework 错误塞进 Standard。

### Open Collaboration V0

推进 Issue #19，但先复用 GitHub 原生协作机制，不建设 Agent 专用任务系统：

```text
Issue / Ready
   ↓
一个主要执行者接手
   ↓
Work / PR
   ↓
独立 Review
   ↓
Done
```

第一阶段重点是让 `CONTRIBUTING.md` 能回答“去哪里找任务、如何接手、如何提交和 Review”，并用 2–3 个真实 Issue 验证人类与 Agent 是否可以共用同一流程。只有实践证明不够时，再研究 Lease / Heartbeat / Scheduler。

### Queryable / Explanation 前置

- 修复 #7 `alternative_to` 查询作用域并增加回归测试；
- 逐步推进 #3 标准解释层和 #4 同类比较；
- 先在一个真实标准族上验证，不一次性扩展整个 Atlas。

## P2 — 中期能力与生态

### Mappable / Explorable / Analyzable

- Dynamic Maps、搜索、多维过滤、子图探索、路径视图；
- Pathfinder、Coverage / Gap Analyzer、Comparator、Dependency Audit 等；
- broken references、orphan objects、stale sources、missing evidence 等逐步形成 Atlas Health。

### Agent 可发现性与外部贡献入口

Issue #18 记录一个重要的前中期生态方向：让外部 AI / Agent 在执行标准检索和相关任务时有机会发现 InteropAtlas，并知道 IA 是开放、可提交 Issue / Evidence / 建议 / PR 的项目。

当前只记录能力目标，不立即建设“利用外部闲置算力”的系统。后续优先研究开放的机器可发现格式、AGENTS.md、贡献入口、身份与授权、质量控制，再决定 IA 是否需要自己的 Profile。

### 自产规范 / 多后端研究

- #6：Graph backend / RDF / Neo4j 等继续保持 database-agnostic；
- #11：自产 Methodology / Specification / Standard 的标识、版本、生命周期与仓库边界；
- 暂不建设重型标准组织。

## Prior Art 是持续流程

每进入一个新能力点都先调查成熟方案，不为“研究完整”提前研究所有标准。

当前参考池除了 Wikidata、OpenStreetMap、FAIR、W3C DCAT / SHACL、IETF、W3C Process 等，也已加入：

- ISO/IEC Human-Machine Teaming 系列；
- ISO/IEC 5339 / NIST AI RMF；
- Linux Foundation AAIF / AGENTS.md；
- GitHub Coding Agents / 开源协作实践。

详见 `prior-art-and-method-reference.zh-CN.md` 和 `human-ai-open-collaboration-prior-art.zh-CN.md`。

## 当前建议执行顺序

### 立即

1. 完成 #17 Object Page Shell v0.1；
2. 用 #13 给这一 vertical slice 加真实浏览器验收；
3. #8 并行补齐 Validator + Resolver + Graph/Backlink 最小可信基础；
4. 根据 #14 / #16 已形成的规范与审计，只选择下一小块 Human Route 继续改进。

### 紧随其后

5. 用真实对象共同推进 #9 Curation、#10 Evidence 和 #15 非标准参考对象模型；
6. 用 2–3 个真实 Issue 实验 #19 Open Collaboration V0，并补充 CONTRIBUTING；
7. 修复 #7，再在一个真实标准族上试做 #3 / #4 Explanation / Comparison。

### 先记录、不抢当前主线

8. #18 Agent 可发现性与外部 AI 贡献入口；
9. #6 多后端 / 图数据库；
10. #11 自产规范完整生命周期；
11. 重型标准治理、固定 IA 标准编号、每标准一仓库；
12. 一次性设计完整网站、完整 ontology 或完整 Agent 自治系统。

## 待办管理方式

- `docs/roadmap.zh-CN.md`：总体优先级与阶段；
- GitHub Issues：统一的可执行任务池，面向人类与未来 Agent；
- GitHub Projects / Issue Fields：逐步承载 Status / Priority / Area 等协作状态；
- YAML / Schemas / Relations：事实与模型；
- Engine：确定性解析、查询与分析；
- Renderer / Site：人类可读 Projection；
- Methodology / Prior Art docs：项目建设方法、依据和暂定规范。

原则：**先建立最小闭环，再让真实使用决定下一轮结构扩展。**
