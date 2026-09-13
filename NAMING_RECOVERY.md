# Naming Recovery

这是 InteropAtlas Naming Workstream 的**稳定单一恢复入口**。新 Agent 接管命名相关工作时，从本文件开始；不要依赖旧聊天记忆，也不要要求 Owner 重新提供历史上下文。

## 恢复

1. 先遵守 [`AGENTS.md`](AGENTS.md) 与 [`PROJECT_STATE.md`](PROJECT_STATE.md) 的仓库级规则。
2. 读取当前状态：[`03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml`](03_Evolution/01_Research/03_Tests/organization-naming-411-state.yaml)。
3. 按状态中的引用，只读取当前任务直接需要的 Issue / PR / experiment / report / evidence；实时协作主入口为 #408（方法研究）与 #411（真实组织命名），PR #416 仅在状态指向时读取。
4. 从状态里的 `next_action` 继续。不要从头重跑历史，也不要创建平行替代流程。

## 解释规则

- 仓库中的当前状态与可追溯证据优先于聊天记忆；发现冲突时保留冲突，不自行补全历史。
- `paused / blocked / draft / experimental / not_tested` 等状态必须按字面保持，不能因为 CI 通过或模型给出答案而自动晋级。
- 是否允许生成、付费、现实注册/购买、稳定晋升、合并或最终采用，以当前状态和 Owner 明确授权为准。
- 实验结果必须区分：生成质量、选择质量、流程可靠性、语义判断、现实筛查、Owner 采用意愿。

## 持续接管

完成一段有持续价值的工作后，把结果、证据、阻塞和下一动作写回当前 Primary Home，并更新 state 的 `next_action`。只有 Naming Workstream 的稳定恢复路径本身发生变化时，才修改本文件。

**目标：聊天可以丢失；只靠本文件和仓库当前事实，也能恢复并继续。**
