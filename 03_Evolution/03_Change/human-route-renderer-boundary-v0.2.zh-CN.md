# Human Route Renderer Boundary v0.2

<!-- InteropAtlas Document Metadata v0
Document Status: Working Architecture Decision
Document Created At: 2026-09-02T12:10:00+08:00
Document Updated At: 2026-09-02T12:10:00+08:00
Lifecycle Time Provenance: direct_record
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
> Parent: #16 / Work Item: #107

## 1. 本轮选择

第二批 permanent Human Route boundary 只迁移一个最小闭环：**shared Page Shell entry point + semantic Breadcrumb + stable Human route-link helper + shared Human view labels**。

不迁移 Homepage、Local Map HTML、Organization renderer 或全部 legacy HTML primitives。

## 2. 新边界

新增：

`02_Runtime/01_Engine/human_route_shell.py`

它负责：

- Human-facing semantic view labels；
- semantic Breadcrumb；
- stable Human HTML route link resolution；
- Search / Compare / Resource Page 共用的 Page Shell entry point。

`render_site_semantic.py` 只保留薄 compatibility hooks，把 Legacy/v0 semantic projection 传给 permanent shell。

## 3. 为什么这一刀足够小

Breadcrumb 与 route helper 已经过 Gate B、Search、Compare 和四类 Resource Page 的 Browser evidence；它们不应继续作为 transitional adapter 的实现细节。同时底层 CSS / theme / legacy HTML shell primitive 仍留在 `render_site.py`，避免本轮演变成 renderer rewrite。

依赖方向变为：

```text
Legacy/v0 semantic projection
        ↓
render_site_semantic.py  (compatibility adapter)
        ↓
human_route_shell.py     (permanent Human shell contract)
        ↓
render_site.py            (low-level legacy primitives, temporary)
```

Search、Compare 与 Resource Page 现在通过同一个 Human Route `page_shell` entry point 生成页面，而不是由 semantic adapter 直接把 legacy shell callback 分发给各模块。

## 4. 保持不变

- Canonical data / Knowledge Model 不变；
- stable Resource URL 不变；
- Breadcrumb 文案与层级不变；
- Search / Compare URL 不变；
- Homepage projection 不变；
- Local Map runtime contract 不变；
- 不引入 frontend framework。

## 5. 后续债务

下一批候选仍是：

1. 把低层 HTML shell primitive / style ownership 从 legacy renderer 进一步分离；
2. Resource Page renderer registry；
3. Local Map HTML projection；
4. Homepage / collection projection。

这些不属于 #107 当前 slice，必须继续小步迁移并保留 Browser / Machine / Graph 回归。
