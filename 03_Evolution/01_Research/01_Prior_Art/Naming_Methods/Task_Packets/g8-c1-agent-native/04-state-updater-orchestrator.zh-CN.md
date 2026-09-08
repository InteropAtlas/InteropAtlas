# G8 IA C1.0 — 执行任务包 04：State Updater / Orchestrator

## 角色
Arm-local State Updater / Orchestrator。

## 任务
读取当前 Region Brief、冻结候选与 Reality Observer 结果，更新 G8 自己的局部 naming-space state，决定下一步继续 exploit 当前区域、调整区域边界，还是 move 到新区域。此 Worker 不直接生成候选。

## 允许上下文
- 当前 G8 arm-local compressed state；
- 当前 Region Brief；
- 当前 micro-cycle proposals；
- Reality Observation Records；
- frozen exploration / exploitation policy。

## 禁止上下文
- G0–G7 候选、通过率和排名；
- benchmark leaderboard；
- Owner 对其他路线候选的偏好；
- 完整历史聊天文本；
- 在本阶段直接创造名称。

## 输入
当前 micro-cycle 的结构化结果。

## 输出
更新后的 **arm-local internal compressed state**，至少包含：
- explored region summary；
- observed failure topology；
- survivor / failure pattern，但不得压缩成“安全后缀模板”；
- confidence；
- explore / exploit / move decision；
- 下一轮最小 region guidance；
- cumulative operation count / search count；
- 是否触发 stop condition。

该 internal state **只交给新的 G8 Task 01 Region Strategy 或后续 State Updater 实例，不得直接交给 Micro Generator**。

若继续生成，真正交给 Generator 的唯一策略性反馈载体是由 Task 01 根据 internal state 重新生成并冻结的 `Region Brief`。Region Brief 只能表达下一段探索空间、construction boundaries 与 region-level guidance，不得携带具体 survivor / Red / Yellow、domain / registry 状态、collision identities、失败候选清单或“安全词根 / 后缀”结论。

## 规则
- failure topology 只能影响 G8 自身后续，不外泄到其他 arm；
- 不把 domain 404 等单一信号当作 overall quality；
- 不直接生成名称；
- 不把 Reality Observation Record 或 internal compressed state 直接交给 Generator；
- 达到目标候选数量或 stop condition 后结束 micro-cycle loop，并进入共用 feasibility / quality / Owner gates。

## 完成条件
状态已持久化，并明确下一步：
- Continue → 交给新实例 G8 Task 01，由其冻结下一份 Region Brief，再进入 Task 02；
- 或结束 G8 generation phase。

## 交接
- Continue → 新实例 G8 Task 01 Region Strategy；
- Stop → 共用 E1/E2 feasibility、E3 Quality、E4 Integrity、E5 Owner Exposure。