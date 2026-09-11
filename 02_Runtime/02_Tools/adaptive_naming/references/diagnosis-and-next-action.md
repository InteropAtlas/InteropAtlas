# 诊断与下一步决策规则 v0.3

本文件回答：**观察到了什么以后，Controller 下一步应该做什么？**

原则：先区分事实、诊断、策略结论。Owner 负责真实目标、真实边界和最终主观选择；Mission / Value Model、方法调度、路径切换、变形救援和内部预算由 Controller 负责。

---

## 1. 五层诊断

### 1.1 候选级

回答：这个名字本身发生了什么？

常见类型：

- `quality_semantic`：语义不匹配、过窄、过直白或延展不足；
- `quality_linguistic`：发音、听写、拼写、节奏、视觉问题；
- `quality_scale`：像功能 / SaaS / 单一产品，不像目标对象；
- `quality_distinctiveness`：过于普通或类别化；
- `quality_architecture`：品牌架构中弱或锁死；
- `value_alignment_tension`：与一个或多个 core value 存在张力；
- `value_alignment_contradiction`：与 core value 明显冲突；
- `owner_fit`：Owner pull / repel，与一般质量分开；
- `reality_collision`：现实 exact / near identity；
- `domain_unavailable`：目标域名已有强注册证据；
- `reality_unknown`：查询阻塞或证据不足；
- `promising`：值得继续推进。

### 1.2 批次 / 区域级

回答：同一问题是否重复出现？集中在哪个 value target、semantic region、方法 family、音形或品牌类别？

观察：

- 同类问题出现次数；
- 是否来自同一 strategy；
- 是否有反例；
- 强候选是否重复现实撞名；
- 新信息是否仍增加；
- value coverage 是否真实扩大。

### 1.3 Mission / Value Model 级

回答：Agent 是否真的理解使命，还是只抓了表面关键词？

常见类型：

- `value_flattening`：使命被压成若干关键词，主体关系、agency、循环或目的消失；
- `mission_overcompression`：要求单个名字承担完整使命 / 全部价值；
- `value_proxy_collapse`：某个表面 proxy 被误当成完整 core value；
- `value_priority_invention`：没有证据却自行发明价值优先级；
- `value_score_smuggling`：把不确定价值关系偷偷转成统一数值权重；
- `value_coverage_gap`：core value 长期低采样；
- `naming_implication_confusion`：把 guardrail-only / indirect value 错当成必须字面表达。

### 1.4 搜索完整性 / 调度级

回答：Agent 是否还在真实探索，还是被单一模式、单一方法或错误控制逻辑锁住？

常见类型：

- `semantic_mode_collapse`；
- `morphological_mode_collapse`；
- `construction_mode_collapse`；
- `scheduler_monoculture`：工具箱很多，但长期只调用一个方法 family；
- `method_underuse`：当前失败模式明确适配某方法，却长期未调用；
- `incumbent_anchoring`；
- `rescue_overfit`：Transformation Rescue 超出有限预算，变成新的 incumbent anchoring；
- `survivorship_feedback`；
- `strategy_fidelity`；
- `negative_constraint_priming`；
- `isolation_overclaim`；
- `constraint_drift`；
- `search_path_delegation`；
- `owner_boundary_false_positive`。

这些诊断关注搜索过程，不等于候选本身质量失败。

### 1.5 策略级

只有在重复证据足够时才改变：

- 修 mission / value model；
- 补 value coverage；
- 调整 method portfolio / budget；
- 并行多个方法小批探索；
- 从 exploitation 退回 exploration；
- 换 semantic region / construction family / name architecture；
- 设置或解除 task-local cooldown；
- 开启或终止 transformation rescue；
- 切换 fresh / isolated runtime；
- 审计 constraint provenance；
- 先 reality verification；
- 通过 Owner Interaction Gate 后询问 Owner；
- stop。

---

## 2. Mission / Value Model if / then

### 使命被压成几个关键词

**如果** Mission / Vision 中存在主体关系、循环、agency、rights、长期变化，但 state 只剩几个 `semantic_core` 词，  
**那么**诊断 `value_flattening`。

下一步：

1. 回到 source；
2. 恢复 actors / objects / transformations / relations / temporal structure / desired world；
3. 建立 value claims 与 evidence type；
4. 再决定哪些 value 应 direct / indirect / guardrail-only 表达。

### 一个名字被要求解释完整使命

**如果**候选长期因为“没有同时表达全部愿景”被淘汰，或 Generator Brief 要求一个裸名压缩完整 mission loop，  
**那么**诊断 `mission_overcompression`。

下一步：

- 每轮只选少量 value target / structural hint；
- 其余 core values 降为 alignment guardrail；
- 允许品牌意义后置积累；
- 重新检查此前被过度淘汰的路线是否值得恢复。

### 表面 proxy 替代了真正价值

**如果**近期候选大量围绕某个容易生成的表面概念，而该概念只代表 core value 的一个 proxy，  
**那么**诊断 `value_proxy_collapse`。

例如“多 / 汇聚 / 循环”可能只是 proxy，不自动等于 individual agency、commons rights 或 creation。

下一步：

- 标出 proxy 与真实 value 的差异；
- 降低 proxy 采样；
- 补低覆盖 core value；
- 不建立永久 blacklist。

### Agent 自己发明价值排序

**如果** state 出现“V1 最高、V2 次之”或 1–10 权重，但 mission / Owner 没有相应证据，  
**那么**诊断 `value_priority_invention` / `value_score_smuggling`。

下一步：

- 撤回无来源排序；
- 改为 core / high / supporting / optional / unknown；
- 为每项 priority 记录 source / confidence；
- tension 保留为 tension，不强行平均。

### Core value 长期低覆盖

**如果** value coverage 显示某 core value 长期 `low`，而其他 proxy 已高采样，  
**那么**优先让 Method Scheduler 给该 value target 分配多个差异化方法小批，而不是继续旧区域。

---

## 3. Method Scheduler if / then

### 不确定哪个方法最好

**如果**存在 2 个以上合理方法，成本低且都不违反 confirmed constraints，  
**那么**默认选择 3–5 个差异化 strategy / family 小批并行，而不是问 Owner，也不是硬选唯一方法。

### 某方法连续高收益

**如果**某 strategy 跨批出现：

- quality yield 高；
- value coverage 有增益；
- information gain 高；
- concentration risk 可控；

**那么**可 `boost` 并进入有限 exploitation。

必须设退出条件；现实可占用单独不足以证明应 boost。

### 某方法连续低收益

**如果**连续若干批只重复已知失败、错误尺度、现实拥挤或低信息增益，  
**那么**降权为 `deprioritized` 或短期 `cooled`。

不要永久删除；当任务条件或组合方式改变时允许 reopen。

### 工具箱很多但一直用同一方法

**如果** state 中 construction toolbox 丰富，但 recent rounds 长期只调用一个 family，且无明确 exploitation 理由，  
**那么**诊断 `scheduler_monoculture`。

下一步：

- 检查哪些 methods 从未被调度；
- 根据当前最大未知选择差异化方法组合；
- 至少补一个 semantic/value 维度和一个 construction 维度的对照。

### 明明有适配工具却没有调用

**如果**失败模式已经明确适配工具箱中的某方法，例如“名字本体强但现实占用”却长期只生成全新名字，从未测试低失真变形，  
**那么**诊断 `method_underuse`。

下一步应优先调用对应 method / rescue branch，而不是继续同类生成。

### 方法间表现相近

**如果**多个方法都给出中等但不同信息，  
**那么**保持 portfolio，不急于选 winner。继续少量并行直到差异足以改变预算。

---

## 4. Transformation Rescue if / then

### 强名字主要死于现实占用

**如果**候选 intrinsic quality 强、value alignment 无明显冲突，主要失败来自 exact / near identity、domain 或 namespace 拥挤，  
**那么**不要把 seed 的 construction value 一并丢弃。

检查是否开启 `transformation_rescue`。

优先低失真 operator：

1. controlled spelling mutation；
2. doubled / repeated letter；
3. base + single letter；
4. meaningful affix；
5. clipping / telescoping；
6. light blend / second semantic anchor；
7. institutional pair / phrase expansion；
8. larger controlled coinage。

不要求依次全部执行。

### Rescue 是否违反 anti-anchoring？

Transformation Rescue 是显式 exploitation exception，不是隐性泄漏。

必须记录：

- seed id；
- trigger；
- allowed operators；
- attempt budget；
- exit conditions。

Seed 只进入 rescue branch，不进入 general exploration brief。

### 变形结果看起来只是 typo

**如果**变形明显降低 dictation recovery、视觉自然、长期机构感或增加“廉价科技词”感，  
**那么**该 operator 失败，不代表 seed 全部 rescue 空间失败。

切换另一个低失真 operator；连续失败后再关闭 branch。

### 变形后仍 near collision

**如果**多个变形仍与原现实 identity 高度近似，尤其可能触发商标近似风险，  
**那么**停止只做表面字母变化；要么增加 semantic/structural distance，要么关闭 rescue。

### Rescue 越来越像 seed family 批量繁殖

**如果**超出明确预算，或新候选只是越来越多相邻变体且信息增益下降，  
**那么**诊断 `rescue_overfit`，关闭 branch，回到 portfolio exploration。

---

## 5. 传统候选 / 搜索完整性规则

### 单个强名字现实撞名

保留 intrinsic quality 与 learning；更新 feasibility。判断是孤立碰撞还是区域拥挤，并检查 rescue trigger。

### 同一区域多个强名字反复撞名

提高 `reality_crowding`；尝试保持价值 / 语义但换 construction，或换相邻 region。不要总结成“这个价值不好”。

### 可注册名字质量普遍低

不能把“空”当成质量优势；降低该 method / region 的 quality potential 或换语义锚点。

### 多个候选发音 / 拼写困难

收紧 recoverability target，并让 Scheduler 降低导致问题的 strategy 权重。

### 多个候选过于产品化

提高 scale / longevity / architecture 要求；换更适合长期母组织的结构，而不是只换词尾。

### 近期 / 强候选属于同一 semantic / morphological / construction family

执行 `check_search_integrity`。若不是显式 exploitation：

1. 诊断相应 mode collapse；
2. 加 task-local cooldown；
3. 具体 cooldown 留在 Controller-only；
4. 补低覆盖 value / region；
5. 重新调度 methods；
6. post-generation filter 检查回流。

### Incumbent 泄漏为通用模板

诊断 `incumbent_anchoring`：

- 标 `comparison_only`；
- 具体名称 / 成功形态留在 Controller-only；
- general Generator Brief 只看正向目标；
- 若值得 rescue，另开显式 bounded rescue branch，而不是让 seed 泄漏到主池。

### 负面提示成为锚点

诊断 `negative_constraint_priming`：删具体 negative examples，保留 Controller-only exclusions，用正向 Brief + post-filter；必要时换 fresh / isolated runtime。

### 隔离夸大

同一聊天历史已见过相关信息时，若写成“Generator 未看到”，诊断 `isolation_overclaim`，改成 `best_effort_same_context`。需要真实 blind 时换 fresh / isolated runtime。

### Post-generation filter 高命中

先检查 context contamination、Brief 过窄、scheduler monoculture、strategy fidelity；不要把所有命中记成名称质量失败。

### Survivorship feedback

现实 survivor 只更新 feasibility / crowding，不直接提示 Generator“多生成这种词形”。

### 声称探索 A，实际又生成 X

诊断 `strategy_fidelity`。该轮不能证明 A 失败；重写 Brief / 重调方法后再验证。

---

## 6. Constraint / Owner 规则

### Search variable 被误当 Owner boundary

**如果**单词/多词、透明/不透明、现成/新造、构词法、抽象度等只来自 Agent 临时选择，却在后续写成 Owner boundary，  
**那么**诊断 `constraint_drift`。

下一步：

1. 查 provenance；
2. 没有来源则撤回 hard status；
3. 放回 controller search variable；
4. 根据信息增益自主扩大 / 切换 / 并行。

### 把路径菜单交给 Owner

**如果** Agent 要求 Owner 选 A/B/C，而选项只是内部方法或可逆架构路线，  
**那么**诊断 `search_path_delegation`。

若路线均不违反 confirmed constraints：Controller 自主选择信息增益最高者；若相近则小批并行。

### 阶段性路线收敛被误判为 Owner pause

**如果**当前一条路线低收益，但其他未被硬约束禁止的 value / method / architecture 空间仍明显存在，  
**那么**诊断 `owner_boundary_false_positive`。

继续调度，不问 Owner。

### 真正应该问 Owner

只有：

- 要改变明确 confirmed hard constraint；
- 缺失目标事实无法从 source 恢复；
- 少数强候选只剩长期认同 / 气质等主观差异；
- 最终采用决策；
- 预算 / 时间边界。

---

## 7. Exploration / Exploitation 切换

### exploration → exploitation

只有在：

- 某 value / region / method 跨批出现稳定强度；
- search-integrity 未发现 collapse；
- 深挖可回答明确问题；
- 有退出条件。

Transformation Rescue 属于特殊 bounded exploitation。

### exploitation → exploration

触发：

- 变体越来越近；
- information gain 下降；
- 优势主要来自 reality survivor 而非质量；
- core value 长期低覆盖；
- mode collapse / anchoring / rescue overfit。

---

## 8. Owner Preference 与 Pareto

### 候选难以客观区分

2–3 个强候选形成 Pareto front，剩余差异主要属于长期认同、气质和主观 resonance → 才交 Owner。

### Owner 一次喜欢 / 讨厌

记录但不立即升级稳定偏好；跨候选 / 跨轮重复出现后再提高 confidence。

### Pareto 淘汰

候选可退出 active pool，但保留：

- semantic / value targets；
- construction / method；
- quality observations；
- reality observations；
- 被谁支配 / 哪些维度；
- 是否值得 rescue 或留下 method learning。

原则：

> **候选可以死，经验不能死；现实失败的强原型也不应自动丢掉可变形价值。**

---

## 9. 下一动作选择优先级

每轮优先问：

1. Mission / Value Model 是否缺结构？ → `model_values`
2. 所谓边界是否有 provenance？ → `audit_constraints`
3. value coverage 是否失衡？ → `map / schedule_methods`
4. 是否存在 mode collapse / scheduler monoculture / isolation 问题？ → `check_search_integrity`
5. 哪几个方法能最大降低当前未知？ → `schedule_methods`
6. 需要新样本吗？ → `generate`
7. 是否先过 Controller-only filter？ → `post_generation_filter`
8. intrinsic quality / value alignment 不清楚？ → `evaluate_*`
9. 强候选现实未知？ → `verify_reality`
10. 强 seed 主要死于现实占用？ → `open_rescue_branch`
11. 观察很多但意义不清？ → `diagnose`
12. 剩余差异主要是 Owner 主观选择？ → `ask_owner`
13. 足够 finalist 或真正无信息增益？ → `stop`

不要因为“流程下一步本来是什么”选择动作，只根据当前最大未知、价值覆盖、方法状态、可逆性与信息增益选择。

---

## 10. 状态更新最小要求

每次重要策略变化至少记录：

- trigger；
- diagnosis；
- confidence；
- mission / value model change（如有）；
- value coverage change；
- method scheduler state / budget change；
- constraint provenance / drift；
- search_mode before / after；
- generation isolation；
- Controller-only exclusions；
- post-generation filter；
- rescue branch status；
- next_action；
- why_now。

这样后续 Agent 才能区分：事实地图、价值解释、控制器私有约束、方法状态、Generator 实际看到的上下文和当时的策略推断。
