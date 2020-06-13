# 欢迎来到 FurryGamesIndex （兽人控游戏索引）项目。

创建该项目的动机是狗哥（LuckyDoge）放弃了他的[兽人控游戏合集](https://doge.im/recommend/kemono-games.html)项目，Utopic Panther 曾经受益于狗哥的项目，试图在互联网上重建一个游戏合集。[狗哥慷慨地提供了他曾经付出大量努力取得的成果](https://github.com/FurryGamesIndex/games/blob/master/luckydoge.txt)，使这个项目快速发展为实用的列表成为了可能。该项目更加注重可维护性，更加鼓励社区参与，为社区参与提供便利的基础设施和提高易用性（如标签及搜索功能（目前尚未完全实施）），未来可能还会做评分和讨论功能。

本项目中，每个游戏被组织到一个单独的 YAML 文件中结构化地表示，YAML 非常易于兽人和人类编辑，然后使用 python 脚本将其自动渲染成多种语言的 HTML 版本。

## 我们想要你的参与

### 所有兽控们

帮助「添加游戏」到列表、「维护现有游戏」（如替换失效的外部链接）、「为游戏添加标签」、「修复现有游戏信息中的缺陷」等

[立即了解如何贡献](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.zh-cn.md)，只需要花费你几分钟的时间了解贡献的步骤。

### 开发者

帮助「查找和修复 Bug」、「优化代码的结构和性能」、「实现激动兽心的新功能」，可见下文的 TODO 列表。

[构建指南](https://github.com/FurryGamesIndex/games/blob/master/BUILD.md)

### Web 设计师

帮助「改善样式、交互和用户体验」等。

## 版权信息

所有游戏数据和文档按照 [创作共用署名-非商业性使用-相同方式共享(CC BY-NC-SA) 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可。参见项目根目录的 LICENSE.CC-BY-NC-SA4 文件。

部分数据（如游戏截图）版权归原始权利人所有。我们仅在[合理使用](https://en.wikipedia.org/wiki/Fair_use)的前提下发布它们。

本项目的代码按照 GNU General Public License 的第 3 版或更高版本进行许可。参见项目根目录的 LICENSE.GPL3 文件。

## TODO

- [x] 使用响应式布局适配移动端
- [x] 自动生成繁体中文版本
- [ ] 简体中文和繁体中文贡献无缝转换
- [ ] 标题/描述搜索和多标签搜索（实现更强大的搜索功能）
- [ ] 文档的英文翻译 (WIP)
