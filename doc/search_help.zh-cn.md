# 搜索帮助

“搜索标题” 和 “搜索标题和描述” 将尝试匹配游戏标题或描述中的相关关键字，然后显示匹配结果。这应该是很直观的而不需要过多解释。

“搜索标签” 是 FGI 为用户提供的更强大的搜索功能，此帮助则通过给出示例的方式来说明如何使用此功能。

## 标签系统

在开始之前，简单说明一下 FGI 的标签系统是有必要的。

FGI 的标签包含两部分，可选的 “命名空间” 和 “值”。例如 `male:dog` 标签，命名空间是 `male:`，值则为 `dog`。

命名空间是可选的，因此 `dog` 也是合法的标签。当不带命名空间时，表示不对命名空间进行限定，带有 `male:dog` 或 `female:dog` 或二者都包含的游戏将被认定为包含 `dog` 标签。

标签的值部分可能有一个或多个“别名”，以遍于搜索，例如 `netorare` 标签有一个别名 `ntr`。你可以使用 `ntr` 代替 `netorare`，用 `male:ntr` 代替 `male:netorare`，等。

标签之间还可能存在依赖关系，但这对于搜索来讲无关紧要。

**你可以从 [这里](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.zh-cn.md) 查看 FGI 当前支持的全部标签的列表。如果你发现某个游戏缺失它该有的标签，欢迎参与贡献。如果你认为应该添加更多标签，欢迎联系我们。**

## 基本的搜索

### 搜索单一标签

| |
|-|
| `dog` |
| 搜索任意命名空间中包含 `dog` 标签的游戏。此示例将搜索含有犬兽人的游戏。 |
| `felidae` |
| 搜索在任意命名空间中含有 `felidae` 标签的游戏。此示例将搜索含有猫科兽人的游戏。 |

### 对标签所在命名空间进行限定

| |
|-|
| `male:dog` |
| 搜索在 `male:` 命名空间包含 `dog` 标签的游戏。此示例将搜索含有雄性犬兽人的游戏。 |

### 何时需要引号

如果你使用的标签中包括空格，你 **必须** 将其放置在双引号之中。如果标签不包含空格，则可以用双引号也可以不用。

| |
|-|
| `type:visual-novel`<br>`"type:visual-novel"` |
| 搜索在 `type:` 命名空间包含 `visual-novel` 标签的游戏。此示例将搜索视觉小说游戏。此时两种写法等价。 |
| `"author:The Echo Project"` |
| 搜索在 `author:` 命名空间包含 `"The Echo Project"` 标签的游戏。此示例将搜索由 Echo Project 开发的游戏。使用 `author:The Echo Project` （不带引号）搜索将不按预期工作。 |

### 如果需要排除标签

| |
|-|
| `not misc:work-in-process` |
| 搜索在 `misc:` 命名空间不包含 `work-in-process` 标签的游戏。此示例将搜索已正式发布（而不是仍在开发中的）游戏。 |
| `not yiff` |
| 搜索在任意命名空间不包含 `yiff` 标签的游戏。此示例将排除含有成人内容的游戏。<br> > `yiff` 标签只存在于 `type:` 命名空间。因此对于此标签而言，`type:yiff` 和 `yiff` 等效。 |

## 搜索多个标签

### 与，或，非

| |
|-|
| `misc:3d lang:en wolf`<br>`misc:3d and lang:en and wolf` |
| 搜索同时含有 `misc:3d`, `lang:en` 和 `wolf` 标签的游戏（冒号前表示对命名空间进行限定） |
| `misc:freeware platform:android type:bara`<br>`misc:freeware and platform:android and type:bara` |
| 搜索同时含有 `misc:freeware`, `platform:android` 和 `type:bara` 标签的游戏（冒号前表示对命名空间进行限定） |
| `canine or dragon` |
| 搜索含有 `canine` 标签或含有 `dragon` 标签或二者都含有的游戏。 |
| `male:canine or female:canine` |
| 搜索含有 `male:canine` 标签或含有 `female:canine` 标签或二者都含有的游戏。（在这个示例中，这个表达式实际上与搜索 `canine` 等效. |
| `male:felidae and visual-novel not "author:Studio Klondike"` |
| 搜索含有 `male:fedidae` 标签和 `visual-novel` 标签，但是不含有 `"author:Studio Klondike"` 标签的游戏。此示例将搜索主要角色中包括雄性猫科兽人并且类型是视觉小说，但作者不是 `“Studio Klondike”` 的游戏。 |

### 改变优先级

表达式的优先级为从左到右运算，你可以添加括号来强制改变优先级。括号作为一个整体的部分与父级参与运算。

考虑 `male:canine and type:visual-novel or type:dating-sim` 表达式先查找含有 `male:canine` 的游戏，然后从中筛选含有 `type:visual-novel` 的游戏，再加上从全部游戏中含有 `type:dating-sim` 的游戏。因此它将搜索含有雄性犬科兽人的视觉小说或（不一定要包含雄性犬科兽人）的约会模拟器。如果你是要查找含有雄性犬科兽人的视觉小说或约会模拟器，这显然不是你想要的。解决办法是先让搜索引擎搜索 `type:visual-novel or type:dating-sim`，然后将结果与 `male:canine` 做与运算。我们可以按从左到右的顺序重写表达式，也可以用括号改变优先级。

| |
|-|
| `male:canine and (type:visual-novel or type:dating-sim)` |
| 这个表达式将先找到“视觉小说”或“约会模拟器”的游戏，再在这些游戏里筛选出包含雄性犬科兽人的游戏。 |
| `misc:3d and (lang:en or lang:zh or lang:en-unofficial or lang:zh-unofficial) not type:yiff` |
| 搜索支持英文或中文语言的全年龄向 3D 风格游戏。 |
| `A and (B or (C and D) not (E or (F and G)))` |
| 这个示例仅表示表示括号可以存在多级。最大层级数量与具体浏览器有关。 |

### 改变排序

| |
|-|
| `@reverse` |
| 搜索全部游戏，但结果以 Z-A 的字母顺序排序。（A-Z 顺序的反向） |
| `@lastmod` |
| 搜索全部游戏，但以最近修改顺序排序，最近修改的游戏排序靠前。 |
| `@lastmod @reverse` |
| 搜索全部游戏，但以最近修改顺序反向排序，最近修改的游戏排序靠后。 |
| `misc:freeware @lastmod` |
| 搜索带有 `misc:freeware` 标签的游戏，但以最近修改顺序反向排序，最近修改的游戏排序靠前。 |
| `platform:android or platform:ios @reverse` |
| 搜索 Android 或 iOS 游戏，但结果是 `platform:android or platform:ios` 搜索结果的反向。 |
| `platform:android or (platform:ios @reverse)` |
| 搜索 Android 或 iOS 游戏，但**只**含有 `platform:ios` 标签的游戏将以 Z-A 的字母顺序排序。（A-Z 顺序的反向） |
| `platform:android @lastmod or platform:ios` |
| 搜索 Android 或 iOS 游戏，但含有 `platform:android` 标签或二者都含有的游戏将以最近修改顺序排序，最近修改的游戏排序靠前。 |
| `steam and itchio @lastmod`<br>`steam itchio @lastmod`<br>`steam @lastmod and itchio`<br>`steam @lastmod itchio` |
| 搜索同时在 itch.io 和 Steam 发布的游戏，但以最近修改顺序排序，最近修改的游戏排序靠前。 |
| `steam and (itchio @lastmod)`<br>`steam (itchio @lastmod)` |
| 可能会让用户感到奇怪，但这种写法实际上与 `steam and itchio` 或 `steam itchio` 等效。 |
