# Naming State Template

`naming-state-template.yaml` 是**单次 Naming Job 的运行时状态模板**，不是 Skill 本体，也不是跨任务长期数据库。

使用时复制为该 Naming Job 的独立 state，并在每个重要观察 / 诊断 / 状态转移后更新。

应保留：

- 已探索区域与地图变化；
- 候选，包括已退出 active pool 的候选；
- 质量与现实可用性两条独立观察；
- 诊断及其证据；
- Owner 偏好信号；
- 当前最大未知与下一动作；
- 可能跨任务成立的 `experience_candidates`。

不要把某次任务的 state 写回 `SKILL.md`。
