## 2 Type

`object` ([ScreenshotYoutubeEmbeddedVideo](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo.md))

# ScreenshotYoutubeEmbeddedVideo Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                               |
| :------------ | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type) | `string` | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-type.md "undefined#/properties/screenshots/items/oneOf/2/properties/type") |
| [uri](#uri)   | `string` | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-uri.md "undefined#/properties/screenshots/items/oneOf/2/properties/uri")   |

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

## uri

Must be `youtube:ID`. ID is the video's ID.


`uri`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshotyoutubeembeddedvideo-properties-uri.md "undefined#/properties/screenshots/items/oneOf/2/properties/uri")

### uri Type

`string`
