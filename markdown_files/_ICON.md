# _ICON
> The _ICON statement uses an image handle from _LOADIMAGE for the program header and icon image in the OS.

## SYNTAX
`_ICON [ mainImageHandle& [, smallImageHandle& ]]`

## PARAMETERS
* mainImageHandle& is the [LONG](LONG.md) handle value of the OS icon and title bar image pre-loaded with [_LOADIMAGE](_LOADIMAGE.md) when used alone.
* smallImageHandle& is the [LONG](LONG.md) handle value of a different title bar image pre-loaded with [_LOADIMAGE](_LOADIMAGE.md) when used.
* No image handle designates use of the default QB64 icon or the embedded icon set by $EXEICON .


## DESCRIPTION
* If no image handle is passed, the default QB64 icon will be used (all versions). If the $EXEICON metacommand is used, [_ICON](_ICON.md) without an image handle uses the embedded icon from the binary (Windows only).
* Beginning with version 1.000 , the following is considered:


## EXAMPLES
> Example 1: Loading an image to a 32 bit palette in SCREEN 0 (the default screen mode).

```vb
i& =_LOADIMAGE("RDSWU16.BMP", 32) '<<<<<<< use your image file name here

IF i& < -1 THEN
 _ICON i&
 _FREEIMAGE i& ' release image handle after setting icon
END IF
```

> Example 2: Function that converts an icon into a temporary bitmap for use in QB64. Function returns the available image count.

```vb
i& =_LOADIMAGE("RDSWU16.BMP", 32) '<<<<<<< use your image file name here

IF i& < -1 THEN
 _ICON i&
 _FREEIMAGE i& ' release image handle after setting icon
END IF
```


```vb
i& =_LOADIMAGE("RDSWU16.BMP", 32) '<<<<<<< use your image file name here

IF i& < -1 THEN
 _ICON i&
 _FREEIMAGE i& ' release image handle after setting icon
END IF
```

* [_TITLE](_TITLE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* $EXEICON
* Creating Icon Bitmaps (member-contributed program)
* Bitmaps , Icons and Cursors
* Icon Extraction

```vb
i& =_LOADIMAGE("RDSWU16.BMP", 32) '<<<<<<< use your image file name here

IF i& < -1 THEN
 _ICON i&
 _FREEIMAGE i& ' release image handle after setting icon
END IF
```



# SEE ALSO
* [_TITLE](_TITLE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* $EXEICON
* Creating Icon Bitmaps (member-contributed program)
* Bitmaps , Icons and Cursors
* Icon Extraction

