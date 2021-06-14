# 提交补丁的注意事项

当通过 Github Pull request 提交补丁时，建议尽可能得使一个 pull requst 尽可能的小，涉及面尽可能窄。例如编辑游戏数据文件的 pull request 中不应该修改文档、模板、样式表或代码（修改标签定义文件是可以容忍的），添加游戏数据文件时也不要同时添加多个完全不相关的游戏。

我们要求在 git 中**最终**记录的 commits 消息符合以下格式。

```
[标识] 组件或范围: 子组件: 摘要 (引用)
```

在大多数情况下，不使用 `[标识]`，`子组件:` 和 `(引用)`（或其中几部分），`组件或范围:` 和 `摘要` 是不可省略的。即消息的格式很可能为

```
组件或范围: 摘要
```

**您可以在 pull request 的提交中使用混乱的提交格式，因为在这种情况下维护者会采用压缩合并，使其变为一条提交，然后维护者会为您编写一个合适的 commits 消息。** 这主要是便于那些直接在 Github 网页上编辑的贡献者。但是如果您的一个 pull request 中修改了 FGI 中互不相关的几个部分，当维护者认为难以编写提交消息时，维护者可能要求您整理您的修改并重新发起 pull request。

> 如果 pull request 中每个提交都符合此要求，维护者应该首选采用默认的合并方式（类似于 git 的非快进合并）。以便修改记录尽可能详细。

这就是为什么您的 pull request 应该尽可能小的原因。

**如果您确实希望同时修改多个部分，则我们强烈建议您同时提交多个 pull request（您需要在 fork 后的仓库中创建多个分支）。**

本文中的所有做法都是为了尽可能使提交历史记录具体、便于搜索，为审查工作提供便利。

以下是一些如果编写提交消息的例子：

## 核心部分

除非另有说明，`组件或范围: ` 使用文件路径。不带扩展名。

### 游戏和作者

添加 Adastra 游戏：

> 可同时添加游戏缩略图等资源，无需在消息中体现这一点。

```
games/Adastra: new game
```

添加 The Echo Project 作者：

> 可同时添加作者头像图片文件，无需在消息中体现这一点。

```
authors/The_Echo_Project: new author
```

更新 Adastra 游戏的标签和链接：

```
games/Adastra: update tags and links
```

更新 Adastra 游戏额中文本地化补丁链接：

```
games/Adastra: update link of chinese l10n patch
```

更新 Adastra 游戏的缩略图

> 除非是仅更新游戏的缩略图，否则我们反而建议将更新图片和更新数据文件合并到一个提交，提交信息可以体现更新了缩略图。

```
assets/Adastra: update thumbnail.jpg
assets/_avatar/The_Echo_Project: update avatar
```

更新多个游戏数据文件时：

```
games: update author info for 3 games from Echo Project
games: remove deprecated property sensitive_media for all entities
```

更新 Adastra 条目的翻译数据文件（不体现语言的变体）：

```
games/l10n/zh: Adastra: update translation for description
```

更新 Adastra 条目的翻译数据文件，涉及到 `X-Chinese-Convertor-Hint` 变体相关的属性时，应指定变体：

```
games/l10n/zh-tw: Adastra: set X-Chinese-Convertor-Hint
```

更新多个游戏条目的翻译数据文件：

```
games/l10n/zh: add description-format for all entries
```

### 代码

对代码修改时，当一个模块包含多个类时，且只对其中一个类进行修改时，可以使用 `子组件: ` 指定类的名字。

```
fgi/game: GameDescription: initial brief-description support
test/tagmgr: update unit test case
scripts/build-next: do not use uimod plugin
```

例外1: 对于插件代码（fgi/plugins/...），`组件或范围: ` 中应删除 `fgi/` 前辍，剩余部分遵守文件路径。

```
plugins/steam-cdn-unite: add new akamai CDN URI prefix
```

例外2：对于渲染器代码（fgi/renderers/...）`组件或范围: ` 中应删除 `fgi/` 前辍，剩余部分遵守文件路径。

> 历史上，`fgi/renderers/` 目录曾经是 `renderers/`，此要求保证了格式与历史消息格式相同。

```
renderers/list: initial multi-klass support
```

### 模板和样式表

```
templates: fixup xxx bug
```

```
templates/list: use list_item widget
```

```
templates/peafowl-private/header: fixup opengraph description escape
```

样式表文件虽然存放于 `webroot/styles/`，但 `组件或范围: ` 中应删除 `webroot/` 前辍，剩余部分遵守文件路径。

```
styles/32_game_entry: add workarounds for Mozilla Firefox
```

### Webroot

例外1: webroot/base/ 下的文件，`组件或范围: ` 中应将 `webroot/base/` 前辍改为 `webroot/`，剩余部分遵守文件路径。

> 历史上，`webroot/base/` 目录曾经是 `webroot/`，此要求保证了格式与历史消息格式相同。

```
webroot/robots: disallow /classic-ui
webroot/scripts/searchexpr: initial @reverse and @lastmod support
```

例外2: service worker 文件直接使用 `sw: ` 作为 `组件或范围: `。

```
sw: proactive opaque cache avoiding
```

### UI l10n 资源文件

文件路径中不体现语言变体。

```
uil10n/zh: add translation for ...
uil10n/zh: add translation for many keys
```

但是，如果修改 `_PRIVATE.yaml` 后辍的文件，应指定语言变体。同时使用 `PRIVATE: ` 作为 `子组件`。

```
uil10n/zh-tw: PRIVATE: add hotfix for list-klass-platform-mobile
```

### 文档

```
doc/search_help: add more exampless
```

### staging-ui 和 classic-ui

如果修改 `staging-ui` 和 `classic-ui` 下的文件，则应该使用 `staging-ui: ` 或者 `classic-ui/UI包代号: ` 作为 `组件或范围: `，同时使用剩余的文件名部分作为 `子组件`。

```
staging-ui: styles/32_game_entry: add workarounds for Mozilla Firefox
classic-ui/pioneer: templates/pioneer-private/header: fixup build
```

### git 子模块

> 这种情况下永不使用 `子组件:`

通过 git 子模块（git submodule）引入的组件的提交消息是非常形式化的。只有以下两种情况。

被 FGI 组织正式维护的仓库，使用以下提交消息表明更新到最新版本。

```
icons: bump to lastest version
```

由第三方维护的仓库，使用以下提交消息表明更新到上游某一版本，`master` 可以替换为大部分的 git 引用，可以是分支名、标签或 commmit hash，但不能是 HEAD 等。

```
some_thirdparty/some_submodule: bump to upstream master
```

### 全树范围

全树范围（`treewide`）表示修改覆盖了整个源代码树，通常是和具体组件不太相关的修改。

> 这种情况下永不使用 `子组件:`

例如如下的修复文件换行符号或运行中文转换器的提交：

```
treewide: fixup line endings
treewide: run zhconv
```

## 标识

目前 FGI 只有一种标识，`[DO NOT MERGE]`。

### `[DO NOT MERGE]` 标识

`[DO NOT MERGE]` 声明此提交不提交到主分支，且不应该被合并到主分支。

例如如下的消息，在 FGI-next 构建中禁用隐私政策的 hack：

```
[DO NOT MERGE] next: renderers/nonl10n/singles: disable privacy-policy page
```

## 引用

引用为查找和此补丁修改内容的相关地址，以便于审查者通过这些链接找到和此修改的更多原因和其他信息。如 `PR #数字` 引用 pull request，`Fixed #数字` 引用相关的 issues。

以下是一些例子：

```
games/Adastra: new game (PR #23333)
games/Adastra: use stock link for chinese patch (PR #23335, Fixed #23334)
games/Adastra: use stock link for chinese patch (Fixed #23334)
```

## 例外情况

有几种例外情况是不需要（完全）符合此格式。

1. 使用 `git revert` 撤销提交时，使用默认的 `Revert "..."` 格式。`"..."` 需要符合本文规定的格式或（递归地符合）此例外情况。

2. 使用 `git merge --no-ff` 或 github 默认的 pull request 合并方式时，使用默认的 `Merge ...` 格式

	不允许非必要的 `Merge ...` 合并消息。如果您的代码库需要更新时，建议首选 `git pull --rebase`。
	
	如果有此类提交，维护者可能会采用压缩合并并重新编写提交消息。
