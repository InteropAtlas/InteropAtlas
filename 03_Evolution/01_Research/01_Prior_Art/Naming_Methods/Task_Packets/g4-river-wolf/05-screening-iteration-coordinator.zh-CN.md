# G4 River + Wolf — 执行任务包 05：Screening / Iteration Coordinator

## 角色
Screening / Iteration Coordinator。

## 任务
汇总 G4 shortlist 的现实筛查与方法内表现，决定本轮是结束、进入共用评估层，还是基于结构化原因开启下一轮迭代。此 Worker 负责协调回流，不直接生成名称。

## 允许上下文
- 冻结 4Cs Brief；
- G4 Task 04 shortlist；
- 必要的 reality / linguistic screening 结果；
- 本轮 method-fidelity / degeneration observations。

## 禁止上下文
- 其他 arm 候选和成绩；
- benchmark leaderboard；
- Owner 对其他路线的偏好；
- 在本 Session 中直接创造 replacement names。

## 输入
shortlist + screening observations。

## 输出
二选一：

### A. 结束本轮
- 保留候选；
- 淘汰候选；
- 进入共用 Quality Gate 的集合；
- 方法完整性摘要。

### B. 开启迭代
生成一份结构化 Iteration Brief，仅包含：
- 哪个 4C 参数需要澄清或调整；
- 哪类输出偏离目标；
- 哪些问题是 reality collision，哪些是 creative fit；
- 新一轮允许传回 Development 的最小信息；
- 新 parameter version。

## 规则
- feedback 必须经压缩后回流；不得把整轮聊天历史、所有失败名和其他 arm 信息喂给新 Generator；
- 若只是个别候选撞名，不自动修改 4Cs；
- 参数调整必须有方法内理由，而不是为了追求 benchmark 通过率；
- 新一轮 Development 必须开启新隔离 Session。

## 完成条件
明确决定 stop 或 iterate，并留下可复现的回流理由。

## 交接
- Stop → 共用 E3 Quality / Pareto Reviewer；
- Iterate → 新实例的 G4 Task 03 Development Worker（必要时先更新 Task 02 的 4Cs 版本）。