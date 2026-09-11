---
name: adaptive-naming
description: 自适应品牌、组织、项目与产品命名。先建立目标、价值模型、名称职责与真实边界，再由 Controller 按当前最大未知动态调度工作流、研究、生成、评价、现实验证与救援；跨任务经验经证据与回归后可受控进化方法本身。
version: 0.4.0
---

# Adaptive Naming Skill v0.4.0

## 1. 定位：Adaptive Naming System，而不是固定流水线

本 Skill 是 Naming Controller 的稳定入口，不是要求每个任务把所有专业命名步骤跑一遍。

核心原则：

> **目标明确，边界稳定，路径开放，按需加载，状态学习，经验累积，方法受控进化。**

角色分工：

> **Owner 决定“要什么、真正不能变什么、最后喜欢什么”；Controller 决定“怎么理解、怎么找、先试什么、何时换路、采用什么工作流、加载哪些模块、哪些方法并行、哪些强原型值得救援”。**

v0.3.3 已通过真实 #411 Fit Test 的 job-level Controller 行为继续作为内循环 baseline。v0.4.0 在其外部增加：

- Search Landscape；
- Workflow Pattern Scheduler；
- adaptive search cadence；
- Runtime Adapter；
- cross-task Method Evolution Outer Loop。

详细系统架构：

[`references/adaptive-system-evolution-and-runtime.md`](references/adaptive-system-evolution-and-runtime.md)

---

## 2. 三层自适应

### Level 1 · Search / Candidate Adaptation

当前 Naming Job 内调整：region、territory material、construction operator、batch/cadence、explore/exploit、reality、rescue、validation。

### Level 2 · Workflow Adaptation

根据 diagnosis 选择不同认知 / 执行模式，例如 white-space mapping、territory expansion、divergence burst、creative + linguistic parallel、architecture stress、feedback/refinement、online observe/update。

### Level 3 · Method Evolution

跨 Naming Job 把 experience candidate 聚合成 method hypothesis，经 counterevidence、regression、live-fit 后才能 promote / revise / reject / supersede。

**候选难找 ≠ 方法必须修改。单次候选输赢不得直接改稳定 Skill。**

---

## 3. 稳定不变量

运行中不得为了“得到结果”随意破坏：

1. 使命 / 愿景先结构化理解，不直接压成几个关键词。
2. **Value Model ≠ Name Job。** 组织珍视什么，不等于名称必须表达什么。
3. 名称不需要压缩完整使命；允许只承载一个核心价值、关系、气质或长期身份。
4. 名称本身质量、value alignment、现实可用性分开记录。
5. 硬约束必须有 provenance；搜索属性默认不是硬约束。
6. Owner preference 与一般质量分开；最终采用权属于 Owner。
7. 搜索多样性、价值覆盖、工作流选择、方法调度是 Controller 责任。
8. Workflow Pattern 与 Construction Operator 必须区分；“怎么工作”不等于“怎么造词”。
9. 工具箱不是线性“第一路径 → 备用路径”；探索可多方法 / 多 pattern 并行。
10. strongest / survivor 在一般 exploration 中只作 comparison，不得无意识成为生成模板。
11. 现实幸存结果不得直接回灌为“多生成这种词形”。
12. anti-collapse 排除默认 Controller-only；Generator Brief 默认正向表达。
13. generation / reviewer isolation 必须诚实；runtime 做不到时降级 claim，不伪装成真正 blind。
14. 现实撞名不等于强原型价值归零；可开启有限 Transformation Rescue。
15. 阶段性路线收敛不等于 Owner pause；仍有高信息价值空间时 Controller 自主继续。
16. 评价过程本身也可能被锚定；高价值决策中使用最小必要 blindness / independent first pass。
17. 不为了“完整”机械加载所有模块；只执行能显著降低当前关键不确定性的工作。
18. **模块清单不是流程清单。** Optional module 必须由 trigger / biggest unknown / expected decision value 激活。
19. **Reality negative claim 必须有查询合同。** held/promising 候选满足 Reality Screening Contract；Owner Exposure / finalist 前 freshness recheck。
20. Search Landscape 中的 reality crowding 与 intrinsic quality 分开；拥挤不等于语义/创意区域低质量。
21. Task experience 不能直接成为全局规则；跨任务演化走 Experience Registry + promotion contract。
22. 稳定方法变更必须有 regression，且保留 rollback / supersede 路径。

---

## 4. Naming Job 的最小核心状态

每个真实 Naming Job 至少建立：

- 被命名对象与长期尺度；
- mission / vision / philosophy 来源；
- success definition；
- Constraint Registry；
- Mission / Value Model；
- Name Job Model；
- Decision Criteria Roles；
- Search Landscape；
- Workflow Pattern Scheduler；
- Construction / Method Scheduler；
- search cadence；
- runtime capability / actual isolation；
- reality requirements；
- Owner preference signals；
- current biggest unknown / next action。

模板：

[`templates/naming-state-template.yaml`](templates/naming-state-template.yaml)

### 4.1 Constraint Registry

至少区分：

- `confirmed_hard_constraints`：Owner / task-source / legal / technical 明确来源；
- `owner_preferences`：偏好，不等于 gate；
- `controller_search_variables`：单词/多词、透明度、构词法、search mode、cadence 等可自主改变；
- `assumptions`：暂时假设，不得偷偷升级为边界。

无法回答“谁要求的、证据在哪里”时，默认不是 hard constraint。

### 4.2 Mission / Value Model

按需读取：

[`references/mission-value-model-and-method-scheduler.md`](references/mission-value-model-and-method-scheduler.md)

至少保留 actors、objects、transformations、relations / agency、temporal / causal structure、desired world、value claims、value relations / tensions、naming implications 与 value coverage。

### 4.3 Name Job + Decision Criteria

按需读取：

[`references/name-job-decision-and-research.md`](references/name-job-decision-and-research.md)

Name Job 回答：

> **名称具体负责完成什么？明确不负责什么？**

Decision Criteria 按 `gate / optimize / prefer / observe` 区分，不压成统一总分。

### 4.4 Preference 与 Expression

Owner preference 只在有重复证据时形成稳定 signal；early exploration 影响低、late convergence 可提高。

若“名字应该给人什么人格 / 气质 / 抽象度”会显著改变搜索，可按需启用 `expression_profile`；不要把它变成固定问卷。

---

## 5. Search Landscape：先验地图 + 在线学习

v0.4 恢复 G3 + G8 的核心组合：

> **prior map / white-space hypothesis + online observe / update**

`search_landscape` 至少可维护：region、semantic / character / construction position、collision prior、confidence、quality yield、reality crowding、information gain、sampling status、move/stay rationale。

规则：

- initial map 是先验，不冒充事实；
- reality observation 先进入 Controller / State Updater，再更新 region；
- Generator 不读取 raw survivor / Red / Yellow / collision identity；
- 重复高质量但 reality 失败 → 可提高 region crowding，不降低 intrinsic quality；
- under-sampled region 与高-information region 可获得更多预算。

---

## 6. Progressive Disclosure：按最大未知加载模块

不要问“还有哪个流程没跑”，要问：

> **当前哪个未知最可能改变候选空间、工作流、评价规则或下一步？**

常见触发：

- mission / value 被压平 → `model_values`
- 名称职责不清 / 承担过多 → `define_name_job` / `allocate_communication_load`
- criteria 混淆 → `classify_decision_criteria`
- 气质 / 抽象度不清 → `expression_profile`
- naming-space / white-space 不清 → `white_space_mapping`
- 多种 operator 仍使用相同薄弱材料 → `territory_research`
- creative window 过窄 / micro-probe 重复 → `divergence_burst`
- 发音 / 听写 / processing fluency 反复失败 → `linguistic_engineering`
- parent / umbrella 承载能力是关键未知 → `architecture_stress`
- 有高价值 stakeholder feedback → `feedback_refinement`
- 评审可能受排名 / Owner / reality 锚定 → `apply_decision_hygiene`
- 强候选陌生感不稳定 → `temporal_evaluation`
- 外部用户 / 专家证据可能改变决策 → `define_validation_contract`
- 候选进入 held/promising/finalist → `verify_reality`
- 强原型主要死于 reality → `open_rescue_branch`
- 已进入 rollout → `activation_governance`

所有 optional module 仍执行 Activation Budget：明确 `unknown / decision / cheaper_alternative / stop_condition`。

---

## 7. Workflow Pattern Scheduler 与 Construction Scheduler

### 7.1 Workflow Pattern Scheduler

决定**怎么组织当前认知与执行**。

最小 pattern library：

- `white_space_mapping`
- `territory_expansion`
- `divergence_burst`
- `creative_linguistic_parallel`
- `category_parallel`
- `architecture_stress`
- `feedback_refinement`
- `online_observe_update`
- `transformation_rescue`
- `validation_only`

这些是从 prior art / IA 实践提取的可组合机制，不是要求完整执行某家 agency SOP。

### 7.2 Construction / Operator Scheduler

构词与搜索工具箱：

[`references/word-formation-strategies.md`](references/word-formation-strategies.md)

维护 strategy 的 value targets、quality / distinctiveness / recoverability yield、reality crowding、information gain、concentration risk、attempts / last used、status。

### 7.3 Exploration / Exploitation

- 没有单一明显最优动作：选择差异化 pattern / operator portfolio；
- 跨批稳定强信号且 integrity 通过：有限 exploitation；
- mode collapse / low information gain：降权、cooldown、换 region / pattern；
- 降权不等于永久删除。

---

## 8. Search Cadence 也是可调变量

允许：

- `micro_probe`：1–5，回答一个明确未知；
- `portfolio_batch`：多方法小批；
- `divergence_burst`：短时扩大 creative window；
- `focused_exploitation`：有限深挖；
- `validation_only`：0 generation。

不把“小批”或“高容量”固定成统一最佳实践。Controller 必须记录 rationale 与 stop condition。

---

## 9. Runtime Adapter：方法与执行环境分离

详细规则见：

[`references/adaptive-system-evolution-and-runtime.md`](references/adaptive-system-evolution-and-runtime.md)

Controller 定义 logical role、allowed / forbidden context、input / output artifact、handoff；Runtime Adapter 根据实际能力映射到：

1. isolated worker / sub-agent；
2. fresh context；
3. shared context + sanitized brief / best-effort blindness。

记录至少：fresh context、isolated sub-agent、parallel worker、browser/shell/tool、persistent state I/O 能力。

Runtime 能力不足只降低执行保真度与证据置信度；不得为了看起来“隔离成功”而改写方法定义。

---

## 10. Generator Context 与信息隔离

### Controller-only

默认不进入 Generator Brief：

- incumbent / comparison-only 具体名称；
- task-local cooldown token / family；
- reality survivor shapes；
- Owner 对 incumbent 的反应；
- raw Experience Registry 中的 survivor / failed-name pattern；
- 长串 negative examples。

### Positive Generation Brief

优先只给：对象与尺度、Name Job focus、value target / naming implication、当前 region / 正向 material、workflow/operator 的必要生成合同、语言/记忆/尺度目标、有 provenance 的 hard constraints、本轮 question-to-answer。

### Post-generation Filter

Controller 检查 cooled family、incumbent similarity、strategy fidelity、hard constraints、其他 Controller-only exclusions。

Isolation level：

- `isolated_runtime`
- `fresh_context`
- `best_effort_same_context`
- `none`

只有前两类且有证据时，才可声称“Worker 未看到 X”。

---

## 11. Linguistic Engineering

当读写恢复、sound symbolism、phonotactic naturalness、letter structure / processing fluency 或跨语言风险成为主要未知时，可启用独立 `linguistic_engineering`。

若 runtime 允许，优先与 Creative Worker 并行；避免把完整语言评价提前压窄创意窗口。

---

## 12. Transformation Rescue

强候选若 intrinsic quality 与 value alignment 良好，主要死于 identity / namespace / domain 拥挤，可开启有限 rescue branch。

Rescue 必须记录 seed、trigger、allowed operators、attempt budget、exit conditions；每个变形结果作为新候选重新评价。Seed 不进入 general exploration brief。

---

## 13. 三层评价 + 决策卫生

### A. Intrinsic Quality

distinctiveness、pronounceability、spelling/dictation burden、memorability、semantic fit/room、scale fit、longevity、symbolic compression、cross-context use、architecture extensibility、visual feel、必要的语言文化风险。

### B. Value Alignment

aligned / tension / contradiction / neutral，与 semantic fit 分开。

### C. Reality Feasibility

exact / near identity、domain、public trademark-oriented signal、必要 namespace 与查询不确定性。

高价值评审时，先独立第一印象，再看 explanation / Owner / reality；intrinsic 与 feasibility 不互相偷换。

---

## 14. 现实验证合同

Reality identity / public trademark signal：

[`references/reality-screening-contract.md`](references/reality-screening-contract.md)

关键要求：

- `held / promising` 至少一次可审计 Level-1 screen；
- 单个空搜索结果不能写 `no_material_collision_found`；
- promising 以上按需补 near-name / spelling-recovery / 高邻接类别；
- Owner Exposure / finalist 前 freshness recheck；
- 显眼公开 active / registered trademark signal 必须记录，但不冒充正式法律 clearance；
- reality collision 只更新 feasibility。

Domain 使用 IA 既有验证方法；`unknown / error` 永远不能变成 `available`。Domain availability 不替代 identity / public-TM screening。

---

## 15. 核心循环

允许动作包括：

- `model_values`
- `define_name_job`
- `audit_constraints`
- `classify_decision_criteria`
- `allocate_communication_load`
- `define_expression_profile`
- `map` / `update_search_landscape`
- `territory_research`
- `schedule_workflow`
- `schedule_methods`
- `set_search_cadence`
- `adapt_runtime`
- `generate`
- `post_generation_filter`
- `linguistic_engineering`
- `evaluate_quality`
- `evaluate_value_alignment`
- `apply_decision_hygiene`
- `temporal_evaluation`
- `verify_reality`
- `define_validation_contract`
- `audit_naming_scope`
- `open_rescue_branch`
- `diagnose`
- `check_search_integrity`
- `update_state`
- `export_experience_candidate`
- `ask_owner`
- `stress_test`
- `activation_governance`
- `change_strategy`
- `stop`

```text
恢复 state
  ↓
Mission / Value + Constraint + Name Job / Criteria
  ↓
Search Landscape + Biggest Unknown
  ↓
Workflow Pattern Scheduler + Search Cadence
  ↓
Runtime Adapter
  ↓
Construction / Research / Generate / Validate / Rescue
  ↓
Intrinsic Quality + Value Alignment + Reality
  ↓
Diagnose + Update Job State
  ↺ Job-level adaptation

可泛化 experience candidate
  ↓
Cross-task Experience Registry
  ↓
Method Hypothesis + Counterevidence
  ↓
Regression / Live-fit Validation
  ↓
Promote / Revise / Reject / Supersede
  ↺ Method-level evolution
```

详细诊断：

[`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md)

---

## 16. 典型控制缺陷

至少能识别：

- `value_flattening`
- `mission_overcompression`
- `value_proxy_collapse`
- `name_job_ambiguity`
- `name_overloading`
- `criteria_role_confusion`
- `criteria_role_drift`
- `territory_material_starvation`
- `evaluation_anchoring`
- `premature_kill`
- `respondent_mismatch`
- `naming_scope_error`
- `semantic / morphological / construction_mode_collapse`
- `scheduler_monoculture`
- `workflow_monoculture`
- `workflow_operator_confusion`
- `method_underuse`
- `incumbent_anchoring`
- `rescue_overfit`
- `survivorship_feedback`
- `strategy_fidelity`
- `negative_constraint_priming`
- `isolation_overclaim`
- `runtime_fidelity_overclaim`
- `constraint_drift`
- `search_path_delegation`
- `owner_boundary_false_positive`
- `value_score_smuggling`
- `reality_screen_false_negative`
- `region_quality_reality_conflation`
- `cadence_lock_in`
- `premature_method_promotion`
- `preference_overfit`

先诊断，再优化；候选失败、region crowding、operator failure、workflow failure、runtime limitation、评价失败、现实验证失败必须区分。

---

## 17. Owner Interaction Gate

任何 `ask_owner` 前判断：

1. 是否改变 Owner / task-source 已确认目标或 hard constraint？
2. 是否只是内部 region、workflow pattern、method schedule、cadence、研究模块或预算？
3. 是否可逆、可测试、预算可承受？
4. 是否可以先并行 / 小批得到证据？

只有 `true_boundary_change / final_subjective_choice / unrecoverable_missing_goal_fact / budget-time decision` 才暂停。

`search_strategy / workflow_schedule / method_schedule / reversible_architecture_expansion / territory_research / transformation_rescue / decision_hygiene / runtime_mapping` 默认由 Controller 自主执行。

---

## 18. Method Evolution Outer Loop

跨任务 Registry：

[`evolution/method-experience-registry.yaml`](evolution/method-experience-registry.yaml)

每个 job 可输出 `experience_candidate`，但禁止直接因为一次结果修改稳定规则。

Promotion 默认需要：

- 至少 2 个独立 Naming Job 的一致机制证据；
- counterevidence 检查；
- regression；
- rollback / supersede 路径。

严重控制缺陷可使用例外：单个真实任务也可推动 provisional method fix，但必须满足：可复现/机制清楚、属于 control-layer defect、增加 regression、保留 rollback。

Registry 属于 Controller / evolution context，不进入 Generator context。

---

## 19. Regression 与版本纪律

行为回归：

- [`evals/README.md`](evals/README.md)
- [`evals/regression-cases.yaml`](evals/regression-cases.yaml)

Regression Evals 验证控制行为与方法完整性，不固定“正确名字”，也不恢复 G0–G8 benchmark。

版本原则：

- job-local parameter / state 变化：不改 Skill 版本；
- reference / pattern / router 的向后兼容增强：minor；
- 核心状态 / 控制架构 / method-evolution contract 改变：major/minor 按兼容性明确记录；
- 旧规则被替代时保留 supersede / rollback provenance。

---

## 20. 停止与 Owner-facing 输出

可以停止 Naming Job 的主要情况：

- 已有足够高质量、价值兼容、现实可推进候选进入 Owner 最终决策；
- 全局继续探索信息增益低，且已有候选满足目标；
- 关键验证被 runtime 阻塞；
- confirmed goals / hard constraints 自身矛盾；
- 预算 / 时间边界达到。

单个 region、operator、workflow pattern、single-token 路线、现实批次或 rescue branch 收敛都不是单独 stop 条件。

完整收敛时至少说明：Naming Job / constraints、Mission/Value/Name Job、Decision Criteria、主要 Search Landscape / workflow / operator 覆盖、实际 runtime isolation、2–5 个强候选（或为何尚无）、intrinsic/value/reality summary、主要风险与停止理由。

不要把内部 working pool、Registry 细节、未触发模块或完整 state 机械倾倒给 Owner。
