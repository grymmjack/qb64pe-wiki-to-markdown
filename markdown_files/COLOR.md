# COLOR
> The COLOR statement is used to change the foreground and background colors for printing text.

## SYNTAX
`COLOR [ foreground& ][, background& ]`

## DESCRIPTION
* background& colors are available in all QB64 color [SCREEN](SCREEN.md) modes.
* [SCREEN](SCREEN.md) mode 10 has only 3 white foreground attributes including flashing.
* To change the background& color only, use a comma and the desired color. Ex: [COLOR](COLOR.md) , background&
* Graphic drawing statements like [PSET](PSET.md) , [PRESET](PRESET.md) , [LINE](LINE.md) , etc, also use the colors set by the [COLOR](COLOR.md) statement if no color is passed when they are called.
* The $[COLOR](COLOR.md) metacommand adds named color constants for both text and 32-bit modes.


## EXAMPLES
> Example 1: Reading the default RGB color settings of color attribute 15.

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```

> Example 2: Changing the color settings of attribute 0 (the background) to blue in SCREENs 12 or 13.

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```

> Example 3: Printing in fullscreen SCREEN 0 mode with a color background under the text only.

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```

> Example 4: Using CLS after setting the background color in SCREEN 0 to make the color cover the entire screen.

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```

> Example 5: Using a different foreground color for each letter:

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```


```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```

* $[COLOR](COLOR.md) (metacommand)
* [_RGB](_RGB.md) , [_RGBA](_RGBA.md) , [_RGB32](_RGB32.md) , RGBA32 .
* [_RED](_RED.md) , [_GREEN](_GREEN.md) , [_BLUE](_BLUE.md)
* [_RED32](_RED32.md) , [_GREEN32](_GREEN32.md) , [_BLUE32](_BLUE32.md)
* [_ALPHA](_ALPHA.md) , [_ALPHA32](_ALPHA32.md) , [_CLEARCOLOR](_CLEARCOLOR.md)
* [PRINT](PRINT.md) , [LOCATE](LOCATE.md) , [SCREEN](SCREEN.md)
* [POINT](POINT.md) , [SCREEN](SCREEN.md) (function)
* [OUT](OUT.md) , [INP](INP.md) , [PALETTE](PALETTE.md)
* [_BLINK](_BLINK.md)
* [_DEFAULTCOLOR](_DEFAULTCOLOR.md)
* [_BACKGROUNDCOLOR](_BACKGROUNDCOLOR.md)
* [_PALETTECOLOR](_PALETTECOLOR.md)
* Color Dialog Box
* $[COLOR](COLOR.md):0 Name Table
* $[COLOR](COLOR.md):32 Name Table

```vb
SCREEN 12
alpha$ = "FF" 'solid alpha colors only
PRINT "Attribute = Hex value      Red          Green         Blue "
PRINT
COLOR 7
FOR attribute = 1 TO 15
 OUT &H3C7, attribute 'set color attribute to read
 red$ = HEX$(INP(&H3C9) * 255 / 63) 'convert port setting to 32 bit values
 grn$ = HEX$(INP(&H3C9) * 255 / 63)
 blu$ = HEX$(INP(&H3C9) * 255 / 63)
 IF LEN(red$) = 1 THEN red$ = "0" + red$ '2 hex digits required
 IF LEN(grn$) = 1 THEN grn$ = "0" + grn$ 'for low or zero hex values
 IF LEN(blu$) = 1 THEN blu$ = "0" + blu$
 hex32$ = "&H" + alpha$ + red$ + grn$ + blu$
 _PALETTECOLOR attribute, VAL(hex32$) 'VAL converts hex string to a LONG 32 bit value
 IF attribute THEN COLOR attribute 'exclude black color print
 PRINT "COLOR" + STR$(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute
NEXT
```



# SEE ALSO
* $[COLOR](COLOR.md) (metacommand)
* [_RGB](_RGB.md) , [_RGBA](_RGBA.md) , [_RGB32](_RGB32.md) , RGBA32 .
* [_RED](_RED.md) , [_GREEN](_GREEN.md) , [_BLUE](_BLUE.md)
* [_RED32](_RED32.md) , [_GREEN32](_GREEN32.md) , [_BLUE32](_BLUE32.md)
* [_ALPHA](_ALPHA.md) , [_ALPHA32](_ALPHA32.md) , [_CLEARCOLOR](_CLEARCOLOR.md)
* [PRINT](PRINT.md) , [LOCATE](LOCATE.md) , [SCREEN](SCREEN.md)
* [POINT](POINT.md) , [SCREEN](SCREEN.md) (function)
* [OUT](OUT.md) , [INP](INP.md) , [PALETTE](PALETTE.md)
* [_BLINK](_BLINK.md)
* [_DEFAULTCOLOR](_DEFAULTCOLOR.md)
* [_BACKGROUNDCOLOR](_BACKGROUNDCOLOR.md)
* [_PALETTECOLOR](_PALETTECOLOR.md)
* Color Dialog Box
* $[COLOR](COLOR.md):0 Name Table
* $[COLOR](COLOR.md):32 Name Table

