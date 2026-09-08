# G7 — NameStormers Method Profile v0.1

## 定位

外部专业机构方法。当前研究中最鲜明的特征是 collaborative iteration：不是一次性 solo generation，而是通过 Lightning Round、pitch/context、feedback/test 和 refinement 多轮推进。

## 可确认流程

```text
Discover / Strategy
   ↓
Brainstorm / Lightning Round
   ↓
Screen
   ↓
Pitch 10–20 names + rationale / tagline
   ↓
Feedback / Test
   ↓
Fine Tune / Refine
   ↺ 必要时继续循环
   ↓
Final / ROI / implementation
```

## 关键机制

1. Lightning Round：快速产生较宽候选集。
2. Screening：先进行基础筛查，再进入更重的 stakeholder interaction。
3. Pitch in context：名字不是裸字符串，而是附 rationale / tagline / positioning support 呈现。
4. Feedback / Testing：显式吸收 stakeholder learning。
5. Fine Tune：反馈会真正进入下一轮 refinement。

## 推荐隔离执行拓扑

建议 **7 个 method-specific isolated worker contexts**：

1. **G7-S1 Discover / Strategy Worker**
   - 输出冻结 strategy brief。
2. **G7-S2 Lightning Generation Worker**
   - 快速发散生成；只读取 S1。
3. **G7-S3 Prescreen Worker**
   - 基础现实筛查；不参与改名。
4. **G7-S4 Pitch / Context Worker**
   - 为通过基础筛查的候选形成 rationale / tagline / positioning support。
5. **G7-S5 Feedback / Test Worker**
   - 收集结构化 stakeholder feedback / test evidence，不直接生成替代名字。
6. **G7-S6 Refinement Worker**
   - 只接收冻结 strategy + 经 Orchestrator 压缩后的结构化 feedback，执行 fine tune / refinement。
   - 不读取其他 arm，也不读取 benchmark 排名。
7. **G7-S7 Final / Decision-support Worker**
   - 对 refined set 做最终 contextual decision support。

发生第二轮 refinement 时，优先启动新的 S6 context，并复用同一 task packet；不要在原对话中无限积累历史。这样既保留 NameStormers 的反馈回路，又控制上下文污染。

**Method stages：7 个公开阶段；建议独立方法上下文：7 / 基础 cycle。第三层 task packets：7，循环阶段复用 S5/S6 包。**

## 公开证据边界

Public-confirmed：Discover / Strategy、Brainstorm / Lightning Round、Screen、Pitch、Fine Tune、Test、Final 的公开流程方向，以及较强 collaborative / feedback orientation。

Unknown / proprietary：内部具体评分表、stakeholder voting 权重、每轮生成规模与停止条件。

## Benchmark adaptation 注意

过去 G7 基本只执行了第一轮 generation 风格，没有真正把 pitch → feedback/test → refinement 跑起来，因此不能把之前的 G7 benchmark 当成对 NameStormers 完整流程的验证。后续隔离实验应至少加入一次真实 feedback/refinement 回路。