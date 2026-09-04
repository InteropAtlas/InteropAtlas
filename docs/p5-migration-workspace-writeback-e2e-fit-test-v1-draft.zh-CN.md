# P5 Legacy→V1 Migration + Workspace + Write-back E2E Fit Test v1 — Draft

> Status: P5 Research / E2E Fit Test Draft
>
> Work Item: #133
>
> Checked At: 2026-09-04
>
> Scope: dry-run only；不修改生产 Canonical 数据，不冻结最终 V1 Schema，不执行 Legacy retirement。

## 1. First checkpoint goal

本 checkpoint 只验证 P4.3 的 mapping classes 是否能用真实 Legacy 数据稳定区分，并提前暴露 semantic loss / ambiguity。

选择 4 条记录，分别覆盖 A / B / C / D：

1. `engine_v0_1_uses_semver` — A Lossless structural mapping；
2. `apple_human_interface_guidelines` — B Normalization mapping；
3. `rfc3339_profiles_iso8601` — C Semantic promotion；
4. `bcp14_rfc2119_rfc8174` — D Ambiguous / unresolved mapping。

这些记录故意同时包含 Object 与 Relation，以避免只验证一种数据形态。

## 2. Cohort mapping table

| Legacy record | Class | V1 dry-run intent | Stable ID | Loss / ambiguity |
| --- | --- | --- | --- | --- |
| `engine_v0_1_uses_semver` | A | 保留 relation occurrence；`source/relation/target` 结构映射为 V1 binary relation fast path；保留 notes + provenance | preserve | 无已知语义损失；仅结构表达变化 |
| `apple_human_interface_guidelines` | B | 保留 subject；将 `official_url` 归入 locator role，将 `last_verified` 归入 verification/freshness，将 `type/reference_project + project_kind` 映射到 family/kind 语义层 | preserve | `project_kind: other` 信息量低；不能机械当作最终 V1 kind |
| `rfc3339_profiles_iso8601` | C | 保留 relation ID 和 endpoints；把当前 `extends` + caveat 从“确定 predicate”提升为 explicit assertion/provisional semantic mapping，保留 relation-vocabulary gap | preserve | 旧结构让机器看起来比 Human notes 更确定；若直接照抄 `extends` 会产生语义失真 |
| `bcp14_rfc2119_rfc8174` | D | 保留现有 IA subject identity；保留 BCP 14 当前对象及 RFC 2119/RFC 8174 来源；将 `versions[]` 标记为 unresolved publication/composition mapping，等待后续 semantic decision | preserve by default | 不能可靠判定 `versions[]` 是版本、组成 publication、update relation 或需要新 publication layer；禁止脚本自动 split/merge |

## 3. Dry-run V1-shaped mapping

以下仅用于验证 semantic shape，不是最终生产 serialization。

### A — lossless relation

```yaml
id: engine_v0_1_uses_semver
relation:
  subject: engine_v0_1_bootstrap
  predicate: uses
  object: semantic_versioning_2_0_0
provenance: preserved_from_legacy
```

结果：现有信息可以无损进入 binary fast path。文件路径、schema generation 或字段包装变化都不需要新 ID。

### B — normalization object

```yaml
id: apple_human_interface_guidelines
identity:
  labels: ...
classification:
  family: reference_or_guidance_asset   # provisional
  kind: human_interface_guidance        # provisional
locators:
  - role: official_current
    url: https://developer.apple.com/design/human-interface-guidelines/
verification:
  last_verified_at: 2026-09-01
sources: preserved
```

结果：`official_url` 和 `last_verified` 可以明确归位，但 `reference_project / project_kind: other` 不应通过字符串替换直接冻结成 V1 taxonomy。Normalization 可自动化一部分，但 classification 仍需 semantic review。

### C — semantic promotion relation

```yaml
id: rfc3339_profiles_iso8601
participants:
  subject: rfc3339
  object: iso_8601_1_2019
assertion:
  proposed_predicate: profile_of
  legacy_predicate: extends
  mapping_state: provisional
assessment:
  state: semantic_gap
provenance: preserved_from_legacy
```

结果：这里不能做 A/B 类机械迁移。Legacy `notes_zh` 已经表达“`extends` 只是近似”，因此 V1 dry-run 必须显式提升这个 caveat。若只是复制 predicate，会制造假确定性。

### D — ambiguous publication/composition mapping

```yaml
id: bcp14_rfc2119_rfc8174
identity:
  canonical_id: bcp14_rfc2119_rfc8174
publication_mapping:
  state: unresolved
legacy_members:
  - RFC 2119
  - RFC 8174 update
possible_interpretations:
  - publications_participate_in_bcp
  - update_relation_between_publications
  - publication_layer_under_stable_bcp_subject
migration_decision: pending_semantic_review
```

结果：不得根据 `versions[]` 字段名推断“RFC 2119 是 v1、RFC 8174 是 v2”。当前正确迁移行为是 preserve identity + preserve evidence + mark ambiguity，而不是猜测。

## 4. Semantic loss / ambiguity report

### A `engine_v0_1_uses_semver`

- loss: none detected；
- ambiguity: none affecting relation identity；
- automation potential: high；
- review: Machine Review + ordinary semantic spot check。

### B `apple_human_interface_guidelines`

- loss risk: `project_kind: other` 若被机械归一，会伪造 taxonomy precision；
- ambiguity: family/kind exact vocabulary 尚未冻结；
- safe automation: locator / verification field placement；
- semantic review required: classification mapping。

### C `rfc3339_profiles_iso8601`

- loss risk: copy `extends` as exact V1 predicate；
- ambiguity: final relation registry 是否采用 `profile_of` 尚未冻结；
- safe migration behavior: preserve endpoints + original predicate + caveat, expose provisional mapping；
- semantic review required: relation vocabulary acceptance。

### D `bcp14_rfc2119_rfc8174`

- loss risk: automatic version normalization destroys composition/update meaning；
- ambiguity: Work/BCP subject vs publication layer；
- destructive risk: script-triggered split/merge/new IDs；
- safe migration behavior: preserve existing IA ID and all source material, mark unresolved；
- authority: any future split/merge is Class E / higher gate, not part of this batch。

## 5. First checkpoint conclusions

P4.3 mapping classes are useful in practice and are not merely theoretical categories：

- A can be highly automated；
- B can automate structural normalization but not semantic taxonomy decisions；
- C requires promotion of hidden caveats/claims into explicit semantics；
- D must stop automation and preserve uncertainty。

Most important finding：**migration risk does not correlate with file size or field count.** A tiny relation can be Class C because one approximate predicate changes meaning, while a larger object can still be mostly Class B normalization。

Stable IA IDs survive all four dry-run mappings by default. No case in this cohort justifies automatic identity replacement。

## 6. Guardrails confirmed before E2E continuation

1. dry-run transformation is a Candidate Patch, not Canonical acceptance；
2. mapping class must be visible in diagnostics；
3. loss / ambiguity report is mandatory for C/D；
4. D does not fail by forcing a value — it succeeds by preserving unresolved state；
5. projection later in #133 must be generated from V1-shaped dry-run state, not from silently corrected Legacy data；
6. any correction discovered in Workspace must return through Candidate Write / Intake, not directly mutate Canonical。

## 7. Next checkpoint

Use this same four-record cohort to produce minimal V1-shaped experiment data and test：

- structural validation；
- reference / relation compatibility；
- semantic diff against Legacy；
- a small Compare / Evidence / Timeline-or-Graph projection set；
- one deliberate correction discovered from a projection and returned as Candidate Patch + Evidence。

Do not build production UI and do not accept any migrated record into Canonical during this experiment。
