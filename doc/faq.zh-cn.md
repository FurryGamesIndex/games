# 常见问题解答

## 有关 FGI 的一般常见问题

### 我发现了页面错误、链接失效

欢迎[参与 FGI 贡献](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.zh-cn.md)

### 你们接受直男向游戏吗？

实际上是的。但是为本项目做贡献的志愿者们大部分是同性恋，因此导致了列表上出现的同性恋游戏较多。

即使如此，我们仍然添加了一些直男向游戏。如果你希望看到你喜欢的直男向游戏出现在此列表上，不要犹豫，现在就贡献吧。

### 你们接受 "Kemonomimi" 游戏吗?

永远不会。并且，如果一个游戏同时包含 Kemonomimi 和可接受的 Furry 元素, Kemonomimi 将被认定为“人类或智人 [humankind](https://furrygamesindex.github.io/en/search.html?tagx?male:humankind%20or%20female:humankind)”。

<a id="search_help"></a>
### 我该如何充分利用本站的“搜索”功能

我们提供三种搜索模式：“搜索标题”，“搜索标题和描述” 和 “搜索标签”

“搜索标题”和“搜索标题和描述”即其字面意思你需要稍加了解的是“搜索标签”

1. 你需要使用标签的原名，不能对标签进行模糊搜索。如 `male:wolf`, `type:visual-novel` 等。

2. 如果你使用的标签中包括空格，你**必须**将其放置在双引号之中，如 `"author:The Echo Project"`。如果标签不包含空格，则可以用双引号也可以不用，即 `type:yiff` 和 `"type:yiff"` 是等价的。

	**如果你只需要搜索一个标签，只需了解 1，2 即可，但当你需要搜索多个标签时，请继续向下阅读。**

3. 在两个部分之间使用 `or` （仅限小写字母） 关键字，它们表示左右的两个部分进行“取并集”（或）

	例子：<code>male:canine **or** female:canine</code> 搜索游戏条目标签含有“男性犬科兽人”，或含有"女性犬科兽人"或两个标签都有的游戏。即搜索主要角色包含犬科兽人的游戏。

4. 在两个部分之间使用 `and` （仅限小写字母） 关键字，它们表示左右的两个部分进行“取交集”（与）。

	例子：<code>misc:3d **and** lang:en **and** male:wolf</code> 搜索游戏条目标签必须同时含有 "3D" 和 "官方英文" 和 "男性狼兽人" 三个标签，即搜索主要采用 3D 形式表现的、官方支持英文的、并且含有男性狼兽人的游戏。

	例子：<code>misc:freeware **and** platform:android **and** type:bara</code> 搜索支持 Android 平台且免费（或有很大部分免费）的男同性恋游戏

	曾经你必须这样写。但很多网站的站内搜索中，可直接输入多个关键字达到同样的效果。幸运的是，现在的 FGI 已经支持省略 `and`，这一个特性叫做 "默认 and"。

	例子：`misc:3d lang:en male:wolf` 和 <code>misc:3d **and** lang:en **and** male:wolf</code> 等效。

5. 在两个部分之间使用 `not` （仅限小写字母） 关键字，它们表示左右的两个部分进行“取差集”（非）。在整个表达式的开头或一个括号部分的开头使用 `not`，表示对全部游戏和后侧部分“取差集”（非）。

	例子：<code>male:felidae **and** type:visual-novel **not** "author:Studio Klondike"</code> 搜索主要角色中包括猫科兽人并且类型是视觉小说，但作者不包含有“Studio Klondike” 的游戏。

	例子：<code>**not** type:yiff</code> 搜索不是“含有成人内容”的游戏，即搜索全部的全年龄游戏。

6. 表达式的优先级为从左到右运算，你可以添加括号来强制改变优先级。括号作为一个整体的部分与父级参与运算。

	例子：<code>male:canine **and** **(**type:visual-novel **or** type:dating-sim**)**</code>，这个表达式将先找到“视觉小说”或“约会模拟器”的游戏，再在这些游戏里筛选出包含“男性犬科兽人”的游戏。
	在这个例子中，如果你不加括号，即 `male:canine and type:visual-novel or type:dating-sim` 表示含有“男性犬科兽人”的视觉小说或（不一定要包含男性犬科兽人）的约会模拟器，这可能不是你想要的。

	例子：<code>misc:3d **and** **(**lang:en **or** lang:zh **or** lang:en-unofficial **or** lang:zh-unofficial**)** **not** type:yiff</code> 搜索支持英文或中文语言的全年龄向 3D 风格游戏

	提示：括号可以存在多级，如 `A and (B or (C and D) not (E or (F and G)))`

7. 如果你的表达式有语法错误，很多时候 FGI 并不会报错，但可能返回一个可能令人匪夷所思的结果。如左右括号不匹配等。

另外值得一题的是，点击游戏页面中的标签，也可以快速进入搜索页面。

有的游戏可能缺失标签或被添加了错误的标签。这会影响大家的搜索。如果你发现了，欢迎通过 [Github](https://github.com/FurryGamesIndex/games/) 上的 issues 或 pull request 请求修正（使用 [Telegram](https://t.me/FurryGamesIndex) 联系维护者也是可以的），非常感谢。

你可以从 [这里](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.zh-cn.md) 查看 FGI 当前支持的全部标签的列表。如果你认为应该添加更多标签，也欢迎联系本项目。

### 是否提供离线版本

是的，对于希望保存此列表的人来说，我们提供离线版本

离线版本会附带所有引用的外部图片资源，可以在这些图片地址被封锁的地区使用

构建脚本每天都会自动构建一份离线版本，可以前往[此处](https://github.com/FurryGamesIndex/games/releases/tag/_gh_assets)下载

## 有关贡献的相关问题

### 我能选择匿名贡献吗

虽然不推荐，但我们允许匿名贡献，我们尊重贡献者的要求。同时，如果未来有一天匿名贡献者改变想法，想把自己的名字和联系方式加入到“贡献者列表”中，则我们非常欢迎，随时可以将他们（你们）加入列表！

请注意，即使你匿名贡献，如果你采用 Github Pull Request 的方式，你的 Github 帐号仍会被自动记录。（如果你未设置“隐藏邮箱”，则你的邮箱地址也可能泄漏）

