# Repository Canonical Storage Contract v0.1

> 文件名保留为 `repository-data-root-contract-v0.1.zh-CN.md` 以保持历史链接；标题已按 #31 修正。
>
> 状态：Implementation Preparation / Migration Guardrail
>
> 原 Work Item：#25；Corrigendum：#31
>
> 本文只定义“怎样找到 Canonical Data 的物理位置”。**没有执行任何目录迁移，也不规定未来知识分类文件夹。**

## 1. 为什么修正

#25 的正确目标是：迁移前先把路径耦合集中起来。

但第一版实现把当前 9 个目录写成 `OBJECT_FAMILIES`，并假设未来可能继续是：

```text
data/standards/
data/capabilities/
data/relations/
...
```

这会把两个问题重新绑在一起：

```text
物理文件放哪
    ≠
对象在知识模型里是什么
```

#31 明确修正：**路径合同只能描述 storage，不得充当 ontology registry。**

---

## 2. 当前真实情况

现在 Canonical YAML 仍然物理分布在：

```text
standards/
capabilities/
scenarios/
organizations/
implementations/
reference-projects/
gaps/
relations/
maps/
```

这些目录现在统一称为：

> **Current / Legacy Canonical Storage Paths**

它们是历史物理位置，不是未来必须保留的语义分区。

---

## 3. 修正后的 Engine Contract

`engine/repository_layout.py` 现在集中定义：

```text
CURRENT_CANONICAL_STORAGE_PATHS
```

它回答：

> 当前 Loader 应该到哪些 repository-relative paths 找 YAML？

它不回答：

> 这些 YAML 属于哪些知识类别？

未来可以传入任意经批准的 repository-relative storage paths，例如一个统一区域或技术分片；Loader 不要求目录名等于 `standard`、`relation`、`method` 等对象类别。

---

## 4. Semantic Identity 来自对象内容

修正前 Loader 允许通过：

```text
family == "relations"
```

辅助判断一个文档是不是 Relation。

修正后：

```yaml
type: relation
```

才是语义判断依据。

这意味着同一个物理目录可以同时存：

```text
Standard
Capability
Organization
Relation
Method
Design System
...
```

只要对象自身的数据合同可以明确表达身份。

目录不负责分类。

---

## 5. `_object_family` 被撤销

#25 第一版 Loader 会从物理目录注入：

```text
_object_family
```

#31 删除这一行为。

原因：这会让一个运行时“语义字段”来自文件夹，而不是对象数据，重新制造目录 = ontology 的耦合。

当前保留：

- `_physical_source`：真实 repository-relative 文件位置；
- `_source`：当前为了兼容既有 Renderer / generated path，仍与当前 physical source 相同。

---

## 6. Public URL 问题重新定义

#25 第一版用“保留 family-relative logical source”来模拟未来 `data/standards/...` 迁移后 URL 不变。

这个办法隐含了“未来仍有 standards/ 等 family folders”的假设，因此不能继续作为通用方案。

修正后明确：

> **未来真实移动 Canonical Data 之前，必须单独定义 public view route / generated URL 与 physical storage path 的解耦方式。**

可能依据 stable ID、显式 route、Renderer registry 或其他方案；现在不拍板。

本次修正只保证：**当前 layout 下现有 generated path 不变化。**

---

## 7. Storage Path 的安全边界

Canonical storage path 当前只接受 repository-relative path：

- 不允许绝对路径；
- 不允许 `..` 逃出 repository；
- 可以配置一个或多个路径；
- 目录内部可以递归扫描 YAML；
- future storage path 名称不需要与 object type 相同。

这样既保持可复现性，也不给未来目录方案预设 ontology。

---

## 8. 回归测试

#31 的新测试验证：

1. 当前 `standards/sample.yaml` 仍生成原来的 `standards/sample.md`，所以本次修正不改变当前 public behavior；
2. 一个任意命名的 `mixed/` 目录中可以同时放 Standard、Capability 和 Relation；
3. Relation 由 `type: relation` 被识别，而不是由目录名识别；
4. nested storage 可以被扫描；
5. storage path 不能逃出 repository；
6. 不再注入 `_object_family`。

---

## 9. 当前 Graph Baseline

#31 必须继续保持 #25 合并时的基线：

```text
objects:          112
relations:        107
resolved edges:   161
reference issues: 0
```

代表性 query 也必须不变：

```text
capability = automated_build_deployment
implementations = forgejo_actions, github_actions
open-source + self-hostable = forgejo_actions
```

---

## 10. Residual Coupling

修正后仍然明确存在：

1. Bootstrap workflow `paths:` 仍监听当前 legacy physical paths；
2. Pages workflow `paths:` 同样如此；
3. Renderer 目前的 public generated path 仍与 `_source` 有关系；
4. README / docs / 历史 Issue 里存在当前路径引用；
5. 真正 physical migration 还没有 current → target move table 和 rollback plan。

这些都必须在 Migration Dry Run 里处理。

---

## 11. #15 不再阻塞目录讨论

#15 继续研究：

```text
type / kind / roles / relations / evidence / assessment
```

但它不再决定：

```text
reference-projects/ 改成什么文件夹
是否建 methods/
是否建 precedents/
```

因为这些语义分类根本不应该通过文件夹表达。

所以 Repository Root / first-level layout discussion 可以现在继续，而 #15 可并行推进。

---

## 12. 这次修正没有做什么

没有：

- 移动任何 Canonical Data 文件；
- 修改任何 Schema；
- 修改 stable object IDs；
- 修改 Relation 语义；
- 改变当前 public generated path；
- 决定未来 root 一级目录；
- 决定 future Canonical storage zone 的名字或内部布局。

## 13. 下一步

下一步不是搬目录，而是重新讨论：

> **仓库根目录下面到底应该有哪些一级目录。**

讨论时先按“技术职责 / Artifact responsibility / 外部平台约束”来分，而不是按 Standard / Method / Precedent 等知识类别来分。
