


\_BLEND - QB64 Phoenix Edition Wiki








# \_BLEND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_BLEND statement turns on 32 bit alpha blending for an image or screen mode and is on by default.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_BLEND [*imageHandle&*]
  




## Parameters


* *imageHandle&* refers to an image in memory. If not specified, the current destination page (See [\_DEST](/qb64wiki/index.php/DEST "DEST")) is affected.


  




## Description


* Alpha blending is on by default when loading a .PNG image to a 32-bit surface.
* Normally it is used to turn blending on after a previous [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") call.
* \_BLEND can only be used on 32-bit surfaces, otherwise it will produce the error [Illegal Function Call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes").
* **Note: [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") is faster than the default \_BLEND unless you really need to use it in 32 bit.**
* **32 bit screen surface backgrounds (black) have zero [\_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA") so that they are transparent when placed over other surfaces.**


  




## Examples


*Example:*





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32)  'CLS , _RGB(128, 128, 128) 'change background color for other results  [_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND")  bg& = [POINT](/qb64wiki/index.php/POINT "POINT")(0, 0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_RED](/qb64wiki/index.php/RED "RED")(bg&), [_GREEN](/qb64wiki/index.php/GREEN "GREEN")(bg&), [_BLUE](/qb64wiki/index.php/BLUE "BLUE")(bg&), [_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA")(bg&)  [LINE](/qb64wiki/index.php/LINE "LINE") (100, 100)-(200, 200), [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(255, 128, 0, 128), BF  [LINE](/qb64wiki/index.php/LINE "LINE") (440, 100)-(540, 200), [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(0, 0, 255, 64), BF  K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)  _BLEND  [LINE](/qb64wiki/index.php/LINE "LINE") (270, 300)-(370, 400), [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(255, 128, 0, 128), BF m& = [POINT](/qb64wiki/index.php/POINT "POINT")(303, 302) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_RED](/qb64wiki/index.php/RED "RED")(m&), [_GREEN](/qb64wiki/index.php/GREEN "GREEN")(m&), [_BLUE](/qb64wiki/index.php/BLUE "BLUE")(m&), [_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA")(m&) K$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1)  [LINE](/qb64wiki/index.php/LINE "LINE") (270, 300)-(370, 400), [_RGBA32](/qb64wiki/index.php/RGBA32 "RGBA32")(0, 0, 255, 64), BF m& = [POINT](/qb64wiki/index.php/POINT "POINT")(303, 302) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_RED](/qb64wiki/index.php/RED "RED")(m&), [_GREEN](/qb64wiki/index.php/GREEN "GREEN")(m&), [_BLUE](/qb64wiki/index.php/BLUE "BLUE")(m&), [_ALPHA](/qb64wiki/index.php/ALPHA "ALPHA")(m&)  ``` |
| --- |


  




## See also


* [\_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND"), [\_BLEND (function)](/qb64wiki/index.php/BLEND_(function) "BLEND (function)")
* [Images](/qb64wiki/index.php/Images "Images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BLEND&oldid=8270>"




## Navigation menu








### Search





















