# Adaptive Naming System Evolution / Runtime Architecture v0.4

本文件把 Adaptive Naming 从“会调整搜索路线的 Skill”扩展为“可在任务内调整执行方案、并可通过跨任务证据受控进化方法本身的 Agent-native 系统”。

核心边界：

> **v0.3.3 继续作为经过真实 Fit Test 的 job-level Controller baseline；v0.4 在其外部增加 Workflow Adaptation、Runtime Adapter 与 Method Evolution Outer Loop。**

不因为候选难找就自动修改方法。只有明确的控制缺陷、跨任务经验或高置信机制证据，才进入方法演化层。

---

## 1. 三层自适应

### Level 1 · Search / Candidate Adaptation

在当前 Naming Job 内调整：

- semantic / naming region；
- territory material；
- construction operator；
- exploration / exploitation；
- batch / cadence；
- rescue / reality / validation 等动作。

这一层回答：**“下一步去哪找、怎么造、查什么？”**

### Level 2 · Workflow Adaptation

Controller 根据 diagnosis 选择认知 / 执行模式，而不是始终用同一种 microcycle：

- prior-map / white-space mapping；
- territory / vocabulary expansion；
- divergence burst；
- creative + linguistic parallel；
- category-parallel generation；
- architecture stress；
- feedback → refinement；
- temporal evaluation；
- reality observe → update loop；
- transformation rescue。

这一层回答：**“当前问题最适合用什么工作方式解决？”**

### Level 3 · Method Evolution

跨 Naming Job 汇总经验，形成方法假设，并受控决定是否修改：

- diagnosis rules；
- workflow pattern library；
- router / scheduler policy；
- state schema；
- references；
- regression evals；
- 核心 Skill invariants。

这一层回答：**“我们的方法本身应该不应该改变？”**

Level 3 不得由单次候选胜负直接触发。

---

## 2. Search Landscape：G3 先验地图 + G8 在线学习

每个 Naming Job 维护轻量 `search_landscape`。它不是一次性大报告，而是可持续更新的搜索空间状态。

每个 region 至少可记录：

```yaml
- region_id: R001
  semantic_position: []
  character_position: []
  construction_position: []
  collision_prior: unknown
  evidence_confidence: low
  quality_yield: unknown
  reality_crowding: unknown
  information_gain: unknown
  sampling_status: under_sampled
  move_or_stay_rationale: null
```

规则：

1. 初始 map 只是先验，不冒充现实真值；
2. online observations 通过 Controller / State Updater 更新 region，不直接喂给 Generator；
3. candidate failure 与 region failure 分开；
4. 只有重复、结构化证据才能提高 `reality_crowding` 或改变 collision prior；
5. 地图用于决定 move / stay / reopen，不用于制造“安全词根”。

---

## 3. Workflow Pattern Scheduler

Method Scheduler 分为两层：

### 3.1 Workflow Pattern

决定**怎么组织认知与执行**。

最小 pattern library：

| pattern_id | 主要来源 / 灵感 | 适用触发 |
| --- | --- | --- |
| `white_space_mapping` | Igor / G3 | region 结构、拥挤度、类别差异不清 |
| `territory_expansion` | Catchword / G2 | material starvation / lexical collapse |
| `divergence_burst` | Catchword / NameStormers | creative window 过窄、候选依恋、局部搜索过深 |
| `creative_linguistic_parallel` | Lexicon / G1 | 语言质量反复失败，或高价值候选需并行语言工程 |
| `category_parallel` | Siegel+Gale / G5 | naming style / abstraction space 覆盖不足 |
| `architecture_stress` | Tungsten / G6 | parent / umbrella scale 与未来扩展是关键未知 |
| `feedback_refinement` | NameStormers / G7 | 有高价值 stakeholder feedback，且 refinement 可能改变候选 |
| `online_observe_update` | IA G8 | 现实碰撞高、需要小批实时学习 |
| `transformation_rescue` | IA synthesis | 强原型主要死于 reality / namespace |
| `validation_only` | shared | 当前最大未知是验证，不需要生成 |

Pattern 不是整套 agency SOP。IA 的方法是抽取有效机制，按状态组合。

### 3.2 Construction Operator

决定**名字怎么形成**：existing word、compound、blend、root-derived、coinage、sound-first、spelling mutation 等。

Controller 先决定是否需要特殊 Workflow Pattern，再由 operator scheduler 分配具体生成方式。两层不得混为“方法”。

---

## 4. Search Cadence 是控制变量

不把“小批”写成永久教条。

```yaml
search_cadence:
  mode: micro_probe | portfolio_batch | divergence_burst | focused_exploitation | validation_only
  target_count: null
  rationale: null
  stop_condition: null
```

典型使用：

- `micro_probe`：回答一个明确未知；
- `portfolio_batch`：多个差异化路线并行；
- `divergence_burst`：短暂扩大 creative window，之后统一 funnel；
- `focused_exploitation`：有强跨批信号时有限深挖；
- `validation_only`：不生成。

数量由问题、runtime 成本、mode-collapse 风险和 information gain 决定，不冻结为通用常数。

---

## 5. Runtime Capability Profile / Adapter

逻辑方法与执行环境分离。

Controller 定义：

- logical role；
- allowed context；
- forbidden context；
- input artifact；
- output artifact；
- handoff。

Runtime Adapter 决定这个 role 在当前环境中如何执行。

最小 capability profile：

```yaml
runtime_capability_profile:
  shared_context_only: null
  fresh_context_available: null
  isolated_subagents_available: null
  tool_rich_browser_or_shell: null
  persistent_state_io: null
  parallel_workers_available: null
```

执行优先级：

1. 真 isolated worker / sub-agent；
2. fresh context；
3. 同上下文的 sanitized brief + best-effort blindness；
4. 若连最小隔离都做不到，降低 claim，不伪装成真正 blind review。

Runtime 能力不足改变的是**执行保真度与证据置信度**，不是方法定义本身。

---

## 6. Preference Model：偏好学习但不变成生成模板

Owner preference 与一般 naming quality 始终分离。

可记录：

```yaml
preference_model:
  signals:
    - preference_id: null
      statement: null
      scope: task | organization | cross_task
      evidence_count: 0
      confidence: low
      stability: one_off | emerging | stable | contradicted
      phase_influence: early_low | normal | late_high
```

规则：

- 一次喜欢 / 不喜欢不能升级成稳定规则；
- early exploration 只弱影响搜索，防止过拟合即时口味；
- late convergence 可作为 tie-break / resonance 证据；
- 具体被喜欢过的候选、词根、survivor shape 不直接进入 Generator Brief。

---

## 7. Method Evolution Outer Loop

### 7.1 Experience Candidate

每个 job 可以导出方法经验候选，但不能直接改稳定 Skill。

最少字段：

```yaml
experience_id: null
source_job_id: null
observation: null
proposed_generalization: null
mechanism: null
supporting_evidence: []
counterevidence: []
confidence: low | medium | high
scope: task_local | potentially_general | general_candidate
status: observed
```

### 7.2 Cross-task Experience Registry

所有可泛化经验进入独立 Registry，而不是复制到 Generator context。

状态：

- `observed`
- `hypothesis`
- `provisional_rule`
- `stable_rule`
- `deferred`
- `rejected`
- `superseded`

### 7.3 Promotion Contract

方法变化至少满足以下之一：

**A. Cross-task promotion**
- ≥2 个独立 Naming Job 出现一致机制证据；
- 有反例检查；
- regression 不破坏既有 invariants。

**B. Severe-control-defect promotion**
- 单个真实任务暴露高置信、可复现的控制缺陷；
- 缺陷有明确因果机制，不只是候选表现差；
- 新规则有对应 regression；
- 变更保留 rollback / supersede 路径。

因此跨任务重复是默认强证据，但不是修复严重控制 bug 的绝对前提。

### 7.4 Method Hypothesis

```yaml
hypothesis_id: H001
claim: null
changes: []
expected_benefit: null
known_risk: null
supporting_experience_ids: []
counterevidence: []
regression_cases: []
status: proposed | testing | promoted | rejected | superseded
introduced_in_version: null
rollback_target: null
```

### 7.5 禁止直接自改

Agent 可以自主：

- 记录 experience candidate；
- 聚合重复模式；
- 提出 method hypothesis；
- 创建 regression proposal；
- 建议版本变更。

但不能仅因为“一批结果不好”就把稳定规则自动重写为真理。

---

## 8. Character / Expression Profile

Name Job 说明“名称负责什么”，Value Model 说明“为什么重要”；必要时再增加轻量表达层：

```yaml
expression_profile:
  desired_character: []
  undesired_character: []
  abstraction_continuum: null
  familiarity_novelty_position: null
  institutional_creative_balance: null
  source_refs: []
```

仅当“名字给人的气质 / 人格 / 抽象度”确实会改变搜索时启用，不变成所有任务固定问卷。

---

## 9. Linguistic Engineering 作为可独立 Worker 的候选

当 pronunciation / dictation / processing fluency 是主要未知时，可触发独立 `linguistic_engineering`：

- phonotactic naturalness；
- sound symbolism；
- spoken recovery branches；
- letter structure / visual processing；
- target-language phoneme / spelling risk；
- 必要的文化语言检查。

Creative 与 Linguistic 可以并行，避免语言分析提前压窄创意窗口。若 runtime 允许，优先使用独立 context / worker。

---

## 10. 系统完整循环

```text
Owner goals / constraints
        ↓
Mission / Value → Name Job → Criteria
        ↓
Search Landscape + Biggest Unknown
        ↓
Workflow Pattern Scheduler
        ↓
Construction / Research / Validation actions
        ↓
Workers through Runtime Adapter
        ↓
Quality + Value + Reality observations
        ↓
Diagnosis → update job state
        ↺ Job-level adaptation

job experience candidates
        ↓
Cross-task Experience Registry
        ↓
Method Hypothesis + counterevidence
        ↓
Regression / live-fit validation
        ↓
promote / revise / reject / supersede
        ↺ Method-level evolution
```

这就是“方案可自调 + 方法可进化”的完整含义。
