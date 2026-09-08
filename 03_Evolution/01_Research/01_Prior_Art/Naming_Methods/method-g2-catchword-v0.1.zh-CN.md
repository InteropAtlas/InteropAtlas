# G2 — Catchword Method Profile v0.1

## 定位

外部专业机构方法。当前公开证据最鲜明的特征是：先做 Discovery / Naming Parameters，再进行高容量发散生成，之后统一 shortlist 与 screening，而不是生成一个就判断一个。

## 可确认流程

```text
Discovery
   ↓
Naming Parameters / Creative Brief
   ↓
Project Vocabulary / Naming Territories
   ↓
High-volume Divergent Generation
   ↓
Internal Shortlist against Brief
   ↓
Trademark / Domain / Search Prescreen
   ↓
Linguistic / Cultural Screening（按项目需要）
   ↓
Contextual Evaluation / Decision
```

## 关键机制

1. Discovery：先理解业务、受众、定位和命名目标。
2. Naming Parameters：把目标转成可执行 creative brief。
3. Project Vocabulary：扩展词汇、词根、翻译、前后缀、复合、拼合和蓝海联想。
4. High-volume Generation：大量发散，避免过早依恋单个名字。
5. Shortlist：依据 brief / brand potential，而不是即时喜好。
6. Preliminary Screening：商标、域名、搜索、社交等现实检查。
7. Linguistic / Cultural Screening：目标市场语言与文化风险检查。

## 推荐隔离执行拓扑

建议 **7 个 method-specific isolated worker contexts**：

1. **G2-S1 Discovery + Brief Worker**
   - Discovery 与 Naming Parameters / Creative Brief 连续完成；二者高度依赖，不为隔离而隔离。
   - 输出冻结 brief。
2. **G2-S2 Vocabulary / Territory Worker**
   - 只基于 brief 扩展 project vocabulary、roots、territories、construction space。
3. **G2-S3 Divergent Generation Worker**
   - 只读取冻结 brief + vocabulary/territories；高容量发散。
   - 禁止读取后续 collision / domain / shortlist 结果。
4. **G2-S4 Internal Shortlist Worker**
   - 按 brief / brand potential 收敛，不做现实搜索。
5. **G2-S5 Reality Prescreen Worker**
   - trademark / domain / search / social 等现实可行性检查。
   - 只筛选，不改造候选。
6. **G2-S6 Linguistic / Cultural Worker**
   - 按目标市场需要进行独立语言文化检查；可与 S5 并行。
7. **G2-S7 Contextual Evaluation / Decision-support Worker**
   - 汇总 shortlist 与筛查结果，做 contextual evaluation。

关键隔离是 **S3 Generator 与 S5/S6 Screening**；Catchword 的方法特征要求“先发散、后统一筛”。

**Method stages：8 个公开阶段；建议独立方法上下文：7（Discovery+Brief 合并，Reality/Linguistic 可并行）。第三层 task packets：7。**

## 公开证据边界

Public-confirmed：Discovery、Naming Parameters / Creative Brief、高容量生成、shortlist、preliminary trademark/domain/social screening、linguistic & cultural screening。

Unknown / proprietary：内部具体批次数、团队规模、每个 funnel 阶段阈值、客户协作细节。

## Benchmark adaptation 注意

过去 G2 只保留了“高覆盖发散生成”的核心片段。后续完整隔离测试至少应恢复 `Discovery/Brief → Vocabulary → Generation → Shortlist → Screening` 的顺序，且不能把 G8 的搜索反馈提前注入生成。