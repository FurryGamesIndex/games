---
styles: >
  code {
    background-color: var(--background-color-alt);
  }
  tbody>tr:nth-child(odd) {
    border-top: 1px solid var(--border-color);
  }
  tbody>tr:nth-child(odd) code {
    margin: auto;
    padding: unset;
  }
  table {
    width: 100%;
  }
  thead {
    display: none;
  }
---

# Search Help

The "Search Title" and "Search Title and Description" will try to match relevant keywords in the game title or description and then display the matching results. This should be very intuitive and does not require much explanation.

"Search Tags" is a more powerful search feature that FGI provides to our users, and this help explains how to use this feature by giving examples.

## Tagging System

Before we begin, a brief explanation of FGI's tagging system is in order.

FGI's tags consist of two parts, an optional "namespace" and a "value". For example, for the `male:dog` tag, the namespace is `male:` and the value is `dog`.

The namespace is optional, so `dog` is also a valid tag. When the namespace is not specified, it means that the namespace is not considered, and games with `male:dog` or `female:dog` or both are considered to contain the `dog` tag.

The value portion of the tag may have one or more "aliases", e.g. the `netorare` tag has an alias `ntr`. You can use `ntr` instead of `netorare`, and `male:ntr` instead of `male:netorare`, etc.

There may also be dependencies between tags, but this is irrelevant for search purposes.

**You can see a list of all the tags currently supported by FGI from [here](https://github.com/FurryGamesIndex/games/blob/master/doc/tags.en.md). If you find that a game is missing tag(s), feel free to contribute. If you think more tags should be added, feel free to contact us.**

## Basic Search

### Search for a single tag

| |
|-|
| `dog` |
| Search for games with `dog` tags in any namespace. This example will search for games that contain dog furries. |
| `felidae` |
| Search for games with `felidae` tags in any namespace. This example will search for games that contain felidae furries. |

### Specify the namespace where tags are located

| |
|-|
| `male:dog` |
| Search for games that contain the `dog` tag in the `male:` namespace. This example will search for games that contain male dog furries. |

### When do you need quotes?

If you are using a tag that includes spaces, you MUST place it in double quotes. If the tag does not contain spaces, you can use double quotes or not.

| |
|-|
| `type:visual-novel`<br>`"type:visual-novel"` |
| Search for games that contain the `visual-novel` tag in the `type:` namespace. This example will search for visual novel games. In this case, the two writings are equivalent. |
| `"author:The Echo Project"` |
| Search for games that contain the `"The Echo Project"` tag in the `author:` namespace. This example will search for games developed by The Echo Project. Searching with `author:The Echo Project` (without quotes) will not work as expected. |

### If you need to exclude tags

| |
|-|
| `not misc:work-in-process` |
| Search for games that don't have the `work-in-process` tag in the `misc:` namespace. This example will search for games that are already released (not still in development). |
| `not yiff` |
| Search for games that do not contain the `yiff` tag in any namespace. This example will exclude games with adult contents. <br> > The `yiff` tag exists only in the `type:` namespace. So for this tag, `type:yiff` and `yiff` are equivalent. |

## Search multiple tags

### and, or, not

| |
|-|
| `misc:3d lang:en wolf`<br>`misc:3d and lang:en and wolf` |
| Search for games with both `misc:3d`, `lang:en` and `wolf` tags (preceded by a colon to specify the namespace)
| `misc:freeware platform:android type:bara`<br>`misc:freeware and platform:android and type:bara` |
| Search for games that have both `misc:freeware`, `platform:android` and `type:bara` tags (preceded by a colon to specify the namespace) |
| `canine or dragon` |
| Search for games containing `canine` tag or `dragon` tag or both. |
| `male:canine or female:canine` |
| Search for games with `male:canine` tag or with `female:canine` tag or with both. (In this example, the expression is actually equivalent to searching for `canine`. |
| `male:felidae and visual-novel not "author:Studio Klondike"` |
| Search for games with `male:fedidae` tag and `visual-novel` tag, but without the `"author:Studio Klondike"` tag. This example will search for visual novels that include male feline furries, but are not developed by `"Studio Klondike"`. |

### Change priority

The priority of an expression is running left-to-right, and you can add parentheses to force a change in priority. Parentheses are as whole parts in the operation with the parent.

Consider the `male:canine and type:visual-novel or type:dating-sim` expression that looks for games with `male:canine`, then filters for games with `type:visual-novel`, and then adds  all games with `type:dating-sim` tag. So it will search for visual novels that contain male canines or dating simulators (not necessarily contain male canines). If you are looking for visual novels or dating simulators both with canine furries, this is obviously not what you want. The solution is to have the search engine do a search for `type:visual-novel or type:dating-sim` first and then filters the results with `male:canine`. We can rewrite the expression in left-to-right order, or we can change the priority with parentheses.

| |
|-|
| `male:canine and (type:visual-novel or type:dating-sim)` |
| This expression will find games that are "visual novels" or "dating simulators", and then filter them for games that contain male canines. |
| `misc:3d and (lang:en or lang:zh or lang:en-unofficial or lang:zh-unofficial) not type:yiff` |
| Search for all-ages 3D style games that support English or Chinese language. |
| `A and (B or (C and D) not (E or (F and G)))` |
| This example only indicates that multiple levels can exist in parentheses. The maximum number of levels is browser-specific. |

### Change the order

| |
|-|
| `@reverse` |
| Search all games, but the results are sorted alphabetically by Z-A. (Reverse A-Z order) |
| `@lastmod` |
| Search all games, but sort by most recently modified, the most recently modified games are at the front of the results. |
| `@lastmod @reverse` |
| Search all games, but reverse the order of most recent modified, the most recently modified games are at the end of the results. |
| `misc:freeware @lastmod` |
| Search for games with `misc:freeware` tag, but reverse sort by most recently modified, with most recently modified games are at the front of the results. |
| `platform:android or platform:ios @reverse` |
| Search for Android or iOS games, but the results are the reverse of `platform:android or platform:ios` search results. |
| `platform:android or (platform:ios @reverse)` |
| Search for Android or iOS games, but games which ONLY contains the `platform:ios` tag will be sorted in Z-A alphabetical order. (Reverse A-Z order) |
| `platform:android @lastmod or platform:ios` |
| Search for Android or iOS games, but games which contains the `platform:android` tag or contains both tags will be sorted by most recently modified, the most recently modified games are at the front of the results. |
| `steam and itchio @lastmod`<br>`steam itchio @lastmod`<br>`steam @lastmod and itchio`<br>`steam @lastmod itchio` |
| Search for games that are both published on itch.io and Steam, but sort by most recently modified, the most recently modified games are at the front of the results. |
| `steam and (itchio @lastmod)`<br>`steam (itchio @lastmod)` |
| It may seem strange to users, but this is actually the equivalent of `steam and itchio` or `steam itchio`. |
