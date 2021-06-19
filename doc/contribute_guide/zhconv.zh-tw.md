# 中文變體的協作要求

FGI 目前官方提供兩種中文變體的官方支援：

- 簡化字（中國大陸標準）
- 繁體字（臺灣標準）

FGI 儘可能地自動轉換各種變體到其他變體，試圖避免重複的翻譯工作。

FGI 的自動轉換基於 [Open Chinese Convert 開放中文轉換](https://github.com/BYVoid/OpenCC)

## 預設行為

FGI 的中文變體轉換由 `zhconv.py` 實現，最早的（也是現在預設的）行為是

1. 將簡體中文文件轉換為繁體中文，將其中的指向簡體版本的超連結改為指向繁體版本。

2. 根據遊戲頁面本地化 `games/l10n/zh-cn` 下的遊戲頁面自動生成 `games/l10n/zh-tw` 下的對應頁面。

這個行為有個缺陷，它總是優先使用簡體版本。有的遊戲頁面的中文最初是使用繁體編寫的，簡體轉換繁體因「一簡對多繁」和「一簡對多異」及「地區習慣用詞」問題，可能導致轉換後的結果與原文出現差異，因此需要對特定的遊戲頁面優先使用繁體。

現在 FGI 已經為遊戲頁面設計了一種解決方案，即 `X-Chinese-Convertor-Hint` 提示。但不適用於文件。

## X-Chinese-Convertor-Hint 提示

在遊戲頁面對應的 l10n yaml 檔案中（`games/l10n/zh-cn/*.yaml` 或 `games/l10n/zh-tw/*.yaml`），新增`X-Chinese-Convertor-Hint` 擴充套件，提示轉換器更改預設行為。

```
X-Chinese-Convertor-Hint:
  prefer: <PREFER>
```

PREFER 的取值如下：

- `CN`：預設行為，總是使用簡體版本生成繁體版本
- `TW`：總是使用繁體版本生成簡體版本
- `ignored`：忽略，這個遊戲頁面不進行中文變體轉換（這意味著變體要分別手動編輯）

值得注意的是，若多個 l10n yaml 變體中的 `X-Chinese-Convertor-Hint` 不同，優先採用簡體中文 yaml 檔案中的 `X-Chinese-Convertor-Hint` 提示。

當直接新增一個繁體版本的遊戲 l10n 頁面時，如 `games/l10n/zh-tw/NAME.yaml`，若不存在簡體頁面，將會使用此提示，通常將提示設定為 `prefer: TW`，這樣，第一次轉換出 `games/l10n/zh-cn/NAME.yaml` 的 `prefer` 仍然是 `TW`，即使第二次優先使用 `games/l10n/zh-cn/NAME.yaml` 的 `X-Chinese-Convertor-Hint`，也將會使用繁體版本生成簡體版本的策略。
