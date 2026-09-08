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

## 对 Worker 拆分的直接含义

至少存在天然的并行可能：

- Strategy / Creative Framework Worker
- Creative Generation Worker
- Linguistic Engineering Worker
- Funnel / Selection Worker
- Implementation Worker

其中 Creative Generation 与 Linguistic Engineering 不宜默认放在同一对话上下文，否则会把原有并行机制压扁。

## 公开证据边界

Public-confirmed：Diamond Questions、Creative Framework、Creative Teams + Linguistic Engineering、Identify/Invent/Implement、语言工程方向。

Unknown / proprietary：Lexicon 内部每轮候选数量、具体 team 分工、内部淘汰阈值、客户项目中的完整 SOP。后续 benchmark 不应自行补造这些细节。

## Benchmark adaptation 注意

G1 benchmark 过去把方法压缩成单阶段 generation arm；后续隔离测试应恢复至少“Framework → Creative / Linguistic 并行 → Funnel”的结构，而不是继续只给一个 Generator 一段方法提示。