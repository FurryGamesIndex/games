## X-Chinese-Convertor-Hint Type

`object` ([ExtensionChineseConvertorHint](game-l10n-properties-extensionchineseconvertorhint.md))

# ExtensionChineseConvertorHint Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                  |
| :---------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [prefer](#prefer) | `string` | Optional | cannot be null | [GameL10nEntry](game-l10n-properties-extensionchineseconvertorhint-properties-prefer.md "undefined#/properties/X-Chinese-Convertor-Hint/properties/prefer") |

## prefer

Specify the base Chinese variant. default is `CN`.

To inhibition Chinese convertion, specify `ignored`.


`prefer`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameL10nEntry](game-l10n-properties-extensionchineseconvertorhint-properties-prefer.md "undefined#/properties/X-Chinese-Convertor-Hint/properties/prefer")

### prefer Type

`string`

### prefer Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | ----------- |
| `"CN"`      |             |
| `"TW"`      |             |
| `"ignored"` |             |
