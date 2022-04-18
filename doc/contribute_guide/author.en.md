# Contribution guide - Author

This is a guide that describes how to add authors to FurryGamesIndex (hereinafter may be referred to as FGI), Currently at this stage of draft.

While learning the instruction, you can take an advanced comprehension by looking through files of [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors) directory. Or take it as reference as modifying or adding description file.

## Author ID

Author ID is a string for linking with author description file. The following is its requirement:

- Each author is to be identified by a unique ID without duplicate. Once determined, modification is not allowed in usual.
- Author ID only contain alphabet (upper and lower case), number and underscores in ASCII character set.
- Author ID can not start with a `_`, but can start with two and more `_`. The number of underscores in other positions has no such requirement.

The following is a guide for defining the Author:

- For example, if the author called `Rimentus`, which is in English, we directly use `Rimentus` as the ID.
- For example, if the author called `とりあえず`, which is in Japanese, but it has the official English name or username, so `toriaezu13` is the author ID. Otherwise, we may use its Romanization alphabet `toriaezu` as the ID.
- For example, you found a game called `Black Sun Di`, which has spaces, we replace the spaces with underscores, so `Black_Sun_Di` is the author ID.

## Author Description File

Each author shown on FGI website is made by the description file in author database. The description file is kept in subdirectory of [`authors`](https://github.com/FurryGamesIndex/games/tree/master/authors).

To edit existed author page, just find and edit its description. To create a new author page, you need to create a new author description file. The filename of the description file is.

```
<Author ID>.yaml
```

For example, The author “The Echo Project”, whose description files is `The_Echo_Project.yaml`.

When editing author description file, you need to take care whether the content satisfied the format specification of YAML, otherwise FGI will not use this file correctly.

> The Author Description File uses UNIX (LF) line break, otherwise FGI may not work in expect.
>
> The repository use `.gitattributes` forcing git to use LF line break, in usual the standard git software can work correctly.

Now we will introduce each part in author description file to you.

### Composition of Description File

To increase the readability of description file, you must insert a blank line behind each first-level attribute(the last is optional).

For Example

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

Besides, note the indented spaces in the following grammar, the position and amount of space must conform the definition.

### Name

```
name: Author Name
```

The Name is the same as author ID, includes space but not underscores (if it has).

### Aliases

```
aliases:
  - alias1
  - alias2
  ...
```

An author may have two and more Aliases. The Aliases mean the other name of the author. It's searchable to FGI.

### Author Type

```
type: personal
```

The Author Type provides the following options:

- `unknown`: Unknown
- `personal`: Personal
- `small-team`: Independent Team
- `company`: Company
- `publisher`: Publisher

For example, The Echo Project, as one of author of the game *Echo*, is an independent team, so there is `small-team`.

### Avatar

The Avatar can be inner referred through filename.

Place the picture need be referred into the directory of assets/_avatar/, then type the filename on the referring.

For example, place Black_Sun_Di.jpg into assets/_avatar/, Then referring this picture in Black_Sun_Di.yaml, such as:

```
avatar: Black_Sun_Di.jpg
```

#### Image File Specification

FGI have a clear requirement on author's avatar, in size, both the length and width of picture are 64 pixels. Making or using picture that have same and more required pixels, and crop it.

For performance, under the condition that no significant distortion comparing with the 100% quality original image, the size of file can not exceed 10KiB. And priority upload less sized file if its quality is similar to the original image.

### Link

```
links:
  - name: Name
    uri: URI
  - name: Name
    icon: icon (optional)
    uri: URI
  - ...
```

The links section is to create hyperlinks on the final game page of FGI. We usually use the author's publishing address, author's social platforms, author's Patreon, etc.

The Name is name of the URI. In general terms the URI means a link of a website. If you're not able to clear the meaning, just ignore it.

#### Name

FGI has designed something called "Stock Link" to reduce the workload of translation. The stock link name starts with `.`. They are fixed. It required to be defined in the files [`uil10n`](https://github.com/FurryGamesIndex/games/tree/master/uil10n).

FGI supported stock links include the following:

- `.website`: Official Website
- `.twitter`: Official Twitter
- `.furaffinity`: Official FurAffinity
- `.deviantart`: Official DeviantART
- `.patreon`: Official Patreon
- `.weibo`: Official Weibo
- `.tumblr`: Official Tumblr
- `.pixiv`: Official Pixiv
- `.discord`: Official Discord
- `.youtube`: Official Youtube
- `.facebook`: Official Facebook

When you use the stock link, you don’t need to write such a long word, and you don’t need to write a copy for each language, because the stock link is fixed, and each language can be processed automatically.

When exists requirement matched stock link, it's mandatory using stock link.

If you really need a non-stock link, you can just write the name part directly. Note that we will use English. Such as:

```
  - name: WildDream
    uri: https://www.wilddream.net/user/balabala
```

#### URI

The URI part may be a web address or URL, such as the "Get on YouTube platform" link above, we should jump to open the authors YouTube homepage, so we fill in `https://www.youtube.com/c/MightAndDelight`

At the same time, some links can be abbreviated to the URI form we defined, recommended but not mandatory

- Steam: `steam:ID` such as `steam:570840`, which is equivalent to `https://store.steampowered.com/app/570840`
- Twitter: `twitter:tweeter` such as `twitter:EchoTheVN`, which is equivalent to `https://twitter.com/EchoTheVN/`
- Patreon: `patreon:user name` such as `patreon:EchoGame`, which is equivalent to `https://www.patreon.com/EchoGame`
- Tumblr: `tumblr:user name` such as `tumblr:xxx`, which is equivalent to `https://xxx.tumblr.com/`
- pixiv: `pixiv:user ID` such as `pixiv:123456`, which is equivalent to `https://www.pixiv.net/users/123456`
- Furaffinity: `furaffinity:user name`, which is equivalent to `https://www.furaffinity.net/user/username/`
- DeviantART: `deviantart:user name`, which is equivalent to `https://www.deviantart.com/username`
- FGI misc page: `FGI-misc-page:name`, which is equivalent to `<Relative path referring to the root of site>/misc/name.html`, these pages are files of subdirectory of [`misc-pages`](https://github.com/FurryGamesIndex/games/tree/master/misc-pages) on FGI repository.
