# _DESKTOPHEIGHT
> The _DESKTOPHEIGHT function returns the height of the users current desktop.

## SYNTAX
`y& = _DESKTOPHEIGHT`

## DESCRIPTION
* No parameters are needed for this function.
* This returns the height of the user's desktop, not the size of any screen or window which might be open on that desktop.


## EXAMPLES

```vb
s& = _NEWIMAGE(800, 600, 256)
SCREEN s&
PRINT _DESKTOPWIDTH, _DESKTOPHEIGHT
PRINT _WIDTH, _HEIGHT
```

* [_HEIGHT](_HEIGHT.md) , [_DESKTOPWIDTH](_DESKTOPWIDTH.md)
* [_WIDTH](_WIDTH.md) , [_SCREENIMAGE](_SCREENIMAGE.md)

```vb
s& = _NEWIMAGE(800, 600, 256)
SCREEN s&
PRINT _DESKTOPWIDTH, _DESKTOPHEIGHT
PRINT _WIDTH, _HEIGHT
```



# SEE ALSO
* [_HEIGHT](_HEIGHT.md) , [_DESKTOPWIDTH](_DESKTOPWIDTH.md)
* [_WIDTH](_WIDTH.md) , [_SCREENIMAGE](_SCREENIMAGE.md)

