> The Contribution Guide is under maintenance and may contain information that is partially out of date; the maintainer is planning to refactor this document.

# Contribution guide

This is a guide that describes how to add games to FurryGamesIndex (hereinafter may be referred to as FGI), and if you want to maintain an existing game, you can also learn how to do it in this guide.

Adding and maintaining games on FurryGamesIndex is really easy, it only takes a few minutes to learn.

## Step 1: Collect game information

You need to search the Internet or play games to find these informations. Note that you should not use copyrighted materials, except under the premise of fair use (such as copying game descriptions, public pictures, and limited screenshots).

- The name of the game
- Description of the game (official public description or write your own)
- Who developed the game?
- Thumbnails(usually Logo) and screenshots
- Links to games publish pages.
- Game author's website, SNS, Patreon, etc.

## Step 2: Name the game ID

> If you want to maintain existing game instead of adding one, you can skip this section

We already have the name of the game, why do we need to define an ID? This is because this project requires each games to be identified by a unique ID. The game ID can only contain English, numbers, and underscores.

- For example, you found a game called `Adastra`, which is in English, we directly use `Adastra` as the ID
- For example, if you find a game called `バカ部`, which is in Japanese, first determine whether there is an official English name. If it does not exist, use its Romanization alphabet. So we use `Bakabu` as the ID
- For example, you found a game called `家有大猫`, which is Chinese, but it has the official English name `Nekojishi`, so `Nekojishi` is the game ID. Otherwise, we may use the Pinyin `JiaYouDaMao` as the ID.
- For example, you found a game called `After Class`, which has spaces, we replace the spaces with underscores, so `After_Class` is the game ID.

## Step 3: Create a game description file

> If you want to maintain existing game instead of adding one, you can skip this section

Finally, we started the exciting part. We are going to create a YAML file to describe this game! Don't be scared by the name of YAML (YAML Ain't Markup Language), this is a format that is easy to edit directly by furries and humans. If you are only contributing to this project, you may not even understand the syntax of YAML (of course it is better to know the basic syntax)! We will learn how to edit the game description file next.

You have to create a blank file and name it `Game ID.yaml`, where `Game ID` is the game ID you named in the previous step.

> If you are using Windows, you can right-click on the folder. Create a plain text file and rename it to `xxx.yaml`. Note that you must remove the extension `.txt` part, the final file name must be `xxx.yaml` not `xxx.yaml.txt`

## Step 4: Edit the game description file

Here is a sample description file for the `Adastra` game. After seeing this ([Effect Demo](https://furrygames.top/en/games/Adastra.html)), you may already have a basic understanding of the game description file. If you still don’t understand, It does not matter, because I will introduce you to the meaning and writing of each part of the file.

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
    - zh-unofficial
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
  - name: Unofficial chinese patch
    uri: https://weibo.com/7429628292/J16RMawmi

thumbnail: thumbnail.jpg

screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

### Name

```
name: Adastra
```

The name part is `name: game name`. If the game has official English, the English name should be written. (Unlike the game ID, spaces are not converted to underscores). We will introduce the internationalization mechanism later, where to enter other languages.

If the game does not have an official English name, the name is recommended to be written as `Game ID / Original Name`. For example, `バカ部` can be set to `Bakabu / バカ部`.

### Description

```
description: |
  First line description
  Second line description
  ...

```

The format of the description section is as above. The first line is a fixed `description: |`. Write a new line to start the description. Each line of the description must start with two spaces.

English description should be written here. We will introduce the internationalization mechanism later, where to enter other languages.

> However, one exception is that if it is in the early stage of editing the entry, other languages be temporarily used, but the `sys:staging` tag must be marked.

> Use `description-format` to use rich text descriptions in special formats. Currently, `markdown` is supported. However, the function of modifying the font size will not be applicable.
>
> ```
> description-format: markdown
> ```
>
> Note: Even if you use other formats, you still need to start each line of the description with two spaces.

### Tags

```
tags:
  author:
    - 'The Echo Project'
  type:
    - visual-novel
    - bara
    - yiff
  male:
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
    - zh-unofficial
  publish:
    - itchio
    - patreon
  platform:
    - windows
    - macos
    - linux
    - android
```

The tags describe the characteristics of the game. In FGI, every tags consists of "namespace" and "value". And (unless otherwise indicated) you must use standardized tags. For example, in `type:visual-novel`, the namespace is `type` before the colon, and the value `visual-novel` follows. This label indicates that the "type" of the game is "visual novel". Similarly, `male:wolf` means that the main "male" character of the game is "wolf furry", and `misc:work-in-process` means that the game is unfinished and is under development (but the first experience/Demo is released) Version), `platform:android` means that the game can run on "Android" "platform". For all current standard tags, see [tags](tags.en.md).

> The final list of tags presented on the webpage may be increased. Because FGI uses a mechanism called "tag dependency" to add automatic tags. For example, if "male:wolf" exists, the system will add "male:canine"

Tags have no spaces, with one exception: the tags under the `author` namespace. The `author` namespace indicates the author of the work (developer, publisher, etc.). If it contains spaces, it needs to be wrapped with single quotes `'`.

The first line of the tags list format is the fixed `tags:`, and then contains multiple namespace parts. The first line of each namespace part is <code>&nbsp;&nbsp;Namespace:</code> (with two Beginning with spaces)

```
tags:
  The first namespace:
  The second namespace:
  ...
```

In each namespace, the format of each subsequent line is <code>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;value</code> (beginning with four spaces + one `-` + one space)

```
tags:
  The first namespace:
    - Value 1
    - Value 2
    - Value 3
  The second namespace:
    - Value 1
    - ...
  ...
```

### Link

```
links:
  - name: .itch.io
    uri: https://echoproject.itch.io/adastra
  - name: .patreon
    uri: patreon:EchoGame
  - name: .twitter
    uri: twitter:EchoTheVN
  - name: Unofficial chinese patch
    uri: https://weibo.com/7429628292/J16RMawmi
```

The links section is to create hyperlinks on the final game page of FGI. We usually use the game's publishing address, author's website, author's SNS, author's Patreon, etc. as links so that players can quickly find the games they need.

The first line of links is fixed `links:`, and then contains multiple blocks.

```
  - name: name
    uri: URI
```

> Please note the space before each line

The name is the name of the link, and the URI is colloquially the “URL” of the link. If you don’t know what the URI means, don’t worry.

However, it should be noted that FGI has designed something called "Stock Link" to reduce the workload of translation. The stock link name starts with `.`. They are fixed. (if you feel that new ones should be added, you can issue an issue/PR to discuss)

FGI supported stock links include the following

- `.website`: Official Website
- `.release-page`: Release page
- `.steam`: Get on Steam
- `.epic`: Get on Epic
- `.itch.io`: Get on itch.io
- `.booth`: Get on booth
- `.play-store`: Get on Google Play
- `.apple-appstore`: Get on Apple Appstore
- `.nintendo-e-shop`: Get on Nintendo E-Shop
- `.gog.com`: Get on gog.com
- `.microsoft-store`: Get on Microsoft Store
- `.twitter`: Official Twitter
- `.furaffinity`: Official FurAffinity
- `.patreon`: Patreon
- `.weibo`: Official Weibo
- `.tumblr`: Official Tumblr
- `.pixiv`: Official Pixiv
- `.discord`: Official Discord
- `.unofficial-patch-zh`: Unofficial Chinese patch
- `.unofficial-version-zh`: Unofficial Chinese version

When you use the stock link, you don’t need to write such a long word, and you don’t need to write a copy for each language, because the stock link is fixed, and each language can be processed automatically.

If you really need a non-stock link, you can just write the name part directly. Note that we will use English (and then you may need to write another name in another language) such as <code>&nbsp;&nbsp;- name: Unoffical chinese patch</code> is to create a link to an unofficial Chinese patch. (Now Adastra has used the `.unofficial-patch-zh` stock link instead of this custom link, but this document still uses the old custom link to help you understand and explain how to translate the custom link)

The URI part may be a web address or URL, such as the "Get on itch.io platform" link above, we should jump to open the game's itch.io webpage, so we fill in `https://echoproject.itch.io /adastra`

At the same time, some links can be abbreviated to the URI form we defined, recommended but not mandatory

- Steam platform: `steam:ID` such as `steam:570840`, equivalent to `https://store.steampowered.com/app/570840`
- Twitter: `twitter:tweeter` such as `twitter:EchoTheVN`, which is equivalent to `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:user name` such as `patreon:EchoGame`, which is equivalent to `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:user name` such as `tumblr:xxx`, which is equivalent to `https://xxx.tumblr.com/`
- pixiv: `pixiv:user ID` such as `pixiv:123456`, equivalent to `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:user name`, equivalent to `https://www.furaffinity.net/user/<username>/`
- Google Play store: `google-play-store:package name` such as `google-play-store:com.danfornace.loversofaether`, equivalent to `https://play.google.com/store/apps/details?id=com.danfornace.loversofaether`

icon

The stock link will automatically get a related "icon", for example, there will be a steam mechanical logo before the `.steam` link. However, all non-stock links are an icon by default. If you really need to use a non-default icon on a custom link for aesthetic reasons, such as in Changed

```
  - name: Author's weibo (DragonSnow)
    icon: weibo
    uri: https://weibo.com/u/2594829495
```

Use an optional option `icon` property to set icons for non-stock links. Currently supported icons are `website`, `steam`, `itch.io`, `twitter`, `furaffinity`, `patreon`, `weibo `, `tumblr`, `discord`, `play-store`, `apple-appstore`, `microsoft-store`

### Thumbnail

The thumbnail is the brand icon of the game and is not recommended to exceed 400x400 pixels. Prepare a jpeg or png picture. We use `thumbnail: file name` to indicate the thumbnail.

```
thumbnail: thumbnail.jpg
```

### Game screenshots

The last part is the screenshots of the game. The first line is the fixed `screenshots:`, then each line starts with <code>&nbsp;&nbsp;-&nbsp;</code> (two spaces + one `-` + one space), Then there is the external straight chain or file name of the picture.

We strongly recommend using an external image service or directly pasting the CDN address of the original picture in Steam, etc. If you must host it in FGI, you can write only a file name, such as <code>&nbsp;&nbsp;-&nbsp;1.webp</code>

```
screenshots:
  - https://i.imgur.com/mue7WCx.png
  - https://i.imgur.com/syIeL3g.png
```

Embed special screenshots

- Screenshots of sensitive content

	If you want to add screenshots with sensitive content (R-18, NSFW, Yiff) in the game screenshots, first set `sensitive_media: true`, and use the following format on the sensitive screenshot items

	```
	  - sensitive: true
	    uri: <address>
	```

	The final effect is as follows

	```
	sensitive_media: true

	screenshots:
	  - https://i.imgur.com/...
	  - https://i.imgur.com/...
	  - sensitive: true
	    uri: https://images2.imgbox.com/b8/39/pyHagTIF_o.jpg
	```

	> Many image services (such as imgur) are not allowed to upload sensitive content, please do not use these services to host sensitive content pictures.

In the screenshot section of the game, you can insert other media related to the game, such as Youtube video and HTML video embedded elements

- Embed YouTube videos

	```
	  - type: youtube
	    uri: youtube:<ID>
	```

	The ID is the video ID, which can be obtained from the video link: `https://www.youtube.com/watch?v=<ID>` or `https://youtu.be/<ID>`

- Embed HTML video embedded elements

	HTML video embedded elements can provide multiple types to balance compatibility and performance

	```
	  - type: video
	    src:
	      - uri: https://example.com/1.webm
		mime: video/webm
	      - uri: https://example.com/1.mp4
		mime: video/mp4
	```

## Step 5: Translate key information

Now that we have a file describing game information, we are not far from success! Next (an optional step) we need to prepare translation files for non-English users. If your native language is not English, it is recommended to provide a translation file for your native language. If your native language is Chinese, you can prepare another `Game ID.yaml` file (same name as the file in the previous step), you can Put it in the `l10n/zh-cn/` directory.

The structure of this file is very simple, only three parts

```
name: 阿达斯特拉 / Adastra

description: |
  你在罗马留学时突然被外星人绑架。他想从你那里得到什么？好吧，他似乎不想告诉你真相。而在搞明白发生了什么之前，你已经被带到了离地球一百万英里之外的地方。
  阿达斯特拉（Adastra）是一部融合了大量科幻和政治阴谋的浪漫主义视觉小说。你将体验在一个动荡帝国中的冒险，同时还要决定应该信任或不信任谁。
  在这种充满背叛和阴谋的氛围下，您开始怀疑绑架您的外星人是否是您最信任的人。

links-tr:
  "Unoffical chinese patch": "非官方中文补丁"
```

Among them, the name (name) and description (description) is the same as the format in step 4, but you should translate it into the target language. It is worth mentioning that if the game does not have an official name translation in that language, you should use this format `Private Translation/Official Original Name`

> If there are many kinds of folk translations, it is recommended to write all common names as much as possible, such as `漏夏 / 泄漏的夏天 / 咱的夏天 / 漏れなつ。`, but do not write translations of non-primary languages (here Japanese)) in Chinese translations, such as `Morenatsu`

The links-tr part is the more interesting part. Remember the "non-stock link" in step 4, here, we want to translate the **non** stock links into the local language. The format is fixed in the first line `links-tr:`, and the format of each subsequent line is <code>&nbsp;&nbsp;"The name created in step 4:" "Translation"</code>. There is no need to translate stock links (this is how we use stock links to avoid duplicate translation works).

## Step 6: Send us the game description file and resource file to us

We now have multiple files, you now have two options, if you will use Github, it is recommended that you send a Pull Request, otherwise you can contact me through [Telegram](https://telegram.org) [@UtopicPanther](https://t.me/UtopicPanther).

If you want to send Pull Request, you should organize the file like this:

First fork this repo to your account. (It is recommended that you create a branch and then modify it). You need to create/modify these files

- `games/GameID.yaml` - the game description file you edited in step 4
- `games/l10n/${language}/GameID.yaml` - the translation file you edited in step 5. Correspondingly placed in the sub-directory of the corresponding language, such as Chinese `games/l10n/zh-cn/GameID.yaml`
- `assets/GameID/...` - dependent resource files, such as your prepared thumbnails, in the above example, `assets/Adastra/thumbnail.jpg`

**Indicate your identity (recommended, but you can not write if you want to remain anonymous): edit the file of `CONTRIBUTORS.md` in the root directory and write your name, contribution and contact information to the file! Your contribution should not be forgotten!** (If you send via Telegram, don’t send this file, just send your personal information to me)

Commits your changes and send a pull request to FGI!

> After sending the Pull Request and merging, if you want to contribute again, it is recommended to delete the repo after the fork and re-fork; the local repo recommends `git pull`. Then create a branch and modify it (or use [this method](https://github.com/FurryGamesIndex/games/wiki/%E8%B4%A1%E7%8C%AE%E8%80%85%E7%9A%84%E5%A4%87%E5%BF%98%E5%BD%95%EF%BC%9A%E4%BD%BF%E7%94%A8-Git-%E8%B4%A1%E7%8C%AE%E7%9A%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)).
