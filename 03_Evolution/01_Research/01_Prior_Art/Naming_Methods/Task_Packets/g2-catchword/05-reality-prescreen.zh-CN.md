# G2 Catchword — 执行任务包 05：Reality Prescreen

## 角色
Reality Prescreen Worker。

## 任务
对方法内 shortlist 做 preliminary reality screening：商标导向、公司/产品/项目/软件身份、域名/社交/搜索占用与严重混淆风险。此 Worker 只筛现实可行性，不评价名字是否优美或是否符合 Owner 偏好。

## 允许上下文
- 使用 run-local opaque IDs 的 shortlist candidate strings；
- 必要的官方/公开现实来源；
- 本任务的筛查标准。

## 禁止上下文
- canonical candidate IDs；
- 候选来自 G2 / Catchword 的事实；
- canonical Packet 标题、文件路径、method_arm 与来源型 provenance；
- 其他 arm 候选和成绩；
- Creative Brief 之外不必要的生成 rationale；
- Owner 偏好；
- 为失败候选重新生成替代名。

## 输入
由 Orchestrator 从上游 shortlist 生成的 blind execution input：opaque candidate ID + display name。不得把 `G2-*` ID 或上游文件路径原样传入。

## 输出
每个候选的：
- opaque_candidate_id；
- observed surfaces；
- evidence links / source type；
- Red / Yellow / Clear-to-next-stage（仅为 preliminary status）；
- confidence；
- ambiguity / follow-up need。

## 规则
- preliminary screen ≠ final legal clearance；
- domain availability 只是一个 surface，不代替 identity / trademark-oriented search；
- 不因无搜索结果宣称“法律安全”；
- 不生成新名字。

## 完成条件
所有 shortlist 候选都有可追溯的现实筛查状态。

## 交接
输出先回 Orchestrator 恢复 opaque ID 映射，再作为 G2 Task 07 的结构化输入。

## Blindness
- blind_to_arm: true
- blind_to_owner_preference: true
- blind_to_quality: true

实际 Session 必须使用 Schema 的 Blind runtime instantiation rule；canonical 文档标题中的 `G2 Catchword` 不进入 Worker-visible runtime view。