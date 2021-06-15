# 提交補丁的注意事項

當透過 Github Pull request 提交補丁時，建議儘可能得使一個 pull requst 儘可能的小，涉及面儘可能窄。例如編輯遊戲資料檔案的 pull request 中不應該修改文件、模板、樣式表或程式碼（修改標籤定義檔案是可以容忍的），新增遊戲資料檔案時也不要同時新增多個完全不相關的遊戲。

我們要求在 git 中**最終**記錄的 commits 訊息符合以下格式。

```
[標識] 元件或範圍: 子元件: 摘要 (引用)
```

在大多數情況下，不使用 `[標識]`，`子元件:` 和 `(引用)`（或其中幾部分），`元件或範圍:` 和 `摘要` 是不可省略的。即訊息的格式很可能為

```
元件或範圍: 摘要
```

**您可以在 pull request 的提交中使用混亂的提交格式，因為在這種情況下維護者會採用壓縮合並，使其變為一條提交，然後維護者會為您編寫一個合適的 commits 訊息。** 這主要是便於那些直接在 Github 網頁上編輯的貢獻者。但是如果您的一個 pull request 中修改了 FGI 中互不相關的幾個部分，當維護者認為難以編寫提交訊息時，維護者可能要求您整理您的修改並重新發起 pull request。

> 如果 pull request 中每個提交都符合此要求，維護者應該首選採用預設的合併方式（類似於 git 的非快進合併）。以便修改記錄儘可能詳細。

這就是為什麼您的 pull request 應該儘可能小的原因。

**如果您確實希望同時修改多個部分，則我們強烈建議您同時提交多個 pull request（您需要在 fork 後的倉庫中建立多個分支）。**

本文中的所有做法都是為了儘可能使提交歷史記錄具體、便於搜尋，為審查工作提供便利。

以下是一些如果編寫提交訊息的例子：

## 核心部分

除非另有說明，`元件或範圍: ` 使用檔案路徑。不帶副檔名。

### 遊戲和作者

新增 Adastra 遊戲：

> 可同時新增遊戲縮圖等資源，無需在訊息中體現這一點。

```
games/Adastra: new game
```

新增 The Echo Project 作者：

> 可同時新增作者頭像圖片檔案，無需在訊息中體現這一點。

```
authors/The_Echo_Project: new author
```

更新 Adastra 遊戲的標籤和連結：

```
games/Adastra: update tags and links
```

更新 Adastra 遊戲額中文字地化補丁連結：

```
games/Adastra: update link of chinese l10n patch
```

更新 Adastra 遊戲的縮圖

> 除非是僅更新遊戲的縮圖，否則我們反而建議將更新圖片和更新資料檔案合併到一個提交，提交資訊可以體現更新了縮圖。

```
assets/Adastra: update thumbnail.jpg
assets/_avatar/The_Echo_Project: update avatar
```

更新多個遊戲資料檔案時：

```
games: update author info for 3 games from Echo Project
games: remove deprecated property sensitive_media for all entities
```

更新 Adastra 條目的翻譯資料檔案（不體現語言的變體）：

```
games/l10n/zh: Adastra: update translation for description
```

更新 Adastra 條目的翻譯資料檔案，涉及到 `X-Chinese-Convertor-Hint` 變體相關的屬性時，應指定變體：

```
games/l10n/zh-tw: Adastra: set X-Chinese-Convertor-Hint
```

更新多個遊戲條目的翻譯資料檔案：

```
games/l10n/zh: add description-format for all entries
```

### 程式碼

對程式碼修改時，當一個模組包含多個類時，且只對其中一個類進行修改時，可以使用 `子元件: ` 指定類的名字。

```
fgi/game: GameDescription: initial brief-description support
test/tagmgr: update unit test case
scripts/build-next: do not use uimod plugin
```

例外1: 對於外掛程式碼（fgi/plugins/...），`元件或範圍: ` 中應刪除 `fgi/` 前輟，剩餘部分遵守檔案路徑。

```
plugins/steam-cdn-unite: add new akamai CDN URI prefix
```

例外2：對於渲染器程式碼（fgi/renderers/...）`元件或範圍: ` 中應刪除 `fgi/` 前輟，剩餘部分遵守檔案路徑。

> 歷史上，`fgi/renderers/` 目錄曾經是 `renderers/`，此要求保證了格式與歷史訊息格式相同。

```
renderers/list: initial multi-klass support
```

### 模板和樣式表

```
templates: fixup xxx bug
```

```
templates/list: use list_item widget
```

```
templates/peafowl-private/header: fixup opengraph description escape
```

樣式表文件雖然存放於 `webroot/styles/`，但 `元件或範圍: ` 中應刪除 `webroot/` 前輟，剩餘部分遵守檔案路徑。

```
styles/32_game_entry: add workarounds for Mozilla Firefox
```

### Webroot

例外1: webroot/base/ 下的檔案，`元件或範圍: ` 中應將 `webroot/base/` 前輟改為 `webroot/`，剩餘部分遵守檔案路徑。

> 歷史上，`webroot/base/` 目錄曾經是 `webroot/`，此要求保證了格式與歷史訊息格式相同。

```
webroot/robots: disallow /classic-ui
webroot/scripts/searchexpr: initial @reverse and @lastmod support
```

例外2: service worker 檔案直接使用 `sw: ` 作為 `元件或範圍: `。

```
sw: proactive opaque cache avoiding
```

### UI l10n 資原始檔

檔案路徑中不體現語言變體。

```
uil10n/zh: add translation for ...
uil10n/zh: add translation for many keys
```

但是，如果修改 `_PRIVATE.yaml` 後輟的檔案，應指定語言變體。同時使用 `PRIVATE: ` 作為 `子元件`。

```
uil10n/zh-tw: PRIVATE: add hotfix for list-klass-platform-mobile
```

### 文件

```
doc/search_help: add more exampless
```

### staging-ui 和 classic-ui

如果修改 `staging-ui` 和 `classic-ui` 下的檔案，則應該使用 `staging-ui: ` 或者 `classic-ui/UI包代號: ` 作為 `元件或範圍: `，同時使用剩餘的檔名部分作為 `子元件`。

```
staging-ui: styles/32_game_entry: add workarounds for Mozilla Firefox
classic-ui/pioneer: templates/pioneer-private/header: fixup build
```

### git 子模組

> 這種情況下永不使用 `子元件:`

透過 git 子模組（git submodule）引入的元件的提交訊息是非常形式化的。只有以下兩種情況。

被 FGI 組織正式維護的倉庫，使用以下提交訊息表明更新到最新版本。

```
icons: bump to lastest version
```

由第三方維護的倉庫，使用以下提交訊息表明更新到上游某一版本，`master` 可以替換為大部分的 git 引用，可以是分支名、標籤或 commmit hash，但不能是 HEAD 等。

```
some_thirdparty/some_submodule: bump to upstream master
```

### 全樹範圍

全樹範圍（`treewide`）表示修改覆蓋了整個原始碼樹，通常是和具體元件不太相關的修改。

> 這種情況下永不使用 `子元件:`

例如如下的修復檔案換行符號或執行中文轉換器的提交：

```
treewide: fixup line endings
treewide: run zhconv
```

## 標識

目前 FGI 只有一種標識，`[DO NOT MERGE]`。

### `[DO NOT MERGE]` 標識

`[DO NOT MERGE]` 宣告此提交不提交到主分支，且不應該被合併到主分支。

例如如下的訊息，在 FGI-next 構建中禁用隱私政策的 hack：

```
[DO NOT MERGE] next: renderers/nonl10n/singles: disable privacy-policy page
```

## 引用

引用為查詢和此補丁修改內容的相關地址，以便於審查者透過這些連結找到和此修改的更多原因和其他資訊。如 `PR #數字` 引用 pull request，`Fixed #數字` 引用相關的 issues。

以下是一些例子：

```
games/Adastra: new game (PR #23333)
games/Adastra: use stock link for chinese patch (PR #23335, Fixed #23334)
games/Adastra: use stock link for chinese patch (Fixed #23334)
```

## 例外情況

有幾種例外情況是不需要（完全）符合此格式。

1. 使用 `git revert` 撤銷提交時，使用預設的 `Revert "..."` 格式。`"..."` 需要符合本文規定的格式或（遞迴地符合）此例外情況。

2. 使用 `git merge --no-ff` 或 github 預設的 pull request 合併方式時，使用預設的 `Merge ...` 格式

	不允許非必要的 `Merge ...` 合併訊息。如果您的程式碼庫需要更新時，建議首選 `git pull --rebase`。
	
	如果有此類提交，維護者可能會採用壓縮合並並重新編寫提交訊息。
