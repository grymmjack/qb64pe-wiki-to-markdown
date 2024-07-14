


PALETTE - QB64 Phoenix Edition Wiki








# PALETTE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The PALETTE statement can swap color settings, set colors to default or set the red, green and blue color components of palette colors.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


Screens 11, 12, 13, 256
PALETTE [*attribute%*, *red%* + (*green%* \* 256) + (*blue%* \* 65536)]
Screen 10
PALETTE [*existingAttribute%*, *newAttribute%* (value from 0 to 7)]
Screens 0 and 9
PALETTE [*existingAttribute%*, *newAttribute%* (value from 0 to 63)]
Screens 1, 2, 7, and 8
PALETTE [*existingAttribute%*, *newAttribute%* (value from 0 to 15)]
Screen 32
No Palette available as all 32-bit colors are available.
  




## Description


* *red%*, *green%* and *blue%* values can range from 0 to 63. Many color shades are possible in non-[DAC](/qb64wiki/index.php/DAC "DAC") color attributes. (Valid for screens 11, 12, 13, and 256 only.)
* If the *red%*, *green%* and *blue%* color intensity settings are all the same value the resulting color is a shade of grey. (Valid for screens 11, 12, 13, and 256 only.)
* A swap is often used with [DAC](/qb64wiki/index.php/DAC "DAC") color attributes that cannot change RGB settings. Only the RGB color settings are swapped from original *existingAttribute%* to *newAttribute%*. Screens 0 thru 9 support swaps.
* PALETTE without any value sets any changed RGB settings back to the default color settings, including [DAC](/qb64wiki/index.php/DAC "DAC") colors.
* [PALETTE USING](/qb64wiki/index.php/PALETTE_USING "PALETTE USING") can be used when color intensity values are stored in an [array](/qb64wiki/index.php/Arrays "Arrays").
* QB64 implements the [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR") statement to provide extended palette functionality.


### QBasic/QuickBASIC


* Screens 0, 7 and 9 ([DAC](/qb64wiki/index.php/DAC "DAC")) colors could not be changed using the first syntax, but the program could use [OUT](/qb64wiki/index.php/OUT "OUT") to change intensity settings of attributes 1 thru 5.


  




## Examples


*Example:* Displaying all 64 DAC color hues as backgrounds in SCREEN 9 using a PALETTE swap.





| ```   [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 9 ' background is default black   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 20, 33: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press any Key!"   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 0 [TO](/qb64wiki/index.php/TO "TO") 63    a$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) ' wait for a keypress    PALETTE 0, i   [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


*Note:* Other attributes (1 to 15) can also be swapped for DAC foreground colors.
  




## See also


* [\_PALETTECOLOR](/qb64wiki/index.php/PALETTECOLOR "PALETTECOLOR")
* [PALETTE USING](/qb64wiki/index.php/PALETTE_USING "PALETTE USING")
* [COLOR](/qb64wiki/index.php/COLOR "COLOR")
* [OUT](/qb64wiki/index.php/OUT "OUT"), [INP](/qb64wiki/index.php/INP "INP")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PALETTE&oldid=8587>"




## Navigation menu








### Search





















