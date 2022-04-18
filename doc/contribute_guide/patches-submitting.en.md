# Note on Patches Submitting

When you submit Patch(es) through Pull Request on GitHub, it recommended making a pull request smaller and narrower if possible. For example, a pull request with a modification of game description file(s) should not contain the modification of document, template, style and code (it's tolerant to modify the tags defined file). And should not add multiple completely unrelated games when adding game description file.

We require the **FINAL** recorded commits on git content the following format.

```
[Identifier] Mod or Range: Sub Mod: Summary (Referring)
```

In most instances, no need to use `[Identifier]`，`Sub Mod:` and `(Referring)` (or parts of it), but `Mod or Range` is necessary. i.e. the final format of submits can be:

```
Mod or Range: Summary
```

**You can use chaotic submitting format in pull request, because the maintainer will use 'Squash and merge' making them be one submit. Then maintainer will write a proper commits message for you.** This is mainly convenient for those contributors who modifying through GitHub website. If the maintainer considers it hard to write a commit message, he/she will require you to collate your modification and re-pull request.

> If each submit on pull request contents the requirement. The maintainer should use default merge (similar to non-fast merge on git) to make the edition records as detailed as possible.

This is why your pull request should be as small as possible.

**If you still want to modify multiple parts at a time, we strongly recommend that you submit multiple pull request simultaneously. (you need to create multiple branches in forked repository.**

All these things in this article is making the records of former commit more specific and searchable, for the easier review process.

The following is examples of writing submitting message.

## The Core

Unless extra indication, `Mod or Range: ` use path of file, with no filename extension.

### Game and Author

Add game Adastra：

> You can add resource like game thumbnail, etc., no need to reflect this in message.

```
games/Adastra: new game
```

Add author The Echo Project:

> You can add resource like avatar file, etc., no need to reflect this in message.

```
authors/The_Echo_Project: new author
```

Update tag and link of game Adastra：

```
games/Adastra: update tags and links
```

Update link of Chinese localization patch of game Adastra:

```
games/Adastra: update link of chinese l10n patch
```

Update thumbnail of game Adastra

> Unless updating game thumbnail only, we suggest that combining updating of image and data files into one commit. Submitting information can reflect that the thumbnail has updated.

```
assets/Adastra: update thumbnail.jpg
assets/_avatar/The_Echo_Project: update avatar
```

While updating multiple game description files:

```
games: update author info for 3 games from Echo Project
games: remove deprecated property sensitive_media for all entities
```

Update translation file of the item Adastra (no variant reflection):

```
games/l10n/zh: Adastra: update translation for description
```

When updating translation file of item Adastra, the variant should be specified if involved in `X-Chinese-Convertor-Hint` related property.

```
games/l10n/zh-tw: Adastra: set X-Chinese-Convertor-Hint
```

Updating multiple translation files of game items:

```
games/l10n/zh: add description-format for all entries
```

### Code

When modifying code, if a module contains multiple classes and only one of them is modified, you can use `Sub Mod:` to specify the name of the class.

```
fgi/game: GameDescription: initial brief-description support
test/tagmgr: update unit test case
scripts/build-next: do not use uimod plugin
```

Exception1: For code in plugin (fgi/plugins/...), the prefix `fgi/` in `Mod or Range:` should be deleted, then make the remaining to comply with file path.

```
plugins/steam-cdn-unite: add new akamai CDN URI prefix
```

Exception2：For code in renderers (fgi/renderers/...), the prefix `fgi/` in `Mod or Range:` should be deleted, the remaining compliance file path.

> In the past, the directory `fgi/renderers/` once was `renderers/`, This requirement ensures that the format is the same as the historical message format.

```
renderers/list: initial multi-klass support
```

### Templates and Styles

```
templates: fixup xxx bug
```

```
templates/list: use list_item widget
```

```
templates/peafowl-private/header: fixup opengraph description escape`webroot/`
```

Although the styles files stored in `webroot/styles/`, the prefix `fgi/` in `webroot/` should be deleted, then make the remaining to comply with file path.

```
styles/32_game_entry: add workarounds for Mozilla Firefox
```

### Webroot

Exception1: if you modified the file in the directory of webroot/base/, the prexix `webroot/base/` in `Mod or Range:` should be changed to `webroot/`, then make the remaining to comply with file path.

> In the past, the directory `webroot/base/` once was `webroot/`, This requirement ensures that the format is the same as the historical message format.

```
webroot/robots: disallow /classic-ui
webroot/scripts/searchexpr: initial @reverse and @lastmod support
```

Exception2: if you modified the file 'service worker', directly use `sw: ` as `Mod or Range:`。

```
sw: proactive opaque cache avoiding
```

### UI l10n translation file

File path no need to reflect the variant.

```
uil10n/zh: add translation for ...
uil10n/zh: add translation for many keys
```

But, if you modified the file with the suffix `_PRIVATE.yaml`, the variant should be specified. Meanwhile, use `PRIVATE: ` as `Sub Mod`.

```
uil10n/zh-tw: PRIVATE: add hotfix for list-klass-platform-mobile
```

### Document

```
doc/search_help: add more exampless
```

### staging-ui and classic-ui

if you modified the file that in directory `staging-ui` and `classic-ui`, you should use `staging-ui: ` or `classic-ui/UI包代号: ` as `Mod or Range: `, Meanwhile, use the remaining filename as `Sub Mod`.

```
staging-ui: styles/32_game_entry: add workarounds for Mozilla Firefox
classic-ui/pioneer: templates/pioneer-private/header: fixup build
```

### Sub mod of git

> Never use `Sub Mod:` in the following situation

The submitting message whose mod is pulled through git submodule is highly formalized. There are only two cases.

If the repositories is officially maintained by FGI organization, you can use the following message to indicate an updating to the latest version.

```
icons: bump to latest version
```

If the repositories is maintained by 3rd organization, you can use the following message to indicate an updating to an upstream version. `master` can be replaced with most of the git referring, which can be branch name, tags and commit hash, but can't be HEAD, etc.

```
some_thirdparty/some_submodule: bump to upstream master
```

### Treewide

The Treewide (`treewide`) indicate the modification covered in whole source code tree, which is not related to specific module usually.

> Never use `Sub Mod:` in the following situation

The example is, submits that can fix file newlines or run the Chinese converter:

```
treewide: fixup line endings
treewide: run zhconv
```

## The Identifier

In current, GFI has still one identifier, `[DO NOT MERGE]`.

### `[DO NOT MERGE]` Identifier

`[DO NOT MERGE]` declare that this submits will not and shouldn't be committed to main branch.

For example, the following message, which is about hack of disabling privacy policy in FGI-next builds:

```
[DO NOT MERGE] next: renderers/nonl10n/singles: disable privacy-policy page
```

## The Referring

The Referring means an address which is related to what this patch modifies, and reviewers can find more helpful information about this modification via these links. For example, `PR #number` referring pull request，`Fixed #number` referring related issues.

Here are some instances:

```
games/Adastra: new game (PR #23333)
games/Adastra: use stock link for chinese patch (PR #23335, Fixed #23334)
games/Adastra: use stock link for chinese patch (Fixed #23334)
```

## The Exception

There are several exceptions in which you needn't (Completely) content the format.

1. When use `git revert` revert commits, with default `Revert "..."` format. The `"..."` need content the format that defined by this article, or need content (recursively) this exception.

2. When use `git merge --no-ff` or default pull request on GitHub, with default `Merge ...` format.

	Do not allow non-essential `Merge ...` merge message. If your code base need be updated. We suggest `git pull --rebase` as your first option.
	
	If there are such submits, maintainer may use 'squash and merge' and rewrite the commit message.
