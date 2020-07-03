# 常见问题解答

## 有关 FGI 的一般常见问题

### 我发现了页面错误、链接失效

欢迎[参与 FGI 贡献](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.zh-cn.md)

### 我该如何充分利用本站的“搜索”功能

<a id="search_help"></a>

“搜索标题”和“搜索标题和描述”即其字面意思，你需要稍加了解的是“搜索标签”

使用搜索标签时，简单说，共有 5 条规则

1. 你需要使用标签的原名，不能对标签进行模糊搜索。如 `male:wolf`, `type:visual-novel` 等。

2. 如果你使用的标签中包括空格，你**必须**将其放置在双引号之中，如 `"author:The Echo Project"`。如果标签不包含空格，则可以用双引号也可以不用，即 `type:yiff` 和 `"type:yiff"` 是等价的。

3. 如果你只需要搜索一个标签，只需了解 1，2 即可，但当你需要搜索多个标签时，你需要在标签之间使用 `and`, `or` 和 `not` 关键字，它们表示左右的两个部分进行“取交集”（与）、“取并集”（或）和“取差集”（非），请**仅使用小写**。

4. 表达式的优先级为从左到右运算，你可以添加括号来强制改变优先级，如 `male:canine and (type:visual-novel or type:dating-sim)`，这个表达式将先找到“视觉小说”或“约会模拟器”的游戏，再在这些游戏里筛选出包含“男性犬科兽人”的游戏。如果你不加括号，即 `male:canine and type:visual-novel or type:dating-sim` 表示含有“男性犬科兽人”的视觉小说或（不一定要包含男性犬科兽人）的约会模拟器，这可能不是你想要的。括号可以存在多级，如 `A and (B or (C and D) not (E or (F and G)))`

5. 如果你的表达式有语法错误，很多时候 FGI 并不会报错，但可能返回一个可能令人匪夷所思的结果。一个常见的情况是，因为其他搜索引擎的习惯，忘记在两个标签（或一个被括号包含的部分）直接添加 `and`，这是错误的语法，但 FGI 会接受它并目前将采用之前最近的一次出现的 `and`, `or` 或 `not` 决定使用什么集合运算，若没有找到，则回退使用 `or`，但这种结果并不是保证，该行为可能在将来发生改变。永远不要依赖这种非标准行为，记得加上 `and`, `or` 或 `not`。另一种常见情况是，如果左右括号不匹配，表达式可能提前终止，记得确保括号匹配。

以下是一些例子

- `male:canine` 搜索主要角色中包括男性犬科兽人的游戏

- `male:canine or female:canine` 搜索主要角色中包括犬科兽人的游戏

- `male:felidae and type:visual-novel not "author:Studio Klondike"` 搜索主要角色中包括猫科兽人并且类型是视觉小说，但作者不包含有“Studio Klondike” 的游戏

- `male:canine and (type:visual-novel or type:dating-sim)` 搜索包含男性犬科兽人的视觉小说或约会模拟器

- `misc:freeware and platform:android and type:bara` 搜索支持 Android 平台且免费（或有很大部分免费）的男同性恋游戏

- `misc:3d and (lang:en or lang:zh or lang:en-unofficial or lang:zh-unofficial) not type:yiff` 搜索支持英文或中文语言的全年龄向 3D 风格游戏

另外值得一题的是，点击游戏页面中的标签，也可以快速进入搜索页面。

目前很多游戏都缺失标签，所以搜索一些正常标签时可能不能显示它们。这些缺失标签的游戏可以通过搜索 `sys:tagme` 列出，这可能有助于帮助希望贡献标签的朋友更容易找到要贡献标签的游戏：https://furrygamesindex.github.io/zh-cn/search.html?tagx?sys:tagme

### 是否提供离线版本

是的，对于希望保存此列表的人来说，我们提供离线版本

离线版本会附带所有引用的外部图片资源，可以在这些图片地址被封锁的地区使用

构建脚本每天都会自动构建一份离线版本，可以前往[此处](https://github.com/FurryGamesIndex/games/releases/tag/_gh_assets)下载

## 有关贡献的相关问题

### 我能选择匿名贡献吗

虽然不推荐，但我们允许匿名贡献，我们尊重贡献者的要求。同时，如果未来有一天匿名贡献者改变想法，想把自己的名字和联系方式加入到“贡献者列表”中，则我们非常欢迎，随时可以将他们（你们）加入列表！

请注意，即使你匿名贡献，如果你采用 Github Pull Request 的方式，你的 Github 帐号仍会被自动记录。（如果你未设置“隐藏邮箱”，则你的邮箱地址也可能泄漏）

