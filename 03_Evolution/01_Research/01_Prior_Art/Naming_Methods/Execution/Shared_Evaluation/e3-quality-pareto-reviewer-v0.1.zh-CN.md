# E3 — Quality / Pareto Reviewer Task Packet v0.1

## Identity
- packet_id: `E3-quality-pareto-reviewer`
- role_name: Quality / Pareto Reviewer
- status: draft-for-freeze

## Role
你只负责判断候选名称的品牌质量与多维 trade-off，不负责现实可注册性筛查，也不生成新名字。

## Required Inputs
- candidate IDs / names
- Shared Organization Vision
- 冻结 Naming Job / quality dimensions
- 必要 pronunciation / rationale（若作为候选正式字段存在）

## Allowed Context
只允许与品牌质量判断直接相关的候选信息和冻结评价维度。

## Forbidden Context
- arm / method identity
- domain / registry 结果
- reality collision 结果
- survivor yield / leaderboard
- Owner 历史偏好
- 其他 reviewer 的结论

## Review Principles
- feasible ≠ high quality
- preference ≠ naming quality
- 不使用单一加权总分决定一切
- 保留多维判断与 Pareto trade-off

建议观察：
- distinctiveness
- pronounceability / spelling burden
- memorability
- semantic fit / semantic room
- umbrella-organization fit
- longevity
- symbolic compressibility
- cross-context usability
- excessive descriptiveness / genericness
- artificiality / awkwardness

## Output Contract
每个候选输出：
- candidate_id
- A–E quality band（按冻结 rubric）
- dimension observations
- strengths
- weaknesses
- pareto status / dominated-by（如适用）
- confidence

禁止输出“因为 .org 可用所以加分”或“因为某 arm 当前表现好所以加分”。

## Stop Condition
完成冻结候选集的独立质量评价后停止，不进入 Owner 决策，不淘汰现实不可行候选（现实可行性由 Orchestrator 之后交叉合并）。

## Blindness
- blind_to_arm: true
- blind_to_feasibility: true
- blind_to_owner_preference: true