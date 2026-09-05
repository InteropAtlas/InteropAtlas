# Gate B Requirement / Gap Priority Audit

<!-- InteropAtlas Document Metadata v0
Document Status: Draft Audit / Gate B scope control
Document Created At: 2026-09-02T08:04:53+08:00
Document Updated At: 2026-09-02T08:04:53+08:00
Metadata Backfilled At: 2026-09-02T11:02:46+08:00
Metadata Provenance: mixed
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: owner_confirmed_cutoff
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Human — ff6962757
  GitHub Actor: ff6962757
-->

> 日期：2026-09-02
>
> Parent: #14
>
> Work item: #80
>
> 状态：Draft Audit / Gate B scope control

## 1. 审计目的

五个 Human Interface Draft Profiles 已经存在。当前问题不再是“还能补什么规范”，而是：

> **哪些缺口如果不关闭，就不能合理宣布 Human Interface Foundation 可依赖？**

本审计为 Gate B 划定毕业线，防止 Foundation 因 Search、完整 Compare 产品、大型 Graph、完整 Token System 等长期产品能力而无限延长。

---

## 2. 优先级定义

### P0 — Gate B Blocker

不关闭就无法证明核心 Human Interface 合同在真实 Reference Implementation 上成立。

### P1 — Post-Gate Near-term

重要，但不影响 Foundation 是否已经达到最小可依赖状态。Gate B 后与 Reference Implementation 一起推进。

### Later — Product Expansion

属于高级产品能力、规模化、精细化或尚未出现的复杂需求，不应阻塞 Foundation。

---

## 3. Gap Priority Matrix

### Information Architecture

| Gap | Priority | Gate B 判断 |
|---|---|---|
| `HI-IA-GAP-001` Entry-point coverage | **P0（缩小范围）** | 不要求现在实现所有入口；必须证明至少一组核心任务可以通过现有入口稳定找到目标对象，并明确未来入口不被单一对象类型树锁死。 |
| `HI-IA-GAP-002` Resource-page coverage | **P1** | 不要求所有 Identity Object 都有页面；Gate B 只验证代表性 Resource Page。 |
| `HI-IA-GAP-003` Findability evaluation | **P0** | 必须至少完成一组 task walkthrough / tree-test-equivalent evidence。 |
| `HI-IA-GAP-004` Compare architecture | **P0（最小合同） / P1（完整产品）** | Gate B 必须保留 Compare 作为核心任务并验证最小比较路径 / 维度合同；完整 Compare UI、筛选和并排产品体验不阻塞 Gate B。 |

### Information Presentation

| Gap | Priority | Gate B 判断 |
|---|---|---|
| `HI-IP-GAP-001` Strong Profile key facts | **P0（代表切片）** | 至少对 Capability / Artifact / System / Agent 四个代表身份定义并验证“先看到什么”。 |
| `HI-IP-GAP-002` Evidence / Assessment presentation | **P0（边界级）** | 必须证明事实来源、Evidence、Assessment 不会在人类界面中被混成同一种“来源/结论”；不要求一次完成所有未来 Assessment UI。 |
| `HI-IP-GAP-003` Compare presentation | **P0（最小语义） / P1（完整 UI）** | Gate B 至少要证明比较维度来自可解释事实 / Statement / Assessment，并完成非 UI 或最小 walkthrough；完整 Compare View 后置。 |
| `HI-IP-GAP-004` Density measurement | **P1** | Gate B 用 task-based human review 判断明显重复/过载，不冻结机械密度数字。 |

### Interaction

| Gap | Priority | Gate B 判断 |
|---|---|---|
| `HI-INT-GAP-001` URL / History state model | **P1** | 当前稳定 Resource Link 必须成立；Filter/Map 状态 URL 化可以 Gate B 后推进。 |
| `HI-INT-GAP-002` Browser E2E contract | **P0** | 必须把真实浏览器、keyboard、focus、JS-disabled、narrow viewport、当前 Recenter 等从计划变成可执行 evidence。 |
| `HI-INT-GAP-003` Error / empty / loading states | **P0（当前 Recenter 路径） / P1（完整系统）** | 当前 Local Map Recenter 已有真实异步 loading/failure 行为，因此其成功、载入和失败反馈必须进入 Gate B Browser slice；未来完整 Error/Loading System 后置。 |
| `HI-INT-GAP-004` Complex graph controls | **Later** | 尚不存在 pan/zoom/drag/multi-select 复杂合同，不提前发明。 |

### Visual Presentation

| Gap | Priority | Gate B 判断 |
|---|---|---|
| `HI-VIS-GAP-001` type / spacing / width scales | **P1** | Gate B 验证可读、reflow、层级即可，不冻结完整 scale。 |
| `HI-VIS-GAP-002` Relation visual vocabulary | **P1** | 只要求当前关系表达不依赖颜色且语义可辨；完整视觉词汇后置。 |
| `HI-VIS-GAP-003` focus / motion evidence | **P0** | focus visibility、reduced-motion、zoom/reflow 属于当前可验证的基础可访问性。 |
| `HI-VIS-GAP-004` Token artifact | **Later** | DTCG-compatible artifact 不应成为 Foundation 毕业条件。 |

### Accessibility / Conformance

| Gap | Priority | Gate B 判断 |
|---|---|---|
| `HI-CONF-GAP-001` Browser test harness | **P0** | Gate B 最重要的缺失证据之一。 |
| `HI-CONF-GAP-002` Requirement registry/report format | **P1** | Markdown matrix 足够完成 v0.1 Gate；机器可读 registry 后置。 |
| `HI-CONF-GAP-003` accessibility exception policy | **P1** | v0.1 可以记录已知例外；正式 exception governance 后置。 |
| `HI-CONF-GAP-004` human evaluation protocol | **P0（最小版）** | 至少形成一个可重复的代表任务 walkthrough 模板并执行，且任务集合包含最小 Compare。 |
| `HI-CONF-GAP-005` broader accessibility capability modeling | **P1 / Knowledge debt** | 属于 Atlas 知识覆盖，不应阻塞 Human Interface Gate。 |

---

## 4. Gate B 真正的 P0 集合

去掉重复后，Gate B 只保留五组 P0：

### P0-A — Representative Information Architecture Tasks

至少验证：

1. Identify an object；
2. Find an implementation for a capability；
3. Follow a meaningful relation and return；
4. Verify source/evidence where available；
5. Compare alternatives — **只要求最小任务 / 信息架构 / 比较维度 walkthrough，不要求完整 Compare UI**。

不要求完整 Search / Domain navigation / Compare product。

### P0-B — Representative Resource Page Contract

至少选择四个代表身份：

```text
concept / capability
artifact / normative artifact
system / implementation
agent / organization
```

验证：

- stable identity / title；
- summary；
- key facts；
- important relationships；
- source / evidence boundary；
- machine/raw view 的位置；
- 不按 YAML 字段顺序机械打印。

### P0-C — Browser / Interaction Baseline

必须有真实 Browser evidence：

- stable Link navigation；
- Back / Forward；
- keyboard-only core path；
- visible focus；
- JS-disabled core reading/navigation；
- narrow viewport / reflow；
- reduced-motion preference（存在 motion 时）；
- **当前 Local Map Recenter 的成功路径**；
- **当前 Local Map Recenter 的 loading / failure feedback**。

说明：这里只把**已经存在、用户可触达的 Recenter 异步行为**纳入 P0；不要求为了 Gate B 建造通用 Error / Loading framework。

### P0-D — Accessibility Baseline

至少证明：

- semantic landmarks / headings；
- Link / Button semantics；
- keyboard operability；
- focus visibility；
- applicable contrast / non-text contrast；
- zoom / reflow；
- color not sole semantic channel；
- 当前 Recenter 的 loading / failure 状态有可感知反馈，不能只依赖不可发现的内部状态。

目标仍为 WCAG 2.2 AA；Gate B v0.1 不把“采用 accessible component”当作整站合规证明。

### P0-E — Minimal Human Task Evaluation

执行一个可重复的任务 walkthrough，至少覆盖 P0-A 的五类任务，并记录：

```text
Task
Starting point
Expected destination/outcome
Observed path
Friction / ambiguity
Requirement affected
Result: Conform / Partial / Non-conform / Unknown
```

Gate B 不要求大规模用户研究；至少要证明规范曾与真实任务接触，而不是只做文档自洽检查。

---

## 5. 明确不阻塞 Gate B 的工作

以下工作不能被重新升级成 Foundation 无限延期理由，除非 P0 evidence 证明它们实际阻塞核心任务：

- 完整 Search；
- **完整 Compare UI / 产品系统**（但最小 Compare task / architecture walkthrough 仍是 P0）；
- Domain / Organization / Scenario 所有入口；
- 大型 Graph Explorer；
- pan / zoom / drag / multi-select；
- 完整 URL state model；
- **完整 Error/Loading state system**（但当前 Recenter 的现有 loading/failure 路径仍是 P0）；
- 完整 typography / spacing scale；
- 完整 Relation visual vocabulary；
- DTCG token artifact；
- 所有 Identity Object 的 Human Page；
- machine-readable Human Interface Requirement Registry；
- 全面用户研究；
- Full Canonical Migration；
- repository-wide Schema Enforcement；
- Ruleset / governance automation。

---

## 6. Representative Conformance Slice

Gate B 不审计整个未来产品，而审计一个能穿过五个 Profile 的代表切片：

```text
Home / Entry Point
        ↓
Capability Resource Page
        ↓
Implementation Resource Page
        ↓
Meaningful Relation / Back navigation
        ↓
Local Map Recenter + failure feedback
        ↓
Source / Evidence inspection
        ↓
Minimal Compare walkthrough
```

并横向检查：

```text
Information Architecture
Information Presentation
Interaction
Visual Presentation
Accessibility / Conformance
```

同时抽样 Artifact 与 Organization 页面，确认四个 Core Identity Family 的 Human Presentation 没有结构性冲突。

---

## 7. Gate B Stop Condition

当且仅当以下条件同时满足，可建议 Gate B PASS：

- [x] 五个 Human Interface Draft Profiles 存在并可独立审计；
- [x] 关键 Requirements 有上游标准 / Mature Prior Art / IA-specific basis；
- [x] Adopt / Profile / Extend / Invent 边界已记录；
- [ ] 四类代表 Resource Page 的 key-facts / source / relation presentation 已验证；
- [ ] Browser E2E baseline 可重复执行并通过核心路径；
- [ ] Keyboard / focus / reflow / semantic structure 有 evidence；
- [ ] 当前 Local Map Recenter 的成功、loading、failure feedback 已验证；
- [ ] 至少一组代表 Human Task Walkthrough 已执行，并包含最小 Compare 任务；
- [ ] Compare 至少具备可解释的最小任务 / 信息架构 / 比较维度合同；
- [ ] 新一轮 Conformance Audit 没有未处理的 P0 structural non-conformance；
- [ ] 所有剩余 Gap 已明确降级为 P1 / Later 或记录为已接受风险。

### 明确停止规则

满足以上条件后：

> **Gate B SHOULD PASS，即使完整 Search、完整 Compare 产品、大型 Graph、完整 Tokens 和全部页面类型尚未完成。**

Gate B PASS 后，Human Interface Foundation 从主 P0 退出；Reference Implementation 恢复为主要产品实现线，五个 Profiles 继续作为约束和反馈系统演化。

---

## 8. 下一执行顺序

```text
#80 Priority Audit
        ↓
#13 Browser E2E / Accessibility foundation
        ↓
Representative Resource Page conformance slice
        ↓
Minimal Human Task Walkthrough（含 Compare）
        ↓
Gate B Conformance Audit
        ↓
PASS or explicit blocker list
```

#80 本身不需要实现完整 Search / Compare / Graph 新功能。它的完成标准是把 Gate B 的工作量从“所有可能缺口”压缩为上述五组 P0 evidence，同时确保已经存在的用户可触达行为不会逃过测试。
