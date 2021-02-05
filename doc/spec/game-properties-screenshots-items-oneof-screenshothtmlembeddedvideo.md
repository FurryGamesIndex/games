## 3 Type

`object` ([ScreenshotHTMLEmbeddedVideo](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo.md))

# ScreenshotHTMLEmbeddedVideo Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                      |
| :---------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [type](#type)           | `string`  | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-type.md "undefined#/properties/screenshots/items/oneOf/3/properties/type")           |
| [sensitive](#sensitive) | `boolean` | Optional | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/3/properties/sensitive") |
| [src](#src)             | `array`   | Required | cannot be null | [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-src.md "undefined#/properties/screenshots/items/oneOf/3/properties/src")             |

## type

Must be `video`


`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-type.md "undefined#/properties/screenshots/items/oneOf/3/properties/type")

### type Type

`string`

### type Constraints

**constant**: the value of this property must be equal to:

```json
"video"
```

## sensitive

`true` if the media is sensitive


`sensitive`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-sensitive.md "undefined#/properties/screenshots/items/oneOf/3/properties/sensitive")

### sensitive Type

`boolean`

## src




`src`

-   is required
-   Type: `object[]` ([HTMLVideoSource](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-src-htmlvideosource.md))
-   cannot be null
-   defined in: [GameEntry](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-src.md "undefined#/properties/screenshots/items/oneOf/3/properties/src")

### src Type

`object[]` ([HTMLVideoSource](game-properties-screenshots-items-oneof-screenshothtmlembeddedvideo-properties-src-htmlvideosource.md))
