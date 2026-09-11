# InteropAtlas Human Interface Profiles v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft Package / Gate B Verified Primary Baseline**
Document Created At: 2026-09-02T07:39:56+08:00
Document Updated At: 2026-09-05T14:58:00+08:00
Metadata Backfilled At: 2026-09-02T11:35:52+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Owner-authorized consolidation
  GitHub Actor: ff6962757
-->

> 状态：**Draft Package / Gate B Verified Primary Baseline**
>
> Parent: #14
>
> Consolidation work item: #78
>
> Final Gate B audit: [`gate-b-final-conformance-audit-2026-09-02.zh-CN.md`](/03_Evolution/01_Research/02_Audits/gate-b-final-conformance-audit-2026-09-02.zh-CN.md)

## 1. 目的

本文件是 InteropAtlas Human Interface Standards Package 的模块入口，也是当前 Human Interface Living Specification 的 Primary Home。

早期综合草案已经完成其收敛作用；Gate B 后，五个 Profile 将同一组 `IA-HI-*` Requirements 拆成独立、可审计、可测试的模块。当前实现和后续规范维护应从本 Package 与五个 Profile 获取 Human Interface 合同：

1. [`human-interface-information-architecture-profile.zh-CN.md`](/docs/02_System/02_Interface/02_Profiles/human-interface-information-architecture-profile.zh-CN.md)
2. [`human-interface-information-presentation-profile.zh-CN.md`](/docs/02_System/02_Interface/02_Profiles/human-interface-information-presentation-profile.zh-CN.md)
3. [`human-interface-interaction-profile.zh-CN.md`](/docs/02_System/02_Interface/02_Profiles/human-interface-interaction-profile.zh-CN.md)
4. [`human-interface-visual-presentation-profile.zh-CN.md`](/docs/02_System/02_Interface/02_Profiles/human-interface-visual-presentation-profile.zh-CN.md)
5. [`human-interface-accessibility-conformance-profile.zh-CN.md`](/docs/02_System/02_Interface/02_Profiles/human-interface-accessibility-conformance-profile.zh-CN.md)

这些文件是对同一套 Requirements 的模块化、依据补全和验收方式显式化，不是第二套规则。

2026-09-02 Final Conformance Audit 已确认该 Draft Package 达到 Gate B Foundation 的最小可依赖状态。这里的“Primary Baseline”表示当前 Living Document 的唯一主要维护入口；它**不等于**把整个 Package 晋升为 Stable Specification，稳定状态仍需独立治理决策。

---

## 2. 共同采用原则

所有 Profile 共同遵守：

> **Adopt → Profile → Extend → Invent**

优先级：

```text
用户任务 / Context of Use
        ↓
正式标准与 Web 语义
ISO / WCAG / HTML / WAI-ARIA
        ↓
成熟 HCI / IA / Visualization 方法
        ↓
成熟 Design Systems / Reference Implementations
        ↓
IA Profile
        ↓
必要的 IA-specific Extension
```

Design System、产品实践和研究方法不能因为“成熟”就自动成为 IA 的规范性要求。

---

## 3. 共同基础 Requirements

下列要求属于五个 Profile 的共同上层约束，并继续使用已经稳定引用的 ID：

| Requirement | 核心约束 | 主要依据 | 采用方式 |
|---|---|---|---|
| `IA-HI-BASE-001` | 重要设计先记录用户任务与上游依据 | ISO 9241-210 | Profile |
| `IA-HI-BASE-002` | Reference Implementation 不自动成为 IA 规范 | HCD / evidence discipline | IA Profile |
| `IA-HI-BASE-003` | 偏离上游标准时记录原因与验证方式 | HCD / conformance | IA Profile |
| `IA-HI-PR-001` | Knowledge Infrastructure First | ISO 9241-210 / 112 | IA Profile |
| `IA-HI-PR-002` | User Task Before Component | ISO 9241-210 | Adopt + Profile |
| `IA-HI-PR-003` | Familiarity Before Novelty | ISO 9241-110 | Adopt + Profile |
| `IA-HI-PR-004` | User Agency and Recoverability | ISO 9241-110 | Adopt + Profile |
| `IA-HI-PR-005` | Facts / Graph / View 分离 | IA Knowledge Model | IA-specific Profile |
| `IA-HI-PR-006` | Progressive Enhancement | Web mature practice | Profile |

---

## 4. Requirement 的最小记录格式

五个 Profile 中的重要 Requirement 至少记录：

```text
Requirement ID
用户任务 / Context
规则
上游依据
采用方式：Adopt / Profile / Extend / Invent
Conformance 方法
依赖 / 例外（如有）
```

Conformance 方法允许分成：

- `Static` — 静态结构 / 源码 / 构建产物可确定；
- `Browser` — 需要真实浏览器行为；
- `Accessibility` — 自动 + 键盘 + 辅助技术 / 人工检查；
- `Human` — 需要任务评价、Tree Testing、可用性观察等；
- `Data` — 需要检查 Canonical Facts / Graph / View 不变量；
- `Review` — 需要设计 / 语义 Review，不能由机器单独判断。

---

## 5. Profile 之间的职责边界

```text
Information Architecture
“人通过什么结构与路径找到东西？”
        ↓
Information Presentation
“到了一个 View 后，信息以什么顺序与形式被理解？”
        ↓
Interaction
“用户怎样操作、改变状态、导航与恢复？”
        ↓
Visual Presentation
“这些信息与状态怎样被感知、区分和编码？”
        ↓
Accessibility / Conformance
“不同用户是否能完成任务，以及怎样证明实现符合要求？”
```

它们不是五个互不相干的 silo。

典型依赖：

- IA 不能用一个 Navigation Component 替代 Information Architecture；
- Information Presentation 不能为了排版改变 Canonical Facts；
- Interaction 必须服从 HTML / Accessibility 语义；
- Visual Presentation 不得用颜色作为唯一语义渠道；
- Accessibility / Conformance 横向验证前四个 Profile，而不只是“第五套样式规则”。

---

## 6. 冲突处理

发生冲突时按以下顺序处理：

1. 用户任务 / Context of Use；
2. 适用的正式标准；
3. Web 原生语义与 WCAG / WAI-ARIA；
4. 成熟方法 / Pattern；
5. Reference Implementation；
6. IA-specific Profile / Extension。

如果为了 IA 特有需求必须偏离上游成熟规则：

- MUST 记录偏离原因；
- SHOULD 记录影响范围；
- SHOULD 指定验证方法；
- 不得通过复制另一套 Design System 的视觉惯例来绕过冲突分析。

---

## 7. Primary Home 与历史综合草案

从本次仓库整理开始：

- 本 Package + 五个 Profile 是 Human Interface 当前唯一主要规范维护入口；
- 早期 integrated specification 不再作为并行 Living Specification 维护；其历史内容由 Git history / Evolution 保留；
- `IA-HI-*` Requirement IDs 保持连续，不因物理文档收敛而重新编号；
- Compare / Search 等独立功能 Contract 继续作为下游合同存在，不并入五个基础 Profile；
- 后续发现跨 Profile 冲突时，在对应 Primary Home 修正规则，并通过 Change / Audit 留痕，不重新创建第二份综合规范。

这次职责收口是 **Primary Home consolidation**，不是 Stable Specification promotion。

---

## 8. Gate B 状态

```text
Information Architecture Draft          ✅ auditable / representative evidence
Information Presentation Draft         ✅ auditable / representative evidence
Interaction Draft                      ✅ auditable / Browser evidence
Visual Presentation Draft              ✅ auditable / focus-motion-reflow evidence
Accessibility / Conformance Draft      ✅ auditable / Browser + task evidence
Requirement upstream traceability      ✅ Gate B minimum
Cross-profile conflict rules           ✅ v0.1 defined
Representative Resource Pages          ✅ four-family slice
Minimal Compare contract               ✅
Minimal Human Task Walkthrough         ✅
Gate B Final Conformance Audit         ✅ PASS
```

Gate B PASS 的准确含义是：**Foundation contract 已达到最小可依赖状态。**

它不意味着 Search、完整 Compare UI、大型 Graph、所有页面类型、完整 Visual Token artifact 或全面 WCAG certification 已完成。这些继续作为后续 Reference Implementation 与质量工作。
