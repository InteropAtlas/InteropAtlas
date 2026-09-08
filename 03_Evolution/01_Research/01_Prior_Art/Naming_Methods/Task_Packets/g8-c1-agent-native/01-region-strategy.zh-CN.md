# G8 IA C1.0 — 执行任务包 01：Region Strategy

## 角色
Region Strategy Worker。

## 任务
基于 Organization Vision 与当前 G8 局部状态，选择下一段要探索的 naming region，并估计该区域的 collision prior。此阶段不生成正式候选。

## 允许上下文
- Organization Vision Context；
- G8 当前 arm-local compressed state；
- 已记录的 region-level failure topology；
- Naming Job constraints。

## 禁止上下文
- G0–G7 的候选、survivor、成绩；
- benchmark leaderboard；
- Owner 对其他路线的偏好；
- 完整历史聊天记录；
- 在本阶段生成正式名称。

## 输入
- Organization Vision Context；
- previous compressed region state（首轮可为空）；
- 当前 exploration / exploitation policy。

## 输出
Region Brief，至少包含：
- region definition；
- semantic / construction boundaries；
- estimated collision prior；
- why explore vs exploit；
- what evidence would trigger move / stay；
- prohibited overfitting signals。

## 规则
- region 不是具体词根清单；
- 不因为某个后缀曾通过 `.org` 就自动把它定义成安全区；
- 不生成候选；
- 只使用 G8 自己的局部历史，不吸收其他 arm 结果。

## 完成条件
形成足够小而明确的 Region Brief，可交给单次 Micro Generator。

## 交接
交给 G8 Task 02 — Micro Generator。