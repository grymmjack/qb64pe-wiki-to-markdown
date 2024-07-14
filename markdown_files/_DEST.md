


\_DEST - QB64 Phoenix Edition Wiki








# \_DEST



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_DEST statement sets the current write image or page. All graphic and print changes will be done to this image.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_DEST *imageHandle&*
  




## Description


* *imageHandle&* is the handle of the image that will act as the current write page.
* **\_DEST 0** refers to the present program [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"). You can use 0 to refer to the present program [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN").
* \_DEST [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE") can set the destination to send information to a console window using [PRINT](/qb64wiki/index.php/PRINT "PRINT") or [INPUT](/qb64wiki/index.php/INPUT "INPUT").
* If *imageHandle&* is an invalid handle, an [invalid handle](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error occurs. Always check for valid handle values first (*imageHandle&* < -1).
* *Note:* Use [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE") when you need to read a page or image with [POINT](/qb64wiki/index.php/POINT "POINT"), [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") or the [SCREEN](/qb64wiki/index.php/SCREEN_(function) "SCREEN (function)") function.


  




## Examples


*Example 1:* Placing a center point and a circle using [\_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") to eliminate the background color black.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 'program screen can use 256 colors a& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(320, 200, 13) 'create 2 screen page handles a& and b& b& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(320, 200, 13) _DEST a& 'set destination image to handle a& [PSET](/qb64wiki/index.php/PSET "PSET") (100, 100), 15 'draw a dot on the current destination handle a& _DEST b& 'set destination image to handle b& [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (100, 100), 50, 15 'draw a circle on the current destination handle b& [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") 0 'make page b color 0 (black) transparent [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , b&, a& 'put circle on image b to image a& (a PSET dot) [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , a&, 0 'put what is on image a& to the screen (handle 0)  ``` |
| --- |




---


*Example 2:* Demonstrates how [printed](/qb64wiki/index.php/PRINT "PRINT") text can be stretched using [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") with \_DEST pages.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") a(10) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") [DIM](/qb64wiki/index.php/DIM "DIM") b [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  [REM](/qb64wiki/index.php/REM "REM") Sets up a newimage for B then sets the screen to that. b = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") b  [REM](/qb64wiki/index.php/REM "REM") Make pages 48 pixels tall. If the image is not at least that it wont work a(1) = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(240, 48, 32) a(2) = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(240, 48, 32) a(3) = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(98, 48, 32)  xa = 100 ya = 120 xm = 4 ym = 4  [REM](/qb64wiki/index.php/REM "REM") Some fun things for the bouncing text. st$(0) = "doo" st$(1) = "rey" st$(2) = "mee" st$(3) = "faa" st$(4) = "soo" st$(5) = "laa" st$(6) = "tee"  sta$(0) = "This is a demo" sta$(1) = "showing how to use" sta$(2) = "the _DEST command" sta$(3) = "with PRINT" sta$(4) = "and _PUTIMAGE"  [REM](/qb64wiki/index.php/REM "REM") prints to a(3) image then switches back to the default 0 _DEST a(3): f = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 6): [PRINT](/qb64wiki/index.php/PRINT "PRINT") st$(3): _DEST 0  [DO](/qb64wiki/index.php/DO "DO")     [REM](/qb64wiki/index.php/REM "REM") prints to a(1) and a(2) then switches bac to 0     _DEST a(1)     [CLS](/qb64wiki/index.php/CLS "CLS")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") sta(r)     _DEST a(2)     [CLS](/qb64wiki/index.php/CLS "CLS")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") sta(r + 1)     _DEST 0 'destination zero is the main program page      [REM](/qb64wiki/index.php/REM "REM") a loop to putimage the images in a(1) and a(2) in a way to make it look like its rolling     [FOR](/qb64wiki/index.php/FOR "FOR") yat = 150 [TO](/qb64wiki/index.php/TO "TO") 380 [STEP](/qb64wiki/index.php/STEP "STEP") 4         [CLS](/qb64wiki/index.php/CLS "CLS")         [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, yat)-(640, 380), a(1)         [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 150)-(640, yat), a(2)         [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") bounce         [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 20     [NEXT](/qb64wiki/index.php/NEXT "NEXT") yat      r = r + 1     [IF](/qb64wiki/index.php/IF "IF") r = 4 [THEN](/qb64wiki/index.php/THEN "THEN") r = 0 [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [END](/qb64wiki/index.php/END "END")  bounce: [IF](/qb64wiki/index.php/IF "IF") xa > 600 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") xa < 20 [THEN](/qb64wiki/index.php/THEN "THEN") xm = xm * -1: _DEST a(3): f = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 6): [CLS](/qb64wiki/index.php/CLS "CLS"): [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") st$(f): _DEST 0 [IF](/qb64wiki/index.php/IF "IF") ya > 400 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") ya < 20 [THEN](/qb64wiki/index.php/THEN "THEN") ym = ym * -1: _DEST a(3): f = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 7): [CLS](/qb64wiki/index.php/CLS "CLS"): [_CLEARCOLOR](/qb64wiki/index.php/CLEARCOLOR "CLEARCOLOR") 0: [PRINT](/qb64wiki/index.php/PRINT "PRINT") st$(f): _DEST 0 [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (xa, ya)-(xa + 150, ya + 80), a(3) xa = xa + xm ya = ya + ym [RETURN](/qb64wiki/index.php/RETURN "RETURN")  ``` |
| --- |


Adapted from code by CodeViper
  




## See also


* [\_DEST (function)](/qb64wiki/index.php/DEST_(function) "DEST (function)")
* [\_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE")
* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_CONSOLE](/qb64wiki/index.php/CONSOLE "CONSOLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DEST&oldid=8307>"




## Navigation menu








### Search





















