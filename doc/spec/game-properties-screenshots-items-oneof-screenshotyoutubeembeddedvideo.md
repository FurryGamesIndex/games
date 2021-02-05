## 2 Type

`object` ([ScreenshotYoutubeEmbeddedVideo](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo.md))

# ScreenshotYoutubeEmbeddedVideo Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                         |
| :---------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)           | `string`  | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-type.md "undefined#/properties/screenshots/items/oneOf/2/properties/type")           |
| [id](#id)               | `string`  | Optional | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-id.md "undefined#/properties/screenshots/items/oneOf/2/properties/id")               |
| [sensitive](#sensitive) | `boolean` | Optional | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/2/properties/sensitive") |
| [uri](#uri)             | `string`  | Optional | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-uri.md "undefined#/properties/screenshots/items/oneOf/2/properties/uri")             |

## type

Must be `youtube`


`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-type.md "undefined#/properties/screenshots/items/oneOf/2/properties/type")

### type Type

`string`

### type Constraints

**constant**: the value of this property must be equal to:

```json
"youtube"
```

## id

Video ID of the youtube video, Required when you do not specify `uri`.


`id`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-id.md "undefined#/properties/screenshots/items/oneOf/2/properties/id")

### id Type

`string`

## sensitive

`true` if the media is sensitive


`sensitive`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/2/properties/sensitive")

### sensitive Type

`boolean`

## uri

Must be `youtube:ID`. ID is the video's ID. Required when you do not specify `id`.

WARNNING: This is a **deprecated** property.
But FGI also supports it due to backward compatible.
It should not be used in newly edited game entries.


`uri`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-uri.md "undefined#/properties/screenshots/items/oneOf/2/properties/uri")

### uri Type

`string`
