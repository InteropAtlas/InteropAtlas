# P5 Relation + Evidence / Assertion / Conflict + Lifecycle Fit Test v1 — Draft

> Status: P5 Research / Fit Test Draft
>
> Work Item: #132
>
> Checked At: 2026-09-04
>
> Scope: 小批量真实场景压力测试；不修改生产 Relation Schema，不执行全量迁移，不 stable-promote P4 drafts。

## 1. First checkpoint

本轮先不发明新的生产字段，而是用现有 IA Relations + #130 的真实标准样本，判断 P4.1 的关系、证据和生命周期边界是否足够。

核心问题不是“Relation YAML 应该长什么样”，而是先判断真实世界至少需要哪些不同语义层。

## 2. Scenario matrix

| Scenario | Existing / real case | What is being tested | Result |
| --- | --- | --- | --- |
| S1 simple binary | `engine_v0_1_bootstrap uses semantic_versioning_2_0_0` | source-predicate-target 是否足够 | binary fast path 足够 |
| S2 qualified binary | Apple HIG `provides` web accessibility | relation 带 capability context + scope conditions | endpoints 仍是 binary；qualifier/context 属于 assertion scope |
| S3 relation vocabulary mismatch | RFC 3339 vs ISO 8601 | V0 只有 `extends`，但更准确语义是 `profile_of` | vocabulary gap 会造成语义损失，必须可标记 approximation/provisional |
| S4 composite / participant roles | BCP 14 + RFC 2119 + RFC 8174 | 多个 publication 共同参与一个 maintained practice | 简单 version edge 不足；需要 rich association / explicit grouped semantics |
| S5 same participants, different occurrence semantics | publication/work pairs | 同一 participants 下多种事实 | participant set 不能充当 relation identity |
| S6 evidence-supported stable fact | Apple HIG `governed_by` Apple | 官方来源支持低争议关系 | compact relation + source/evidence fast path 可行 |
| S7 evidence gap / provisional assertion | RFC 3339 `extends` approximation | predicate 只是近似 | `confidence` 数字不足以表达 semantic gap |
| S8 historical / supersession lifecycle | ISO/IEC 27001:2013 vs 2022 | publication / supersession / IA lifecycle 正交 | superseded publication 不等于删除 IA record |
| S9 source freshness vs IA verification | Living Standard / maintained guides | upstream revision 与 IA verification | 两种时间必须分离 |
| S10 conflicting assertion | competing claims with different evidence | support/refute / incompatible claims | 保留并存 Assertions；禁止 last-writer-wins |

## 3. Binary fast path boundary

简单二元边仍然有价值，例如 Engine `uses` SemVer、Apple HIG `governed_by` Apple。

Binary fast path 成立条件：

1. 两个 endpoint 足以定义参与者结构；
2. predicate 的语义无需 participant roles 才能理解；
3. qualifier/context 即使存在，也只是限定 assertion，不改变参与者角色；
4. 不需要把多个 relation occurrence 合并成一个复杂事件/组合结构。

因此 V1 不应把所有边都强制对象化成重型 Association。

## 4. Promotion to rich association

出现以下任一压力时，应允许从 binary fast path promotion：

- 三个或更多参与者共同定义事实；
- participant role 是事实语义的一部分；
- relation occurrence 自身需要稳定引用；
- 多个 qualifier/context 共同决定事实含义；
- 需要把一组参与关系作为一个组合事实评审；
- 简单 predicate 会把 composition/profile/amendment/errata 等语义压扁。

BCP 14 是当前最强 promotion candidate：把 RFC 2119 和 RFC 8174 当作 `versions[]` 会损失“多个独立 publication 共同构成 maintained BCP”的结构。

## 5. Relation occurrence ≠ Assertion ≠ Evidence

V0 中已经存在把这些层揉在一起的迹象：relation record 表示关系 occurrence，`sources[]` 给来源，`confidence` 给评估，`notes` / `conditions` 又携带 assertion 限定和 caveat。

P5 确认 P4 的语义分离方向：

- **Relation / Association**：参与者和关系结构；
- **Assertion**：IA 对某个关系/属性事实提出的可评审陈述；
- **Source**：信息来源载体；
- **Evidence**：Source 中实际支持或反驳 Assertion 的证据；
- **Assessment**：可信度、争议、验证状态等判断；
- **Provenance**：该记录/判断如何进入 IA、由谁执行/审查、何时发生。

低争议场景可以 compact serialization，但这些概念不能在语义上等同。

## 6. Concrete V0 risk: approximate predicates can masquerade as facts

现有 `rfc3339_profiles_iso8601` 使用：

`RFC 3339 --extends--> ISO 8601`

但其 `notes_zh` 已说明：RFC 3339 是 ISO 8601 的 Internet profile，而当前 vocabulary 没有 `profile_of`，所以暂时使用 `extends` 近似。

这意味着 Human 能读到 caveat，机器却可能把 `extends` 当成精确 Canonical fact。

V1 至少需要保证：

- exact assertion 与 approximation/provisional mapping 可区分；
- vocabulary gap 不通过确定 predicate 静默隐藏；
- vocabulary 增强后可以纠正语义，同时保留原始来源和审查历史。

这不授权现在新增生产 `profile_of`。

## 7. Second pressure point: qualified binary remains binary

现有 `iso_9241_20_provides_accessibility_approach` 是更强的真实案例：

- source = ISO 9241-20:2021；
- relation = `provides`；
- target = `web_accessibility`；
- `capability_context` 同时包含 `web_accessibility` 与 `human_system_interaction`；
- `conditions_zh` 明确提醒：标准范围比 Web 更广，当前 target 只是 IA Capability 模型中的近似投影。

这验证了一个重要边界：**上下文复杂，不等于参与者结构复杂。**

该关系仍只有两个 endpoint，因此没有必要仅因为存在 scope/condition 就 promotion 成 rich association。正确做法是保持 binary relation，同时让 Assertion/qualifier 能表达 scope、projection caveat 和 verification state。

## 8. Minimal conflict / evidence-gap representation

为了避免把整个 V1 设计成重型 provenance graph，#132 只验证最小语义结构，不确定最终字段名：

```yaml
assertion:
  subject: A
  predicate: profile_of
  object: B
  qualifiers: {...}

evidence:
  - source: official_source_1
    stance: supports
  - source: source_2
    stance: refutes

assessment:
  state: disputed
  verification: reviewed
```

若只有来源但尚未找到支持该 Assertion 的具体证据，则应能表达：

```yaml
assessment:
  state: unverified
  evidence_gap: true
```

关键不在字段名，而在以下语义不被压平：

- `unknown`：现实值未知；
- `not_recorded`：IA 尚未记录；
- `not_applicable`：该字段/关系不适用；
- `unverified`：已有 assertion，但尚未完成验证；
- `disputed`：存在相互冲突的 assertion/evidence。

`confidence: 0.5` 无法替代这些状态。

## 9. Lifecycle orthogonality

至少需要概念上区分：

- IA repository record lifecycle；
- publisher publication lifecycle；
- applicability/adoption lifecycle；
- supersession/historical relation state；
- verification freshness；
- assertion dispute/verification state。

一个 2013 edition 可以同时是 publisher 层面 withdrawn/superseded、IA 层面仍 active/readable、legacy applicability 仍成立、verification 层面 recently verified。因此不能用一个万能 `status` 压扁。

## 10. Serialization implications for P6

本 Fit Test 只给出生产实现约束，不冻结字段：

1. 保留二元 `subject/predicate/object` fast path；
2. qualifier/context 应可附着到 assertion/relation occurrence，而不是发明无限 predicate；
3. rich association 是 promotion path，不是默认形式；
4. relation vocabulary 必须允许“尚无精确 predicate”的 provisional 状态；
5. Source/Evidence/Assertion/Assessment/Provenance 语义分层必须可恢复；
6. conflict preservation 是 Canonical contract requirement；
7. lifecycle 是多维状态，不是单 `status`；
8. compact serialization 可以存在，但必须能无损 promotion 到显式结构。

## 11. Unresolved but intentionally deferred

以下问题没有必要在 #132 中继续展开：

- `profile_of`、`amends`、`errata_for` 等最终 relation registry；
- Assertion 是否全部 first-class object；
- rich association 的最终 ID / participant serialization；
- Evidence 引用到 source 的粒度；
- Assessment vocabulary 的最终枚举；
- compact form 与 explicit form 的具体 JSON/YAML schema。

这些属于 P6 serialization / implementation，或在后续真实迁移中按压力决定。

## 12. Exit conclusion

#132 的代表性测试通过，没有发现需要推翻 P4.1 的证据。

最重要的新发现不是“需要更多 relation type”，而是：

> **V1 必须显式区分“精确事实”和“由于当前模型不足而产生的近似表达”，否则 Canonical machine-readable data 会比 Human-readable notes 更确定。**

同时确认：复杂 qualifier 不自动要求 rich association；conflict/evidence gap 可以用轻量但语义分层的结构表达，不需要把每条普通关系都建成重型 knowledge graph node。

本 Work Item 可以进入 Review；独立审查仍待 Human / independent reviewer，self-check 不等于 independent review。
