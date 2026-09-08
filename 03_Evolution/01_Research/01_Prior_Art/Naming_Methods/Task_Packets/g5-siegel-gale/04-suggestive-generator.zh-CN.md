# G5 Siegel+Gale — 执行任务包 04：Suggestive Generator

## 角色
Suggestive Naming Generator。

## 任务
只在 Suggestive category 内生成候选：通过隐喻、联想或间接语义提示组织价值，但不直接描述业务，也不进入纯造词区域。

## 允许上下文
- Organization Vision Context；
- Simplicity Strategy；
- Suggestive Category Brief；
- 当前候选数量与输出格式。

## 禁止上下文
- Descriptive / Coined / Edgy Generator 的输入输出；
- 其他 arm 候选与成绩；
- reality/domain/trademark 结果；
- Owner 对具体历史候选的偏好。

## 输入
Suggestive Category Brief。

## 输出
正式候选集，每个候选至少包含：
- name；
- implied association / metaphor；
- relationship to simplicity；
- pronunciation / spelling notes；
- strengths / ambiguity；
- provenance。

## 规则
- 不退化成描述性标签；
- 不进入无稳定语义的纯 coinage；
- 不搜索现实占用；
- 不读取其他三个 category 的结果。

## 完成条件
形成一组真正属于 Suggestive 区域、可供盲式 Contextual Evaluation 比较的候选。

## 交接
交给 G5 Task 07 — Blind Contextual Evaluation Worker。