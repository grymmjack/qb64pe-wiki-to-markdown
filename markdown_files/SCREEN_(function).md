## SCREEN (function)
---

### The SCREEN function returns the ASCII code of a text character or the color attribute at a set text location on the screen.

#### SYNTAX

`codeorcolor% = SCREEN ( row% , column% [, colorflag%] )`

#### PARAMETERS
* row and column are the [INTEGER](./INTEGER.md) text coordinates of the [SCREEN](./SCREEN.md) mode used.
* Optional colorflag [INTEGER](./INTEGER.md) value can be omitted or 0 for ASCII code values or 1 for color attributes.


#### SEE ALSO
* [PRINT](./PRINT.md) , [SCREEN](./SCREEN.md)
* [COLOR](./COLOR.md) , CHR$ , [POINT](./POINT.md)
* [CSRLIN](./CSRLIN.md) , [POS](./POS.md) , ASCII
* Screen Memory
