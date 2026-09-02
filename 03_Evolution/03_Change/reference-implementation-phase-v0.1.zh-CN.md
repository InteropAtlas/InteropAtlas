# InteropAtlas Reference Implementation Phase v0.1

> Status: Working Phase Plan
>
> Starts after: Gate B Final Conformance Audit 2026-09-02
>
> Current umbrella: #16
>
> Human Interface baseline: `docs/human-interface-profiles-v0.1.zh-CN.md`

## 1. Phase transition

Foundation First 已经建立三项主要 Gate：

```text
Gate A — Repository Structure     ✅ PASS
Gate B — Human Interface          ✅ PASS
Gate C — Open Collaboration       ✅ PASS
```

Knowledge Model v0 / Machine Contract 也已经完成 representative foundation validation。

因此主线从：

> “继续证明 Foundation 是否足够”

切换为：

> **“在已经建立的 Foundation 合同下建设 Reference Implementation（参考实现），并用真实产品工作继续反向验证这些合同。”**

F4 Curation / Evidence / Machine Correctness 仍作为平行质量线继续，不阻塞每一个产品小步。

## 2. Current P0 — Human Route architecture

当前第一优先不是马上堆 Search / Compare / Graph 新功能，而是先把 Gate B 期间形成的 transitional Human Route 收敛为更长期的实现结构。

当前网站仍存在一个明确技术债：

- `render_site_semantic.py` 同时承担 Legacy/v0 compatibility adapter 和 Gate B Human Interface hooks；
- 这些 hooks 在 Foundation 阶段是有意的 bounded bridge；
- Gate B 已通过后，不应该无限把永久产品能力继续堆在 transitional adapter 上。

因此 #16 的下一阶段目标 SHOULD 是：

1. 明确 permanent Human Route renderer / page-shell architecture；
2. 保留已经验证的 stable routes、four-family Resource Page、Browser E2E 和 accessibility behaviors；
3. 逐步把 Gate B compatibility hooks 从“临时桥接”迁入长期结构；
4. 不改变 Canonical Facts / Knowledge Model；
5. 不趁机重写整个网站或引入大型前端框架。

## 3. Product capability order

Permanent Human Route 基础稳定后，产品能力按用户价值逐个选择 vertical slice，不同时把所有 P1 拉成 P0。

当前候选：

### A. Task-oriented discovery / Search

价值：降低只能从 Capability-first 入口浏览的限制。

可能包括：
- lightweight Search；
- Domain / Organization / Scenario entry points；
- query-driven collection views。

### B. Compare product slice

Gate B 已有 Minimum Compare semantic contract，但没有 dedicated UI。

下一层可能包括：
- 2-candidate Compare View；
- explainable dimensions；
- responsive / stacked presentation；
- direct evidence access；
- no hidden ranking。

### C. Evidence / Assessment presentation

将 Fact / Relation / Evidence / Assessment 在 Human View 中进一步稳定成明确的信息职责和视觉层级。

### D. Graph exploration evolution

只有在真实任务需要 pan / zoom / larger graph / multi-select 时，才评估 Cytoscape.js / Sigma.js / Graphviz / D3 等成熟基础设施；不提前发明复杂 Graph control system。

## 4. Ongoing contracts

每个 Reference Implementation PR 继续受以下合同约束：

```text
Knowledge Representation Contract
        +
Human Interface Profiles
        +
Open Collaboration / Agent Continuity
        +
Provenance / Evidence rules
        +
Machine Review / Browser E2E
```

### Human Interface regression minimum

重大 Human Route 变化 SHOULD 继续验证：

- stable link / Back / Forward；
- keyboard / visible focus；
- JS-disabled core reading；
- reflow；
- reduced motion；
- meaningful feedback / recoverability；
- representative Resource Pages；
- affected Human Task walkthrough。

## 5. Non-goals / independent decision gates

以下事项不会因为 Gate B PASS 自动获批：

- Full Canonical Migration；
- Repository-wide Schema Enforcement；
- Ruleset / Branch Protection automation；
- stable Specification promotion；
- 大规模数据删除；
- destructive Knowledge Model change；
- frontend framework rewrite；
- premature full Graph engine replacement。

## 6. First resume point

```text
#16 Reference Implementation umbrella
        ↓
Audit current transitional Human Route architecture
        ↓
Define one small permanent-renderer migration slice
        ↓
Preserve current Gate B regression evidence
        ↓
Then choose the first high-value product slice
(Search / task entry OR Compare UI, based on user value)
```

Stop condition for the first slice：

> **把 Human Route 从“Gate B 临时兼容层能工作”推进到“长期实现结构可以继续承载产品能力”，但不重写整站。**
