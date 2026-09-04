# Public Knowledge Commons & Personal Knowledge Space v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: active long-term direction / research-sensitive
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T19:53:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> Status: Long-term product direction. The public/personal boundary is a design commitment; exact personalization models, schemas, ranking algorithms and storage contracts remain research questions.

## 1. Why this document exists

InteropAtlas 同时追求两个看似相反、实际互补的目标：

1. **为全人类维护一个尽可能完整、开放、共享的互操作知识世界；**
2. **让每个人只在需要时面对适合自己当前状态的那一部分知识，并以适合自己的方式理解和操作它。**

因此，未来 IA 不应只有“公共网站”，也不应只有“个人推荐”。它应允许公共知识基础设施与个人知识空间在清晰边界下协同。

## 2. Public Knowledge Commons

公共层是 InteropAtlas 的共同事实世界。

```text
Standards / Methods / Implementations / Organizations
Capabilities / Scenarios / Relations / Events
Evidence / Sources / Provenance / Lifecycle / Gaps
                         ↓
                 Canonical Knowledge
```

公共层的目标不是针对某个人优化，而是尽可能准确地描述方案空间，并保持：

- Stable Identity；
- Evidence Before Assertion；
- Fact ≠ Assessment；
- explicit unknown / not-recorded；
- Lifecycle / historical recoverability；
- Human / Machine readability；
- open contribution with bounded authority。

同一事实不应因为不同用户的兴趣而变成不同事实。

## 3. Personal Knowledge Space

个人知识空间是建立在公共 Atlas 之上的个人认知与注意力层。

它回答的不是“世界是什么”，而是：

> **对这个人，在这个时间、这个状态、这个任务下，什么值得出现？以什么方式出现？**

未来可能使用的 Personal State 包括但不限于：

```text
Current goals
Current work / projects
Learning topics
Long-term interests
Recent activity
Known / unknown knowledge
Time budget
Desired depth
Cognitive / media preference
Accessibility needs
Explicit user controls
Temporary life/context state
```

例如，一个用户近期主要从事 TVC / 视频制作，系统可以提高视频接口、时间码、色彩、编码、同步、元数据等相关知识的注意力优先级；当用户转向通信学习时，Personal Perspective 可以重新求值。

这些状态不应自动成为公共 Canonical Knowledge。

## 4. Personalization has two independent axes

### 4.1 What to show — Content / Attention Personalization

决定：

- 什么进入 Active Window；
- 什么被强调；
- 什么被降权；
- 什么暂时隐藏但仍可恢复；
- 什么新的相邻领域值得主动探索。

这主要属于 Perspective / Selection / Ranking。

### 4.2 How to show — Representation Personalization

决定同一知识怎样表达。

```text
同一 Canonical Knowledge
        │
        ├─ Article / Text
        ├─ Diagram / Image
        ├─ Timeline
        ├─ Graph
        ├─ Compare / Matrix
        ├─ Audio / Video
        ├─ Interactive Explanation
        ├─ Simulation
        └─ Game-like Experience
```

某人喜欢文字并不意味着文字是知识的本体；某人更适合图像、视频或交互，也不意味着需要复制一份知识。

## 5. Public Perspective vs Personal Perspective

未来应避免把所有 Perspective 混成一个概念。

### Knowledge / Public Perspective

主要根据知识本身选择：

- Domain / type；
- organization；
- time；
- lifecycle；
- version；
- relation distance；
- evidence quality；
- scope / context；
- explicit query。

### Personal Perspective

把公共知识与个人状态结合：

```text
Canonical Knowledge
+
User State
+
Current Intent
+
Context
+
Representation Preference
        ↓
Personal Perspective
        ↓
Selected / Ranked / Emphasized Knowledge
```

Personal Perspective 可以是动态、临时、保存、可分享或持续重新求值的；具体语义需要后续 Prior Art、隐私、安全与真实实验支持。

## 6. Personal Attention Lifecycle

个人注意力生命周期与公共知识 Lifecycle 不是同一件事。

公共层可能记录：

```text
current / deprecated / superseded / historical / archived
```

个人层可能记录或计算：

```text
active / warm / cold / temporarily relevant / reactivated
```

一个 superseded 标准可以在公共层保持历史有效记录，并在某个维修旧设备的用户 Personal Perspective 中重新成为 Active。

因此：

> **Public lifecycle describes knowledge state; Personal lifecycle describes attention state.**

## 7. Anti-filter-bubble requirements

个性化必须从第一天就承认信息茧房风险。

长期产品应至少支持：

- `Public / Neutral View`：回到公共基线；
- `Why am I seeing this?`：解释选择或排序依据；
- `What is being de-emphasized?`：在合理范围内检查被弱化的知识；
- `Expand beyond my perspective`：主动扩大视野；
- `Explore distant but important knowledge`：探索远离当前兴趣但重要的领域；
- 临时关闭历史行为影响；
- 用户主动调整 Personal State / Perspective；
- 多 Perspective 并存，而不是一个永久画像；
- 避免把商业 Engagement 最大化当成知识相关性的代理。

## 8. Privacy and ownership boundary

Personal Knowledge Space 可能包含敏感的个人状态，因此未来必须明确：

- 什么只存在本地；
- 什么可以同步；
- 什么可以分享；
- 什么可以被 Agent 使用；
- 什么可以被公共 Atlas 学习；
- 如何撤回；
- 如何导出和迁移；
- 如何避免 Personal State 变成公共 Provenance 的意外泄露源。

默认原则应倾向：**Personal State is private unless explicitly shared.**

具体隐私模型尚未定案。

## 9. Interoperable personal space

因为 InteropAtlas 本身研究互操作，Personal Knowledge Space 长期应优先考虑：

- Perspective 可导出；
- Preferences 可携带；
- Workspace state 可迁移；
- Personal overlays 与 Canonical IDs 对齐；
- 不要求把公共知识复制进每个个人库；
- 不把用户锁死在单一 IA 官方客户端；
- 允许第三方客户端在遵守公共 Contract 的前提下产生新的个人体验。

这意味着 GitHub 仓库可以继续是公共知识和项目建设的重要载体，但未来完整 IA 不应被限制为“只能通过 GitHub 使用”。

## 10. Human + Agent in personal space

Agent 可以成为个人知识空间中的协作者，但不应成为不可解释的替用户决定者。

未来可能包括：

- 根据当前目标帮助建立 Perspective；
- 解释为什么某知识相关；
- 操作当前 Workspace；
- 帮助用户跳出既有 Perspective；
- 发现公共 Atlas 中的缺口；
- 把个人使用中发现的新事实转成 Candidate Contribution；
- 在用户授权下维护 Personal Attention State。

Agent 对个人空间的操作权限与对公共 Canonical Knowledge 的写入权限必须分开。

## 11. From personal use back to the commons

个人化不是单向消费。

```text
Public Atlas
    ↓
Personal Perspective / Workspace
    ↓
Real use / problem solving
    ↓
Discover gap / error / new relation / new implementation
    ↓
Candidate contribution
    ↓
Validation / Review
    ↓
Public Atlas grows
```

这使公共知识与个人知识空间形成正反馈，而不是彼此隔离。

## 12. What is decided vs not decided

### Long-term direction already decided

- IA 是公共知识基础设施；
- 个人知识空间建立在公共 Atlas 之上；
- 个性化同时影响“显示什么”和“怎样显示”；
- 个性化不能改变公共事实；
- 个性化必须透明、可逆、允许回到公共世界；
- Personal State 与 Public Canonical Knowledge 必须有隐私/权限边界；
- 长期应避免客户端锁定并支持可互操作的个人空间。

### Still research / experiment questions

- Personal State 的最小数据模型；
- Perspective 是否成为持久化一等对象；
- 动态/连续求值机制；
- 推荐与 Ranking 算法；
- 用户画像是否需要、如何最小化；
- 本地优先 vs 云同步；
- Personal Knowledge Graph / overlay 是否需要；
- Representation preference 如何学习；
- 如何量化信息茧房与探索质量；
- 如何安全地让 Agent 操作 Personal Workspace；
- 哪些协议/标准可用于 Perspective / Preference / Workspace portability。

这些问题必须继续遵守 `Adopt → Profile → Extend → Invent`，不能因为长期方向清晰就提前冻结实现。
