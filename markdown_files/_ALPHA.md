


\_ALPHA - QB64 Phoenix Edition Wiki








# \_ALPHA



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ALPHA function returns the alpha channel transparency level of a color value used on a screen page or image.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result&* = \_ALPHA(*color~&* [, *imageHandle&*])
  




## Description


* If *imageHandle&* is omitted, it is assumed to be the current write page. Invalid handles will create [Illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") errors.
* [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") 32 bit [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") modes will always use an [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") *color~&* value.
	+ Color values that are set as a [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") always have an alpha level of 0 (transparent).
	+ [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") can set any alpha level from 0 (or fully transparent) to 255 (or opaque).
	+ Normal color values that are set by [\_RGB](/qb64wiki/index.php/RGB "RGB") or [\_RGB32](/qb64wiki/index.php/RGB32 "RGB32") always have an alpha level of 255(opaque).
* In 4 (16 color) or 8 (256 color) bit palette screens the function will always return 255.
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"), [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32") and [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32") are all equivalent to [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE") and \_ALPHA but they are highly optimized and only accept a 32-bit color (B8:G8:R8:A8). Using them (opposed to dividing then ANDing 32-bit color values manually) makes code easy to read.
* **NOTE: 32 bit [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page backgrounds are transparent black or \_ALPHA 0. Use [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") or [CLS](/qb64wiki/index.php/CLS "CLS") for opaque.**


  




## Examples


*Example 1:* Alpha transparency levels are always 255 in 4 or 8 bit screen modes.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13  clr~& = [_RGBA](/qb64wiki/index.php/RGBA "RGBA")(255, 0, 255, 192) 'returns closest palette color attribute [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Color:"; clr~&  [COLOR](/qb64wiki/index.php/COLOR "COLOR") clr~& [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Alpha:"; _ALPHA(clr~&)  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




| ``` Color 36 Alpha: 255  ``` |
| --- |


*Explanation:* [\_RGBA](/qb64wiki/index.php/RGBA "RGBA") cannot change the \_ALPHA level. [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32") would return 0 on any non-32 bit image or page.


---


*Example 2:* Finding the transparency of a 32 bit screen mode's background before and after [CLS](/qb64wiki/index.php/CLS "CLS").





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) BG& = [POINT](/qb64wiki/index.php/POINT "POINT")(1, 1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Alpha ="; _ALPHA(BG&); "Press a key to use CLS!" K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [CLS](/qb64wiki/index.php/CLS "CLS") BG& = [POINT](/qb64wiki/index.php/POINT "POINT")(1, 1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "CLS Alpha ="; _ALPHA(BG&)  ``` |
| --- |




| ``` CLS Alpha = 255    ``` |
| --- |


*Explanation:* Set the ALPHA value to 255 using [CLS](/qb64wiki/index.php/CLS "CLS") to make the background opaque when overlaying pages.
  




## See also


* [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32"), [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA")
* [\_RGBA](/qb64wiki/index.php/RGBA "RGBA"), [\_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32") (set color with alpha)
* [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR"), [\_CLEARCOLOR (function)](/qb64wiki/index.php/CLEARCOLOR_(function) "CLEARCOLOR (function)")
* [\_RED](/qb64wiki/index.php/RED "RED"), [\_GREEN](/qb64wiki/index.php/GREEN "GREEN"), [\_BLUE](/qb64wiki/index.php/BLUE "BLUE")
* [\_RED32](/qb64wiki/index.php/RED32 "RED32"), [\_GREEN32](/qb64wiki/index.php/GREEN32 "GREEN32"). [\_BLUE32](/qb64wiki/index.php/BLUE32 "BLUE32")
* [CLS](/qb64wiki/index.php/CLS "CLS"), [COLOR](/qb64wiki/index.php/COLOR "COLOR"), [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ALPHA&oldid=8256>"




## Navigation menu








### Search





















