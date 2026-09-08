# G6 — Tungsten Branding Method Profile v0.1

## 定位

外部专业机构方法。核心差异是先找到长期稳定的 Pivot Point，再围绕它建立可扩展母品牌与命名架构。

## 可确认流程

```text
Identify enduring Pivot Point
   ↓
Define evergreen umbrella concept
   ↓
Develop parent / corporate name
   ↓
Test brand architecture extensibility
   ├─ masterbrand
   ├─ sub-brand
   ├─ offering / product family
   └─ future acquisitions / extensions
   ↓
Select / implement
```

## 关键机制

1. Pivot Point：寻找企业长期不会轻易变化的核心属性 / enduring principle / value proposition。
2. Evergreen naming：不被当前单一产品或短期业务限制。
3. Brand Architecture：名称必须能支撑未来产品族、子品牌和扩张。
4. Parent-name system：部分公开案例体现 parent name + 可扩展命名家族的思路。

## 推荐隔离执行拓扑

建议 **4 个 method-specific isolated worker contexts**：

1. **G6-S1 Pivot / Evergreen Strategy Worker**
   - 连续完成 enduring Pivot Point → evergreen umbrella concept。
   - 输出冻结的长期核心与 architecture assumptions。
2. **G6-S2 Parent Name Development Worker**
   - 只读取 S1 的冻结输出生成 parent / corporate name candidates。
   - 不读取 architecture stress-test 结果或其他 arm。
3. **G6-S3 Architecture Stress-test Worker**
   - 对候选分别测试 masterbrand / sub-brand / product family / future extension 承载能力。
   - 只测试，不重新发明名字。
4. **G6-S4 Selection / Implementation Worker**
   - 综合候选与 architecture 结果进行选择和 contextual implementation。

如果 architecture stress-test 暴露结构性问题，应由 Orchestrator 决定是否开启新一轮 S2；不要让 S3 直接替 Generator 修名字。

**Method stages：5 个公开阶段；建议独立方法上下文：4（Pivot+Evergreen 合并）。第三层 task packets：4。**

## 公开证据边界

Public-confirmed：Pivot Point、长期核心、Brand Architecture 连续性、parent/sub-brand extensibility 方向及若干公开案例。

Unknown / proprietary：完整内部 workshop、架构评分方法、候选数量及客户审批 SOP。

## Benchmark adaptation 注意

过去 G6 主要保留了 Pivot Point + `[Name] Research / Commons / Tools` architecture probe，这一核心方向是合理的；但后续应把 Pivot 定义与 Name Development 分开，使 Generator 只收到已冻结的 enduring concept，而不是整个 benchmark 历史。