# 搜尋幫助

“搜尋標題” 和 “搜尋標題和描述” 將嘗試匹配遊戲標題或描述中的相關關鍵字，然後顯示匹配結果。這應該是很直觀的而不需要過多解釋。

“搜尋標籤” 是 FGI 為使用者提供的更強大的搜尋功能，此幫助則透過給出示例的方式來說明如何使用此功能。

## 標籤系統

在開始之前，簡單說明一下 FGI 的標籤系統是有必要的。

FGI 的標籤包含兩部分，可選的 “名稱空間” 和 “值”。例如 `male:dog` 標籤，名稱空間是 `male:`，值則為 `dog`。

名稱空間是可選的，因此 `dog` 也是合法的標籤。當不帶名稱空間時，表示不對名稱空間進行限定，帶有 `male:dog` 或 `female:dog` 或二者都包含的遊戲將被認定為包含 `dog` 標籤。

標籤的值部分可能有一個或多個“別名”，以遍於搜尋，例如 `netorare` 標籤有一個別名 `ntr`。你可以使用 `ntr` 代替 `netorare`，用 `male:ntr` 代替 `male:netorare`，等。

標籤之間還可能存在依賴關係，但這對於搜尋來講無關緊要。

**你可以從 [這裡](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.zh-tw.md) 檢視 FGI 當前支援的全部標籤的列表。如果你發現某個遊戲缺失它該有的標籤，歡迎參與貢獻。如果你認為應該新增更多標籤，歡迎聯絡我們。**

## 基本的搜尋

### 搜尋單一標籤

| |
|-|
| `dog` |
| 搜尋任意名稱空間中包含 `dog` 標籤的遊戲。此示例將搜尋含有犬獸人的遊戲。 |
| `felidae` |
| 搜尋在任意名稱空間中含有 `felidae` 標籤的遊戲。此示例將搜尋含有貓科獸人的遊戲。 |

### 對標籤所在名稱空間進行限定

| |
|-|
| `male:dog` |
| 搜尋在 `male:` 名稱空間包含 `dog` 標籤的遊戲。此示例將搜尋含有雄性犬獸人的遊戲。 |

### 何時需要引號

如果你使用的標籤中包括空格，你 **必須** 將其放置在雙引號之中。如果標籤不包含空格，則可以用雙引號也可以不用。

| |
|-|
| `type:visual-novel`<br>`"type:visual-novel"` |
| 搜尋在 `type:` 名稱空間包含 `visual-novel` 標籤的遊戲。此示例將搜尋視覺小說遊戲。此時兩種寫法等價。 |
| `"author:The Echo Project"` |
| 搜尋在 `author:` 名稱空間包含 `"The Echo Project"` 標籤的遊戲。此示例將搜尋由 Echo Project 開發的遊戲。使用 `author:The Echo Project` （不帶引號）搜尋將不按預期工作。 |

### 如果需要排除標籤

| |
|-|
| `not misc:work-in-process` |
| 搜尋在 `misc:` 名稱空間不包含 `work-in-process` 標籤的遊戲。此示例將搜尋已正式釋出（而不是仍在開發中的）遊戲。 |
| `not yiff` |
| 搜尋在任意名稱空間不包含 `yiff` 標籤的遊戲。此示例將排除含有成人內容的遊戲。<br> > `yiff` 標籤只存在於 `type:` 名稱空間。因此對於此標籤而言，`type:yiff` 和 `yiff` 等效。 |

## 搜尋多個標籤

### 與，或，非

| |
|-|
| `misc:3d lang:en wolf`<br>`misc:3d and lang:en and wolf` |
| 搜尋同時含有 `misc:3d`, `lang:en` 和 `wolf` 標籤的遊戲（冒號前表示對名稱空間進行限定） |
| `misc:freeware platform:android type:bara`<br>`misc:freeware and platform:android and type:bara` |
| 搜尋同時含有 `misc:freeware`, `platform:android` 和 `type:bara` 標籤的遊戲（冒號前表示對名稱空間進行限定） |
| `canine or dragon` |
| 搜尋含有 `canine` 標籤或含有 `dragon` 標籤或二者都含有的遊戲。 |
| `male:canine or female:canine` |
| 搜尋含有 `male:canine` 標籤或含有 `female:canine` 標籤或二者都含有的遊戲。（在這個示例中，這個表示式實際上與搜尋 `canine` 等效. |
| `male:felidae and visual-novel not "author:Studio Klondike"` |
| 搜尋含有 `male:fedidae` 標籤和 `visual-novel` 標籤，但是不含有 `"author:Studio Klondike"` 標籤的遊戲。此示例將搜尋主要角色中包括雄性貓科獸人並且型別是視覺小說，但作者不是 `“Studio Klondike”` 的遊戲。 |

### 改變優先順序

表示式的優先順序為從左到右運算，你可以新增括號來強制改變優先順序。括號作為一個整體的部分與父級參與運算。

考慮 `male:canine and type:visual-novel or type:dating-sim` 表示式先查詢含有 `male:canine` 的遊戲，然後從中篩選含有 `type:visual-novel` 的遊戲，再加上從全部遊戲中含有 `type:dating-sim` 的遊戲。因此它將搜尋含有雄性犬科獸人的視覺小說或（不一定要包含雄性犬科獸人）的約會模擬器。如果你是要查詢含有雄性犬科獸人的視覺小說或約會模擬器，這顯然不是你想要的。解決辦法是先讓搜尋引擎搜尋 `type:visual-novel or type:dating-sim`，然後將結果與 `male:canine` 做與運算。我們可以按從左到右的順序重寫表示式，也可以用括號改變優先順序。

| |
|-|
| `male:canine and (type:visual-novel or type:dating-sim)` |
| 這個表示式將先找到“視覺小說”或“約會模擬器”的遊戲，再在這些遊戲裡篩選出包含雄性犬科獸人的遊戲。 |
| `misc:3d and (lang:en or lang:zh or lang:en-unofficial or lang:zh-unofficial) not type:yiff` |
| 搜尋支援英文或中文語言的全年齡向 3D 風格遊戲。 |
| `A and (B or (C and D) not (E or (F and G)))` |
| 這個示例僅表示表示括號可以存在多級。最大層級數量與具體瀏覽器有關。 |

### 改變排序

| |
|-|
| `@reverse` |
| 搜尋全部遊戲，但結果以 Z-A 的字母順序排序。（A-Z 順序的反向） |
| `@lastmod` |
| 搜尋全部遊戲，但以最近修改順序排序，最近修改的遊戲排序靠前。 |
| `@lastmod @reverse` |
| 搜尋全部遊戲，但以最近修改順序反向排序，最近修改的遊戲排序靠後。 |
| `misc:freeware @lastmod` |
| 搜尋帶有 `misc:freeware` 標籤的遊戲，但以最近修改順序反向排序，最近修改的遊戲排序靠前。 |
| `platform:android or platform:ios @reverse` |
| 搜尋 Android 或 iOS 遊戲，但結果是 `platform:android or platform:ios` 搜尋結果的反向。 |
| `platform:android or (platform:ios @reverse)` |
| 搜尋 Android 或 iOS 遊戲，但**只**含有 `platform:ios` 標籤的遊戲將以 Z-A 的字母順序排序。（A-Z 順序的反向） |
| `platform:android @lastmod or platform:ios` |
| 搜尋 Android 或 iOS 遊戲，但含有 `platform:android` 標籤或二者都含有的遊戲將以最近修改順序排序，最近修改的遊戲排序靠前。 |
| `steam and itchio @lastmod`<br>`steam itchio @lastmod`<br>`steam @lastmod and itchio`<br>`steam @lastmod itchio` |
| 搜尋同時在 itch.io 和 Steam 釋出的遊戲，但以最近修改順序排序，最近修改的遊戲排序靠前。 |
| `steam and (itchio @lastmod)`<br>`steam (itchio @lastmod)` |
| 可能會讓使用者感到奇怪，但這種寫法實際上與 `steam and itchio` 或 `steam itchio` 等效。 |
