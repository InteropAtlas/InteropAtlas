# G4 River + Wolf — 执行任务包 03：Development

## 角色
Name Development Worker。

## 任务
仅依据冻结的 4Cs 参数与组织愿景发展正式候选。Generator 不读取其他路线历史，也不读取 screening feedback。

## 允许上下文
- Organization Vision Context；
- 冻结的 G4 4Cs Brief；
- 当前候选数量与输出字段要求。

## 禁止上下文
- 其他 arm 的候选、survivor、成绩；
- 本 arm 历史高频词根作为模板；
- domain / trademark / reality 筛选结果；
- Owner 对具体历史候选的偏好。

## 输入
冻结的 4Cs Brief。

## 输出
正式候选集，每个候选至少记录：
- name；
- intended pronunciation（如需要）；
- 对 Character / Communication / Construction / Continuum 的对应关系；
- construction mechanism；
- strengths / ambiguity；
- provenance / parameter version。

## 规则
- 不能把 4Cs 简化成词根拼接表；
- 相似 morphology 可以自然出现，但不得因历史 survivor 人为重复；
- 不搜索现实占用；
- 若上一轮迭代后再次运行，应开启新 Session，只接收新的压缩 4Cs / iteration brief，不继承原聊天全文。

## 完成条件
达到要求的冻结候选数量并保留完整 4Cs trace。

## 交接
交给 G4 Task 04 — Shortlist Worker。