# InteropAtlas Work Item Reference Seeding v0.1

> 状态：Draft Addendum to Open Collaboration Profile v0.1
>
> 目的：规定在发布 Issue / Work Item 时，如何预装任务已知会用到的 InteropAtlas 标准、成熟先例与上位规范，以减少后续 Human / Agent 重复检索，同时保留对新标准和新先例的持续发现能力。

## 1. 核心思想

任务发布者通常已经知道一部分高价值依据。如果这些依据已经进入 InteropAtlas，就不应该让每一位后续协作者重新从零搜索。

因此 Ready Work Item SHOULD 提供 **Reference Seeding（参考依据预装）**：

```text
已有项目知识
    ↓
任务发布时预装高价值依据
    ↓
Executor 从已知基线开始
    ↓
执行 Freshness / Delta Check
    ↓
发现新增标准 / 先例
    ↓
反哺 Atlas
```

Reference Seeding 是起点，不是封闭的参考文献清单。

## 2. 三层参考结构

### 2.1 Must Read（必须先读）

任务正确执行所必需的上位合同，例如：
- InteropAtlas Definition；
- 相关 IA Specification / Profile；
- Schema；
- Parent Issue / Decision；
- 直接约束本任务的正式标准。

Executor MUST 在开始实质工作前读取。

### 2.2 Seed References（已知参考）

Task Author 已经知道、且很可能帮助执行者的标准、成熟先例、方法或实现。

如果对象已经在 Atlas，SHOULD 优先引用其 stable object ID / repository object，而不是只贴外部 URL。

示例：

```text
Seed References
- standard: reuse_specification_3.3
- reference_project: w3c_browser_specs
- reference_project: github_collaboration_primitives
- reference_project: openssf_best_practices_badge
```

### 2.3 Freshness Check Required（仍需增量检查）

对以下任务，Executor SHOULD 检查是否出现了比 Seed References 更新或更合适的 Existing Standards & Prior Art：
- 标准 / 规范调查；
- 快速演进技术；
- AI / Agent 生态；
- Web / browser / accessibility；
- security / governance；
- 任何明确要求“current / latest”的任务。

## 3. Requirements

### IA-OC-RS-001 — Ready Task 应优先复用 Atlas 内已有依据

如果某个已知相关 Standard / Precedent 已经是 Canonical Atlas Object，Task Author SHOULD 在 Work Item 中引用该对象，而不是要求 Executor 从互联网重新识别同一对象。

### IA-OC-RS-002 — Seed References 不得宣称穷尽

Seed References MUST 被理解为“已知起点”，MUST NOT 被描述为完整方案空间，除非任务本身已经完成有证据的 exhaustive coverage assessment。

### IA-OC-RS-003 — 新鲜度检查不能被预装参考替代

任务涉及当前状态或演进中的生态时，Executor SHOULD 进行 Freshness / Delta Check，确认：
- 是否出现新版本；
- 是否出现替代标准；
- 是否出现新的成熟先例；
- 既有依据的状态是否改变；
- 是否有新的官方来源。

### IA-OC-RS-004 — 新发现应反哺 Atlas

如果任务执行中发现了明确相关、可复用且符合收录边界的新 Standard / Mature Precedent / Method / Implementation，Executor SHOULD：
1. 在当前任务允许范围内纳入 Atlas；或
2. 创建明确的后续 intake / modeling Work Item。

不得只在任务报告里提到后让知识再次丢失。

### IA-OC-RS-005 — 预装参考应保持高信号

Task Author SHOULD 提供最相关的参考起点，而不是把整个 Atlas 邻居列表机械复制到 Issue。

优先顺序：
1. 直接上位规范；
2. 已被项目真实采用的依据；
3. 最接近任务问题的成熟先例；
4. 重要替代方案。

### IA-OC-RS-006 — 引用应尽量稳定

Atlas 内部引用 SHOULD 使用 stable object ID；外部依据 SHOULD 同时保留官方来源。

这样即使仓库未来从 `standards/` 迁移到 `data/standards/`，任务语义仍可恢复。

## 4. 推荐 Issue 区块

```text
Read First / Upstream Contracts
- docs/...profile...
- standard: bcp14_rfc2119_rfc8174

Seed References
- standard: reuse_specification_3.3
- reference_project: w3c_browser_specs
- reference_project: spdx_license_list

Freshness Check
- Required: yes
- Focus: repository standards / licensing / open-source governance
- Last seeded: 2026-09-01
```

## 5. 对效率的影响

Reference Seeding 会增加 Task Author 的前置成本，但减少 N 个后续执行者重复搜索相同基础资料的成本。

因此其价值随着任务复用次数增加而增加：

```text
一次任务作者投入
      ↓
Human A 少查一次
Agent B 少查一次
Agent C 少查一次
Reviewer D 也能看到依据
      ↓
共享知识被持续复用
```

它也让 Issue 成为更完整的公开上下文，使任务更容易被租约式接手、释放和 Handoff。

## 6. 与 InteropAtlas 反馈环的关系

长期形成：

```text
Atlas 已有对象
   ↓ seed
Work Item
   ↓ execute + freshness check
新发现
   ↓ curate
Atlas 扩充
   ↓
未来 Work Item 获得更好的 Seed References
```

这使 Open Collaboration Route 与 Curation Route 直接形成正反馈环。

## 7. 实施时机

本增补现在作为 Open Collaboration Profile 的 Draft requirement input。

如果后续进入 Collaboration Implementation Pilot（候选 Work Package B），Issue Template SHOULD 直接包含：
- Read First；
- Seed References；
- Freshness Check。
