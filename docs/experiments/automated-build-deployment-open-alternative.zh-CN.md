# 自动构建与部署：开放替代方案支持性实验

状态：初始实验

## 目的

这不是测试 InteropAtlas（Atlas）能否自行推理，而是测试：**Atlas 当前保存的结构化事实，是否已经足够支持确定性 Engine 或上层 Agent 回答一个真实问题。**

真实问题：

> InteropAtlas Engine v0.1 需要自动构建与部署。当前候选实现包含 GitHub Actions。Atlas 是否已经提供足够事实，使外部查询/分析层能够发现开放、可自托管的替代实现？

## 当前输入事实

Scenario：`engine_v0_1_bootstrap`

Requirement / Capability：`automated_build_deployment`

已收录 Implementation：

- `github_actions`
  - `kind: platform_service`
  - `open_source: false`
  - `self_hostable: false`
  - capability: `automated_build_deployment`
- `forgejo_actions`
  - `kind: platform_service`
  - `open_source: true`
  - `self_hostable: true`
  - capability: `automated_build_deployment`

已收录 Relation：

- `forgejo_actions --alternative_to--> github_actions`
- capability context: `automated_build_deployment`

## 当前可以确定性回答的内容

在不进行语义推理的前提下，一个查询层已经可以：

1. 从 Scenario 找到 `automated_build_deployment` 能力需求；
2. 找到声明提供该能力的 Implementation；
3. 按 `open_source`、`self_hostable` 等结构化属性过滤；
4. 找到 GitHub Actions 与 Forgejo Actions 之间已记录的 `alternative_to` 关系。

因此，Atlas 当前数据已经足以支持以下**事实型查询结果**：

> 对 `automated_build_deployment`，当前 Atlas 中存在一个被记录为开源且可自托管的 Implementation：Forgejo Actions；它同时被记录为 GitHub Actions 的替代方案。

## 当前不能直接推出的内容

Atlas 当前数据还不足以仅凭确定性查询可靠推出：

- Forgejo Actions 对某个具体项目是否是“足够好的”替代方案；
- 两者兼容程度是多少；
- 工作流迁移需要多少修改；
- 是否依赖专有 API、Marketplace Action 或 GitHub 特有上下文；
- 治理开放性、数据可迁移性、生态成熟度是否满足某个 Openness Policy；
- 在特定 Scenario 约束下是否应判定为 `Open Gap: NO`。

这些问题需要更多结构化事实、明确规则，或上层 Agent / Human 的判断。

## 本轮暴露出的第一个模型缺口

`open_source: true/false` 与 `self_hostable: true/false` 只能描述实现开放性的两个维度，**不能等价于“开放替代方案成立”**。

因此当前阶段不应让 Atlas 写入一个静态的 `Open Gap: NO` 结论。

后续应继续通过真实案例逐步确定：哪些开放性维度属于事实，哪些属于 Policy，哪些属于动态 Assessment。

## 实验结论

本轮结果为：**部分支持（PARTIAL）**。

Atlas 已能支持“发现候选开放实现”的确定性查询，但还不能仅凭现有事实可靠完成“开放替代方案是否充分”或“是否存在 Open Gap”的最终判断。

这正是实践反馈环需要记录的负向数据：现有模型不是失败，而是通过真实问题暴露了下一层需要补充的语义。
