# 诊断与下一步决策规则 v0.3.1

本文件回答：**观察到了什么以后，Controller 下一步应该做什么？**

原则：候选失败、Name Job 定义失败、评价过程失败、搜索控制失败、现实可用性失败必须分开。先诊断，再改变策略。

详细 Mission / Value 与 Scheduler 规则见：

- [`mission-value-model-and-method-scheduler.md`](mission-value-model-and-method-scheduler.md)
- [`name-job-decision-and-research.md`](name-job-decision-and-research.md)

---

## 1. 诊断层级

### Candidate

- `quality_semantic`
- `quality_linguistic`
- `quality_scale`
- `quality_distinctiveness`
- `quality_architecture`
- `value_alignment_tension`
- `value_alignment_contradiction`
- `owner_fit`
- `reality_collision`
- `domain_unavailable`
- `reality_unknown`

### Mission / Value / Name Job

- `value_flattening`：使命被压成关键词，主体、agency、循环或长期目的消失；
- `mission_overcompression`：要求一个裸名表达全部使命；
- `value_proxy_collapse`：表面 proxy 被误当成完整 core value；
- `value_priority_invention / value_score_smuggling`：无证据发明排序或数值权重；
- `name_job_ambiguity`：不知道名称本身究竟负责什么；
- `name_overloading`：把 descriptor / narrative / architecture 能承担的信息全部压给名称；
- `naming_implication_confusion`：guardrail-only value 被误当成必须字面表达。

### Decision Model / Evaluation

- `criteria_role_confusion`：gate / optimize / prefer / observe 混为一谈；
- `criteria_role_drift`：弱偏好或搜索变量逐步升级为 gate；
- `evaluation_anchoring`：前人评价、Owner 反应、现实结果或解释污染独立判断；
- `premature_kill`：强但陌生候选在缺少必要时间 / 语境时被过早淘汰；
- `respondent_mismatch`：让不合适的受访者回答其无资格判断的问题；
- `naming_scope_error`：本不需要独立品牌名的对象被强行命名，或品牌层级判断错误。

### Search / Scheduler / Research Integrity

- `semantic_mode_collapse`
- `morphological_mode_collapse`
- `construction_mode_collapse`
- `scheduler_monoculture`
- `method_underuse`
- `territory_material_starvation`：方法很多，但真实材料来源持续贫乏，最终仍回到常见词根 / 套壳；
- `incumbent_anchoring`
- `rescue_overfit`
- `survivorship_feedback`
- `strategy_fidelity`
- `negative_constraint_priming`
- `isolation_overclaim`
- `constraint_drift`
- `search_path_delegation`
- `owner_boundary_false_positive`

---

## 2. 关键 if / then

### Mission / Value 被压平

如果使命有主体关系、rights / agency、循环或长期变化，但 state 只剩若干语义词：

→ `value_flattening`；回到 source，恢复结构，再建立 value claims / relations / naming implications。

### 一个名字被要求解释整个组织

如果候选反复因“没有表达所有价值”淘汰：

→ `mission_overcompression`；定义 Name Job，把非必要表达移到 `non_jobs` 或 communication load 的其他载体。

### 不知道名字到底要完成什么

如果 quality / semantic / architecture 标准互相冲突，而且无法说明哪个更重要：

→ `name_job_ambiguity`；先建立 `primary_jobs / secondary_jobs / non_jobs / tensions`，再继续生成。

### 名称承担过多传播任务

如果候选必须靠越来越复杂的字面结构才能同时表达 mission、业务、价值和架构：

→ `name_overloading`；启用 `communication_load_allocation`，把 descriptor / tagline / narrative / visual / architecture 能承担的内容分出去。

### Criteria 角色混乱

如果 `.org`、Owner preference、semantic fit、collision 等被混成总分，或弱偏好开始淘汰强候选：

→ `criteria_role_confusion / drift`；重新标记 `gate / optimize / prefer / observe` 与 source。

### 不确定该用哪个方法

如果存在多个合理方法且成本低：

→ Scheduler 选 3–5 个差异化 family 小批并行；不要问 Owner，也不要强选唯一方法。

### 工具很多但一直用一种

如果 recent rounds 长期只调用一个 family 且没有明确 exploitation 理由：

→ `scheduler_monoculture`；补不同 value target + construction family 对照。

### 明明有适配工具却没用

如果强名字主要死于 reality，但系统只会继续造全新名字：

→ `method_underuse`；检查 Transformation Rescue。

### 多方法仍反复出现相同词根 / 套壳

如果换了 construction family 仍回到相同语言材料：

→ `territory_material_starvation`；先做 `territory_research`，建立真实 material map，再由 Controller 选择材料进入 Generator Brief。

### 强名字主要死于现实占用

如果 intrinsic quality 强、value alignment 无明显冲突、主要失败来自 identity / domain / namespace：

→ 可开启 bounded Transformation Rescue。

Seed 只能进入 rescue branch；设置 operator、预算、退出条件；每个变形结果作为新候选重新评价。

### Rescue 变成无限近亲繁殖

如果超预算、near variants 越来越多、信息增益下降：

→ `rescue_overfit`；关闭 branch，回到 portfolio exploration。

### 评审受上下文污染

如果 reviewer 已先看到 Owner 喜恶、domain/collision、其他 reviewer 排名或长篇辩护：

→ `evaluation_anchoring`；对下一轮高价值判断启用 independent first pass / task-specific blindness。

### 强但陌生候选第一眼被杀

如果候选 intrinsic quality 强、问题主要是陌生感，而非明确读写或价值失败：

→ 不自动保留，也不自动淘汰；对少数 finalist-level 候选启用 `temporal_evaluation`，区分 first / informed / delayed signals。

### 外部研究问了错误的问题

如果只问“你喜欢哪个”，或让普通受访者判断战略、商标或最终 Owner fit：

→ `respondent_mismatch`；先定义 Validation Contract：respondent、问题、blindness、可推断范围。

### 对象可能不需要独立名称

如果 feature / component / internal tool 被当成 standalone brand，导致架构膨胀：

→ `naming_scope_error`；启用 `audit_naming_scope`，判断 standalone / sub-brand / descriptor / feature label / no separate name。

### Current route 信息增益下降

如果若干微循环只重复已知失败：

→ 先判断是 value gap、method gap、material gap、architecture gap 还是 Name Job / criteria 本身错误；再换动作，不默认继续生成。

### Incumbent 泄漏

一般 exploration 中 strongest 的词根 / 语义 / 声音不断回流：

→ `incumbent_anchoring`；comparison-only + Controller-only exclusions + positive Brief。

若确实值得围绕其原型深挖，只能另开 bounded rescue / exploitation，不得隐性泄漏。

### Negative prompt 反向锚定

Generator Brief 反复列“不要 X / 不要 Y”且近邻持续出现：

→ `negative_constraint_priming`；排除项移回 Controller-only，重写正向 Brief，必要时换 fresh / isolated runtime。

### 隔离夸大

同一聊天历史见过相关内容，却写“Generator 未看到”：

→ `isolation_overclaim`；改为 `best_effort_same_context`。真正 blind 才用 fresh / isolated runtime。

### 内部路径被甩给 Owner

如果所谓 Owner question 只是单词/多词、透明/不透明、方法 A/B/C、territory research 或 rescue 是否尝试：

→ `search_path_delegation / owner_boundary_false_positive`；Controller 自主试验或并行。

---

## 3. 下一动作优先级

每轮结束后优先问：

1. 目标 / Name Job /真实 boundary 是否不清？
2. 价值理解是否失真？
3. Decision Criteria 是否角色混乱？
4. 搜索 / Scheduler / isolation 是否失真？
5. 是否缺真实 material，而不是缺更多随机候选？
6. 是否有强原型值得 rescue？
7. 是否有候选需要 intrinsic / value / reality 的下一层证据？
8. 是否真的需要 external validation / temporal evaluation？
9. 剩余差异是否已经主要属于 Owner 最终长期认同？

不要按固定流程选择动作，只按当前最大未知和信息价值。

---

## 4. 状态更新最小要求

只更新本轮实际相关内容：

- trigger / observation；
- diagnosis + confidence；
- loaded module；
- state change；
- method allocation / rescue budget（如有）；
- generation isolation；
- relevant integrity checks；
- next action / why now。

未触发模块保持 inactive，不要为了模板完整而填充。
