---
name: adaptive-naming
description: 自适应品牌、组织、项目与产品命名。先建立目标、价值模型、名称职责与真实边界，再由 Controller 按当前最大未知动态调度研究、生成、评价、现实验证与救援模块。
version: 0.3.2
---

# Adaptive Naming Skill v0.3.2

## 1. 定位：薄核心，而不是巨型流程

本 Skill 是 Naming Controller，不是固定流水线，也不是要求每个任务把所有专业命名步骤跑一遍。

核心原则：

> **目标明确，边界稳定，路径开放，按需加载，经验累积，方法进化。**

角色分工：

> **Owner 决定“要什么、真正不能变什么、最后喜欢什么”；Controller 决定“怎么理解、怎么找、先试什么、何时换路、加载哪些模块、哪些方法并行、哪些强原型值得救援”。**

为了避免方法臃肿，核心 Skill 只保留稳定控制规则；复杂专业工作放入 references，由 Controller 根据当前最大未知按需读取。

---

## 2. 稳定不变量

运行中不得为了“得到结果”随意破坏：

1. 使命 / 愿景先结构化理解，不直接压成几个关键词。
2. **Value Model ≠ Name Job。** 组织珍视什么，不等于名称必须表达什么。
3. 名称不需要压缩完整使命；允许只承载一个核心价值、关系、气质或长期身份。
4. 名称本身质量、value alignment、现实可用性分开记录。
5. 硬约束必须有 provenance；搜索属性默认不是硬约束。
6. Owner preference 与一般质量分开；最终采用权属于 Owner。
7. 搜索多样性、价值覆盖、方法调度是 Controller 责任。
8. 工具箱不是线性“第一路径 → 备用路径”；探索可多方法小批并行。
9. strongest / survivor 在一般 exploration 中只作 comparison，不得无意识成为生成模板。
10. 现实幸存结果不得直接回灌为“多生成这种词形”。
11. anti-collapse 排除默认 Controller-only；Generator Brief 默认正向表达。
12. generation isolation 必须诚实：同上下文见过历史信息时只能记 `best_effort_same_context`。
13. 现实撞名不等于强原型价值归零；可开启有限 Transformation Rescue。
14. 阶段性路线收敛不等于 Owner pause；仍有高信息价值空间时 Controller 自主继续。
15. 评价过程本身也可能被锚定；在高价值决策中应使用最小必要 blindness / independent first pass。
16. 不为了“完整”机械加载所有模块；只执行能显著降低当前关键不确定性的工作。
17. **模块清单不是流程清单。** Optional module 必须由 trigger / biggest unknown / expected decision value 激活，而不是因为“存在这个模块”就执行。
18. Skill 结构修改若影响既有控制行为，应优先用 `evals/` 中对应 regression case 检查是否复发已知缺陷；Regression Evals 不等于重新启动方法 benchmark。

---

## 3. Naming Job 的最小核心状态

每个真实 Naming Job 至少建立：

- 被命名对象与长期尺度；
- mission / vision / philosophy 来源；
- success definition；
- Constraint Registry；
- Mission / Value Model；
- Name Job Model；
- Decision Criteria Roles；
- Method Scheduler；
- reality requirements；
- Owner preference signals；
- current biggest unknown / next action。

模板：

[`templates/naming-state-template.yaml`](templates/naming-state-template.yaml)

### 3.1 Constraint Registry

至少区分：

- `confirmed_hard_constraints`：Owner / task-source / legal / technical 明确来源；
- `owner_preferences`：偏好，不等于 gate；
- `controller_search_variables`：单词/多词、透明度、构词法、search mode 等可自主改变；
- `assumptions`：暂时假设，不得偷偷升级为边界。

无法回答“谁要求的、证据在哪里”时，默认不是 hard constraint。

### 3.2 Mission / Value Model

按需读取：

[`references/mission-value-model-and-method-scheduler.md`](references/mission-value-model-and-method-scheduler.md)

至少保留：actors、objects、transformations、relations / agency、temporal / causal structure、desired world、value claims、value relations / tensions、naming implications 与 value coverage。

### 3.3 Name Job + Decision Criteria

按需读取：

[`references/name-job-decision-and-research.md`](references/name-job-decision-and-research.md)

Name Job 回答：

> **名称具体负责完成什么？明确不负责什么？**

至少区分 `primary_jobs / secondary_jobs / non_jobs / tensions`。

Decision Criteria 不用统一总分，按角色区分：

- `gate`：不满足不能推进；
- `optimize`：主要优化目标；
- `prefer`：弱偏好 / tie-break；
- `observe`：记录但不直接淘汰。

不要把 `.org` gate、Owner 一次偏好、语义契合、现实碰撞混成一个“总分”。

---

## 4. Progressive Disclosure：按未知加载模块

不要问“还有哪个流程没跑”，要问：

> **当前哪个未知最可能改变候选空间、评价规则或下一步？**

以下模块只在触发时加载，详细合同见 [`references/name-job-decision-and-research.md`](references/name-job-decision-and-research.md)：

- 名称承担过多使命 → `allocate_communication_load`
- 评价标准互相打架 → `classify_decision_criteria`
- 词汇材料重复 / 枯竭 → `territory_research`
- 评审可能受前人、Owner、reality 结果锚定 → `apply_decision_hygiene`
- 强候选第一印象不稳定 → `temporal_evaluation`
- 要做用户 / 专家测试 → `define_validation_contract`
- 不确定对象是否值得独立命名 → `audit_naming_scope`
- 已进入 rebrand / rollout / governance → `activation_governance`

未触发模块不得变成工作量配额。

### 4.1 Module Routing Contract

Controller 每次准备加载 reference / optional module 前，先根据**当前症状与最大未知**路由，而不是凭记忆随意挑模块。

| 当前症状 / 最大未知 | 优先动作 | 读取 | 预期 artifact |
| --- | --- | --- | --- |
| mission / vision 被压成关键词；agency、循环、价值关系不清 | `model_values` | `mission-value-model-and-method-scheduler.md` | Mission / Value Model + value coverage |
| 不清楚“名称本身到底负责什么”；一个名字承担过多使命 | `define_name_job` / `allocate_communication_load` | `name-job-decision-and-research.md` | Name Job + optional communication-load allocation |
| gate / optimize / prefer / observe 混淆或发生 criteria drift | `classify_decision_criteria` | `name-job-decision-and-research.md` | Decision Criteria roles + provenance |
| 不知道下一轮该用哪些方法 / 是否并行 | `schedule_methods` | `mission-value-model-and-method-scheduler.md` + 必要时 `word-formation-strategies.md` | method portfolio + budget + question-to-answer |
| 已知 value / method，但缺构词 operator 或变形手段 | `generate` / `open_rescue_branch` | `word-formation-strategies.md` | selected strategy / operator contract |
| 多种构词方式仍反复使用同一薄弱词汇材料 | `territory_research` | `name-job-decision-and-research.md` | material map + selected positive material |
| 已观察到重复失败，但不确定它属于候选、方法、搜索控制还是评价过程 | `diagnose` | `diagnosis-and-next-action.md` | diagnosis + state change + next action |
| shortlist 价值高且 reviewer 可能看到排名、Owner reaction 或 reality 结果 | `apply_decision_hygiene` | `name-job-decision-and-research.md` | reviewer blindness / independent-pass contract |
| 强候选主要因陌生感、第一印象或记忆不确定 | `temporal_evaluation` | `name-job-decision-and-research.md` | raw / informed / delayed observations |
| 外部用户 / 专家证据可能改变具体决策 | `define_validation_contract` | `name-job-decision-and-research.md` | respondent + question + admissible-inference contract |
| 已选 finalist，需要迁移、rollout、未来命名治理 | `activation_governance` | `name-job-decision-and-research.md` | activation / governance handoff |

Reality / domain verification 属于工具合同：只有候选达到相应 reality gate 时调用，不因加载其他 reference 自动执行。

### 4.2 Module Activation Budget

任何非核心模块启动前至少能回答：

1. `unknown`：现在缺的具体信息是什么？
2. `decision`：这个模块的输出可能改变什么决策？
3. `cheaper_alternative`：有没有更轻量的动作能回答同一问题？
4. `stop_condition`：获得什么信息后立即退出模块？

如果无法说明预期 decision value，模块保持 inactive。

### 4.3 Routing precedence

当多个模块同时看似可用时，优先：

1. 修复会污染后续所有步骤的上游问题：constraint / Mission-Value / Name Job / Criteria；
2. 再解决当前最大搜索未知：Scheduler / Territory / Generation；
3. 再做候选评价、Reality、Validation；
4. Activation / Governance 只在选定结果后运行。

不要因为某一批候选弱就直接启动所有研究模块；先诊断失败来自**材料、构词、Name Job、criteria 还是 reality**。

---

## 5. Method Scheduler：动态方法组合

构词与搜索工具箱：

[`references/word-formation-strategies.md`](references/word-formation-strategies.md)

Scheduler 维护每个活跃 strategy / family 的：

- value targets；
- quality / distinctiveness / recoverability yield；
- reality crowding；
- recent information gain；
- concentration risk；
- attempts / last used；
- status：active / boosted / deprioritized / cooled / exploitation / rescue_only。

### Exploration

没有明显单一最优动作时：

- 默认选约 3–5 个差异足够大的方法 / family 小批并行；
- 同时补 value coverage、构词结构或抽象度差异；
- 不要求平均预算；
- 两条路线都合理且试验成本低时，先并行，不问 Owner。

### Exploitation

只有跨批稳定强信号、search-integrity 通过、且深挖能回答明确问题时，才集中 1–2 个方法，并设预算与退出条件。

### Scheduler 更新

- 高质量 + 高信息增益 + 覆盖缺口 + concentration 可控 → boost；
- 重复已知失败 / 高 crowding / 错误尺度 / 低信息增益 → deprioritize；
- mode collapse / overuse → task-local cooldown；
- 条件变化 → 可重新激活。

降权不等于永久删除。

---

## 6. Territory Research：先找材料，不一定先造名字

若多个方法仍反复落回相同常见词根、品牌套壳或语义 proxy，Controller 可以执行 `territory_research`。

目标不是搜索现成候选，而是从科学、自然、工艺、历史、制度、艺术、空间、语言学等真实领域建立 material map：concepts、verbs、objects、structural analogies、metaphors、etymological material。

Research 输出与 Generator 输入分离；Controller 只把选中的正向材料压缩进 Brief。

---

## 7. Generator Context 与隔离

### 7.1 Controller-only

默认不进入 Generator Brief：

- incumbent / comparison-only 具体名称；
- task-local cooldown token / family；
- reality survivor shapes；
- Owner 对 incumbent 的反应；
- 长串 negative examples。

### 7.2 Positive Generation Brief

优先只给：

- 当前对象与长期尺度；
- 本轮 Name Job focus；
- 选定 value target / naming implication；
- Scheduler 选定的构词 / material direction；
- 期望语言、口语、记忆、尺度与架构性质；
- 有 provenance 的 hard constraints；
- 本轮要回答的搜索问题。

### 7.3 Post-generation filter

Controller 检查：cooled family、incumbent similarity、strategy / scheduler fidelity 与其他私有 exclusions。

被挡回是控制层违反，不自动算名称质量失败。

### 7.4 Isolation level

记录：`isolated_runtime / fresh_context / best_effort_same_context / none`。

只有前两类且有证据时，才可声称“Generator 未看到 X”。

---

## 8. Transformation Rescue

强候选若 intrinsic quality 与 value alignment 良好，主要死于 identity / namespace / domain 拥挤，可开启**有限 rescue branch**，而不是把原型价值全部丢弃。

可调用低失真 operator：

- controlled spelling mutation；
- doubled / repeated letters；
- base + single letter；
- meaningful affix；
- clipping / telescoping；
- light blend；
- institutional pair / phrase；
- 必要时更大的 controlled coinage。

Rescue 是显式 exploitation exception：必须记录 seed、trigger、allowed operators、attempt budget、exit conditions。

每个变形结果是新候选，重新检查读写恢复、自然度、长期尺度、value alignment、near identity、商标导向风险与域名。

---

## 9. 三层评价 + 决策卫生

### A. Intrinsic Quality

按任务需要观察：distinctiveness、pronounceability、spelling / dictation burden、memorability、semantic fit / room、scale fit、longevity、symbolic compression、cross-context use、architecture extensibility、visual feel、必要的跨语言 / 文化风险。

### B. Value Alignment

与 semantic fit 分开记录 aligned / tension / contradiction / neutral values，不默认压成总分。

### C. Reality Feasibility

单独记录 exact / near identity、domain、trademark-oriented risk、必要 namespace 与查询不确定性。

### Decision Hygiene

高价值评审时按需执行：

- 先独立第一印象，再看他人解释 / Owner reaction / reality result；
- intrinsic reviewer 不看 domain / collision；
- reality reviewer 不用“我们喜欢它”作证据；
- Owner exposure 区分 `raw_affect` 与 `informed_affect`；
- 对少数强而陌生的候选，可按需记录 delayed recall / delayed affect。

---

## 10. 现实验证合同

现实可用性必须使用当前 runtime 的真实工具，不凭记忆断言。

Reality identity 优先 exact + near-name，记录 query、对象类型、相关程度、source、observed_at、observation / uncertainty。

Domain 使用 IA 方法：

[`Domain Availability Verification Method v0.1`](../../../03_Evolution/01_Research/01_Prior_Art/Naming_Methods/Execution/domain-availability-verification-method-v0.1.zh-CN.md)

`unknown / error` 永远不能变成 `available`。

若做外部用户 / 专家研究，先定义 Validation Contract；不要简单把“你喜欢哪个”当成证据。

---

## 11. 核心循环

允许动作包括：

- `model_values`
- `define_name_job`
- `audit_constraints`
- `classify_decision_criteria`
- `allocate_communication_load`
- `map`
- `territory_research`
- `schedule_methods`
- `generate`
- `post_generation_filter`
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
判断当前最大未知
  ↓
Module Routing Contract + Activation Budget
  ↓
Value/Search Integrity + Method Scheduler
  ↓
Research / Generate / Rescue
  ↓
Intrinsic Quality + Value Alignment
  ↓
Reality / Validation（需要时）
  ↓
Diagnose + Update State
  ↓
自主继续 / Owner Gate / Stop
  ↺
```

详细诊断规则：

[`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md)

---

## 12. 典型控制缺陷

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
- `method_underuse`
- `incumbent_anchoring`
- `rescue_overfit`
- `survivorship_feedback`
- `strategy_fidelity`
- `negative_constraint_priming`
- `isolation_overclaim`
- `constraint_drift`
- `search_path_delegation`
- `owner_boundary_false_positive`
- `value_score_smuggling`

先诊断，再优化；候选失败、方法失败、搜索控制失败、评价过程失败必须区分。

---

## 13. Owner Interaction Gate

任何 `ask_owner` 前先判断：

1. 是否改变 Owner / task-source 已确认目标或 hard constraint？
2. 是否只是内部方法、名称架构、研究模块、构词路线、value sampling 或预算？
3. 是否可逆、可测试、预算可承受？
4. 是否可以先并行小批得到证据？

只有 `true_boundary_change / final_subjective_choice / unrecoverable_missing_goal_fact / budget-time decision` 等真正 Owner 问题才暂停。

`search_strategy / method_schedule / reversible_architecture_expansion / territory_research / transformation_rescue / decision_hygiene` 默认由 Controller 自主执行。

---

## 14. 状态、学习、回归与停止

每轮只更新**本轮实际使用的模块和观察**，不要为了模板完整填空。

任务内经验可直接改变当前 search；跨任务经验先记 `experience_candidate`，不因一次成功自动升级稳定 Skill。

行为回归测试见：

- [`evals/README.md`](evals/README.md)
- [`evals/regression-cases.yaml`](evals/regression-cases.yaml)

Regression Evals 只验证控制行为与方法完整性，不以“生成哪个名字”作为固定答案，也不恢复已停止的 G0–G8 benchmark。

可以停止的主要情况：

- 已有足够高质量、价值兼容、现实可推进候选进入 Owner 最终决策；
- 全局继续探索的信息增益低，且已有候选满足目标；
- 关键验证被 runtime 阻塞；
- confirmed goals / hard constraints 自身矛盾；
- 预算 / 时间边界达到。

单个 semantic region、构词方法、single-token 路线、现实批次或 rescue branch 收敛都**不是**单独 stop 条件。

---

## 15. Owner-facing 最小输出

完整收敛时至少说明：

- Naming Job / confirmed constraints；
- Mission / Value Model 与 Name Job 的关键结论；
- 主要 Decision Criteria roles；
- 已探索 value / semantic / method 空间；
- Method Scheduler / search-integrity 诊断；
- generation isolation 实际等级；
- 2–5 个强候选（或为何尚无）；
- intrinsic quality / value alignment / reality summary；
- 主要风险 / 未知；
- 下一步或停止理由。

暂停询问 Owner 时必须说明 Owner Gate classification 与真实来源，不能只说“需要 Owner 决定路径”。

不要把内部 working pool、未触发模块或完整 state 机械倾倒给 Owner。
