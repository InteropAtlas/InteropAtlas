# G0 — IA Internal Baseline Method Profile v0.1

## 定位

IA 自己的内部 baseline，不是外部机构方法。它用于回答：在不引入某家专业 agency 框架时，仅根据 Organization philosophy / semantic space，模型会如何命名。

## 当前流程

```text
Organization philosophy / vision
   ↓
Semantic space
   ↓
Familiar-but-New / pronounceability / symbolic compressibility
   ↓
Construction choice
   ├─ existing word
   ├─ compound
   ├─ blend
   └─ root-derived / coined form
   ↓
Generate candidates
```

## 核心语义

`Commons → Perspective → Creation → Commons ↺`

以及 Flow / Transformation / Boundary / Known↔Unknown 等辅助语义。

## 对 Worker 拆分的直接含义

为了保持 baseline 简洁，后续不应人为给 G0 增加外部机构没有的复杂流程。合理拆分最多是：

- Vision / Semantic-space preparation
- Baseline Generator
- 独立 downstream screener / reviewer

Generator 不应看到 collision statistics 或其他 arm 输出。

## 推荐隔离执行拓扑

方法步骤按 2 个执行阶段处理，建议 **2 个 method-specific isolated worker contexts**：

1. **G0-S1 Vision / Semantic-space Worker**
   - 输入：组织愿景、使命、命名对象边界。
   - 输出：冻结的 semantic space 与基本生成原则。
   - 不看：历史候选、其他 arm、筛选结果。
2. **G0-S2 Baseline Generator**
   - 输入：S1 的冻结输出。
   - 输出：rationale-bearing candidates。
   - 不看：collision / domain / quality / Owner 结果。

后续 Reality / Domain / Quality / Owner 等属于 benchmark 共用的下游评估层，不算 G0 方法自身步骤，也不应把这些信息反馈给 Generator。

**Method steps：2。建议独立方法上下文：2。第三层 task packets：2。**

## 证据边界

这是 IA 自有方法，因此不存在“外部公开证据不足”的问题；但必须区分历史 Owner 偏好与正式方法规则。Owner 曾喜欢某些候选，只能作为偏好信号，不能变成构词模板。

## Benchmark adaptation 注意

G0 的价值正是作为低干预 baseline。后续隔离测试应保持它比 G1–G7 更少的方法输入，否则会失去对照意义。