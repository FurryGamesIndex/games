# FAQ

## General FAQs about FGI

### I found problem in pages or link failure

Welcome [participate in FGI contributions](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.en.md)

### How can I make full use of the "search" function of this site

<a id="search_help"></a>

"Search title" and "search title and description" are literal meanings, what you need to know a little bit is "search tags"

When using search tags, there are 5 rules

1. You need to use the full name of the tag, you can not do fuzzy search on the tag. Such as `male:wolf`, `type:visual-novel`, etc.

2. If the tag you use includes spaces, you **must** put it in double quotes, such as `"author:The Echo Project"`. If the tag does not contain spaces, you can use double quotes or not, for example, `type:yiff` and `"type:yiff"` are equivalent.

3. If you only need to search for one tag, you only need to understand 1, 2 but when you need to search for multiple tags, you need to use the keywords "and", "or" and "not" between the tags, They indicate that the two parts on the left and right are "take intersection" (and), "take union" (or), and "take difference set" (not), please **use only lowercase**.

4. The priority of the expression is from left to right, you can add parentheses to force change the priority, such as `male:canine and (type:visual-novel or type:dating-sim)`, this expression will be first finding the games of "visual novels" or "dating simulators", and then select the games containing "male canine furries" in these games. If you do not add parentheses, that is, male:canine and type:visual-novel or type:dating-sim` means a visual novel containing "male canine furries" or a dating simulator (not necessarily including male canine furries) , This may not be what you want. There can be multiple levels of parentheses, such as `A and (B or (C and D) not (E or (F and G)))`

5. If your expression has a grammatical error, many times FGI will not report an error, but may return a result that may be incredible. A common situation is that, because of the habits of other search engines, forget to add `and` in two tags (or a part enclosed in parentheses), which is the wrong syntax, but FGI will accept it and will currently adopt the most recent The occurrence of `and`, `or` or `not` decides which set operation to use. If it is not found, it will fall back to use `or`, but this result is not a guarantee and the behavior may change in the future. Never rely on this non-standard behavior, remember to add `and`, `or` or `not`. Another common situation is that if the left and right parentheses do not match, the expression may terminate early. Remember to ensure that the parentheses match.

Here are some examples

- `male:canine` search for games that include male canine furries in the main character

- `male:canine or female:canine` search for games that include canine furries in the main characters

- `male:felidae and type:visual-novel not "author:Studio Klondike"`searches for games includes felidae furries and the type is a visual novel, but the author does not include "Studio Klondike"

- `male:canine and (type:visual-novel or type:dating-sim)` search for visual novels or dating simulators containing male canine furries

- `misc:freeware and platform:android and type:bara` search for gay games that support the Android platform and are free (or a large part of them are free)

- `misc:3d and (lang:en or lang:zh or lang:en-unofficial or lang:zh-unofficial) not type:yiff` search for all-age (SFW) (as expression, not Yiff) 3D style games that support English or Chinese language

It is worth mentioning that, you can also quickly enter the search page by clicking the tag in the game page.

Many games currently lack tags, so they may not be displayed when searching for some normal tags searching. These games with missing tags can be listed by searching `sys:tagme`, which may help to help friends who want to contribute tags find the games to contribute more easily: https://furrygamesindex.github.io/en/search.html?tagx?sys:tagme

### Is there a downloadable offline version

	Yes, we provide offline version for furries who want to save this list locally.

	The external images will included in offline version.

	Build script is releasing offline version everyday, you can go to [here](https://github.com/FurryGamesIndex/games/releases/tag/_gh_assets) to download one.

## Questions about contributions

### Can I choose to contribute anonymously

	Although not recommended, we allow anonymous contributions, and we respect the requests of contributors. At the same time, if one day an anonymous contributor changes his mind and wants to add his name and contact information to the "Contributor List", we are very welcome and can add the list is ready for you!
The

	Please note that even if you contribute anonymously, when you use Github Pull Request, your Github account will still be automatically recorded. (If you have not set "Keep my email addresses private", your email address may also be leaked)
