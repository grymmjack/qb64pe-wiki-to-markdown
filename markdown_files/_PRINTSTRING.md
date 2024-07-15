# _PRINTSTRING
> The _PRINTSTRING statement prints text strings using graphic column and row coordinate positions.

## SYNTAX
`_PRINTSTRING ( column , row ), textExpression$ [, imageHandle& ]`

## PARAMETERS
* column and row are [INTEGER](INTEGER.md) or [LONG](LONG.md) starting PIXEL (graphic) column and row coordinates to set text or custom fonts.
* textExpression$ is any literal or variable string value of text to be displayed.
* imageHandle& is the optional image or destination to use. Zero designates current [SCREEN](SCREEN.md) page.


## DESCRIPTION
* The starting coordinate sets the top left corner of the text to be printed. Use [_FONTHEIGHT](_FONTHEIGHT.md) to calculate that text or font position
* The [_FONT](_FONT.md) size can affect the screen and row heights. Custom fonts are not required. [_PRINTSTRING](_PRINTSTRING.md) can print all ASCII characters.
	* Custom fonts are not required. [_PRINTSTRING](_PRINTSTRING.md) can print all ASCII characters.
* Custom fonts are not required. [_PRINTSTRING](_PRINTSTRING.md) can print all ASCII characters.
* [_PRINTWIDTH](_PRINTWIDTH.md) can be used to determine how wide a text print will be so that the screen width is not exceeded.
* If the imageHandle& is omitted, the current image, page or screen destination is used.
* Can use the current font alpha blending with a designated image background. See the [_RGBA](_RGBA.md) function example.
* Use the [_PRINTMODE](_PRINTMODE.md) statement before printing to set how the background is rendered. Use the [_PRINTMODE](_PRINTMODE.md) (function) to find the current [_PRINTMODE](_PRINTMODE.md) setting.
	* Use the [_PRINTMODE](_PRINTMODE.md) (function) to find the current [_PRINTMODE](_PRINTMODE.md) setting.
* Use the [_PRINTMODE](_PRINTMODE.md) (function) to find the current [_PRINTMODE](_PRINTMODE.md) setting.
* In [SCREEN](SCREEN.md) 0 (text only), [_PRINTSTRING](_PRINTSTRING.md) works as one-line replacement for [LOCATE](LOCATE.md) x, y: [PRINT](PRINT.md) text$ , without changing the current cursor position.


## EXAMPLES
> Example 1: Printing those unprintable ASCII control characters is no longer a problem!

```vb
SCREEN _NEWIMAGE(800, 600, 256)

FOR code = 0 TO 31
 chrstr$ = chrstr$ + CHR$(code) + SPACE$(1)
NEXT

_FONT _LOADFONT("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font

_PRINTSTRING (0, 16), chrstr$

END
```

> Example 2: Making any QB64 program window larger using a SUB that easily converts PRINT to _PRINTSTRING .

```vb
SCREEN _NEWIMAGE(800, 600, 256)

FOR code = 0 TO 31
 chrstr$ = chrstr$ + CHR$(code) + SPACE$(1)
NEXT

_FONT _LOADFONT("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font

_PRINTSTRING (0, 16), chrstr$

END
```

> Example 3: Rotating a text string around a graphic object.

```vb
SCREEN _NEWIMAGE(800, 600, 256)

FOR code = 0 TO 31
 chrstr$ = chrstr$ + CHR$(code) + SPACE$(1)
NEXT

_FONT _LOADFONT("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font

_PRINTSTRING (0, 16), chrstr$

END
```


```vb
SCREEN _NEWIMAGE(800, 600, 256)

FOR code = 0 TO 31
 chrstr$ = chrstr$ + CHR$(code) + SPACE$(1)
NEXT

_FONT _LOADFONT("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font

_PRINTSTRING (0, 16), chrstr$

END
```

* [_NEWIMAGE](_NEWIMAGE.md) , [_PRINTWIDTH](_PRINTWIDTH.md) , [_PRINTMODE](_PRINTMODE.md)
* [_CONTROLCHR](_CONTROLCHR.md)
* [_FONT](_FONT.md) , [_LOADFONT](_LOADFONT.md) , [_FONTHEIGHT](_FONTHEIGHT.md) , [_FONTWIDTH](_FONTWIDTH.md)
* [_SCREENIMAGE](_SCREENIMAGE.md) , [_SCREENPRINT](_SCREENPRINT.md)
* Text Using Graphics

```vb
SCREEN _NEWIMAGE(800, 600, 256)

FOR code = 0 TO 31
 chrstr$ = chrstr$ + CHR$(code) + SPACE$(1)
NEXT

_FONT _LOADFONT("C:\Windows\Fonts\Cour.ttf", 20, "MONOSPACE") 'select monospace font

_PRINTSTRING (0, 16), chrstr$

END
```



# SEE ALSO
* [_NEWIMAGE](_NEWIMAGE.md) , [_PRINTWIDTH](_PRINTWIDTH.md) , [_PRINTMODE](_PRINTMODE.md)
* [_CONTROLCHR](_CONTROLCHR.md)
* [_FONT](_FONT.md) , [_LOADFONT](_LOADFONT.md) , [_FONTHEIGHT](_FONTHEIGHT.md) , [_FONTWIDTH](_FONTWIDTH.md)
* [_SCREENIMAGE](_SCREENIMAGE.md) , [_SCREENPRINT](_SCREENPRINT.md)
* Text Using Graphics

