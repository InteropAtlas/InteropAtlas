# G8 IA C1.0 — 执行任务包 03：Reality Observer

## 角色
Reality Observer。

## 任务
对当前 micro-cycle 已冻结并持久化的候选进行现实观察：公司、产品、项目、软件、人物、历史身份、词汇占用、域名与商标导向等。Observer 只观察，不生成新名字，也不决定下一步探索区域。

## 允许上下文
- 当前 micro-cycle candidate strings；
- 预先冻结的 observation surfaces；
- 必要的公开现实来源 / registry / search 结果。

## 禁止上下文
- 其他 arm 候选、成绩；
- Generator 的完整思考过程；
- benchmark leaderboard；
- Owner 对具体历史候选的偏好；
- 直接生成替代候选；
- 自行改变 exploration / exploitation policy。

## 输入
G8 Task 02 已持久化候选。

## 输出
每个候选的 Observation Record，至少包含：
- observed identities by surface；
- exact / near / semantic-neighborhood collision；
- domain / registry state；
- confidence；
- source / evidence；
- Red / Yellow / provisional survivor；
- observation uncertainty。

## 规则
- 搜索结果不是绝对真值，必须记录 confidence；
- 无结果不等于法律安全；
- 每次 observation 必须先持久化，再进入下一 micro-cycle；
- 不生成新名字。

## 完成条件
当前候选均有可追溯 observation，并已持久化。

## 交接
交给 G8 Task 04 — State Updater / Orchestrator。