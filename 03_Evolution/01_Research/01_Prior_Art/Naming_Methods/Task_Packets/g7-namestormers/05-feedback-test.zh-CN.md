# G7 NameStormers — 执行任务包 05：Feedback / Test

## 角色
Feedback / Test Worker。

## 任务
对 Pitch Cards 收集结构化 stakeholder feedback / test 结果，并把“偏好”“理解”“记忆”“疑惑”“误读”“策略适配”等不同信号分开记录。此阶段不直接生成或修改名称。

## 允许上下文
- Pitch Cards；
- 预先冻结的 feedback / test protocol；
- 必要的受众 / stakeholder context。

## 禁止上下文
- 其他 arm 候选、成绩和排名；
- Generator 原聊天历史；
- Refinement 方案；
- benchmark leaderboard；
- 为迎合反馈现场重写名称。

## 输入
G7 Task 04 Pitch Cards。

## 输出
结构化 Feedback Brief，至少包含：
- comprehension；
- recall / pronunciation / spelling observations；
- emotional / associative response；
- preference（单独记录，不等同质量）；
- confusion / objection；
- recurring patterns；
- minority concerns；
- confidence / sample limitations。

## 规则
- feedback 是学习信号，不是多数票；
- preference ≠ naming quality；
- 不把单个强烈意见自动放大；
- 不生成新名字。

## 完成条件
形成可以安全压缩回流给 Refinement Worker 的反馈，而不需要传递完整原始聊天历史。

## 交接
交给 G7 Task 06 — Refinement Worker。