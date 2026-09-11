# Human Interface Five-Profile Consolidation Audit

<!-- InteropAtlas Document Metadata v0
Document Status: Consolidation Audit / Gate B evidence
Document Created At: 2026-09-02T07:39:56+08:00
Document Updated At: 2026-09-02T07:39:56+08:00
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

> 日期：2026-09-01
>
> Parent: #14
>
> Work item: #78
>
> 状态：Consolidation Audit / Gate B evidence

## 1. 问题

#14 要求五个独立、可审计的 Human Interface Draft Profiles。

此前项目已经有较完整的综合规范 `docs/human-interface-specification-v0.1.zh-CN.md`，但它存在三个管理问题：

1. Interaction、Information Presentation、Visual、Accessibility 等规则长期放在同一个大文档，模块责任不够清楚；
2. Requirement ID 已经存在，但“用户任务 / 上游依据 / 采用方式 / conformance 方法”不是每条都以一致结构展示；
3. Gate B 很难回答“哪个 Profile 已有 Draft coverage，哪个仍缺什么”。

本轮不是重新设计一套 UI，而是把现有规则第一次收敛成可独立审计的 Package。

---

## 2. 输入材料

本轮主要复用：

- `docs/human-interface-specification-v0.1.zh-CN.md`；
- `docs/human-readable-interaction-baseline.zh-CN.md`；
- `03_Evolution/01_Research/human-interface-standards-baseline.zh-CN.md`；
- `03_Evolution/01_Research/human-interface-reference-map.zh-CN.md`；
- `03_Evolution/01_Research/human-interface-conformance-audit-2026-09-01.zh-CN.md`；
- 已完成的 Knowledge Model v0 / #61 machine contract，尤其 Facts / Statement / Evidence / Assessment 与 View 分离原则。

---

## 3. 输出结构

新增正式 Draft Package：

```text
docs/human-interface-profiles-v0.1.zh-CN.md
│
├── Information Architecture Profile
├── Information Presentation Profile
├── Interaction Profile
├── Visual Presentation Profile
└── Accessibility / Conformance Profile
```

综合 `human-interface-specification-v0.1` 暂时不删除，也不静默失效。Gate B Audit 前，它继续作为 umbrella source 与既有 Requirement ID 的来源；五个 Profile 是模块化 projection。

---

## 4. Requirement coverage

### Shared Foundation

继续共享：

- `IA-HI-BASE-001..003`
- `IA-HI-PR-001..006`

这些规则不复制成五套不同版本。

### Information Architecture

已有核心 Requirements：

- `IA-HI-IA-001..006`

覆盖：Task-based Entry Points、No Canonical Navigation Tree、IA Before Navigation UI、Stable Resource Pages、Multiple Paths、Breadcrumb as View。

新增显式 Gap：

- `HI-IA-GAP-001` Entry-point coverage；
- `HI-IA-GAP-002` Resource-page coverage；
- `HI-IA-GAP-003` Findability evaluation；
- `HI-IA-GAP-004` Compare architecture。

### Information Presentation

已有核心 Requirements：

- `IA-HI-IP-001..007`

覆盖：Summary Before Detail、非 YAML 镜像、层级、Concision、Human Labels、Progressive Disclosure、Source Visibility。

新增显式 Gap：

- `HI-IP-GAP-001` Strong Profile key-facts presentation；
- `HI-IP-GAP-002` Evidence / Assessment presentation；
- `HI-IP-GAP-003` Compare presentation；
- `HI-IP-GAP-004` density evaluation。

### Interaction

已有核心 Requirements：

- `IA-HI-INT-001..009`
- 复用 `IA-HI-GR-004 / 005 / 007` 作为 Graph interaction contract。

新增显式 Gap：

- `HI-INT-GAP-001` URL / History state；
- `HI-INT-GAP-002` Browser E2E；
- `HI-INT-GAP-003` error / empty / loading states；
- `HI-INT-GAP-004` future complex graph controls。

### Visual Presentation

已有核心 Requirements：

- `IA-HI-VIS-001..008`
- `IA-HI-ADP-001..004`
- `IA-HI-TOK-001..004`

新增显式 Gap：

- `HI-VIS-GAP-001` type / spacing / width scales；
- `HI-VIS-GAP-002` relation visual vocabulary；
- `HI-VIS-GAP-003` focus / motion evidence；
- `HI-VIS-GAP-004` DTCG-compatible token artifact。

### Accessibility / Conformance

已有核心 Requirements：

- `IA-HI-A11Y-001..006`
- `IA-HI-CONF-001..008`

新增显式 Gap：

- `HI-CONF-GAP-001` Browser harness；
- `HI-CONF-GAP-002` Requirement registry / report format；
- `HI-CONF-GAP-003` accessibility exception policy；
- `HI-CONF-GAP-004` human evaluation protocol；
- `HI-CONF-GAP-005` broader accessibility Capability modeling。

---

## 5. Adopt / Profile / Extend / Invent 审计

总体判断：**当前绝大多数规则不需要 Invent。**

| 领域 | 主要模式 | 判断 |
|---|---|---|
| HCD / task-first | ISO 9241-210 | Adopt / Profile |
| Interaction principles | ISO 9241-110 | Adopt / Profile |
| Information Presentation | ISO 9241-112 / 125 | Adopt / Profile |
| HTML Link / Button | HTML | Adopt |
| Accessibility | WCAG / WAI-ARIA | Adopt / Profile |
| APG patterns | mature authoring guidance | Profile |
| Design Tokens | DTCG format | Compatibility Profile |
| Graph facts vs view | IA Knowledge Model | IA-specific Profile |
| Flat graph / no single nav tree | IA Knowledge Model + IA method | IA-specific Profile |
| Human Evidence / Assessment presentation | IA Knowledge Model | **Extension needed later** |
| Compare View semantics | IA-specific task | **Gap; do not invent UI yet** |

这一结果符合项目原则：IA 的主要工作是**选择、组合、Profile 和验证**，不是创造一套全新的 HCI 学说。

---

## 6. 上游依据完整性

### 足够形成 Draft 的部分

- HCD process；
- Link / Button / native semantics；
- keyboard / basic accessibility；
- information hierarchy；
- visual hierarchy / contrast / reflow；
- progressive enhancement；
- Requirements → test evidence direction。

### Gate B 前仍需加强的部分

1. Compare 作为核心用户任务，目前缺更具体的 IA Profile；
2. Evidence / Assessment 的 Human Presentation 需要与 Knowledge Model v0 对齐；
3. Visual numeric scale 尚未有真实页面族验证，不应提前冻结；
4. Browser E2E / Accessibility Evidence 尚未成为正式流水线；
5. Human task evaluation 还没有统一最小模板；
6. Entry Point / findability 还没有 tree testing 或等价任务 evidence。

---

## 7. 冲突与边界

### 7.1 Breadcrumb / hierarchy vs Flat Graph

APG Breadcrumb 可以表达导航路径，但不能被解释成 Canonical Graph 的唯一父子层级。

结论：**无冲突，只要明确 Breadcrumb 是 View。**

### 7.2 ARIA widget vs native Web

APG 提供 Tree / complex widget patterns，但 IA 不因底层存在图或层级就自动采用 Tree Widget。

结论：原生 Link / Disclosure 优先；只有真实任务需要复杂 Widget 才进入对应 APG contract。

### 7.3 Design Systems vs normative standards

Apple / Material / USWDS / GOV.UK 等继续是 Reference Implementations。它们可以影响 pattern selection 和 implementation quality，不能自动产生 IA MUST。

### 7.4 DTCG Design Tokens status

DTCG 2025.10 是稳定 Community Group Final Report，不是 W3C Recommendation。

结论：可以作为兼容格式方向，但不能在依据层级中冒充正式 W3C Standard。

### 7.5 Existing website vs Profile

第一次 Audit 已发现网站存在 IA / Presentation / Browser test Gap。

结论：网站是 Reference Implementation / Test Bed，不能因为已有代码而反向降低 Requirements。

---

## 8. 当前 Gate B 判断

五个模块现在第一次达到：

> **Draft coverage exists and can be audited independently.**

但 Gate B **仍然 NOT PASS**，因为还缺：

- 对五个 Draft 的第二轮 Requirement audit；
- cross-profile Gap 排序；
- Browser E2E / Accessibility evidence；
- 至少一个 task-based Human evaluation；
- 对当前 Reference Implementation 的新一轮 conformance evidence；
- 明确哪些 Gap 必须在 Gate B 前关闭、哪些可以进入 post-Gate backlog。

因此不能把“写出五份文档”误报为 Gate B 完成。

---

## 9. 推荐下一顺序

```text
Five Draft Profiles
✅ 当前小步
        ↓
Requirement / Gap priority audit
        ↓
P0: Object Page + semantic structure conformance slice
        ↓
#13 Browser E2E / Accessibility foundation
        ↓
Task-based IA evaluation
        ↓
Gate B Audit
```

重点：下一步可以开始让规范重新接触真实实现，但目标是**产生 Conformance Evidence**，而不是恢复“想到什么功能就加什么功能”的开发方式。
