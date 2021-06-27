## GameEntry Type

`object` ([GameEntry](game.md))

# GameEntry Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                    |
| :---------------------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------- |
| [name](#name)                             | `string`  | Required | cannot be null | [GameEntry](game-properties-name.md "undefined#/properties/name")                             |
| [description](#description)               | `string`  | Required | cannot be null | [GameEntry](game-properties-description.md "undefined#/properties/description")               |
| [description-format](#description-format) | `string`  | Optional | cannot be null | [GameEntry](game-properties-description-format.md "undefined#/properties/description-format") |
| [brief-description](#brief-description)   | `string`  | Optional | cannot be null | [GameEntry](game-properties-brief-description.md "undefined#/properties/brief-description")   |
| [expuged](#expuged)                       | `boolean` | Optional | cannot be null | [GameEntry](game-properties-expuged.md "undefined#/properties/expuged")                       |
| [replaced-by](#replaced-by)               | `string`  | Optional | cannot be null | [GameEntry](game-properties-replaced-by.md "undefined#/properties/replaced-by")               |
| [authors](#authors)                       | `array`   | Optional | cannot be null | [GameEntry](game-properties-authors.md "undefined#/properties/authors")                       |
| [tags](#tags)                             | `object`  | Required | cannot be null | [GameEntry](game-properties-tagdict.md "undefined#/properties/tags")                          |
| [links](#links)                           | `array`   | Required | cannot be null | [GameEntry](game-properties-links.md "undefined#/properties/links")                           |
| [thumbnail](#thumbnail)                   | `string`  | Required | cannot be null | [GameEntry](game-properties-thumbnail.md "undefined#/properties/thumbnail")                   |
| [sensitive_media](#sensitive_media)       | `boolean` | Optional | cannot be null | [GameEntry](game-properties-sensitive_media.md "undefined#/properties/sensitive_media")       |
| [auto-steam-widget](#auto-steam-widget)   | `boolean` | Optional | cannot be null | [GameEntry](game-properties-auto-steam-widget.md "undefined#/properties/auto-steam-widget")   |
| [screenshots](#screenshots)               | `array`   | Required | cannot be null | [GameEntry](game-properties-screenshots.md "undefined#/properties/screenshots")               |
| [X-Created-by](#x-created-by)             | `string`  | Optional | cannot be null | [GameEntry](game-properties-x-created-by.md "undefined#/properties/X-Created-by")             |
| [X-Co-edited-by](#x-co-edited-by)         | `array`   | Optional | cannot be null | [GameEntry](game-properties-x-co-edited-by.md "undefined#/properties/X-Co-edited-by")         |

## name

The name of the game.

For English games, it should be `Game name`.

For non-English games, it should be `English name / Original name` or `Original name`.


`name`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-name.md "undefined#/properties/name")

### name Type

`string`

## description

The description of the game. In English.


`description`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-description.md "undefined#/properties/description")

### description Type

`string`

## description-format

Game description should be `plain` (default) text or will be rendered by `markdown`.


`description-format`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-description-format.md "undefined#/properties/description-format")

### description-format Type

`string`

### description-format Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | ----------- |
| `"plain"`    |             |
| `"markdown"` |             |

## brief-description

A brief description of the game. For English, the max size of brief-description is 480 characters and min size of brief-description is 200.
brief-description will be used in standard list page.
If you do not specify a brief-description, we will use first 480 characters from description.


`brief-description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-brief-description.md "undefined#/properties/brief-description")

### brief-description Type

`string`

## expuged

`true` if the game entry should be expuged.

If the game is not expuged, do not add this property.


`expuged`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-expuged.md "undefined#/properties/expuged")

### expuged Type

`boolean`

## replaced-by

A game ID who the owner has replaced this game.

If the game is not replaced by another game, do not add this property.


`replaced-by`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-replaced-by.md "undefined#/properties/replaced-by")

### replaced-by Type

`string`

## authors

The infomation about the author(s) of the game.


`authors`

-   is optional
-   Type: `object[]` ([GameAuthor](game-properties-authors-gameauthor.md))
-   cannot be null
-   defined in: [GameEntry](game-properties-authors.md "undefined#/properties/authors")

### authors Type

`object[]` ([GameAuthor](game-properties-authors-gameauthor.md))

## tags

The tags of the game.


`tags`

-   is required
-   Type: `object` ([TagDict](game-properties-tagdict.md))
-   cannot be null
-   defined in: [GameEntry](game-properties-tagdict.md "undefined#/properties/tags")

### tags Type

`object` ([TagDict](game-properties-tagdict.md))

## links




`links`

-   is required
-   Type: `object[]` ([Link](game-properties-links-link.md))
-   cannot be null
-   defined in: [GameEntry](game-properties-links.md "undefined#/properties/links")

### links Type

`object[]` ([Link](game-properties-links-link.md))

## thumbnail

The path or URI of the thumbnail image of the game.


`thumbnail`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-thumbnail.md "undefined#/properties/thumbnail")

### thumbnail Type

`string`

## sensitive_media

`true` if at last one of the screenshots is sensitive.

WARNNING: This is a **deprecated** property.
FGI will ignore this property and decide whether to add a sensitive media notification bar based on other information.
It should not be used in newly edited game entries.


`sensitive_media`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-sensitive_media.md "undefined#/properties/sensitive_media")

### sensitive_media Type

`boolean`

## auto-steam-widget

Default is `true` and FGI will use infomations in `links` to generate steam store widget media in screenshots. Specify `false` to disable it.


`auto-steam-widget`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-auto-steam-widget.md "undefined#/properties/auto-steam-widget")

### auto-steam-widget Type

`boolean`

## screenshots

The screenshots or other related medias of the game.


`screenshots`

-   is required
-   Type: an array of merged types ([Details](game-properties-screenshots-items.md))
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots.md "undefined#/properties/screenshots")

### screenshots Type

an array of merged types ([Details](game-properties-screenshots-items.md))

## X-Created-by

Specify the actual contributor who creates the game entry.

Use git commit infomation when not specified.

This field should not used when the actual contributor uses git (not commited by the maintainer).

Allow `name` or `name <email address>`


`X-Created-by`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-x-created-by.md "undefined#/properties/X-Created-by")

### X-Created-by Type

`string`

## X-Co-edited-by

Specify the actual contributors who edited the game entry (except X-Created-by).

Use git commit infomation when not specified.

This field should not used when the actual contributor uses git (not commited by the maintainer).

Allow `name` or `name <email address>`


`X-Co-edited-by`

-   is optional
-   Type: `array`
-   cannot be null
-   defined in: [GameEntry](game-properties-x-co-edited-by.md "undefined#/properties/X-Co-edited-by")

### X-Co-edited-by Type

`array`
