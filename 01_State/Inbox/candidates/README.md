# Candidate State / 收录候选

`01_State/Inbox/candidates/` 是未正式接纳的 Candidate V1 载体，不是 Canonical 事实源。每个 YAML 文档遵守 `candidate-object.v1.schema.json`；一个批次文件可包含多个以 `---` 分隔的文档，身份始终由 `candidate_id` 确定。

- `new` 仅表示尚无已知确定性身份冲突，不等于全球唯一或已接纳。
- `duplicate` 指向既有 Canonical；已接纳候选也用此状态防止重复创建，历史接纳事实以验收事件为准。
- `possible_duplicate`、`identity_risk`、`deferred` 阻止普通路径建正式对象，需解决身份或范围问题。
- 验证器不得授权合并、拆分或等价推断；名称、URL、发布者或版本相似均不足以自动合并。
- 正式接纳必须有独立语义复核、来源与单独验收事件；同一 Executor 的自检不算独立审核。

## 本轮入口

跨领域候选在 `cross-domain-intake-20260913.yaml`。类别及关系种子在 [收录覆盖计划](../relations/intake-coverage-20260913.yaml)，正式记录在 `01_State/01_Objects/`，历史验收事件在 `01_State/Inbox/acceptance-events/`。

运行 `python 02_Runtime/01_Engine/intake_coverage_audit.py --root .`，从原始载体派生候选状态与类别清单；不维护第二套状态表。工作协调继续使用 Issue #146。本次是有界种子扩充，不代表全库候选全部复核完成。
