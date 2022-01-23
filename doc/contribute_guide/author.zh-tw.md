# 貢獻指南 - 作者

這是一篇介紹如何向 FurryGamesIndex（下文簡稱 FGI）添加或編輯作者信息的快速指南，目前處於草案試行階段。

在學習本指南的同時，可以檢視 [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors) 目錄下已有的資料檔案加深理解，或在修改、新增資料檔案的時候參考。

## 作者 ID

作者 ID 是用於引用作者的字串，並具有以下要求：

- 每位作者都有一個唯一的 ID 進行標識，ID 不可重複，且一旦 ID 確定，通常不再允許修改。
- 作者 ID 只能包含 ASCII 字符集中的英文（大小寫均可）、數字和下劃線。
- 作者 ID 不可以以一個 `_` 開頭，但可以以兩個或更多的 `_` 開頭。其他位置的下劃線數量沒有要求。

以下是定義作者 ID 的一般思路：

- 例如，如果作者的名字叫 `Rimentus` ，這是英文，我們直接使用 `Rimentus` 作為 ID。
- 例如，如果作者的名字叫 `とりあえず`，這是日文，但它有官方英文名稱或用戶名，因此 `toriaezu13` 是作者 ID。否則我們可能使用其羅馬音 `toriaezu` 作為 ID。
- 例如，如果作者的名字叫 `Black Sun Di`，它有空格，我們將空格替換為下劃線，即 `Black_Sun_Di` 是作者 ID。

## 作者資料檔案

FGI 網站上顯示的每位作者都是由來自 FGI 作者資料庫中的資料檔案進行加工製成的。 FGI 作者資料檔案存放的位置是 [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors) 子目錄。

要編輯現有作者頁資料檔案，只需要找到對應的資料檔案進行編輯。要創建一個新的作者頁面，則需要創建一個新的作者資料檔案。資料檔案的檔名為

```
<作者ID>.yaml
```

例如，作者 “The Echo Project”（回音製作組）對應的資料檔案為 `The_Echo_Project.yaml`。

在編輯作者資料檔案時，需特別注意內容編寫是否符合 YAML 格式規範，否則 FGI 將無法正常利用此檔案。

> 作者資料檔案需要使用 UNIX（LF）換行符，否則 FGI 可能無法按照預期工作。
>
> 此倉庫已使用 `.gitattributes` 要求 git 使用 LF 換行符，標準的 git 軟體通常可以正常工作。

下面將介紹作者資料檔案的各個部分。

### 資料檔案排版

為了增強資料檔案的易讀性，必須在每個一級屬性（最後一個可加可不加）後插入一個空行。

例如

```

name: Black Sun Di

aliases:
  - Bieas

type: personal

avatar: Black_Sun_Di.jpg

links:
  - name: .furaffinity
    uri: furaffinity:blacksundi

```

此外，要注意下面語法中用於縮排的空格，空格的位置和個數必須完全符合定義。

### 名稱

```
name: 作者名
```

作者名稱使用與作者ID相同的正式名稱，但包含空格時不用下劃線替換。

### 別名

```
aliases:
  - 別名1
  - 別名2
  ...
```

一位作者可能有多個名稱。別名是指除了 `name` 之外的作者名，同樣可被 FGI 檢索。

### 作者類型

```
type: personal
```

作者類型提供以下選項：

- `unknown`: 未知
- `personal`: 個人
- `small-team`: 獨立遊戲團隊
- `company`: 公司
- `publisher`: 發行商

例如《Echo》遊戲的其中一位作者 The Echo Project 為開發團隊，那麼此處應填入 `small-team`。

### 作者頭像

作者頭像通過檔名進行內部引用

將需要引用的圖片放置於 assets/_avatar/ 目錄下，然後在資源引用處直接填寫檔名。

例如，將 Black_Sun_Di.jpg 放置到 assets/_avatar/，然後在 Black_Sun_Di.yaml 中可以引用此圖片，如下：

```
avatar: Black_Sun_Di.jpg
```

#### 圖片資源檔案規範

FGI 對作者頭像有著明確的規定，在規格上，圖片的長和寬統一為 64px。盡量製作或選用大於此規格的圖片，並對其裁剪和縮小尺寸。

出於效能考慮，在與100%質量原圖比較未有明顯失真的條件下，檔案大小不得超過 10KiB，且在與原圖視覺效果相近的情況下優先上傳更小的檔案。

### 連結

```
links:
  - name: 名稱
    uri: URI
  - name: 名稱
    icon: 圖標（可選）
    uri: URI
  - ...
```

連結為 FGI 最終的作者頁面建立超連結，我們通常在這裡寫上作者在各個網站上的用戶主頁以便玩家可以快速了解作者動向。可以添加作者的社交平台、作者的 Patreon 等等。

名稱為連結的名稱，URI 通俗地說是該連結的“網址”，如果你不清楚 URI 的意思，也無需在意。

#### 名稱

FGI 設計了一種叫 “庫存連結”（Stock Link）的東西減少翻譯的工作量。庫存連結名稱以 `.` 開頭。它們是固定的，需要在 [`uil10n`](https://github.com/FurryGamesIndex/games/tree/master/uil10n) 檔案中定義。

作者檔案下的庫存連結可包含以下幾個：

- `.website`: 官方網站
- `.twitter`: 官方 Twitter
- `.furaffinity`: 官方 FurAffinity
- `.deviantart`: 官方 DeviantART
- `.patreon`: 官方 Patreon
- `.weibo`: 官方微博
- `.tumblr`: 官方 Tumblr
- `.pixiv`: 官方 Pixiv
- `.discord`: 官方 Discord
- `.youtube`: 官方 Youtube
- `.facebook`: 官方 Facebook

當你使用庫存連結時，你就無需寫這麼一段長字，而且無需為每種語言寫一份，因為庫存連結是固定的，每種語言都可以自動處理。

存在符合要求的庫存連結時，必須使用庫存連結。

如果確實需要非庫存連結，則名稱部分直接寫就可以了，注意這裡我們要使用英文。例如：

```
  - name: WildDream
    uri: https://www.wilddream.net/user/balabala
```

#### URI

URI 部分可能是一個網址或 URL，比如上面的“在 YouTube 平台上獲取”連結上，我們應該跳轉打開該作者的 youtube 用戶主頁，因此我們填寫 `https://www.youtube.com/c/MightAndDelight`

同時，部分連結可以簡寫成我們定義的 URI 形式，推薦使用但並非強制

- Steam: `steam:ID` 比如 `steam:570840`，相當於 `https://store.steampowered.com/app/570840`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相當於 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:用戶名` 比如 `patreon:EchoGame`，相當於 `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:用戶名` 比如 `tumblr:xxx`，相當於 `https://xxx.tumblr.com/`
- pixiv: `pixiv:用戶ID` 比如 `pixiv:123456`，相當於 `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:用戶名`, 相當於 `https://www.furaffinity.net/user/用戶名/`
- DeviantART: `deviantart:用戶名`, 相當於 `https://www.deviantart.com/用戶名`
- FGI misc page: `FGI-misc-page:name` 相當於 `<相對路徑引用網站根目錄>/misc/name.html`，這些頁面是由 FGI 倉庫中的 [`misc-pages`](https://github.com/FurryGamesIndex/games/tree/master/misc-pages) 子目錄下的檔案生成的。
