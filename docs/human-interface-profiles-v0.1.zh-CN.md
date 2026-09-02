# InteropAtlas Human Interface Profiles v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft Package / Gate B Working Baseline**
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

> 状态：**Draft Package / Gate B Working Baseline**
>
> Parent: #14
>
> Consolidation work item: #78

## 1. 目的

本文件是 InteropAtlas Human Interface Standards Package 的模块入口。

现有 [`human-interface-specification-v0.1.zh-CN.md`](human-interface-specification-v0.1.zh-CN.md) 已经形成一套综合草案，但 Gate B 要求这些规则能够被分成独立、可审计、可测试的 Profile，而不是所有规则长期挤在一个大文件中。

因此 v0.1 Package 分成五个 Profile：

1. [`human-interface-information-architecture-profile-v0.1.zh-CN.md`](human-interface-information-architecture-profile-v0.1.zh-CN.md)
2. [`human-interface-information-presentation-profile-v0.1.zh-CN.md`](human-interface-information-presentation-profile-v0.1.zh-CN.md)
3. [`human-interface-interaction-profile-v0.1.zh-CN.md`](human-interface-interaction-profile-v0.1.zh-CN.md)
4. [`human-interface-visual-presentation-profile-v0.1.zh-CN.md`](human-interface-visual-presentation-profile-v0.1.zh-CN.md)
5. [`human-interface-accessibility-conformance-profile-v0.1.zh-CN.md`](human-interface-accessibility-conformance-profile-v0.1.zh-CN.md)

这些文件首先是对已经存在的 `IA-HI-*` Requirements 做**模块化、依据补全和验收方式显式化**，不是重新发明第二套 Human Interface 规则。

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

下列要求属于五个 Profile 的共同上层约束，继续使用综合规范中的稳定 ID：

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

## 7. 与综合规范的关系

在 Gate B Audit 完成前：

- `human-interface-specification-v0.1.zh-CN.md` 继续作为综合源与历史稳定 Requirement ID 的来源；
- 五个 Profile 是 Gate B 的**模块化 Draft Projection**；
- 两者共享同一 `IA-HI-*` Requirement IDs；
- 本轮不通过改 ID 制造“新规范”；
- 如果发现内容冲突，应进入 #14 / #78 Review，而不是静默选择其中一个版本。

Gate B Audit 通过后，再决定综合文件是继续作为 umbrella specification，还是由 Package index + 五个 Profile 正式取代其规范职责。

---

## 8. 当前 Gate B 状态

```text
Information Architecture Draft          🟡 extracted / audit pending
Information Presentation Draft         🟡 extracted / audit pending
Interaction Draft                      🟡 extracted / audit pending
Visual Presentation Draft              🟡 extracted / audit pending
Accessibility / Conformance Draft      🟡 extracted / audit pending
Requirement upstream traceability      🟡 improving
Cross-profile conflict rules           ✅ v0.1 defined
Representative machine intake path     ✅ usable
Gate B conformance audit               ⬜ pending
```

当前目标不是马上让 Gate B 变成 PASS，而是让五个模块第一次具备**可单独审计的形态**。
