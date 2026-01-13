---
name: internal-comms
description: 一套资源，帮助我编写各种内部通信，使用我的公司喜欢使用的格式。每当要求编写某种内部通信时，Claude 应该使用此技能（状态报告、领导更新、3P 更新、公司通讯、常见问题解答、事件报告、项目更新等）。
license: Complete terms in LICENSE.txt
---

## 何时使用此技能
要编写内部通信，请使用此技能用于：
- 3P 更新（Progress、Plans、Problems）
- 公司通讯
- 常见问题解答回复
- 状态报告
- 领导更新
- 项目更新
- 事件报告

## 如何使用此技能

要编写任何内部通信：

1. **从请求中识别通信类型**
2. **从 `examples/` 目录加载相应的指南文件**：
    - `examples/3p-updates.md` - 用于 Progress/Plans/Problems 团队更新
    - `examples/company-newsletter.md` - 用于公司范围的通讯
    - `examples/faq-answers.md` - 用于回答常见问题
    - `examples/general-comms.md` - 用于任何其他不明确匹配上述之一的内容
3. **遵循该文件中的具体说明**，了解格式、语调和内容收集

如果通信类型不匹配任何现有指南，请要求澄清或更多关于所需格式的上下文。

## 关键词
3P 更新、公司通讯、公司通信、每周更新、常见问题解答、常见问题、更新、内部通信
