# Provenance / Traceability Prior Art 研究 — 2026-09-02

> 状态：Research Record（研究记录）
>
> 创建时间：2026-09-02T09:10:00+08:00
>
> 最后实质更新：2026-09-02T09:10:00+08:00

## 结论

InteropAtlas 当前的轻量留痕模型方向成立，不需要引入完整 Provenance（溯源）本体或软件供应链证明系统。

当前应保留四类信息：

1. 时间：Record 创建、实质更新、最后验证；
2. 身份：Initiator（发起人）、Executor（实际执行者）、Reviewer（审核人），GitHub Actor（GitHub 操作账号）独立；
3. 来源：Object 的 `sources` / Relation 的 `evidence`；
4. 验证：`last_verified_at` / `last_verified_by`。

Git / GitHub 继续承担完整 Change History（变更历史），不在 Canonical Data 中重复建设事件日志。

## 参考对象

### W3C PROV-DM / PROV-O

采用：
- Entity（实体）/ Activity（活动）/ Agent（参与者）应分开；
- Attribution（归因）、Association（关联）、Delegation（委派）、Derivation（派生）是不同关系；
- Provenance 本身可以形成可查询的结构化图。

当前不采用：
- 完整 PROV 本体；
- 为每次 Record 修改建立 Activity 对象；
- 完整 derivation / bundle 模型。

原因：当前 Git 已经保存逐次变更事件，完整复制会显著增加维护成本。

### W3C PROV-CONSTRAINTS

采用其原则：Provenance 不只是备注，而应允许机器检查一致性。

当前只要求 Schema / Validator 能检查必要字段格式与引用；不实现完整 PROV 推理。

### W3C PROV-AQ

记录为未来参考：它说明 Provenance 可以被定位、获取和查询。

当前不建设独立 Provenance Query Service（溯源查询服务）；IA 未来直接通过统一 Query / View（查询 / 视图）层暴露即可。

### SPDX 3.0.1 CreationInfo

采用：
- 创建时间应结构化；
- 创建者 / Agent 应结构化；
- 工具身份在需要判断可靠性时有价值。

Profile（定制）：IA 将贡献身份拆成 Initiator / Executor / Reviewer，而不是只有单一 `createdBy`。

当前不要求每条知识记录保存 `createdUsing`；Agent / tool 信息主要留在贡献记录，避免 Canonical Knowledge Record 被仓库操作细节污染。

### DCMI Metadata Terms

采用：
- `modified` 证明“资源修改时间”是成熟通用元数据概念；
- `provenance` 证明来源/保管历史对于真实性、完整性和解释有价值。

Profile：IA 明确区分现实对象时间、IA Record 生命周期、Git 变更历史和 Knowledge Provenance（知识溯源）。

### SLSA 1.2 Provenance

采用其可靠性思想：
- Provenance 应尽可能可验证；
- 应区分真正的执行主体与平台/系统身份；
- 完整性、真实性、准确性是不同质量维度；
- 运行实例 / invocation ID（调用实例标识）对事故调查有价值。

当前不采用：
- Build Definition（构建定义）、resolvedDependencies（已解析依赖）、artifact digest（制品摘要）等软件构建专用结构；
- 强制签名 / Attestation（证明声明）。

这些能力只有在 IA 未来需要更高安全等级或自动发布供应链时再考虑。

## Adopt / Profile / Defer

### Adopt（直接采用思想）
- 时间、参与者、来源、验证分离；
- 来源 / Evidence 可追溯；
- 验证时间与修改时间分离；
- GitHub Actor 与真实 Executor 分离；
- Provenance 字段应机器可读。

### Profile（按 IA 场景定制）
- 核心贡献角色：Initiator / Executor / Reviewer；
- GitHub Actor 单列；
- Object 使用 `sources`，Relation 使用 `evidence`；
- `record_created_at` / `record_updated_at` / `last_verified_at` / `last_verified_by`；
- Git 作为完整变更事件日志。

### Defer（暂缓）
- 完整 W3C PROV Activity 图；
- Provenance 专用查询协议；
- 每次验证都生成独立事件对象；
- 加密签名、Attestation、不可伪造证明；
- 全部旧数据一次性回填。

## 对现有 Profile 的影响

研究没有发现需要推翻当前 `docs/provenance-traceability-profile-v0.1.zh-CN.md` 的结构性问题。

补充结论：

1. `last_verified_at` 不应由 `record_updated_at` 替代；
2. `last_verified_by` 应记录真实 Human / Agent verifier（验证者），不是 GitHub Actor；
3. `sources.accessed` 只代表访问来源，不代表完整验证；
4. Agent 使用了什么模型 / 工具属于 Contribution Provenance（贡献溯源），不默认塞进每个 Knowledge Object（知识对象）；
5. 未来如果需要更强“靠谱”保证，优先增加 Verification Event / Attestation（验证事件 / 证明声明），而不是不断向 Object 顶层堆字段。

## Stop Condition

本轮 Prior Art（先例研究）在以下范围停止：W3C PROV 核心家族、SPDX CreationInfo、DCMI Metadata Terms、SLSA Provenance。

它们已经覆盖通用概念模型、元数据、工程创建信息、机器一致性和高可靠软件溯源五个角度。当前没有必要继续开放式搜集更多 Provenance 标准；后续只有遇到具体模型缺口时再扩展。
