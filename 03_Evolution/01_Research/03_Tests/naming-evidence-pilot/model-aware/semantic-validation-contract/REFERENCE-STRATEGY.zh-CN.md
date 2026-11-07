# SEM-408 参考验证策略：把强模型变成校准器，而不是流水线必经成本

## 1. 目标

本策略解决两个问题：

1. 如何验证小模型的语义判断，而不是让另一个模型简单投票；
2. 如何避免把昂贵强模型变成每个候选都必须调用的生产依赖。

原则：**cheap model 做大规模探索，deterministic checks 做硬边界，strong/independent reference 只做小样本校准；Owner 只承担真正的偏好与采用判断。**

## 2. 不同 claim 使用不同参考来源

| Claim | 首选参考 | 强模型是否必须 | 说明 |
|---|---|---|---|
| 可见拼写/结构 | deterministic / 人工直接观察 | 否 | 不需要模型替代肉眼可确认事实 |
| 可能读音 | 独立语言判断；必要时真人读写测试 | 否 | 模型只能提出候选读法 |
| 构词/词源 | 字典/来源或标为 hypothesis | 否 | 没来源就不能升成事实 |
| 用户联想 | 独立盲评/小样本人类测试 | 可选 | 强模型意见只是参考，不是用户事实 |
| brief fit | 独立高能力参考评审 + 冻结 rubric | 建议小样本使用 | 这是最适合强模型做周期校准的部分 |
| priority/hold | 由已验证 claim + 稳定性规则合成 | 否 | 不允许一个模型直接变成质量真值 |
| Owner 偏好 | Owner 明确反馈 | 否 | 任何模型都不能替代 |
| 商标/域名/现实 | 权威工具/来源 | 否 | 强模型也不能代替现实证据 |

## 3. 推荐的成本结构

### A. 日常生产：低成本

- simple 生成作为默认；必要时才展开 redesign。
- 小模型负责生成候选、创造意图、初步 surface/association hypotheses。
- deterministic contract 过滤任务理解错误、证据越界、格式问题。
- selector 只做 conservative triage；不稳定或证据不足进入 hold。

这一层不需要强模型常驻。

### B. 周期校准：小样本强参考

不是“每 100 个候选调用 100 次强模型”，而是抽取冻结的小型 benchmark packet，例如本轮 `SEM-408-REF-PACKET-001` 的 4 个已有候选。

独立高能力参考只评价冻结 packet，主要检查：

- 小模型有没有把 hypothesis 当事实；
- brief-fit 理由是否候选相关；
- hard failure 是否真的有依据；
- 小模型 priority/drop 是否出现系统性错误。

强参考本身仍不是绝对 ground truth。若强参考之间明显分歧，结论应是“这个维度主观/不稳定”，而不是强行挑一个答案。

### C. Owner：只在高价值节点介入

Owner 不负责替模型做日常 QA。Owner 应集中在：

- 真实组织任务的候选偏好；
- 语义取舍无法从任务 brief 推导时；
- 最终 shortlist / finalist；
- 商业价值与采用。

## 4. 本地 30B/MoE 应放在哪里

Owner 的本地 30B/MoE（例如 qwen3.6-30b-a3b 类部署）**当前不能因为参数更大就自动当 reference truth**。它应该先作为一个独立 tier 做角色实测：

- generation：是否比 4B 明显提高优质候选率或搜索空间；
- semantic association：是否减少 hallucinated derivation / unsupported claims；
- resource triage：是否提高顺序稳定性；
- final selector：只有前面证据成立后才考虑。

如果 30B 能稳定承担 triage，就可以显著减少强云模型的校准频率；如果不能，也不会因为本地免费就让它自动掌握最终裁决权。

## 5. 当前最小下一步

`SEM-408-REF-PACKET-001` 已冻结，不含方法标签、旧判断、generator risk 或实验 provenance 元信息。

在真正执行参考评审前，只剩一个资源选择问题：

- **独立高能力模型**：适合验证 brief-fit / semantic calibration，成本较高但只需小样本；
- **Owner 本地 30B/MoE**：适合先测试是否能从 4B 上升为可靠中间层，但不能作为唯一 reference；
- **人工/语言测试**：适合读音、恢复性和真实用户联想，不需要强模型替代。

因此后续不应再用同一 4B Reviewer + 更多 prompt 修补。应根据要验证的 claim 选择对应 reference source。
