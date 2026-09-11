# G7 NameStormers — 执行任务包 06：Refinement

## 角色
Refinement Worker。

## 任务
基于结构化 Feedback Brief 对候选进行受控 refinement。可以微调、重组、替换或补充候选，但所有变化必须可追溯到反馈与 Strategy Brief，不得把 refinement 变成重新随机生成。

## 允许上下文
- Organization Vision Context；
- G7 Task 01 Strategy Brief；
- 经过压缩的 G7 Task 05 Feedback Brief；
- 需要 refinement 的候选及其 Pitch Card。

## 禁止上下文
- Feedback Worker 的完整原始聊天历史；
- 其他 arm 候选、成绩和筛选结果；
- benchmark leaderboard；
- Owner 对其他路线候选的偏好。

## 输入
Strategy Brief + compressed Feedback Brief + candidate set。

## 输出
- refined candidates；
- retained unchanged candidates；
- dropped candidates；
- 每个变化对应的 feedback source / rationale；
- 是否需要再次进入 Prescreen / Pitch / Feedback 的建议；
- provenance version。

## 规则
- 新一轮必须使用新隔离 Session；
- 不继承旧聊天上下文；
- 不能只为提高现实通过率而改词形，除非该反馈来自本方法允许的 prescreen / stakeholder learning；
- 变化必须可追溯。

## 完成条件
形成一轮可审计 refinement 结果，并明确下一步是再次循环还是进入 Final。

## 交接
- 如需循环：重新进入 G7 Task 03 Prescreen → Task 04 → Task 05；
- 如结束：交给 G7 Task 07 — Final Decision Worker。