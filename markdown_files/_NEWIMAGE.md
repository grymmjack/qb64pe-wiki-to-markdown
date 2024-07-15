# _NEWIMAGE
> The _NEWIMAGE function prepares a window image surface and returns the LONG handle value.

## SYNTAX
`handle& = _NEWIMAGE ( width& , height& [, { 0 | 1 | 2 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 256 | 32 }])`

## PARAMETERS
* Minimum [LONG](LONG.md) screen dimensions are width& >= 1, height& >= 1 measured in pixels as [INTEGER](INTEGER.md) or [LONG](LONG.md) values. For mode 0 (text), width& and height& are measured in character blocks, not pixels.
	* For mode 0 (text), width& and height& are measured in character blocks, not pixels.
* For mode 0 (text), width& and height& are measured in character blocks, not pixels.
* Mode is either a QBasic type screen mode (0 to 2 or 7 to 13), 256 colors or 32 bit (16 million colors) compatible.


## DESCRIPTION
* If the mode is omitted, an image will be created with the same BPP mode, font (which may block freeing of that font), palette, selected colors, transparent color, blend state and print method settings as the current _DESTination image/ screen page.
* Valid [LONG](LONG.md) handle returns are less than -1. Invalid handles equal -1 and a zero or positive value is also invalid.
* You can create any sized window (limited by the OS) in any emulated [SCREEN](SCREEN.md) mode or 32 bit using this function.
* Default text block size in emulated [SCREEN](SCREEN.md) modes 1, 2, 7, 8 and 13 is 8 X 8; 9 and 10 is 8 X 14; 11, 12, 256 and 32 bit is 8 X 16. The text block pixel size will allow you to calculate the available text rows and columns in a custom sized screen.
* To view the image page, just use [SCREEN](SCREEN.md) handle& . Even if another procedure changes the screen mode and clears the screen, the image can be restored later by using the same [SCREEN](SCREEN.md) handle mode.
* Use the [_COPYIMAGE](_COPYIMAGE.md) function to preserve a [SCREEN](SCREEN.md) handle value when changing to another screen mode to restore it later.
* 32 bit screen surface backgrounds (black) have zero [_ALPHA](_ALPHA.md) so that they are transparent when placed over other surfaces.


## EXAMPLES
> Example 1: Shrinking a SCREEN 0 text window's size:

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```

> Example 2: Creating an 800 by 600 window version of SCREEN 12 with 256 colors (text 37 X 100):

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```

> Example 3: Setting up a 32 bit SCREEN with _NEWIMAGE for page flipping in QB64.

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```

> Example 4: Switching between two different SCREEN modes

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```

* SaveImage [SUB](SUB.md)
* [_PIXELSIZE](_PIXELSIZE.md)

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```

* [_COPYIMAGE](_COPYIMAGE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* [_SAVEIMAGE](_SAVEIMAGE.md)
* [_FREEIMAGE](_FREEIMAGE.md)
* [_PUTIMAGE](_PUTIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_CLIPBOARDIMAGE](_CLIPBOARDIMAGE.md) (function)
* [SCREEN](SCREEN.md)

```vb
SCREEN _NEWIMAGE(28, 25, 0)
```



## MORE EXAMPLES
* SaveImage [SUB](SUB.md)
* [_PIXELSIZE](_PIXELSIZE.md)


# SEE ALSO
* [_COPYIMAGE](_COPYIMAGE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* [_SAVEIMAGE](_SAVEIMAGE.md)
* [_FREEIMAGE](_FREEIMAGE.md)
* [_PUTIMAGE](_PUTIMAGE.md)
* [_SCREENIMAGE](_SCREENIMAGE.md)
* [_CLIPBOARDIMAGE](_CLIPBOARDIMAGE.md) (function)
* [SCREEN](SCREEN.md)

