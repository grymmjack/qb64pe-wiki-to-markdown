## _WIDTH (function)
---

### The _WIDTH function returns the width of an image handle or of the current write page.

#### SYNTAX

`columns& = _WIDTH [( imageHandle& )]`

#### DESCRIPTION
* If imageHandle& is omitted, it's assumed to be the handle of the current [SCREEN](./SCREEN.md) or write page.
* To get the width of the current program screen window use zero for the handle value or nothing: columns& = [_WIDTH](./_WIDTH.md) (0) or columns& = [_WIDTH](./_WIDTH.md)
* If the image specified by imageHandle& is in text only( [SCREEN](./SCREEN.md) 0) mode, the number of characters per row is returned.
* If the image specified by imageHandle& is in graphics mode, the number of pixels per row is returned.
* If imageHandle& is an invalid handle, then an invalid handle error is returned.
* The last visible pixel coordinate of a program screen is [_WIDTH](./_WIDTH.md) - 1 .


#### EXAMPLES
##### Example: A SUB program that centers text in any graphic screen mode except text mode SCREEN 0.
```vb
s& = _NEWIMAGE(800, 600, 256)
SCREEN s&
Align 15, 5, s&, "This text is centered on the screen!"

SUB Align (Tcolor, Trow, mode&, txt$)
  center& = _WIDTH (mode&) \ 2     'returns pixels in graphic modes
  MaxCol = (center& \ 8) + 1              'screen text width = 8 pixels
  Tcol = MaxCol - (LEN(txt$) \ 2)
  COLOR Tcolor: LOCATE Trow, Tcol: PRINT txt$;
END SUB
```
  


#### SEE ALSO
* [_HEIGHT](./_HEIGHT.md) , [_LOADIMAGE](./_LOADIMAGE.md) , [_NEWIMAGE](./_NEWIMAGE.md)
* [WIDTH](./WIDTH.md)
* Bitmaps
