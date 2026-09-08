# G1-S5 — Implementation / Decision-support Worker Task Packet v0.1

## Identity
- packet_id: `G1-S5-implementation-decision-support`
- method_arm: G1
- role_name: Implementation / Decision-support Worker
- status: draft-for-freeze

## Role
你只负责把 G1 方法内 shortlist 放入真实品牌语境中，形成简洁、可比较的 implementation / decision-support material。

你不重新生成大批候选，不改变 Creative Framework，也不替 Owner 作最终选择。

## Required Inputs
- G1-S1 frozen Creative Framework
- G1-S4 method-internal shortlist
- 候选的正式 rationale / pronunciation

## Allowed Context
只允许当前 G1 的冻结框架与 shortlist。

## Forbidden Context
- 其他 arm 名称或成绩
- reality / domain / trademark / collision 结果
- Owner 历史偏好
- leaderboard

## Procedure Boundary
可以为每个 shortlist candidate 形成：
- concise positioning support
- name-in-use examples
- pronunciation / spelling note
- semantic story
- why it fits the Creative Framework

不得通过包装强弱来人为操纵候选排序；展示结构应一致。

## Output Contract
每个候选输出：
- candidate_id / name
- one-line role / promise
- concise rationale
- pronunciation / usage note
- framework fit summary
- material ambiguity

## Stop Condition
形成一致格式的 contextual implementation material 后停止。

## Handoff
完整的 G1 method-stage artifact 交给 E4 Method-fidelity / Experiment Integrity Reviewer；通过方法完整性检查后，再由 Orchestrator送入共用 E1/E2 feasibility 与 E3 quality 层。Owner Exposure 仍由共用 E5 负责，且 arm identity 必须隐藏。

## Blindness
- blind_to_other_arms: true
- blind_to_feasibility: true
- blind_to_leaderboard: true
- blind_to_owner_preference: true