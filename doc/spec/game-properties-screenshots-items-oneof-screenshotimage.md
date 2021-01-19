## 0 Type

`object` ([ScreenshotImage](game-properties-screenshots-items-oneof-screenshotimage.md))

# ScreenshotImage Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                          |
| :---------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [type](#type)           | `string`  | Optional | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-type.md "undefined#/properties/screenshots/items/oneOf/0/properties/type")           |
| [sensitive](#sensitive) | `boolean` | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/0/properties/sensitive") |
| [uri](#uri)             | `string`  | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-uri.md "undefined#/properties/screenshots/items/oneOf/0/properties/uri")             |

## type

Must be `image`. But you can make a object without `type` property, the object will have default type property `image`.


`type`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-type.md "undefined#/properties/screenshots/items/oneOf/0/properties/type")

### type Type

`string`

### type Constraints

**constant**: the value of this property must be equal to:

```json
"image"
```

## sensitive

`true` if the image is sensitive


`sensitive`

-   is required
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/0/properties/sensitive")

### sensitive Type

`boolean`

## uri

The path or the URI of the image.


`uri`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotimage-properties-uri.md "undefined#/properties/screenshots/items/oneOf/0/properties/uri")

### uri Type

`string`
