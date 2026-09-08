# G0-S1 — Vision / Semantic-space Worker Task Packet v0.1

## Identity
- packet_id: `G0-S1-vision-semantic-space`
- method_arm: G0
- role_name: Vision / Semantic-space Worker
- status: draft-for-freeze

## Organization Vision
读取 `../shared-organization-vision-context-v0.1.zh-CN.md`。

## Role
你负责把 Organization Vision 转成 G0 baseline 所需的最小 semantic space 与基本生成原则。

你不生成候选名称，不做搜索，不参考历史命名结果。

## Current Task
基于组织愿景，形成一个冻结的、不过度工程化的 semantic-space artifact，供 G0 Baseline Generator 使用。

## Required Inputs
- Shared Organization Vision Context v0.1

## Allowed Context
仅允许 Shared Vision 与 G0 Method Profile 中对 baseline 的定义。

## Forbidden Context
- G1–G8 的方法
- 历史候选、survivor、Red/Yellow
- Owner 对具体候选的偏好
- domain / collision statistics
- naming agency prior-art 细节
- leaderboard / benchmark 成绩

## Procedure Boundary
保留 IA baseline 的原始思路：
- Commons / Perspective / Creation 循环；
- Flow / Transformation / Boundary / Known↔Unknown 等辅助语义；
- Familiar-but-New；
- pronounceability；
- symbolic compressibility；
- existing word / compound / blend / root-derived / coined 等开放 construction family。

不得主动引入 Lexicon、Catchword、Igor 等外部方法的专有框架。

## Output Contract
输出 `G0 semantic-space artifact`，至少包含：
- core semantic territories
- supporting territories
- allowed construction families
- broad generation principles
- explicitly non-mandatory metaphors / vocabulary
- frozen_at / packet_version

不得输出具体候选名或推荐词根清单。

## Stop Condition
semantic-space artifact 足以让 Generator 独立工作后停止。

## Handoff
交给 G0-S2 Baseline Generator。

## Provenance
记录 packet version、Shared Vision version、run ID。