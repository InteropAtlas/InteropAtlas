# InteropAtlas Minimal Compare Contract v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Draft / Gate B Contract
Document Created At: 2026-09-02T10:46:00+08:00
Document Updated At: 2026-09-02T10:46:00+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: native
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> Document Status: Draft / Gate B Contract
>
> Document Created At: 2026-09-02T10:46:00+08:00
>
> Document Updated At: 2026-09-02T10:46:00+08:00
>
> Metadata Provenance: native
>
> Latest Substantive Contribution: Initiator = Human — ff6962757; Executor = Agent — OpenAI / ChatGPT / GPT-5.6 Sol; Reviewer = Pending; GitHub Actor = ff6962757
>
> Parent: #14 / Work Item: #94

## 1. 目的

Compare（比较）是 InteropAtlas 的核心 Human Task（人类任务），但 Gate B 不要求现在建设完整 Compare 产品。

本合同只定义最小可依赖语义：

> **在一个明确任务 / 能力上下文中，用户怎样知道哪些候选可以放在一起看、为什么可以比较、应该比较哪些维度、每个值来自哪里，以及哪些差异不能被自动解释成“谁更好”。**

本合同关闭的是 `HI-IA-GAP-004` / `HI-IP-GAP-003` 的 Gate B minimum（最小范围），不是完整 Compare UI。

---

## 2. 最小比较流程

```text
User Task / Context
        ↓
Comparable Candidate Set
        ↓
Explainable Dimension Set
        ↓
Per-candidate Values + Missing Semantics
        ↓
Evidence / Relation / Assessment Boundary
        ↓
Human-readable Differences
        ↓
No automatic winner unless an explicit Assessment exists
```

Compare 是 View / Projection（视图 / 投影），不是新的 Canonical Fact（规范事实）来源。

---

## 3. Comparable Context（可比较上下文）

### `IA-HI-CMP-001` — Context Before Comparison

系统 MUST 在展示比较结果前明确当前比较问题或上下文。

最小上下文可以是：

- 一个 Capability（能力）；
- 一个 Scenario（场景）；
- 一个明确 Requirement set（需求集合）；
- 一个已记录 Relation context（关系上下文）。

不得把“两个对象字段长得相似”当成它们天然可比较的充分理由。

**Gate B fixture：** `automated_build_deployment`。

---

## 4. Candidate Eligibility（候选进入条件）

### `IA-HI-CMP-002` — Explain Why Each Candidate Is Here

每个候选 MUST 有可解释的进入理由。

在 Capability Compare 中，最小进入依据为：

1. Candidate 是可识别的 Identity Object；
2. Candidate 明确记录支持当前 Capability，或存在等价的可解释 Statement / Relation；
3. 如果候选之间存在 `alternative_to` 等关系，可以作为额外上下文，但不能替代 Capability 支持事实。

Gate B 当前样例：

- `forgejo_actions` 支持 `automated_build_deployment`；
- `github_actions` 支持 `automated_build_deployment`；
- 另有 `forgejo_actions alternative_to github_actions`，其条件明确限定在 CI/CD / repository workflow automation 语境。

### 重要边界

`alternative_to` **不等于**：

- `compatible_with`；
- drop-in replacement（无缝替代）；
- recommended_over（优于 / 推荐替代）；
- equivalent_to（完全等价）。

Compare View MUST NOT 擅自升级 Relation 语义。

---

## 5. Dimension Selection（比较维度选择）

### `IA-HI-CMP-003` — Dimensions Must Be Explainable

一个比较维度只有在满足以下至少一项时才能进入最小 Compare：

- 是多个候选共享语义的 Canonical Property；
- 来自明确 Relation / Statement；
- 来自显式 Assessment，并清楚标记为 Assessment；
- 是当前任务直接需要、且其推导规则可解释的 Projection。

不得使用：

- 隐藏模型评分；
- 未记录的“综合实力”；
- Agent 临场感觉；
- 单纯为了让表格对称而制造的字段。

### Gate B 最小维度

对于当前 `automated_build_deployment` 样例，只要求使用现有数据中语义稳定、可解释的维度：

| Dimension | Semantic class | Forgejo Actions | GitHub Actions |
|---|---|---|---|
| Supports capability | Fact / property | `automated_build_deployment` | `automated_build_deployment` |
| Open source | Fact / property | true | false |
| Full service self-hostable | Fact / property | true | false |
| Deployment models | Fact / property | self-hosted platform; self-hosted runner | GitHub-hosted runner; self-hosted runner |
| License expression | Fact / property | GPL-3.0-or-later | not recorded for the platform service |
| Alternative relation | Relation / context | alternative to GitHub Actions under recorded conditions | target of recorded alternative relation |
| Compatibility claim | **Not established** | Forgejo explicitly does not claim full compatibility | no inverse compatibility claim inferred |

这张表是 semantic fixture（语义样例），不是未来最终页面布局要求。

---

## 6. Missing Semantics（缺失值语义）

### `IA-HI-CMP-004` — Missing ≠ False

Compare MUST 区分至少以下状态：

```text
false
已明确记录为否

unknown
当前明确知道“尚不确定”

not recorded / absent
当前记录没有这个值

not applicable
这个维度对该对象不适用
```

例如：Forgejo Actions 有 `license_expression`，而当前 GitHub Actions 平台服务记录没有对应 `license_expression`。

正确表达是：

> `not recorded（当前记录未提供）`

而不是：

> `none（没有许可证）`

也不能因此推导任何开放性结论；GitHub Actions 的 `open_source: false` 是独立记录的事实。

---

## 7. Fact / Relation / Assessment Boundary

### `IA-HI-CMP-005` — Comparison Must Preserve Semantic Class

Compare MUST 让用户能够分辨：

- Fact / Property（事实 / 属性）；
- Relation / Statement（关系 / 陈述）；
- Evidence / Source（证据 / 来源）；
- Assessment（评估）。

系统不得把 Assessment 渲染成与事实值完全不可区分的“普通字段”。

如果未来显示 `maturity`、`recommended`、`confidence`、`fit` 等内容，必须先遵守 Knowledge Model 对 Assessment 的边界。

Gate B 不要求现在实现完整 Assessment UI。

---

## 8. No Hidden Ranking（禁止隐藏排名）

### `IA-HI-CMP-006` — Compare Is Not Recommendation

最小 Compare MUST NOT 自动输出：

- winner；
- overall score；
- best choice；
- recommended；
- “A 比 B 更好”。

除非仓库中存在明确的 Assessment Object / Statement，并记录：

- criteria（标准）；
- context（适用上下文）；
- evidence / basis（依据）；
- assessor / provenance（评估者 / 溯源）。

因此：

> Forgejo Actions 是 open source + self-hostable

不能自动推导成：

> Forgejo Actions 比 GitHub Actions 更好。

对某些用户，这两个维度可能是关键优势；对另一些任务则未必。

---

## 9. Presentation Minimum（最小呈现合同）

### `IA-HI-CMP-007` — Scan Differences Without Losing Context

Gate B 只要求未来 Compare View 能满足以下信息职责：

1. 清楚显示 Compare Context；
2. 显示 Candidate identities；
3. 按共享维度对齐事实；
4. 显式显示 missing semantics；
5. 提供来源 / Evidence 的可发现路径；
6. 将 Relation / Assessment 与普通 property 区分；
7. 不依赖颜色作为唯一差异编码；
8. 在窄屏 / 辅助技术场景中仍保持“维度 ↔ 候选值”的关联。

具体可以使用 Table、stacked comparison（堆叠比较）或其他模式；Gate B 不冻结最终 UI。

---

## 10. Gate B Representative Walkthrough Fixture

### Task

> 我需要一个支持自动构建 / 部署的仓库自动化方案。Forgejo Actions 和 GitHub Actions 有什么已经记录、可以验证的差异？

### Starting context

Capability: `automated_build_deployment`

### Candidate eligibility

两者都在 Canonical record 中声明该 Capability，因此进入候选集合。

### Observed comparable facts

- 两者都支持当前 Capability；
- Forgejo Actions：`open_source = true`；GitHub Actions：`open_source = false`；
- Forgejo Actions：完整平台服务 `self_hostable = true`；GitHub Actions：完整平台服务 `self_hostable = false`；
- 两者都涉及 self-hosted runner，但其平台自托管语义不同；
- Forgejo Actions 记录 GPL-3.0-or-later；GitHub Actions 平台服务当前记录没有 license expression；
- Canonical Relation 记录 Forgejo Actions 是 GitHub Actions 的 `alternative_to`，同时明确“不使用 compatible_with”。

### Valid conclusion

> 两者都能进入自动构建 / 部署的候选集合，并且在开放源码、完整平台自托管、部署方式与已记录许可信息方面存在可解释差异。Atlas 当前还没有提供足够 Assessment 来宣布哪一个“整体更好”。

### Invalid conclusions

- “Forgejo Actions 与 GitHub Actions 完全兼容”；
- “Forgejo Actions 一定更好”；
- “GitHub Actions 没有许可证”；
- “self-hosted runner = GitHub Actions 整个平台可自托管”。

---

## 11. Gate B Conformance

Minimal Compare Contract 达到 Gate B minimum，当：

- [x] Compare Context 有定义；
- [x] Candidate Eligibility 有定义；
- [x] Dimension Selection 有定义；
- [x] Missing Semantics 有定义；
- [x] Fact / Relation / Assessment 边界有定义；
- [x] No Hidden Ranking 有定义；
- [x] 一个真实候选对可以只根据已有 Canonical Data 走通；
- [ ] 该任务被纳入下一步 Minimal Human Task Walkthrough 并实际执行；
- [ ] 最终 Gate B Conformance Audit 确认无 P0 structural non-conformance。

因此本合同完成后：

- `HI-IA-GAP-004`：Gate B minimum 可视为关闭；完整 Compare architecture / product 继续 P1；
- `HI-IP-GAP-003`：Gate B minimum semantic presentation contract 可视为关闭；最终 UI pattern 继续 P1。

---

## 12. Non-goals

本合同不定义：

- 完整 Compare 页面；
- Search / filtering；
- 自动评分；
- 个性化推荐；
- 多维权重系统；
- “最佳方案”算法；
- 新 Canonical Facts；
- 新 Relation 事实；
- Full Canonical Migration。
