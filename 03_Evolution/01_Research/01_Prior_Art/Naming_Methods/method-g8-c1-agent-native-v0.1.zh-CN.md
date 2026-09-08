# G8 — IA C1.0 Agent-native Naming Method Profile v0.1

## 定位

IA 自己的 Agent-native synthesis。它不是某家外部机构的方法，而是为 Agent 条件下的高碰撞命名空间设计的 clearance-aware / search-guided 流程。

## 当前流程

```text
Select naming region
   ↓
Estimate collision prior
   ↓
Generate locally
   ↓
Immediate reality observation / search
   ↓
Update region state
   ↓
Exploit or move
   ↺ repeat
```

最终再进入统一 feasibility / quality / Owner gates。

## 核心机制

1. Region-first：先选择局部命名空间，不在整个语义空间随机游走。
2. Collision Prior：生成前估计区域拥挤程度。
3. Multi-surface reality model：公司、产品、项目、GitHub、人物、历史、词汇、域名等都可能构成现实占用。
4. Observation Confidence：搜索结果不是绝对真值，需要记录置信度。
5. Failure-topology feedback：失败不是只淘汰单个名字，而是更新对该区域的认识。
6. Exploration / Exploitation：在继续深挖与换区之间做受控选择。

## 对 Worker 拆分的直接含义

G8 不能被简单拆成“Generator → 20 个名字 → Screener”。搜索反馈本身就是 generation mechanism。

合理结构更像：

- Region Strategy Worker
- Micro-cycle Generator
- Reality Observer
- State Updater / Orchestrator
- 然后重复 Generator ↔ Observer ↔ Updater

为了隔离上下文，Generator 可以只收到当前 region state，而不必知道完整 benchmark；Observer 只负责现实搜索；Updater 掌握该 arm 的局部历史。

## 证据边界

这是 IA 自有实验方法。其有效性需要由 benchmark 证明，不能因为可行率高就直接宣称质量更高。

## Benchmark adaptation 注意

此前 G8 已按“每一个 proposal 先持久化、再搜索、再回写 observation、然后生成下一个”的方式执行，这是目前最接近该方法原意的一条路线。后续重点不是继续加更多搜索，而是防止它坍缩成“不断复用容易过 `.org` 的安全词根”。