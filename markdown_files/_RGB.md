


\_RGB - QB64 Phoenix Edition Wiki








# \_RGB



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_RGB function returns the closest palette attribute index (legacy SCREEN modes) OR the [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit color value (32-bit screens).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*colorIndex~&* = \_RGB(*red&*, *green&*, *blue&*[, *imageHandle&*])
  




## Description


* The value returned is either the closest color attribute number or a 32-bit [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") color value.
* **Return variable types must be [LONG](/qb64wiki/index.php/LONG "LONG") or resulting color may lose the [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") value.**
* *red&* specifies the red component intensity from 0 to 255.
* *green&* specifies the green component intensity from 0 to 255.
* *blue&* specifies the blue component intensity from 0 to 255.
* Intensity values outside the valid range are clipped.
* Returns [LONG](/qb64wiki/index.php/LONG "LONG") 32-bit hexadecimal values from **&HFF000000** to **&HFFFFFFFF**, always with full [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA").
* When [LONG](/qb64wiki/index.php/LONG "LONG") values are [PUT](/qb64wiki/index.php/PUT "PUT") to file, the ARGB values become BGRA. Use [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([MKL$](/qb64wiki/index.php/MKL$ "MKL$")(*colorIndex~&*), 3) to place 3 colors.
* If the *imageHandle&* is omitted the image is assumed to be the current [destination](/qb64wiki/index.php/DEST "DEST") or [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") page.
* Colors returned are always opaque as the transparency value is always 255. Use [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") or [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") to change it.
* **NOTE: Default 32-bit backgrounds are clear black or [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, 0). Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque.**


  




## Examples


*Example:* Converting the color port RGB intensity palette values 0 to 63 to 32 bit hexadecimal values.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [DIM](/qb64wiki/index.php/DIM "DIM") hex32$(15) [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") attribute = 1 [TO](/qb64wiki/index.php/TO "TO") 15   [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C7, attribute      'set color attribute to read   red = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values   grn = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4   blu = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4   hex32$(attribute) = "[&H](/qb64wiki/index.php/%26H "&H")" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")([_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(red, grn, blu))   'always returns the 32 bit value   [COLOR](/qb64wiki/index.php/COLOR "COLOR") attribute   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[COLOR](/qb64wiki/index.php/COLOR "COLOR")" + [STR$](/qb64wiki/index.php/STR$ "STR$")(_RGB(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` COLOR 1 = &HFF0000A8 COLOR 2 = &HFF00A800 COLOR 3 = &HFF00A8A8 COLOR 4 = &HFFA80000 COLOR 5 = &HFFA800A8 COLOR 6 = &HFFA85400 COLOR 7 = &HFFA8A8A8 COLOR 8 = &HFF545454 COLOR 9 = &HFF5454FC COLOR 10 = &HFF54FC54 COLOR 11 = &HFF54FCFC COLOR 12 = &HFFFC5454 COLOR 13 = &HFFFC54FC COLOR 14 = &HFFFCFC54 COLOR 15 = &HFFFCFCFC  ``` |
| --- |


*Note:* This procedure also shows how the returns from \_RGB and [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") differ in a non-32 bit screen mode.
  




## See also


* [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")
* [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")
* [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values"), [POINT](/qb64wiki/index.php/POINT "POINT")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Hexadecimal Color Values](http://www.w3schools.com/html/html_colornames.asp)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RGB&oldid=8668>"




## Navigation menu








### Search





















