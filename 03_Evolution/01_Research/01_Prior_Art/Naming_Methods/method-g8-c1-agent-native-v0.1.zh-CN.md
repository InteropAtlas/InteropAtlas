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

## 推荐隔离执行拓扑

G8 不能被拆成普通 `Generator → 20 names → Screener`。建议 **4 个长期角色 / isolated context types**，按 micro-cycle 重复使用：

1. **G8-S1 Region Strategy Worker**
   - 输入：组织愿景、当前 arm 的允许状态摘要。
   - 输出：当前 naming region + collision prior assumptions。
2. **G8-S2 Micro-cycle Generator**
   - 每次只接收当前 region state 和必要生成约束，产出 1–3 个 formal proposals。
   - 不直接搜索现实身份。
3. **G8-S3 Reality Observer**
   - 对刚提出的 formal proposals 做 multi-surface search / domain observation；只报告证据与置信度。
   - 不生成替代名。
4. **G8-S4 State Updater / Local Orchestrator**
   - 读取 proposal + observation，更新 failure topology、region state、explore/exploit 决策。
   - 给下一次 S2 只传递压缩后的局部状态，而不是完整历史。

循环为：`S1（首次/换区时） → S2 → S3 → S4 → S2 ↔ S3 ↔ S4 ...`。如果 S4 决定换区，再回到新的 S1 context。

这 4 个角色必须相互区分：Generator 不做搜索，Observer 不生成，Updater 不直接创造名字。这样才能避免一个长上下文同时承担“想名字、找证据、学会规避”后发生安全词根坍缩。

**Method stages：6 个逻辑阶段；建议独立 context types：4。第三层 task packets：4；运行时会多次实例化 S2/S3/S4，而不是新增文档。**

## 证据边界

这是 IA 自有实验方法。其有效性需要由 benchmark 证明，不能因为可行率高就直接宣称质量更高。

## Benchmark adaptation 注意

此前 G8 已按“每一个 proposal 先持久化、再搜索、再回写 observation、然后生成下一个”的方式执行，这是目前最接近该方法原意的一条路线。后续重点不是继续加更多搜索，而是防止它坍缩成“不断复用容易过 `.org` 的安全词根”。