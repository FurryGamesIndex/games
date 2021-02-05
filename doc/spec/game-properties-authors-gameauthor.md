## items Type

`object` ([GameAuthor](game-properties-authors-gameauthor.md))

# GameAuthor Properties

| Property                  | Type      | Required | Nullable       | Defined by                                                                                                                           |
| :------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)             | `string`  | Required | cannot be null | [GameEntry](game-properties-authors-gameauthor-properties-name.md "undefined#/properties/authors/items/properties/name")             |
| [standalone](#standalone) | `boolean` | Optional | cannot be null | [GameEntry](game-properties-authors-gameauthor-properties-standalone.md "undefined#/properties/authors/items/properties/standalone") |
| [role](#role)             | `array`   | Required | cannot be null | [GameEntry](game-properties-authors-gameauthor-properties-role.md "undefined#/properties/authors/items/properties/role")             |

## name

The name of the author. If the author has been defined in author database, MUST use the name specified in `name` property in author datafile.


`name`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [GameEntry](game-properties-authors-gameauthor-properties-name.md "undefined#/properties/authors/items/properties/name")

### name Type

`string`

## standalone

`true` if this author is a standalone author.
Standalone author is only in current game scope and do not generate tags, do not link with author database.


`standalone`

-   is optional
-   Type: `boolean`
-   cannot be null
-   defined in: [GameEntry](game-properties-authors-gameauthor-properties-standalone.md "undefined#/properties/authors/items/properties/standalone")

### standalone Type

`boolean`

## role

What role is the author playing around this game.


`role`

-   is required
-   Type: `string[]`
-   cannot be null
-   defined in: [GameEntry](game-properties-authors-gameauthor-properties-role.md "undefined#/properties/authors/items/properties/role")

### role Type

`string[]`
