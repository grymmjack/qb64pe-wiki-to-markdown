


\_CLEARCOLOR - QB64 Phoenix Edition Wiki








# \_CLEARCOLOR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CLEARCOLOR statement sets a specific color to be treated as transparent when an image is later put (via [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")) onto another image.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_CLEARCOLOR {*color&*|\_NONE}[, *Dest\_Handle&*]
  




## Parameters


* In color modes using a palette, *color&* is the palette index of the new transparent color value or \_NONE designates no clear colors.
* If *color&* is not a valid palette index, an [illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will occur.
* In 32-bit color modes, *color&* is the [\_LONG](/qb64wiki/index.php/LONG "LONG") color value of the new transparent color.
* If *Dest\_Handle&* is omitted, the destination is assumed to be the current write page. Zero can designate the current program screen.


  




## Description


* If *Dest\_Handle&* is an invalid handle, then an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error is returned. Check for bad handle values of -1 first.
* In 32-bit color modes, it simply sets the Alpha to 0 for all pixels matching the specified color.
* In the second syntax, transparency is disabled for color modes using a palette.
* **Note:** [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") can affect any \_CLEARCOLOR alpha setting within the color range set.
* **NOTE: 32 bit [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") screen page backgrounds are transparent black or [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") 0. Use [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") or [CLS](/qb64wiki/index.php/CLS "CLS") for opaque.**


  




## Examples


*Example 1:* Using \_CLEARCOLOR to "mask" the background color of an image.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 img& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png") [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , img&, 0 'place actual image with background K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0) 'clear screen with red background _CLEARCOLOR [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255), img& [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , img&, 0 'place image without white background [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR_(function) "CLEARCOLOR (function)")(img&) 'displays closest clear color attribute [END](/qb64wiki/index.php/END "END")  ``` |
| --- |




---


*Example 2:* Using a \_CLEARCOLOR transparency with images created on a [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") page. Does not require an image file.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(512, 384, 32) ' screen uses handle value [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (50, 50), 50, [_RGB](/qb64wiki/index.php/RGB "RGB")(128, 0, 0) ' create a red ball image [PAINT](/qb64wiki/index.php/PAINT "PAINT") (50, 50), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 0, 0), [_RGB](/qb64wiki/index.php/RGB "RGB")(128, 0, 0) redball = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(101, 101, 32) ' create a new image page [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , 0, redball, (0, 0)-(101, 101) ' put screen page 0 image onto redball page _CLEARCOLOR [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 0), redball ' makes black become see-through [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 255) ' erase original ball and create a blue background [DO](/qb64wiki/index.php/DO "DO")     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") ([RND](/qb64wiki/index.php/RND "RND") * 512, [RND](/qb64wiki/index.php/RND "RND") * 384), redball     [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") 1 ' one second delay [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  ``` |
| --- |




---


*Example 3:* Fading an image with a \_CLEARCOLOR background using a new page image to prevent [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") changes.





| ``` mainscreen = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) ' Main Screen (viewable) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") mainscreen [_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") [_MIDDLE](/qb64wiki/index.php/MIDDLE "MIDDLE") Image1& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png") '<<<<<< any image with one background color to clear  [IF](/qb64wiki/index.php/IF "IF") Image1& < -1 [THEN](/qb64wiki/index.php/THEN "THEN") 'check loaded image handle value before using!     [_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") Image1&     clr~& = [POINT](/qb64wiki/index.php/POINT "POINT")(0, 0) 'get background color from image source     _CLEARCOLOR clr~&, Image1& 'clear background color of loaded image     NewImage1& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(Image1&), [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(Image1&), 32) 'new image page     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Image1&, NewImage1& 'put image without background color on new page     [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") Image1& 'free loaded image from memory [END IF](/qb64wiki/index.php/END_IF "END IF") [_DEST](/qb64wiki/index.php/DEST "DEST") mainscreen:  a& = 0: d = 1 [DO](/qb64wiki/index.php/DO "DO")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10 'regulate speed of fades     [CLS](/qb64wiki/index.php/CLS "CLS")     a& = a& + d     [IF](/qb64wiki/index.php/IF "IF") a& = 255 [THEN](/qb64wiki/index.php/THEN "THEN") d = -d 'reverse fade     [_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") a&, , NewImage1& 'sets alpha level of all colors to fade image page in/out     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 342), NewImage1&     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Alpha: "; a&     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") a& = 0 [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Note:* If the \_CLEARCOLOR image background was not put onto a separate page, [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") would display it also.
  




## See also


* [\_CLEARCOLOR (function)](/qb64wiki/index.php/CLEARCOLOR_(function) "CLEARCOLOR (function)")
* [\_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") (sets transparency level)
* [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA"), [\_ALPHA32](/qb64wiki/index.php/ALPHA32 "ALPHA32") (read functions)
* [Images](/qb64wiki/index.php/Images "Images"), [Creating Sprite Masks](/qb64wiki/index.php/Creating_Sprite_Masks "Creating Sprite Masks")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLEARCOLOR&oldid=8279>"




## Navigation menu








### Search





















