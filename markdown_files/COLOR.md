


COLOR - QB64 Phoenix Edition Wiki








# COLOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The COLOR statement is used to change the foreground and background colors for printing text.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Screen Mode Attributes](#Screen_Mode_Attributes) 	+ [3.1 24/32-Bit colors using QB64](#24/32-Bit_colors_using_QB64) * [4 RGB Palette Intensities](#RGB_Palette_Intensities) 	+ [4.1 Read & write color port intensities with INP & OUT](#Read_&_write_color_port_intensities_with_INP_&_OUT) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


COLOR [*foreground&*][, *background&*]
  




## Description


* *background&* colors are available in all QB64 color SCREEN modes.
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mode 10 has only 3 white foreground attributes including flashing.
* To change the *background&* color only, use a comma and the desired color. Ex: COLOR , *background&*
* Graphic drawing statements like [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET"), [LINE](/qb64wiki/index.php/LINE "LINE"), etc, also use the colors set by the COLOR statement if no color is passed when they are called.
* The [$COLOR](/qb64wiki/index.php/$COLOR "$COLOR") metacommand adds named color constants for both text and 32-bit modes.


  




## Screen Mode Attributes


* **SCREEN 0** *background&* colors 0 to 7 can be changed each text character without affecting other text. Use [CLS](/qb64wiki/index.php/CLS "CLS") after a background color statement to create a fullscreen background color. 64 [DAC](/qb64wiki/index.php/DAC "DAC") hues with 16 high intensity blinking foreground (16 to 31) color attributes. See [\_BLINK](/qb64wiki/index.php/BLINK "BLINK").
	+ See example 7 below for more SCREEN 0 background colors.
* **SCREEN 1** has **4 background color attributes**: 0 = black, 1 = blue, 2 = green, 3 = grey. White foreground color only.
* **SCREEN 2** is **monochrome** with white forecolor and black background.
* **SCREEN 7** can use 16 ([DAC](/qb64wiki/index.php/DAC "DAC")) colors with background colors. RGB settings can be changed in colors 0 to 7 using [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR").
* **SCREEN 8** has 16 color attributes with 16 background colors.
* **SCREEN 9** can use up to 64 [DAC](/qb64wiki/index.php/DAC "DAC") color hues in 16 color attributes with background colors assigned to attribute 0 with a [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") swap. RGB settings can be changed in colors 0 to 5 and 7 using [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR").
* **SCREEN 10** has **only 4 color attributes** with black background. COLOR 0 = black, 1 = grey, 2 = flash white and 3 = bright white.
* **SCREEN 11** is **monochrome** with white forecolor and a black background.
* **SCREEN 12** can use 16 color attributes with a black background. 256K possible RGB color hues. Background colors can be used with QB64.
* **SCREEN 13** can use 256 color attributes with a black background. 256K possible RGB hues.
* [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE") swaps can be made in SCREEN 7 and 9 only. Those screens were [DAC](/qb64wiki/index.php/DAC "DAC") screen modes in QBasic.
* [\_DEST](/qb64wiki/index.php/DEST "DEST") can be used to set the destination page or image to color using **QB64**.
* [\_DEFAULTCOLOR](/qb64wiki/index.php/DEFAULTCOLOR "DEFAULTCOLOR") returns the current color being used on an image or screen page handle.


### 24/32-Bit colors using QB64


* Pixel color intensities for red, green, blue and alpha range from 0 to 255 when used with [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") and [RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32").
* Combined RGB function values returned are [LONG](/qb64wiki/index.php/LONG "LONG") values. **Blue intensity values may be cut off using [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variables.**
* [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") transparency values can range from 0 as transparent up to 255 which is fully opaque.
* [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") can also be used to set a color as transparent.
* Colors can be mixed by using [\_BLEND](/qb64wiki/index.php/BLEND "BLEND") (default) in 32-bit screen modes. [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") disables blending.
* **NOTE: Default 32-bit backgrounds are clear black or [\_RGBA](/qb64wiki/index.php/RGBA "RGBA")(0, 0, 0, 0). Use [CLS](/qb64wiki/index.php/CLS "CLS") to make the black opaque.**


([Return to Table of Contents](#toc))


  




## RGB Palette Intensities


RGB intensity values can be converted to hexadecimal values to create the [LONG](/qb64wiki/index.php/LONG "LONG") [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") value in non-32-bit screens:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 alpha$ = "FF" 'solid alpha colors only [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Attribute = Hex value      Red          Green         Blue " [PRINT](/qb64wiki/index.php/PRINT "PRINT") COLOR 7 [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") attribute = 1 [TO](/qb64wiki/index.php/TO "TO") 15   [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C7, attribute 'set color attribute to read   red$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")([INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 255 / 63) 'convert port setting to 32 bit values   grn$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")([INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 255 / 63)   blu$ = [HEX$](/qb64wiki/index.php/HEX$ "HEX$")([INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) * 255 / 63)   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(red$) = 1 [THEN](/qb64wiki/index.php/THEN "THEN") red$ = "0" + red$ '2 hex digits required   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(grn$) = 1 [THEN](/qb64wiki/index.php/THEN "THEN") grn$ = "0" + grn$ 'for low or zero hex values   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [LEN](/qb64wiki/index.php/LEN "LEN")(blu$) = 1 [THEN](/qb64wiki/index.php/THEN "THEN") blu$ = "0" + blu$   hex32$ = "[&H](/qb64wiki/index.php/%26H "&H")" + alpha$ + red$ + grn$ + blu$   [_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") attribute, [VAL](/qb64wiki/index.php/VAL "VAL")(hex32$) 'VAL converts hex string to a LONG 32 bit value   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") attribute [THEN](/qb64wiki/index.php/THEN "THEN") COLOR attribute 'exclude black color print   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "COLOR" + [STR$](/qb64wiki/index.php/STR$ "STR$")(attribute) + " = " + hex32$, red$, grn$, blu$ 'returns closest attribute [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` Attribute  Hex value      Red        Green       Blue  COLOR 1 = &HFF0000AA       00         00         AA COLOR 2 = &HFF00AA00       00         AA         00 COLOR 3 = &HFF00AAAA       00         AA         AA COLOR 4 = &HFFAA0000       AA         00         00 COLOR 5 = &HFFAA00AA       AA         00         AA COLOR 6 = &HFFAA5500       AA         55         00 COLOR 7 = &HFFAAAAAA       AA         AA         AA COLOR 8 = &HFF555555       55         55         55 COLOR 9 = &HFF5555FF       55         55         FF COLOR 10 = &HFF55FF55      55         FF         55 COLOR 11 = &HFF55FFFF      55         FF         FF COLOR 12 = &HFFFF5555      FF         55         55 COLOR 13 = &HFFFF55FF      FF         55         FF COLOR 14 = &HFFFFFF55      FF         FF         55 COLOR 15 = &HFFFFFFFF      FF         FF         FF  ``` |
| --- |


*Explanation:* The DAC intensity values are multiplied by (255 / 63) to get the [\_RGB](/qb64wiki/index.php/RGB "RGB") intensity values as [hexadecimal](/qb64wiki/index.php/HEX$ "HEX$") values. The individual 2 digit [HEX$](/qb64wiki/index.php/HEX$ "HEX$") intensity values can be added to "&HFF" to make up the 32-bit hexadecimal string value necessary for [VAL](/qb64wiki/index.php/VAL "VAL") to return to [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR"). The statement is only included in the example to show how that can be done with any 32-bit color value.
### Read & write color port intensities with [INP](/qb64wiki/index.php/INP "INP") & [OUT](/qb64wiki/index.php/OUT "OUT")


* Legacy code may use [INP](/qb64wiki/index.php/INP "INP") and [OUT](/qb64wiki/index.php/OUT "OUT") to read or set color port intensities. **QB64** emulates VGA memory to maintain compatibility.
* The same can be achieved using [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") (**recommended practice**).


**OUT &H3C7, attribute** 'Set port to read RGB settings with:
**color\_intensity = INP(&H3C9)** 'reads present intensity setting
**OUT &H3C8, attribute** 'Set port to write RGB settings with:
**OUT &H3C9, color\_intensity** 'writes new intensity setting
* After every 3 reads or writes, changes to next higher color attribute. Loops can be used to set more than one attribute's intensities.
* Color port setting of red, green and blue intensities can be done in ascending order.
* Color port attribute intensity values range from 0 to 63 (1/4 of the 32-bit values) in QBasic's legacy 4 and 8 bit screen modes.


([Return to Table of Contents](#toc))


  




## Examples


*Example 1:* Reading the default RGB color settings of color attribute 15.





| ```  [OUT](/qb64wiki/index.php/OUT "OUT") &H3C7, 15  red% = [INP](/qb64wiki/index.php/INP "INP")(&H3C9)  green% = [INP](/qb64wiki/index.php/INP "INP")(&H3C9)  blue% = [INP](/qb64wiki/index.php/INP "INP")(&H3C9)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") red%, green%, blue%  ``` |
| --- |




| ```  63       63       63  ``` |
| --- |


  

*Example 2:* Changing the color settings of attribute 0 (the background) to blue in [SCREENs](/qb64wiki/index.php/SCREEN "SCREEN") 12 or 13.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C8, 0          'set color port attribute to write [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 0          'red intensity [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 0          'green intensity [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C9, 42         'blue intensity  [OUT](/qb64wiki/index.php/OUT "OUT") [&H](/qb64wiki/index.php/%26H "&H")3C7, 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9); [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9); [INP](/qb64wiki/index.php/INP "INP")([&H](/qb64wiki/index.php/%26H "&H")3C9) [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ```  0  0  42 ``` |
| --- |


  

*Example 3:* Printing in fullscreen SCREEN 0 mode with a color background under the text only.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0: [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") ' used for fullscreen instead of window COLOR 14, 6: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 4, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello!"  ``` |
| --- |




| ```        Hello!  ``` |
| --- |


  

*Example 4:* Using [CLS](/qb64wiki/index.php/CLS "CLS") after setting the background color in SCREEN 0 to make the color cover the entire screen.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0: [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") COLOR , 7: [CLS](/qb64wiki/index.php/CLS "CLS") COLOR 9: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello"  ``` |
| --- |




| ``` Hello  ``` |
| --- |


  

*Example 5:* Using a different foreground color for each letter:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 COLOR 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "H"; COLOR 3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "E"; COLOR 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "L"; COLOR 5: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "L"; COLOR 6: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "O" COLOR 9: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "W"; COLOR 11: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "O"; COLOR 12: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "R"; COLOR 13: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "L"; COLOR 14: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "D"  ``` |
| --- |




| ``` HELLO WORLD  ``` |
| --- |


  




## See also


* [$COLOR](/qb64wiki/index.php/$COLOR "$COLOR") (metacommand)
* [\_RGB](/qb64wiki/index.php/RGB "RGB"), [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32"), [RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32").
* [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"), [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")
* [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA"), [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32"), [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR")
* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [POINT](/qb64wiki/index.php/POINT "POINT"), [SCREEN (function)](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)")
* [OUT](/qb64wiki/index.php/OUT "OUT"), [INP](/qb64wiki/index.php/INP "INP"), [PALETTE](/qb64wiki/index.php/PALETTE "PALETTE")
* [\_BLINK](/qb64wiki/index.php/BLINK "BLINK")
* [\_DEFAULTCOLOR](/qb64wiki/index.php/DEFAULTCOLOR "DEFAULTCOLOR")
* [\_BACKGROUNDCOLOR](/qb64wiki/index.php/BACKGROUNDCOLOR "BACKGROUNDCOLOR")
* [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR")
* [Color Dialog Box](/qb64wiki/index.php/Windows_Libraries#Color_Dialog_Box "Windows Libraries")
* [$COLOR:0 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color0.html)
* [$COLOR:32 Name Table](https://qb64phoenix.com/qb64wiki/resources/Color32.html)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=COLOR&oldid=8973>"




## Navigation menu








### Search





















