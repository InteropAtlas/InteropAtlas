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

## 推荐隔离执行拓扑

建议 **8 个 method-specific isolated worker contexts**：

1. **G5-S1 Strategy / Simplicity Worker**
   - 输出冻结的 naming strategy 与 simplicity intent。
2. **G5-S2 Category Strategy Worker**
   - 明确各 category 的边界与任务，不生成具体名字。
3. **G5-S3A Descriptive Generator**
4. **G5-S3B Suggestive Generator**
5. **G5-S3C Coined Generator**
6. **G5-S3D Edgy / Unconventional Generator**
   - 四个 Generator 平行、互不可见，只共享 S1/S2 的冻结输入。
7. **G5-S4 Contextual Evaluation Worker**
   - 将四路候选放回一致的品牌语境评价；不知道候选来自哪个 category 时优先盲评。
8. **G5-S5 Governance / Decision Worker**
   - 综合 evaluation 与必要 testing；明确避免简单多数投票代替判断。

Optional Testing 可以作为 S5 的外部输入，也可以在需要严谨测试时另开独立 Tester；但它不是所有项目必需，因此不计入基础上下文数。

这里最重要的实验设计是：**四种 naming category 必须真正分成四个干净生成上下文**。过去把它们塞给同一个 Generator，会把“多类别探索”污染成一个混合风格。

**Method stages：5 个主阶段，其中 generation 含 4 个平行分支。建议独立方法上下文：8（基础）；可选 testing +1。第三层 task packets：8 个基础包 + 1 个 optional testing 包。**

## 公开证据边界

Public-confirmed：Simplicity 主张、多 naming categories、命名评价研究、对 consensus / voting 的警惕。

Unknown / proprietary：真实项目中每个 category 的数量、生成团队结构、最终审批制度细节。

## Benchmark adaptation 注意

过去 G5 把“anti-consensus + 多类别”压成一次生成，导致 `Common Strange / One Else` 一类反常规形式占比变高。后续应真正分 category 并行生成，再进行盲式 contextual evaluation，而不是把“edgy”理解成总体风格。