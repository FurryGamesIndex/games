# 贡献指南 - 作者

这是一篇介绍如何向 FurryGamesIndex（下文简称 FGI）添加或编辑作者信息的快速指南，目前处于草案试行阶段。

在学习本指南的同时，可以查看 [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors) 目录下已有的数据文件加深理解，或在修改、新增数据文件的时候参考。

## 作者 ID

作者 ID 是用于引用作者文件的字符串，并具有以下要求：

- 每位作者都有一个唯一的 ID 进行标识，ID 不可重复，且一旦 ID 确定，通常不再允许修改。
- 作者 ID 只能包含 ASCII 字符集中的英文（大小写均可）、数字和下划线。
- 作者 ID 不可以以一个 `_` 开头，但可以以两个或更多的 `_` 开头。其他位置的下划线数量没有要求。

以下是定义作者 ID 的一般思路：

- 例如，如果作者的名字叫 `Rimentus` ，这是英文，我们直接使用 `Rimentus` 作为 ID。
- 例如，如果作者的名字叫 `とりあえず`，这是日文，但它有官方英文名称或用户名，因此 `toriaezu13` 是作者 ID。否则我们可能使用其罗马音 `toriaezu` 作为 ID。
- 例如，如果作者的名字叫 `Black Sun Di`，它有空格，我们将空格替换为下划线，即 `Black_Sun_Di` 是作者 ID。

## 作者数据文件

FGI 网站上显示的每位作者都是由来自 FGI 作者数据库中的数据文件进行加工制成的。FGI 作者数据文件存放的位置是 [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors) 子目录。

要编辑现有作者页面，只需要找到对应的数据文件进行编辑。要创建一个新的作者页面，则需要创建一个新的作者数据文件。数据文件的文件名为

```
<作者ID>.yaml
```

例如，作者 “The Echo Project”（回音制作组）对应的数据文件为 `The_Echo_Project.yaml`。

在编辑作者数据文件时，需特别注意内容编写是否符合 YAML 格式规范，否则 FGI 将无法正常利用此文件。

> 作者数据文件需要使用 UNIX（LF）换行符，否则 FGI 可能无法按照预期工作。
>
> 此仓库已使用 `.gitattributes` 要求 git 使用 LF 换行符，标准的 git 软件通常可以正常工作。

下面将介绍作者数据文件的各个部分。

### 数据文件排版

为了增强数据文件的易读性，必须在每个一级属性（最后一个可加可不加）后插入一个空行。

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

此外，要注意下面语法中用于缩进的空格，空格的位置和个数必须完全符合定义。

### 名称

```
name: 作者名称
```

作者名称使用与作者ID相同的正式名称。

### 别名

```
aliases:
  - 别名1
  - 别名2
  ...
```

### 作者类型

```
type: personal
```

作者类型提供以下选项：

- `unknown`: 未知
- `personal`: 个人
- `small-team`: 独立游戏团队
- `company`: 公司
- `publisher`: 发行商

例如《Echo》游戏的其中一位作者 The Echo Project 为开发团队，那么此处应填入 `small-team`。

### 作者头像

作者头像通过文件名进行内部引用

将需要引用的图片放置于 assets/_avatar/ 目录下，然后在资源引用处直接填写文件名。

例如，将 Black_Sun_Di.jpg 放置到 assets/_avatar/，然后在 Black_Sun_Di.yaml 中可以引用此图片，如下：

```
avatar: Black_Sun_Di.jpg
```

#### 图片资源文件规范

FGI对作者头像有着明确的规定，在规格上，图片的长和宽统一为 64px。尽量制作或选用大于此规格的图片，并对其裁剪和缩小。

出于性能考虑，在与100%质量原图比较未有明显失真的条件下，文件大小不得超过 10KiB，且在与原图视觉效果相近的情况下优先上传更小的文件。

### 链接

```
links:
  - name: 名称
    uri: URI
  - name: 名称
    icon: 图标（可选）
    uri: URI
  - ...
```

链接为 FGI 为作者页面创建的超链接，这里通常写入作者在各个网站上的官方主页以便玩家可以快速了解作者动向。可以添加作者的社交平台、作者的 Patreon 等等。

名称为链接的名称，URI 通俗地说是该链接的“网址”，如果你不清楚 URI 的意思，也无需在意。

#### 名称

FGI 设计了一种叫 “库存链接”（Stock Link）的东西减少翻译的工作量。库存链接名称以 `.` 开头。它们是固定的，需要在 [`uil10n`](https://github.com/FurryGamesIndex/games/tree/master/uil10n) 文件中定义。

作者数据文件下的库存链接可包含以下几个：

- `.website`: 官方网站
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

当你使用库存链接时，你就无需写这么一段长字，而且无需为每种语言写一份，因为库存链接是固定的，每种语言都可以自动处理。

存在符合要求的库存链接时，必须使用库存链接。

如果确实需要非库存链接，则名称部分直接写就可以了，注意这里我们要使用英文。例如：

```
  - name: WildDream
    uri: https://www.wilddream.net/user/balabala
```

#### URI

URI 部分可能是一个网址或 URL，比如上面的“在 YouTube 平台上获取”链接上，我们应该跳转打开该作者的 youtube 用户主页，因此我们填写 `https://www.youtube.com/c/MightAndDelight`

同时，部分链接可以简写成我们定义的 URI 形式，推荐使用但并非强制

- Steam: `steam:ID` 比如 `steam:570840`，相当于 `https://store.steampowered.com/app/570840`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相当于 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:用户名` 比如 `patreon:EchoGame`，相当于 `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:用户名` 比如 `tumblr:xxx`，相当于 `https://xxx.tumblr.com/`
- pixiv: `pixiv:用户ID` 比如 `pixiv:123456`，相当于 `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:用户名`, 相当于 `https://www.furaffinity.net/user/用户名/`
- DeviantART: `deviantart:用户名`, 相当于 `https://www.deviantart.com/用户名`
- FGI misc page: `FGI-misc-page:name` 相当于 `<相对路径引用网站根目录>/misc/name.html`，这些页面是由 FGI 仓库中的 [`misc-pages`](https://github.com/FurryGamesIndex/games/tree/master/misc-pages) 子目录下的文件生成的。
