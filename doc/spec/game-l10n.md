## GameL10nEntry Type

`object` ([GameL10nEntry](game-l10n.md))

# GameL10nEntry Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                              |
| :---------------------------------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                                         | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-name.md "undefined#/properties/name")                                              |
| [description](#description)                           | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-description.md "undefined#/properties/description")                                |
| [description-format](#description-format)             | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-description-format.md "undefined#/properties/description-format")                  |
| [links-tr](#links-tr)                                 | `object` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-linktranslation.md "undefined#/properties/links-tr")                               |
| [X-Chinese-Convertor-Hint](#x-chinese-convertor-hint) | `object` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-extensionchineseconvertorhint.md "undefined#/properties/X-Chinese-Convertor-Hint") |

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

## description-format

Game description should be `plain` (default) text or will be rendered by `markdown`.


`description-format`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-description-format.md "undefined#/properties/description-format")

### description-format Type

`string`

### description-format Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value        | Explanation |
| :----------- | ----------- |
| `"plain"`    |             |
| `"markdown"` |             |

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
-   Type: `object` ([ExtensionChineseConvertorHint](game-l10n-properties-extensionchineseconvertorhint.md))
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-extensionchineseconvertorhint.md "undefined#/properties/X-Chinese-Convertor-Hint")

### X-Chinese-Convertor-Hint Type

`object` ([ExtensionChineseConvertorHint](game-l10n-properties-extensionchineseconvertorhint.md))
