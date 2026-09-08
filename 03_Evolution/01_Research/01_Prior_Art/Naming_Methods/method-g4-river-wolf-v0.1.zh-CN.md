# G4 — River + Wolf Method Profile v0.1

## 定位

外部专业机构方法。核心差异是用 4Cs 把命名任务参数化，再进入开发与筛选。

## 可确认流程

```text
Research / Prepare
   ↓
4Cs Parameters
   ├─ Character
   ├─ Communication
   ├─ Construction
   └─ Continuum
   ↓
Develop
   ↓
Shortlist
   ↓
Screen
   ↺ 必要时迭代
```

## 关键机制

- Character：品牌人格与气质。
- Communication：名字需要传达或暗示什么。
- Construction：允许使用哪些构词方式。
- Continuum：在 descriptive ↔ suggestive ↔ abstract 等连续谱上定位。
- 参数变化会显著改变输出风格，因此该方法天然 client-parameter responsive。

## 推荐隔离执行拓扑

建议 **5 个 method-specific isolated worker contexts**：

1. **G4-S1 Research / Preparation Worker**
   - 只负责理解组织、受众、命名对象和约束，输出准备材料。
2. **G4-S2 4Cs Parameter Worker**
   - 基于 S1 形成并冻结 Character / Communication / Construction / Continuum。
   - 4Cs 一旦进入正式生成，不因候选好坏临时改写。
3. **G4-S3 Development Worker**
   - 只读取冻结 4Cs，负责候选开发。
   - 不读取其他 arm 或筛选反馈。
4. **G4-S4 Shortlist Worker**
   - 根据 4Cs 与命名目标对候选收敛；不做现实搜索。
5. **G4-S5 Screening / Iteration Coordinator**
   - 完成现实筛查；只有在方法本身需要回流时，才形成结构化 iteration brief 给新一轮 S2/S3。
   - 回流内容必须是方法内反馈，不得包含其他 arm 成绩或词根统计。

如果发生迭代，原则上开启新的 Development context，而不是让原 Generator 在长上下文中无限累积历史。

**Method stages：5 个主阶段（Screen 后可循环）；建议独立方法上下文：5 / cycle。第三层 task packets：5 个基础包，迭代复用同一包而不是新增文件。**

## 公开证据边界

Public-confirmed：4Cs、Develop / Shortlist / Screen 的基本结构及案例中明显的参数响应性。

Unknown / proprietary：4Cs 在真实项目中的权重、客户协作频次、迭代停止条件和内部评审表。

## Benchmark adaptation 注意

过去 G4 的 frozen 4Cs 本身较接近原方法，但同一长上下文导致词根收缩和 exact repeat。后续测试必须把 4Cs 参数文档与 Development Worker 隔离于其他 arm 历史。