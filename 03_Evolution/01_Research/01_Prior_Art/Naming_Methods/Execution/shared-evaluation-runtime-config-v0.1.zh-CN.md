# Shared Evaluation Runtime Config v0.1

> 状态：dry-run freeze candidate
>
> 作用：为 Naming Benchmark 的共享评估 E1 / E2 / E3 提供可重复实例化的统一运行配置。它不是新的 Naming Method，也不是第四层文档；它属于 `Execution/` 下的 shared evaluation configuration。
>
> 适用对象：当前 InteropAtlas umbrella-organization Naming Job。若 Naming Job 的 hard constraints 改变，必须升版本并记录原因。

## 1. 全局原则

共享评估从同一个冻结的 benchmark-eligible proposal denominator 独立 fan-out：

```text
Frozen proposals
   ├── E1 Domain / Registry
   ├── E2 Reality Identity / Collision
   └── E3 Quality / Pareto
```

执行要求：

- E1 / E2 / E3 使用同一冻结 proposal denominator；
- E1 / E2 与 E3 互相不知道结果；
- E3 不得按 feasibility survivor 过滤、排序或标注；
- method-specific keep / hold / drop 不改变 E1 / E2 / E3 的 generation denominator；
- blind Worker 只看到 run-local opaque candidate IDs，不看到 arm / method / canonical candidate IDs / packet path / source provenance；
- canonical ID 映射由 Orchestrator 在 Session 外维护；
- 查询失败或证据不足必须显式记为 `unknown` / `error`，不得自动推断为通过；
- 本配置提供 benchmark screening / comparison 规则，不构成最终法律 clearance。

## 2. 当前 Naming Job 的冻结动态约束

依据 #409 当前 Naming Job contract：

- naming target：InteropAtlas 上层长期 umbrella organization；
- required domain namespace：`.org`；
- domain matching rule：**exact normalized `.org` 必须可注册，是 hard gate**；
- `get-` / `use-` / 连字符 / 其他前后缀变体不满足该 exact hard gate；
- reality identity / serious-confusion review 是独立 feasibility evidence；
- trademark-oriented evidence 只作为现实冲突证据，不等于正式法律检索或法律意见；
- 当前 shared evaluation 不把社交账号、包管理器 namespace 或 app-store handle 设为 hard gate；
- pronunciation / spelling / semantic quality 进入 E3，不偷换为 E1/E2 的硬注册判定。

## 3. E1 — Domain / Registry Runtime Config

### 3.1 Normalization

对 display name 执行以下固定 normalization：

1. Unicode NFKC；
2. 去除首尾空白；
3. 转小写；
4. 仅在名称本身含空格时移除空格以形成 exact domain label；
5. 不主动删除或替换名称中的其他字符来“修复”候选；
6. 若 normalized label 不符合 DNS / `.org` 可注册字符串规则，则记录 `invalid-label`，视为 hard-gate failure；
7. 查询目标固定为 `<normalized_name>.org`。

本 Job 不允许通过加 `get` / `use` / `the` / 连字符 / 数字等方式绕过 exact-name hard gate。

### 3.2 Query protocol

E1 必须针对 exact normalized `.org` 使用可公开复核的 registry / registrar / RDAP 类信号进行 observation。

优先级：

1. `.org` / RDAP / registry authoritative machine-readable status；
2. 若 authoritative endpoint 暂时不可用，可记录 registrar availability signal 作为辅助，但不得把单一营销页面当成最终权威；
3. 任何查询都必须记录 observed_at 与 source / endpoint。

### 3.3 Observation values

允许值：

- `available`：机器信号明确支持当前 exact normalized `.org` 未注册 / 可注册；
- `registered`：机器信号明确支持已注册 / 已分配；
- `invalid-label`：normalized label 本身不满足注册字符串规则；
- `unknown`：证据不足、信号相互冲突或无法形成可靠结论；
- `error`：endpoint failure、rate limit、解析失败、网络异常等。

Hard gate：

- `available` → E1 pass；
- `registered` / `invalid-label` → E1 fail；
- `unknown` / `error` → 不得判 pass，交 Orchestrator 标记为 unresolved / retry-required。

### 3.4 Evidence minimum

每个候选至少记录：

- opaque_candidate_id
- display_name
- normalized_name
- queried_domain
- observation
- raw machine signal / status
- source / endpoint
- observed_at
- confidence
- caveat（如有）

E1 不评价名字质量，不搜索现实品牌身份，不提出替代拼写。

## 4. E2 — Reality Identity / Collision Runtime Config

### 4.1 Decision classes

固定为四类：

- `red`
- `yellow`
- `no-material-collision-found`
- `unknown`

### 4.2 Red

满足以下任一项，可判 `red`：

1. 与活跃公司 / 组织 / 产品 / app / service / project / software 存在 exact-name identity，且其可见度或使用场景足以构成显著身份占用；
2. near-identity 与当前 Naming Job 的组织级 / knowledge / technology / research / open-infrastructure 等邻近语境高度接近，存在严重混淆风险；
3. 存在强 trademark-oriented evidence 或长期显著品牌身份，使该名称作为新的 umbrella organization 使用明显不适合进入 finalist；
4. prominent person / creator identity 与名称高度重合，且会使组织身份明显被该人物身份吞没。

`red` 是 benchmark reality-screening 的 decisive collision，不是法律判决。

### 4.3 Yellow

判 `yellow` 的典型情况：

- 存在 exact / near identity，但规模、活跃度、地域或类别邻近性不足以直接判 Red；
- 搜索结果存在明显歧义，需要进一步人工 / 法律 / jurisdiction-specific review；
- 有 historical identity 或弱 trademark-oriented evidence，不能忽略但也不足以 decisive fail；
- 多个弱冲突叠加形成实质性 caution。

Yellow 不等于通过，也不等于淘汰；进入 Orchestrator 的 unresolved feasibility state。

### 4.4 No-material-collision-found

仅当指定搜索表面已经覆盖，且没有找到足以达到 Yellow / Red 的 materially relevant identity 时使用。

必须表述为 `no-material-collision-found`，不得写成：

- “商标安全”；
- “全球可用”；
- “已经 clearance”；
- “没有任何人使用”。

### 4.5 Unknown

以下情况使用 `unknown`：

- 搜索失败或结果不足；
- 关键证据无法访问；
- 同名实体无法可靠判定是否活跃 / 相关；
- 结果冲突且不能稳定归类。

不得把 unknown 自动降为 Yellow 或通过。

### 4.6 Required search surfaces

每个候选至少覆盖：

1. general web exact-name search；
2. active company / organization identity；
3. product / app / service；
4. project / software / GitHub identity；
5. trademark-oriented public evidence；
6. prominent person / creator identity（仅当搜索结果显示可能 materially relevant）；
7. historical identity（仅当其遗留品牌强度 materially relevant）。

搜索时应同时检查 exact 与少量自然 near-identity 变体，但不得扩展成无边界的词根家族搜索。

### 4.7 Evidence requirements

每个 Yellow / Red 至少需要：

- collision_surface
- exact_or_near
- identity name
- active / historical status（能判断时）
- adjacency / confusion rationale
- source references
- confidence

单一低质量聚合页、自动生成目录、无来源转载不得单独支持 Red。

## 5. E3 — Quality / Pareto Runtime Config

### 5.1 评价原则

- feasible ≠ high quality；
- Owner preference ≠ naming quality；
- 不以单一加权总分决定一切；
- 保留多维观察与 Pareto trade-off；
- E3 完全 blind to E1 / E2；
- 评价对象是冻结 generation denominator 中的每一个候选，而不是 method survivor。

### 5.2 固定质量维度

每个候选必须观察以下 10 个维度：

1. `distinctiveness` — 是否具有独立品牌边界，避免 generic / ordinary identity；
2. `pronounceability` — 读出、口头复述与跨使用情境下的发音负担；
3. `spelling_burden` — 听觉→拼写、视觉→读音的恢复成本；
4. `memorability` — 是否有足够清晰、稳定且不依赖 gimmick 的记忆抓手；
5. `semantic_fit` — 与 Organization Vision 是否存在可信的语义 / 体验入口；
6. `semantic_room` — 是否给长期品牌叙事和未来扩展留下空间；
7. `umbrella_fit` — 是否像长期母组织，而非单一产品 / 协议 / 工具 / campaign；
8. `longevity` — 是否避免明显短期潮流、过度科技时代感或狭窄类别绑定；
9. `symbolic_compressibility` — 是否能形成简洁、可复述的核心意象 / 品牌故事，而不要求名字承担全部哲学；
10. `cross_context_usability` — 在普通文本、口语、组织署名、项目归属等环境中是否自然成立。

同时必须显式检查两类负向信号：

- `excessive_descriptiveness_or_genericness`
- `artificiality_or_awkwardness`

### 5.3 A–E Quality Band

Quality Band 是整体判断，不是十维平均分。

- **A — exceptional / finalist-grade quality**：多数关键维度强，几乎没有结构性品牌缺陷；存在 trade-off，但不会明显限制长期 umbrella use；值得进入高优先级 finalist pool。
- **B — strong / viable quality**：整体明显成立，有清楚优势；存在一至两个真实弱点或张力，但不破坏长期品牌可能性；值得继续比较。
- **C — mixed / conditional quality**：有可取之处，也有明显结构性代价；需要较强叙事、学习或使用条件才能成立；不应与 A/B 等同。
- **D — weak quality**：多个关键维度明显不足，或存在一个严重但非绝对致命的品牌结构问题；通常不值得进入高优先级 finalist。
- **E — fundamentally poor fit**：作为当前 umbrella-organization Naming Job 在品牌质量层面根本不成立，例如极度描述性 / 类别锁定 / 难读难记 / 人工感严重 / 跨场景明显失效。

Band 不得包含 feasibility 信息。

### 5.4 Pareto status

每个候选输出：

- `pareto_frontier`
- `non_dominated_but_mid_band`
- `dominated`
- `insufficient_comparison_evidence`

定义：

- A 候选不自动等于 Pareto frontier；
- 若候选 X 在所有当前关键维度都不优于 Y，且至少一个关键维度明确更差，可将 X 标记 `dominated-by: <opaque_id>`；
- 只有存在清楚的多维支配关系时才使用 dominated，不允许凭整体偏好声称支配；
- 两个候选若各自在不同维度有实质优势，则视为 trade-off，不判 dominated；
- 小样本或证据不足时可以保守使用 `insufficient_comparison_evidence`。

### 5.5 Confidence

固定为：

- `high`
- `medium`
- `low`

Confidence 表示对观察稳定性的把握，不代表质量高低。

出现以下情况应降低 confidence：

- coined form 存在多种合理发音；
- 关键语义高度依赖文化 / 语言背景；
- rationale 缺失导致 semantic trace 不完整；
- 当前候选信息不足以判断某一维度。

### 5.6 E3 Output minimum

每个候选至少输出：

- opaque_candidate_id
- quality_band: A–E
- 10 dimension observations
- excessive_descriptiveness_or_genericness
- artificiality_or_awkwardness
- strengths
- weaknesses
- pareto_status
- dominated_by（如适用，仅 opaque IDs）
- confidence

不得输出：

- `.org` 状态；
- reality collision；
- Owner preference；
- arm / method identity；
- “因为可注册所以更好”之类混合判断。

## 6. Blind runtime alias rule

由于 canonical `DRY-G1-001` 本身泄露 arm 身份，blind Worker Session 不得使用 canonical run ID。

Orchestrator 必须为 E1 / E2 / E3 / E5 生成中性 runtime alias，例如：

- runtime batch alias：`NX-001`
- opaque candidate IDs：`R7K2`, `M4Q9`, `T8V3`, `H2P6`

实际 alias 必须由 Orchestrator 在每次 run 中生成并私下保存映射；不得把示例值机械复用为正式全局固定值。

Worker-visible：

- 中性 CHAT TITLE；
- 中性 runtime alias；
- opaque candidate IDs；
- sanitized rationale / pronunciation（仅角色确实需要时）；
- 无 arm / method / provenance path。

Canonical storage：

- canonical run ID；
- arm / method；
- opaque ↔ canonical mapping；
- packet / config versions；
- raw Worker output；
- restored canonical results。

## 7. Version / freeze rule

- config_version: `0.1`
- current_status: `dry-run freeze candidate`
- first_validation_run: `DRY-G1-001`

本配置在 dry-run 中可以因真实运行缺陷修正；一旦用于正式 isolated benchmark，必须冻结版本。

后续修改若改变 hard gate、severity class、quality band、Pareto rule、blindness 或 evidence minimum，必须升版本并说明是否影响历史 run 可比较性。

## 8. Provenance

- Naming Job dynamic constraint source: Issue #409 current protocol；
- Shared evaluation packet basis: E1 / E2 / E3 v0.1；
- Historical evidence consulted: Issue #410 Gate A→B→C/D→A–E/Pareto practice，仅作为经验来源，不直接继承为新配置；
- Blind runtime rule source: `worker-task-packet-schema-v0.1.zh-CN.md`；
- Denominator rule source: `naming-worker-conversation-plan-v0.1.zh-CN.md`。
