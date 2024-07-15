# _DEST
> The _DEST statement sets the current write image or page. All graphic and print changes will be done to this image.

## SYNTAX
`_DEST imageHandle&`

## DESCRIPTION
* imageHandle& is the handle of the image that will act as the current write page.
* [_DEST](_DEST.md) 0 refers to the present program [SCREEN](SCREEN.md) . You can use 0 to refer to the present program [SCREEN](SCREEN.md) .
* [_DEST](_DEST.md) [_CONSOLE](_CONSOLE.md) can set the destination to send information to a console window using [PRINT](PRINT.md) or [INPUT](INPUT.md) .
* If imageHandle& is an invalid handle, an invalid handle error occurs. Always check for valid handle values first ( imageHandle& < -1).
* Note: Use [_SOURCE](_SOURCE.md) when you need to read a page or image with [POINT](POINT.md) , [GET](GET.md) or the [SCREEN](SCREEN.md) function.


## EXAMPLES
> Example 1: Placing a center point and a circle using _CLEARCOLOR to eliminate the background color black.

```vb
SCREEN 13 'program screen can use 256 colors
a& = _NEWIMAGE(320, 200, 13) 'create 2 screen page handles a& and b&
b& = _NEWIMAGE(320, 200, 13)
_DEST a& 'set destination image to handle a&
PSET (100, 100), 15 'draw a dot on the current destination handle a&
_DEST b& 'set destination image to handle b&
CIRCLE (100, 100), 50, 15 'draw a circle on the current destination handle b&
_CLEARCOLOR 0 'make page b color 0 (black) transparent
_PUTIMAGE , b&, a& 'put circle on image b to image a& (a PSET dot)
_PUTIMAGE , a&, 0 'put what is on image a& to the screen (handle 0)
```

> Example 2: Demonstrates how printed text can be stretched using _PUTIMAGE with _DEST pages.

```vb
SCREEN 13 'program screen can use 256 colors
a& = _NEWIMAGE(320, 200, 13) 'create 2 screen page handles a& and b&
b& = _NEWIMAGE(320, 200, 13)
_DEST a& 'set destination image to handle a&
PSET (100, 100), 15 'draw a dot on the current destination handle a&
_DEST b& 'set destination image to handle b&
CIRCLE (100, 100), 50, 15 'draw a circle on the current destination handle b&
_CLEARCOLOR 0 'make page b color 0 (black) transparent
_PUTIMAGE , b&, a& 'put circle on image b to image a& (a PSET dot)
_PUTIMAGE , a&, 0 'put what is on image a& to the screen (handle 0)
```


```vb
SCREEN 13 'program screen can use 256 colors
a& = _NEWIMAGE(320, 200, 13) 'create 2 screen page handles a& and b&
b& = _NEWIMAGE(320, 200, 13)
_DEST a& 'set destination image to handle a&
PSET (100, 100), 15 'draw a dot on the current destination handle a&
_DEST b& 'set destination image to handle b&
CIRCLE (100, 100), 50, 15 'draw a circle on the current destination handle b&
_CLEARCOLOR 0 'make page b color 0 (black) transparent
_PUTIMAGE , b&, a& 'put circle on image b to image a& (a PSET dot)
_PUTIMAGE , a&, 0 'put what is on image a& to the screen (handle 0)
```

* [_DEST](_DEST.md) (function)
* [_SOURCE](_SOURCE.md)
* [_PUTIMAGE](_PUTIMAGE.md)
* [_CONSOLE](_CONSOLE.md)

```vb
SCREEN 13 'program screen can use 256 colors
a& = _NEWIMAGE(320, 200, 13) 'create 2 screen page handles a& and b&
b& = _NEWIMAGE(320, 200, 13)
_DEST a& 'set destination image to handle a&
PSET (100, 100), 15 'draw a dot on the current destination handle a&
_DEST b& 'set destination image to handle b&
CIRCLE (100, 100), 50, 15 'draw a circle on the current destination handle b&
_CLEARCOLOR 0 'make page b color 0 (black) transparent
_PUTIMAGE , b&, a& 'put circle on image b to image a& (a PSET dot)
_PUTIMAGE , a&, 0 'put what is on image a& to the screen (handle 0)
```



# SEE ALSO
* [_DEST](_DEST.md) (function)
* [_SOURCE](_SOURCE.md)
* [_PUTIMAGE](_PUTIMAGE.md)
* [_CONSOLE](_CONSOLE.md)

