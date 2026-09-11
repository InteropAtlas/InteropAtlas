# G5 Siegel+Gale — 执行任务包 07：Blind Contextual Evaluation

## 角色
Blind Contextual Evaluation Worker。

## 任务
把四个 category Generator 的候选混合后进行盲式 contextual evaluation。评审不知道每个候选来自 Descriptive / Suggestive / Coined / Edgy 中哪一类，也不知道其他 benchmark arm。目标是比较候选本身，而不是奖励某个 category 标签。

## 允许上下文
- Organization Vision Context；
- Simplicity Strategy；
- 已由 Orchestrator 去除 category / source provenance 并使用 opaque IDs 随机混合的候选及最小必要 rationale；
- Siegel+Gale 公开的相关评价维度：unique、attention-getting、motivational、appropriate、memorable、fits-me 等，作为多维参考而非总分公式。

## 禁止上下文
- canonical candidate IDs / category identity；
- Generator 文件路径、packet ID、category-coded provenance；
- 其他 arm 身份、候选、成绩；
- reality/domain/trademark screening 结果；
- Owner 对具体历史候选的偏好；
- 简单多数投票结果。

## 输入
四路 Generator 的冻结候选，由 Orchestrator：
1. 去除 category 标签与来源型 provenance；
2. 重新映射为 run-local opaque candidate IDs；
3. 随机混合或按预先冻结的中性顺序混合。

## 输出
- quality-qualified candidates（使用 opaque IDs）；
- weaker / deferred candidates；
- 每个候选的多维评价；
- trade-offs；
- 是否存在某种候选形态被系统性高估/低估的提示（不得恢复 category 身份）；
- 推荐进入 Governance 的集合。

## 判断原则
- Preference ≠ naming quality；
- 不使用单一加权总分决定结果；
- simplicity 与 distinctiveness 可以同时存在张力；
- 不因“不熟悉”自动淘汰 coined / edgy，也不因“易懂”自动奖励 descriptive。

## 完成条件
形成一组不依赖 category 标签的质量判断结果。

## 交接
输出先回 Orchestrator 恢复 opaque ID ↔ canonical candidate 映射，再交给 G5 Task 08 — Governance / Decision Worker；如启用 Optional Testing，测试结果作为额外独立证据进入 Governance。

## Blindness
- blind_to_category: true
- blind_to_other_arms: true
- blind_to_feasibility: true
- blind_to_owner_preference: true

实际 Session 必须使用 Schema 的 Blind runtime instantiation rule；canonical 文档标题中的 `G5 Siegel+Gale` 也不应原样出现在 Worker-visible runtime view。