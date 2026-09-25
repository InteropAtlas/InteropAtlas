# Naming Current State

这是 InteropAtlas Organization Naming 当前任务的**最小可执行状态入口**。它不是历史总结，也不替代详细证据；目标是让下一棒 Agent 用最少上下文恢复当前真实状态。

## 当前状态

- Branch：`feat/adaptive-naming-skill-v0.1`
- Workstream：Organization Naming / Adaptive Naming
- Mode：暂停继续生成，等待 Owner 做现实预算边界判断
- Generation：**PAUSED**
- G0–G8 benchmark：**保持停止，不恢复**
- PR #416：仍为 Draft，不合并、不晋升 stable method
- Owner-visible 新候选：当前 0 个
- Preliminary internal survivor：`Recenvia`，仅内部保留，不自动升级为 finalist

## 为什么停在这里

最近连续完成了 Transformation Rescue、Territory Reset 和最终 pre-escalation micro-probe。生成端完整性已通过，但现实命名空间持续拥挤：强候选频繁遇到 exact identity、registered `.com`、个人名/软件/组织等冲突。

最新 micro-probe 的预先停止条件已经触发，因此不能继续静默生成来制造“进展”。

## 当前唯一需要 Owner 决定的问题

`exact .com` 的现实二级市场预算边界，以及“名称质量”与“低购置成本”的优先级。

Owner 需要在以下方向之间定边界：

1. **质量优先 / 接受透明售后**：允许通过身份筛查的强名称进入明确预算区间的 aftermarket 查询；
2. **低购置成本优先**：继续偏向 direct registration / 近零售后成本，并接受成熟、有意义、非个人读感名称的成功率明显下降。

在 Owner 做出这个边界判断前，不启动下一批生成。

## 下一棒 Work Unit

当前 Work Unit 不是生成名字，而是：

- 向 Owner 清楚呈现上述预算/质量取舍；
- 记录 Owner 的边界决定；
- 根据决定更新 Naming Job constraints；
- 只有边界冻结后，才定义下一棒生成或现实筛查任务。

## 必读入口

按顺序：

1. 本文件 `NAMING_CURRENT_STATE.md`；
2. `NAMING_RECOVERY.md` — 最新过程、生成能力恢复规则与现实筛查证据；
3. `02_Runtime/02_Tools/adaptive_naming/SKILL.md` — 只有进入实际命名工作时再读；
4. Issue #408 / #411、PR #416 — 需要研究或审计细节时按需读取。

详细历史状态文件：

`03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml`

其中 snapshot v99 等内容继续作为详细研究/历史状态保留，但其 `next_action` **可能落后于 branch HEAD，不再作为当前行动入口**。

## 当前 Source of Truth 规则

若当前行动发生冲突：

`branch HEAD 的 NAMING_CURRENT_STATE.md / NAMING_RECOVERY.md → 最新明确 Owner 决定 → 详细 state / Issue / PR 历史`

不要从旧 snapshot 恢复已被后续提交取代的 next_action。

## Checkpoint

此状态由 branch HEAD `e2869b5c9807fe7c044b2ef059321b2457b367e4`（`naming: record micro-probe 010 escalation boundary`）整理而来。该提交明确记录：停止静默生成，等待 Owner 决定 `.com` aftermarket budget 与质量/成本优先级。