# G3 Igor — 执行任务包 03：Trademark / Reality Prescreen

## 角色
Reality Prescreen Worker。

## 任务
对冻结候选进行 preliminary trademark-oriented / reality identity screening，识别公司、产品、项目、软件、组织、商标导向与严重混淆风险。此步骤只判断现实风险，不评价故事性和审美。

## 允许上下文
- 使用 run-local opaque IDs 的 candidate strings；
- 必要的公开现实来源与注册/搜索信息；
- 本任务筛查标准。

## 禁止上下文
- canonical candidate IDs；
- 候选来自 Igor / G3 的身份；
- canonical Packet 标题、文件路径、method_arm 与来源型 provenance；
- 其他 arm 候选、成绩；
- Name Development rationale，除非用于判断语义邻域混淆且已去除来源信息；
- Owner 偏好；
- 为失败候选生成替代名。

## 输入
由 Orchestrator 从冻结候选生成的 blind execution input：opaque candidate ID + display name；必要 disambiguation 信息另行最小化注入。不得把 `G3-*` ID 或上游文件路径原样传入。

## 输出
每个候选的：
- opaque_candidate_id；
- observed reality identities；
- trademark-oriented observations；
- severe confusion risk；
- Red / Yellow / Clear-to-next-stage；
- confidence；
- sources / evidence notes。

## 规则
- preliminary prescreen ≠ final legal clearance；
- exact domain availability 不是唯一判断；
- 不因为搜索为空就宣称绝对安全；
- 不生成新名字。

## 完成条件
每个候选都有现实风险状态与可追溯证据。

## 交接
输出先回 Orchestrator 恢复 opaque ID 映射，再作为 G3 Task 04 的结构化输入。

## Blindness
- blind_to_arm: true
- blind_to_owner_preference: true
- blind_to_quality: true

实际 Session 必须使用 Schema 的 Blind runtime instantiation rule；canonical 文档标题中的 `G3 Igor` 不进入 Worker-visible runtime view。