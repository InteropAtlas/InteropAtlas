# Human Route Renderer Boundary v0.1

<!-- InteropAtlas Document Metadata v0
Document Status: Working Architecture Decision
Document Created At: 2026-09-02T11:24:59+08:00
Document Updated At: 2026-09-02T11:24:59+08:00
Metadata Backfilled At: 2026-09-02T11:35:52+08:00
Metadata Provenance: reconstructed_from_git
Lifecycle Time Provenance: reconstructed_from_git
Contribution Identity Provenance: commit_explicit
Latest Substantive Contribution:
  Initiator: Human — ff6962757
  Executor: Agent — OpenAI / ChatGPT / GPT-5.6 Sol
  Reviewer: Pending
  GitHub Actor: ff6962757
-->

> Status: Working Architecture Decision
>
> Date: 2026-09-02
>
> Parent: #16 / Work Item: #101

## 1. 问题

Gate B 为了快速验证 Legacy / v0 共存、四类 Resource Page、Breadcrumb、Local Map 状态反馈和 Browser E2E，使用 `render_site_semantic.py` 作为 transitional adapter（过渡适配层）。

这个策略在 Foundation 阶段是合理的，但 Gate B 通过后继续把新的产品行为塞进 adapter 会产生结构性债务：

```text
Legacy/v0 compatibility
+
Human View selection
+
Organization projection
+
Interaction accessibility behavior
+
CSS patch
+
JavaScript text patch
+
Homepage grouping
```

这些职责不应该永久绑在一起。

## 2. v0.1 边界

本轮只做第一刀，不重写整站。

### Permanent Human Route Runtime

新模块：

`02_Runtime/01_Engine/human_route_runtime.py`

负责已经通过 Gate B 验证、与 Legacy/v0 数据兼容本身无关的用户可观察合同：

- Local Map loading / success / failure / retry；
- `role=status` / `aria-live`；
- visible focus；
- reduced-motion；
- stable Human semantic center label；
- 未来其他真正属于 Human Route runtime 的共享行为。

这些行为不再通过“查找旧 JavaScript 字符串然后替换”的方式注入。

### Transitional Semantic Adapter

`render_site_semantic.py` 暂时继续负责：

- Legacy/v0 Human View selection；
- Organization representative projection；
- semantic breadcrumb / link adaptation；
- homepage grouping；
- 调用 permanent Human Route runtime。

它不再拥有 Interaction CSS / JavaScript patch implementation。

### Legacy Renderer

`render_site.py` 暂时继续提供：

- HTML shell primitives；
- existing map HTML projection；
- legacy build path；
- common low-level helpers。

本轮没有强行把所有 legacy primitive 一次迁走。

## 3. 为什么先迁 Interaction Runtime

这是最适合作为第一刀的职责，因为：

1. Gate B 已有真实 Chromium 回归证据；
2. 它与 Legacy/v0 object identity 没有本质绑定；
3. 原实现依赖 brittle string replacement（脆弱字符串替换）；
4. 后续 Search / Compare / richer Graph 都会继续依赖稳定 runtime behavior；
5. 迁移风险小，且可以保持页面输出和交互基本不变。

## 4. 同步修复：Human semantic type label

旧 Local Map 中心会直接显示 raw `type`，例如：

```text
当前地图中心 · system
```

这泄漏 Knowledge Model / serialization enum（知识模型 / 序列化枚举）到主要 Human View。

v0.1 runtime 增加 Human semantic label：

```text
system + implementation profile
→ 实现

concept + capability profile
→ 能力

agent + organization profile
→ 组织
```

这只是 View projection（视图投影）变化，不修改 Canonical Fact。

## 5. 当前依赖方向

```text
Canonical State
      ↓
semantic normalization / profile selection
      ↓
render_site_semantic.py
Legacy/v0 compatibility adapter
      ↓
human_route_runtime.py
Permanent user-observable runtime contract
      ↓
render_site.py primitives
      ↓
HTML / Browser
```

后续迁移目标是逐步减少 adapter 对 legacy primitives 的依赖，而不是立即删除 `render_site.py`。

## 6. 后续可迁移职责

下一批候选按优先级：

1. Page Shell / stable Human route shell；
2. semantic breadcrumb / Human labels；
3. Resource Page renderer registry；
4. Local Map HTML projection；
5. Homepage / collection view projection。

每一批都应该小步迁移，并保持 Browser / Machine Review / Graph 回归。

## 7. 明确不做

本轮不做：

- Search；
- full Compare UI；
- full renderer rewrite；
- React / Vue；
- Graph library replacement；
- Canonical migration；
- Knowledge Model change；
- URL state redesign；
- Visual redesign。

## 8. Stop condition

#101 第一小步达到完成条件，当：

- interaction/accessibility behavior 不再由 semantic adapter 的 string patch 实现；
- permanent runtime module 有独立测试；
- Local Map center 不再暴露 raw core type；
- Browser E2E 继续通过；
- Machine Review / relation / graph / Compare regression 不退化；
- adapter 职责被明确缩窄；
- 剩余 migration debt 有清晰后续顺序。
