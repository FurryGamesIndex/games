# 貢獻指南 - 遊戲

這是一篇介紹如何向 FurryGamesIndex（下文簡稱 FGI）新增或編輯遊戲的快速指南。

在學習本指南的同時，可以檢視 [`games`](https://github.com/FurryGamesIndex/games/tree/master/games) 目錄下已有的資料檔案加深理解，或在修改、新增資料檔案的時候參考。

## 收集遊戲相關資訊

你需要在網際網路上搜索或親自體驗，獲取遊戲相關資訊。

請注意，除非在合理使用的前提下（如複製遊戲說明、公開圖片和有限截圖），不要使用受版權保護的材料。

- 遊戲名稱
- 遊戲描述
- 遊戲作者
- 遊戲縮圖（通常是Logo）和截圖
- 遊戲釋出的網址
- 遊戲作者的相關網站，社交網站或 Patreon 等

## 	確定遊戲 ID

遊戲 ID 是用於引用遊戲的字串，有以下要求：

- 每個遊戲都有一個唯一的 ID 進行標識，ID 不可重複，且一旦 ID 確定，通常不再允許修改。
- **遊戲 ID 只能包含 ASCII 字符集中的英文（大小寫均可）、數字和下劃線。**
- 遊戲 ID 不可以以一個 `_` 開頭，但可以以兩個或更多的 `_` 開頭。其他位置的下劃線數量沒有要求。

以下是確定遊戲 ID 的一般思路：

- 例如，你找到了一個叫 `Adastra` 的遊戲，這是英文，我們直接使用 `Adastra` 作為 ID。
- 例如，你找到了一個叫 `バカ部` 的遊戲，這是日文，首先確定是否存在官方英文名，如果不存在，應使用其羅馬字母表示。因此我們使用 `Bakabu` 作為 ID。
- 例如，你找到了一個叫 `家有大貓` 的遊戲，這是中文，但它有官方英文名稱 `Nekojishi`，因此 `Nekojishi` 是遊戲 ID。否則我們可能使用其拼音 `JiaYouDaMao` 作為 ID。
- 例如，你找到了一個叫 `After Class` 的遊戲，它有空格，我們將空格替換為下劃線，即 `After_Class` 是遊戲 ID。

若欲新增的遊戲與FGI遊戲庫中的遊戲重名或名稱容易產生混淆，則需要在經過上文處理過後為遊戲ID新增廠商字尾，原遊戲ID與廠商字尾之間需填入兩個 `_`，例如：

- 你找到了一個由 Might and Delight 製作的 `Shelter 2` 遊戲，但這並不是FGI遊戲庫中由 rausmutt 製作的 `Shelter` 續作，因此前者的遊戲ID為 `Shelter_2__Might_and_Delight` 。

## 編寫遊戲資料檔案

FGI 網站上顯示的每個遊戲都是由來自 FGI 遊戲資料庫中的資料檔案進行加工製成的。FGI 遊戲資料檔案存放的位置是 [`games`](https://github.com/FurryGamesIndex/games/tree/master/games) 子目錄。

要編輯現有遊戲頁面，只需要找到對應的資料檔案進行編輯。要建立一個新的遊戲頁面，則需要建立一個新的遊戲資料檔案。資料檔案的檔名為：

```
<遊戲ID>.yaml
```

例如，遊戲 「Angels with Scaly Wings」（鱗翼天使）對應的遊戲資料檔案為 `Angels_with_Scaly_Wings.yaml`。

在編輯遊戲資料檔案時，需特別注意內容編寫是否**符合 YAML 格式規範**，否則 FGI 將無法正常利用此檔案。


### 遊戲資料檔案要求

#### YAML格式規範和排版

**要注意下面語法中用於縮排的空格，空格的位置和個數必須完全符合定義**，具體內容會在下面詳細敘述。

為了增強資料檔案的易讀性，**必須在每個一級屬性後插入一個空行**，（最後一個可加可不加），例如：

```
name: Adastra

description: |
  You're having the time of your life in Rome on a study abroad program when you're suddenly abducted by an alien. What does he want from you? Well, he doesn't seem to want to tell and, before you know it, you're millions of miles away from Earth on your way to a place you know nothing about.
  
 ......

description-format: markdown

authors:
  - name: The Echo Project
    role: [ producer ]
  - name: Howly
    role: [ screenwriter ]
  - name: HAPS
    role: [ artist ]
  - name: Black Sun Di
    role: [ artist ]

...
```


#### 使用 UNIX（LF）換行符

**遊戲資料檔案需要使用 UNIX（LF）換行符，否則 FGI 可能無法按照預期工作。**

> 此倉庫已使用 `.gitattributes` 要求 git 使用 LF 換行符，標準的 git 軟體通常可以正常工作。


#### 資料檔案的自然語言

FGI 遊戲資料庫中不同語言的資料檔案都以英語的資料檔案作為元檔案。這意味即使你提交的遊戲未有英語翻譯，也需要首先在英語檔案的主目錄下建立資料檔案，而後才在其他語言的目錄下建立本地化的資料檔案。

> 這不代表你必須將資料檔案中的各資訊都翻譯為英語。在缺少合適翻譯的條件下，英語檔案中同樣可以寫入原語言的文字。


下面將介紹遊戲資料檔案的各個部分。**以下內容若未作特別說明，則預設以英語編寫內容。遊戲資訊的本地化見「[遊戲本地化資料檔案](#anchor_localization)」。**



### 遊戲名稱等

#### 遊戲名稱

```
name: 遊戲名稱
```
遊戲名稱優先取用該遊戲的官方英語正式名稱。

1. 若該遊戲的官方英語名稱有地區差異，按以下順序優先取用：
    1. 最多數主創人員最長期居住地（以英語為官方語言的地區）的英語形式；
    2. 最多數主創人員出生地（以英語為官方語言的地區）的英語形式；
    3. 開發商所在地的英語形式。

2. 若該遊戲無官方英語名稱，應取用該遊戲官方最廣泛使用的正式名稱。若該名稱為日語名稱，可以使用 `羅馬音 / 原名`。比如 `バカ部` 可以將此欄位設定為 `Bakabu / バカ部`。

需特別注意的是：

- 不可以使用任何來源的暱稱。
- 若名字中帶有 `:` 等特殊字元，你需要將遊戲名稱使用半形單引號括起來，例如 `name: '塵埃：幸福的尾巴 / Dust: An Elysian Tail'`。
- 若名字中帶有半形單引號，則需要改用半形雙引號將遊戲名稱括起來，例如 `name: "Fox's Holiday / 狐の假期"`。


#### 隱藏遊戲頁面（可選）

有些遊戲還未釋出；或曾經發布然後又被刪除，同時作者表示將在未來發布（等情況）。這時需要使用「軟刪除」，隱藏該遊戲（待到重新發布後取消隱藏）。

「軟刪除」屬性，會隱藏該遊戲，遊戲頁面上將顯示警告提示條。在遊戲列表、站內搜尋結果和通用 Web 搜尋引擎中，都無法搜尋到該遊戲。但不會刪除遊戲頁面，不會從作者頁面、該作者的「更多遊戲「小部件中被刪除該遊戲。

- 要隱藏/軟刪除遊戲頁面，請使用：

```
expunge: true
```

> 這是可選屬性，如果不打算軟刪除遊戲，請**不要**新增這個屬性。
>
> 專案不接受使用 `expunge: false` 的遊戲資料檔案，儘管它完全按照預期工作。


#### 替換舊版遊戲頁面（可選）

有些作者可能會放棄開發舊版遊戲，（更換遊戲型別，）從頭開發新版遊戲。如 `Bare Backstreets`、`履雲錄` 等。這時需**在舊版遊戲的資料檔案裡，使用「被取代」屬性指向新版遊戲。**

使用「被取代」屬性後，會從遊戲列表中隱藏舊版遊戲。當你開啟舊版遊戲頁面後，頁面上方的資訊條上將顯示「被（新遊戲）所取代」的資訊，同時提供一個指向 `replaced-by:` 後的新遊戲的連結；但不會在站內搜尋和通用 Web 搜尋引擎的搜尋結果中刪除舊版遊戲。


- 要表示舊遊戲被新遊戲取代，請使用：

```
replaced-by: 新遊戲ID
```

> 這是可選屬性，如果不打算取代舊遊戲，請**不要**新增這個屬性。此外，`新遊戲ID` 對應的遊戲資料檔案必須已經存在，方可使用 `replaced-by:` 屬性。

例如，在舊版的 `lvyunlu.yaml` 中，使用 `replaced-by:` ，指向 `Elysium_Above` ，也就是新版的履雲錄。

```
name: 履雲錄 （AVD 版）
replaced-by: Elysium_Above
```



### 遊戲描述

#### 完整描述

```
description: |
  第一行描述
  第二行描述
  ...
```

描述部分的格式如上。第一行是固定不變的 `description: |`，換行開始編寫描述，**描述的每一行都要以兩個空格開頭。**

使用 `description-format` 可以指定描述使用某種格式進行處理和渲染，目前支援 `plain`（預設）和 `markdown`。

要用 markdown 編寫描述，應在描述部分的下方新增：

```
description-format: markdown
```

> 在 FGI 遊戲頁面中，markdown 的 `#` 將生成 `<h2>` 而不是 `<h1>`，`##` 將生成 `<h3>`，以此類推。這是因為 `<h1>` 在遊戲頁面上是遊戲名稱，避免讓 markdown 描述導致頁面出現多個 `<h1>` 影響 SEO。
> 
> 注意，**即使使用其他格式，仍然需要使描述的每一行以兩個空格開頭。**
> 
> 我們不建議（但不是不允許）在 markdown 中插入圖片。

描述文字的內容應符合以下要求：
- 優先取用官方原文。
- 不涉及關鍵情節或選擇分支後劇情的劇透。
- 不包含敏感資訊或違反目標語言當地法律法律的字詞、文段。

  


#### 簡化描述（可選）

簡化描述將用於在標準列表檢視和元資料中插入描述。

```
brief-description: |
  第一行簡化描述
  第二行簡化描述
  ...
```

一般簡化描述應短於遊戲完整描述，但完整的描述本身較短的除外。簡化描述的長度最大不得超過 400 個英文字元（包括數字、空格、下劃線），推薦長度為 200 至 400 個英文字元。1 箇中文字元等價於 2 個英文字元。

這是一個可選的部分。對於不包含此部分的遊戲，FGI 將使用標準描述進行自動裁剪。

簡化描述中允許使用換行符，但不支援 markdown 等富文字。



### 作者資訊

#### 常規內容

```
authors:
  - name: 作者1名稱
    role: [ 角色 ]
  - name: 作者2名稱
    role: [ 角色, 角色, 角色 ]
  - name: 作者3名稱
    standalone: true
    role: [ 角色, 角色 ]
```

作者名稱需要使用作者資料檔案定義的作者名稱，不可使用別名。

> 如果未建立作者資料檔案，也可以先在此處直接使用作者的名稱。FGI 渲染工具會對此情況產生抱怨，但仍然可以工作。

如果作者有英文名稱，應優先使用英文名稱。在作者資料檔案中新增其他語言的別名。

角色是一個數組，每個作者最少有一項角色，作者可以同時擔任多項角色，可以選擇的值包括這些。

- `producer`: 製作
- `screenwriter`: 劇本
- `programmer`: 程式
- `artist`: 藝術家
- `animation`: 動畫師
- `musician`: 音樂家
- `voice-actor`: 配音演員
- `character-designer`: 角色設計
- `scenographer`: 場景設計
- `translator`: 翻譯者
- `publisher`: 發行商
- `others`: 其他

每個作者項還包括一些其他的元資料。


#### 獨立作者（可選）

`standalone: true` 定義作者為獨立作者。

獨立作者不會關聯到作者資料檔案，也不會為其創造一個 FGI 作者頁面。

通常情況下，如果一個作者並非該遊戲的最關鍵作者之一，且只在整個 FGI 資料庫中，只出現在一個遊戲條目中，則應該將其定義為獨立作者。

> 這是可選屬性，如果不打算設定獨立作者，請**不要**新增這個屬性。

當 `standalone: true` 存在時，以下屬性可用：

`avatar`: 關聯作者頭像檔案，作為獨立作者的頭像，請參閱「頭像資原始檔規範」

`link-uri`：使獨立作者在頁面的作者區域中變成超連結，並指向該連結。

> 這些都是可選屬性，如果不打算設定，請**不要**新增這些屬性。大多數情況下，`avatar` 和 `link-uri` 不需要設定。

> 對於非獨立作者，avatar 為關聯的作者資料檔案中指定的頭像，超連結指向 FGI 為其建立的作者頁面。



### 遊戲標籤

標籤是描述遊戲的特性。在 FGI 中，標籤由「名稱空間」和「值」組成。並且必須使用標準化的標籤。

有關目前所有標準標籤，詳見 **[全部標籤](../tags.zh-cn.md)**。

```
tags:
  type:
    - visual-novel
    - bara
    - yiff
  species:
    - wolf
    - cat
    - humankind
  fetish:
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
    - zh-unofficial
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android
```


如 `type:visual-novel` 中，名稱空間是冒號前面的 `type`，後面的是值 `visual-novel`。這個標籤表示該遊戲的「型別」是「視覺小說」。同樣， `species:wolf` 表示該遊戲存在主要角色是「狼獸人」，`misc:work-in-process` 表示該遊戲「未完成」，正在開發中（但釋出了先行體驗/Demo版本），`platform:android` 表示該遊戲可以在「Android」「平臺」上執行。

> 最終呈現在頁面上的標籤列表可能會進一步增加，因為 FGI 使用一種叫 「標籤蘊含」 的機制新增自動標籤。如 「狼」 存在時系統將新增 「犬科」。
#### 標籤規範

除`author` 名稱空間下的標籤外，其他標籤都不會有空格。 `author` 名稱空間表示作品的作者（開發者、釋出者等）。 如果`author` 名稱空間的標籤包含空格，則需要用單引號`'`包裹。

標籤列表的**第一行是固定的`tags:`**，然後是多個名稱空間。 每個名稱空間都**以兩個空格開頭，以英文冒號結尾。**

在每個名稱空間下的每一行都**以3個空格為開頭，緊接著是連字元/減號，再接1個空格後，接標籤的值。**如：<code>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;value</code>

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



### 遊戲連結

連結為 FGI 最終的遊戲頁面上建立超連結，我們通常將遊戲的各個釋出地址、網站等等作為連結以便讓玩家可以快速找到需要的遊戲。也可能新增作者的社交平臺、作者的 Patreon，特別是對於在作者資訊中新增的作者沒有建立相應的作者資料檔案時。

```
links:
  - name: 名稱
    uri: URI
  - name: 名稱
    icon: 圖示（可選）
    uri: URI
  - ...
```

> 請注意，除`links:`所在行外，每行行首均有2個或4個空格。

#### 連結名稱

`名稱`為連結的名稱，`URI `通俗地說是該連結的「網址」。如果你不清楚 URI 的意思，也無需在意。

FGI 設計了一種叫 「庫存連結」（Stock Link）的東西，以減少翻譯的工作量。庫存連結名稱以 `.` 開頭。它們是固定的，需要在 [`uil10n`](https://github.com/FurryGamesIndex/games/tree/master/uil10n) 檔案中定義。

當你使用庫存連結時，你就無需寫這麼一段長字，而且無需為每種語言寫一份翻譯。因為庫存連結是固定的，每種語言都可以自動處理。

**存在符合要求的庫存連結時，請務必使用庫存連結。此外，建議把社交網站放在上方，遊戲的釋出頁面放在下方。**

下面是FGI 支援的庫存連結：

- `.website`: 官方網站
- `.twitter`: 官方 Twitter
- `.furaffinity`: 官方 FurAffinity
- `.discord`: 官方 Discord
- `.youtube`: 官方 Youtube
- `.facebook`: 官方 Facebook


- `.release-page`: 釋出頁面
- `.steam`: 在 Steam 上獲取
- `.epic`: 在 Epic Games Store 上獲取
- `.itch.io`: 在 itch.io 上獲取
- `.booth`: 在 BOOTH 上獲取
- `.digiket`: 在 DiGiket 上獲取
- `.play-store`: 在 Google Play 上獲取
- `.apple-appstore`: 在 App Store 上獲取
- `.nintendo-e-shop`: 在 Nintendo eShop 上獲取
- `.playstation-store`: 在 PlayStation Store 上獲取
- `.gog.com`: 在 GOG.com 上獲取
- `.microsoft-store`: 在 Microsoft Store 上獲取


- `.demo-version`: 獲取演示版本
- `.demo-version-steam`: 從 Steam 獲取演示版本
- `.demo-version-gog.com`: 從 GOG.com 獲取演示版本


- `.unofficial-archived-download`: 下載（非官方存檔）
- `.unofficial-version-en`: 非官方英文版本
- `.unofficial-patch-en`: 非官方英文補丁
- `.unofficial-version-zh`: 非官方中文版本
- `.unofficial-patch-zh`: 非官方中文補丁

如果確實需要非庫存連結，則名稱部分直接寫就可以了，**注意這裡我們要使用英文**。例如：

```
links:
  - name: R-18 Patch
    uri: https://example.com/balabala
```

#### URI

URI 部分可能是一個網址或 URL，比如上面的「在 itch.io 平臺上獲取」連結上，我們應該跳轉開啟該遊戲的 itch.io 網頁，因此我們填寫 `https://echoproject.itch.io/adastra`

```
links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
```

部分連結可以簡寫成我們定義的 URI 形式，推薦使用但並非強制

- Steam: `steam:ID` 比如 `steam:570840`，相當於 `https://store.steampowered.com/app/570840`
- Discord: `discord:ID` 比如 `discord:xbox`，相當於  ` https://discord.gg/xbox`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相當於 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:使用者名稱` 比如 `patreon:EchoGame`，相當於 `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:使用者名稱` 比如 `tumblr:xxx`，相當於 `https://xxx.tumblr.com/`
- pixiv: `pixiv:使用者ID` 比如 `pixiv:123456`，相當於 `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:使用者名稱`, 相當於 `https://www.furaffinity.net/user/使用者名稱/`
- DeviantART: `deviantart:使用者名稱`, 相當於 `https://www.deviantart.com/使用者名稱`
- Google Play Store: `google-play-store:package_id` 相當於 `https://play.google.com/store/apps/details?id=package_id`
- FGI misc page: `FGI-misc-page:name` 相當於 `<相對路徑引用網站根目錄>/misc/name.html`，這些頁面是由 FGI 倉庫中的 [`misc-pages`](https://github.com/FurryGamesIndex/games/tree/master/misc-pages) 子目錄下的檔案生成的。

#### 連結圖示（可選）

庫存連結會自動獲得一個相關的「圖示」，比如 `.steam` 連結前將會有一個 steam 的機械 logo。

但是所有的非庫存連結都預設是一種圖示，如果因美觀等原因確實需要在自定義連結上使用非預設圖示，則可以使用 `icon` 屬性，該屬性可以為非庫存連結設定圖示，亦可覆蓋庫存連結預設的圖示。

```
  - name: Author's weibo (DragonSnow)
    icon: weibo
    uri: https://weibo.com/u/2594829495
```

所有受支援的圖示見 <https://github.com/FurryGamesIndex/icons/tree/master/src/site>，這裡的檔名去除 `.svg` 後輟後，即為圖示名稱。



<a id="anchor_thumbnail">

### 遊戲縮圖

#### 大小規範

> FGI 曾經未制定此嚴格的標準，因此舊遊戲的縮圖可能不符合此規範。
>
> **對於新新增遊戲的縮圖、以及更新舊遊戲的縮圖，需要符合此規範。**

在規格上，**縮圖的寬高比固定為 15:7，寬度最大不得超過 360px，高度最大不得超過 168px。** 儘量製作或選用最大寬高規格的縮圖，但不得強制放大原始規格的縮圖。

出於效能考慮，在與100%質量原圖比較未有明顯失真的條件下，**檔案大小不得超過 100KiB**，且在與原圖視覺效果相近的情況下優先上傳更小的檔案。
> 這裡指的影象失真包括但不限於：振鈴效應、方塊效應、色調分離、噪點。

#### 內容規範

在內容上，縮圖應滿足以下要求：

- 優先選用該遊戲官方對外公佈的圖片。
- 等比例縮小圖片素材。能保持相同清晰度的情況下可以放大圖片素材。
- 不包含額外新增的外邊框。
- 帶有透明通道的圖片，任何畫素的透明度要麼完全不透明，要麼完全透明。不得出現 「半透明」的情況。
- 裁剪帶有標題文字的圖片時，不得將文字攔腰截斷。（要麼保留完整的文字，要麼將整塊文字全部裁剪掉）
- **不包含敏感資訊。**


選用或創作的縮圖最好還能：

- 影象清晰，不出現馬賽克或線性過濾造成的模糊。
- 展現遊戲的整體格調、風貌。
- 儘量不要使用帶有透明通道的圖片。一個常見的例外是遊戲官方使用的 logo 就是帶有透明通道的圖片。

在不造成明顯的處理痕跡的前提下，可以透過圖片編輯技術，改變圖片中元素的相對位置。

> 對於來自 Steam 的縮圖，已自動符合該比例，通常只需要按比例縮放到 360x168 px 即可。對於來自其他地方的縮圖，通常情況下都將導致丟失資訊。應儘量保證主要內容不被裁剪掉。

#### 存放目錄

將需要引用的圖片放置於 `assets/遊戲ID/` 目錄下，然後在資源引用處直接填寫`thumbnail.jpg`。

例如，將 `thumbnail.jpg` 放置到 `assets/Adastra/`，然後在 `Adastra.yaml` 中可以引用此圖片。


```
thumbnail: thumbnail.jpg
```



### 遊戲截圖和影片

#### 遊戲截圖

```
screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
  - sensitive: true
    uri: https://images2.imgbox.com/b8/39/pyHagTIF_o.jpg
```

- 常規圖片，直接填寫一個 URI 字串引用圖片
- 敏感圖片，應設定 `sensitive: true` ，並使用 `uri` 屬性引用圖片

> 很多圖床（如 imgur）不允許上傳敏感內容，請勿使用這些圖床託管敏感內容圖片。

透過URI引用外部資源時需要注意：

- URI 中引用的檔案需要包含可被識別的後輟，如 `.png`, `.jpg`, `.jpeg` 等等。FGI 可能需要根據此後輟設定 MIME。
- **FGI不接受查詢字串**，例如 `https://example.com/show_image.cgi?filename=some_picture.png` 可能導致未定義行為。

#### 遊戲影片

在遊戲截圖部分，可以插入遊戲相關的其他媒體，如 Youtube 影片和 HTML 影片嵌入元素。

- 嵌入 Youtube 影片

```
screenshots:
  - type: youtube
    id: <ID>
  - ...
```

ID 為影片 ID，可以從影片連結中獲得：`https://www.youtube.com/watch?v=<ID>` 或 `https://youtu.be/<ID>`


- 嵌入 HTML 影片嵌入元素
HTML 影片嵌入元素可以提供多種型別以兼顧相容性和效能

```
screenshots:
  - type: video
    src:
      - mime: video/webm
        uri: https://example.com/1.webm
      - mime: video/mp4
        uri: https://example.com/1.mp4
  - ...
```

### 提交 Pull Request

#todo？



<a id="anchor_localization">

## 遊戲本地化資料檔案(可選)

FGI 提供了一種機制以本地化遊戲頁面。首先需要在 [`games/l10n`](https://github.com/FurryGamesIndex/games/tree/master/games/l10n) 目錄下具體的語言目錄建立和上述遊戲資料檔案同名的檔案，即 `<遊戲ID>.yaml` 作為遊戲本地化資料檔案。

**遊戲本地化資料檔案中的所有部分都是可選的，如果某項屬性不需要翻譯，請不要新增對應的屬性。**


### 提供名稱的翻譯

和遊戲資料檔案的的格式一樣，使用 `name` 提供遊戲名稱的翻譯。

```
name: 阿達斯特拉 / Adastra
```

對於本地化的遊戲名稱取用：

- 優先取用目標語言的官方遊戲名稱。
- 按知名度排序後取用翻譯質量最高的民間譯名。此時應該使用這種格式 `民間翻譯 / 官方原名`。

使用民間譯名時，可以新增多種民間譯名，如 `漏夏 / 咱的夏天 / 漏れなつ`	


### 提供描述的翻譯

和遊戲資料檔案的的格式一樣，使用 `description` 提供描述的翻譯。

```
description: |
  第一行描述
  第二行描述
  ...

```

和遊戲資料檔案的的格式一樣，可以使用 `description-format` 可以指定描述使用某種格式進行處理和渲染，例如

```
description-format: markdown
```


### 提供簡化描述的翻譯

和遊戲資料檔案的的格式一樣，使用 `brief-description` 提供簡化描述的翻譯。

```
brief-description: |
  第一行簡化描述
  第二行簡化描述
  ...
```


### 提供非庫存連結的翻譯

我們可以提供非庫存連結的翻譯，例如

```
links-tr:
  "Unoffical Chinese patch (provided by 北極光漢化組)": "非官方中文補丁（由北極光漢化組提供）"
  "Unoffical Chinese patch (provided by 迴音漢化組)": "非官方中文補丁（由迴音漢化組提供）"
```

將連結 「Unoffical Chinese patch (provided by 北極光漢化組)」 翻譯為 「非官方中文補丁（由北極光漢化組提供）」；「Unoffical Chinese patch (provided by 迴音漢化組)」 翻譯為 「非官方中文補丁（由迴音漢化組提供）」。

> 原始連結如下，以 `.` 開頭的連結是庫存連結，無需也不能在本地化資料檔案中翻譯。
> ```
>  - name: .itch.io
>    uri: https://echoproject.itch.io/echo
>  - name: .patreon
>    uri: patreon:EchoGame
>  - name: .twitter
>    uri: twitter:EchoTheVN 
>  - name: Unoffical Chinese patch (provided by 北極光漢化組)
>    icon: twitter
>    uri: https://twitter.com/ABLocalization/status/1283925296517754887
>  - name: Unoffical Chinese patch (provided by 北極光漢化組)
>    icon: weibo
>    uri: https://weibo.com/7429628292/JbujJ0rbY
>  - name: Unoffical Chinese patch (provided by 迴音漢化組)
>    icon: itch.io
>    uri: https://lupei.itch.io/echo-chinese
> ```


## 其他情況

### 註釋

資料檔案中可以添加註釋。例如，在你違背常見的編輯方式時，可以透過註釋註明特殊情況。

```
# Some comments
```

