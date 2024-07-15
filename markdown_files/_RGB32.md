# _RGB32
> The _RGB32 function returns the 32-bit RGBA color value with specified red, green and blue component intensities and optional alpha.

## PARAMETERS
* red& specifies the red [LONG](LONG.md) component intensity from 0 to 255.
* green& specifies the green [LONG](LONG.md) component intensity from 0 to 255.
* blue& specifies the blue [LONG](LONG.md) component intensity from 0 to 255.
* alpha& specifies the alpha [LONG](LONG.md) component from 0 to 255.
* intensity& specifies the red, green and blue [LONG](LONG.md) components intensity from 0 to 255 simultaneously, to generate a shade of gray.


## DESCRIPTION
* The value returned is always a 32-bit [_UNSIGNED](_UNSIGNED.md) [LONG](LONG.md) color value, as is the [POINT](POINT.md) value.
* Return variable types must be [_UNSIGNED](_UNSIGNED.md) [LONG](LONG.md) or [LONG](LONG.md) , otherwise resulting color may lose the [_BLUE](_BLUE.md) value.
* Parameter values outside of the 0 to 255 range are clipped.
* Returns [LONG](LONG.md) 32 bit hexadecimal values from &H00 00 00 00 to &HFF FF FF FF .
* When [LONG](LONG.md) values are [PUT](PUT.md) to file, the ARGB values become BGRA. Use LEFT$ ( MKL$ ( color32value~& ), 3) to place 3 colors.
* NOTE: Default 32-bit backgrounds are clear black or [_RGB32](_RGB32.md) (0, 0). Use [CLS](CLS.md) to make the black opaque.


## EXAMPLES
> Example 1: Converting the color port RGB intensity palette values 0 to 63 to 32 bit hexadecimal values.

```vb
SCREEN 12
DIM hex32$(15)
FOR attribute = 1 TO 15
 OUT &H3C7, attribute      'set color attribute to read
 red = INP(&H3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
 grn = INP(&H3C9) * 4
 blu = INP(&H3C9) * 4
 hex32$(attribute) = "&H" + HEX$(_RGB32(red, grn, blu))   'always returns the 32 bit value
 COLOR attribute
 PRINT "COLOR" + STR$(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
NEXT
```

> Example 2: Working with 32 bit colors.

```vb
SCREEN 12
DIM hex32$(15)
FOR attribute = 1 TO 15
 OUT &H3C7, attribute      'set color attribute to read
 red = INP(&H3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
 grn = INP(&H3C9) * 4
 blu = INP(&H3C9) * 4
 hex32$(attribute) = "&H" + HEX$(_RGB32(red, grn, blu))   'always returns the 32 bit value
 COLOR attribute
 PRINT "COLOR" + STR$(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
NEXT
```

> Example 3: Comparing the output of the new _RGB32 syntaxes (starting with version 1.3) and their equivalents in previous versions.

```vb
SCREEN 12
DIM hex32$(15)
FOR attribute = 1 TO 15
 OUT &H3C7, attribute      'set color attribute to read
 red = INP(&H3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
 grn = INP(&H3C9) * 4
 blu = INP(&H3C9) * 4
 hex32$(attribute) = "&H" + HEX$(_RGB32(red, grn, blu))   'always returns the 32 bit value
 COLOR attribute
 PRINT "COLOR" + STR$(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
NEXT
```


```vb
SCREEN 12
DIM hex32$(15)
FOR attribute = 1 TO 15
 OUT &H3C7, attribute      'set color attribute to read
 red = INP(&H3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
 grn = INP(&H3C9) * 4
 blu = INP(&H3C9) * 4
 hex32$(attribute) = "&H" + HEX$(_RGB32(red, grn, blu))   'always returns the 32 bit value
 COLOR attribute
 PRINT "COLOR" + STR$(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
NEXT
```

* [_RGBA32](_RGBA32.md) , [_RGB](_RGB.md) , [_RGBA](_RGBA.md)
* [_RED32](_RED32.md) , [_GREEN32](_GREEN32.md) , [_BLUE32](_BLUE32.md)
* [_PALETTECOLOR](_PALETTECOLOR.md)
* HEX$ 32 Bit Values
* SaveImage [SUB](SUB.md)
* Hexadecimal Color Values

```vb
SCREEN 12
DIM hex32$(15)
FOR attribute = 1 TO 15
 OUT &H3C7, attribute      'set color attribute to read
 red = INP(&H3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
 grn = INP(&H3C9) * 4
 blu = INP(&H3C9) * 4
 hex32$(attribute) = "&H" + HEX$(_RGB32(red, grn, blu))   'always returns the 32 bit value
 COLOR attribute
 PRINT "COLOR" + STR$(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
NEXT
```



# SEE ALSO
* [_RGBA32](_RGBA32.md) , [_RGB](_RGB.md) , [_RGBA](_RGBA.md)
* [_RED32](_RED32.md) , [_GREEN32](_GREEN32.md) , [_BLUE32](_BLUE32.md)
* [_PALETTECOLOR](_PALETTECOLOR.md)
* HEX$ 32 Bit Values
* SaveImage [SUB](SUB.md)
* Hexadecimal Color Values

