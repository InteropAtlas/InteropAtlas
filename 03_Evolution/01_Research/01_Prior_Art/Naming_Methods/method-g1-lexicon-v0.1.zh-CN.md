# G1 — Lexicon Branding Method Profile v0.1

## 定位

外部专业机构方法。当前证据显示其核心不是简单“想词”，而是把 strategy、creative invention 与 linguistic engineering 结合。

## 可确认流程

```text
Define Winning / Diamond Questions
        ↓
Creative Framework
        ↓
┌───────────────────────┐
│ Creative Teams        │
│ Linguistic Engineering│
└──────────┬────────────┘
           ↓
Funnel / Selection
           ↓
Implement
```

Placek 后期公开表达可概括为 `Identify → Invent → Implement`。

## 关键机制

1. Diamond / Creative Framework：先定义怎样才算“赢”、已有优势、缺什么、必须表达什么。
2. Creative Teams：保持足够大的 creative window，不把目标写成过度僵硬 objective。
3. Linguistic Engineering：sound symbolism、letter structure、processing fluency 等参与生成与判断。
4. Funnel：创意与语言工程结果汇流，再进入选择。

## 推荐隔离执行拓扑

建议把公开流程转成 **5 个 method-specific isolated worker contexts**，其中第 2、3 个并行：

1. **G1-S1 Strategy / Creative Framework Worker**
   - 连续完成 Diamond Questions → Creative Framework；这两步属于同一战略建模上下文，不强拆。
   - 输出：冻结 Creative Framework。
2. **G1-S2 Creative Generation Worker**
   - 只读取 Creative Framework，负责 invention / candidate generation。
   - 不读取语言工程判断、筛选结果或其他 arm。
3. **G1-S3 Linguistic Engineering Worker**（与 S2 并行）
   - 读取同一 Creative Framework；从 sound symbolism、letter structure、processing fluency 等角度形成语言工程建议/评价。
   - 不读取 S2 的实时思考过程；可以在汇流阶段接收候选。
4. **G1-S4 Funnel / Selection Worker**
   - 接收 Creative candidates + Linguistic Engineering 输出，进行汇流与选择。
5. **G1-S5 Implementation / Decision-support Worker**
   - 对入选名称做 contextual implementation 支撑；不反向修改前面的生成规则。

这里最重要的是 **S2 与 S3 不能合并成一个长上下文**，否则 Lexicon 最有辨识度的 creative / linguistic 双轨结构会被压平。

**Method stages：5（其中 Strategy 内含 Diamond→Framework，Creative/Linguistic 并行）。建议独立方法上下文：5。第三层 task packets：5。**

## 公开证据边界

Public-confirmed：Diamond Questions、Creative Framework、Creative Teams + Linguistic Engineering、Identify/Invent/Implement、语言工程方向。

Unknown / proprietary：Lexicon 内部每轮候选数量、具体 team 分工、内部淘汰阈值、客户项目中的完整 SOP。后续 benchmark 不应自行补造这些细节。

## Benchmark adaptation 注意

G1 benchmark 过去把方法压缩成单阶段 generation arm；后续隔离测试应恢复至少“Framework → Creative / Linguistic 并行 → Funnel”的结构，而不是继续只给一个 Generator 一段方法提示。