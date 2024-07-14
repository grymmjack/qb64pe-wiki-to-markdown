


\_ALPHA32 - QB64 Phoenix Edition Wiki








# \_ALPHA32



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ALPHA32 function returns the alpha transparency level of a 32 bit color value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*alpha&* = \_ALPHA32(*color32~&*)
  




## Parameters


* *color32&* is the [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") 32 bit color value used to retrieve the alpha level.
	+ Color values that are set as a [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") always have an alpha level of 0 (transparent).
	+ [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") can set any alpha level from 0 (or fully transparent) to 255 (or opaque).
	+ Normal color values that are set by [\_RGB](/qb64wiki/index.php/RGB "RGB") or [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") always have an alpha level of 255 (opaque).


  




## Description


* In 4-bit (16 colors) or 8-bit (256 colors) palette screens the function will return 0.
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"), [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32") and \_ALPHA32 are all equivalent to [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") and [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") but they are highly optimized and only accept a 32-bit color (RGBA) value. Using these in your code (opposed to dividing then ANDing 32-bit color values) makes code easy to read.
* **NOTE: 32 bit [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page backgrounds are transparent black or [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 0. Use [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") or [CLS](/qb64wiki/index.php/CLS "CLS") for opaque!**


  




## Examples


*Example:* Finding the alpha transparency level in a 32 bit screen using an [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") color value.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  clr~& = [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(255, 0, 255, 192) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Color:"; clr~&  [COLOR](/qb64wiki/index.php/COLOR "COLOR") clr~& [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Alpha32:"; _ALPHA32(clr~&)  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` Color: 3237937407 Alpha32: 192  ``` |
| --- |


*Notes:* The color value is equivalent to [hexadecimal](/qb64wiki/index.php/%26H "&H") &HC0FF00FF where &HC0 equals 192. [\_RGB](/qb64wiki/index.php/RGB "RGB") alphas are always &HFF(255).
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1060)
* [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA"), [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA")
* [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") (set color with alpha)
* [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"). [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")
* [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR"), [\_CLEARCOLOR (function)](/qb64wiki/index.php/CLEARCOLOR_(function) "CLEARCOLOR (function)")
* [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ALPHA32&oldid=8873>"




## Navigation menu








### Search





















