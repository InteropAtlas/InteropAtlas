# G5 — Siegel+Gale Method Profile v0.1

## 定位

外部专业机构方法。当前研究里最鲜明的差异不是某个固定构词技巧，而是 Simplicity、不同 naming category 的并行探索，以及对 voting / consensus 的警惕。

## 可确认流程

```text
Simplicity / Strategy framing
   ↓
Parallel naming-category exploration
   ├─ Descriptive
   ├─ Suggestive
   ├─ Coined
   └─ Edgy / unconventional
   ↓
Contextual Evaluation
   ↓
Selection / Governance
   ↓
Testing（按项目需要）
```

## 关键机制

1. Simplicity：名称与更大的品牌表达应清楚、容易理解和使用。
2. Category exploration：不把所有候选都塞进同一种命名风格。
3. Evaluation attributes：unique、attention-getting、motivational、appropriate、memorable、fits-me 等维度曾用于其命名研究。
4. Preference ≠ naming quality：简单投票或多数偏好不应自动决定结果。
5. Governance：选择过程本身是方法的一部分。

## 对 Worker 拆分的直接含义

建议：

- Strategy / Simplicity Worker
- Category Strategy Worker
- 多个平行 Generation Worker（按 category）
- Contextual Evaluation Worker
- Governance / Decision Worker
- Optional Testing Worker

如果所有 category 都交给同一个长上下文 Generator，很容易再次收敛成相似词根，因此这一方法尤其适合并行隔离。

## 公开证据边界

Public-confirmed：Simplicity 主张、多 naming categories、命名评价研究、对 consensus / voting 的警惕。

Unknown / proprietary：真实项目中每个 category 的数量、生成团队结构、最终审批制度细节。

## Benchmark adaptation 注意

过去 G5 把“anti-consensus + 多类别”压成一次生成，导致 `Common Strange / One Else` 一类反常规形式占比变高。后续应真正分 category 并行生成，再进行盲式 contextual evaluation，而不是把“edgy”理解成总体风格。