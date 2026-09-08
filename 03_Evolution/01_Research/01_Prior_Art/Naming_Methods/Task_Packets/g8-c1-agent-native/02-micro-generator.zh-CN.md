# G8 IA C1.0 — 执行任务包 02：Micro Generator

## 角色
Micro-cycle Generator。

## 任务
只根据当前 Region Brief 生成极少量正式候选（默认 1–3 个），然后立即停止，等待独立 Reality Observer 的反馈。Generator 不搜索现实占用。

## 允许上下文
- Organization Vision Context；
- 当前 Region Brief；
- 当前 micro-cycle 需要的最小 compressed state；
- Naming Job constraints。

## 禁止上下文
- Reality Observer 的搜索工具与原始搜索过程；
- 其他 arm 候选、成绩；
- benchmark leaderboard；
- 完整 G8 历史聊天；
- Owner 对其他路线候选的偏好。

## 输入
Region Brief + compressed local state。

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
- 不因历史“安全词根”直接重复模板。

## 完成条件
当前 micro-cycle 候选已冻结并持久化。

## 交接
交给 G8 Task 03 — Reality Observer。