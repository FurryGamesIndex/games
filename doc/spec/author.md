## AuthorEntry Type

`object` ([AuthorEntry](author.md))

# AuthorEntry Properties

| Property            | Type     | Required | Nullable       | Defined by                                                                  |
| :------------------ | -------- | -------- | -------------- | :-------------------------------------------------------------------------- |
| [name](#name)       | `string` | Required | cannot be null | [AuthorEntry](author-properties-name.md "undefined#/properties/name")       |
| [aliases](#aliases) | `array`  | Optional | cannot be null | [AuthorEntry](author-properties-aliases.md "undefined#/properties/aliases") |
| [type](#type)       | `string` | Required | cannot be null | [AuthorEntry](author-properties-type.md "undefined#/properties/type")       |
| [avatar](#avatar)   | `string` | Optional | cannot be null | [AuthorEntry](author-properties-avatar.md "undefined#/properties/avatar")   |
| [email](#email)     | `string` | Optional | cannot be null | [AuthorEntry](author-properties-email.md "undefined#/properties/email")     |
| [links](#links)     | `array`  | Optional | cannot be null | [AuthorEntry](author-properties-links.md "undefined#/properties/links")     |

## name

The name of the author.


`name`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [AuthorEntry](author-properties-name.md "undefined#/properties/name")

### name Type

`string`

## aliases




`aliases`

-   is optional
-   Type: an array of merged types ([Details](author-properties-aliases-items.md))
-   cannot be null
-   defined in: [AuthorEntry](author-properties-aliases.md "undefined#/properties/aliases")

### aliases Type

an array of merged types ([Details](author-properties-aliases-items.md))

## type

The type of the author.


`type`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [AuthorEntry](author-properties-type.md "undefined#/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value          | Explanation |
| :------------- | ----------- |
| `"unknown"`    |             |
| `"personal"`   |             |
| `"small-team"` |             |
| `"company"`    |             |
| `"publisher"`  |             |

## avatar

The URI or path of the author avatar.


`avatar`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [AuthorEntry](author-properties-avatar.md "undefined#/properties/avatar")

### avatar Type

`string`

## email

Email address of the author.

Do not use this property to avoid spam.


`email`

-   is optional
-   Type: `string`
-   cannot be null
-   defined in: [AuthorEntry](author-properties-email.md "undefined#/properties/email")

### email Type

`string`

## links

Email address of the author.

If there is not any email address provided by author, do not specify this property.


`links`

-   is optional
-   Type: `object[]` ([AuthorSNSEntry](author-properties-links-authorsnsentry.md))
-   cannot be null
-   defined in: [AuthorEntry](author-properties-links.md "undefined#/properties/links")

### links Type

`object[]` ([AuthorSNSEntry](author-properties-links-authorsnsentry.md))
