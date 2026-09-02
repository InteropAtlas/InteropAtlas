# Human Route Renderer Boundary v0.1

> Status: Working Architecture Decision
>
> Date: 2026-09-02
>
> Parent: #16 / Work Items: #101, #107

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
Document shell / Breadcrumb
+
Homepage grouping
```

这些职责不应该永久绑在一起。

## 2. 第一批边界：Permanent Human Route Runtime（#101）

模块：

`02_Runtime/01_Engine/human_route_runtime.py`

负责已经通过 Gate B 验证、与 Legacy/v0 数据兼容本身无关的用户可观察合同：

- Local Map loading / success / failure / retry；
- `role=status` / `aria-live`；
- visible focus；
- reduced-motion；
- stable Human semantic center label。

这些行为不再通过“查找旧 JavaScript 字符串然后替换”的方式注入。

第一批同时修复了 Local Map center 暴露 raw core `type` 的问题：

```text
system + implementation profile → 实现
concept + capability profile     → 能力
artifact + normative profile     → 标准 / 规范
agent + organization profile     → 组织
```

这是 View projection（视图投影），不修改 Canonical Fact。

## 3. 第二批边界：Permanent Human Route Shell（#107）

新模块：

`02_Runtime/01_Engine/human_route_shell.py`

负责跨 Resource Page / Search / Compare 稳定共享的页面级合同：

- HTML document shell；
- global navigation；
- semantic `<main>`；
- Breadcrumb `<nav aria-label="面包屑">` shell；
- breadcrumb current-page semantics；
- Capability category breadcrumb 作为 View 的链接结构；
- route prefix 在不同深度页面中的统一输入。

`render_site_semantic.py` 不再直接维护这些 HTML 模板，只提供：

- 当前对象的 Legacy/v0 semantic view type；
- Human display/value callbacks；
- category anchor callback；
- 兼容阶段仍需要的 route/link adaptation。

Search 和 Compare 也改为使用同一个 permanent `page_shell` callable，因此它们不再直接依赖 legacy `render_site.page_shell`。

## 4. Transitional Semantic Adapter 当前职责

第二批迁移后，`render_site_semantic.py` 继续保留的主要职责是：

- Legacy/v0 Human View selection；
- Organization representative projection；
- semantic link adaptation；
- Homepage grouping；
- 将 compatibility callbacks 连接到 permanent Human Route modules；
- 调用 Search / Compare / Runtime / Shell 模块完成最终 build。

它不再拥有：

- Interaction CSS / JavaScript patch implementation；
- stable Human Route document shell template；
- Breadcrumb HTML implementation。

因此 adapter 的职责继续缩窄，而不是因为 Search / Compare 新功能重新膨胀。

## 5. Legacy Renderer 当前职责

`render_site.py` 暂时继续提供：

- existing CSS / theme primitive assets；
- existing Local Map HTML projection；
- legacy build path；
- object card / category anchor / Markdown-to-HTML 等低层 helper。

Permanent Shell 当前读取这些共享 asset，但不使用 legacy `page_shell` 实现。

这一步是有意的小迁移：先把**页面职责归属**迁对，再决定是否需要移动 CSS / Theme / Map HTML primitives 的物理代码。

## 6. 当前依赖方向

```text
Canonical State
      ↓
semantic normalization / profile selection
      ↓
render_site_semantic.py
Legacy/v0 compatibility adapter
      ↓
┌──────────────────────────────────┐
│ human_route_shell.py             │
│ human_route_runtime.py           │
│ human_route_search.py            │
│ human_route_compare.py           │
└──────────────────────────────────┘
Permanent Human Route responsibilities
      ↓
render_site.py low-level / legacy primitives
      ↓
HTML / Browser
```

目标不是立刻删除 `render_site.py`，而是逐批减少 permanent product behavior 对 legacy implementation ownership 的依赖。

## 7. 后续可迁移职责

接下来候选按优先级：

1. Resource Page renderer registry（页面类型 → renderer 的长期注册边界）；
2. shared Human link / route helpers；
3. Local Map HTML projection；
4. Homepage / collection view projection；
5. CSS / theme primitives（只有当职责稳定并确有收益时）。

每一批都必须保持：

- stable routes；
- Search；
- Compare；
- four-family Resource Pages；
- Browser E2E；
- Machine Review / Relation / Graph regression。

## 8. 明确不做

当前 renderer-boundary 工作不自动做：

- Search 功能扩张；
- Compare generalization；
- full renderer rewrite；
- React / Vue；
- Graph library replacement；
- Canonical migration；
- Knowledge Model change；
- URL state redesign；
- Visual redesign。

## 9. Stop conditions

### #101 第一批

- [x] interaction/accessibility behavior 不再由 semantic adapter 的 string patch 实现；
- [x] permanent runtime module 有独立测试；
- [x] Local Map center 不再暴露 raw core type；
- [x] Browser / Machine / Graph / Compare regression 保持。

### #107 第二批

完成条件：

- stable document shell 由 permanent module 提供；
- semantic Breadcrumb HTML 由 permanent module 提供；
- Search / Compare / Resource Pages 使用同一 shell contract；
- different route depths 的 Home link 保持正确；
- `render_site_semantic.py` 不再直接拥有 shell / breadcrumb template；
- 全部 Browser / Machine / Relation / Graph regression 继续通过。
