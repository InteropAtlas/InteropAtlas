# G8 IA C1.0 — 执行任务包 02：Micro Generator

## 角色
Micro-cycle Generator。

## 任务
只根据当前冻结的 Region Brief 生成极少量正式候选（默认 1–3 个），然后立即停止，等待独立 Reality Observer 的反馈。Generator 不搜索现实占用。

## 允许上下文
- Organization Vision Context；
- 当前冻结的 Region Brief；
- Naming Job constraints；
- 当前 micro-cycle id / count 等不包含筛选结果的运行元数据。

## 禁止上下文
- Reality Observer 的搜索工具、原始搜索过程与 Observation Records；
- survivor / Red / Yellow / domain / registry / collision 结果；
- failure topology、历史 feasibility pattern 或所谓“安全词根 / 安全后缀”；
- State Updater 的内部 arm-local state；
- 其他 arm 候选、成绩；
- benchmark leaderboard；
- 完整 G8 历史聊天；
- Owner 对其他路线候选的偏好。

## 输入
冻结 Region Brief + 非筛选型运行元数据。

Region Brief 必须由 G8 Task 01 基于 arm-local compressed state 生成；不得把 Task 03 Observation Record 或 Task 04 内部 state 直接转交本 Worker。

## 输出
1–3 个正式候选，每个至少包含：
- name；
- intended pronunciation（如需要）；
- region relation；
- construction mechanism；
- rationale；
- strengths / risks；
- provenance / micro-cycle id。

## 规则
- 每个正式候选必须先持久化，再进入搜索；
- 不自行判断域名、商标或公司占用；
- 不批量生成 20 个后再筛；
- 不因历史“安全词根”直接重复模板；
- 不接受任何带有 survivor / feasibility / collision 标签的上游状态。

## 完成条件
当前 micro-cycle 候选已冻结并持久化。

## 交接
交给 G8 Task 03 — Reality Observer。