# G3 — Igor Method Profile v0.1

## 定位

外部专业机构方法。当前最鲜明的差异是把 competitive naming landscape 放到 generation 之前，用命名 taxonomy 和 white-space 判断指导后续 name development。

## 可确认流程

```text
Positioning
   ↓
Competitive Analysis / Naming Taxonomy
   ↓
White-space / Engagement Direction
   ↓
Name Development
   ↓
Trademark / Prescreen
   ↓
Name + Tagline / Positioning Presentation
```

## 关键机制

1. Positioning：先明确这个名字“要做什么工作”。
2. Competitive Analysis：分析竞争者如何命名，识别过度拥挤的类别与差异化空间。
3. Taxonomy：Functional / Invented / Experiential / Evocative 等类型帮助理解命名空间。
4. Engagement：强调名字需要产生兴趣、故事和参与感，而不是只做功能描述。
5. Name Development：在定位和 white-space 基础上发展候选。
6. Trademark / Presentation：现实检查后，以 contextual story / tagline / positioning 支撑候选理解。

## 推荐隔离执行拓扑

建议 **4 个 method-specific isolated worker contexts**：

1. **G3-S1 Positioning / Competitive Strategy Worker**
   - 连续完成 Positioning → Competitive Analysis / Taxonomy → White-space / Engagement Direction。
   - 这些阶段本来就是同一战略链条，强拆会造成重复解释与交接损失。
   - 输出冻结的 positioning + competitive map + white-space direction。
2. **G3-S2 Name Development Worker**
   - 只读取 S1 的冻结输出发展候选。
   - 不读取其他 arm、历史 survivor、后续筛查结果。
3. **G3-S3 Trademark / Reality Prescreen Worker**
   - 对候选做独立现实筛查，不参与重新生成。
4. **G3-S4 Contextual Presentation Worker**
   - 对通过筛查的候选组织 rationale / tagline / positioning presentation。
   - 不因为 presentation 更好讲而回写生成规则。

**Method stages：6 个公开阶段；建议独立方法上下文：4。第三层 task packets：4。**

## 公开证据边界

Public-confirmed：Positioning、Competitive Analysis、Name Development、Trademark，以及 Functional / Invented / Experiential / Evocative taxonomy 与 engagement 导向。

Unknown / proprietary：竞争分析的完整内部模板、候选生成量、每轮淘汰阈值和客户审批流程。

## Benchmark adaptation 注意

过去 G3 已保留“competitive taxonomy → white-space → evocative / experiential generation”的核心，但把后续 presentation 等环节弱化。后续隔离测试应恢复完整的上下游，而不能把 G3 简化成“多生成短语名”。