---
name: adaptive-naming
description: 自适应品牌、组织、项目与产品命名。先建立真实目标、价值模型与边界，再由 Controller 动态调度多种命名方法，通过生成、评价、现实验证、诊断、变形救援与状态更新循环寻找高质量且现实可采用的名称。
version: 0.3.0
---

# Adaptive Naming Skill v0.3

## 1. 目标

本 Skill 不是固定流水线，也不是一次性名字生成器。它是一套 Naming Controller：理解任务目标与价值结构，维护真实边界和搜索状态，自主选择或并行调度方法，并根据观察不断改变下一步。

核心原则：

> **目标明确，边界稳定，路径开放，经验累积，方法进化。**

进一步的角色分工：

> **Owner 决定“要什么、真正不能变什么、最后喜欢什么”；Controller 决定“怎么理解、怎么找、先试什么、何时换路、哪些方法并行、哪些强原型值得救援”。**

本 Skill 负责“怎么思考与行动”；单次任务的地图、候选、价值覆盖、方法状态、证据和局部经验写入独立 state，不写回稳定 Skill。

---

## 2. 使用边界

适用于：

- organization / umbrella organization；
- brand / company；
- product / project / service；
- open-source project / public initiative；
- 需要长期扩展、现实可采用或多轮探索的 Naming Job。

不适用于变量、函数、普通文件名等纯工程标识。

正式商标法律意见不属于本 Skill 能力；现实筛查只能作为研究与决策支持。

---

## 3. 稳定不变量

运行中不得为了“得到结果”随意改变以下原则：

1. 先明确被命名对象、长期目标、真实硬约束和成功定义。
2. **使命 / 愿景先解构，再生成。** 不把长文本直接压成几个关键词就开始命名。
3. **价值观不等于字面语义。** 名字不需要压缩全部使命；可以只承载一个核心价值、关系、气质或长期身份，只要不与核心价值发生实质冲突。
4. **名称本身质量、价值对齐、现实可用性分开观察、分开记录。**
5. 域名可注册不代表名字好；现实撞名不自动代表创意质量差。
6. 不把多维质量或价值张力默认压成一个平均总分。
7. 可使用严格 Pareto dominance 淘汰明显被全面支配的候选。
8. 候选可以退出 active pool，但 provenance、诊断与学习信号不得丢失。
9. 单个失败不得直接升级为普遍规则；策略变化必须基于诊断和足够证据。
10. `unknown / error` 不得伪装成现实可用。
11. Owner preference 与一般命名质量分开；前期权重低，收敛期可提高，最终采用权属于 Owner。
12. 若已有上下文足够，不要求 Owner 重复回答；只有缺失信息会实质改变目标、真实边界或最终主观选择时才询问。
13. **搜索多样性、价值覆盖和方法调度是 Controller 责任。** 不依赖 Generator 自己维持。
14. **探索阶段 strongest / survivor 默认只作 comparison，不得无意识泄漏成生成模板。**
15. **现实幸存结果不得直接塑造同批或紧邻批次词形模板。**
16. 搜索完整性不能被“某个候选单独解释得通”掩盖；必须检查语义、价值代理、词形、构词来源和方法调用是否集中。
17. **Controller-only exclusions 不应反复写进 Generator Brief。** incumbent、冷却词根/家族、现实幸存形态等由 Controller 私下维护并在生成后过滤。
18. **Generator Brief 默认正向表达。** 用目标、价值方向、待探索空间、质量要求和真实硬约束指导生成，不用长串“不要 X / 不要 Y”。
19. **隔离强度必须诚实。** 同一聊天 / 同一模型历史上下文已见过某信息时，只能记为 `best_effort_same_context`，不得声称 Generator 从未见过。
20. **硬约束必须有来源。** 只有 Owner 明确表达、任务来源明确规定或不可回避的法律/技术条件，才能进入 confirmed hard constraints。
21. **搜索属性默认不是硬约束。** 单词/多词、现成/新造、透明/不透明、抽象度、构词法、语义区、search mode、批量大小等，默认属于 Controller search variables。
22. **不得把 Agent 自己的上一轮假设升级成 Owner 边界。** 无 provenance 时诊断 `constraint_drift`。
23. **内部路径选择不得转嫁给 Owner。** A/B/C 方法菜单通常应由 Controller 自主选择或并行试验。
24. **工具箱不是固定路径。** 不执行“第一方法失败后才允许第二方法”的线性流程；由 Method Scheduler 动态分配预算。
25. **探索默认允许多方法小批并行。** 不要求每轮只用一个构词方法，也不要求所有方法平均覆盖。
26. **现实撞名不等于强原型价值归零。** 若候选本体强而主要死于 namespace，可开启有限 transformation rescue。
27. **Transformation Rescue 是显式、有限、可审计的 exploitation exception。** Seed 只能进入救援分支，不得回流成主探索池隐性模板。
28. **价值排序必须有证据。** 不为了方便调度而凭空给价值打 1–10 分或制造 Owner 未表达的优先级。
29. **阶段性路线收敛不等于 Owner pause。** 仍有未被真实硬约束禁止的高信息价值搜索空间时，Controller 应自主继续。

---

## 4. 建立 Naming Job：目标、约束与 Mission / Value Model

首次执行或使命 / 愿景发生实质变化时，先建立 Naming Job。

至少恢复：

- 被命名对象与长期尺度；
- 主要受众与真实使用语境；
- mission / vision / philosophy；
- 成功定义；
- confirmed hard constraints；
- Owner 已知偏好；
- 必要现实条件，例如目标 TLD、商标 / 组织 / 项目 namespace。

### 4.1 Constraint Registry

至少区分：

1. `confirmed_hard_constraints`：有明确 provenance；
2. `owner_preferences`：偏好信号，不等于硬约束；
3. `controller_search_variables`：Agent 可自主改变；
4. `assumptions`：证据不足的暂时假设。

如果一个限制无法回答“谁明确要求、证据在哪里”，默认不是 hard constraint。

### 4.2 Mission / Value Model

按需读取：

[`references/mission-value-model-and-method-scheduler.md`](references/mission-value-model-and-method-scheduler.md)

不要只提取 `semantic_core`。至少拆解：

- actors / stakeholders；
- objects / resources；
- actions / transformations；
- relations / rights / agency；
- temporal / causal structure；
- desired world / end state；
- 有证据的 anti-values / non-goals；
- value claims、来源、priority 与 confidence；
- value relations / tensions；
- naming implications：direct / indirect / guardrail_only / optional_story / not_required。

如果 Mission 包含循环、反馈或主体关系，必须保留结构，不得把它压成几个同义词。

### 4.3 Value Coverage

维护搜索中的价值覆盖，而不只统计 semantic region 数量。

若大量候选围绕某个表面 proxy，而 core value 的另一部分长期低采样，诊断 `value_proxy_collapse`。

---

## 5. Method Scheduler：动态调度，而不是固定路径

按需读取同一 reference：

[`references/mission-value-model-and-method-scheduler.md`](references/mission-value-model-and-method-scheduler.md)

构词工具箱见：

[`references/word-formation-strategies.md`](references/word-formation-strategies.md)

Scheduler 维护每个活跃 strategy / family 的动态状态，例如：

- value targets；
- quality yield；
- distinctiveness yield；
- recoverability yield；
- reality crowding；
- recent information gain；
- concentration risk；
- attempts / last used；
- active / boosted / deprioritized / cooled / exploitation / rescue_only。

### Exploration

当没有单一明显最优方法时：

- 默认选择约 3–5 个差异足够大的方法 / family，小批并行；
- 同时补价值覆盖、构词结构和抽象度差异；
- 不为了公平平均预算；
- 若两条路线都合理且试验成本低，默认并行，而不是问 Owner。

### Exploitation

只在跨批稳定强信号、search-integrity 通过且存在明确问题时，把预算集中到 1–2 个方法，并设退出条件。

### Scheduler 更新

每批完成后更新**方法状态**，不仅更新候选状态。

- 高质量 + 高信息增益 + 覆盖价值缺口 + concentration 可控 → boost；
- 连续重复已知失败 / 现实拥挤高 / 错误尺度 / 低信息增益 → deprioritize；
- mode collapse / overuse → task-local cooldown；
- 条件变化或新组合出现 → 可重新激活。

降低优先级不等于永久删除方法。

---

## 6. Search Mode：Exploration 与 Exploitation

### Exploration

目标是扩大或修复真实搜索空间覆盖。

要求：

- comparison candidate 不进入通用生成提示；
- 检查 semantic coverage、value coverage、family concentration、method concentration；
- 同批先做名称本体 / value alignment，再做现实筛查；
- reality 结果只进入 Controller feasibility / crowding 诊断；
- task-local cooldown 主要由 post-generation filter 执行。

### Exploitation

目标是验证一个已有独立证据支持的强区域、方法、结构或 rescue seed。

必须记录：

- 为什么值得深挖；
- 本轮允许看到什么结构信息；
- 最大预算；
- 退出条件。

不能在 state 中写 exploration，实际却围绕一个 incumbent 无限生成同族变体。

---

## 7. 核心循环：选择当前信息价值最高的动作

允许动作包括：

- `model_values`：建立 / 修正 mission-value model；
- `audit_constraints`：核对硬约束 provenance；
- `map`：补充竞争 / 语义 / 价值 / 构词空间地图；
- `schedule_methods`：分配方法组合与预算；
- `generate`：按本轮 Brief 生成；
- `post_generation_filter`：执行 Controller-only exclusions；
- `evaluate_quality`：评价名称本身；
- `evaluate_value_alignment`：评价价值对齐；
- `verify_reality`：查询碰撞、域名或其他 namespace；
- `open_rescue_branch`：对强原型开启有限变形救援；
- `diagnose`：解释观察；
- `check_search_integrity`：检查覆盖、坍缩、策略忠实、隔离真实性、constraint drift、scheduler monoculture；
- `update_state`：更新地图、价值模型、方法状态、候选与偏好；
- `ask_owner`：只在 Owner Interaction Gate 通过后使用；
- `stress_test`：长期品牌 / 组织架构压力测试；
- `change_strategy`：换价值目标、语义区、构词法、名称架构、search mode 或预算；
- `stop`：达到停止条件。

```text
恢复完整状态
  ↓
Mission / Value Model + Constraint Audit
  ↓
搜索完整性 + Value Coverage + 最大未知
  ↓
Method Scheduler 分配方法 / 分支 / 预算
  ↓
Controller 形成正向 Generation Brief + 私有 exclusions
  ↓
Generator 生成
  ↓
Controller post-generation filter
  ↓
名称质量 + Value Alignment
  ↓
必要时 Reality Verification / Transformation Rescue
  ↓
诊断 + 更新方法状态 / 候选 / 覆盖
  ↓
自主继续 / 换方向 / Owner Gate / Stop
  ↺
```

批量大小不是固定配额。广泛 exploration 可用多个小批；focused exploitation 通常更小；当前最大未知不是缺候选时可以生成 0 个。

---

## 8. Generator Context 与隔离

### 8.1 Controller-only exclusions

控制器可读取完整 state，并私下维护：

- comparison-only / incumbent；
- task-local cooled families；
- reality survivor shapes；
- Owner 对具体 incumbent 的反应；
- post-generation similarity / family rules。

这些默认不进入 Generator Brief。

### 8.2 Positive Generation Brief

Generator 在 exploration 阶段只接收压缩后的正向 Brief，优先包括：

- 当前对象与长期尺度；
- 本轮选择的 value target / naming implication；
- 本轮正向搜索区域；
- Scheduler 选定的构词方向；
- 期望语言、口语、记忆、尺度与架构性质；
- 有 provenance 的硬约束；
- 本轮要回答的搜索问题。

默认不写入：

- incumbent / survivor 具体名称；
- successful root / suffix / sound pattern；
- cooldown token 清单；
- reality survivor shapes；
- Owner 对 incumbent 的喜欢程度；
- 长串 negative examples。

### 8.3 Post-generation filter

Generator 产出后，由 Controller 检查：

1. cooled family；
2. incumbent similarity；
3. strategy / scheduler fidelity；
4. 其他 Controller-only exclusions。

被挡回者是控制层违反，不自动算名称质量失败。

### 8.4 隔离等级

每轮记录：

- `isolated_runtime`；
- `fresh_context`；
- `best_effort_same_context`；
- `none`。

只有前两类且有证据时，才可说“Generator 未看到 X”。

---

## 9. Transformation Rescue：强原型现实失败后的有限变形

当候选名称本体强，但主要因为现实 identity / namespace / domain 拥挤失败时，不应自动丢弃其 construction value。

可开启 `transformation_rescue`，前提是：

- 本体质量强；
- 主要失败不是发音、拼写、尺度或价值冲突；
- 变形仍有机会形成独立身份；
- rescue 预算有限。

优先考虑低失真 operator：

- controlled spelling mutation；
- doubled / repeated letters；
- base word + single letter；
- meaningful prefix / suffix；
- clipping / telescoping；
- light blend / second semantic anchor；
- institutional pair / phrase expansion；
- 更大的 controlled coinage。

这不是固定流水线；明显不适配的 operator 可跳过。

每个变形结果必须作为**新候选重新评价**，不能继承 seed 的高质量。

重新检查：发音、听写恢复、视觉自然、proper-name identity、长期尺度、value alignment、exact/near collision、商标导向近似风险和目标域名。

若 rescue 开始损害 recoverability、产生 typo / 廉价科技词、near identity 仍高度集中、出现新 mode collapse 或信息增益下降，则停止。

---

## 10. 搜索完整性与典型控制缺陷

至少检查：

- `semantic_mode_collapse`；
- `value_proxy_collapse`；
- `mission_overcompression`；
- `morphological_mode_collapse`；
- `construction_mode_collapse`；
- `scheduler_monoculture`；
- `method_underuse`；
- `incumbent_anchoring`；
- `rescue_overfit`；
- `survivorship_feedback`；
- `strategy_fidelity`；
- `negative_constraint_priming`；
- `isolation_overclaim`；
- `constraint_drift`；
- `search_path_delegation`；
- `owner_boundary_false_positive`；
- `value_score_smuggling`。

详细 if / then 规则见：

[`references/diagnosis-and-next-action.md`](references/diagnosis-and-next-action.md)

原则：先诊断，再优化；不得从单个候选直接跳到永久策略结论。

---

## 11. 三层评价

### A. 名称本身质量

按任务需要观察，不默认求平均分：

- distinctiveness；
- pronounceability；
- spelling / dictation burden；
- memorability；
- semantic fit；
- semantic room；
- target scale fit；
- longevity；
- symbolic compression；
- cross-context use；
- architecture extensibility；
- visual feel；
- 必要时跨语言 / 文化联想。

### B. Value Alignment

与 `semantic_fit` 分开。

至少记录：

- aligned core values；
- tensions；
- contradictions；
- neutral values；
- confidence。

候选可以只直接承载一个 core value，而对其他价值保持 neutral。真正需要警惕的是与 core value 明显 contradiction。

### C. 现实可用性

单独记录：

- exact / near-name identity；
- 域名；
- 商标导向风险；
- 必要的平台 / handle / package namespace；
- 查询不确定性和证据来源。

现实碰撞只能更新 feasibility / crowding；除非同时暴露名称本身问题，否则不要反向改写 intrinsic quality。

---

## 12. 现实验证工具合同

Agent 必须使用当前 runtime 的真实工具，不凭记忆断言现实可用性。

### Reality identity

优先 exact-name 与 near-name 搜索，记录 query、对象类型、相关程度、source、observed_at、observation / uncertainty。

### Domain

调用 IA 统一方法：

[`Domain Availability Verification Method v0.1`](../../../03_Evolution/01_Research/01_Prior_Art/Naming_Methods/Execution/domain-availability-verification-method-v0.1.zh-CN.md)

顺序：registry authoritative RDAP / official availability → IANA bootstrap → registry RDDS/WHOIS → registrar machine/API → two-registrar corroboration → unresolved。

`unknown / error` 永远不能自动变成 `available`。

---

## 13. 状态与学习

每个 Naming Job 使用独立 state，模板：

[`templates/naming-state-template.yaml`](templates/naming-state-template.yaml)

每轮至少按需更新：

- mission / value model；
- value coverage；
- confirmed constraints / search variables；
- method scheduler state；
- rescue branches；
- 新观察与候选；
- reality evidence；
- generation isolation / post-filter；
- search-integrity diagnostics；
- biggest unknown；
- next action / why now。

### 任务内经验

可直接改变当前任务，例如当前区域拥挤、某方法过度产品化、某 family 需要 cooldown。

### 跨任务经验

新发现先记录 `experience_candidate`，不因一次成功自动写回核心 Skill。跨任务证据稳定后再 review / PR。

---

## 14. Owner Interaction Gate

任何 `ask_owner` 前必须回答：

1. 是否在改变 Owner / task-source 已确认目标或 hard constraint？
2. 还是只在改变方法、名称架构、构词路线、语义透明度、value sampling 或预算？
3. 路径变化是否可逆、可测试、预算可承受？
4. 多条合理路线是否可以先并行小批验证？

判定：

- `true_boundary_change` → 可以问 Owner；
- `final_subjective_choice` → 可以问 Owner；
- `missing_goal_fact` 且无法从现有来源恢复 → 可以问 Owner；
- `search_strategy` → 不得问 Owner；
- `reversible_architecture_expansion` → Controller 自主扩大或并行；
- `method_schedule` → Controller 自主执行；
- `transformation_rescue` → Controller 自主执行。

禁止把内部搜索菜单包装成 Owner boundary。

---

## 15. 长期架构压力测试

对强候选放进真实使用语境，而不只看裸名。umbrella organization 可测试：

```text
[Name]
[Name] Research
[Name] Commons
[Name] Tools
[Name] / [Project]
A project by [Name]
```

还应检查：名称呈现的组织身份是否与 mission / value model 长期兼容。

---

## 16. 停止条件

满足任一情况可停止当前循环：

- 已有足够高质量、价值兼容、现实可推进候选进入 Owner 最终决策；
- 当前继续探索的信息增益很低，且已有候选满足任务目标；
- 关键现实验证被环境阻塞，需要 handoff；
- confirmed goals / hard constraints 本身出现实质矛盾，需要 Owner；
- 预算 / 时间边界达到。

以下**不是**单独停止条件：

- 某一个 semantic region 收敛；
- 某一个构词方法低收益；
- single-token 路线收敛；
- 某一批现实碰撞率高；
- 一个 rescue branch 失败。

若仍存在未被 confirmed constraints 排除、且信息价值明显的 value / method / architecture 空间，Controller 应继续调度。

---

## 17. 最小输出合同

Owner-facing 输出只保留必要信息。完整收敛时至少说明：

- Naming Job / confirmed constraints；
- mission / value model 的关键结论；
- 已探索 value / semantic / method 空间；
- 当前 Method Scheduler 诊断；
- generation isolation 实际等级；
- 2–5 个强候选（或为何尚无）；
- intrinsic quality；
- value alignment；
- 独立 reality summary；
- 主要风险 / 未知；
- 下一步或停止理由。

如果暂停询问 Owner，必须说明 `owner_interaction_gate.classification` 与真实来源；不能只说“需要 Owner 决定路径”。

不要把内部海量 working pool 机械倾倒给 Owner。
