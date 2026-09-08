# G7 NameStormers — 执行任务包 03：Prescreen

## 角色
Prescreen Worker。

## 任务
对 Lightning Round 冻结候选做基础现实筛查，排除明显不可用或严重混淆项，为后续 Pitch 留下值得进入 stakeholder interaction 的集合。

## 允许上下文
- 使用 run-local opaque IDs 的 candidate strings；
- 必要的 reality / trademark-oriented / domain / search sources；
- 预先冻结的筛查标准。

## 禁止上下文
- canonical candidate IDs；
- 候选来自 G7 / NameStormers 的身份；
- canonical Packet 标题、文件路径、method_arm 与来源型 provenance；
- 其他 arm 候选与成绩；
- Generator 原聊天历史；
- stakeholder feedback；
- Owner 对具体历史候选的偏好；
- 为被淘汰项生成替代名。

## 输入
由 Orchestrator 从 Lightning Round 冻结候选生成的 blind execution input：opaque candidate ID + display name。不得把 `G7-*` ID 或上游文件路径原样传入。

## 输出
- opaque_candidate_id；
- Pass / Yellow / Red；
- evidence；
- confidence；
- severe confusion notes；
- 可进入 Pitch 的 opaque candidate 集合。

## 规则
- preliminary screen ≠ final legal clearance；
- 不评价候选是否“有故事”；
- 不重新生成。

## 完成条件
形成可供 Pitch Worker 使用的预筛集合。

## 交接
输出先回 Orchestrator 恢复 opaque ID 映射，再交给 G7 Task 04 — Pitch / Context Worker。

## Blindness
- blind_to_arm: true
- blind_to_owner_preference: true
- blind_to_quality: true

实际 Session 必须使用 Schema 的 Blind runtime instantiation rule；canonical 文档标题中的 `G7 NameStormers` 不进入 Worker-visible runtime view。