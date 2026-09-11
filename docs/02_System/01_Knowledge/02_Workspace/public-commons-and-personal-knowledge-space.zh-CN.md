# 公共知识共同体与个人知识空间 v0.1（Public Knowledge Commons & Personal Knowledge Space）

<!-- InteropAtlas Document Metadata v0
Document Status: active long-term direction / research-sensitive
Document Created At: 2026-09-04T19:53:00+08:00
Document Updated At: 2026-09-04T22:40:00+08:00
Metadata Provenance: direct_record
Lifecycle Time Provenance: direct_record
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human Owner — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: pending Owner review
  GitHub Actor: ff6962757
-->

> 状态：当前有效的长期产品方向（Active Long-term Direction）。公共 / 个人边界已经作为设计方向确定；具体个性化模型、模式（Schema）、排序算法和存储契约仍属于研究问题。

## 1. 为什么需要这份文档

InteropAtlas 同时追求两个看似相反、实际互补的目标：

1. **为全人类维护一个尽可能完整、开放、共享的互操作知识世界；**
2. **让每个人只在需要时面对适合自己当前状态的那一部分知识，并以适合自己的方式理解和操作它。**

因此，未来 IA 不应只有“公共网站”，也不应只有“个人推荐”。它应允许公共知识基础设施与个人知识空间在清晰边界下协同。

## 2. 公共知识共同体（Public Knowledge Commons）

公共层是 InteropAtlas 的共同事实世界。

```text
标准 / 方法 / 实现 / 组织
（Standards / Methods / Implementations / Organizations）
能力 / 场景 / 关系 / 事件
（Capabilities / Scenarios / Relations / Events）
证据 / 来源 / 来源追踪 / 生命周期 / 缺口
（Evidence / Sources / Provenance / Lifecycle / Gaps）
                         ↓
                 规范知识（Canonical Knowledge）
```

公共层的目标不是针对某个人优化，而是尽可能准确地描述方案空间，并保持：

- **稳定身份（Stable Identity）**；
- **先有证据，再有断言（Evidence Before Assertion）**；
- **事实 ≠ 评估（Fact ≠ Assessment）**；
- 明确的未知 / 未记录状态（explicit unknown / not-recorded）；
- 生命周期 / 历史可恢复性（Lifecycle / Historical Recoverability）；
- 人 / 机器可读（Human / Machine Readability）；
- 有权威边界的开放贡献（Open Contribution with Bounded Authority）。

同一事实不应因为不同用户的兴趣而变成不同事实。

## 3. 个人知识空间（Personal Knowledge Space）

个人知识空间是建立在公共知识地图（Public Atlas）之上的个人认知与注意力层。

它回答的不是“世界是什么”，而是：

> **对这个人，在这个时间、这个状态、这个任务下，什么值得出现？以什么方式出现？**

未来可能使用的个人状态（Personal State）包括但不限于：

```text
当前目标（Current Goals）
当前工作 / 项目（Current Work / Projects）
学习主题（Learning Topics）
长期兴趣（Long-term Interests）
近期活动（Recent Activity）
已知 / 未知知识（Known / Unknown Knowledge）
时间预算（Time Budget）
期望深度（Desired Depth）
认知 / 媒介偏好（Cognitive / Media Preference）
无障碍需求（Accessibility Needs）
用户显式控制（Explicit User Controls）
临时生活 / 上下文状态（Temporary Life / Context State）
```

例如，一个用户近期主要从事影视广告（TVC）/ 视频制作，系统可以提高视频接口、时间码、色彩、编码、同步、元数据等相关知识的注意力优先级；当用户转向通信学习时，个人视角（Personal Perspective）可以重新求值。

这些状态不应自动成为公共规范知识（Canonical Knowledge）。

## 4. 个性化有两个相互独立的轴

### 4.1 显示什么——内容 / 注意力个性化（Content / Attention Personalization）

决定：

- 什么进入当前活动窗口（Active Window）；
- 什么被强调；
- 什么被降权；
- 什么暂时隐藏但仍可恢复；
- 什么新的相邻领域值得主动探索。

这主要属于视角 / 选择 / 排序（Perspective / Selection / Ranking）。

### 4.2 怎样显示——表达个性化（Representation Personalization）

决定同一知识怎样表达。

```text
同一规范知识（Canonical Knowledge）
        │
        ├─ 文章 / 文字（Article / Text）
        ├─ 图示 / 图像（Diagram / Image）
        ├─ 时间线（Timeline）
        ├─ 关系图（Graph）
        ├─ 比较 / 矩阵（Compare / Matrix）
        ├─ 音频 / 视频（Audio / Video）
        ├─ 交互解释（Interactive Explanation）
        ├─ 模拟（Simulation）
        └─ 游戏式体验（Game-like Experience）
```

某人喜欢文字并不意味着文字是知识的本体；某人更适合图像、视频或交互，也不意味着需要复制一份知识。

## 5. 公共视角与个人视角（Public Perspective vs Personal Perspective）

未来应避免把所有视角（Perspective）混成一个概念。

### 知识 / 公共视角（Knowledge / Public Perspective）

主要根据知识本身选择：

- 领域 / 类型（Domain / Type）；
- 组织（Organization）；
- 时间（Time）；
- 生命周期（Lifecycle）；
- 版本（Version）；
- 关系距离（Relation Distance）；
- 证据质量（Evidence Quality）；
- 范围 / 上下文（Scope / Context）；
- 显式查询（Explicit Query）。

### 个人视角（Personal Perspective）

把公共知识与个人状态结合：

```text
规范知识（Canonical Knowledge）
+
用户状态（User State）
+
当前意图（Current Intent）
+
上下文（Context）
+
表达偏好（Representation Preference）
        ↓
个人视角（Personal Perspective）
        ↓
经过选择 / 排序 / 强调的知识
（Selected / Ranked / Emphasized Knowledge）
```

个人视角可以是动态、临时、保存、可分享或持续重新求值的；具体语义需要后续成熟先例研究（Prior Art）、隐私、安全与真实实验支持。

## 6. 个人注意力生命周期（Personal Attention Lifecycle）

个人注意力生命周期与公共知识生命周期（Lifecycle）不是同一件事。

公共层可能记录：

```text
当前 / 已废弃 / 已被取代 / 历史 / 已归档
（current / deprecated / superseded / historical / archived）
```

个人层可能记录或计算：

```text
活跃 / 温热 / 冷却 / 暂时相关 / 重新激活
（active / warm / cold / temporarily relevant / reactivated）
```

一个已被取代（superseded）的标准可以在公共层保持历史有效记录，并在某个维修旧设备用户的个人视角中重新成为活跃知识（Active）。

因此：

> **公共生命周期描述知识状态；个人生命周期描述注意力状态。**  
> *Public lifecycle describes knowledge state; Personal lifecycle describes attention state.*

## 7. 反信息茧房要求（Anti-filter-bubble Requirements）

个性化必须从第一天就承认信息茧房风险。

长期产品应至少支持：

- **公共 / 中立视图（Public / Neutral View）**：回到公共基线；
- **为什么我会看到这个？（Why am I seeing this?）**：解释选择或排序依据；
- **哪些知识正在被弱化？（What is being de-emphasized?）**：在合理范围内检查被弱化的知识；
- **跳出我的当前视角（Expand beyond my perspective）**：主动扩大视野；
- **探索遥远但重要的知识（Explore distant but important knowledge）**：探索远离当前兴趣但重要的领域；
- 临时关闭历史行为影响；
- 用户主动调整个人状态 / 视角（Personal State / Perspective）；
- 多个视角并存，而不是一个永久画像；
- 避免把商业参与度（Engagement）最大化当成知识相关性的代理。

## 8. 隐私与所有权边界（Privacy and Ownership Boundary）

个人知识空间可能包含敏感的个人状态，因此未来必须明确：

- 什么只存在本地；
- 什么可以同步；
- 什么可以分享；
- 什么可以被智能体（Agent）使用；
- 什么可以被公共知识地图学习；
- 如何撤回；
- 如何导出和迁移；
- 如何避免个人状态成为公共来源追踪（Provenance）的意外泄露源。

默认原则应倾向：

> **除非用户明确分享，否则个人状态保持私有。**  
> *Personal State is private unless explicitly shared.*

具体隐私模型尚未定案。

## 9. 可互操作的个人空间（Interoperable Personal Space）

因为 InteropAtlas 本身研究互操作，个人知识空间长期应优先考虑：

- 视角（Perspective）可导出；
- 偏好（Preferences）可携带；
- 工作空间状态（Workspace State）可迁移；
- 个人叠加层（Personal Overlays）与规范标识（Canonical IDs）对齐；
- 不要求把公共知识复制进每个个人库；
- 不把用户锁死在单一 IA 官方客户端；
- 允许第三方客户端在遵守公共契约（Contract）的前提下产生新的个人体验。

这意味着 GitHub 仓库可以继续是公共知识和项目建设的重要载体，但未来完整 IA 不应被限制为“只能通过 GitHub 使用”。

## 10. 个人空间中的人与智能体（Human + Agent）

智能体（Agent）可以成为个人知识空间中的协作者，但不应成为不可解释的替用户决定者。

未来可能包括：

- 根据当前目标帮助建立视角（Perspective）；
- 解释为什么某知识相关；
- 操作当前工作空间（Workspace）；
- 帮助用户跳出既有视角；
- 发现公共知识地图中的缺口；
- 把个人使用中发现的新事实转成候选贡献（Candidate Contribution）；
- 在用户授权下维护个人注意力状态（Personal Attention State）。

智能体对个人空间的操作权限与对公共规范知识（Canonical Knowledge）的写入权限必须分开。

## 11. 从个人使用回到公共共同体（From Personal Use Back to the Commons）

个人化不是单向消费。

```text
公共知识地图（Public Atlas）
    ↓
个人视角 / 工作空间（Personal Perspective / Workspace）
    ↓
真实使用 / 问题解决（Real Use / Problem Solving）
    ↓
发现缺口 / 错误 / 新关系 / 新实现
（Discover Gap / Error / New Relation / New Implementation）
    ↓
候选贡献（Candidate Contribution）
    ↓
验证 / 审查（Validation / Review）
    ↓
公共知识地图继续成长
```

这使公共知识与个人知识空间形成正反馈，而不是彼此隔离。

## 12. 已确定与尚未确定的内容

### 已确定的长期方向（Long-term Direction Already Decided）

- IA 是公共知识基础设施；
- 个人知识空间建立在公共知识地图之上；
- 个性化同时影响“显示什么”和“怎样显示”；
- 个性化不能改变公共事实；
- 个性化必须透明、可逆、允许回到公共世界；
- 个人状态（Personal State）与公共规范知识（Public Canonical Knowledge）必须有隐私 / 权限边界；
- 长期应避免客户端锁定，并支持可互操作的个人空间。

### 仍需研究 / 实验的问题（Still Research / Experiment Questions）

- 个人状态（Personal State）的最小数据模型；
- 视角（Perspective）是否成为持久化一等对象；
- 动态 / 连续求值机制；
- 推荐与排序（Ranking）算法；
- 用户画像是否需要、如何最小化；
- 本地优先与云同步（Local-first vs Cloud Sync）；
- 是否需要个人知识图谱 / 叠加层（Personal Knowledge Graph / Overlay）；
- 如何学习表达偏好（Representation Preference）；
- 如何量化信息茧房与探索质量；
- 如何安全地让智能体操作个人工作空间（Personal Workspace）；
- 哪些协议 / 标准可用于视角 / 偏好 / 工作空间的可携带性（Perspective / Preference / Workspace Portability）。

这些问题必须继续遵守：

> **采用（Adopt）→ 配置（Profile）→ 扩展（Extend）→ 发明（Invent）**

不能因为长期方向清晰就提前冻结实现。
