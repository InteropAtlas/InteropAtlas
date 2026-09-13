# Naming Recovery

这是 InteropAtlas Naming Workstream 的**稳定单一恢复入口**。新 Agent 接管命名相关工作时，从本文件开始；不要依赖旧聊天记忆，也不要要求 Owner 重新提供历史上下文。

## 当前 Owner 指令：先批量交付，再优化（2026-09-13）

**当前主线已由 Owner 明确调整。首先读取 [#411 当前交付指令](https://github.com/InteropAtlas/InteropAtlas/issues/411#issuecomment-5652226777)，再解释 state。** [#408 方法研究同步](https://github.com/InteropAtlas/InteropAtlas/issues/408#issuecomment-5652241067)。这项优先级变化来自 Owner，不是 CI 或模型自行解除边界。

- 第一阶段：使用既有复杂命名系统和当前实际可用的高能力模型，先一次交付几十个可判断名称，累积 Owner 认可的及格池；首批40个待审提案、累计30个Owner-OK名称是当前执行目标，不是预先宣布已合格。
- 第二阶段：在已交付及格结果的基础上，把复杂系统优化到优秀；再做有目的的 Simple 对照、效率和成本优化。Simple 不替代当前复杂系统主线。
- 减少 Owner 注意力占用：集中交付、集中反馈，不以一个两个名称或每个微循环打断。历史正面反馈保留；未知不冒充确认，初筛不冒充商标/域名可采用许可。

**当前下一动作：`generate_screen_and_present_40_organization_name_proposals_with_existing_complex_method`。** 不先继续4B/12B/30–35B测试、Reviewer校准、gate扩写或旧实验归档。主线不等待这些维护事项。

截至本次恢复入口更新，结构化 state 仍为 v99，v100 迁移在远端投递时遇到403，尚未写回。v99 的研究 `next_action` 与一般生成暂停已被上述 Owner 指令在本轮批量提案范围内取代；其历史证据、未验证结论和最终采用条件仍保留。不要因为 state 的过时动作重跑 SEM-408-006，也不要把修复同步脚本排在名称交付之前。结构化同步属于非阻塞维护；未完成的同步不可伪称完成。

本轮恢复授权不等于启动 G0–G8、注册/购买、外部订阅购买、最终采用、合并或稳定晋升。复杂系统的研究潜力是建设目标，不要求先证明其胜过 Simple 才允许交付。

## 恢复

1. 先遵守 [`AGENTS.md`](AGENTS.md) 与 [`PROJECT_STATE.md`](PROJECT_STATE.md) 的仓库级规则。
2. 先检查上述当前 Owner 指令与其后续更新；读取 [`03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml`](03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml)，区分当前授权和历史研究断点。
3. 按状态中的引用，只读取当前交付直接需要的 Issue / PR / brief / 历史反馈。实时交付主入口为 #411；#408 支持方法研究；PR #416 不替代当前交付指令。
4. 从最新 Owner 授权对应的交付动作继续。不要从头重跑历史，也不要创建平行替代流程。

## 解释规则

- 仓库中的可追溯 Owner 指令与证据优先于聊天记忆。最新明确授权可以变更旧工作断点，但不能改写历史结果。
- `paused / blocked / draft / experimental / not_tested` 等历史状态不因 CI 或模型答案自动晋级；本次批量生成范围的改变应引用上面的 Owner 授权。
- 是否允许生成、付费、现实注册/购买、稳定晋升、合并或最终采用，分别判断，不互相推导授权。
- 分别记录：候选已生成、已展示、Owner已评、Owner认可、现实可采用、优秀程度。规划、CI、归档和快照数不是名称交付进度。

## 持续接管

完成一段有持续价值的工作后，把结果、证据、阻塞和下一动作写回当前 Primary Home，并同步 state。普通内部工程问题不要求 Owner 逐项确认，且不得反复取代交付主线。以后结构化 state 与本指令同步后，可将本页的临时冲突说明收敛为指针，不保留重复状态源。

**目标：聊天可以丢失；只靠本文件和仓库当前事实，也能恢复并继续。**
