# Naming Worker / Conversation Plan v0.1

> 状态：Research synthesis / execution planning baseline
>
> 目的：把 G0–G8 的 Method Profile 转成可执行的隔离 Worker / 对话上下文计划。这里统计的是 **Task Packet 模板 / context type**，不是实际运行时会打开多少次聊天窗口。循环方法可以多次实例化同一 Packet。

## 1. 总原则

```text
Method defines workflow
→ Workflow defines roles
→ Roles define allowed context
→ Allowed context defines isolated worker sessions
```

不是“一个方法一个对话框”，也不是“一个流程名词一个对话框”。拆分依据只有两个：

1. 原方法是否真的需要独立角色 / 并行 / 反馈回路；
2. 把两个阶段放在同一上下文中是否会产生不该有的信息污染。

### 最小知情

- Orchestrator：知道整个实验设计、所有路线、状态与比较逻辑。
- Worker：只知道 Organization Vision + 自己的角色 + 当前任务 + 必要上游产物。
- Generator：默认不知道其他 arm、历史 survivor、collision 统计、leaderboard、下游质量结论。
- Screener：默认不知道候选来自哪个 arm。
- Quality Reviewer：默认不看 feasibility / domain 结果，以免“可用”偷换成“质量高”。
- 只有方法本身要求反馈进入下一轮时才允许结构化回流（G4 / G7 / G8）；结构化回流不等于把原始 feasibility 记录、完整历史或 survivor 标签直接暴露给 Generator。

## 2. 九条路线的确定拆分

| Arm | Method | 公开/逻辑阶段 | 基础 isolated contexts | 第三层基础 Task Packets | 结构特点 |
|---|---|---:|---:|---:|---|
| G0 | IA Baseline | 2 | 2 | 2 | 极简 baseline |
| G1 | Lexicon | 5（含并行） | 5 | 5 | Creative / Linguistic 双轨 |
| G2 | Catchword | 8 | 7 | 7 | 先发散、后统一筛 |
| G3 | Igor | 6 | 4 | 4 | Positioning / competitive / white-space 前置 |
| G4 | River + Wolf | 5 + loop | 5 / cycle | 5 | 4Cs 参数化 + 受控迭代 |
| G5 | Siegel+Gale | 5（generation 四分支） | 8 | 8 | 四类生成并行；Testing 可选 |
| G6 | Tungsten | 5 | 4 | 4 | Pivot → parent name → architecture test |
| G7 | NameStormers | 7 + loop | 7 / base cycle | 7 | pitch / feedback / refinement 回路 |
| G8 | IA C1.0 | 6 + micro-cycle | 4 context types | 4 | Generator / Observer / Updater 循环 |

**Method-specific 基础 Task Packets 合计：46。**

G5 若启用独立 Testing Worker，再增加 **1 个 optional packet**。

## 3. 每条路线的 context topology

### G0 — 2

`Vision/Semantic Space → Baseline Generator`

后续筛查属于共用评估层，不反馈给 Generator。

### G1 — 5

```text
Strategy / Creative Framework
       ├──→ Creative Generator ─────┐
       └──→ Linguistic Engineering ─┤
                                     ↓
                              Funnel / Selection
                                     ↓
                           Implementation Support
```

Creative 与 Linguistic 必须是独立上下文。

### G2 — 7

```text
Discovery + Brief
  ↓
Vocabulary / Territories
  ↓
Divergent Generation
  ↓
Internal Shortlist
  ├──→ Reality Prescreen ────────┐
  └──→ Linguistic/Cultural ──────┤
                                  ↓
                         Contextual Evaluation
```

Generator 不看任何 screening feedback。

### G3 — 4

`Positioning + Competitive Taxonomy + White-space → Name Development → Reality Prescreen → Contextual Presentation`

前三个 strategy 子阶段共用一个 Worker，因为它们本来就是连续的竞争空间建模链。

### G4 — 5 / cycle

`Research → 4Cs → Development → Shortlist → Screening/Iteration Coordinator`

若需迭代，Coordinator 只生成结构化 iteration brief；下一轮 Development 用新上下文，不继续堆积原聊天历史。

### G5 — 8 (+1 optional)

```text
Simplicity Strategy
  ↓
Category Strategy
  ├→ Descriptive Generator ────┐
  ├→ Suggestive Generator ─────┤
  ├→ Coined Generator ─────────┤→ Blind Contextual Evaluation → Governance/Decision
  └→ Edgy Generator ───────────┘
```

四个生成器互不可见。Optional Testing 在 Governance 前作为独立证据输入。

### G6 — 4

`Pivot + Evergreen Strategy → Parent Name Development → Architecture Stress-test → Selection/Implementation`

Architecture Worker 只测，不改名。

### G7 — 7 / base cycle

`Discover → Lightning Generation → Prescreen → Pitch → Feedback/Test → Refinement → Final`

Feedback 只能经结构化压缩后进入新的 Refinement context。循环复用同一 Task Packet，不新增文档。

### G8 — 4 context types

```text
Region Strategy ───────────────→ Micro Generator → Reality Observer → State Updater
     ↑                                                               │
     └──────── arm-local internal compressed state ───────────────────┘

State Updater → Region Strategy：允许读取 arm-local failure topology / feasibility observations
Region Strategy → Micro Generator：只交冻结 Region Brief，不交 survivor / Red / Yellow / domain / collision 记录
```

Generator 不搜索；Observer 不生成；Updater 不直接创造候选。Reality feedback 先进入 Updater 的 arm-local internal state，再由新的 Region Strategy 压缩成不泄露具体 feasibility 结果的 Region Brief。S2/S3/S4 会重复实例化很多次，但第三层只需要 4 份模板。

## 4. Benchmark 共用评估层

为了真正做到 generation / screening / quality 分离，除 46 个 method-specific packets 外，再建立 5 个共用 Task Packet：

1. **E1 Domain / Registry Screener**
   - 只做 exact normalized domain / registry observation；不知道 arm。
2. **E2 Reality Identity / Collision Screener**
   - 公司、产品、项目、软件、人物、商标导向与严重混淆；不知道 arm。
3. **E3 Quality / Pareto Reviewer**
   - 只看冻结 Naming Job 与候选本身；原则上不知道 domain / reality 是否已经通过。
4. **E4 Method-fidelity / Experiment Integrity Reviewer**
   - 只判断 Worker 是否按指定方法执行、是否 drift / template collapse / rationale decline；不重新生成名字。
5. **E5 Owner Exposure / Decision Packet**
   - 最终把少量 quality-qualified、feasible candidates 给 Owner；隐藏 arm 身份与 benchmark 成绩，避免方法标签影响主观判断。

因此：

- **第三层基础 Task Packets：46 + 5 = 51。**
- **若启用 G5 独立 Testing：52。**

这不是 51/52 个同时存在的聊天窗口。实际 session 数由循环次数、并行方式和是否复用上下文实例决定。

## 5. 两个执行基础设施文档（不属于某个方法步骤）

当前已建立：

1. `Execution/worker-task-packet-schema-v0.1.zh-CN.md`：统一定义每份 Packet 必须包含 Role / Vision / Input / Allowed Context / Forbidden Context / Output / Stop Condition / Provenance。
2. `Execution/shared-organization-vision-context-v0.1.zh-CN.md`：所有需要知道总体愿景的 Worker 共用的最小 Vision，不包含 benchmark 战略、其他 arm 或筛选结果。

这两份属于执行基础设施，不计入上面的 51 个步骤包。

method-specific 46 个 Packet 与 Shared Evaluation 5 个 Packet 均已建立；当前工作已从“第三层建设”进入 **Integration Audit / dry-run validation**。

## 6. 文档与聊天窗口不是 1:1

必须明确区分：

- **Task Packet**：可复用的“岗位说明书”。
- **Worker Session / Chat**：某一次实际执行实例。

例如 G8 只有 4 个 Packet，但如果产生 20 个 micro-cycles，Generator / Observer / Updater 可以被多次实例化；不需要复制 60 份文档。

G5 正好相反：四个 category Generator 虽然只跑一轮，也必须使用四个彼此隔离的 session，因为并行多样性本身就是方法的一部分。

## 7. 当前结论

三层执行文档已建立：第一层 Method Map、第二层 9 份 Method Profile、第三层 46 个 method-specific + 5 个 shared evaluation Task Packets（G5 Testing +1 optional），以及两份执行基础设施文档。

当前顺序应为：

`Integration Audit → 单路线完整 dry run → 修复真实交接缺口 → freeze packet versions → 正式 isolated benchmark`

不得回退到“一个方法一个长对话框”或“所有方法共享长上下文”的执行方式。历史 #410 结果继续保留为 shared-context benchmark evidence，与后续 isolated-context denominator 分开。