# _PUTIMAGE
> _PUTIMAGE puts an area of a source image to an area of a destination image in one operation, like GET and PUT .

## SYNTAX
`_PUTIMAGE [STEP] [( dx1 , dy1 )-[STEP][( dx2 , dy2 )]][, sourceHandle& ][, destHandle& ][, ][STEP][( sx1 , sy1 )[-STEP][( sx2 , sy2 )]][, _SMOOTH ]`

## SAMPLES
```vb
_PUTIMAGE 'full source image to fit full destination area after _SOURCE and _DEST are set
```  

```vb
_PUTIMAGE , sourceHandle& , destHandle& 'size full source to fit full destination area
```  

```vb
_PUTIMAGE ( dx1 , dy1 ), sourceHandle& , destHandle& 'full source to top-left corner destination position
```  

```vb
_PUTIMAGE ( dx1 , dy1 )-( dx2 , dy2 ), sourceHandle& , destHandle& 'size full source to destination coordinate area
```  

```vb
_PUTIMAGE ( dx1 , dy1 ), sourceHandle& , destHandle& , ( sx1 , sy1 )-( sx2 , sy2 ) 'portion of source to the top-left corner of the destination page
```  

```vb
_PUTIMAGE , sourceHandle& , destHandle& , ( sx1 , sy1 )-( sx2 , sy2 ) 'portion of source to full destination area
```  

```vb
_PUTIMAGE ( dx1 , dy1 )-( dx2 , dy2 ), sourceHandle& , destHandle& ,( sx1 , sy1 ) 'right side of source from top-left corner to destination
```  


## PARAMETERS
* Relative coordinates to a previous graphical object can be designated using [STEP](STEP.md) as opposed to literal surface coordinates (version 1.000 and up).
* Coordinates dx and dy map the box area of the destination area to use. When omitted the entire desination area is used. If only one coordinate is used, the source is placed with its original dimensions. Coordinates can be set to flip or resize the image. dx1 = the column coordinate at which the insertion of the source will begin (leftmost); when larger than dx2 , reverses image. dy1 = the row coordinate at which the insertion of the source will begin (topmost); when larger than dy2 , inverts image. dx2 = the column coordinate at which the insertion of the source will end (rightmost); further apart, widens image. dy2 = the row coordinate at which the insertion of the source will end (bottommost); closer together, shrinks image
	* dx1 = the column coordinate at which the insertion of the source will begin (leftmost); when larger than dx2 , reverses image.
	* dy1 = the row coordinate at which the insertion of the source will begin (topmost); when larger than dy2 , inverts image.
	* dx2 = the column coordinate at which the insertion of the source will end (rightmost); further apart, widens image.
	* dy2 = the row coordinate at which the insertion of the source will end (bottommost); closer together, shrinks image
* dx1 = the column coordinate at which the insertion of the source will begin (leftmost); when larger than dx2 , reverses image.
* dy1 = the row coordinate at which the insertion of the source will begin (topmost); when larger than dy2 , inverts image.
* dx2 = the column coordinate at which the insertion of the source will end (rightmost); further apart, widens image.
* dy2 = the row coordinate at which the insertion of the source will end (bottommost); closer together, shrinks image
* sourceHandle& = the [LONG](LONG.md) handle of the source image created with [_NEWIMAGE](_NEWIMAGE.md) , [_LOADIMAGE](_LOADIMAGE.md) or [_COPYIMAGE](_COPYIMAGE.md) .
* destHandle& = the [LONG](LONG.md) handle of the destination image may be created with [_NEWIMAGE](_NEWIMAGE.md) , [SCREEN](SCREEN.md) or destination 0.
* Coordinates sx and sy [GET](GET.md) the box area of the source image to transfer to the destination image, page or screen : sx1 = the column coordinate of the left-most pixel to include of the source. When omitted, the entire image is used sy1 = the row coordinate of the upper-most pixel to include of the source. When omitted, the entire image is used sx2 = the column coordinate of the right-most pixel to include of the source. Can be omitted to get rest of image. sy2 = the row coordinate of the bottom-most pixel to include of the source. Can be omitted to get rest of image.
	* sx1 = the column coordinate of the left-most pixel to include of the source. When omitted, the entire image is used
	* sy1 = the row coordinate of the upper-most pixel to include of the source. When omitted, the entire image is used
	* sx2 = the column coordinate of the right-most pixel to include of the source. Can be omitted to get rest of image.
	* sy2 = the row coordinate of the bottom-most pixel to include of the source. Can be omitted to get rest of image.
* sx1 = the column coordinate of the left-most pixel to include of the source. When omitted, the entire image is used
* sy1 = the row coordinate of the upper-most pixel to include of the source. When omitted, the entire image is used
* sx2 = the column coordinate of the right-most pixel to include of the source. Can be omitted to get rest of image.
* sy2 = the row coordinate of the bottom-most pixel to include of the source. Can be omitted to get rest of image.
* [_SMOOTH](_SMOOTH.md) applies linear filtering ( version 1.000 and up ).
Note: The PUT options PSET, PRESET, AND, OR and XOR are not available with _PUTIMAGE. QB64 can use transparency of colors to achieve the same results.


## DESCRIPTION
* [_PUTIMAGE](_PUTIMAGE.md) can be used without any handle parameters if the [_SOURCE](_SOURCE.md) and/or [_DEST](_DEST.md) are already defined.
* If the area of the source is bigger or smaller than the area of the destination then the image is adjusted to fit that area.
* Supports 32 bit alpha blending, color key transparency, true type fonts, stretching, mirroring/flipping, and a variety of graphics file formats including gif, png, bmp & jpg. 32 bit screen surface backgrounds (black) have zero [_ALPHA](_ALPHA.md) and are transparent when placed over other surfaces. Use [CLS](CLS.md) or [_DONTBLEND](_DONTBLEND.md) to make a new surface background [_ALPHA](_ALPHA.md) 255 or opaque.
* All graphical surfaces, including screen pages, can be acted upon in the same manner, and are referred to as "images".
* Hardware images (created using mode 33 via [_LOADIMAGE](_LOADIMAGE.md) or [_COPYIMAGE](_COPYIMAGE.md) ) can be used as the source or destination.
* Handles are used to identify graphical surfaces. Positive values are used to refer to screen pages. -1 (negative one) indicates an invalid surface. It is recommended to store image handles in [LONG](LONG.md) variables. Passing an invalid handle generates an "Invalid handle" error.
* When handles are not passed (or cannot be passed) to subs/functions then the default destination image or source image is referenced. These are set to the active page when the [SCREEN](SCREEN.md) statement is called, but can be changed to any image. So it is possible to read from one image using [POINT](POINT.md) and write to a different one with [PSET](PSET.md) .
* PRINTed text cannot be transferred and positioned accurately. Use [_PRINTSTRING](_PRINTSTRING.md) for graphical text or font placement.
* Images are not deallocated when the [SUB](SUB.md) or [FUNCTION](FUNCTION.md) they are created in ends. Free them with [_FREEIMAGE](_FREEIMAGE.md) .
* It is important to free discarded or unused images with [_FREEIMAGE](_FREEIMAGE.md) to prevent CPU memory overflow errors.


## EXAMPLES
> Example 1:

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

> Example 2: You don't need to do anything special to use a .PNG image with alpha/transparency. Here's a simple example:

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

> Example 3: Flipping and enlarging an image with _PUTIMAGE by swapping or increasing the desination coordinates.

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

> Example 4: Using _PUTIMAGE to scroll a larger image created on a separate _NEWIMAGE screen page with QB64.

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

> Example 5: _PUTIMAGE can be used with no parameters at all if the _SOURCE and _DEST are already set.

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

* Bitmaps
* SaveImage [SUB](SUB.md)

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```

* Featured in our "Keyword of the Day" series
* [_LOADIMAGE](_LOADIMAGE.md) , [_NEWIMAGE](_NEWIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_MAPTRIANGLE](_MAPTRIANGLE.md) , [STEP](STEP.md)
* [_DEST](_DEST.md) , [_SOURCE](_SOURCE.md) , [_FREEIMAGE](_FREEIMAGE.md)
* Hardware images

```vb
SCREEN 13
a& = _NEWIMAGE(640, 200, 13) ' creates a 640 * 200 image with the LONG handle a&
_DEST a& ' makes image a& the default drawing output.
LINE (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
_PUTIMAGE (0, 0)-(320, 200), a&, 0, (0, 0)-(320, 200)
```



## MORE EXAMPLES
* Bitmaps
* SaveImage [SUB](SUB.md)


# SEE ALSO
* Featured in our "Keyword of the Day" series
* [_LOADIMAGE](_LOADIMAGE.md) , [_NEWIMAGE](_NEWIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md) , [_SAVEIMAGE](_SAVEIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_MAPTRIANGLE](_MAPTRIANGLE.md) , [STEP](STEP.md)
* [_DEST](_DEST.md) , [_SOURCE](_SOURCE.md) , [_FREEIMAGE](_FREEIMAGE.md)
* Hardware images

