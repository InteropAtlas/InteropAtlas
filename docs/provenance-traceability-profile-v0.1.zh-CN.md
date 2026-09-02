# InteropAtlas Provenance / Traceability Profile v0.1

> 状态：Draft Specification（草案规范）
>
> 文档创建时间：2026-09-02T08:50:00+08:00
>
> 文档最后实质更新：2026-09-02T09:10:00+08:00
>
> 目的：以尽量轻量、结构化、可检索的方式记录 InteropAtlas 知识与贡献的时间、身份、来源和验证留痕。

## 1. 核心原则

InteropAtlas 将“靠谱、可追溯、可重新验证”作为标准类知识的重要质量要求。

V0.1 采用四类留痕：

1. **时间留痕**：记录何时创建、何时最后实质更新、何时最后验证；
2. **身份留痕**：记录谁发起、谁实际执行、谁独立审核，并单独保留 GitHub Actor（GitHub 平台操作账号）；
3. **来源留痕**：记录知识来自哪些权威来源 / Evidence（证据）；
4. **验证留痕**：记录最近何时、由谁、基于已有来源 / Evidence 重新核验。

变更历史不在 Canonical Record 中重复造一套日志。Commit、Diff、PR、Issue 等变更留痕继续由 Git / GitHub 作为权威事件历史承担。

## 2. 上游标准与先例

本 Profile 采用 `Adopt → Profile → Extend → Invent（采用 → 定制 → 扩展 → 最后才自行发明）` 原则。

本轮已经正式研究并收录：

- **W3C PROV-DM（W3C 溯源数据模型）**：提供 Entity（实体）、Activity（活动）、Agent（参与者）以及 Attribution（归因）、Association（关联）、Delegation（委派）、Derivation（派生）等概念边界；
- **W3C PROV-O（W3C 溯源本体）**：PROV 数据模型的 OWL2（Web 本体语言）表达，用于可交换的结构化 Provenance（溯源）；
- **W3C PROV-CONSTRAINTS（W3C 溯源约束）**：说明 Provenance 可以进行一致性和有效性机器检查；
- **W3C PROV-AQ（W3C 溯源访问与查询）**：说明 Provenance 可以通过标准 Web 机制定位、获取和查询；该文档是 Working Group Note（工作组说明），不是 Recommendation（推荐标准）；
- **SPDX 3.0.1 CreationInfo（SPDX 创建信息模型）**：提供 `created`、`createdBy`、`createdUsing`、`specVersion` 等结构化创建信息；
- **DCMI Metadata Terms（都柏林核心元数据术语）**：提供 `modified`、`provenance` 等成熟通用元数据概念；
- **SLSA 1.2 Provenance（SLSA 1.2 溯源规范）**：强调可验证 Provenance 的完整性、真实性、准确性，以及 Builder（构建者）、运行实例、输入和时间等工程边界。

详细对照研究见 `03_Evolution/01_Research/provenance-traceability-prior-art-2026-09-02.zh-CN.md`。

研究结论是：InteropAtlas 当前不需要复制完整 PROV 本体、SLSA 构建结构或另建 Change Log（变更日志）系统，而应采用这些标准的核心边界并保持轻量 Profile（定制规范）。

## 3. 时间留痕

Canonical Object（规范对象）和 Relation（关系）使用：

```yaml
record_created_at: 2026-09-02T08:50:00+08:00
record_updated_at: 2026-09-02T08:50:00+08:00
last_verified_at: 2026-09-02T08:50:00+08:00
```

含义：

- `record_created_at`：该 InteropAtlas Record（记录）首次创建时间；
- `record_updated_at`：该 Record 最近一次**实质内容更新**时间；
- `last_verified_at`：最近一次依据来源 / Evidence 完成实质核验的时间。

验证但没有修改事实时，`last_verified_at` 可以更新，而 `record_updated_at` 不应因此自动改变。

现实对象自己的发布时间、生效时间、废止时间等属于对象事实，不得与 Repository Record（仓库记录）生命周期时间混用。

## 4. 身份留痕

核心贡献身份保持三个：

```text
Initiator（发起人）
Executor（实际执行者）
Reviewer（审核人）
```

另外单独记录：

```text
GitHub Actor（GitHub 操作账号）
```

GitHub Actor 是平台 Provenance（平台溯源），不是第四个贡献角色。

Approver（批准人）只在 Governance Authorization（治理授权）需要时记录，不作为每次普通贡献的必填核心身份。

完整规则见 `docs/agent-attribution-contribution-identity-profile-v0.1.zh-CN.md`。

## 5. 来源留痕

Object 使用 `sources`，Relation 使用 `evidence` 记录来源。标准、规范、协议等对象 SHOULD 优先引用官方发布者、一手规范页面或其他权威来源。

来源至少应尽可能包含：

```yaml
- url: https://example.org/spec
  title: Official Specification
  language: en
  accessed: 2026-09-02
```

`accessed` 表示该来源被访问的日期，不自动等于整个 Record 已完成验证。

## 6. 验证留痕

Canonical Record SHOULD 在完成实质核验后维护：

```yaml
last_verified_at: 2026-09-02T08:50:00+08:00
last_verified_by: agent:openai:chatgpt
```

验证必须有来源 / Evidence 依据。`last_verified_by` 记录真正执行验证的 Human（人类）或 Agent（智能体），不能因为 Agent 使用 Human GitHub 账号就把 GitHub Actor 当作验证者。

验证的目的包括：

- 检查标准是否出现新版本；
- 检查是否被 supersede（取代）/ withdraw（撤回）/ deprecate（弃用）；
- 检查官方 URL、状态、组织、版本等关键事实是否变化；
- 为未来 Freshness（新鲜度 / 时效性）查询提供结构化依据。

## 7. Freshness（新鲜度 / 时效性）

`last_verified_at` 应允许未来查询：

> 哪些标准已经较长时间没有重新核验？

V0.1 不规定统一的“过期”天数。不同知识类型的变化速度不同，后续可以按 Kind（类型细分）或 Domain（领域）建立 Revalidation Policy（重新验证策略）。

## 8. 旧数据迁移

不立即批量修改全部 Legacy Object / Relation（旧对象 / 关系）。

采用渐进策略：

- 新建 v0 Record：SHOULD 填写时间、来源和验证留痕；
- 旧 Record 发生实质修改或重新验证：顺手补齐适用字段；
- 完全未触碰的旧数据：当前不要求为了回填而单独进行大规模迁移；
- 不确定的历史创建时间不得伪造。

## 9. 规范文档留痕

InteropAtlas 自产 Specification / Profile / Governance Document（规范 / 配置规范 / 治理文档）本身也会演化，因此 SHOULD 在文档头部提供至少：

```text
状态：Draft / Stable / Superseded ...
文档创建时间：...
文档最后实质更新：...
版本：适用时记录
```

Git 历史仍保存完整逐次变更；文档头部字段用于人类阅读和结构化检索。未来如果文档进入 Canonical Object 模型，可通过稳定 ID 与对应 Record 生命周期关联。

## 10. 可靠性边界

当前结构化留痕提高的是可追溯性和可复核性，不等于自动证明内容真实。

参考 SLSA（软件供应链等级）与 PROV-CONSTRAINTS（溯源约束）的思想，未来更高保证等级可以增加 Verification Event（验证事件）、Attestation（证明声明）、签名或更严格机器验证，但 V0.1 不提前引入这些复杂度。

## 11. V0.1 最小执行规则

1. Git / GitHub 继续独立承担变更历史，不重复建立 Change Log 数据模型；
2. 新建或实质修改的 v0 Object / Relation SHOULD 维护 `record_created_at`、`record_updated_at`；
3. 完成实质核验时 SHOULD 维护 `last_verified_at`、`last_verified_by`；
4. 标准类知识 SHOULD 保留权威来源 / Evidence；
5. Agent / mixed contribution（智能体 / 混合贡献）按 Contribution Identity Profile 记录 Initiator / Executor / Reviewer，并分离 GitHub Actor；
6. 自产规范文档 SHOULD 维护可见的创建 / 最后实质更新时间；
7. 不因本 Profile 立即触发全仓库 Legacy Data（旧数据）批量迁移；
8. 如果未来需要更高可靠性，优先增加独立 Verification / Attestation 层，而不是持续向 Object 顶层堆积字段。
