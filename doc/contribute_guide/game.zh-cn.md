# 贡献指南 - 游戏

这是一篇介绍如何向 FurryGamesIndex（下文简称 FGI）添加或编辑游戏的快速指南。

在学习本指南的同时，可以查看 [`games`](https://github.com/FurryGamesIndex/games/tree/master/games) 目录下已有的数据文件加深理解，或在修改、新增数据文件的时候参考。



## 游戏 ID

游戏 ID 是用于引用游戏的字符串，并具有以下要求：

- 每个游戏都有一个唯一的 ID 进行标识，ID 不可重复，且一旦 ID 确定，通常不再允许修改。
- 游戏 ID 只能包含 ASCII 字符集中的英文（大小写均可）、数字和下划线。
- 游戏 ID 不可以以一个 `_` 开头，但可以以两个或更多的 `_` 开头。其他位置的下划线数量没有要求。

以下是定义游戏 ID 的一般思路：

- 例如，你找到了一个叫 `Adastra` 的游戏，这是英文，我们直接使用 `Adastra` 作为 ID。
- 例如，你找到了一个叫 `バカ部` 的游戏，这是日文，首先确定是否存在官方英文名，如果不存在，应使用其罗马字母表示。因此我们使用 `Bakabu` 作为 ID。
- 例如，你找到了一个叫 `家有大貓` 的游戏，这是中文，但它有官方英文名称 `Nekojishi`，因此 `Nekojishi` 是游戏 ID。否则我们可能使用其拼音 `JiaYouDaMao` 作为 ID。
- 例如，你找到了一个叫 `After Class` 的游戏，它有空格，我们将空格替换为下划线，即 `After_Class` 是游戏 ID。

若欲添加的游戏与FGI游戏库中的游戏重名或名称容易产生混淆，则需要在经过上文处理过后为游戏ID添加厂商后缀，原游戏ID与厂商后缀之间需填入两个 `_`，例如：

- 你找到了一个由 Might and Delight 制作的 `Shelter 2` 游戏，但这并不是FGI游戏库中由 rausmutt 制作的 `Shelter` 续作，因此前者的游戏ID为 `Shelter_2__Might_and_Delight` 。



## 游戏数据文件

FGI 网站上显示的每个游戏都是由来自 FGI 游戏数据库中的数据文件进行加工制成的。FGI 游戏数据文件存放的位置是 [`games`](https://github.com/FurryGamesIndex/games/tree/master/games) 子目录。

要编辑现有游戏页面，只需要找到对应的数据文件进行编辑。要创建一个新的游戏页面，则需要创建一个新的游戏数据文件。数据文件的文件名为：

```
<游戏ID>.yaml
```

例如，游戏 “Angels with Scaly Wings”（鳞翼天使）对应的游戏数据文件为 `Angels_with_Scaly_Wings.yaml`。

在编辑游戏数据文件时，需特别注意内容编写是否**符合 YAML 格式规范**，否则 FGI 将无法正常利用此文件。



### 游戏数据文件要求

#### YAML格式规范和排版

**要注意下面语法中用于缩进的空格，空格的位置和个数必须完全符合定义，**具体内容会在下面详细叙述。

为了增强数据文件的易读性，**必须在每个一级属性后插入一个空行**，（最后一个可加可不加），例如：

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

#### 使用 UNIX（LF）换行符

**游戏数据文件需要使用 UNIX（LF）换行符，否则 FGI 可能无法按照预期工作。**

> 此仓库已使用 `.gitattributes` 要求 git 使用 LF 换行符，标准的 git 软件通常可以正常工作。



#### 数据文件的自然语言

FGI 游戏数据库中不同语言的数据文件都以英语的数据文件作为元文件。这意味即使你提交的游戏未有英语翻译，也需要首先在英语文件的主目录下创建数据文件，而后才在其他语言的目录下创建本地化的数据文件。

> 这不代表你必须将数据文件中的各信息都翻译为英语。在缺少合适翻译的条件下，英语文件中同样可以写入原语言的文本。

**以下部分若未作特别说明，则默认以英语编写内容。游戏信息的本地化见「[游戏本地化数据文件](#anchor_localization)」。**

如果你不太清楚，可以复制一个已有游戏的数据文件，然后照葫芦画瓢，修改相应内容。

下面将介绍游戏数据文件的各个部分。



### 游戏名称

```
name: 游戏名称
```
游戏名称优先取用该游戏的官方英语正式名称。

1. 若该游戏的官方英语名称有地区差异，按以下顺序优先取用：
    1. 最多数主创人员最长期居住地（以英语为官方语言的地区）的英语形式；
    2. 最多数主创人员出生地（以英语为官方语言的地区）的英语形式；
    3. 开发商所在地的英语形式。

2. 若该游戏无官方英语名称，应取用该游戏官方最广泛使用的正式名称。若该名称为日语名称，可以使用 `罗马音 / 原名`。比如 `バカ部` 可以将此字段设置为 `Bakabu / バカ部`。

需特别注意的是：

- 不可以使用任何来源的昵称。
- 若名字中带有 `:` 等特殊字符，你需要将游戏名称使用半角单引号括起来，例如 `name: '尘埃：幸福的尾巴 / Dust: An Elysian Tail'`。
- 若名字中带有半角单引号，则需要改用半角双引号将游戏名称括起来，例如 `name: "Fox's Holiday / 狐の假期"`。



#### 软删除和被取代（可选）

- 要软删除游戏页面，请使用：

```
expunge: true
```

这将使该游戏从游戏列表、站内搜索结果和通用 Web 搜索引擎中被删除，但游戏页面仍然实际存在。游戏页面上将显示警告提示条。

> 此属性不会导致游戏从作者页面、该作者的“更多游戏小部件”中被删除。

> 这是可选属性，如果不打算软删除游戏，请**不要**添加这个属性。项目不接受使用 `expunge: false` 的游戏数据文件，尽管它完全按照预期工作。

这么做的常见原因通常是游戏未发布，或曾经发布然后又被删除，同时作者表示将在未来发布等。



- 要表示游戏被另一个游戏取代，请使用：

```
replaced-by: 游戏ID
```

这将使该游戏从游戏列表中被删除，但不会导致从站内搜索和通用 Web 搜索引擎中被删除。游戏页面上将显示“被取代”信息条，同时包含一个指向 `replaced-by:` 指定的游戏的链接。

> 这是可选属性，如果不打算取代游戏，请**不要**添加这个属性。`游戏ID` 对应的游戏数据文件必须已经存在。

这么做的原因是游戏被重新开发，且旧版游戏在未完成开发之前被废弃。如 `Bare Backstreets`、`履云录` 等



### 游戏描述

```
description: |
  第一行描述
  第二行描述
  ...
```

描述部分的格式如上。第一行是固定不变的 `description: |`，换行开始编写描述，**描述的每一行都要以两个空格开头。**

使用 `description-format` 可以指定描述使用某种格式进行处理和渲染，目前支持 `plain`（默认）和 `markdown`。

要用 markdown 编写描述，应在描述部分的下方添加：

```
description-format: markdown
```

> 在 FGI 游戏页面中，markdown 的 `#` 将生成 `<h2>` 而不是 `<h1>`，`##` 将生成 `<h3>`，以此类推。这是因为 `<h1>` 在游戏页面上是游戏名称，避免让 markdown 描述导致页面出现多个 `<h1>` 影响 SEO。

> 注意，即使使用其他格式，仍然需要使描述的每一行以两个空格开头。

> 我们不建议（但不是不允许）在 markdown 中插入图片。有关插入图片的更多信息，请参阅「[资源引用](#anchor_resref)」。

描述文本的内容应符合以下要求：
- 优先取用官方原文。
- 不涉及关键情节或选择分支后剧情的剧透。
- 不包含敏感信息或违反目标语言当地法律法律的字词、文段。



#### 简化描述（可选）

简化描述将用于在标准列表视图和元数据中插入描述。

```
brief-description: |
  第一行简化描述
  第二行简化描述
  ...
```

一般简化描述应短于游戏完整描述，但完整的描述本身较短的除外。简化描述的长度最大不得超过 400 个英文字符（包括数字、空格、下划线），推荐长度为 200 至 400 个英文字符。1 个中文字符等价于 2 个英文字符。

这是一个可选的部分。对于不包含此部分的游戏，FGI 将使用标准描述进行自动裁剪。

简化描述中允许使用换行符，但不支持 markdown 等富文本。



### 作者信息

```
authors:
  - name: 作者1名称
    role: [ 角色 ]
  - name: 作者2名称
    role: [ 角色, 角色, 角色 ]
  - name: 作者3名称
    standalone: true
    role: [ 角色, 角色 ]
```

作者名称需要使用作者数据文件定义的作者名称，不可使用别名。

> 如果未创建作者数据文件，也可以先在此处直接使用作者的名称。FGI 渲染工具会对此情况产生抱怨，但仍然可以工作。

如果作者有英文名称，应优先使用英文名称。在作者数据文件中添加其他语言的别名。

角色是一个数组，每个作者最少有一项角色，作者可以同时担任多项角色，可以选择的值包括这些。

- `producer`: 制作
- `screenwriter`: 剧本
- `programmer`: 程序
- `artist`: 艺术家
- `animation`: 动画师
- `musician`: 音乐家
- `voice-actor`: 配音演员
- `character-designer`: 角色设计
- `scenographer`: 场景设计
- `translator`: 翻译者
- `publisher`: 发行商
- `others`: 其他

每个作者项还包括一些其他的元数据。



#### 独立作者（可选）

`standalone: true` 定义作者为独立作者。

独立作者不会关联到作者数据文件，也不会为其创造一个 FGI 作者页面。

通常情况下，如果一个作者并非该游戏的最关键作者之一，且只在整个 FGI 数据库中，只出现在一个游戏条目中，则应该将其定义为独立作者。

> 这是可选属性，如果不打算设置独立作者，请**不要**添加这个属性。

当 `standalone: true` 存在时，以下属性可用：

`avatar`: 关联作者头像文件，作为独立作者的头像，请参阅「头像资源文件规范」

`link-uri`：使独立作者在页面的作者区域中变成超链接，并指向该链接。

> 这些都是可选属性，如果不打算设置，请**不要**添加这些属性。大多数情况下，`avatar` 和 `link-uri` 不需要设置。

> 对于非独立作者，avatar 为关联的作者数据文件中指定的头像，超链接指向 FGI 为其创建的作者页面。



### 游戏标签

有关目前所有标准标签，详见 **[全部标签](../tags.zh-cn.md)**。

```
tags:
  第一个命名空间:
    - 值1
    - 值2
    - 值3
  第二个命名空间:
    - 值1
    - ...
  ...
```

标签是描述游戏的特性。在 FGI 中，标签由“命名空间”和“值”组成。并且必须使用标准化的标签。如 `type:visual-novel` 中，命名空间是冒号前面的 `type`，后面的是值 `visual-novel`。这个标签表示该游戏的「类型」是「视觉小说」。同样， `species:wolf` 表示该游戏存在主要角色是「狼兽人」，`misc:work-in-process` 表示该游戏「未完成」，正在开发中（但发布了先行体验/Demo版本），`platform:android` 表示该游戏可以在「Android」「平台」上运行。

> 最终呈现在页面上的标签列表可能会进一步增加，因为 FGI 使用一种叫 “标签蕴含” 的机制添加自动标签。如 “狼” 存在时系统将添加 “犬科”。



### 游戏链接

```
links:
  - name: 名称
    uri: URI
  - name: 名称
    icon: 图标（可选）
    uri: URI
  - ...
```

链接为 FGI 最终的游戏页面上创建超链接，我们通常将游戏的各个发布地址、网站等等作为链接以便让玩家可以快速找到需要的游戏。也可能添加作者的社交平台、作者的 Patreon，特别是对于在作者信息中添加的作者没有创建相应的作者数据文件时。

名称为链接的名称，URI 通俗地说是该链接的“网址”，如果你不清楚 URI 的意思，也无需在意。



#### 链接名称

FGI 设计了一种叫 “库存链接”（Stock Link）的东西，以减少翻译的工作量。库存链接名称以 `.` 开头。它们是固定的，需要在 [`uil10n`](https://github.com/FurryGamesIndex/games/tree/master/uil10n) 文件中定义。

当你使用库存链接时，你就无需写这么一段长字，而且无需为每种语言写一份翻译。因为库存链接是固定的，每种语言都可以自动处理。

**存在符合要求的库存链接时，请务必使用库存链接。建议把社交网站放在上方，游戏的发布页面放在下方。**

下面是FGI 支持的库存链接：

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

  

- `.release-page`: 发布页面

- `.steam`: 在 Steam 上获取

- `.epic`: 在 Epic Games Store 上获取

- `.itch.io`: 在 itch.io 上获取

- `.booth`: 在 BOOTH 上获取

- `.digiket`: 在 DiGiket 上获取

- `.play-store`: 在 Google Play 上获取

- `.apple-appstore`: 在 App Store 上获取

- `.nintendo-e-shop`: 在 Nintendo eShop 上获取

- `.playstation-store`: 在 PlayStation Store 上获取

- `.gog.com`: 在 GOG.com 上获取

- `.microsoft-store`: 在 Microsoft Store 上获取

- `.unofficial-patch-en`: 非官方英文补丁

- `.unofficial-version-en`: 非官方英文版本

- `.unofficial-patch-zh`: 非官方中文补丁

- `.unofficial-version-zh`: 非官方中文版本

- `.demo-version`: 获取演示版本

- `.demo-version-steam`: 从 Steam 获取演示版本

- `.demo-version-gog.com`: 从 GOG.com 获取演示版本

- `.unofficial-archived-download`: 下载（非官方存档）

  

如果确实需要非库存链接，则名称部分直接写就可以了，**注意这里我们要使用英文**。例如：

```
links:
  - name: R-18 Patch
    uri: https://example.com/balabala
```



#### URI

URI 部分可能是一个网址或 URL，比如上面的“在 itch.io 平台上获取”链接上，我们应该跳转打开该游戏的 itch.io 网页，因此我们填写 `https://echoproject.itch.io/adastra`

```
links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
```

部分链接可以简写成我们定义的 URI 形式，推荐使用但并非强制

- Steam: `steam:ID` 比如 `steam:570840`，相当于 `https://store.steampowered.com/app/570840`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相当于 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:用户名` 比如 `patreon:EchoGame`，相当于 `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:用户名` 比如 `tumblr:xxx`，相当于 `https://xxx.tumblr.com/`
- pixiv: `pixiv:用户ID` 比如 `pixiv:123456`，相当于 `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:用户名`, 相当于 `https://www.furaffinity.net/user/用户名/`
- DeviantART: `deviantart:用户名`, 相当于 `https://www.deviantart.com/用户名`
- Google Play Store: `google-play-store:package_id` 相当于 `https://play.google.com/store/apps/details?id=package_id`
- FGI misc page: `FGI-misc-page:name` 相当于 `<相对路径引用网站根目录>/misc/name.html`，这些页面是由 FGI 仓库中的 [`misc-pages`](https://github.com/FurryGamesIndex/games/tree/master/misc-pages) 子目录下的文件生成的。



#### 图标

图标属性是可选的，库存链接会自动获得一个相关的“图标”，比如 `.steam` 链接前将会有一个 steam 的机械 logo。但是所有的非库存链接都默认是一种图标，如果因美观等原因确实需要在自定义链接上使用非默认图标，则可以使用 `icon` 属性，该属性可以为非库存链接设置图标，亦可覆盖库存链接缺省的图标。

所有受支持的图标见 <https://github.com/FurryGamesIndex/icons/tree/master/src/site>，这里的文件名去除 `.svg` 后辍后，即为图标名称。

```
  - name: Author's weibo (DragonSnow)
    icon: weibo
    uri: https://weibo.com/u/2594829495
```



<a id="anchor_thumbnail">

### 游戏缩略图

将需要引用的图片放置于 `assets/游戏ID/` 目录下，然后在资源引用处直接填写`thumbnail.jpg`。

例如，将 `thumbnail.jpg` 放置到 `assets/Adastra/`，然后在 `Adastra.yaml` 中可以引用此图片。


```
thumbnail: thumbnail.jpg
```

#### 缩略图文件规范

> FGI 曾经未制定此严格的标准，因此旧游戏的缩略图可能不符合此规范。
>
> **对于新添加游戏的缩略图、以及更新旧游戏的缩略图，需要符合此规范。**

在规格上，**缩略图的宽高比固定为 15:7，宽度最大不得超过 360px，高度最大不得超过 168px。**尽量制作或选用最大宽高规格的缩略图，但不得强制放大原始规格的缩略图。

出于性能考虑，在与100%质量原图比较未有明显失真的条件下，**文件大小不得超过 100KiB**，且在与原图视觉效果相近的情况下优先上传更小的文件。
> 这里指的图像失真包括但不限于：振铃效应、方块效应、色调分离、噪点。



在内容上，缩略图应满足以下要求：

- 优先选用该游戏官方对外公布的图片。
- 等比例缩小图片素材。能保持相同清晰度的情况下可以放大图片素材。
- 不包含额外添加的外边框。
- 带有透明通道的图片，任何像素的透明度要么完全不透明，要么完全透明。不得出现 “半透明”的情况。
- 裁剪带有标题文字的图片时，不得将文字拦腰截断。（要么保留完整的文字，要么将整块文字全部裁剪掉）
- **不包含敏感信息。**



选用或创作的缩略图最好还能：

- 图像清晰，不出现马赛克或线性过滤造成的模糊。
- 展现游戏的整体格调、风貌。
- 尽量不要使用带有透明通道的图片。一个常见的例外是游戏官方使用的 logo 就是带有透明通道的图片。

在不造成明显的处理痕迹的前提下，可以通过图片编辑技术，改变图片中元素的相对位置。

> 对于来自 Steam 的缩略图，已自动符合该比例，通常只需要按比例缩放到 360x168 px 即可。对于来自其他地方的缩略图，通常情况下都将导致丢失信息。应尽量保证主要内容不被裁剪掉。



### 游戏截图和视频

#### 添加游戏截图

```
screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
  - sensitive: true
    uri: https://images2.imgbox.com/b8/39/pyHagTIF_o.jpg
```

- 常规图片，直接填写一个 URI字符串引用图片
- 敏感图片，应设置 `sensitive: true`，并使用 `uri` 属性引用图片

> 很多图床（如 imgur）不允许上传敏感内容，请勿使用这些图床托管敏感内容图片。

通过URI引用外部资源时需要注意：

- URI 中引用的文件需要包含可被识别的后辍，如 `.png`, `.jpg`, `.jpeg` 等等。FGI 可能需要根据此后辍设置 MIME。
- **FGI的不接受查询字符串**，例如 `https://example.com/show_image.cgi?filename=some_picture.png` 可能导致未定义行为。



#### 添加游戏视频

在游戏截图部分，可以插入游戏相关的其他媒体，如 Youtube 视频和 HTML 视频嵌入元素

- 嵌入 Youtube 视频

```
screenshots:
  - type: youtube
    id: <ID>
  - ...
```

ID 为视频 ID，可以从视频链接中获得：`https://www.youtube.com/watch?v=<ID>` 或 `https://youtu.be/<ID>`


- 嵌入 HTML 视频嵌入元素

HTML 视频嵌入元素可以提供多种类型以兼顾兼容性和性能

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





<a id="anchor_localization">

## 游戏本地化数据文件(可选)

FGI 提供了一种机制以本地化游戏页面。首先需要在 [`games/l10n`](https://github.com/FurryGamesIndex/games/tree/master/games/l10n) 目录下具体的语言目录创建和上述游戏数据文件同名的文件，即 `<游戏ID>.yaml` 作为游戏本地化数据文件。

**游戏本地化数据文件中的所有部分都是可选的，如果某项属性不需要翻译，请不要添加对应的属性。**



### 提供名称的翻译

和游戏数据文件的的格式一样，使用 `name` 提供游戏名称的翻译。

```
name: 阿达斯特拉 / Adastra
```

对于本地化的游戏名称取用：

- 优先取用目标语言的官方游戏名称。
- 按知名度排序后取用翻译质量最高的民间译名。此时应该使用这种格式 `民间翻译 / 官方原名`。

使用民间译名时，可以添加多种民间译名，如 `漏夏 / 咱的夏天 / 漏れなつ`	



### 提供描述的翻译

和游戏数据文件的的格式一样，使用 `description` 提供描述的翻译。

```
description: |
  第一行描述
  第二行描述
  ...

```

和游戏数据文件的的格式一样，可以使用 `description-format` 可以指定描述使用某种格式进行处理和渲染，例如

```
description-format: markdown
```



### 提供简化描述的翻译

和游戏数据文件的的格式一样，使用 `brief-description` 提供简化描述的翻译。

```
brief-description: |
  第一行简化描述
  第二行简化描述
  ...
```



### 提供非库存链接的翻译

我们可以提供非库存链接的翻译，例如

```
links-tr:
  "Unoffical Chinese patch (provided by 北极光汉化组)": "非官方中文补丁（由北极光汉化组提供）"
  "Unoffical Chinese patch (provided by 回音汉化组)": "非官方中文补丁（由回音汉化组提供）"
```

将链接 “Unoffical Chinese patch (provided by 北极光汉化组)” 翻译为 “非官方中文补丁（由北极光汉化组提供）”；“Unoffical Chinese patch (provided by 回音汉化组)” 翻译为 “非官方中文补丁（由回音汉化组提供）”。

> 原始链接如下，以 `.` 开头的链接是库存链接，无需也不能在本地化数据文件中翻译。
> ```
>  - name: .itch.io
>    uri: https://echoproject.itch.io/echo
>  - name: .patreon
>    uri: patreon:EchoGame
>  - name: .twitter
>    uri: twitter:EchoTheVN 
>  - name: Unoffical Chinese patch (provided by 北极光汉化组)
>    icon: twitter
>    uri: https://twitter.com/ABLocalization/status/1283925296517754887
>  - name: Unoffical Chinese patch (provided by 北极光汉化组)
>    icon: weibo
>    uri: https://weibo.com/7429628292/JbujJ0rbY
>  - name: Unoffical Chinese patch (provided by 回音汉化组)
>    icon: itch.io
>    uri: https://lupei.itch.io/echo-chinese
> ```



## 其他情况

### 注释

数据文件中可以添加注释。例如，在你违背常见的编辑方式时，可以通过注释注明特殊情况。

```
# Some comments
```

