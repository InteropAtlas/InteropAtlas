# SEM-408-TASK-GATE-001：Reviewer 任务理解门槛

## 结论

本轮完成了一个**确定性任务理解门槛**，用于判断语义 Reviewer 的输出是否至少理解了“正在评价名称，而不是评价产品本身是否实现功能”。它不是名称质量评委，也不判断 `advance / hold / stop` 哪个结论正确。

对 SEM-408-003 已恢复的六条历史输出重放：

- `block`：5 条；
- `review`：1 条；
- `pass`：0 条；
- 可进入后续语义证据使用：0 条。

因此，SEM-408-003 仍不能作为独立语义质量证据，也不能用于建立 Qwen 与 Gemma 的名称质量胜负。

## 门槛检查什么

`pass / review / block` 只描述任务理解资格：

- **block**：明显把名称当成必须实现产品功能的对象；把 brief / instruction / validation 等任务文字当作候选本身的特征；只用“名字包含自己”之类循环陈述；或没有把观察落在当前候选上。
- **review**：没有明确任务层级错误，但仍存在过度要求名称字面编码产品功能、或最终理由过于泛化而缺少候选依据。
- **pass**：没有观察到上述任务理解失败。`pass` 只允许该输出进入下一层语义审查，**不证明名称好，也不证明 Reviewer 判断正确**。

门槛明确忽略最终 `advance / hold / stop` 标签是否符合作者观点；同一合格内容即使把 disposition 从 advance 改成 hold 或 stop，任务理解结果也不应变化。

## 历史 SEM-408-003 重放

| ID | 门槛结果 | 主要原因 |
| --- | --- | --- |
| C001 | block | 把名称缺少“inherent analytical value”当作产品适配失败，给名称强加产品能力负担 |
| C002 | block | 把 `frozen brief` 等任务文本当作候选观察/联想 |
| C003 | block | 明确出现 “It’s a name, not a tool.”，并伴随循环式候选观察 |
| C004 | block | 以 “lacks inherent product features”否定名称，且最终理由复用短观察 |
| C005 | review | 没有明确层级错误，但最终理由主要是泛化的 memorability / brand recognition 陈述 |
| C006 | block | “name contains the word itself”式循环陈述 |

这些分类只说明为什么旧输出不具备作为独立语义证据的最低资格，不重评分这些名字本身。

## 合成控制与验证

使用匿名占位 token，而不是生成新的真实候选名，冻结了 6 个最小控制例：

1. 正常候选级观察 → pass；
2. 给名称强加产品功能 → block；
3. 把任务文本当候选证据 → block；
4. 循环陈述 → block；
5. 过度要求名称字面描述功能 → review；
6. 没有候选级 grounding → block。

测试同时验证：

- `brief_fit` 可以正常引用 brief，本身不会被误判为 instruction leak；
- “名称不需要编码全部产品功能”是允许的；
- disposition 改变不影响任务理解判断；
- 门槛的 scope 明确为 `task_understanding_only_not_name_quality_or_disposition_correctness`。

CI run `34744133574` 完成：任务理解门槛 6/6 单测通过；原有 28/28 control、12/12 state、14/14 integration、25 protocol、18×2 transport、20×2 workflow、19 selection 和 6 format-adapter 检查继续通过。没有模型调用。

## 原始证据保真修正

第一次把新门槛接入永久 CI 时，旧 `git diff --check` 对 v96 保存的原始 Actions `job.log` 报告 trailing whitespace。该日志是按字节保留的原始证据，清理空格会破坏此前记录的 SHA256。

因此 CI 只把 whitespace check 收窄到实际要审查的 state 文件，不修改原始日志字节。该修正改变的是检查范围，不改变任何历史模型输出、state 事实或名称判断。

## 下一步

当前最小有信息量的下一步不是重新跑六项，而是**一个既有开发候选的真实 Reviewer canary**：

- 不生成新名称；
- 不恢复 IA / G0–G8；
- 只发送一个既有候选；
- 使用冻结 brief 与同一语义评价维度；
- 明确名称是 identity label，不要求名称自身实现或列举产品功能；
- 无重试；
- 输出先经过本任务理解门槛；
- 若为 `block` 或 `review`，立即停止，不发送其余候选；
- 即使 `pass`，也只证明该次输出具备进入语义审查的最低资格，不证明质量判断正确，也不自动扩大实验。

本轮新增名称 0、模型调用 0、付费推理 0。Adaptive Naming Skill 仍为 v0.4.0；PR #416 保持 Draft；稳定方法未晋升。
