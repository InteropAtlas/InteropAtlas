# G2 Catchword — 执行任务包 03：High-volume Divergent Generation

## 角色
Divergent Generation Worker。

## 任务
依据 Creative Brief 与 Vocabulary / Territory Map 进行高覆盖、延迟判断的候选生成。目标是扩大可供后续统一比较的候选空间，而不是边生成边淘汰。

## 允许上下文
- Organization Vision Context；
- Creative Brief；
- Vocabulary / Territory Map；
- 当前要求的候选数量与输出字段。

## 禁止上下文
- 域名 / 商标 / reality collision 反馈；
- 其他 arm 候选或成绩；
- Owner 对具体历史名字的偏好；
- 后续 shortlist / quality 结果；
- 为追求可注册率而进行 search-guided generation。

## 输入
- Creative Brief；
- Vocabulary / Territory Map。

## 输出
正式候选集。每个候选至少记录：
- name；
- intended pronunciation（如需要）；
- territory；
- construction mechanism；
- brief fit rationale；
- immediate strengths / ambiguities；
- provenance / order。

## 执行规则
- 保持多个 territory 和 construction family 的覆盖；
- 不因即时个人偏好提前停止；
- 不进行现实搜索；
- 不把内部重复观察转化为跨 arm 经验；
- 若出现 exact within-batch repeat，标记并替换，保留 provenance。

## 完成条件
达到要求的正式候选数量，覆盖面足够，且所有候选在任何 downstream screening 之前已冻结。

## 交接
交给 G2 Task 04 — Internal Shortlist Worker。