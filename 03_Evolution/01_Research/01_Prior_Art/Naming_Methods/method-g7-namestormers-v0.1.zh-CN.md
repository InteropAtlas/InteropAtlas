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

## 对 Worker 拆分的直接含义

建议：

- Discover / Strategy Worker
- Lightning Generation Worker
- Prescreen Worker
- Pitch / Context Worker
- Feedback / Test Worker
- Refinement Worker
- Final Decision Worker

这一路线允许受控的信息回流：Feedback Worker 的输出可以进入 Refinement Worker；但不能把其他 arm 的结果回流进来。

## 公开证据边界

Public-confirmed：Discover / Strategy、Brainstorm / Lightning Round、Screen、Pitch、Fine Tune、Test、Final 的公开流程方向，以及较强 collaborative / feedback orientation。

Unknown / proprietary：内部具体评分表、stakeholder voting 权重、每轮生成规模与停止条件。

## Benchmark adaptation 注意

过去 G7 基本只执行了第一轮 generation 风格，没有真正把 pitch → feedback/test → refinement 跑起来，因此不能把之前的 G7 benchmark 当成对 NameStormers 完整流程的验证。后续隔离实验应至少加入一次真实 feedback/refinement 回路。