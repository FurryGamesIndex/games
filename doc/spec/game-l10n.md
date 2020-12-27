## GameL10nEntry Type

`object` ([GameL10nEntry](game-l10n.md))

# GameL10nEntry Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                         |
| :---------------------------------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------- |
| [name](#name)                                         | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-name.md "undefined#/properties/name")                                         |
| [description](#description)                           | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-description.md "undefined#/properties/description")                           |
| [links-tr](#links-tr)                                 | `object` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-linktranslation.md "undefined#/properties/links-tr")                          |
| [X-Chinese-Convertor-Hint](#x-chinese-convertor-hint) | `object` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-x-chinese-convertor-hint.md "undefined#/properties/X-Chinese-Convertor-Hint") |

## name

The translated name of the game.


`name`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-name.md "undefined#/properties/name")

### name Type

`string`

## description

The translated description of the game.


`description`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-description.md "undefined#/properties/description")

### description Type

`string`

## links-tr

A map contains translated link names.


`links-tr`

-   is optional
-   Type: `object` ([LinkTranslation](game-l10n-properties-linktranslation.md))
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-linktranslation.md "undefined#/properties/links-tr")

### links-tr Type

`object` ([LinkTranslation](game-l10n-properties-linktranslation.md))

## X-Chinese-Convertor-Hint

Hints for Chinese convertor. Should only be used in `zh-*` l10n entries.


`X-Chinese-Convertor-Hint`

-   is optional
-   Type: `object` ([Details](game-l10n-properties-x-chinese-convertor-hint.md))
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-x-chinese-convertor-hint.md "undefined#/properties/X-Chinese-Convertor-Hint")

### X-Chinese-Convertor-Hint Type

`object` ([Details](game-l10n-properties-x-chinese-convertor-hint.md))
