# InteropAtlas 路线对齐审计 — 2026-09-01

> 状态：Point-in-time Alignment Audit（阶段性路线对齐审计）
>
> 目的：把近期多会话讨论、仓库实际演化、当前 Issues 与既有 Roadmap 对齐，判断主方向是否需要转向，并给出新的近期执行顺序。

## 1. 结论

**主方向没有走偏，不需要项目级 Pivot（转向）；需要更新的是“当前阶段判断”和优先级。**

仍然成立的核心骨架：

- Interoperability（互操作性）继续作为问题边界；
- Facts → Engine / Rules → Assessments 的基本分层继续成立；
- Structured Source, Linked View；
- Flat Objects + Rich Relations + Dynamic Maps；
- Human ↔ Machine Co-development；
- Reuse Before Invent；
- Evidence Before Assertion；
- Practice-driven Feedback；
- graph-native, database-agnostic。

真正发生的变化不是目标改变，而是项目已经从“验证概念可行”进入了“给各路线建立可审计契约和小型闭环”的阶段。

## 2. 旧 Roadmap 为什么已经落后

旧 Roadmap 仍把近期 Human Route 概括为：

```text
Readable + Navigable + Connected
```

并把 Machine Route 的主要阻塞描述为：

```text
Validator + Reference Resolver + Graph / Backlink Index
```

这两个描述方向上仍对，但粒度已经落后于实际仓库。

### Human Route 已经前进了一层

当前实际链条已经形成：

```text
外部 Standards / Prior Art
        ↓
IA Human Interface Standards Baseline
        ↓
IA-HI Specification v0.1
        ↓
Requirement-based Conformance Audit
        ↓
Vertical Slice
        ↓
Browser / Accessibility Acceptance
        ↓
下一轮 Information Architecture / Visual Profile
```

这比“继续改善网页”更成熟：网页现在是 Specification 的 Reference Implementation / Test Bed，而不是设计决策的起点。

第一次 IA-HI v0.1 审计已经检查 68 个 Requirement，并明确指出当前主要问题集中在 Information Architecture、Object Page 信息职责、重复关系呈现、Web 语义、真实浏览器验收和 Visual System。

因此 Human Route 当前最合理的 P0 已经不是继续增加 Local Map 功能，而是 **Object Page Shell v0.1**。

## 3. Human Route 当前判断

### 已经建立

- Human-readable 静态站点与 GitHub Pages；
- Capability / Standard / Implementation 资源页；
- Graph-driven relations / backlinks；
- Human Interface 外部标准基线；
- `IA-HI Specification v0.1`；
- 第一次 Requirement-based Conformance Audit；
- Object Page Shell v0.1 vertical slice 计划；
- Link / Button 等基础 Web 语义纠正。

### 当前真正的 P0

1. **#17 Object Page Shell v0.1**
   - 先稳定对象页的信息职责与 HTML 语义；
   - Identity / Summary / Core Context 在 Explore 之前；
   - `<main>`、semantic Breadcrumb、`aria-current`；
   - 消除 Local Map / 一跳邻居 / 直接关系的无职责重复；
   - Human View 不泄漏内部机器枚举。

2. **#13 Browser E2E + Accessibility acceptance**
   - `build success != interaction acceptance success`；
   - 真实验证 Link、Button、Filter、Recenter、Keyboard、JS-disabled fallback；
   - 后续逐步形成可持续 conformance gate。

3. **全局 Information Architecture**
   - 在 Object Page Shell 稳定后再重构首页 / 全局入口；
   - 从 Identify / Find / Understand / Relate / Compare / Verify / Explore 等用户任务推导入口；
   - 不把 Capability category 或对象类型目录伪装成唯一知识树。

4. **Visual Profile / Design Tokens**
   - 排在信息职责与全局 IA 之后；
   - 不先冻结颜色、字号、间距和框架；
   - 后续优先兼容 DTCG-compatible semantic tokens。

## 4. Machine Route 当前判断

Machine Route 比旧 Roadmap 描述得更靠前。

最新已验证阶段（`d8e62cc` 附近）：

- 90 objects；
- 82 explicit relations；
- 126 resolved edges；
- `reference_issues: []`。

此前 3 个指向 `interopatlas` 的 unresolved relation source 已通过把 InteropAtlas 自身建模为 `reference_project` 解决。

因此：

- **Resolvable：已形成可用最小版本；**
- **Graphable：已形成可用最小版本；**
- Graph / Backlink Index 已经实际服务 Renderer；
- CI 已经能报告 Graph health。

但 Machine Route 仍不能被描述成“基础层完成”：

### 仍需优先补齐

1. **正式 Validator / Schema validation**
   - 当前 bootstrap 能加载和做部分 diagnostics，但还不是完整结构化 Validation Report；
   - 需要逐步覆盖 schema、type consistency、Evidence requirements、severity。

2. **#7 Query correctness**
   - `alternative_to` 查询仍存在跨 capability 作用域污染；
   - 当前 deterministic query 仍可能返回 URL ↔ URI、SemVer ↔ CalVer 等与目标 Capability 无关的关系；
   - 在 Comparator / Pathfinder / Open Gap / Coverage 依赖 Query 之前必须修复并加入 regression test。

3. **Queryable contract**
   - Graph 可连通不等于 Query 可依赖；
   - 下一阶段 Machine 重点应从“把图建出来”转为“让查询结果可信且可回归测试”。

## 5. Governance / Standardization Route 的阶段变化

旧 Roadmap 说 Governance 当前只做最小护栏，这个判断需要细化。

当前并没有建设重型标准组织，但已经通过真实 Human Interface 问题跑出了一条轻量规范循环：

```text
Prior Art
  ↓
Provisional Specification
  ↓
BCP 14 Requirement IDs
  ↓
Conformance Audit
  ↓
Implementation Slice
  ↓
Feedback / Revision
```

这正符合项目自己的 Standardization Ladder，而不是过早标准化。

因此当前应描述为：

> **Lightweight Specification Loop 已激活；Heavy Governance 仍暂缓。**

`IA-HI v0.1` 仍是 Draft / Provisional Specification，不升级成正式 Standard。

## 6. Open Collaboration 是否应该成为第六条路线？

**当前不应该。**

近期人类 + Agent 协作讨论很重要，但问题本质已经从“Agent 工程”重新定义为“开放协作”：

```text
InteropAtlas 开放项目
   ├── Human contributors
   └── AI / Agent contributors

Automation infrastructure
   └── CI / Renderer / Test / Deployment / Scheduling
```

当前 Open Collaboration 更适合被视为 **cross-cutting operating layer（横向协作运行层）**：

- 重点补强 Curation / Contribution 的“谁来贡献、如何接手”；
- 重点补强 Governance 的“谁 Review、谁监督、谁授权”；
- Human / Agent 尽量使用相同公开的 Issue / PR / Review 语义。

V0 优先采用 GitHub 原生机制：

- Issue；
- Assignee；
- Projects / Fields；
- Sub-issues / Dependencies；
- PR / Review；
- CODEOWNERS / Required Review；
- activity / stale。

暂不创造独立 Lease / Heartbeat / Agent-only Goal / Task 系统。

只有真实多人 / 多 Agent 实践证明 GitHub 原生机制不足后，再考虑 IA 自有协调能力。

相关：#19；Agent 可发现性 / 外部贡献入口保持 #18 P2。

## 7. 五路线模型是否仍有效？

**有效，暂不增加第六条。**

更准确的当前图应该是：

```text
                         Sources
                            ↓
                   Curation / Contribution
                            ↓
                   Evidence / Provenance
                            ↓
                     Canonical Facts
                            ↓
             Validator / Resolver / Graph
                            ↓
                         Engine
                    ↙              ↘
              Human Route      Machine Route

              Governance / Standardization
              约束方法、规范和演进

              Open Collaboration
              横向作用于“谁做 / 如何接手 / 如何 Review / 如何授权”
```

Open Collaboration 是 operating concern，不与五条 knowledge-system routes 竞争。

## 8. 调整后的优先级

### P0 — 当前主闭环

**Human**
1. #17 Object Page Shell v0.1；
2. #13 Browser E2E / Accessibility acceptance；
3. #16 按 IA-HI v0.1 持续审计和小步重构；
4. #14 Human Interface Specification / Profile 只随实践修订，不继续无限调研。

**Machine**
5. #8 从“建立 Graph”转向“补齐 Validator / regression / type correctness”；
6. #7 修复 query scope，作为所有分析器的可信前置；
7. 保持 `reference_issues = 0` 作为 CI health invariant。

### P1 — 第一轮 P0 稳定后

8. 全局 Information Architecture / 多入口导航；
9. #9 Curation / Contribution 最小收录流程；
10. #10 Evidence / Provenance / Trust 最小模型；
11. #15 Method / Guideline / Design System 等非标准参考对象模型；
12. #19 Open Collaboration V0：用 2–3 个真实 Issue 验证 GitHub 原生协作；
13. #3 / #4 Explanation / Standard Family / Comparison；
14. Visual Profile + DTCG-compatible Design Tokens。

### P2

15. Dynamic Maps / Search / 多维过滤 / 路径探索；
16. Comparator / Pathfinder / Coverage / Gap / Openness 等 Analysis；
17. Atlas Linter / Atlas Health；
18. #18 Agent 可发现性与外部 AI 贡献入口。

### P3

19. Federation / 多后端；
20. Neo4j / RDF / SPARQL 等可选运行时；
21. 正式 IA 自产标准治理、独立仓库、编号体系（仅在真实需求成熟后）。

## 9. 当前执行顺序

```text
Route alignment / Roadmap sync
        ↓
#17 Object Page Shell v0.1
        ↓
#13 Browser E2E + Accessibility gate
        ↓
Global Information Architecture
        ↓
Visual Profile / Tokens
```

Machine lane 与其并行：

```text
Keep Graph clean
        ↓
Validator / schema correctness
        ↓
Fix #7 query scope + regression tests
        ↓
Reliable Query API
        ↓
Analysis
```

Collaboration lane 暂不抢占 P0：

```text
#19 GitHub-native Open Collaboration V0
        ↓
真实 2–3 个任务实践
        ↓
记录缺口
        ↓
只有确有缺口才考虑 Lease / Scheduler / Agent-specific coordination
```

## 10. 最终判断

当前路线的主要问题不是“方向错误”，而是 **Roadmap 没有及时反映项目已经通过实践获得的新层次**。

最重要的调整是：

1. Human Route 从“直接做网页”升级为“标准 → Specification → Audit → Vertical Slice → Acceptance”；
2. Machine Route 从“先有 Graph”推进到“可信 Validator + Query correctness”；
3. Governance 从“只有原则”升级为“轻量 Specification Loop”，但不进入重型治理；
4. Open Collaboration 作为横向 operating layer，保持 Human-first / agent-compatible，不制造 Agent-only 仓库结构；
5. 继续用真实项目自身作为标准地图的实践测试场。

因此：**不转向，更新阶段定义；不扩大战线，收紧当前 P0。**
