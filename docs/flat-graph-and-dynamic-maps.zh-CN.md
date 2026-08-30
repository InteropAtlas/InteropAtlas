# 扁平图谱与动态 Map 方法

> 状态：Architecture Principle（架构原则），Pre-Alpha。当前用于指导数据建模，不冻结底层存储与前端实现。

InteropAtlas 不应依赖一棵深层、唯一、固定的分类树来组织全部知识。更适合当前项目方向的方法是：

> **Flat Objects（扁平对象） + Rich Relations（丰富关系） + Dynamic Maps（动态地图）**

也可以表达为：

> **底层对象尽量扁平，关系尽量丰富；层级和导航主要由 View（视图）与 Map（地图）动态产生。**

## 1. 为什么不采用单一深层树结构

标准、协议、能力、组织、实现、场景和缺口通常同时属于多个领域和语境。例如 WebRTC 可以同时与视频通信、实时通信、浏览器、媒体、安全、网络传输和 Agent 场景有关。

如果强制每个对象只能进入唯一层级，就会不断遇到“它到底应该放在哪个目录”的问题，并把分类决策错误地变成事实本身。

因此，InteropAtlas 的核心事实层优先保存稳定对象和明确关系，而不是保存唯一目录位置。

## 2. Map 是视图，不是事实源

Map（地图）可以是人工定义、规则生成或 Engine（分析引擎）动态计算得到的导航视图。

例如：

- 视频传输 Map
- Agent 通信 Map
- 开放标准 Map
- 机器人互操作 Map
- 低延迟通信 Map
- 没有开放替代方案 Map
- InteropAtlas 自身技术栈 Map

同一个对象可以同时出现在多张 Map 中，而对象本身仍然只有一个稳定 ID。

未来可能的结构：

```text
Facts + Relations
      ↓
   Engine
      ↓
Query / Filter / Workflow
      ↓
Dynamic Map / List / Table / API
```

因此不应让前端图形结构反向决定事实数据结构。

## 3. 与成熟标准和既有方法的关系

这个方向并非完全自创。InteropAtlas 可以参考并兼容以下成熟知识组织方法，但目前不直接绑定其中任何一种实现。

### SKOS（Simple Knowledge Organization System，简单知识组织系统）

W3C SKOS 提供 `Concept（概念）`、`ConceptScheme（概念方案）` 以及 `broader（更宽泛）`、`narrower（更具体）`、`related（相关）` 等语义关系。

值得借鉴：

- 一个概念可以进入 Concept Scheme，而不是必须被固定到唯一目录；
- 区分层级关系和关联关系；
- 不把所有关系都压缩成父子树；
- 可以把不同知识组织体系作为不同 Concept Scheme 共存。

InteropAtlas 后续可考虑把部分 `Capability（能力）`、领域词汇和分类体系映射到 SKOS，但不应把所有对象都强制建模为 SKOS Concept。

### RDF（Resource Description Framework，资源描述框架）

RDF 使用 `subject–predicate–object（主语–谓语–宾语）` 三元组构成图。

值得借鉴：

- 对象与关系天然组成图；
- 数据模型和具体展示解耦；
- 同一事实可以被不同查询、视图和上层语义模型重复使用；
- 后续可以从 YAML 事实源导出 RDF，而不要求今天就把仓库改成 RDF。

InteropAtlas 当前 `source + relation + target` 的 Relation 模型与 RDF 三元组在思想上高度兼容，但 Relation 仍允许附加证据、条件、场景和置信度等上下文。

### Topic Maps（主题地图，ISO/IEC 13250）

Topic Maps 标准允许表达 Topic（主题）、Association（关联）、Occurrence（相关信息资源）以及 Scope（作用域）。

值得借鉴：

- 同一对象可以存在多种关联；
- 关联可以具有 Role（角色）；
- Scope（作用域）可以限定某个关系在什么上下文中成立或相关；
- Topic Map 本身更接近“知识导航地图”而不是文件目录。

这与 InteropAtlas 的 `scenario_context`、`capability_context` 和未来动态 Map 很接近。后续可以研究是否借用 Scope / Role 的概念完善 Relation 模型。

## 4. 当前采用原则

现阶段采用“概念兼容、实现不绑定”的策略：

1. 保持 YAML + JSON Schema 作为当前事实源；
2. 保持稳定 Object ID；
3. Relation 作为一等对象；
4. 不要求对象拥有唯一父节点；
5. 分类信息允许多值；
6. Map / View 可以动态产生；
7. 后续支持导出到 RDF / SKOS 或其他图模型；
8. 遇到成熟标准已有合适语义时优先映射或复用，不重新发明等价概念；
9. 仅当成熟标准不足以表达 InteropAtlas 特有语义时，再定义项目自己的扩展关系。

## 5. 目前不决定的事情

当前不决定：

- 是否使用图数据库；
- 是否以 RDF 作为内部主存储；
- 是否采用某个具体知识图谱前端；
- Map 是否需要独立持久化对象；
- 是否完整采用 SKOS Ontology（本体）；
- 是否实现 ISO Topic Maps 数据模型。

这些问题应该等真实数据量、查询需求和 Engine 工作流逐步出现后再决定。

## 核心原则

> **InteropAtlas 的结构应该由关系产生，而不是由目录强行规定。**

> **Map 是对同一张底层事实图的不同观察方式，而不是另一份互相竞争的数据。**
