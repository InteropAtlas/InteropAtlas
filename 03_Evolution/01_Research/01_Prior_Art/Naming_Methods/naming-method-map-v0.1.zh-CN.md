# Naming Method Map v0.1

> 状态：Research synthesis / orchestration baseline
> 
> 来源：Issue #407 的 prior-art / deep-dive 研究、Issue #408 的方法地图目标，以及 #409–#410 的 Agent / benchmark 实践证据。

## 1. 这份文档解决什么问题

这是一层总文档。它不教某个 Agent 具体生成名字，也不替任何一种方法补写未公开的内部流程。它只回答四个问题：

1. 当前有哪些命名路线；
2. 每条路线公开可确认的主要阶段是什么；
3. 哪些阶段是串行、并行或循环；
4. 后续应该把哪些阶段拆成独立 Worker / 对话上下文。

第二层为每条路线建立 Method Profile；第三层按真实步骤建立 Worker Task Packet。三层当前均已建立，正式执行前仍需通过 Integration Audit / dry run 验证真实交接。

## 2. 路线分类

### A. 外部专业机构方法

| Benchmark Arm | 方法来源 | 可确认的核心机制 | 当前流程形态 |
|---|---|---|---|
| G1 | Lexicon Branding / David Placek | Diamond / Creative Framework；Creative Teams 与 Linguistic Engineering；Identify → Invent → Implement | **并行 + 漏斗** |
| G2 | Catchword | Discovery；Naming Parameters / Creative Brief；Project Vocabulary；high-volume divergent generation；shortlist；screening | **高容量发散 → 收敛** |
| G3 | Igor | Positioning；Competitive Analysis / naming taxonomy；Name Development；Trademark / prescreen；contextual presentation | **竞争空间前置** |
| G4 | River + Wolf | Research / Prepare；4Cs：Character / Communication / Construction / Continuum；Develop；Shortlist；Screen | **参数化 + 迭代** |
| G5 | Siegel+Gale | Simplicity；descriptive / suggestive / coined / edgy 等类别探索；contextual evaluation；警惕 voting / consensus | **多类别并行 + 延迟评价** |
| G6 | Tungsten Branding | Pivot Point；evergreen umbrella concept；Brand Architecture / naming family extensibility | **长期母品牌 / 架构驱动** |
| G7 | NameStormers | Discover / Strategy；Brainstorm / Lightning Round；Screen；Pitch；Fine Tune；Test；Final | **多轮反馈 / 迭代** |

### B. IA 内部实验路线

| Benchmark Arm | 来源 | 核心机制 | 注意事项 |
|---|---|---|---|
| G0 | IA Internal Baseline | Organization philosophy → semantic space → Familiar-but-New / pronounceability / symbolic compressibility → generation | **不是外部机构方法**；用于 baseline |
| G8 | IA C1.0 Agent-native synthesis | region-first → collision prior → generate → observe/search → update region → repeat | **搜索反馈属于生成机制本身**；反馈先进入 arm-local state / Region Strategy，再以冻结 Region Brief 进入新的 Generator，不能把 Observation / survivor 结果直接喂给 Generator |

## 3. 工作图

```text
Orchestrator
  │
  ├─ G0  IA Baseline
  ├─ G1  Lexicon
  ├─ G2  Catchword
  ├─ G3  Igor
  ├─ G4  River + Wolf
  ├─ G5  Siegel+Gale
  ├─ G6  Tungsten
  ├─ G7  NameStormers
  └─ G8  IA C1.0
```

这里的关键原则是：**不同路线不强制使用同一个 Worker 数量或同一个流程模板。**

Method defines workflow → Workflow defines roles → Roles define contexts → Contexts define chat / Agent sessions.

详细拆分见：`naming-worker-conversation-plan-v0.1.zh-CN.md`。

## 4. Context Isolation 原则

后续正式隔离实验采用最小知情原则：

- Orchestrator 知道整个 benchmark；
- Worker 只知道组织愿景、自己的角色、当前步骤和必要输入；
- Generator 不应看到其他 arm 的候选、survivor、collision 结果或 leaderboard；
- Screener 不应知道候选来自哪一种生成方法；
- Quality Reviewer 原则上不看 feasibility 结果；
- Owner Exposure Gate 不看 arm 身份；
- 只有当某种原方法本身要求反馈进入下一轮生成时，才允许把该反馈以方法允许的结构化形式传回同一路线（典型：G4 / G7 / G8）；即使如此，也不默认向 Generator 暴露原始 feasibility 记录或完整历史。

## 5. 证据边界

这套 Method Map 只复原公开可确认的方法结构，不把机构营销语言或 IA 推断伪装成对方的正式 SOP。

标记规则：

- **Public-confirmed**：公开资料能直接确认；
- **Research synthesis**：由多条公开证据归纳；
- **Benchmark adaptation**：为 IA benchmark 做的执行化改造；
- **Unknown / proprietary**：公开资料不足，不猜。

## 6. 第二层文档

本目录维护：

- `method-g0-ia-baseline-v0.1.zh-CN.md`
- `method-g1-lexicon-v0.1.zh-CN.md`
- `method-g2-catchword-v0.1.zh-CN.md`
- `method-g3-igor-v0.1.zh-CN.md`
- `method-g4-river-wolf-v0.1.zh-CN.md`
- `method-g5-siegel-gale-v0.1.zh-CN.md`
- `method-g6-tungsten-v0.1.zh-CN.md`
- `method-g7-namestormers-v0.1.zh-CN.md`
- `method-g8-c1-agent-native-v0.1.zh-CN.md`

九份 Method Profile 已完成第一轮 worker-topology 审计，分别明确 method stages、建议 isolated context 数、并行 / 循环边界和第三层 packet 数。

## 7. 第三层执行基线

当前已建立：

- method-specific 基础 Task Packets：**46**；
- benchmark 共用评估 Task Packets：**5**；
- 基础第三层合计：**51**；
- G5 独立 Testing Worker：**+1 optional**。

注意：Task Packet 是可复用岗位模板，不等于实际聊天窗口数量。G4 / G7 / G8 的循环会重复实例化同一个 Packet。

第三层统一规则与公共输入：

- `Execution/worker-task-packet-schema-v0.1.zh-CN.md`
- `Execution/shared-organization-vision-context-v0.1.zh-CN.md`
- `Execution/Shared_Evaluation/e1-domain-registry-screener-v0.1.zh-CN.md`
- `Execution/Shared_Evaluation/e2-reality-collision-screener-v0.1.zh-CN.md`
- `Execution/Shared_Evaluation/e3-quality-pareto-reviewer-v0.1.zh-CN.md`
- `Execution/Shared_Evaluation/e4-method-fidelity-integrity-reviewer-v0.1.zh-CN.md`
- `Execution/Shared_Evaluation/e5-owner-exposure-decision-packet-v0.1.zh-CN.md`

method-specific packets 位于 `Task_Packets/`，目录索引见 `Task_Packets/README.zh-CN.md`。

当前下一步不是继续建设新的文档层，而是：**Integration Audit → 单路线完整 dry run → 修正真实交接缺口 → freeze → isolated benchmark。**