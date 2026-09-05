# 扁平图谱与动态 Map 方法 — Early Architecture Principle

> Lifecycle: **Historical / Absorbed into V1 Core Architecture**
>
> Original Role: Pre-Alpha 数据建模原则。
>
> Successors: `docs/architecture.zh-CN.md` + `docs/repository-structure-profile.zh-CN.md` + Workspace / Graph projections.
>
> Current Role: 保存 `Flat Objects + Rich Relations + Dynamic Maps` 形成过程；当前有效原则已由 V1 Core Architecture 与 Repository Structure Profile 承接。

## Historical principle

> **Flat Objects（扁平对象） + Rich Relations（丰富关系） + Dynamic Maps（动态地图）**

早期设计明确反对用单一深层、唯一、固定分类树组织全部知识。标准、协议、能力、组织、实现、场景和缺口往往同时属于多个领域和语境；如果物理目录承担唯一分类，就会把导航选择错误地提升为事实。

因此当时提出：

- 底层保存稳定对象和明确关系；
- 同一对象只有一个稳定身份，但可以出现在多张 Map；
- Map 可以人工定义、规则生成或动态计算；
- Map 是 View，不是第二事实源；
- Graph / Index / Query 应承担分类、连接和导航，而不是复制对象文件。

## Absorption into current architecture

这些原则现已进入更正式的架构不变量：

- Physical Storage ≠ Semantic Classification ≠ View；
- Relation 是一等知识资产；
- Generated / Derived View 不成为第二事实源；
- stable identity 不依赖物理路径；
- Workspace / Projection 可以产生 Graph / Ecosystem 等动态视图。

因此本文不再需要作为 `docs/` 中独立的 Living Architecture Principle，但保留其设计来源和早期表达。
