# _PALETTECOLOR
> The _PALETTECOLOR statement sets the color value of a palette entry of an image using 256 color modes or less (4 or 8 BPP).

## SYNTAX
`_PALETTECOLOR attribute% , newColor& [, destHandle& ]`

## DESCRIPTION
* The attribute% is the palette index number of the color to set, ranging from 0 to 15 (4 bit) or 0 to 255 (8 bit) color modes.
* The [LONG](LONG.md) newColor& is the new color value to set using [_RGB32](_RGB32.md) or [_RGBA32](_RGBA32.md) values or using HEX$ 32 Bit Values .
* If destHandle& is omitted, destination is assumed to be the current write page or screen surface.
* If attribute% is outside of image or screen mode attribute range (0 to 15 or 0 to 255), an illegal function call error will occur.
* If destHandle& does not use a palette, an illegal function call error occurs. Will not work in 24/32 bit color palette modes.
* If destHandle& is an invalid handle value, an invalid handle error occurs.


## EXAMPLES
> Example: Creating custom background colors in SCREEN 0 that follow the text. CLS makes entire background one color.

```vb
Attribute        Description     Red   Green   Blue   32 HEX    HTML Name 
        0            Black            0      0       0    000000    Black
        1            Dark Blue        0      0      42    00008B    DarkBlue
        2            Dark Green       0     42       0    006400    DarkGreen
        3            Dark Cyan        0     42      42    008B8B    DarkCyan
        4            Dark Red        42      0       0    8B0000    DarkRed
        5            Dark Magenta    42      0      42    8B008B    DarkMagenta
        6            Dark Yellow     42     21       0    DAA520    GoldenRod
        7            Light Grey      42     42      42    D3D3D3    LightGrey
        8            Dark Grey       21     21      21    696969    DimGray
        9            Blue            21     21      63    0000FF    Blue
       10            Green           21     63      21    15FF15    Lime
       11            Cyan            21     63      63    15FFFF    Cyan
       12            Red             63     21      21    FF1515    Red
       13            Magenta         63     21      63    FF15FF    Magenta
       14            Yellow          63     63      21    FFFF00    Yellow
       15            White           63     63      63    FFFFFF    White
```


```vb
Attribute        Description     Red   Green   Blue   32 HEX    HTML Name 
        0            Black            0      0       0    000000    Black
        1            Dark Blue        0      0      42    00008B    DarkBlue
        2            Dark Green       0     42       0    006400    DarkGreen
        3            Dark Cyan        0     42      42    008B8B    DarkCyan
        4            Dark Red        42      0       0    8B0000    DarkRed
        5            Dark Magenta    42      0      42    8B008B    DarkMagenta
        6            Dark Yellow     42     21       0    DAA520    GoldenRod
        7            Light Grey      42     42      42    D3D3D3    LightGrey
        8            Dark Grey       21     21      21    696969    DimGray
        9            Blue            21     21      63    0000FF    Blue
       10            Green           21     63      21    15FF15    Lime
       11            Cyan            21     63      63    15FFFF    Cyan
       12            Red             63     21      21    FF1515    Red
       13            Magenta         63     21      63    FF15FF    Magenta
       14            Yellow          63     63      21    FFFF00    Yellow
       15            White           63     63      63    FFFFFF    White
```

* [COLOR](COLOR.md) , [_RGB32](_RGB32.md) , [_RGBA32](_RGBA32.md)
* [_PALETTECOLOR](_PALETTECOLOR.md) (function)
* [PALETTE](PALETTE.md) , [OUT](OUT.md) , [INP](INP.md)
* Images
* HEX$ 32 Bit Values

```vb
Attribute        Description     Red   Green   Blue   32 HEX    HTML Name 
        0            Black            0      0       0    000000    Black
        1            Dark Blue        0      0      42    00008B    DarkBlue
        2            Dark Green       0     42       0    006400    DarkGreen
        3            Dark Cyan        0     42      42    008B8B    DarkCyan
        4            Dark Red        42      0       0    8B0000    DarkRed
        5            Dark Magenta    42      0      42    8B008B    DarkMagenta
        6            Dark Yellow     42     21       0    DAA520    GoldenRod
        7            Light Grey      42     42      42    D3D3D3    LightGrey
        8            Dark Grey       21     21      21    696969    DimGray
        9            Blue            21     21      63    0000FF    Blue
       10            Green           21     63      21    15FF15    Lime
       11            Cyan            21     63      63    15FFFF    Cyan
       12            Red             63     21      21    FF1515    Red
       13            Magenta         63     21      63    FF15FF    Magenta
       14            Yellow          63     63      21    FFFF00    Yellow
       15            White           63     63      63    FFFFFF    White
```



# SEE ALSO
* [COLOR](COLOR.md) , [_RGB32](_RGB32.md) , [_RGBA32](_RGBA32.md)
* [_PALETTECOLOR](_PALETTECOLOR.md) (function)
* [PALETTE](PALETTE.md) , [OUT](OUT.md) , [INP](INP.md)
* Images
* HEX$ 32 Bit Values

