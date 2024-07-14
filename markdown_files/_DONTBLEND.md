


\_DONTBLEND - QB64 Phoenix Edition Wiki








# \_DONTBLEND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DONTBLEND statement turns off 32 bit alpha blending for the current image or screen mode where [\_BLEND](/qb64wiki/index.php/BLEND "BLEND") is default.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_DONTBLEND [*imageHandle&*]
  




## Parameters


* If *imageHandle&* is omitted, it is assumed to be the current [\_DESTination](/qb64wiki/index.php/DEST "DEST") write page.


  




## Description


* If *imageHandle&* is not valid, an [Invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* \_DONTBLEND is faster than the default [\_BLEND](/qb64wiki/index.php/BLEND "BLEND"). **You may want to disable it**, unless you really need to use it in 32 bit.
* **32 bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") so that they are transparent when placed over other surfaces.**
* Use [CLS](/qb64wiki/index.php/CLS "CLS") to make a new surface background [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 255 or opaque.
* Both [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") and [\_DEST](/qb64wiki/index.php/DEST "DEST") must have [\_BLEND](/qb64wiki/index.php/BLEND "BLEND") enabled, or else colors will NOT blend.


  




## Examples


*Example 1:* Use \_DONTBLEND when you want the 32 bit screen surface to be opaque so that it covers up other backgrounds. [CLS](/qb64wiki/index.php/CLS "CLS") works too.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(1280, 720, 32) 'CLS _DONTBLEND '<<< comment out to see the difference  [LINE](/qb64wiki/index.php/LINE "LINE") (100, 100)-(500, 500), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(255, 255, 0), BF  b& = SaveBackground&  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "This is just test junk" [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hit any key and the text should disappear, leaving us our pretty yellow box." [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") RestoreBackground b&  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") SaveBackground&     SaveBackground& = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(0) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [SUB](/qb64wiki/index.php/SUB "SUB") RestoreBackground (Image [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Image, 0 [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




---


*Example 2:* Turning off blending to create transparency.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) alphaSprite& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(64, 64, 32)  _DONTBLEND alphaSprite& ' turn off alpha-blending  'Create a simple sprite with transparency [_DEST](/qb64wiki/index.php/DEST "DEST") alphaSprite& [FOR](/qb64wiki/index.php/FOR "FOR") y = 0 [TO](/qb64wiki/index.php/TO "TO") 63     [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 63         alpha = [SQR](/qb64wiki/index.php/SQR "SQR")((x - 32) ^ 2 + (y - 32) ^ 2) / 32         [IF](/qb64wiki/index.php/IF "IF") alpha < 0 [THEN](/qb64wiki/index.php/THEN "THEN") alpha = 0         alpha = (1 - alpha * alpha) 'parabolic curve         [PSET](/qb64wiki/index.php/PSET "PSET") (x, y), [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(255, 255, 255, alpha * 255)     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  'Make a simple background texture [_DEST](/qb64wiki/index.php/DEST "DEST") 0 [FOR](/qb64wiki/index.php/FOR "FOR") y = 1 [TO](/qb64wiki/index.php/TO "TO") 479     [FOR](/qb64wiki/index.php/FOR "FOR") x = 0 [TO](/qb64wiki/index.php/TO "TO") 639         [PSET](/qb64wiki/index.php/PSET "PSET") (x, y), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")(x [AND](/qb64wiki/index.php/AND "AND") 255, y [AND](/qb64wiki/index.php/AND "AND") 255, (x [XOR](/qb64wiki/index.php/XOR "XOR") y) [AND](/qb64wiki/index.php/AND "AND") 255)     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  'Store background so we can show moveable objects on it background& = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(0)  'Treat my alpha values as transparency [_BLEND](/qb64wiki/index.php/BLEND "BLEND") alphaSprite&  ph = 0 [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60     x = 320 - 250 * [COS](/qb64wiki/index.php/COS "COS")(ph) - ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(alphaSprite&) \ 2)     y = 240 - 150 * [COS](/qb64wiki/index.php/COS "COS")(ph * 1.3) - ([_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(alphaSprite&) \ 2)     ph = ph + 0.03     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , background&, 0     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (x, y), alphaSprite&, 0     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [LEN](/qb64wiki/index.php/LEN "LEN")([INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"))  ``` |
| --- |


Code by Zom-B
*Explanation:* To make the alpha image, turn alpha blending off. Otherwise PSET blends the pixel to instead of making the sprite transparent.


  




## See also


* [\_BLEND](/qb64wiki/index.php/BLEND "BLEND")
* [\_BLEND (function)](/qb64wiki/index.php/BLEND_(function) "BLEND (function)")
* [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DONTBLEND&oldid=8315>"




## Navigation menu








### Search





















