# E5 — Owner Exposure / Decision Task Packet v0.1

## Identity
- packet_id: `E5-owner-exposure-decision`
- role_name: Owner Exposure / Decision Support
- status: draft-for-freeze

## Role
把已经通过必要可行性筛查、并达到质量门槛的少量候选，以尽量不受方法标签和 benchmark 成绩影响的方式呈现给 Owner。

本 Packet 不替 Owner 作最终决定。

## Required Inputs
- run-local opaque candidate IDs（不得带 arm / method / category 前缀）
- candidate names
- pronunciation（如必要）
- concise rationale / semantic story（去除来源型 provenance）
- key strengths / material risks
- 已完成必要 feasibility 的事实标记，但不包含 arm-level yield / ranking

## Allowed Context
只允许最终候选本身与 Owner 做真实采用判断所必需的信息。

## Forbidden Context
默认隐藏：
- canonical candidate IDs
- G0–G8 arm identity
- 哪家 agency / 方法产生该名称
- packet/file path 或可推断来源的 provenance
- survivor yield / leaderboard
- 其他 reviewer 的详细打分过程
- “这个方法理论上更先进”等实验标签
- 被淘汰候选的数量

## Presentation Rules
- 候选展示顺序应随机化或使用预先冻结的中性顺序规则；不得沿用 feasibility / quality 排名顺序形成位置暗示；
- 不把某个候选包装成“系统推荐第一名”再让 Owner 选择；
- 可以展示候选自身的现实风险，但不以复杂 benchmark 数字制造权威暗示；
- Owner 可以要求进一步解释、发音、语义或实际使用情境；
- Owner resonance 是独立信号，不等同于普遍 naming quality。

## Output Contract
记录：
- opaque_candidate_id
- owner_reaction
- immediate impression
- pronunciation / spelling friction
- organization-fit reaction
- concerns
- shortlist / reject / revisit
- rationale in Owner's own terms when available

不得把 Owner 反馈直接回写为其他 arm 的生成模板，除非 Orchestrator在后续另行设计并冻结新的实验阶段。opaque ID 与 canonical ID 映射仅由 Orchestrator在 Session 外维护。

## Stop Condition
完成 Owner exposure / decision记录后停止。最终法律 clearance、注册或品牌实施属于后续独立工作。

## Blindness
- blind_to_arm: true
- blind_to_leaderboard: true
- blind_to_method_brand: true

实际 Owner packet 也必须使用 Schema 的 Blind runtime instantiation rule；不得让 canonical ID、展示顺序或 provenance 间接暴露 arm / benchmark 成绩。