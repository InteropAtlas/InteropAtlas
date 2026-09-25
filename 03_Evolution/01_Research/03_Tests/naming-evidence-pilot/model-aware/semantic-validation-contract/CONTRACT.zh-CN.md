# SEM-408：语义判断有效性合同与小模型角色边界

状态：实验方法合同；不属于稳定 Adaptive Naming Skill。Primary Home：#408。当前不授权新 Reviewer 推理、IA 名称生成、付费调用、购买注册、合并或稳定晋升。

## 1. 为什么需要这一层

现有实验已经证明，**任务理解通过不等于语义判断正确**。

- SELECT-408-001 中，同一候选会因生成者解释不同而出现缺少依据的相反判断；去掉 risk 输入能减少部分风险传播，但仍出现未经查证的许可/现实措辞与同名矛盾判断。
- SELECT-408-002 中，同一 seed 仅改变候选顺序，6 个候选中 4 个发生决定变化；因此当前小模型选择器不能当作稳定质量裁判。
- SEM-408-003 中，Reviewer 出现把名称当产品实现、把 brief/instruction 当候选证据和循环陈述等任务层错误。
- SEM-408-004 的单项 canary 在修正任务包装后通过 task gate，但这只证明该次输出没有触发已知任务理解错误。
- SEM-408-005 的两个结果在 Gate v1 下都 pass，但人工检查发现 context-only 元信息泄漏与长指令复述；Gate v2 后验重放均 block。说明继续堆 prompt/正则本身不能替代“语义正确性”验证。

因此以后所有模型语义输出都必须经过下面的分层，不能从结构完成或 task-gate pass 直接升级为质量证据。

## 2. 五层验证

### L0 — Task Understanding / 任务理解

检查 Reviewer 是否知道自己在评价一个名称/identity label，而不是要求名称本身执行产品功能；同时检查指令、实验 provenance、context-only 元信息是否被误当成候选属性。

L0 只能回答：**这份回答有没有明显理解错任务。**

它不能回答名字好不好。

### L1 — Candidate Grounding / 候选依据

每个观察必须能追溯到：

- 可见拼写/结构；或
- 明确提供、允许使用的候选事实。

不得把模型自行发明的词源、构词故事、用户联想写成事实。无法从裸名确认的内容必须降级为 hypothesis / unknown。

### L2 — Claim Calibration / 主张校准

将语义内容明确分为：

- observable：直接观察；
- hypothesis：可能联想，需要验证；
- supported：已有独立证据支持；
- unknown：目前不知道。

尤其是 pronunciation、cross-language recoverability、association、derivation、semantic fit，不能因为模型说得流畅就自动进入 supported。

### L3 — Comparative Reliability / 比较可靠性

模型要承担 priority/drop 等资源分流时，必须在冻结候选与简报的前提下接受受控扰动：例如顺序变化、独立重复或其它预先定义的无关变量变化。

- 一致：可以作为相对资源分流的一个证据；
- 不一致：必须进入 hold，不允许自动 drop；
- 不得把“一致”解释成质量真值。

### L4 — Human / External Validity / 人与现实有效性

以下事项不能由裸模型输出自行确认：

- 用户会如何理解或发音；
- 中文/英文跨语言恢复负担；
- Owner 实际偏好；
- 公司/产品撞名；
- 商标、域名、法律状态；
- 最终采用。

必须使用对应的人类反馈、实际测试或权威外部证据。最终采用仍是 Owner Gate。

## 3. 小模型当前角色边界

### 可以继续使用，但只能作为“提案者”

**Candidate Generation**：允许生成候选和创造意图。REAL-408-003 已证明小模型能产出一部分值得继续看的探索材料，但没有证明复杂路线或 simple 在质量上胜出。生成者自己的 risk、词源和用户联想都不能自动变成筛选事实。

**Surface Observation**：在 L0–L2 满足时，可以提出拼写、读写、可能发音等观察；跨语言和真实发音仍需独立验证。

**Semantic Association**：可以提出 association hypotheses，默认证据等级为 hypothesis，对质量分数自动影响为 0。

### 可以承担保守资源分流，但不能当裁判

**Resource Triage**：只有在 L0–L3 满足后，允许用于 priority / hold 的保守分流。任何顺序敏感、理由冲突或证据不足的候选都进入 hold。当前不授权模型单独自动 drop。

### 当前不能自动承担

**Final Quality Selector**：现有 4B 实验已经出现顺序敏感、同名矛盾、unsupported association 和 task/gate failure，因此不允许把其输出视为“哪个名字更好”的独立真值。

**Reality / Legal / Domain Clearance**：没有权威工具数据时，语言模型只能整理证据，不能宣布 clearance。

**Owner Preference**：只有 Owner 明确反馈是事实；模型推断必须标为 reversible hypothesis。

**Final Adoption**：Owner only。

## 4. 对 Simple vs Redesign 的影响

当前结论不变：

- Simple：下一开发默认基线；
- Redesign / 三路线：需要扩展搜索空间时的可选探索方式；
- winner：not established。

复杂路线在现有 DEV-02 中有非常弱的 priority 数量优势，但评审敏感；同时生成阶段约 2.28 倍 tokens、1.66 倍时间。由于当前 selector/reviewer 还不足以建立质量真值，不能用这些模型判断把弱倾向升级为“复杂系统更好”。

## 5. 未来怎样真正验证“语义判断正确”

下一次语义验证必须预先冻结一个 validation packet，并满足：

1. **固定对象**：候选、brief、允许上下文、禁止上下文、评价维度和输出合同在运行前固定。
2. **独立参考**：至少有一种不依赖被测小模型的参考证据；可以是独立高能力参考模型、隔离人工评审、语言/用户测试，按 claim 类型选择，不要求每项都用强模型。
3. **逐 claim 对齐**：比较的不是“最后都 hold 所以一致”，而是每个具体 observation / association / fit reason 是否有依据、是否校准为正确的 evidence class。
4. **稳定性单独记账**：顺序/重复稳定性与语义正确性分开。稳定但错误仍是错误。
5. **角色级结论**：只允许得出“这个模型在这个角色、这个任务族、这个配置下达到什么证据等级”；不能从 4B 测试外推到 Owner 的 30B/MoE 或所有小模型。

### 最小成功条件

若未来要让小模型成为自动 `resource_triage`，至少需要：L0、L1、L2 均通过，L3 在预先设定的扰动中达到可接受稳定性，并由独立参考确认没有系统性 unsupported-hard-drop。

若未来要让小模型成为 `final_quality_selector`，除上述条件外，还需要跨任务留出验证和独立质量参考。当前证据距离这一条件明显不足，因此该角色保持关闭。

## 6. 当前停止条件

在 validation packet 和 reference strategy 冻结前：

- 不再增加 Gemma/Qwen Reviewer 请求；
- 不继续给 Gate 增加针对单个样本的补丁；
- 不用 ChatGPT 事后意见伪装成独立 ground truth；
- 不恢复 IA 正式命名；
- 不改变 Simple 默认 / Redesign 可选的工程选择；
- 不晋升 Skill v0.4.0。

机器可读角色边界见 `role-boundary.json`；确定性合同检查见 `validate.py` 与 `test_validate.py`。这些检查证明的是方法边界自洽，不是命名质量。
