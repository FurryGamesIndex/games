# 中文变体的协作要求

FGI 目前官方提供两种中文变体的官方支持：

- 简化字（中国大陆标准）
- 繁体字（臺灣標準）

FGI 尽可能地自动转换各种变体到其他变体，试图避免重复的翻译工作。

FGI 的自动转换基于 [Open Chinese Convert 開放中文轉換](https://github.com/BYVoid/OpenCC)

## 默认行为

FGI 的中文变体转换由 `zhconv.py` 实现，最早的（也是现在默认的）行为是

1. 将简体中文文档转换为繁体中文，将其中的指向简体版本的超链接改为指向繁体版本。

2. 根据游戏页面本地化 `games/l10n/zh-cn` 下的游戏页面自动生成 `games/l10n/zh-tw` 下的对应页面。

这个行为有个缺陷，它总是优先使用简体版本。有的游戏页面的中文最初是使用繁体编写的，简体转换繁体因「一簡對多繁」和「一簡對多異」及「地區習慣用詞」问题，可能导致转换后的结果与原文出现差异，因此需要对特定的游戏页面优先使用繁体。

现在 FGI 已经为游戏页面设计了一种解决方案，即 `X-Chinese-Convertor-Hint` 提示。但不适用于文档。

## X-Chinese-Convertor-Hint 提示

在游戏页面对应的 l10n yaml 文件中（`games/l10n/zh-cn/*.yaml` 或 `games/l10n/zh-tw/*.yaml`），添加`X-Chinese-Convertor-Hint` 扩展，提示转换器更改默认行为。

```
X-Chinese-Convertor-Hint:
  prefer: <PREFER>
```

PREFER 的取值如下：

- `CN`：默认行为，总是使用简体版本生成繁体版本
- `TW`：总是使用繁体版本生成简体版本
- `ignored`：忽略，这个游戏页面不进行中文变体转换（这意味着变体要分别手动编辑）

值得注意的是，若多个 l10n yaml 变体中的 `X-Chinese-Convertor-Hint` 不同，优先采用简体中文 yaml 文件中的 `X-Chinese-Convertor-Hint` 提示。

当直接添加一个繁体版本的游戏 l10n 页面时，如 `games/l10n/zh-tw/NAME.yaml`，若不存在简体页面，将会使用此提示，通常将提示设置为 `prefer: TW`，这样，第一次转换出 `games/l10n/zh-cn/NAME.yaml` 的 `prefer` 仍然是 `TW`，即使第二次优先使用 `games/l10n/zh-cn/NAME.yaml` 的 `X-Chinese-Convertor-Hint`，也将会使用繁体版本生成简体版本的策略。
