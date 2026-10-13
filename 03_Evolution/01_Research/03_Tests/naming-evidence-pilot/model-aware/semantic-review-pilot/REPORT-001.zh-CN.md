# SEM-408-001：跨模型单候选语义审查 — 接口失败记录

状态：6 次真实 Gemma 3 4B 单候选推理均完成，但 6/6 输出不是约定 JSON，全部按冻结解析规则阻断。因此本轮**没有可用 reviewer disposition，不能用于评价候选、比较 Qwen/Gemma 或判断方法语义质量**。

## 1. 冻结条件确实执行

- 只复用 REAL-408-003 `cell-2-simple-411921` 六个既有虚构产品名称，0 新名称；
- reviewer 为 `ggml-org/gemma-3-4b-it-GGUF` Q4_K_M，精确 revision `d0976223747697cb51e056d85c532013931fe52e`，权重 SHA256 `882e8d2db44dc554fb0ea5077cb7e4bc49e7342a1f0da57901c0802ea21a0863`；
- 每个请求只含冻结 brief + 一个裸名称，不含 Qwen 决定、v95 队列、creator pronunciation/meaning/derivation/risk、其他候选、现实筛查或 Owner 偏好；
- temperature 0.2、top_p 0.9、seed 63001，每项最多 900 输出 tokens，未重试。

运行 `34718595007` 的 validation / setup / six-review execution / evidence persistence 均成功。成功指执行与保存成功，不表示 reviewer 任务成功。

## 2. 实际失败是什么

`summary.json` 中 C001–C006 全部为 `blocked`，错误均为 JSON decode error。原始输出显示 reviewer 没有输出评审对象，而是把结构化任务本身当作待分析文本。例如 C001 从“Okay, let's break down this incredibly detailed and layered piece of text”开始，C002从“This is an incredibly complex and well-structured piece of text”开始，随后总结任务结构与规则。

因此这里不是“Gemma 认为六个名字都不好”，也不是“Gemma 不会命名评审”。本轮测到的是**当前任务包装对该模型不足以让其进入执行姿态**。不能从这些自然语言总结中人工抽取一个 disposition，也不能由 ChatGPT补写成合规 JSON。

## 3. 下一次最小修复

新实验编号 SEM-408-002 保持候选、brief、blindness、reviewer模型、采样与评价维度不变，只修任务执行接口：

1. 增加明确 system 指令：执行用户提供的 naming-review task，不要总结任务，只返回约定 JSON；
2. 使用冻结 llama.cpp 已支持的 `json_schema` completion 约束，确保输出只能采用目标结构；
3. 原 SEM-408-001 保持 blocked，不追认、重评分或复用其自然语言输出作为语义判断。

JSON schema 只约束表示，不构成语义正确性证明。若 SEM-408-002 能结构完成，才第一次有资格比较独立 reviewer 的 intrinsic observations；跨模型一致仍不等于质量真值。
