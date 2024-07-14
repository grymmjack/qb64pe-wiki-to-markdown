


\_RGB32 - QB64 Phoenix Edition Wiki








# \_RGB32



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_RGB32 function returns the 32-bit *RGBA* color value with specified red, green and blue component intensities and optional alpha.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*Original syntax*:



*color32value~&* = \_RGB32(*red&*, *green&*, *blue&*)
*Alternative Syntax 2*:



*color32value~&* = \_RGB32(*red&*, *green&*, *blue&*, *alpha&*)
*Alternative Syntax 3*:



*color32value~&* = \_RGB32(*intensity&*, *alpha&*)
*Alternative Syntax 4*:



*color32value~&* = \_RGB32(*intensity&*)
  




## Parameters


* *red&* specifies the red [LONG](/qb64wiki/index.php/LONG "LONG") component intensity from 0 to 255.
* *green&* specifies the green [LONG](/qb64wiki/index.php/LONG "LONG") component intensity from 0 to 255.
* *blue&* specifies the blue [LONG](/qb64wiki/index.php/LONG "LONG") component intensity from 0 to 255.
* *alpha&* specifies the alpha [LONG](/qb64wiki/index.php/LONG "LONG") component from 0 to 255.
* *intensity&* specifies the red, green and blue [LONG](/qb64wiki/index.php/LONG "LONG") components intensity from 0 to 255 simultaneously, to generate a shade of gray.


  




## Description


* The value returned is always a 32-bit [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") color value, as is the [POINT](/qb64wiki/index.php/POINT "POINT") value.
* **Return variable types must be [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") or [LONG](/qb64wiki/index.php/LONG "LONG"), otherwise resulting color may lose the [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") value.**
* Parameter values outside of the 0 to 255 range are clipped.
* Returns [LONG](/qb64wiki/index.php/LONG "LONG") 32 bit hexadecimal values from **&H00000000** to **&HFFFFFFFF**.
* When [LONG](/qb64wiki/index.php/LONG "LONG") values are [PUT](/qb64wiki/index.php/PUT "PUT") to file, the ARGB values become BGRA. Use [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")([MKL$](/qb64wiki/index.php/MKL$ "MKL$")(*color32value~&*), 3) to place 3 colors.
* **NOTE: Default 32-bit backgrounds are clear black or \_RGB32(0, 0). Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque.**


  




## Availability


* Alternative syntaxes available with **version 1.3 and up**.


  




## Examples


*Example 1:* Converting the color port RGB intensity palette values 0 to 63 to 32 bit hexadecimal values.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [DIM](/qb64wiki/index.php/DIM "DIM") hex32$(15) [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") attribute = 1 [TO](/qb64wiki/index.php/TO "TO") 15   [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C7, attribute      'set color attribute to read   red = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values   grn = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4   blu = [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 4   hex32$(attribute) = "[&H](/qb64wiki/index.php/%26H "&H")" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(_RGB32(red, grn, blu))   'always returns the 32 bit value   [COLOR](/qb64wiki/index.php/COLOR "COLOR") attribute   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[COLOR](/qb64wiki/index.php/COLOR "COLOR")" + [STR$](/qb64wiki/index.php/STR$ "STR$")([_RGB](/qb64wiki/index.php/RGB "RGB")(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` COLOR 1 = &HFF0000A8 COLOR 2 = &HFF00A800 COLOR 3 = &HFF00A8A8 COLOR 4 = &HFFA80000 COLOR 5 = &HFFA800A8 COLOR 6 = &HFFA85400 COLOR 7 = &HFFA8A8A8 COLOR 8 = &HFF545454 COLOR 9 = &HFF5454FC COLOR 10 = &HFF54FC54 COLOR 11 = &HFF54FCFC COLOR 12 = &HFFFC5454 COLOR 13 = &HFFFC54FC COLOR 14 = &HFFFCFC54 COLOR 15 = &HFFFCFCFC  ``` |
| --- |


*Note:* This procedure also shows how the returns from [\_RGB](/qb64wiki/index.php/RGB "RGB") and \_RGB32 differ in a non-32 bit screen mode.
  

*Example 2:* Working with 32 bit colors.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  [CLS](/qb64wiki/index.php/CLS "CLS") , _RGB32(0, 0, 128) 'deep blue background  [LINE](/qb64wiki/index.php/LINE "LINE") (100, 100)-(540, 380), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0), BF ' a red box [LINE](/qb64wiki/index.php/LINE "LINE") (200, 200)-(440, 280), [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 255, 0), BF ' a green box   [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 'Just so we can see our pretty background before we print anything on it.   [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(255, 255, 255), 0 'White on NO BACKGROUND  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 10     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is just a whole bunch of happy nothing!  Happy World!!" [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT"): [PRINT](/qb64wiki/index.php/PRINT "PRINT"):  [COLOR](/qb64wiki/index.php/COLOR "COLOR") 0, _RGB32(0, 0, 0) 'And here, we're going with NO [COLOR](/qb64wiki/index.php/COLOR "COLOR") text, with a BLACK background. 'Notice how this doesn't change the color on the screen at all, where the text is, but does toss a black background to it.  [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , 15: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "NOTICE HOW OUR 0 [COLOR](/qb64wiki/index.php/COLOR "COLOR") WORKS?" [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , 15: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "NEAT, HUH?" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") SYSTEM  ``` |
| --- |


Code by Steve McNeill
  

*Example 3:* Comparing the output of the new \_RGB32 syntaxes (starting with version 1.3) and their equivalents in previous versions.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(400, 400, 32)  [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(255, 255, 255) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "White" [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(255) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "White, too, but with less typing" [PRINT](/qb64wiki/index.php/PRINT "PRINT")  [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(80, 80, 80) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Dark gray" [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(80) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Same gray, but with less typing" [PRINT](/qb64wiki/index.php/PRINT "PRINT")  [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(255, 255, 255, 120) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "White with alpha of 120 (out of 255)" [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(255, 120) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "White with alpha of 120 - but with less typing" [PRINT](/qb64wiki/index.php/PRINT "PRINT")  [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(255, 0, 255, 110) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Magenta, 110 alpha" [COLOR](/qb64wiki/index.php/COLOR "COLOR") _RGB32(255, 0, 255, 110) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Magenta too, 110 alpha - but with less typing"  ``` |
| --- |


  




## See also


* [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32"), [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"), [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")
* [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR")
* [HEX$ 32 Bit Values](/qb64wiki/index.php/HEX$_32_Bit_Values "HEX$ 32 Bit Values")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [Hexadecimal Color Values](http://www.w3schools.com/html/html_colornames.asp)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RGB32&oldid=8669>"




## Navigation menu








### Search





















