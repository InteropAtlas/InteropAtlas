# 诊断与下一步决策规则 v0.2.2

本文件回答一个核心问题：**观察到了什么以后，系统下一步应该干什么？**

原则：先区分事实、诊断和策略结论。不要从一个候选直接跳到全局规则；也不要因为每个候选单独都说得通，就忽略整个搜索过程已经发生偏置。Owner 只负责真实目标、真实边界与最终主观选择；内部搜索路径由 Controller 负责。

## 1. 四层诊断

### 候选级

回答：这个名字本身发生了什么？

常见类型：

- `quality_semantic`：语义不匹配、过窄、过直白、缺乏延展；
- `quality_linguistic`：发音、听写、拼写、节奏或视觉问题；
- `quality_scale`：像功能 / SaaS / 单一产品，不像长期组织或目标对象；
- `quality_distinctiveness`：名称本身过于普通或类别化；
- `quality_architecture`：放进品牌架构后弱、别扭或容易锁死；
- `owner_fit`：Owner 明确 pull / repel，但需与一般质量分开；
- `reality_collision`：现实已有强 exact / near identity；
- `domain_unavailable`：目标域名已有强注册证据；
- `reality_unknown`：查询阻塞或证据不足；
- `promising`：质量和现实信号都值得继续。

### 批次 / 区域级

回答：同一个问题是否重复出现？它是否集中在某个语义区域、构词方式、音形模式或品牌类别？

不要只计失败数量。观察：

- 同类问题出现次数；
- 是否来自同一策略；
- 是否有反例；
- 强候选是否也出现同一现实碰撞；
- 新信息是否仍在增加。

### 搜索完整性级

回答：Agent 是否还在探索真实的命名空间，还是已经围绕某个成功模式局部爬山？控制器声称的“隔离”是否与实际运行上下文一致？当前所谓“边界”是否真有来源？

常见类型：

- `semantic_mode_collapse`：近期候选过度集中于同一语义代理，任务其他重要语义持续低采样；
- `morphological_mode_collapse`：共享词根、前后缀、同族派生或声音骨架在 recent / active / promising 中异常集中；
- `construction_mode_collapse`：虽然表面词不同，但反复使用同一构词模板；
- `incumbent_anchoring`：strongest / survivor 候选从比较基准泄漏成隐性生成模板；
- `survivorship_feedback`：现实筛查的幸存形态反向塑造生成，导致“容易占用”被误学成“更好”；
- `strategy_fidelity`：声称探索的区域 / 策略与实际生成或入选候选不一致；
- `negative_constraint_priming`：为了避免旧模式，Generation Brief 反复点名 incumbent / cooldown / banned examples，反而维持或提高这些模式在生成上下文中的显著性；
- `isolation_overclaim`：同一模型/聊天历史已经见过完整信息，却把“本轮 Brief 未重复写入”表述成“Generator 未看到”；
- `constraint_drift`：Agent 自己选择的搜索属性被后续误写成 Owner / task hard constraint，但查不到明确 provenance；
- `search_path_delegation`：只属于内部路线选择的问题被包装成 A/B/C 菜单转交 Owner；
- `owner_boundary_false_positive`：阶段性路线收敛被误判为“需要 Owner 放宽边界”，但其实存在未被 confirmed constraints 禁止的可逆搜索空间。

这些诊断关注的是搜索过程，不等于相关候选本身质量失败。

### 策略级

只有当重复模式或搜索完整性问题足够清晰时，才调整：

- 继续深挖当前区域；
- 从 exploitation 退回 exploration；
- 保持语义、换构词法；
- 保持构词法、换语义区；
- 调整语言约束；
- 调整对象尺度要求；
- 调整名称架构，如单词 / 多词、透明 / 更轻语义；
- 设置 task-local family cooldown；
- 补地图 / 修复 semantic coverage；
- 生成正向 Generation Brief；
- 把具体 exclusions 留在 Controller-only 状态；
- 增加或收紧 post-generation filter；
- 切换 fresh / isolated runtime；
- 审计 constraint provenance；
- 自主并行两个高信息价值搜索分支；
- 先做现实验证而不是继续生成；
- 在 Owner Interaction Gate 通过后询问 Owner；
- 停止。

## 2. 典型 if / then 规则

### 单个强名字现实撞名

**如果**候选名称本身质量强，但出现明确现实 collision，  
**那么**退出该候选的现实推进路径，保留其质量评价；不要因此降低对应语义或构词策略的质量判断。

下一步优先判断：这是孤立碰撞，还是区域拥挤的一个样本？

### 同一区域多个强名字反复撞名

**如果**同一语义 / 构词区域连续产生多个质量较强但现实被占用的名字，  
**那么**提高该区域的 `crowding` 判断；优先尝试“保持好语义，改变构词方式”或探索相邻区域。

不要总结成“这个语义不好”。更合理的结论通常是“这个区域有吸引力，但明显/拥挤”。

### 可注册名字质量普遍低

**如果**一个区域域名很空，但名称本身质量持续低，  
**那么**不要把“空”当成优势。降低该区域的质量潜力判断，或重新寻找语义锚点。

### 多个候选发音 / 拼写困难

**如果**同一批或同一构词策略反复出现发音不确定、听写不可逆或拼写负担，  
**那么**收紧语言约束，再生成少量对照候选；必要时降低该构词策略优先级。

### 多个候选过于产品化

**如果**多个候选在其他维度不错，但持续像 app / SaaS / feature，而目标是 umbrella organization，  
**那么**提高 `scale / longevity / architecture` 约束；可换更制度化、抽象或长期语义区，而不是只换词尾。

### 某一区域连续产生强候选

**如果**某一区域产生多个在质量上非支配、现实也有推进空间的候选，  
**那么先做搜索完整性检查**，至少回答：

- 这些候选是否高度共享同一词根 / 语义家族 / 构词模板？
- 是否有 incumbent 作为隐性生成参照？
- 是否只是其他路线被现实筛查大量淘汰后留下的幸存者？
- 当前 search_mode 是否明确为 exploitation？

只有没有明显坍缩，或已明确进入有限 exploitation 时，才优先局部深挖。否则先恢复 exploration。

### 当前区域新信息越来越少

**如果**连续若干微循环只得到已知失败模式或近似候选，  
**那么**认为边际信息增益下降；换语义区、换构词策略、换名称架构、补充外部地图，或做搜索空间重置。

若这些替代路线没有违反 confirmed hard constraints，Controller 应自主执行，不需要 Owner 先选路线。

### 近期 / 强候选连续属于同一语义或形态家族

**如果**多个近期候选或多个 promising 候选共享高相似词根、前后缀、同义代理、声音骨架或构词模板，  
**那么**不要等 Owner 发现重复；主动执行 `check_search_integrity`。

若集中度不能由显式 exploitation 合理解释：

1. 诊断 `semantic/morphological/construction_mode_collapse`；
2. 比较长期目标各语义区域的实际采样覆盖；
3. 对当前家族设置 task-local cooldown，而不是建立永久黑名单；
4. 把具体 cooldown 信息留在 Controller-only 状态；
5. 补采样被忽略区域；
6. 重新生成正向 Generation Brief；
7. 由 post-generation filter 检查意外回流。

### Incumbent 泄漏为生成模板

**如果**新候选持续复用 strongest candidate 的词根、语义代理、声音或结构，而任务并未明确进入 exploitation，  
**那么**诊断 `incumbent_anchoring`。

下一步：

- 将 incumbent 标记为 `comparison_only`；
- 将其具体名称和成功词形留在 Controller-only exclusions；
- Generator Brief 只保留与任务目标有关的正向质量约束和待探索区域；
- 必要时暂时冷却同一语义 / 形态家族；
- 由 post-generation filter 拦截同族回流；
- 恢复其他区域探索。

### 负面提示本身开始成为锚点

**如果**为了避免模式复发，Generation Brief 持续列出“不要某候选 / 不要某词根 / 不要某同族”的具体名称或 token，而后续仍频繁出现这些模式、其近邻变体，或 post-generation filter 命中率升高，  
**那么**诊断 `negative_constraint_priming`。

下一步按顺序处理：

1. 从 Generator Brief 删除具体负面样本和 cooldown token 清单；
2. 将它们保留在 Controller-only exclusions；
3. 用正向目标、低采样区域、目标气质和构词方向重写 Brief；
4. 先生成，再由控制器做 post-generation filter；
5. 若同上下文仍持续回流，优先切换 fresh / isolated runtime，而不是继续增加更多负面提示。

不要把“更长的禁止列表”当作默认修复手段。

### 同一聊天中声称 Generator 从未看到旧候选

**如果**同一个聊天 / 同一个模型上下文在历史消息、state、recovery 或用户讨论中已经暴露过 incumbent / cooldown / reality survivor 信息，而当前执行记录写成“Generator 未看到这些信息”，  
**那么**诊断 `isolation_overclaim`。

下一步：

- 将隔离等级改为 `best_effort_same_context`；
- 事实表述改为“当前 Generation Brief 未再次暴露，但历史上下文可能已见过”；
- 若本轮目的需要真实 blind / isolated generation，切换 `fresh_context` 或 `isolated_runtime`；
- 不需要因此否定已生成候选，但不能把本轮当作强隔离证据。

### Post-generation filter 反复拦截大量候选

**如果**同一批或连续批次有较高比例候选命中 cooldown / incumbent similarity / strategy mismatch，  
**那么**不要把这些全部记成名称质量差；先诊断控制层问题。

优先检查：

- 当前 search frame 是否仍隐含旧锚点；
- runtime isolation 是否不足；
- 正向 Brief 是否过窄，导致模型只能回到旧模式；
- strategy fidelity 是否实际失败。

优先改 search frame 或 runtime isolation；只有真正属于任务硬约束的内容才需要直接加入 Generator Brief。

### 现实幸存结果反向影响创意生成

**如果**某类词形因域名、身份或商标空间较空而连续幸存，随后 Generator 开始更多生成同类词形，  
**那么**诊断 `survivorship_feedback`。

探索阶段应立即隔离：

- 同批质量评价先完成，再做现实筛查；
- reality 结果只进入控制器的 feasibility / crowding 诊断；
- 不向 Generator 暴露“哪个词根更容易有域名 / 更少撞名”的具体形态信息。

### 声称探索 A，实际又生成 X

**如果**本轮 brief 声称探索新语义区或新构词法，但实际候选仍回到旧家族，  
**那么**诊断 `strategy_fidelity`。

该轮不能作为“A 已经失败”的证据。下一步应：

- 重写更窄、更可检验的正向 Generation Brief；
- 必要时把生成与评价分开；
- 对实际输出做策略一致性检查后再进入 funnel。

### Agent 自己把搜索路线升级成硬约束

**如果**某个属性出现在当前 Brief / Generation Brief / 状态里，例如：

- 必须单词；
- 必须两词；
- 必须语义透明；
- 必须使用现成词；
- 必须使用新造词；
- 必须某个构词家族或抽象程度；

但在 Owner 明确输入、Issue/任务来源、法律/技术条件里找不到对应来源，  
**那么**诊断 `constraint_drift`。

下一步：

1. 标记该属性的 provenance 为 `unconfirmed / controller_assumption`；
2. 从 hard constraint 撤回；
3. 放入 `controller_search_variables`；
4. 回看它是否导致搜索空间被无意缩窄；
5. 若是，恢复未被真实边界禁止的路线；
6. 不因为“放宽这个假约束”询问 Owner。

原则：**没有来源的限制，不是 Owner 边界。**

### 当前路线到达 frontier，但存在其他未禁止路线

**如果**当前路线出现稳定的 trade-off / frontier，例如“更独特就更难拼、更易恢复就更拥挤”，而相邻搜索架构仍未充分测试，  
**那么**先检查这些相邻路线是否被 confirmed hard constraints 明确禁止。

- 若没有禁止：诊断为当前路线阶段性收敛，不是 Owner boundary；Controller 自主换路或并行探索。
- 若只有偏好而非硬约束：保留偏好权重，同时仍可小批探索以获得证据。
- 只有确实要违反 Owner / task-source 明确边界时，才进入 `true_boundary_change` 并询问 Owner。

### 把 A/B/AB/C 搜索菜单交给 Owner

**如果**Agent 想让 Owner 在多个内部搜索路线之间选择，而这些路线都不改变已确认目标和硬约束，  
**那么**诊断 `search_path_delegation`。

修复：

1. 取消 Owner 路径选择问题；
2. 按 expected information gain、可逆性、成本和覆盖增益排序；
3. 若两条路线都高价值且成本可控，默认并行小批探索；
4. 用实际质量/现实结果比较，再决定后续资源；
5. 只在出现强候选或真实边界冲突时再找 Owner。

不要把 Controller 的职责外包给 Owner。

### Owner Interaction Gate

任何 `ask_owner` 前必须先分类：

- `true_boundary_change`：需要改变 Owner / task-source 明确确认的硬约束；
- `final_subjective_choice`：少数强候选剩余差异主要是长期认同、气质、偏好；
- `missing_goal_fact`：缺失事实会改变成功定义且现有来源无法恢复；
- `search_strategy`：只改变寻找路径、名称架构、构词路线、语义透明度、抽象度、search mode；
- `reversible_architecture_expansion`：当前路线收敛，但存在未被硬约束禁止的新架构空间。

只有前三类允许 `ask_owner`。后二类必须自主执行。

### Exploration 与 Exploitation 切换

**从 exploration → exploitation** 只有在以下情况之一成立时才合理：

- 某一区域的强度在跨批、跨构词方法下重复出现；
- 搜索完整性检查未发现 incumbent 泄漏或家族坍缩；
- 深挖能回答一个明确且高信息价值的问题。

**从 exploitation → exploration** 在以下情况应触发：

- 局部变体越来越相似；
- 新信息增益下降；
- 强候选优势主要来自现实可占用，而非名称本身质量；
- 其他核心语义区域长期低采样；
- incumbent anchoring / mode collapse 被发现。

### 候选之间难以客观区分

**如果**2–3 个强候选在关键质量维度形成 Pareto 前沿，且剩余区别主要属于气质 / 感受 / 长期认同，  
**那么**把最小必要集合交给 Owner，而不是继续堆机器评分。

### Owner 一次强烈喜欢 / 讨厌

**如果**只出现一次偏好信号，  
**那么**记录但不要立即把它升级为稳定偏好。

**如果**相似偏好跨多个不同候选、不同轮次重复出现，  
**那么**提高其 preference confidence，并在后期收敛阶段提高影响力。

### 现实查询失败

**如果**域名 / collision 查询得到 `unknown` 或 `error`，  
**那么**记录查询历史，切换可用 adapter 或稍后重试；不得把失败解释为 `available / no collision`。

### 产生新的构词方法

**如果**Agent 在当前任务中发现 Skill 未列出的有效搜索策略，  
**那么**记录为 `experience_candidate`。当前任务可以继续使用，但不自动修改核心 Skill。

跨任务再次验证后，才提出版本升级。

## 3. 帕累托淘汰后的学习保留

候选 B 被 A 严格帕累托支配时：

- `active=false`；
- 记录 `dominated_by=A`；
- 保留 B 的 semantic region、construction strategy、quality observations、reality observations；
- 记录它具体在哪些维度被支配；
- 若 B 暴露了一个新失败模式，该模式仍进入诊断。

原则：

> **候选可以死，经验不能死。**

## 4. 下一动作选择优先级

每轮结束先检查约束来源和搜索完整性，再选择最能减少关键不确定性的动作：

1. **当前所谓硬约束都有明确 provenance 吗？** → 否：`audit_constraints / constraint_drift`
2. **准备问 Owner 吗？** → 先跑 `owner_interaction_gate`
3. **目标/真实硬边界本身不清楚吗？** → `ask_owner / refine_brief`
4. **搜索是否可能坍缩、被负面提示锚定或隔离表述不真实吗？** → `check_search_integrity`
5. **当前路线收敛但还有未被禁止的高价值路线吗？** → `change_strategy / parallel_exploration`
6. **不知道该去哪探索吗？** → `map`
7. **知道区域但缺样本吗？** → `generate`
8. **生成结果是否先要过 Controller-only exclusions？** → `post_generation_filter`
9. **有候选但不知道好不好吗？** → `evaluate_quality`
10. **质量强但不知道现实能不能用吗？** → `verify_reality`
11. **有很多观察但不知道意味着什么吗？** → `diagnose`
12. **剩余差异主要是 Owner 主观选择吗？** → `ask_owner`
13. **已有足够强且现实可推进的 finalist 吗？** → `stop / owner_decision`

不要因为“流程下一步本来应该是什么”选择动作，也不要因为当前路线阶段性收敛就自动问 Owner。只根据当前最大未知、信息价值、confirmed constraints 和搜索完整性选择。

## 5. 状态更新的最小要求

每次重要策略变化至少记录：

- `trigger`：哪些观察触发；
- `diagnosis`：如何解释；
- `confidence`：低 / 中 / 高；
- `state_change`：具体改了什么；
- `constraint_provenance_check`：涉及边界时，确认来源是什么；
- `search_variable_changes`：哪些只是 Controller 路线参数；
- `owner_interaction_gate`：若考虑 `ask_owner`，记录分类与结论；
- `search_mode_before / after`：如有模式切换；
- `generation_isolation_level`：isolated_runtime / fresh_context / best_effort_same_context / none；
- `controller_only_exclusions_changed`：是否新增/解除 cooldown 或 incumbent 排除；
- `post_generation_filter`：是否执行、命中多少、命中类型；
- `integrity_check`：是否发现家族集中、incumbent 泄漏、负面提示锚定、隔离夸大、constraint drift、path delegation、幸存者反馈或策略不忠实；
- `next_action`：下一步；
- `why_now`：为什么现在做这个动作比其他动作更有价值。

这样后续 Agent 才能区分“事实地图”“Owner 真边界”“Controller 搜索变量”“当时的推断”“控制器私有约束”“Generator 实际看到的上下文”和“搜索控制状态”。