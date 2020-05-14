# 貢獻指南

這是一篇介紹如何向 FurryGamesIndex (下文中可能簡稱 FGI) 新增遊戲的指導，但是如果你想維護現有遊戲，你也可以在這篇指導中學會方法。

在 FurryGamesIndex 上新增和維護遊戲真的非常簡單，只需要花費幾分鐘的時間瞭解。

## 第一步：收集遊戲資訊

你需要透過網際網路搜尋或遊玩遊戲來找到這些資訊。注意，在使用資訊時請勿使用版權材料，除非在合理使用的前提下（例如複製遊戲簡介、公開圖片和有限的截圖）。

- 遊戲的名字
- 遊戲的描述（官方公開描述或自己編寫）
- 遊戲是誰開發的？
- 縮圖和截圖
- 獲取遊戲的連結
- 遊戲作者的網站、社交平臺和 Patreon 等

## 第二步：命名遊戲 ID

> 如果你要維護遊戲而不是新增遊戲，可以跳過本節

我們已經有了遊戲的名字，為什麼還需要定義一個 ID？這是由於，本專案要求每個遊戲都要有一個唯一的 ID 進行標識，遊戲 ID 只能包含英文、數字和下劃線。

- 例如，你找到了一個叫 `Adastra` 的遊戲，這是英文，我們直接使用 `Adastra` 作為 ID
- 例如，你找到了一個叫 `バカ部` 的遊戲，這是日文，首先確定是否存在官方英文名，如果不存在，應使用其羅馬字母表示。因此我們使用 `Bakabu` 作為 ID
- 例如，你找到了一個叫 `家有大貓` 的遊戲，這是中文，但它有官方英文名稱 `Nekojishi`，因此 `Nekojishi` 是遊戲 ID。否則我們可能使用其拼音 `JiaYouDaMao` 作為 ID。
- 例如，你找到了一個叫 `After Class` 的遊戲，它有空格，我們將空格替換為下劃線，即 `After_Class` 是遊戲 ID。

## 第三步：建立遊戲描述檔案

> 如果你要維護遊戲而不是新增遊戲，可以跳過本節

終於，我們開始了激動人心的部分。我們要建立 YAML 檔案來描述這個遊戲了！別被 YAML（YAML Ain't Markup Language）的名字嚇到，這是一種很易於獸人和人類直接編輯的格式。如果你只是為本專案貢獻，你甚至都可以不瞭解 YAML 的語法（當然瞭解一下基本語法會更好）！我們接下來會學習如何編輯遊戲描述檔案。

你要建立一個空白檔案，命名為 `遊戲ID.yaml`，`遊戲ID` 就是你上一步中命名的遊戲 ID。

> 如果你使用的 Windows，你可以在資料夾中右鍵-新建-文字文件，並將其改名為 `xxx.yaml`，注意你必須將副檔名 `.txt` 部分移除，最後的檔名需要是 `xxx.yaml` 而不能是 `xxx.yaml.txt`

## 第四步：編輯遊戲描述檔案

這裡首先給出 `Adastra` 遊戲的一個樣板描述檔案。看到這個模板（[效果演示](https://furrygamesindex.github.io/zh-cn/games/Adastra.html)），你可能已經對遊戲描述檔案有一個基本瞭解了，即使你仍然不明白，也沒有關係，因為接下來，我會給你介紹每一部分的含義和寫法。

```
name: Adastra

description: |
  You're having the time of your life in Rome on a study abroad program when you're suddenly abducted by an alien. What does he want from you? Well, he doesn't seem to want to tell and, before you know it, you're millions of miles away from Earth on your way to a place you know nothing about.
  Adastra is a romance visual novel with a whole bunch of sci-fi and political intrigue mixed in. You'll experience the perils of navigating an empire in turmoil while deciding who you should and who you definitely shouldn't trust.
  In this climate of turncoats and backstabbers, you start to wonder if the alien that abducted you is the one person you can trust the most.

tags:
  author:
    - 'The Echo Project'
  type:
    - visual-novel
    - bara
    - yiff
  male:
    - canine
    - felidae
    - wolf
    - cat
    - humankind
    - muscle
    - anal
    - human-on-furry
  misc:
    - freeware
    - uncensored
    - engine-renpy
    - multiple-endings
    - work-in-process
  lang:
    - en
    - zh-unoffical
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android

links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
  - name: .patreon
    uri: patreon:EchoGame
  - name: .twitter
    uri: twitter:EchoTheVN 
  - name: Unoffical chinese mod
    uri: https://weibo.com/7429628292/J16RMawmi

thumbnail: thumbnail.jpg

screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

### 名稱

```
name: Adastra
```

名稱部分是 `name: 遊戲名稱`，如果遊戲有官方英文，應寫英文名稱。（和遊戲ID不同，空格不轉換為下劃線）。我們會在後面介紹國際化機制，在哪裡輸入其他語言。

如果遊戲沒有官方英文名稱，則名稱推薦寫為 `遊戲ID / 原名`。比如 `バカ部` 可以設定為 `Bakabu / バカ部`。

### 描述

```
description: |
  第一行描述
  第二行描述
  ...

```

描述部分的格式如上。第一行是固定不變的 `description: |`，換行開始編寫描述，描述的每一行都要以兩個空格開頭。

### 標籤

```
tags:
  author:
    - 'The Echo Project'
  type:
    - visual-novel
    - bara
    - yiff
  male:
    - canine
    - felidae
    - wolf
    - cat
    - humankind
    - muscle
    - anal
    - human-on-furry
  misc:
    - freeware
    - uncensored
    - engine-renpy
    - multiple-endings
    - work-in-process
  lang:
    - en
    - zh-unoffical
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android
```

標籤是描述遊戲的特性。在 FGI 中，標籤由“名稱空間”和“值”組成。並且必須使用標準化的標籤。如 `type:visual-novel` 中，名稱空間是冒號前面的 `type`，後面的是值 `visual-novel`。這個標籤表示該遊戲的「型別」是「視覺小說」。同樣 `male:canine` 表示該遊戲存在主要「男性」角色是「犬科獸人」，`misc:work-in-process` 表示該遊戲「未完成」，正在開發中（但釋出了先行體驗/Demo版本），`platform:android` 表示該遊戲可以在「Android」「平臺」上執行。有關目前所有標準標籤，見 [標籤](tags.zh-cn.md)。

標籤不帶空格，除了一個例外，就是 `author` 名稱空間下的標籤。`author` 名稱空間指示作品的作者（開發者、發行者等）。如果包含空格，需要使用單引號`'`包裹起來。

tags 列表的格式第一行是固定的 `tags:`，然後包含多個名稱空間部分，每個名稱空間部分的第一行是 <code>&nbsp;&nbsp;名稱空間:</code>（以兩個空格開頭）

```
tags:
  第一個名稱空間:
  第二個名稱空間:
  ...
```

在每一個名稱空間中，之後的每一行格式是 <code>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;值</code>（以四個空格+一個`-`+一個空格開頭）

```
tags:
  第一個名稱空間:
    - 值1
    - 值2
    - 值3
  第二個名稱空間:
    - 值1
    - ...
  ...
```

### 連結

```
links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
  - name: .patreon
    uri: patreon:EchoGame
  - name: .twitter
    uri: twitter:EchoTheVN 
  - name: Unoffical chinese mod
    uri: https://weibo.com/7429628292/J16RMawmi
```

連結為 FGI 最終的遊戲頁面上建立超連結，我們通常將遊戲的釋出地址、作者的網站、作者的社交平臺、作者的 Patreon 等等作為連結以便讓玩家可以快速找到需要的遊戲。

連結的第一行是固定的 `links:`，然後包含多個塊。

```
  - name: 名稱
    uri: URI
```

> 請注意每行前面的空格

名稱為連結的名稱，URI 通俗地說是該連結的“網址”，如果你不清楚 URI 的意思，也無需在意。

但是，需要注意的是，FGI 設計了一種叫“庫存連結”（Stock Link）的東西減少翻譯的工作量。庫存連結名稱以 `.` 開頭。它們是固定的，不能自行定義（如果你覺得應該增加新的，可以發 issue/PR 討論）

FGI 支援的庫存連結包括以下幾個

- `.website`: 作者的官方網站
- `.itch.io`: 在 itch.io 平臺上獲取
- `.steam`: 在 Steam 平臺上獲取
- `.patreon`: 在 Patreon 平臺上贊助作者
- `.twitter`: 作者的 Twitter

當你使用庫存連結時，你就無需寫這麼一段長字，而且無需為每種語言寫一份，因為庫存連結是固定的，每種語言都可以自動處理。

如果確實需要非庫存連結，則名稱部分直接寫就可以了，注意這裡我們要使用英文（然後可能還需要再在它處寫其他語言的名稱）比如本例的 <code>&nbsp;&nbsp;- name: Unoffical chinese mod</code>，是建立一個指向非官方中文補丁的連結。

URI 部分可能是一個網址或 URL，比如上面的“在 itch.io 平臺上獲取”連結上，我們應該跳轉開啟該遊戲的 itch.io 網頁，因此我們填寫 `https://echoproject.itch.io/adastra`

同時，部分連結可以簡寫成我們定義的 URI 形式，推薦使用但並非強制

- Steam 平臺: `steam:ID` 比如 `steam:570840`，相當於 `https://store.steampowered.com/app/570840`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相當於 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:使用者名稱` 比如 `patreon:EchoGame`，相當於 `https://www.patreon.com/EchoGame`

### 縮圖

縮圖是遊戲的品牌圖示，不推薦超過 400x400 畫素。準備好一個 jpeg 或 png 圖片。我們使用 `thumbnail: 檔名` 指示該縮圖。

```
thumbnail: thumbnail.jpg
```

### 遊戲截圖

最後是遊戲截圖部分，第一行是固定的 `screenshots:`，隨後每一行以 <code>&nbsp;&nbsp;-&nbsp;</code> 開頭（兩個空格+一個`-`+一個空格），然後是圖片的外部直鏈或檔名。

我們強烈推薦使用外部圖床或直接貼原 Steam 中的圖片 CDN 地址等，來存放截圖，如果一定要在 FGI 中託管，可以只寫一個檔名，如 <code>&nbsp;&nbsp;-&nbsp;1.webp</code>

```
screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

## 第五步：翻譯關鍵資訊

現在我們有了描述遊戲資訊的檔案，我們已經離成功不遠了！接下來（一個可選的步驟）我們需要為非英文使用者準備翻譯檔案。如果你的母語不是英語，推薦為自己的母語提供一份翻譯檔案，假如你的母語是簡體中文，你可以再準備一份 `遊戲ID.yaml` 檔案（和上一步中的檔案同名），你可以把它放到 `l10n/zh-cn/` 目錄下。

這個檔案的結構就非常簡單了，只有三部分

```
name: 阿達斯特拉 / Adastra

description: |
  你在羅馬留學時突然被外星人綁架。他想從你那裡得到什麼？好吧，他似乎不想告訴你真相。而在搞明白髮生了什麼之前，你已經被帶到了離地球一百萬英里之外的地方。
  阿達斯特拉（Adastra）是一部融合了大量科幻和政治陰謀的浪漫主義視覺小說。你將體驗在一個動盪帝國中的冒險，同時還要決定應該信任或不信任誰。
  在這種充滿背叛和陰謀的氛圍下，您開始懷疑綁架您的外星人是否是您最信任的人。

links-tr:
  "Unoffical chinese mod": "非官方中文補丁"
```

其中，名字（name）和描述（description）和第 4 步中的格式一樣，只是你應該將其翻譯為相應語言。值得一提的是，如果遊戲沒有該語言的官方名字翻譯，你應該使用這種格式 `民間翻譯 / 官方原名`

> 如果民間翻譯有多種，則推薦儘可能將常用名都寫上，如 `漏夏 / 洩漏的夏天 / 咱的夏天 / 漏れなつ。`，但不要在中文翻譯中寫非主要語言（這裡是日語）的翻譯，如 `Morenatsu`

links-tr 部分是比較有趣的部分，還記得第 4 步中的“庫存連結”嗎，我們這裡，要將**非**庫存連結翻譯成本地語言。格式為第一行固定 `links-tr:`，隨後每一行的格式是 <code>&nbsp;&nbsp;"第 4 步中建立的名字": "翻譯"</code>。庫存按鈕無需翻譯(我們正是這樣利用庫存按鈕避免重複的翻譯工作)。

## 第六步：將你編輯的遊戲描述檔案和資原始檔傳送給我們

我們現在有了多個檔案，你現在有兩個選擇，如果你會使用 Github，推薦你傳送 Pull Request，否則你可以透過 [Telegram](https://telegram.org) 聯絡我 [@UtopicPanther](https://t.me/UtopicPanther) 傳送。

如果你要傳送 Pull Request，你應該這樣組織檔案：

首先將本倉庫 fork 到你的賬戶下。你需要建立/修改這幾個檔案

- `games/遊戲ID.yaml` - 你在第 4 步中編輯的遊戲描述檔案
- `games/l10n/${language}/遊戲ID.yaml` - 你在第 5 步中編輯的翻譯檔案。對應放到相應語言的子目錄中，如簡體中文 `games/l10n/zh-cn/遊戲ID.yaml`
- `assets/遊戲ID/...` - 依賴的資原始檔，比如你準備的縮圖，上例中為 `assets/Adastra/thumbnail.jpg`

**註明你的身份（推薦，但如果你想保密，可以不寫）：編輯根目錄下的 `CONTRIBUTORS.md` 的檔案，把你的大名、貢獻和聯絡方式寫到檔案中！你的貢獻不應該被遺忘！**（如果你透過 Telegram 傳送，不要傳這個檔案，直接將你的個人資訊傳送給我即可）

簽入你的修改，然後向 FGI 傳送 Pull Request 吧！
