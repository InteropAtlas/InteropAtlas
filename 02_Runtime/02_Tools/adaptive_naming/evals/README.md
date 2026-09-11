# Adaptive Naming Regression Evals

本目录用于 **Skill 行为回归测试**，不是重新启动 G0–G8 benchmark，也不比较哪种命名方法“产出的名字更好”。

目标是防止已修复的控制层缺陷在后续 Skill 修改中复发。

## 原则

- 测控制行为，不测单次候选审美高低。
- 每个 case 只验证少量清晰 expectation。
- 允许不同模型给出不同名称，只要控制决策满足合同。
- 不要求所有 case 每次发布都全跑；修改涉及相关模块时优先跑对应 case。
- 如果 runtime 无法提供真正隔离，只验证是否诚实记录 isolation level，不把环境限制误判为 Skill 失败。
- 回归失败先判断是 Skill、runtime adapter、state migration 还是执行 fidelity 问题。

## 当前 case 集

见 `regression-cases.yaml`。

覆盖重点：

- Owner boundary / search path 分离；
- hard constraint provenance；
- generation isolation 诚实性；
- Mission / Value 解构；
- value proxy collapse；
- Name Job / mission over-compression；
- Method Scheduler 多样性与 method underuse；
- Transformation Rescue 的触发与退出；
- evaluator anchoring / Decision Hygiene；
- Progressive Disclosure，防止 optional modules 被机械全量执行；
- Territory Research 的正确触发。

## 通过标准

每个 case 使用 `must` / `must_not` 描述可观察行为。若同一 case 在多个 runtime 上行为不同，应分别记录 runtime identity 和 capability，而不是把差异抹平。
