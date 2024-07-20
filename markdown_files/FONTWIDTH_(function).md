## _FONTWIDTH (function)
---

### The _FONTWIDTH function returns the point-size width of a monospace font.

#### SYNTAX

`result& = _FONTWIDTH ( fontHandle& )`

#### DESCRIPTION
* If fontHandle& is omitted, it is assumed to be the font of the current write page.
* If fontHandle& is an invalid handle, an invalid handle error is thrown.
* If the font specified by fontHandle& is not a monospace font, 0 (zero) is returned.


#### SEE ALSO
* [_FONTWIDTH](./_FONTWIDTH.md)
* [_FONTHEIGHT](./_FONTHEIGHT.md) , [_FONTHEIGHT](./_FONTHEIGHT.md) (function)
* [_LOADFONT](./_LOADFONT.md)
