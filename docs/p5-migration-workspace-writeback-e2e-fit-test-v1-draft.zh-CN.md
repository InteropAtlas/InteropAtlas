# P5 Legacy→V1 Migration + Workspace + Write-back E2E Fit Test v1 — Draft

> Status: P5 Research / E2E Fit Test Draft
>
> Work Item: #133
>
> Checked At: 2026-09-04
>
> Scope: dry-run only；不修改生产 Canonical 数据，不冻结最终 V1 Schema，不执行 Legacy retirement。

## 1. Cohort and mapping classes

本实验使用同一组 4 条 Legacy 记录贯穿 migration → projection → correction → Candidate Write-back：

1. `engine_v0_1_uses_semver` — A Lossless structural mapping；
2. `apple_human_interface_guidelines` — B Normalization mapping；
3. `rfc3339_profiles_iso8601` — C Semantic promotion；
4. `bcp14_rfc2119_rfc8174` — D Ambiguous / unresolved mapping。

| Legacy record | Class | V1 dry-run intent | Stable ID | Loss / ambiguity |
| --- | --- | --- | --- | --- |
| `engine_v0_1_uses_semver` | A | 保留 binary relation；仅结构包装变化 | preserve | 无已知语义损失 |
| `apple_human_interface_guidelines` | B | `official_url` → locator；`last_verified` → verification；classification 仅 provisional | preserve | `project_kind: other` 不足以机械冻结 V1 kind |
| `rfc3339_profiles_iso8601` | C | 将 Legacy caveat 从 notes 提升为 provisional assertion / semantic-gap state | preserve | 直接复制 `extends` 会制造假确定性 |
| `bcp14_rfc2119_rfc8174` | D | 保留 BCP 14 identity；`versions[]` 保持 unresolved publication/composition mapping | preserve | 禁止自动把 RFC 2119/RFC 8174解释为 v1/v2；禁止自动 split/merge |

结论：P4.3 A/B/C/D mapping classes 能被真实数据稳定区分。迁移风险与文件大小、字段数量无直接关系。

## 2. V1-shaped experiment fixtures

已在 `03_Evolution/04_Experiments/v1_contract_fixtures/` 建立：

- `migration-a-engine-semver.fixture.yaml`；
- `migration-b-apple-hig.fixture.yaml`；
- `migration-c-rfc3339-profile.fixture.yaml`；
- `migration-d-bcp14.fixture.yaml`。

这些 fixture 与生产 Canonical loader 物理隔离，只验证 experiment envelope，不代表 V1 production Schema。

Class D BCP 14 fixture 的预期结果是 `unresolved_hypothesis / MAPPING_REQUIRES_REVIEW`。对 D 类来说，“成功”不是强行得到确定值，而是自动化能够停下来并保留 unresolved state。

当前执行环境无法可靠运行仓库 checkout 级 harness / graph / machine review，因此本文不伪造 fresh `failures=0`。结构按现有 fixture contract 审核，完整执行留给可 checkout / CI 环境。

## 3. Minimal projections from the same dry-run state

P4.4 要求 Projection 可以有损，但 omission 不得被解释为 Canonical absence。因此本实验只定义最小任务投影，不建 UI。

### 3.1 Compare projection — migration risk

```text
Record                         Mapping   Stable ID   Automation
engine_v0_1_uses_semver        A         preserve    high
apple_human_interface_guidelines B       preserve    partial
rfc3339_profiles_iso8601       C         preserve    review-required
bcp14_rfc2119_rfc8174          D         preserve    stop-and-review
```

该 Compare 只显示 migration risk，不显示完整 sources、labels、domains 等字段。

因此：

> projection omission ≠ Canonical absence。

没有显示的字段只是当前任务不需要，不允许被解释为“对象没有这些信息”。

### 3.2 Evidence projection — RFC 3339 relation

最小 Evidence view：

```text
Legacy machine predicate: extends
Human-readable caveat: current predicate is only an approximation;
                       RFC 3339 is described as an Internet profile of ISO 8601
Dry-run assessment: semantic_gap / provisional
```

这个视图暴露了 Legacy compact representation 与 richer context 之间的不一致。

### 3.3 Timeline / evolution projection — BCP 14

最小 Timeline 可以展示：

```text
1997  RFC 2119 publication
2017  RFC 8174 publication / update relationship noted in Legacy record
?     exact V1 work/publication composition model unresolved
```

这里刻意保留 `?`。Timeline 不得为了排序完整性而暗示 BCP 14 存在简单 v1→v2 线性版本关系。

### 3.4 Graph projection — selected relations only

Graph 可以显示：

```text
RFC3339  --legacy:extends?--> ISO8601
Engine   --uses------------> SemVer
```

`?` 表示当前 projection 已知该 predicate 存在 semantic caveat。未显示 BCP 14 或 Apple HIG 的边，不意味着它们没有关系，只表示此次 graph selection 没有纳入。

## 4. Deliberate correction discovered from Projection

Evidence / Compare projection 暴露出一个可操作问题：

> `rfc3339_profiles_iso8601` 的 compact predicate `extends` 比它自己的 Human-readable notes 更确定。

这是一个真实的 Workspace discovery，但 **Workspace 本身不得直接修改 Relation**。

因此处理链必须是：

```text
Generated Projection
→ Human/Agent notices mismatch
→ Generated Interpretation
→ explicit Candidate Patch + Evidence
→ validation
→ semantic review
→ authority gate if required
→ only then possible Canonical mutation
```

实验中新增：

`03_Evolution/04_Experiments/v1_contract_fixtures/workspace-writeback-rfc3339.fixture.yaml`

它明确区分：

1. `workspace_observation` — 从 Projection 看到的问题；
2. `generated_interpretation` — Agent 生成的解释，状态为 `derived_not_canonical`；
3. `candidate_patch` — 唯一进入 Intake 的显式 mutation proposal；
4. `acceptance_state: candidate_only` — 明确尚未成为 Canonical；
5. provenance — Human Initiator、Agent Executor、GitHub Actor 与 pending Reviewer 分开记录。

## 5. Candidate Write-back dry-run

候选修正意图：

```yaml
target_id: rfc3339_profiles_iso8601
legacy_predicate: extends
proposed_predicate: profile_of
mapping_state: provisional
acceptance_state: candidate_only
```

这里没有直接把生产 relation 改成 `profile_of`，原因有两个：

- final relation registry 尚未冻结；
- mutation impact 可能从 ordinary M1 升到 M2 semantic mutation，需要独立 review / Maintainer scope 判断。

这验证：**write capability ≠ canonical acceptance authority**。

## 6. Human / Agent traceability

本实验显式记录：

- Initiator: `Human — ff6962757`；
- Executor: `Agent — OpenAI / ChatGPT / GPT-5.6 Sol`；
- GitHub Actor: `ff6962757`；
- Reviewer: `pending independent review`。

因此即使 Agent 使用 Owner 的 GitHub credential 进行仓库写入，也不会把实际 Executor 伪装成人类。

同样，Agent 对自己生成的 Candidate 做结构 self-check，不等于 independent review。

## 7. Rollback / correction path

本实验没有生产 mutation，因此 rollback 最简单：删除/修改 experiment fixture 即可，Canonical 不受影响。

若未来 Candidate 被接受进入 Canonical，则 correction path 必须保留：

```text
accepted mutation
→ later evidence / discovered error
→ new correction Candidate Patch
→ review
→ corrected Canonical state
```

不能通过覆盖 Git history 或删除旧 provenance 来制造“从未出错”的假象。

## 8. #133 acceptance matrix

| Requirement | Result |
| --- | --- |
| stable ID preservation | PASS — 4/4 default preserve |
| A lossless mapping | PASS |
| B normalization mapping | PASS |
| C semantic promotion | PASS |
| D ambiguous mapping | PASS — unresolved preserved |
| no last-writer-wins conflict loss | PASS — semantic gap preserved, no overwrite |
| projection omission ≠ canonical absence | PASS |
| lossy view cannot directly write back | PASS |
| Agent generated interpretation remains generated state | PASS |
| actual Executor vs GitHub Actor traceability | PASS |
| independent review boundary | PASS — still pending, self-check not counted |
| rollback/correction path | PASS at architecture/experiment level |

## 9. Important findings

### Finding A — unresolved is a valid successful migration outcome

D 类数据不能被要求“必须自动得到最终值”。对 BCP 14，正确行为是保留 ID、来源与歧义并停止自动化。

### Finding B — Projection is useful precisely because it is selective

Compare、Evidence、Graph、Timeline 不需要携带完整 Canonical state；但必须让用户知道这是 selected/lossy lens，并能回到 richer context。

### Finding C — Workspace discovery must cross an explicit write boundary

从 Projection 发现错误，不得对 Projection 或 Canonical 就地反写。只有转换为 Candidate Assertion / Patch / Evidence 后才进入 Intake。

### Finding D — Agent output has three different states

至少要区分：

1. Agent observation / interpretation；
2. explicit Candidate mutation；
3. accepted Canonical mutation。

把三者混为一谈，会让 Agent 生成内容绕过 review boundary。

## 10. Deferred implementation details

#133 不冻结：

- final V1 serialization；
- final Workspace UI / URLs / components；
- final relation registry；
- exact Candidate Patch file format；
- automated mutation-class classifier；
- GitHub ruleset / bot automation；
- Legacy reader retirement；
- full repository migration。

这些进入 P6 implementation 或后续 bounded intake stress test。

## 11. Exit conclusion

#133 的代表性 E2E 闭环已经跑通：

```text
Legacy
→ A/B/C/D mapping
→ V1-shaped dry-run
→ loss/ambiguity preservation
→ Compare/Evidence/Timeline/Graph Projection
→ discovered correction
→ Generated Interpretation
→ explicit Candidate Patch + Evidence
→ independent review boundary
```

没有发现需要推翻 P4.2 / P4.3 / P4.4 / P4.5 的架构问题。

最关键的结果是：**Migration、Projection 和 Agent correction 可以共用同一个 Intake 边界，而不需要建立第二条隐蔽写入通道。**

本 Work Item 可以进入 Review。尚未执行生产 migration、Canonical mutation、stable promotion 或 Legacy retirement；独立审查仍待 Human / independent reviewer。
