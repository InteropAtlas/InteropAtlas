# G8 — IA C1.0 Agent-native Naming Method Profile v0.1

## 定位

IA 自己的 Agent-native synthesis。它不是某家外部机构的方法，而是为 Agent 条件下的高碰撞命名空间设计的 clearance-aware / search-guided 流程。

## 当前流程

```text
Select naming region
   ↓
Estimate collision prior
   ↓
Freeze Region Brief
   ↓
Generate locally
   ↓
Immediate reality observation / search
   ↓
Update arm-local region state
   ↓
Exploit or move
   ↺ repeat through a new Region Strategy context
```

最终再进入统一 feasibility / quality / Owner gates。

## 核心机制

1. Region-first：先选择局部命名空间，不在整个语义空间随机游走。
2. Collision Prior：生成前由 Region Strategy 估计区域拥挤程度；Generator 只接收冻结后的 region guidance，不接收原始筛选结果。
3. Multi-surface reality model：公司、产品、项目、GitHub、人物、历史、词汇、域名等都可能构成现实占用。
4. Observation Confidence：搜索结果不是绝对真值，需要记录置信度。
5. Failure-topology feedback：失败不是只淘汰单个名字，而是更新 G8 arm-local 对该区域的认识；该信息先进入 State Updater / Region Strategy，不直接暴露给 Generator。
6. Exploration / Exploitation：在继续深挖与换区之间做受控选择。

## 推荐隔离执行拓扑

G8 不能被拆成普通 `Generator → 20 names → Screener`。建议 **4 个长期角色 / isolated context types**，按 micro-cycle 重复使用：

1. **G8-S1 Region Strategy Worker**
   - 输入：组织愿景、当前 G8 arm-local internal compressed state。
   - 输出：冻结 Region Brief，包含当前 naming region、construction boundaries、collision-prior assumption 与 move/stay 条件。
   - 不生成正式候选；输出不得携带具体 survivor / Red / Yellow、domain / registry、collision identity、失败候选清单或“安全词根 / 后缀”。
2. **G8-S2 Micro-cycle Generator**
   - 每次只接收冻结 Region Brief、Naming Job constraints 与不含筛选结果的运行元数据，产出 1–3 个 formal proposals。
   - 不直接搜索现实身份，也不读取 Observation Record / survivor / feasibility state。
3. **G8-S3 Reality Observer**
   - 对刚提出的 formal proposals 做 multi-surface search / domain observation；只报告证据与置信度。
   - 不生成替代名。
4. **G8-S4 State Updater / Local Orchestrator**
   - 读取 proposal + observation，更新 failure topology、arm-local region state、explore/exploit 决策。
   - internal state 只交给新的 S1 / 后续 Updater；不得直接交给 S2。

循环为：`S1 → S2 → S3 → S4 → new S1 → new S2 → ...`。S4 可以决定继续当前区域、调整边界或换区，但都必须先经过新的 S1，把 reality-derived state 压缩成新的冻结 Region Brief，再进入新的 Generator Session。

这 4 个角色必须相互区分：Generator 不做搜索，Observer 不生成，Updater 不直接创造名字，Region Strategy 负责把 reality-derived arm-local state 转换成不泄露候选级 feasibility 结果的区域策略。这样既保留 search-guided / failure-topology feedback，又避免一个生成上下文直接学到 survivor 模板后发生安全词根坍缩。

**Method stages：6 个逻辑阶段；建议独立 context types：4。第三层 task packets：4；运行时会多次实例化 S1/S2/S3/S4，而不是新增文档。**

## 证据边界

这是 IA 自有实验方法。其有效性需要由 benchmark 证明，不能因为可行率高就直接宣称质量更高。

## Benchmark adaptation 注意

此前 G8 已按“每一个 proposal 先持久化、再搜索、再回写 observation、然后生成下一个”的方式执行，这是 shared-context 历史 benchmark 中最接近该方法原意的一条路线，但其生成与筛选反馈仍可能因共享上下文发生污染。

后续 isolated benchmark 的关键不是继续增加搜索，而是把 search feedback 限定在 `Observer → Updater → Region Strategy`，只把冻结 Region Brief 交给新的 Generator，从机制上避免直接学习 `.org` survivor、Red/Yellow 或具体 collision 结果并坍缩成“安全词根”模板。