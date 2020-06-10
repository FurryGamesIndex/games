# 歡迎來到 FurryGamesIndex （獸人控遊戲索引）專案。

建立該專案的動機是狗哥（LuckyDoge）放棄了他的[獸人控遊戲合集](https://doge.im/recommend/kemono-games.html)專案，Utopic Panther 曾經受益於狗哥的專案，試圖在網際網路上重建一個遊戲合集。狗哥慷慨地提供了他曾經付出大量努力取得的成果，使這個專案快速發展為實用的列表成為了可能（目前正在整理[資料](https://furrygamesindex.github.io/staging-from-luckydoge.txt)）。該專案更加註重可維護性，更加鼓勵社群參與，為社群參與提供便利的基礎設施和提高易用性（如標籤及搜尋功能（目前尚未完全實施）），未來可能還會做評分和討論功能。

本專案中，每個遊戲被組織到一個單獨的 YAML 檔案中結構化地表示，YAML 非常易於獸人和人類編輯，然後使用 python 指令碼將其自動渲染成多種語言的 HTML 版本。

## 我們想要你的參與

### 所有獸控們

幫助「新增遊戲」到列表、「維護現有遊戲」（如替換失效的外部連結）、「為遊戲新增標籤」、「修復現有遊戲資訊中的缺陷」等

[立即瞭解如何貢獻](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.zh-tw.md)，只需要花費你幾分鐘的時間瞭解貢獻的步驟。

### 開發者

幫助「查詢和修復 Bug」、「最佳化程式碼的結構和效能」、「實現激動獸心的新功能」，可見下文的 TODO 列表。

### Web 設計師

幫助「改善樣式、互動和使用者體驗」等。

## 版權資訊

所有遊戲資料和文件按照 [創作共用署名-非商業性使用-相同方式共享(CC BY-NC-SA) 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 許可。參見專案根目錄的 LICENSE.CC-BY-NC-SA4 檔案。

部分資料（如遊戲截圖）版權歸原始權利人所有。我們僅在[合理使用](https://en.wikipedia.org/wiki/Fair_use)的前提下發布它們。

本專案的程式碼按照 GNU General Public License 的第 3 版或更高版本進行許可。參見專案根目錄的 LICENSE.GPL3 檔案。

## TODO

- [x] 使用響應式佈局適配移動端
- [x] 自動生成繁體中文版本
- [ ] 簡體中文和繁體中文貢獻無縫轉換
- [ ] 標題/描述搜尋和多標籤搜尋（實現更強大的搜尋功能）
- [ ] 文件的英文翻譯 (WIP)
