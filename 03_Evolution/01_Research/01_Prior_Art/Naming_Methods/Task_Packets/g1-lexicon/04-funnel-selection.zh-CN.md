# G1-S4 — Funnel / Selection Worker Task Packet v0.1

## Identity
- packet_id: `G1-S4-funnel-selection`
- method_arm: G1
- role_name: Funnel / Selection Worker
- status: draft-for-freeze

## Role
你负责把 Creative candidates 与 Linguistic Engineering observations 汇流，按冻结 Creative Framework 做第一轮方法内选择。

你不做现实搜索，不生成大量新候选，也不看其他 arm。

## Required Inputs
- G1-S1 frozen Creative Framework
- G1-S2 formal candidates
- G1-S3 linguistic engineering outputs

## Allowed Context
只允许当前 G1 的上述结构化产物。

## Forbidden Context
- 其他 arm
- domain / trademark / reality screening
- Owner preference
- benchmark成绩
- 其他 evaluator 结果

## Procedure Boundary
Selection 依据：
- 与 Creative Framework 的 fit
- original-in-context / accessibility / unexpectedness 的平衡
- linguistic engineering observations

不得因为某名称“看起来可能更容易注册”而提前偏好；现实可行性属于下游独立评估。

## Output Contract
每个候选输出：
- candidate_id
- framework_fit
- linguistic_summary
- keep / hold / drop
- rationale
- unresolved ambiguity

同时输出一个 method-internal shortlist，保留 provenance 与原始 order。

## Stop Condition
完成方法内 funnel / shortlist 后停止。

## Handoff
method-internal shortlist **必须先交给 G1-S5 Implementation / Decision-support Worker**，完成 G1 方法内的 contextual implementation 阶段。不得从 S4 直接跳到 E4 或共用 feasibility / quality 层。

## Blindness
- blind_to_other_arms: true
- blind_to_feasibility: true
- blind_to_owner_preference: true