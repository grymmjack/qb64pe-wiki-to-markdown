# _CLEARCOLOR
> The _CLEARCOLOR statement sets a specific color to be treated as transparent when an image is later put (via _PUTIMAGE ) onto another image.

## SYNTAX
`_CLEARCOLOR { color& |_NONE}[, Dest_Handle& ]`

## PARAMETERS
* In color modes using a palette, color& is the palette index of the new transparent color value or [_NONE](_NONE.md) designates no clear colors.
* If color& is not a valid palette index, an illegal function call error will occur.
* In 32-bit color modes, color& is the _LONG color value of the new transparent color.
* If Dest_Handle& is omitted, the destination is assumed to be the current write page. Zero can designate the current program screen.


## DESCRIPTION
* If Dest_Handle& is an invalid handle, then an invalid handle error is returned. Check for bad handle values of -1 first.
* In 32-bit color modes, it simply sets the Alpha to 0 for all pixels matching the specified color.
* In the second syntax, transparency is disabled for color modes using a palette.
* Note: [_SETALPHA](_SETALPHA.md) can affect any [_CLEARCOLOR](_CLEARCOLOR.md) alpha setting within the color range set.
* NOTE: 32 bit [_NEWIMAGE](_NEWIMAGE.md) screen page backgrounds are transparent black or [_ALPHA](_ALPHA.md) 0. Use [_DONTBLEND](_DONTBLEND.md) or [CLS](CLS.md) for opaque.


## EXAMPLES
> Example 1: Using _CLEARCOLOR to "mask" the background color of an image.

```vb
SCREEN 13
img& = _LOADIMAGE("qb64_trans.png")
_PUTIMAGE , img&, 0 'place actual image with background
K$ = INPUT$(1)
CLS , _RGB(255, 0, 0) 'clear screen with red background
_CLEARCOLOR _RGB(255, 255, 255), img&
_PUTIMAGE , img&, 0 'place image without white background
PRINT _CLEARCOLOR(img&) 'displays closest clear color attribute
END
```

> Example 2: Using a _CLEARCOLOR transparency with images created on a _NEWIMAGE page. Does not require an image file.

```vb
SCREEN 13
img& = _LOADIMAGE("qb64_trans.png")
_PUTIMAGE , img&, 0 'place actual image with background
K$ = INPUT$(1)
CLS , _RGB(255, 0, 0) 'clear screen with red background
_CLEARCOLOR _RGB(255, 255, 255), img&
_PUTIMAGE , img&, 0 'place image without white background
PRINT _CLEARCOLOR(img&) 'displays closest clear color attribute
END
```

> Example 3: Fading an image with a _CLEARCOLOR background using a new page image to prevent _SETALPHA changes.

```vb
SCREEN 13
img& = _LOADIMAGE("qb64_trans.png")
_PUTIMAGE , img&, 0 'place actual image with background
K$ = INPUT$(1)
CLS , _RGB(255, 0, 0) 'clear screen with red background
_CLEARCOLOR _RGB(255, 255, 255), img&
_PUTIMAGE , img&, 0 'place image without white background
PRINT _CLEARCOLOR(img&) 'displays closest clear color attribute
END
```


```vb
SCREEN 13
img& = _LOADIMAGE("qb64_trans.png")
_PUTIMAGE , img&, 0 'place actual image with background
K$ = INPUT$(1)
CLS , _RGB(255, 0, 0) 'clear screen with red background
_CLEARCOLOR _RGB(255, 255, 255), img&
_PUTIMAGE , img&, 0 'place image without white background
PRINT _CLEARCOLOR(img&) 'displays closest clear color attribute
END
```

* [_CLEARCOLOR](_CLEARCOLOR.md) (function)
* [_SETALPHA](_SETALPHA.md) (sets transparency level)
* [_ALPHA](_ALPHA.md) , [_ALPHA32](_ALPHA32.md) (read functions)
* Images , Creating Sprite Masks

```vb
SCREEN 13
img& = _LOADIMAGE("qb64_trans.png")
_PUTIMAGE , img&, 0 'place actual image with background
K$ = INPUT$(1)
CLS , _RGB(255, 0, 0) 'clear screen with red background
_CLEARCOLOR _RGB(255, 255, 255), img&
_PUTIMAGE , img&, 0 'place image without white background
PRINT _CLEARCOLOR(img&) 'displays closest clear color attribute
END
```



# SEE ALSO
* [_CLEARCOLOR](_CLEARCOLOR.md) (function)
* [_SETALPHA](_SETALPHA.md) (sets transparency level)
* [_ALPHA](_ALPHA.md) , [_ALPHA32](_ALPHA32.md) (read functions)
* Images , Creating Sprite Masks

