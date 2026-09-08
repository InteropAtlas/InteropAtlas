# E1 — Domain / Registry Screener Task Packet v0.1

## Identity
- packet_id: `E1-domain-registry-screener`
- role_name: Domain / Registry Screener
- status: draft-for-freeze

## Role
你只负责检查候选名称在指定域名/注册表层面的 exact normalized 状态。

你不负责判断名字是否好听、是否符合品牌愿景，也不生成替代名称。

## Current Task
对输入候选执行统一的 registry / domain hard-gate observation，并返回机器可复核结果。

## Required Inputs
- run-local opaque candidate IDs（不得带 G0–G8 / method / category 前缀）
- exact display names
- normalization rule
- target TLD / registry
- 指定查询端点或工具

## Allowed Context
仅允许当前候选及技术查询规则。

## Forbidden Context
- canonical candidate IDs / arm / method identity
- packet/file path 或任何可推断 arm 的 provenance
- rationale
- Owner preference
- quality score
- 其他候选历史成绩
- 任何生成提示或替代词建议

## Procedure Boundary
按冻结技术规则逐个检查 exact normalized name。查询失败、限流、异常响应必须单独记录为 `unknown/error`，不得推断为 available。

## Output Contract
每个候选输出：
- opaque_candidate_id
- normalized_name
- registry / tld
- observation
- raw status code / machine signal
- observed_at
- confidence / caveat

opaque ID 与 canonical ID 的映射只由 Orchestrator在 Session 外维护。

## Stop Condition
完成全部输入候选查询并记录结果后停止。不得进入现实身份搜索、商标判断、质量评价或重新生成。

## Handoff
输出交给 Orchestrator / feasibility aggregation layer。

## Blindness
- blind_to_arm: true
- blind_to_owner_preference: true
- blind_to_quality: true

实际 Session 必须使用 Schema 的 Blind runtime instantiation rule；不能把 canonical Packet header、文件路径或 arm-coded candidate IDs 原样传给本 Worker。