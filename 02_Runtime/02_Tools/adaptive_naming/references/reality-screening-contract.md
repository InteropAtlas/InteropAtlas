# Reality Screening Contract v0.3.3

本文件定义 Adaptive Naming Controller 的**现实身份初筛合同**。它不是正式商标法律意见，也不能替代律师 / 官方数据库的最终 clearance；目标是在候选进入 `promising / finalist / Owner Exposure` 前，降低容易避免的现实身份漏检。

核心原则：

> **一次搜索没有看到结果，不等于“无冲突”。`no_material_collision_found` 必须来自一组可审计的查询，而不是单个 query 的空结果。**

同时保持：

> **Reality 只更新 feasibility；不得因为名字现实被占，就反向篡改 intrinsic quality。**

---

## 1. 什么时候执行

- 普通 exploration：只对通过 intrinsic quality + value alignment 的 top slice 做现实初筛；不要给所有 working-pool 候选做昂贵搜索。
- `held / promising`：必须已有至少一次完整的 Level-1 screen。
- `finalist / Owner Exposure`：必须在暴露前重新执行 freshness recheck；旧结果不能自动沿用。
- Transformation Rescue 结果：每个新变体都作为新候选重新筛。

Domain availability 只能在 identity screen 已足以支持继续推进后检查；域名可用不能修复 identity collision。

---

## 2. Level-1：最低 exact-identity 查询集

对一个候选 `NAME`，至少执行并记录以下查询意图。具体搜索引擎语法可按 runtime 调整，但信息目标不能省略：

1. **bare exact**：`"NAME"`
2. **organization / company**：`"NAME" company organization`
3. **software / product / project**：`"NAME" software app product project`
4. **research / education / nonprofit**：当 Naming Job 可能落入这些领域时，查询 `"NAME" research education foundation nonprofit` 等高邻接类别
5. **trademark-oriented public signal**：`"NAME" trademark` / `"NAME" registered trademark`，用于发现显眼的公开注册记录或争议；这仍不是正式 clearance

若搜索服务支持 freshness，应至少有一条查询覆盖当前 / 近期网络结果，同时保留一条不限制时间的查询以发现历史身份。

### 最低通过条件

只有在：

- 上述意图已覆盖；
- 没有发现 material exact identity；
- 结果不是明显因为工具 error / indexing gap / query malformed 而缺失；

才允许写 `no_material_exact_collision_found_current_screen`。

不要写绝对的 `clear / available / no collision exists`。

---

## 3. Level-2：近似身份 / 邻接风险

当候选准备从 working pool 升到 `promising`，或 exact screen 通过但名称明显接近已有身份时，补：

- 一字母 / 一音节近似；
- 常见拼写恢复分支；
- 同音 / 近音；
- 去空格 / 加空格 / 连字符变体；
- 与构词 seed 或现实高邻接名称的近似；
- 目标行业 / research / software / public-knowledge 邻接类别中的 near identity。

若 active near identity 与 Naming Job 高邻接，即使没有 exact identity，也可判 `red / material-near-collision`。

不要用低失真字母变形规避一个本质上仍然高度近似的现实身份。

---

## 4. Trademark-oriented public screen 与正式 clearance 分开

`trademark-oriented public screen` 只用于发现明显信号，例如：

- 搜索结果直接出现 active / registered word mark；
- 官方或可信数据库显示相关类别注册；
- 公开诉讼 / opposition / confusion history；
- 同名主体已经在高度邻接业务中持续使用。

它只能产生：

- `material_public_tm_signal`
- `no_material_public_tm_signal_found_in_current_screen`
- `unknown`

不得产生“法律上可注册 / 可安全使用”的结论。

正式商标 clearance 仍按任务政策单独处理。

---

## 5. Domain 的位置

顺序默认：

`intrinsic/value pass → identity screen → public TM signal screen → domain gate → finalist freshness recheck → formal clearance（若任务需要）`

若任务有特殊成本结构可调整，但不得把 domain availability 当作 identity evidence。

Domain 查询继续调用 IA 的 Domain Availability Verification Method；`unknown / error` 不得变成 available。

---

## 6. Freshness 与重复筛查

现实空间会变化。至少记录：

```yaml
reality_screen:
  level: 1 | 2
  observed_at: null
  query_intents: []
  sources: []
  exact_result: null
  near_result: null
  public_tm_signal: null
  confidence: low | medium | high
  recheck_before_owner_exposure: true
```

出现以下情况必须 recheck：

- 候选从 held/promising 升 finalist；
- Owner Exposure 前；
- 搜索结果较旧或候选搁置后恢复；
- 新证据与旧结论矛盾；
- 域名结果很好但 identity evidence 很薄；
- 之前只跑过单 query / 单来源。

---

## 7. Reality false negative 诊断

如果一个候选先前被记录为 `no_material_collision_found`，随后用简单 exact/category/trademark 查询就发现活跃 exact identity、相关类别注册商标或明显高邻接 near identity，诊断：

`reality_screen_false_negative`

下一步：

1. 立即撤回旧 feasibility 结论；
2. 保留旧结论作为历史证据，不假装没发生；
3. 检查同批 surviving candidates 是否使用了同样薄弱的 query contract；
4. 批量 recheck 同批 survivors；
5. 若是方法缺口而非一次工具故障，更新 Skill / regression；
6. 不因此降低候选 intrinsic quality，除非新现实证据同时揭示名称本体问题。

---

## 8. Stop rule

Reality screening 的目标不是穷尽互联网。

当 Level-1/2 已覆盖任务相关意图，并且继续搜索的边际信息价值低时停止；记录 `current_screen` 和 uncertainty。若发现一个足以淘汰的 material collision，也可立即停止该候选剩余昂贵检查。
