# Implementations（实现）

本目录记录把能力、标准、协议或规范真正落地为可运行软件、服务、硬件或平台能力的对象。

## 为什么单独建这一层

InteropAtlas 需要严格区分：

- Capability：需要完成什么；
- Standard / Specification：共同遵循什么规则；
- Implementation：什么真实对象把能力或规范实现出来；
- Organization：谁治理、维护或提供这些对象。

Implementation 不等于 Open Standard。一个实现可以是开源软件、闭源产品、托管服务、平台服务、硬件或参考实现。

## 当前最小分类

`kind` 当前支持：

- software
- library
- tool
- service
- platform_service
- hardware
- firmware
- reference_implementation

这只是当前实践所需的最小模型。只有真实场景证明不足时再继续扩充。

## Platform 暂不独立成对象类型

现阶段先使用 `implementation.kind: platform_service` 表达 GitHub Actions 这类平台能力。

如果后续出现大量需要表达“平台包含多个服务、统一身份、计费、托管、扩展市场、运行环境”等平台级关系的场景，再评估独立 `platform` 对象类型。
