# 03_Evolution

`03_Evolution` 是 InteropAtlas 三个核心一级目录之一。

它承载项目**如何观察自己、学习、验证、决策并改变自己**的内容。

```text
03_Evolution/
├── 01_Research/      为什么这样判断
├── 02_Experiments/   我们怎样试过 / 验证过
├── 03_Change/        接下来怎样改变 / 过去怎样迁移
└── README.md
```

- [`01_Research/`](01_Research/)：研究、Prior Art、Reference、Fit Test、Gap、Audit、Verification、方案比较；
- [`02_Experiments/`](02_Experiments/)：原型、试运行、Dry Run、可复现实验、fixture 与实验结果；
- [`03_Change/`](03_Change/)：Roadmap、Route、Phase Plan、Proposal、Decision、Migration、Deprecation / Transition、Future Direction 与必要的演化历史。

## 与 `docs/` 的区别

`docs/` 是当前项目正式文档入口：保存新的贡献者今天为了正确理解和参与项目而需要阅读的 Definition、Architecture、Specification、Profile、Policy、Operating Model 与长期规则。

`03_Evolution` 保存形成这些当前状态的过程，以及项目下一步如何变化。

可以记成：

```text
docs/
    现在应该相信 / 遵守 / 理解什么

03_Evolution/01_Research/
    为什么这样判断

03_Evolution/02_Experiments/
    我们怎样试过 / 验证过

03_Evolution/03_Change/
    接下来怎样改变
```

## 生命周期原则

一项 Research / Experiment / Change 的结果如果被正式采用，应根据其性质进入：

- `01_State` — 成为项目当前正式承认的数据 / 合同；
- `02_Runtime` — 成为当前运行实现；
- `docs/` — 成为当前需要人类 / Agent 理解或遵守的项目规则与说明。

Evolution 可以继续保存形成该结果的依据、实验和迁移历史，但不应让历史过程材料冒充当前事实或当前规范。
