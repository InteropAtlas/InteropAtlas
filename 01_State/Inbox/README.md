# Inbox

`Inbox/` 是 InteropAtlas 的非正式收入工作区（intake workspace）。它不属于编号的 Canonical 主入口，也不代表已经正式收入项目知识图谱。

## 什么时候应该进入 Inbox

任何准备新增到 InteropAtlas、但尚未完成正式验证和接纳流程的内容，默认先进入 `Inbox/`，而不是直接写入 `01_Objects/` 或 `02_Relations/`。

典型情况包括：

- 新发现的标准、协议、实现、组织、方法或其他候选对象；
- 尚未完成身份确认、判重、来源核验或语义检查的对象；
- 尚未完成关系验证的新 Relation 候选；
- 需要进一步研究、人工审核或 Authority Gate 的收入请求。

## 当前结构

```text
Inbox/
├── candidates/          候选对象池
├── acceptance-events/   审核 / 接纳决策记录与合同
└── README.md             本说明
```

### `candidates/`

用于保存尚未正式进入 Canonical State 的候选对象。候选进入这里后，可以继续做机器验证、研究、判重、身份审查、语义审核和接纳判断。

### `acceptance-events/`

用于保存候选经过审核后的结构化决策证据，例如：接受、判定重复、延期、要求身份审查等。它记录“为什么发生这个决定”，但本身不是正式 Canonical 对象库。

## 什么时候可以进入正式 State

内容只有在满足当前适用的 intake / validation / review / authority 规则后，才能从 Inbox 进入正式 `01_Objects/` 或 `02_Relations/`。

至少应确认：

- 身份与稳定 ID 已明确；
- 必要来源与 Provenance 已具备；
- Schema / machine validation 通过；
- 需要的语义审核、判重和 Authority Gate 已完成；
- 没有未解决的 identity risk、duplicate risk 或其他阻塞条件。

机器检查通过本身不等于完成正式接纳；如果当前规则要求独立语义审核或更高 Authority Gate，仍必须完成对应步骤。

## 给维护者和 Agent 的默认行为

当你不确定一个新内容是否已经具备正式收入资格时：

> **默认放进 `Inbox/`，不要直接写入编号的 Canonical 目录。**

只有能够明确证明其已经满足正式接纳条件时，才应直接修改 `01_Objects/` 或 `02_Relations/`。

`Inbox/` 的目的不是增加一道形式流程，而是防止未经验证的内容与当前正式 State 混在一起，同时保留一条清楚、可审计的收入路径。