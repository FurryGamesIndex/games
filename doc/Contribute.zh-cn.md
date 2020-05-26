# 贡献指南

这是一篇介绍如何向 FurryGamesIndex (下文中可能简称 FGI) 添加游戏的指导，但是如果你想维护现有游戏，你也可以在这篇指导中学会方法。

在 FurryGamesIndex 上添加和维护游戏真的非常简单，只需要花费几分钟的时间了解。

## 第一步：收集游戏信息

你需要通过互联网搜索或游玩游戏来找到这些信息。注意，在使用信息时请勿使用版权材料，除非在合理使用的前提下（例如拷贝游戏简介、公开图片和有限的截图）。

- 游戏的名字
- 游戏的描述（官方公开描述或自己编写）
- 游戏是谁开发的？
- 缩略图和截图
- 获取游戏的链接
- 游戏作者的网站、社交平台和 Patreon 等

## 第二步：命名游戏 ID

> 如果你要维护游戏而不是添加游戏，可以跳过本节

我们已经有了游戏的名字，为什么还需要定义一个 ID？这是由于，本项目要求每个游戏都要有一个唯一的 ID 进行标识，游戏 ID 只能包含英文、数字和下划线。

- 例如，你找到了一个叫 `Adastra` 的游戏，这是英文，我们直接使用 `Adastra` 作为 ID
- 例如，你找到了一个叫 `バカ部` 的游戏，这是日文，首先确定是否存在官方英文名，如果不存在，应使用其罗马字母表示。因此我们使用 `Bakabu` 作为 ID
- 例如，你找到了一个叫 `家有大貓` 的游戏，这是中文，但它有官方英文名称 `Nekojishi`，因此 `Nekojishi` 是游戏 ID。否则我们可能使用其拼音 `JiaYouDaMao` 作为 ID。
- 例如，你找到了一个叫 `After Class` 的游戏，它有空格，我们将空格替换为下划线，即 `After_Class` 是游戏 ID。

## 第三步：创建游戏描述文件

> 如果你要维护游戏而不是添加游戏，可以跳过本节

终于，我们开始了激动人心的部分。我们要创建 YAML 文件来描述这个游戏了！别被 YAML（YAML Ain't Markup Language）的名字吓到，这是一种很易于兽人和人类直接编辑的格式。如果你只是为本项目贡献，你甚至都可以不了解 YAML 的语法（当然了解一下基本语法会更好）！我们接下来会学习如何编辑游戏描述文件。

你要创建一个空白文件，命名为 `游戏ID.yaml`，`游戏ID` 就是你上一步中命名的游戏 ID。

> 如果你使用的 Windows，你可以在文件夹中右键-新建-文本文档，并将其改名为 `xxx.yaml`，注意你必须将扩展名 `.txt` 部分移除，最后的文件名需要是 `xxx.yaml` 而不能是 `xxx.yaml.txt`

## 第四步：编辑游戏描述文件

这里首先给出 `Adastra` 游戏的一个样板描述文件。看到这个模板（[效果演示](https://furrygamesindex.github.io/zh-cn/games/Adastra.html)），你可能已经对游戏描述文件有一个基本了解了，即使你仍然不明白，也没有关系，因为接下来，我会给你介绍每一部分的含义和写法。

```
name: Adastra

description: |
  You're having the time of your life in Rome on a study abroad program when you're suddenly abducted by an alien. What does he want from you? Well, he doesn't seem to want to tell and, before you know it, you're millions of miles away from Earth on your way to a place you know nothing about.
  Adastra is a romance visual novel with a whole bunch of sci-fi and political intrigue mixed in. You'll experience the perils of navigating an empire in turmoil while deciding who you should and who you definitely shouldn't trust.
  In this climate of turncoats and backstabbers, you start to wonder if the alien that abducted you is the one person you can trust the most.

tags:
  author:
    - 'The Echo Project'
  type:
    - visual-novel
    - bara
    - yiff
  male:
    - canine
    - felidae
    - wolf
    - cat
    - humankind
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
    - zh-unoffical
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android

links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
  - name: .patreon
    uri: patreon:EchoGame
  - name: .twitter
    uri: twitter:EchoTheVN 
  - name: Unoffical chinese mod
    uri: https://weibo.com/7429628292/J16RMawmi

thumbnail: thumbnail.jpg

screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

### 名称

```
name: Adastra
```

名称部分是 `name: 游戏名称`，如果游戏有官方英文，应写英文名称。（和游戏ID不同，空格不转换为下划线）。我们会在后面介绍国际化机制，在哪里输入其他语言。

如果游戏没有官方英文名称，则名称推荐写为 `游戏ID / 原名`。比如 `バカ部` 可以设置为 `Bakabu / バカ部`。

### 描述

```
description: |
  第一行描述
  第二行描述
  ...

```

描述部分的格式如上。第一行是固定不变的 `description: |`，换行开始编写描述，描述的每一行都要以两个空格开头。

此处应写英文描述。我们会在后面介绍国际化机制，在哪里输入其他语言。

> 但是，一个例外是，如果是该条目编辑的早期，允许暂时使用其他语言，但是必须标记 `sys:staging` 标签。


> 使用 `description-format` 可以使用特殊格式的富文本描述，目前支持 `markdown`。但修改字体大小的功能可能不适用。
> 
> ```
> description-format: markdown
> ```
> 
> 注意：即使使用其他格式，仍然需要使描述的每一行以两个空格开头。

### 标签

```
tags:
  author:
    - 'The Echo Project'
  type:
    - visual-novel
    - bara
    - yiff
  male:
    - canine
    - felidae
    - wolf
    - cat
    - humankind
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
    - zh-unoffical
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android
```

标签是描述游戏的特性。在 FGI 中，标签由“命名空间”和“值”组成。并且必须使用标准化的标签。如 `type:visual-novel` 中，命名空间是冒号前面的 `type`，后面的是值 `visual-novel`。这个标签表示该游戏的「类型」是「视觉小说」。同样 `male:canine` 表示该游戏存在主要「男性」角色是「犬科兽人」，`misc:work-in-process` 表示该游戏「未完成」，正在开发中（但发布了先行体验/Demo版本），`platform:android` 表示该游戏可以在「Android」「平台」上运行。有关目前所有标准标签，见 [标签](tags.zh-cn.md)。

标签不带空格，除了一个例外，就是 `author` 命名空间下的标签。`author` 命名空间指示作品的作者（开发者、发行者等）。如果包含空格，需要使用单引号`'`包裹起来。

tags 列表的格式第一行是固定的 `tags:`，然后包含多个命名空间部分，每个命名空间部分的第一行是 <code>&nbsp;&nbsp;命名空间:</code>（以两个空格开头）

```
tags:
  第一个命名空间:
  第二个命名空间:
  ...
```

在每一个命名空间中，之后的每一行格式是 <code>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;值</code>（以四个空格+一个`-`+一个空格开头）

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

### 链接

```
links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
  - name: .patreon
    uri: patreon:EchoGame
  - name: .twitter
    uri: twitter:EchoTheVN 
  - name: Unoffical chinese mod
    uri: https://weibo.com/7429628292/J16RMawmi
```

链接为 FGI 最终的游戏页面上创建超链接，我们通常将游戏的发布地址、作者的网站、作者的社交平台、作者的 Patreon 等等作为链接以便让玩家可以快速找到需要的游戏。

链接的第一行是固定的 `links:`，然后包含多个块。

```
  - name: 名称
    uri: URI
```

> 请注意每行前面的空格

名称为链接的名称，URI 通俗地说是该链接的“网址”，如果你不清楚 URI 的意思，也无需在意。

但是，需要注意的是，FGI 设计了一种叫“库存链接”（Stock Link）的东西减少翻译的工作量。库存链接名称以 `.` 开头。它们是固定的，不能自行定义（如果你觉得应该增加新的，可以发 issue/PR 讨论）

FGI 支持的库存链接包括以下几个

- `.website`: 官方网站
- `.itch.io`: 在 itch.io 平台上获取
- `.steam`: 在 Steam 平台上获取
- `.patreon`: Patreon (在 Patreon 平台上赞助作者)
- `.twitter`: 官方 Twitter
- `.furaffinity`: 官方 FurAffinity
- `.weibo`: 官方微博
- `.tumblr`: 官方 Tumblr
- `.discord`: 官方 Discord
- `.unoffical-patch-zh-cn`: 非官方简体中文补丁
- `.unoffical-ver-zh-cn`: 非官方简体中文版本
- `.unoffical-patch-zh-tw`: 非官方繁体中文补丁
- `.unoffical-ver-zh-tw`: 非官方繁体中文版本

当你使用库存链接时，你就无需写这么一段长字，而且无需为每种语言写一份，因为库存链接是固定的，每种语言都可以自动处理。

如果确实需要非库存链接，则名称部分直接写就可以了，注意这里我们要使用英文（然后可能还需要再在它处写其他语言的名称）比如本例的 <code>&nbsp;&nbsp;- name: Unoffical chinese patch</code>，是创建一个指向非官方中文补丁的链接。（现在 Adastra 已经使用 `.unoffical-patch-zh-cn` 库存链接代替此自定义链接，但本文档仍然使用旧的自定义链接以帮助你理解以及说明自定义链接的翻译方法）

URI 部分可能是一个网址或 URL，比如上面的“在 itch.io 平台上获取”链接上，我们应该跳转打开该游戏的 itch.io 网页，因此我们填写 `https://echoproject.itch.io/adastra`

同时，部分链接可以简写成我们定义的 URI 形式，推荐使用但并非强制

- Steam 平台: `steam:ID` 比如 `steam:570840`，相当于 `https://store.steampowered.com/app/570840`
- Twitter: `twitter:推主` 比如 `twitter:EchoTheVN`，相当于 `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:用户名` 比如 `patreon:EchoGame`，相当于 `https://www.patreon.com/EchoGame`

图标

库存链接会自动获得一个相关的“图标”，比如 `.steam` 链接前将会有一个 steam 的机械 logo。但是，所有的非库存链接都默认是一种图标，如果因美观等原因确实需要在自定义链接上使用非默认图标，例如在 Changed 中

```
  - name: Author's weibo (DragonSnow)
    icon: weibo
    uri: https://weibo.com/u/2594829495
```

使用一个可选选项 `icon` 属性可以为非库存链接设置图标，目前支持的图标有 `website`, `steam`, `itch.io`, `twitter`, `furaffinity`, `patreon`, `weibo`, `tumblr`

### 缩略图

缩略图是游戏的品牌图标，不推荐超过 400x400 像素。准备好一个 jpeg 或 png 图片。我们使用 `thumbnail: 文件名` 指示该缩略图。

```
thumbnail: thumbnail.jpg
```

### 游戏截图

最后是游戏截图部分，第一行是固定的 `screenshots:`，随后每一行以 <code>&nbsp;&nbsp;-&nbsp;</code> 开头（两个空格+一个`-`+一个空格），然后是图片的外部直链或文件名。

我们强烈推荐使用外部图床或直接贴原 Steam 中的图片 CDN 地址等，来存放截图，如果一定要在 FGI 中托管，可以只写一个文件名，如 <code>&nbsp;&nbsp;-&nbsp;1.webp</code>

```
screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

敏感内容截图

	如果游戏截图要添加带有敏感内容（R-18，NSFW，Yiff）的截图，首先请设置`sensitive_media: true`，并在敏感的截图项上使用以下格式

	```
	  - sensitive: true
	    uri: <地址>
	```

	最终效果如下

	```
	sensitive_media: true

	screenshots:
	  - https://i.imgur.com/...
	  - https://i.imgur.com/...
	  - sensitive: true
	    uri: https://images2.imgbox.com/b8/39/pyHagTIF_o.jpg
	```

	> 很多图床（如 imgur）不允许上传敏感内容，请勿使用这些图床托管敏感内容图片。

在游戏截图部分，可以插入游戏相关的其他媒体，如 Youtube 视频和 HTML 视频嵌入元素

嵌入 Youtube 视频`

	```
	  - type: youtube
	    uri: youtube:<ID>
	```

	ID 为视频 ID，可以从视频链接中获得：`https://www.youtube.com/watch?v=<ID>` 或 `https://youtu.be/<ID>`

嵌入 HTML 视频嵌入元素

	HTML 视频嵌入元素可以提供多种类型以兼顾兼容性和性能

	```
	  - type: video
	    src:
	      - uri: https://example.com/1.webm
		mime: video/webm
	      - uri: https://example.com/1.mp4
		mime: video/mp4
	```

## 第五步：翻译关键信息

现在我们有了描述游戏信息的文件，我们已经离成功不远了！接下来（一个可选的步骤）我们需要为非英文用户准备翻译文件。如果你的母语不是英语，推荐为自己的母语提供一份翻译文件，假如你的母语是中文，你可以再准备一份 `游戏ID.yaml` 文件（和上一步中的文件同名），你可以把它放到 `l10n/zh-cn/` 目录下。

这个文件的结构就非常简单了，只有三部分

```
name: 阿达斯特拉 / Adastra

description: |
  你在罗马留学时突然被外星人绑架。他想从你那里得到什么？好吧，他似乎不想告诉你真相。而在搞明白发生了什么之前，你已经被带到了离地球一百万英里之外的地方。
  阿达斯特拉（Adastra）是一部融合了大量科幻和政治阴谋的浪漫主义视觉小说。你将体验在一个动荡帝国中的冒险，同时还要决定应该信任或不信任谁。
  在这种充满背叛和阴谋的氛围下，您开始怀疑绑架您的外星人是否是您最信任的人。

links-tr:
  "Unoffical chinese patch": "非官方中文补丁"
```

其中，名字（name）和描述（description）和第 4 步中的格式一样，只是你应该将其翻译为相应语言。值得一提的是，如果游戏没有该语言的官方名字翻译，你应该使用这种格式 `民间翻译 / 官方原名`

> 如果民间翻译有多种，则推荐尽可能将常用名都写上，如 `漏夏 / 泄漏的夏天 / 咱的夏天 / 漏れなつ。`，但不要在中文翻译中写非主要语言（这里是日语）的翻译，如 `Morenatsu`

links-tr 部分是比较有趣的部分，还记得第 4 步中的“库存链接”吗，我们这里，要将**非**库存链接翻译成本地语言。格式为第一行固定 `links-tr:`，随后每一行的格式是 <code>&nbsp;&nbsp;"第 4 步中创建的名字": "翻译"</code>。库存链接无需翻译(我们正是这样利用库存链接避免重复的翻译工作)。

## 第六步：将你编辑的游戏描述文件和资源文件发送给我们

我们现在有了多个文件，你现在有两个选择，如果你会使用 Github，推荐你发送 Pull Request，否则你可以通过 [Telegram](https://telegram.org) 联系我 [@UtopicPanther](https://t.me/UtopicPanther) 发送。

如果你要发送 Pull Request，你应该这样组织文件：

首先将本仓库 fork 到你的账户下。（推荐你创建一个分支再修改）。你需要创建/修改这几个文件

- `games/游戏ID.yaml` - 你在第 4 步中编辑的游戏描述文件
- `games/l10n/${language}/游戏ID.yaml` - 你在第 5 步中编辑的翻译文件。对应放到相应语言的子目录中，如中文 `games/l10n/zh-cn/游戏ID.yaml`
- `assets/游戏ID/...` - 依赖的资源文件，比如你准备的缩略图，上例中为 `assets/Adastra/thumbnail.jpg`

**注明你的身份（推荐，但如果你想保密，可以不写）：编辑根目录下的 `CONTRIBUTORS.md` 的文件，把你的大名、贡献和联系方式写到文件中！你的贡献不应该被遗忘！**（如果你通过 Telegram 发送，不要传这个文件，直接将你的个人信息发送给我即可）

签入你的修改，然后向 FGI 发送 Pull Request 吧！

> 发送 Pull Request 合并后，如果希望再次贡献，建议删除 fork 后的仓库重新 fork；本地仓库建议 `git pull`。然后再创建分支并修改。
