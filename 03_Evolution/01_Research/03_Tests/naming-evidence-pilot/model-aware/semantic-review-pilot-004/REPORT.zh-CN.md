# SEM-408-004：单候选 Reviewer 任务理解 Canary

## 结论

在 SEM-408-TASK-GATE-001 已经建立确定性任务理解门槛后，本轮只对一个**既有开发候选**执行一次真实 Reviewer 请求，用来判断修正后的任务包装是否至少能避免此前的名称/产品层级混淆。

结果：**canary 通过任务理解门槛。**

- 候选：C003 / Linetap（既有 DEV-02 候选，不是新名称）；
- Reviewer：与 SEM-408-003 相同的 `ggml-org/gemma-3-4b-it-GGUF` / Q4_K_M 路线；
- 请求数：1；
- 重试：0；
- 新名称：0；
- 付费推理 API：0；
- task gate：`pass`；
- gate findings：0；
- `semantic_evidence_eligible=true`；
- `semantic_quality_validated=false`；
- quality ground truth：无。

因此可以说：**在这一个冻结样本上，明确区分“名称是 identity label、产品功能属于产品本身”后，Reviewer 不再复现 SEM-408-003 中的任务层级错误。** 不能由此声称 Reviewer 已经整体可靠，也不能把它的具体名称判断当成质量真值。

## 为什么选择 Linetap

SEM-408-003 对同一候选 C003 曾给出 “It’s a name, not a tool.” 这样的理由，是最清晰的任务层级失败之一。因此本轮使用同一既有候选，能够直接检验任务包装是否修复了这一类错误，而不需要生成新名称。

本轮不是严格的模型 A/B：任务包装发生了明确变化，目的正是验证这种变化是否能消除已知失败模式。

## 这次改变了什么

与 SEM-408-003 相比，候选、brief、Reviewer 模型家族、权重路线、sampling、评价维度和 JSON schema 保持不变；任务说明增加并冻结了三条边界：

1. 候选是产品的**身份标签**，不是产品实现本身；
2. 不要求名称自身执行、枚举或字面编码产品功能；
3. brief / instruction 只作为比较上下文，不能被写成候选自身的可观察特征或语言联想。

输出之后立即经过 `semantic-review-task-gate/gate.py`。即使 gate pass，也不会自动扩展到其余五个候选。

## 实际输出的边界

本次输出把 Linetap 判为 `hold`、brief fit 为 `mixed`，并给出了若干 association hypotheses。任务理解门槛没有发现：

- 给名称强加产品功能；
- 把 brief / instruction 当作候选证据；
- 循环 candidate grounding；
- 缺少候选级 grounding；
- 明显过度要求字面功能编码。

因此该输出获得**进入下一层语义审查的最低资格**。

但门槛不验证诸如“可能关联某类电影类型/编辑风格”等具体联想是否真实、典型或重要；这些仍只是 Reviewer 提出的待验证假设。`hold` 本身也没有被本门槛证明为正确。

## 证据

- run：`34744282097`；
- job：`103689175084`；
- evidence commit：`6659c3ac5b3e19affa5fe556d9362a025dd6ad1b`；
- artifact：`10313663077`；
- artifact ZIP SHA256：`b109baee713b7b7601fa06da53877fbfdd6bfd633de486256563202f2cf6eb79`；
- 实际输入：540 tokens；
- 实际输出：213 tokens；
- 推理回执耗时：约 31.02 秒。

完整输入、request、raw answer、parsed review、task-gate result、runtime identity 与 server log 已保存到本目录 `results/`。artifact 在分支写入之前完成上传，因此即使后续分支投递发生竞争，原运行仍有独立证据副本。

## 下一步判断

一个 pass 足以说明“任务包装值得继续”，但不足以说明修复已经泛化。最小下一步应是**针对另外两个不同历史失败类型的既有候选做确认性回归**：

- 一个此前出现 instruction / brief leakage 的候选；
- 一个此前出现 circular grounding 的候选。

仍使用同一冻结包装、每个候选独立请求、无重试、无新名称；若任一输出为 `block` 或 `review`，停止扩大并回到任务包装诊断。若两项均 pass，则可以更有根据地认为 Reviewer 的最低任务理解层已在这三个不同失败类型上恢复，之后才研究“语义判断本身是否正确”。

本轮不改变 Simple vs redesign 的方法胜负，不恢复 IA / G0–G8，不晋升 Adaptive Naming Skill，不合并 #416。
