# InteropAtlas Search Contract v0.1

> Status: Draft / Reference Implementation Contract
>
> Date: 2026-09-02
>
> Parent: #16 / Work Item: #103

## 1. 目的

Search（搜索）是 InteropAtlas 的 View / Projection（视图 / 投影），用于完成 Find / Identify / Explore 用户任务。

它不定义新的 Canonical taxonomy（规范分类），也不改变对象事实。

首版目标非常有限：

> **让用户能通过名称、关键词或稳定 ID 找到当前已经拥有 Human Resource Page 的对象，并沿真实稳定链接进入对象页。**

## 2. Search source

Search index MUST 由当前 Human Route 已发布对象 deterministic build（确定性生成）。

首版索引字段：

- stable ID；
- Human display name；
- Human summary；
- Human semantic type label；
- aliases（存在时）；
- stable Resource Page URL。

不得把未发布 Human View 的内部对象偷偷暴露成不可访问结果。

## 3. Query semantics

### `IA-HI-SRCH-001` — Transparent substring matching

v0.1 使用大小写不敏感的简单文本匹配。

匹配来源：name / ID / summary / Human type label / aliases。

不使用：

- embedding；
- vector search；
- LLM inference；
- hidden personalization；
- opaque relevance scoring。

### `IA-HI-SRCH-002` — Deterministic ordering

结果排序 MUST 可解释、可重复。

v0.1 规则：

```text
exact name / ID
↓
prefix name / ID
↓
other substring match
↓
Human name / stable ID deterministic order
```

这只是 result ordering，不是 recommendation。

## 4. URL state

### `IA-HI-SRCH-003` — Query is URL-worthy state

Search query MUST 进入 URL `?q=`。

用户 SHOULD 可以：

- 复制搜索 URL；
- 刷新后恢复 query；
- Browser Back / Forward 恢复 query；
- 从 result 进入 Resource Page 后 Back 回到原 query。

这落实 Interaction Profile 对 URL-worthy state 的第一个真实产品切片。

## 5. Result contract

每个结果 MUST 至少显示：

- Human name；
- stable Resource Page link；
- Human semantic type label；
- stable ID；
- summary（存在时）。

Raw core type（如 `system` / `concept` / `artifact` / `agent`）MUST NOT 作为主要 Human type label。

Search result 不得自动加入：

- “最佳”；
- 推荐分数；
- popularity；
- confidence；
- hidden ranking reason。

除非未来这些信息本身有独立 Assessment / provenance contract。

## 6. Accessibility / progressive enhancement

- Search form 使用原生 `form / input[type=search] / button`；
- result 使用真实 hyperlink；
- result count / failure 使用 perceivable status；
- query path MUST keyboard-operable；
- narrow viewport MUST reflow；
- JavaScript 禁用时 Search page 的说明、Home navigation 和其他稳定 Resource Pages 仍可用。

v0.1 不承诺 JS disabled 下提供动态搜索结果。

## 7. Failure behavior

如果 `search-index.json` 载入失败：

- MUST 显示可感知失败提示；
- MUST NOT 把整个 Human Route 变成不可导航；
- Home / existing Resource Pages 继续可用。

## 8. Representative acceptance queries

首版至少验证：

```text
Forgejo
→ Forgejo Actions

自动构建
→ 自动构建与部署

YAML
→ YAML

Apple
→ 苹果公司
```

## 9. Non-goals

v0.1 不包含：

- facets；
- advanced filters；
- typo tolerance；
- fuzzy semantic matching；
- vector DB；
- remote service；
- search analytics；
- recommendation；
- full Compare UI。

## 10. 下一层

Search v0.1 稳定后，再根据真实任务决定：

1. 加 Domain / Organization / Scenario entry points；
2. 加 lightweight filters；
3. 把 Search result candidate set 接入 Compare；
4. 或优先建设 dedicated Compare View。

不要因为首版 Search 成立就自动扩张成搜索平台工程。
