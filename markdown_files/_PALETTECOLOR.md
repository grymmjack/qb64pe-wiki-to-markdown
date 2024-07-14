


\_PALETTECOLOR - QB64 Phoenix Edition Wiki








# \_PALETTECOLOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PALETTECOLOR statement sets the color value of a palette entry of an image using 256 color modes or less (4 or 8 BPP).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_PALETTECOLOR *attribute%*, *newColor&*[, *destHandle&*]
  




## Description


* The *attribute%* is the palette index number of the color to set, ranging from 0 to 15 (4 bit) or 0 to 255 (8 bit) color modes.
* The [LONG](/qb64wiki/index.php/LONG "LONG") *newColor&* is the new color value to set using [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") or [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") values or using [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values").
* If *destHandle&* is omitted, [destination](/qb64wiki/index.php/DEST "DEST") is assumed to be the current write page or screen surface.
* If *attribute%* is outside of image or [screen](/qb64wiki/index.php/SCREEN "SCREEN") mode attribute range (0 to 15 or 0 to 255), an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* If *destHandle&* does not use a palette, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs. **Will not work in 24/32 bit color palette modes.**
* If *destHandle&* is an invalid handle value, an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs.


  




**Basic's 16 Default Color Attributes (non-[DAC](/qb64wiki/index.php/DAC "DAC"))**


| ```      Attribute        Description     Red   Green   Blue   32 HEX    HTML Name           0            Black            0      0       0    000000    Black          1            Dark Blue        0      0      42    00008B    DarkBlue          2            Dark Green       0     42       0    006400    DarkGreen          3            Dark Cyan        0     42      42    008B8B    DarkCyan          4            Dark Red        42      0       0    8B0000    DarkRed          5            Dark Magenta    42      0      42    8B008B    DarkMagenta          6            Dark Yellow     42     21       0    DAA520    GoldenRod          7            Light Grey      42     42      42    D3D3D3    LightGrey          8            Dark Grey       21     21      21    696969    DimGray          9            Blue            21     21      63    0000FF    Blue         10            Green           21     63      21    15FF15    Lime         11            Cyan            21     63      63    15FFFF    Cyan         12            Red             63     21      21    FF1515    Red         13            Magenta         63     21      63    FF15FF    Magenta         14            Yellow          63     63      21    FFFF00    Yellow         15            White           63     63      63    FFFFFF    White  ``` |
| --- |


[HTML Color Table Values and Names](http://www.w3schools.com/html/html_colornames.asp) or [Other RGB colors](http://www.tayloredmktg.com/rgb/#OR)
*Note:* **QB64** 32 bit color intensity values from 0 to 255 can be found by multiplying above values by 4.
*Summary:* The red, green, and blue intensity values can be changed using [OUT](/qb64wiki/index.php/OUT "OUT") or [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE") statements. Some **QBasic** RGB color attribute values can be changed in [DAC](/qb64wiki/index.php/DAC "DAC") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes and the [DAC](/qb64wiki/index.php/DAC "DAC") RGB intensity settings may be different.


  




## Examples


*Example:* Creating custom background colors in SCREEN 0 that follow the text. [CLS](/qb64wiki/index.php/CLS "CLS") makes entire background one color.





| ``` _PALETTECOLOR 1, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 255, 255) ' white. _PALETTECOLOR 2, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 170, 170) ' lighter red. _PALETTECOLOR 3, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 85, 85) ' light red. _PALETTECOLOR 4, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 0, 0) ' red. _PALETTECOLOR 5, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(170, 0, 0) ' dark red. _PALETTECOLOR 6, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(85, 0, 0) ' darker red.  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on white." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on lighter red." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on light red." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on red." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 5: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on dark red." [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "black on darker red.  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 1, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "white on darker red" [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2, 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ligher red on darker red"  ``` |
| --- |


*Note:* \_PALETTECOLOR expects [LONG](/qb64wiki/index.php/LONG "LONG") [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") or [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") 32 bit color values, not [\_RGB](/qb64wiki/index.php/RGB "RGB") or [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") palette attribute values.
  




## See also


* [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [\_PALETTECOLOR (function)](/qb64wiki/index.php/PALETTECOLOR_(function) "PALETTECOLOR (function)")
* [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE"), [OUT](/qb64wiki/index.php/OUT "OUT"), [INP](/qb64wiki/index.php/INP "INP")
* [Images](/qb64wiki/index.php/Images "Images")
* [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PALETTECOLOR&oldid=7921>"




## Navigation menu








### Search





















