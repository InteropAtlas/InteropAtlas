# v95 / SELECT-408-002：固定候选选择稳定性与顺序交叉检查

状态：固定候选稳定性试验已完成；观察到显著顺序敏感。实验工作流已据此接入保守的同 seed 正序/反序交叉检查。没有新增名称，没有现实核查，没有质量真值，也没有稳定方法晋升。

发起：Owner 在 v94 后要求继续。执行：OpenAI / ChatGPT / GPT-6 Astra Pro；模型判断由 Qwen3-4B-Instruct-2507 / Q4_K_M 在公开 GitHub CPU runner 实际完成。执行者事后分析不是独立语义评审。执行前冻结见 #408 comment `5648508810`；实际运行 `34717382400`；原始证据位于 `results/evidence.json`。

## 1. 实验控制与实际结果

只复用 REAL-408-003 `cell-2-simple-411921` 的六个既有虚构产品候选。brief、suggested pronunciation、creator intent、evidence rules、output contract、模型权重、runtime、temperature=0.7、top_p=0.9 均固定；生成者 risk 不进入 selector。只改变 items 顺序与 sampling seed。

四个预注册条件：

1. 原始顺序 / seed 52001；
2. 原始顺序 / seed 52002；
3. 反向顺序 / seed 52001；
4. 反向顺序 / seed 52002。

四次请求均真实发出，无重试、无人工修答案、无新增名称、无计费推理 API。请求 1、3、4 结构有效；请求 2 返回包含非法控制字符的 JSON，解析失败，原文保留，不能追认为有效结果。因此完整 2×2 factorial 被删失，不能完整估计 seed 效应。

### 同 seed 52001，仅改变候选顺序

| ID | 原始顺序 | 反向顺序 |
|---|---|---|
| C001 | keep | drop |
| C002 | hold | keep |
| C003 | keep | keep |
| C004 | hold | drop |
| C005 | keep | hold |
| C006 | keep | keep |

**4/6 改判。** 这是本轮最明确的诊断：在完全相同 seed、brief、intent 与模型条件下，仅倒转批次顺序即可大幅改变资源决策。

### 同为反向顺序，仅改变 seed

seed 52001 与 52002 相比，仅 C003 从 keep 变 hold，**1/6 改判**。由于原始顺序/52002 无效，不能据此声称 seed 普遍只有 1/6 影响，也不能作统计显著性判断。

三个有效请求中，只有 C006 始终 keep。这只是稳定性观察，不表示 C006 语义上正确或可采用。

## 2. 工程响应：保守顺序交叉，而不是更长提示词

单次批量 selector 不再作为 priority/drop 的单点依据。实验 `selection_policy.py` 升为 `0.3.0-experimental`，新增 `order_crosschecked_queues()`：

- 同一候选池、相同 seed，正序和反序都 `keep` → `priority`；
- 两次都 `drop` → `not_pursued`；
- 任一 `hold` 或两次决定不一致 → `hold`。

对本轮 seed 52001 的两次真实输出做确定性重放得到：

- priority：C003、C006；
- hold：C001、C002、C004、C005；
- not_pursued：空。

这是一种**保守资源分配**，不是真值投票。顺序一致只说明同一模型在这两个排列中一致，不能代替独立专家、用户测试或现实核查。

实验 `workflow.py` 已把旧的抽样 rejection audit 默认步骤替换为：name-only 观察 → explained 正序 → explained 反序（同 seed）→ 保守聚合。redesign 仍显式可选，simple 仍是开发默认。旧实验由 source hash / policy version 保护，不以 v95 重解释历史结果。

确定性回归与实际稳定性结果重放均通过；接线过程不调用语言模型。原 Adaptive Naming Skill v0.4.0 未改变，#416 仍为 Draft。

## 3. 仍未解决的问题与下一步

### 3.1 稳定不等于正确

本次没有独立质量真值。即使两个顺序都 keep，也可能是同一模型稳定地犯同一个错误；两个顺序不一致也不说明候选本身差。交叉检查只降低单个批次排列直接控制资源投入的风险。

### 3.2 自由文本语义理由仍可能自相矛盾

v94 已观察到同名在不同池中出现相反的“自然/不自然”等理由。本次主要测决定稳定性，没有证明这些理由可靠。程序能够隔离 creator risk 和 verified facts，但不能靠 schema 证明自由文本判断为真。

### 3.3 下一阶段应验证语义判断，而不是继续加规则

下一项研究应使用既有候选、冻结 brief 和候选信息，建立**独立于当前 selector 输出的语义质量验证**，重点比较名称观察、creator intent 与需要实证的用户联想。优先使用可配置、明确记录身份的 reviewer；不得把当前 ChatGPT 隐藏成运行时兜底，也不得把同源自评冒充独立评审。

在该证据出现前：不恢复 IA 正式命名，不扩大生成，不宣称 Qwen3-4B selector 已可靠，不晋升稳定方法，不合并 #416。
