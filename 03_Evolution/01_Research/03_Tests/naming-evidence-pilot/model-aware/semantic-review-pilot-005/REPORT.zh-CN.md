# SEM-408-005：两类历史失败确认与 Gate False Negative

## 结论

本轮按 snapshot v97 冻结计划，只对两个**既有 DEV-02 候选**进行确认性回归：

- C002 / Diffly：历史上出现 brief / instruction 内容泄漏；
- C006 / Sublyte：历史上出现循环 candidate grounding。

SEM-408-004 的任务包装保持不变，每项独立请求、无重试，计划要求“首项非 pass 即停止”。实际旧版 task gate（v1）把 C002、C006 都判为 `pass`，因此两次请求均被发送。

**事后检查发现两个 `pass` 都是假阴性（false negative）。因此本轮不是 Reviewer 任务理解修复成功，而是证明 v1 gate 本身仍不充分。** 原始 gate 结果保持不改；后续只允许以新版本 gate 另行重放，不得静默覆写历史结果。

## C002：brief 元信息泄漏没有被 v1 捕获

C002 的输出把任务简报中的 `虚构的 / fictional` 当成候选语义依据：

- association hypothesis 直接解释 `虚构的`；
- brief-fit 与最终 reason 又以“fictional tool”影响名称适配判断。

`虚构的`在这个开发任务里只是**合成任务的 provenance / 元信息**，不是 Diffly 的词形、产品功能或用户语言联想。v1 gate 只识别固定的 `frozen brief`、`validation` 等英文指令词，没有任务本地的 provenance-aware context，因此漏判。

这也意味着：由于 C002 被旧 gate 错判为 pass，冻结的“首项非 pass 即停止”没有触发，C006 随后被发送。第二次请求仍在原先最大预算 2 次以内，但 stop policy 在 gate false negative 下没有发挥预期作用。

## C006：直接复述任务边界没有被 v1 捕获

C006 的最终 `reason` 几乎逐字复制任务边界：名称是 identity label、不是 product implementation、不应要求名称实现或枚举功能、brief 只是 comparison context 等。

这是明确的 instruction echo，不是候选级判断依据。v1 gate 只在 `observable_form` 与 `association_hypotheses` 中搜索部分 instruction leak，并没有对 `reason / brief_fit` 做结构化指令重合检查，因此再次产生 false negative。

此外，C006 的其他文本还包含 underwater technology、unique/distinctive 等未经验证的语义判断。它们属于后续“语义正确性”问题，不需要靠 task-understanding gate 一次解决；本轮最明确的失败已经是最终理由复制任务指令。

## Gate v2 修订

因此 `semantic-review-task-gate/gate.py` 升级到 `2.0-experimental`，增加两个**可选、任务本地**的 provenance 输入，而不是硬编码某一个开发任务：

1. `context_only_terms`：由任务构建者明确标记只能作为 provenance / synthetic metadata、不得成为候选语义的词或短语；
2. `instruction_texts`：对输出进行至少 6 token 的结构化重合检查，用于发现较长的 instruction echo，同时避免因为短语如 “against the brief” 就误伤正常比较。

新增匿名控制例：

- context-only metadata 泄漏 → `block`；
- 长段 instruction echo → `block`。

历史结果不改写。Gate v2 的重放目标是：

- SEM-408-004 / C003 原 canary 仍为 `pass`；
- SEM-408-005 / C002 由原 v1 `pass` → v2 `block`，理由为 context-only metadata leakage；
- SEM-408-005 / C006 由原 v1 `pass` → v2 `block`，理由为 instruction echo。

这只是对**任务理解资格**的更严格后验分类，不代表 C002/C006 名称质量差，也不重写模型原 disposition。

## 实际执行与证据

- run：`34744595667`；
- job：`103690048899`；
- source commit：`57c2a9dbe18a814651542aa448da630815ffba8c`；
- evidence commit：`160f376edbf139b32b6f89917b640dc0bfe4b2c1`；
- artifact：`10314065187`；
- artifact ZIP SHA256：`279143b544d837865818c7ab0743db55ddf63872c41325ad8c970bd1e1bb9fec`；
- 实际 Reviewer 请求：2；
- 重试：0；
- 新名称：0；
- 付费推理 API：0；
- C002：538 input tokens / 321 output tokens / ~49.18 s；
- C006：540 input tokens / 308 output tokens / ~48.87 s。

本轮仍没有 quality ground truth，没有现实筛查，也没有方法 winner。

## 下一步

**停止继续调用 Reviewer 模型。** 先完成 Gate v2 的离线控制与 SEM-408-004/005 重放，并把 false-negative 事实写入 state。只有新 gate 的 deterministic regression 全部通过后，才讨论是否还值得增加真实 Reviewer 请求。

即使 Gate v2 工作正常，下一阶段也应从“任务理解是否正确”进入“语义判断是否正确”，不能把不断扩张 gate 规则本身当成最终 Naming Method。Simple vs redesign 的方法比较不因本轮发生胜负变化；Adaptive Naming Skill v0.4.0 不晋升，#416 不合并，IA / G0–G8 继续暂停。
