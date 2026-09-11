# Naming Task Packets — 第三层执行文档索引

> 作用：这是 Naming Method Map（第一层）和各 Method Profile（第二层）之后的第三层执行文档入口。
>
> 每个 Task Packet 是一个可复用的“岗位说明书 / 执行任务包”，不是某一次聊天本身。一个 Packet 可以被多次实例化为不同的 Worker Session。

## 1. 目录与数量

| Arm | Method | 基础 Task Packets | 结构 |
|---|---|---:|---|
| G0 | IA Internal Baseline | 2 | 极简 baseline |
| G1 | Lexicon | 5 | Creative / Linguistic 双轨 |
| G2 | Catchword | 7 | 发散 → shortlist → 双路 prescreen → evaluation |
| G3 | Igor | 4 | positioning / competitive / white-space 前置 |
| G4 | River + Wolf | 5 | 4Cs + controlled iteration |
| G5 | Siegel+Gale | 8 | 四类并行 generation + blind evaluation + governance |
| G6 | Tungsten | 4 | Pivot → parent name → architecture test |
| G7 | NameStormers | 7 | pitch / feedback / refinement loop |
| G8 | IA C1.0 | 4 | Generator / Observer / Updater micro-cycle |

基础 method-specific Task Packets 合计：**46**。

G5 另有 `optional-testing.zh-CN.md`，不计入基础 46。

## 2. 共用执行文档

以下不放在本目录，而在 `../Execution/`：

- `worker-task-packet-schema-v0.1.zh-CN.md` — Task Packet 统一字段 / 最小知情规范；
- `shared-organization-vision-context-v0.1.zh-CN.md` — 需要知道组织愿景的 Worker 所用最小公共 Vision；
- `Shared_Evaluation/` — 5 个共用评估 Worker：Domain / Reality / Quality / Integrity / Owner Exposure。

共用评估包：**5**。

因此整个第三层基础执行模板为：

- 46 个 method-specific；
- 5 个 shared evaluation；
- 合计 **51**；
- 若启用 G5 independent testing，则为 **52**。

## 3. 使用原则

真正启动一个新对话框 / Agent Session 时，不把总地图全文塞给 Worker。Orchestrator 根据当前 Task Packet 组装“完成本任务所需的最小上下文”。

通常包含：

1. 当前 Task Packet；
2. 该任务确实需要时才加入 Shared Organization Vision；
3. 当前步骤必需的上游结构化产物。

默认不加入：

- 其他 arm；
- benchmark 成绩 / leaderboard；
- 历史 survivor / collision 统计；
- Owner 对具体历史候选的偏好；
- 下游筛选结果，除非原方法本身要求反馈回流。

## 4. Chat / Session 与 Packet 的关系

- Packet = 可复用岗位说明书；
- Session / Chat = 某一次实际执行实例。

因此不是固定 51 个聊天窗口。

例如：
- G5 四个 category Generator 是 4 个互相隔离的 Session；
- G8 只有 4 个 Packet，但 Generator / Observer / Updater 会被反复实例化；
- G4 / G7 若进入迭代，下一轮生成/细化必须开启新 Session，并只接收压缩后的结构化反馈。

## 5. 编排来源

总流程与数量以：

- `../naming-method-map-v0.1.zh-CN.md`
- `../naming-worker-conversation-plan-v0.1.zh-CN.md`

为上层编排依据。

本目录只负责第三层 method-specific execution packets。