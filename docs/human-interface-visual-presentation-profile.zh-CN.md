# InteropAtlas Visual Presentation Profile v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: **Draft / Gate B Module**
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

> 状态：**Draft / Gate B Module**
>
> Package: [`human-interface-profiles-v0.1.zh-CN.md`](human-interface-profiles-v0.1.zh-CN.md)

## 1. 目标

本 Profile 约束：

> **信息、关系、状态和交互怎样通过层级、分组、文字、空间、颜色与其他视觉变量被清楚感知和区分。**

v0.1 不冻结品牌色、字体品牌或最终美学风格。视觉系统首先服务信息职责、交互状态和 Accessibility。

---

## 2. 上游依据

### Normative / high-authority

- ISO 9241-112:2025 — information presentation；
- ISO 9241-125:2017 — visual presentation of information；
- ISO 9241-161:2025 — visual user-interface elements；
- WCAG 2.2 — contrast、non-text contrast、focus、reflow、text resize、motion considerations；
- CSS / HTML Web platform semantics。

### Mature methods / reference practice

- Gestalt grouping principles；
- visual hierarchy；
- semantic color / state systems；
- GOV.UK / USWDS / Carbon / Material / Apple HIG 作为 Reference Implementations；
- DTCG Design Tokens Format 2025.10 作为机器交换格式参考。

DTCG 2025.10 是 Community Group Final Report，不是 W3C Recommendation。

---

## 3. Requirements

### `IA-HI-VIS-001` — Visual Hierarchy Serves Information

颜色、字体、空间、边框、尺寸和布局 MUST 有信息或交互职责；纯装饰 SHOULD 克制。

- 用户任务：Scan / Understand
- 采用方式：**Profile**
- 上游：ISO 9241-112 / 125
- Conformance：`Visual + Human + Review`

### `IA-HI-VIS-002` — Consistent Visual Vocabulary

相同语义 SHOULD 使用一致视觉表达，不同语义 SHOULD 足够可区分。

- 采用方式：**Adopt + Profile**
- 上游：ISO 9241-125 / 161
- Conformance：`Static + Multi-page + Visual`

### `IA-HI-VIS-003` — Color Is Not the Only Channel

颜色 MUST NOT 是类型、关系、错误、状态、选择的唯一表达渠道。

- 采用方式：**Adopt**
- 上游：WCAG 2.2 / ISO visual presentation
- Conformance：`Static + Accessibility`

### `IA-HI-VIS-004` — Controlled Information Density

信息密度 SHOULD 与任务匹配；高密度和大量留白都不是目标本身。

- 采用方式：**Profile**
- 上游：ISO 9241-112 / 125
- Conformance：`Human + Visual`
- 验收重点：重复 Relationship 区块、过早 Graph、无信息职责卡片等。

### `IA-HI-VIS-005` — Reading Width

长篇正文 SHOULD 使用受控阅读宽度，避免在大屏形成过长行长。

- 采用方式：**Profile**
- 上游：readability mature practice + ISO visual presentation
- Conformance：`Static + Visual + Responsive`

### `IA-HI-VIS-006` — Semantic Theme Equivalence

Light / Dark SHOULD 共享相同 semantic roles，再映射具体值。

- 采用方式：**Profile**
- 上游：WCAG + mature design-system practice
- Conformance：`Static + Accessibility + Visual`

### `IA-HI-VIS-007` — Focus Is Visible

键盘 focus MUST 清晰可见并满足适用 WCAG 要求。

- 采用方式：**Adopt**
- 上游：WCAG 2.2
- Conformance：`Browser + Accessibility`

### `IA-HI-VIS-008` — Motion Has Purpose

Motion MAY 用于反馈、连续性和空间关系解释；SHOULD NOT 成为无职责装饰，并 SHOULD 尊重 reduced-motion 偏好。

- 采用方式：**Adopt + Profile**
- 上游：WCAG / platform user preference
- Conformance：`Static + Browser + Accessibility`

---

## 4. Adaptive / Responsive Requirements

### `IA-HI-ADP-001` — Reflow First

核心内容 MUST 在窄屏、放大和 reflow 下可读可操作。

- Conformance：`Browser + Accessibility`

### `IA-HI-ADP-002` — Adaptive Navigation

Navigation MAY 随空间改变结构，但信息身份和任务 MUST 保持一致。

- Conformance：`Responsive + Human`

### `IA-HI-ADP-003` — No Desktop-only Core Task

核心任务 MUST NOT 依赖 hover、drag 或超宽屏。

- Conformance：`Browser + Accessibility`

### `IA-HI-ADP-004` — Large Screen Uses Space Intentionally

大屏 MAY 增加并行上下文，但 SHOULD NOT 只是拉宽正文。

- Conformance：`Visual + Human`

---

## 5. Design Tokens Requirements

### `IA-HI-TOK-001` — Semantic Tokens

稳定视觉决策 SHOULD 使用 semantic tokens 表达，减少散落的 magic values。

- 用户任务 / Context：跨页面识别一致的视觉语义，并让实现可维护
- 采用方式：**Profile**
- 上游：ISO 9241-125 / 161 的一致视觉表达；成熟 Design System practice
- Conformance：`Static + Machine + Multi-page`

### `IA-HI-TOK-002` — Token ≠ Design Rule

Token MUST NOT 被当成“为什么这样设计”的全部规范。Profile 定义语义；Token 负责值的机器交换。

- 用户任务 / Context：理解视觉语义、审查设计决策
- 采用方式：**IA-specific Profile**
- 上游：DTCG token model + IA Requirement / Profile 分层原则
- Conformance：`Review + Static`

### `IA-HI-TOK-003` — DTCG Compatibility

机器可读 Token Format SHOULD 优先评估兼容 DTCG Design Tokens Format 2025.10。

- 用户任务 / Context：Human / Agent / tooling 交换和处理视觉 tokens
- 采用方式：**Compatibility Profile**
- 上游：DTCG Design Tokens Format 2025.10（Community Group Final Report）
- Conformance：`Static + Machine + Review`
- 说明：DTCG 不是 W3C Recommendation；兼容目标不得被描述成 W3C Recommendation conformance。

### `IA-HI-TOK-004` — Theme Mapping

主题差异 SHOULD 通过 semantic token → concrete value 映射；组件不应各自维护独立主题逻辑。

- 用户任务 / Context：在 Light / Dark 等主题中保持相同信息和状态语义
- 采用方式：**Profile**
- 上游：WCAG；mature semantic-token / theming practice
- Conformance：`Static + Machine + Accessibility + Multi-page`

本轮只定义 Token 的语义合同与兼容方向，不冻结具体 token 数值。

---

## 6. 第一版语义视觉层

未来 Tokens SHOULD 优先表达这些角色，而不是直接从颜色名开始：

```text
text-primary
text-secondary
surface-primary
surface-raised
border-subtle
link
focus
state-selected
state-error
state-warning
relation-*
evidence-*
spacing-*
typography-*
```

是否需要把不同 Relation kind 映射为独立颜色，必须先经过 Information Presentation + Accessibility 审查；不能因为 Graph 容易着色就给每种关系随意分配颜色。

---

## 7. 当前实现证据

第一次 Audit 已确认：

- Light / Dark 主文字与链接对比度没有发现明显问题；
- 现有 CSS 已有一层很薄的 semantic variables；
- 页面有基本 max-width；
- 颜色不是 Relation / Filter 的唯一信息渠道；
- 但 Tokens 体系还非常薄；
- 视觉层级仍受重复关系区块影响；
- `smooth` scroll 曾缺少 reduced-motion 处理；
- focus appearance 尚缺真实 Browser test。

因此现有视觉实现可作为 test bed，不能视为 Visual Profile 已完成。

---

## 8. 当前 Gap

### `HI-VIS-GAP-001` — Type / spacing / width scales

尚未冻结 typography scale、spacing scale、prose width、layout width。应先用真实 Object Page / Compare / Index 任务验证，再形成值层。

### `HI-VIS-GAP-002` — Relation visual vocabulary

需要定义 Relation、field reference、Evidence、Assessment、status 等哪些语义值得视觉编码，以及编码优先使用文字、形状、边框、位置还是颜色。

### `HI-VIS-GAP-003` — Focus and motion evidence

需要 Browser E2E 验证 focus visibility、reduced-motion、zoom/reflow。

### `HI-VIS-GAP-004` — Token artifact

Gate B Draft 只要求方向与语义合同；真正 DTCG-compatible token artifact 应在至少一个页面族的信息职责稳定后生成，避免把当前临时 CSS 固化为规范。

---

## 9. 与其他 Profile 的依赖

- Information Architecture 决定哪些信息 / View 需要视觉化；
- Information Presentation 决定层级和密度职责；
- Interaction 决定 hover/focus/selected/loading 等状态；
- Accessibility / Conformance 对所有视觉编码设置硬约束。

**Reference Implementations 可以告诉 IA“成熟系统怎样做”，但不能直接决定 IA 的品牌视觉或语义编码。**
