## GameEntry Type

`object` ([GameEntry](game.md))

# GameEntry Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                    |
| :---------------------------------------- | --------- | -------- | -------------- | :-------------------------------------------------------------------------------------------- |
| [name](#name)                             | `string`  | Required | cannot be null | [GameEntry](game-properties-name.md "undefined#/properties/name")                             |
| [description](#description)               | `string`  | Required | cannot be null | [GameEntry](game-properties-description.md "undefined#/properties/description")               |
| [description-format](#description-format) | `string`  | Optional | cannot be null | [GameEntry](game-properties-description-format.md "undefined#/properties/description-format") |
| [expuged](#expuged)                       | `boolean` | Optional | cannot be null | [GameEntry](game-properties-expuged.md "undefined#/properties/expuged")                       |
| [replaced-by](#replaced-by)               | `string`  | Optional | cannot be null | [GameEntry](game-properties-replaced-by.md "undefined#/properties/replaced-by")               |
| [tags](#tags)                             | `object`  | Required | cannot be null | [GameEntry](game-properties-tagdict.md "undefined#/properties/tags")                          |
| [links](#links)                           | `array`   | Required | cannot be null | [GameEntry](game-properties-links.md "undefined#/properties/links")                           |
| [thumbnail](#thumbnail)                   | `string`  | Required | cannot be null | [GameEntry](game-properties-thumbnail.md "undefined#/properties/thumbnail")                   |
| [sensitive_media](#sensitive_media)       | `boolean` | Optional | cannot be null | [GameEntry](game-properties-sensitive_media.md "undefined#/properties/sensitive_media")       |
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


`sensitive_media`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-sensitive_media.md "undefined#/properties/sensitive_media")

### sensitive_media Type

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
