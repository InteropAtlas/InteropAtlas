# InteropAtlas 人类可读路线（暂定参考）

<!-- InteropAtlas Document Metadata v0
Document Status: Provisional Reference（暂定参考）。用于指导近期实践，不代表冻结架构。
Document Created At: 2026-08-31T18:59:42+08:00
Document Updated At: 2026-09-01T17:15:05+08:00
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

> 状态：Provisional Reference（暂定参考）。用于指导近期实践，不代表冻结架构。

## 目标

人类可读层不是简单把 YAML 变成网页，而是逐步让人做到：看得到、看得懂、找得到、看懂关系、形成地图感、能够探索、能够理解方案空间，并最终辅助实际决策。

## 路线

1. **Visible（看得到）**
   - YAML 事实可以自动生成网页并通过 GitHub Pages 发布。
   - 已基本完成第一步。

2. **Readable（单个对象看得懂）**
   - 对象页不是字段转写，而是结构化知识页面。
   - 需要中文解释、信息层级、术语解释、来源/证据、标准族/版本等更友好的呈现。

3. **Navigable（找得到）**
   - 不依赖唯一目录树。
   - 通过能力、领域、系统层级、组织、标准族、开放程度、成熟度、时间、实现、场景等多种入口导航。
   - 与 Flat Objects + Dynamic Maps 原则保持一致。

4. **Connected（看懂关系）**
   - 对象页应展示相关能力、标准、实现、组织、替代关系、依赖关系、被谁使用、反向引用等。
   - 需要可信的 Reference Resolver、Graph / Backlink Index 支撑，而不应长期依赖 Renderer 临时扫描。

5. **Mappable（形成地图）**
   - 能够按某个能力、领域、系统层级或场景生成整体结构视图。
   - Map 是 View（视图），不是底层唯一真相。

6. **Explorable（可探索）**
   - 搜索、过滤、排序、标签、面包屑、快速跳转、相关对象、反向引用。
   - 可以从整张 Atlas 中切出一个子空间。

7. **Understandable（理解方案空间）**
   - 标准族指南、同类方案比较、组合方式、历史演化、典型架构、Scenario 解释。
   - 从“对象数据库”升级为“知识地图”。

8. **Actionable（可用于行动与决策）**
   - 用户可以从需求/场景出发，看到相关能力、候选标准、组合方案、实现、开放性、风险和缺口。
   - 与 Engine 的查询和分析结果结合。

## 近期三条相互驱动的主线

当前优先同时推进：

- **Readable**：把单个对象真正讲清楚；
- **Navigable**：建立多入口导航和基本结构感；
- **Connected**：让对象之间的关系可见、可点、可追踪。

这三者形成第一个真正的人类可读闭环：

```text
找到一个东西
     ↓
读懂它是什么
     ↓
看到它和谁有关
     ↓
沿关系进入下一个东西
     ↓
继续理解
```

## 与机器路线的关系

人类可读层不维护第二份事实。原则仍然是：

```text
Structured Source, Linked View

YAML / Canonical Facts
        ↓
      Engine
        ↓
Renderer / View Generator
        ↓
网页、列表、表格、地图、图形化视图
```

网页体验中暴露出来的结构缺口，应反向推动数据模型、关系模型、解释层和 Engine 能力演进。