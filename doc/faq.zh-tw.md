# 常見問題解答

## 有關 FGI 的一般常見問題

### 我發現了頁面錯誤、連結失效

歡迎[參與 FGI 貢獻](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.zh-tw.md)

<a id="search_help"></a>
### 我該如何充分利用本站的“搜尋”功能

我們提供三種搜尋模式：“搜尋標題”，“搜尋標題和描述” 和 “搜尋標籤”

“搜尋標題”和“搜尋標題和描述”即其字面意思你需要稍加了解的是“搜尋標籤”

1. 你需要使用標籤的原名，不能對標籤進行模糊搜尋。如 `male:wolf`, `type:visual-novel` 等。

2. 如果你使用的標籤中包括空格，你**必須**將其放置在雙引號之中，如 `"author:The Echo Project"`。如果標籤不包含空格，則可以用雙引號也可以不用，即 `type:yiff` 和 `"type:yiff"` 是等價的。

	**如果你只需要搜尋一個標籤，只需瞭解 1，2 即可，但當你需要搜尋多個標籤時，請繼續向下閱讀。**

3. 在兩個部分之間使用 `or` （僅限小寫字母） 關鍵字，它們表示左右的兩個部分進行“取並集”（或）

	例子：<code>male:canine **or** female:canine</code> 搜尋遊戲條目標籤含有“男性犬科獸人”，或含有"女性犬科獸人"或兩個標籤都有的遊戲。即搜尋主要角色包含犬科獸人的遊戲。

4. 在兩個部分之間使用 `and` （僅限小寫字母） 關鍵字，它們表示左右的兩個部分進行“取交集”（與）。

	例子：<code>misc:3d **and** lang:en **and** male:wolf</code> 搜尋遊戲條目標籤必須同時含有 "3D" 和 "官方英文" 和 "男性狼獸人" 三個標籤，即搜尋主要採用 3D 形式表現的、官方支援英文的、並且含有男性狼獸人的遊戲。

	例子：<code>misc:freeware **and** platform:android **and** type:bara</code> 搜尋支援 Android 平臺且免費（或有很大部分免費）的男同性戀遊戲

	曾經你必須這樣寫。但很多網站的站內搜尋中，可直接輸入多個關鍵字達到同樣的效果。幸運的是，現在的 FGI 已經支援省略 `and`，這一個特性叫做 "預設 and"。

	例子：`misc:3d lang:en male:wolf` 和 <code>misc:3d **and** lang:en **and** male:wolf</code> 等效。

5. 在兩個部分之間使用 `not` （僅限小寫字母） 關鍵字，它們表示左右的兩個部分進行“取差集”（非）。在整個表示式的開頭或一個括號部分的開頭使用 `not`，表示對全部遊戲和後側部分“取差集”（非）。

	例子：<code>male:felidae **and** type:visual-novel **not** "author:Studio Klondike"</code> 搜尋主要角色中包括貓科獸人並且型別是視覺小說，但作者不包含有“Studio Klondike” 的遊戲。

	例子：<code>**not** type:yiff</code> 搜尋不是“含有成人內容”的遊戲，即搜尋全部的全年齡遊戲。

6. 表示式的優先順序為從左到右運算，你可以新增括號來強制改變優先順序。括號作為一個整體的部分與父級參與運算。

	例子：<code>male:canine **and** **(**type:visual-novel **or** type:dating-sim**)**</code>，這個表示式將先找到“視覺小說”或“約會模擬器”的遊戲，再在這些遊戲裡篩選出包含“男性犬科獸人”的遊戲。
	在這個例子中，如果你不加括號，即 `male:canine and type:visual-novel or type:dating-sim` 表示含有“男性犬科獸人”的視覺小說或（不一定要包含男性犬科獸人）的約會模擬器，這可能不是你想要的。

	例子：<code>misc:3d **and** **(**lang:en **or** lang:zh **or** lang:en-unofficial **or** lang:zh-unofficial**)** **not** type:yiff</code> 搜尋支援英文或中文語言的全年齡向 3D 風格遊戲

	提示：括號可以存在多級，如 `A and (B or (C and D) not (E or (F and G)))`

7. 如果你的表示式有語法錯誤，很多時候 FGI 並不會報錯，但可能返回一個可能令人匪夷所思的結果。如左右括號不匹配等。

另外值得一題的是，點選遊戲頁面中的標籤，也可以快速進入搜尋頁面。

有的遊戲可能缺失標籤或被添加了錯誤的標籤。這會影響大家的搜尋。如果你發現了，歡迎透過 [Github](https://github.com/FurryGamesIndex/games/) 上的 issues 或 pull request 請求修正（使用 [Telegram](https://t.me/FurryGamesIndex) 聯絡維護者也是可以的），非常感謝。

你可以從 [這裡](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.zh-tw.md) 檢視 FGI 當前支援的全部標籤的列表。如果你認為應該新增更多標籤，也歡迎聯絡本專案。

### 是否提供離線版本

是的，對於希望儲存此列表的人來說，我們提供離線版本

離線版本會附帶所有引用的外部圖片資源，可以在這些圖片地址被封鎖的地區使用

構建指令碼每天都會自動構建一份離線版本，可以前往[此處](https://github.com/FurryGamesIndex/games/releases/tag/_gh_assets)下載

## 有關貢獻的相關問題

### 我能選擇匿名貢獻嗎

雖然不推薦，但我們允許匿名貢獻，我們尊重貢獻者的要求。同時，如果未來有一天匿名貢獻者改變想法，想把自己的名字和聯絡方式加入到“貢獻者列表”中，則我們非常歡迎，隨時可以將他們（你們）加入列表！

請注意，即使你匿名貢獻，如果你採用 Github Pull Request 的方式，你的 Github 帳號仍會被自動記錄。（如果你未設定“隱藏郵箱”，則你的郵箱地址也可能洩漏）

