# FAQ

## General FAQs about FGI

### I found problem in pages or link failure

Welcome [participate in FGI contributions](https://github.com/FurryGamesIndex/games/blob/master/doc/Contribute.en.md)

### Do you accept straight games?

Actually yes. But most of the volunteers who contributed to this project are gay, which resulted in more gay games appearing on the list.

Even so, we've still added some straight games. If you'd like to see your favorite straight games appear on this list, don't hesitate to contribute now.

For those who want to filter out some of the sexual orientation, we offer two tags, `type:bara` for games with gay contents and `type:yuri` for games with lesbian contents. This can be used in conjunction with the "How can I make full use of the search function of this site" below.

### Do you accept "Kemonomimi" games?

Never. Also, if a game contains both Kemonomimi and acceptable furries, Kemonomimi will be identified as "[humankind](https://furrygamesindex.github.io/en/search.html?tagx?male:humankind%20or%20female:humankind)".

<a id="search_help"></a>
### How can I make full use of the "search" function of this site

There are three search modes: "Search Title", "Search Title and Description" and "Search Tags"

"Search title" and "search title and description" are literal meanings, what you need to know a little bit is "search tags"

1. You need to use the full name of the tag, you can not do fuzzy search on the tag. Such as `male:wolf`, `type:visual-novel`, etc.

2. If the tag you use includes spaces, you **must** put it in double quotes, such as `"author:The Echo Project"`. If the tag does not contain spaces, you can use double quotes or not, for example, `type:yiff` and `"type:yiff"` are equivalent.

	**If you only need to search for one tag, you only need to understand 1, 2 but when you need to search for multiple tags, Keep reading.**

3. Use the keyword `or` (lowercase letters only) between the two parts. They indicate the "union" of the left and right parts (or)

	Example: <code>male:canine **or** female:canine</code> searches for games that contain "male canine furries", or "female canine furries" or both tags. That is, search for games where the main character contains canine furries.

4. Use the keywords `and` (lowercase letters only) between the two parts. They indicate that the two parts on the left and right "take the intersection" (and).

	Example: <code>misc:3d **and** lang:en **and** male:wolf</code> search game that must contain the three tags "3D", "official English" and "male wolfman", that is, search for games that mainly expressed in 3D, have official English supporting and contains male wolf furries.

	Example: <code>misc:freeware **and** platform:android **and** type:bara</code> searches for gay games that support the Android platform and are free of charge (or a lot of them are free of charge)

	Some times ago, you had to write like this. However, in the site search of many websites, you can directly enter multiple keywords to achieve the same effect. Fortunately, FGI now supports the omission of `and`, this feature is called "default and".

	Example: `misc:3d lang:en male:wolf` and <code>misc:3d **and** lang:en **and** male:wolf</code> are equivalent.

5. Use the keyword `not` (lowercase letters only) between the two parts. They indicate that the left and right parts are "set of difference" (not). Use `not` at the beginning of the entire expression or at the beginning of a parenthesis part, which means "take difference" (not) for all games and the right part.

	Example: <code>male:felidae **and** type:visual-novel **not** "author:Studio Klondike"</code>, that is, search for games with felidae furries main character and the type of it is visual novel, but the author is NOT "Studio Klondike".

	Example: <code>**not** type:yiff</code> searches for games that are not "contains adult/sensitive content", that is, searches for all games for all ages.

6. The priority of the expression is from left to right, you can add parentheses to force change the priority.

	Example: <code>male:canine **and** **(**type:visual-novel **or** type:dating-sim**)**</code>, this expression will be first finding the games of "visual novels" or "dating simulators", and then select the games containing "male canine furries" in these games.
	In this example, if you do not add parentheses, that is, `male:canine and type:visual-novel or type:dating-sim` means a visual novel containing "male canine furries" or a dating simulator (not necessarily including male canine furries) , This may not be what you want.

	Example: <code>misc:3d **and** **(**lang:en **or** lang:zh **or** lang:en-unofficial **or** lang:zh-unofficial**)** **not** type:yiff</code> Search for all 3D style games that support English or Chinese languages (official or third-party) with adult/sensitive content.

	Tips: There can be multiple levels of parentheses, such as `A and (B or (C and D) not (E or (F and G)))`

7. If your expression has a grammatical error, many times FGI will not report an error, but may return a result that may be incredible. for example, like the left and right parentheses do not match.

It is worth mentioning that, you can also quickly enter the search page by clicking the tag in the game page.

Some games may miss tags or contain incorrect tags. This will affect your search. If you find it, welcome to request corrections via issues or pull requests on [Github](https://github.com/FurryGamesIndex/games/) (use [Telegram](https://t.me/FurryGamesIndex) to contact maintainer is also acceptable), thank you very much.

You can view the list of all tags currently supported by FGI from [here](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.zh-cn.md). If you think more tags should be added, welcome to contact this project too.

### Is there a downloadable offline version

Yes, we provide offline version for furries who want to save this list locally.

The external images will included in offline version.

Build script is releasing offline version everyday, you can go to [here](https://github.com/FurryGamesIndex/games/releases/tag/_gh_assets) to download one.

## Questions about contributions

### Can I choose to contribute anonymously

Although not recommended, we allow anonymous contributions, and we respect the requests of contributors. At the same time, if one day an anonymous contributor changes his mind and wants to add his name and contact information to the "Contributor List", we are very welcome and can add the list is ready for you!
The

Please note that even if you contribute anonymously, when you use Github Pull Request, your Github account will still be automatically recorded. (If you have not set "Keep my email addresses private", your email address may also be leaked)
