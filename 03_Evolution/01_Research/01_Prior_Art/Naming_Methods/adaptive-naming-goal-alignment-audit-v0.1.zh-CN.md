# Adaptive Naming Goal Alignment Audit v0.1

> 日期：2026-09-11
> 范围：用 #407/#408 的 prior-art 方法地图、G0–G8 设计目标与当前 Adaptive Naming v0.3.3 对照，检查是否偏离“IA 自己的、可自适应并可进化的 Agent + Skill 命名系统”目标。
>
> 本文是方法架构自查，不重启 G0–G8 benchmark，也不否定 v0.3.3 已通过的 job-level control regression baseline。

## 1. 目标重述

最终目标不是得到一条固定的“最佳命名流程”，也不是把 G1–G8 机械拼成巨型 SOP。

更准确的目标是建立一套 **Adaptive Naming System**：

1. 在单个 Naming Job 内，Agent 根据当前状态、自主诊断和调整搜索方案、工作流、构词方法、研究与验证动作；
2. 在多个 Naming Job 之间，系统能够把经验与失败模式积累为证据，经过验证后调整方法库 / 调度策略 / Skill，而不是把单次经验直接写回稳定规则；
3. 逻辑方法与运行环境分离：相同方法能在单对话、fresh context、sub-agent、Codex/Work、CI / shell 等不同 runtime 下执行，并诚实记录实际隔离等级；
4. Owner 只决定真正的目标、边界与最终主观选择，内部搜索路径和方法调度由 Controller 负责；
5. 方法可以进化，但必须可审计、可回归、可回滚，不能变成 Agent 自由改写自身规则。

因此，“自我调整方案”和“自我调整方法”应明确拆成两层：

- **Job-level adaptation（内循环）**：当前任务里换区域、换方法、换 batch、开/关模块、探索/利用、Reality/Rescue/Feedback；
- **Method-level evolution（外循环）**：跨任务把经验候选聚合成方法假设，经多任务证据 + regression 验证后，再 promote / revise / reject / rollback。

---

## 2. 当前 v0.3.3 已经做对的部分

### 2.1 上游战略理解不再压成关键词

Mission / Value Model → Name Job → Decision Criteria 已经明显优于早期 `semantic_core → generation`；这吸收并扩展了 Lexicon、Igor、River + Wolf、Tungsten 的上游战略工作。

### 2.2 Controller 已能按最大未知改变路径

Module Router + Method Scheduler + diagnosis + Owner Gate 已能做到：

- generation 不是默认下一步；
- territory / reality / rescue / decision hygiene 按触发加载；
- search strategy 不转嫁给 Owner；
- exploration / exploitation 可切换；
- reality failure 与 intrinsic quality 分离。

这已经是 G8 Agent-native loop 的实质升级。

### 2.3 生成污染与评价污染已有显式控制

Controller-only exclusions、positive Generation Brief、reality-feedback quarantine、truthful isolation、Decision Hygiene、Reality Screening Contract 已修复真实 Fit Test 暴露的多个 Agent-native failure modes。

### 2.4 Progressive Disclosure 解决了“大型 Skill 臃肿”问题

当前 thin Controller + references + templates + evals 的方向合理；复杂专业能力不应因为“存在”就每次执行。

---

## 3. 本轮重新对照 prior art 后发现的缺口

下面区分“目标级遗漏”和“可选能力增强”。

## P0-A：跨任务 Method Evolution Loop 尚未真正实现

这是当前最重要的缺口。

#408 曾明确要求：

- 任务内学习与跨任务 Skill 演化分开；
- 跨任务经验有独立积累位置；
- 单次任务只产生 `experience_candidate`，不直接改核心 Skill。

当前 v0.3.3 只有 per-job state 中的 `experience_candidates`，但没有真正的跨任务 Experience Registry，也没有：

- candidate learning 的聚合；
- supporting / contradicting task evidence；
- generalizability 判断；
- promotion threshold；
- regression requirement；
- method patch 的 rollback / supersede 状态。

因此当前系统已经会“任务内自适应”，但“方法自己逐步进化”仍主要依赖人工在聊天中发现问题并直接改 Skill。

### 建议

新增独立 **Method Evolution Layer**：

```text
per-job experience_candidate
        ↓
Cross-task Experience Registry
        ↓
Method Hypothesis
        ↓
Evidence accumulation / counterexample
        ↓
Regression + live-fit validation
        ↓
promote | revise | reject | defer
        ↓
Skill / reference / eval version update
        ↓
rollback path preserved
```

这层不能直接给 Generator 使用，避免“跨任务 survivor feedback”污染创意搜索。

---

## P0-B：缺少明确的 Runtime Adapter / Execution Topology Layer

早期 Method Map 的重要原则是：

> Method defines workflow → Workflow defines roles → Roles define contexts → Contexts define sessions.

#408 也明确把“平台中立执行 + 不同网络 / 子 Agent / shell 能力的适配器”列为目标。

当前 v0.3.3 能记录 `best_effort_same_context / fresh_context / isolated_runtime`，但主要是在**事后描述隔离能力**，还没有一层正式的 runtime capability → worker topology 映射。

这意味着：

- 在普通聊天里，Generator / Evaluator / Reality Observer 可能仍共享历史；
- 在支持 sub-agent / fresh context 的 runtime 中，也没有统一合同告诉 Controller 应如何把同一逻辑方法拆成独立 Worker；
- Superpowers 式多 Skill / Worker 结构未来也缺一个接入点。

### 建议

定义 `runtime_capability_profile` 与 adapter：

- `single_shared_context`
- `fresh_context_available`
- `isolated_subagents_available`
- `tool_rich_browser_or_shell`
- `persistent_state_io`

Controller 只定义逻辑角色与 artifact contract；Adapter 决定一个角色是在同一对话 best-effort、fresh session、sub-agent 还是外部 runner 执行。

---

## P1-A：G3 + G8 的 Search Landscape Map 被弱化了

早期明确目标是：

> **先验地图（G3） + 在线学习（G8）**。

当前 template 仍有 `map`，但它没有进入 v0.3.3 的“每个 Naming Job 最小核心状态”；Scheduler 主要维护 strategy yield / crowding，而不是显式维护 naming-region / taxonomy / collision prior / white-space hypothesis。

这会让系统在长期运行中更像“调构词法”，而不是“学习命名空间”。

### 建议

把轻量 `search_landscape` 恢复为一级状态对象，而不是每次都做大规模竞争分析：

- region / territory id；
- semantic / character / construction position；
- collision prior；
- evidence confidence；
- quality yield；
- reality crowding；
- information gain；
- sampled / under-sampled；
- move / stay rationale。

它是 G3 prior map 与 G8 online update 的统一表示。

---

## P1-B：当前 Scheduler 主要调“构词策略”，但还缺“工作流方法模式”这一层

这是本轮最关键的新抽象之一。

第三方方法真正有价值的差异，并不全是构词法：

- Lexicon：Creative + Linguistic Engineering 并行；
- Catchword：Vocabulary / Territory → high-volume divergence → shortlist；
- Igor：competitive map / taxonomy / white-space 前置；
- River + Wolf：Character / Communication / Construction / Continuum 参数化；
- Siegel+Gale：多 category 并行 + contextual evaluation；
- Tungsten：Pivot / evergreen + architecture stress；
- NameStormers：pitch → feedback/test → refinement；
- G8：observe → update → move/stay 在线循环。

当前 Module Router 已覆盖其中一部分，但 Method Scheduler 仍更像 **operator scheduler**。

### 建议：把方法分成两种可调度资源

1. **Workflow Patterns**：决定“怎么组织认知与执行”
   - white-space mapping
   - vocabulary / territory expansion
   - divergence burst
   - creative + linguistic parallel
   - category-parallel generation
   - architecture stress
   - feedback-refinement loop
   - temporal evaluation
   - reality-observe/update loop
   - transformation rescue

2. **Construction Operators**：决定“名字怎么造”
   - lexical / compound / blend / root-derived / coinage / sound-first / mutation 等。

Controller 应先根据 diagnosis 选择 Workflow Pattern，再由 Operator Scheduler 选择构词方法。

这比“把 G1/G2/G3 整套固定执行”更符合 IA 自己的方法：**拆出有效机制，按状态动态组合。**

---

## P1-C：Batch / Search Cadence 还没有成为真正可自适应的控制变量

G8 强项是小批在线学习；Catchword 和 NameStormers 则保留 high-volume divergence / Lightning Round 的价值。

当前系统偏向 microcycle，小批是默认合理选择，但不能把它变成新的固定教条。

### 建议

让 Controller 调整 `search_cadence`：

- `micro_probe`：1–5，快速回答一个未知；
- `portfolio_batch`：多方法小批；
- `divergence_burst`：当局部搜索/候选依恋过强、需要扩大创意窗口时短暂高容量发散；
- `focused_exploitation`：围绕有证据的强方向有限深挖；
- `validation_only`：0 generation。

触发依据是 information gain、mode collapse、material starvation、candidate attachment risk、runtime cost，而不是固定数字。

---

## P1-D：Linguistic Engineering 目前更多是“评价维度”，还不是独立认知能力

Lexicon 公开方法把 Creative Teams 与 Linguistic Engineering 并行；Catchword 也有独立 linguistic / cultural screening。

当前 Skill 会看 pronunciation / spelling / cultural risk，但通常是在候选出来以后检查，尚未显式支持：

- sound symbolism；
- phonotactic naturalness；
- letter structure / visual processing；
- processing fluency；
- spoken recovery branches；
- target-language phoneme / spelling risk；
- linguistic guidance 在不污染 creative generation 的情况下形成并行 artifact。

### 建议

先作为 optional `linguistic_engineering` module，而不是核心固定步骤。

触发：

- 口语 / 听写恢复是高优先级；
- 多批候选语义不错但读写质量反复失败；
- 进入全球 / 多语言 shortlist；
- high-value candidate 需要语言级压力测试。

若未来有独立 runtime，这也是最适合晋升成独立 Skill / Worker 的能力之一。

---

## P1-E：Owner Preference 目前有记录，但缺“学习模型”

早期设计曾明确：

- Owner 不审大量 working pool；
- 从重复反馈学习稳定偏好；
- 偏好与 general quality 分开；
- early exploration 权重较低、late convergence 权重提高。

当前 v0.3.3 有 `owner_preferences` 和 Owner Gate，但没有显式：

- feedback evidence count；
- stable vs one-off preference；
- confidence；
- scope（某任务 / 某组织 / 跨任务）；
- phase-dependent influence；
- contradiction / change over time。

### 建议

增加轻量 `preference_model`，但绝不把历史偏好变成生成模板；它主要影响 shortlist / tie-break / late-stage convergence。

---

## P2-A：River + Wolf 的 Character / Continuum 被吸收得不够显式

当前 Name Job 回答“名字负责什么”，Value Model 回答“为什么重要”，但仍缺一个清晰问题：

> **名字应该给人什么人格 / 气质 / 表达感？**

这不是 mission，也不是 semantic meaning。

可以增加可选 `expression_profile`：

- desired character / tone；
- descriptive ↔ suggestive ↔ abstract continuum；
- institutional ↔ playful；
- warm ↔ technical；
- familiar ↔ strange；
- calm ↔ energetic；

这些默认是 search variables / preferences，除非有来源支持为硬要求。

不建议做成高维评分表，只需要帮助 Generator / Scheduler 不把“语义正确”误当成“品牌人格正确”。

---

## 4. 对“自我调整方法”的更准确理解

Owner 的理解方向是对的，但应加一个安全边界：

> **不是让 Agent 在运行中随意重写自己的 Skill，而是让 Agent 拥有“可调整当前方法组合”的内循环，以及“基于跨任务证据受控修改方法库”的外循环。**

因此建议把 IA Naming 的自适应分成三层：

### Layer 1 — Search / Candidate Adaptation

调整 region、material、candidate family、construction operator、batch size、explore/exploit。

### Layer 2 — Workflow Adaptation

调整要调用哪些 method patterns / modules / worker topology，例如先做 white-space、开 divergence burst、并行 linguistic engineering、做 architecture stress、请求 feedback refinement。

### Layer 3 — Method Evolution

跨任务聚合经验，改变 pattern library、diagnosis rules、router、scheduler policy、regression cases 与 Skill 本体。

前三者的改变权限不同：

- L1：Controller 可完全自主；
- L2：Controller 通常自主，只有改变 Owner 目标 / 真实边界才询问；
- L3：可自动提出 method hypothesis / patch proposal，但必须经过证据阈值、回归检查、版本化与 rollback，不能静默自改稳定 Skill。

---

## 5. 建议的 v0.4 架构方向

不要推翻 v0.3.3。将它视为已经通过真实 Fit Test 的 **Inner Controller baseline**，在外面增加尚未实现的层：

```text
                ┌─────────────────────────────┐
                │ Method Evolution Layer      │
                │ Experience Registry         │
                │ Hypothesis / promotion      │
                │ Regression / rollback       │
                └──────────────┬──────────────┘
                               │ stable changes only
                               ↓
┌─────────────────────────────────────────────────────────┐
│ Adaptive Naming Controller                              │
│ Mission/Value → Name Job → Criteria → Search Landscape │
│                    ↓                                    │
│           Workflow Pattern Scheduler                    │
│                    ↓                                    │
│           Construction Operator Scheduler               │
│                    ↓                                    │
│ Research / Generate / Linguistic / Evaluate / Reality   │
│                    ↓                                    │
│ Diagnose → state update → next action ↺                 │
└──────────────────────────┬──────────────────────────────┘
                           │ logical worker contracts
                           ↓
                ┌─────────────────────────────┐
                │ Runtime Adapter             │
                │ same-context / fresh /      │
                │ sub-agent / shell / CI      │
                └─────────────────────────────┘
```

这仍然是 **thin core + progressive disclosure**，不是巨型固定流程。

---

## 6. 建议实施优先级

### 必须补齐后才算真正达到原目标

1. Cross-task Experience Registry + Method Evolution contract；
2. Runtime Capability / Adapter contract；
3. Search Landscape 重新成为 first-class state；
4. Workflow Pattern Scheduler 与 Construction Operator Scheduler 分层。

### 第二优先级 / 按需模块

5. adaptive search cadence / divergence burst；
6. linguistic engineering / linguistic-cultural screening；
7. phase-aware Owner preference model；
8. lightweight expression / character profile。

### 暂时不要做

- 不拆成十几个永久独立 Skill；
- 不把所有 prior-art method 都固定执行；
- 不让 Experience Registry 直接影响 Generator token/词根；
- 不允许一次任务的成功经验自动升级 core rule；
- 不为了“自进化”允许 Agent 静默重写稳定 Skill。

---

## 7. Baseline / freeze 解释

v0.3.3 的 freeze 仍然有效，但应精确定义为：

> **job-level Controller baseline frozen unless a new control defect appears.**

本轮发现的是原始目标中尚未完成的 **meta-method / cross-task / runtime architecture**，不是 RND-061 对 v0.3.3 内循环 regression 的反例。

因此后续可以在不破坏 v0.3.3 job-level baseline 的前提下发展 v0.4 外层架构。

这也更符合 IA 的核心方向：不是寻找一次性的“最佳命名 SOP”，而是建立一个能够在真实任务中持续学习、调整执行方案，并通过受控证据让方法本身逐步进化的 Agent-native Naming System。
