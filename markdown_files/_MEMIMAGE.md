


\_MEMIMAGE - QB64 Phoenix Edition Wiki








# \_MEMIMAGE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MEMIMAGE function returns a [\_MEM](/qb64wiki/index.php/MEM "MEM") value referring to an image's memory using a designated image handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*imageBlock* = \_MEMIMAGE[(*imageHandle&*)]
  




## Parameters


* The *imageBlock* [\_MEM](/qb64wiki/index.php/MEM "MEM") type variable holds the read-only elements .OFFSET, .SIZE, .TYPE and .ELEMENTSIZE.
* If the optional *imageHandle&* isn't passed, it is assumed to be the current [\_DESTination](/qb64wiki/index.php/DEST "DEST") program screen image.


  




## Description


* Use the function to place images into memory access blocks for faster data access.
* All values created by this function must be freed using [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") with a valid [\_MEM](/qb64wiki/index.php/MEM "MEM") variable.
* Image handle values and the memory used must still be freed using [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") when no longer required.


  




## Examples


*Example 1:* Darkening an image using memory with [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):OFF for greater speed. Use any 24 bit image file name on the second code line.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(1024, 768, 32) i& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("turtle.jpg") '<<<<<<<<<<<<< use any 24 bit image file  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") n! = 1 [TO](/qb64wiki/index.php/TO "TO") 0.01 [STEP](/qb64wiki/index.php/STEP "STEP") -0.01     i2& = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(i&)     DarkenImage i2&, n!     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0), i2&     [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") i2&     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [SUB](/qb64wiki/index.php/SUB "SUB") DarkenImage (Image [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Value_From_0_To_1 [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") Value_From_0_To_1 <= 0 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") Value_From_0_To_1 >= 1 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") [_PIXELSIZE](/qb64wiki/index.php/PIXELSIZE "PIXELSIZE")(Image) <> 4 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB") [DIM](/qb64wiki/index.php/DIM "DIM") Buffer [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM"): Buffer = _MEMIMAGE(Image) 'Get a memory reference to our image [DIM](/qb64wiki/index.php/DIM "DIM") Frac_Value [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): Frac_Value = Value_From_0_To_1 * 65536 'Used to avoid slow floating point calculations [DIM](/qb64wiki/index.php/DIM "DIM") O [AS](/qb64wiki/index.php/AS "AS") [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET"), O_Last [AS](/qb64wiki/index.php/AS "AS") [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET") O = Buffer.OFFSET 'We start at this offset O_Last = Buffer.OFFSET + [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(Image) * [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(Image) * 4 'We stop when we get to this offset 'use on error free code ONLY! [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):OFF DO     [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") Buffer, O, [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(Buffer, O, [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")) * Frac_Value \ 65536 [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")     [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") Buffer, O + 1, [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(Buffer, O + 1, [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")) * Frac_Value \ 65536 [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")     [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") Buffer, O + 2, [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(Buffer, O + 2, [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")) * Frac_Value \ 65536 [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")     O = O + 4 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") O = O_Last 'turn checking back on when done! [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING"):ON [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") Buffer [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Galleon
*Explanation:* The second value passed to DarkenImage is a value from 0.0 to 1.0 where 0.0 is full darkness and 1 is none.
  

*Example 2:* Reading information stored in an image with \_MEMIMAGE to print [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") text characters to the screen.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [_FULLSCREEN](/qb64wiki/index.php/FULLSCREEN "FULLSCREEN") [PSET](/qb64wiki/index.php/PSET "PSET") (0, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("H") [PSET](/qb64wiki/index.php/PSET "PSET") (1, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("E") [PSET](/qb64wiki/index.php/PSET "PSET") (2, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("L") [PSET](/qb64wiki/index.php/PSET "PSET") (3, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("L") [PSET](/qb64wiki/index.php/PSET "PSET") (4, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("O") [PSET](/qb64wiki/index.php/PSET "PSET") (5, 0), 32 [PSET](/qb64wiki/index.php/PSET "PSET") (6, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("W") [PSET](/qb64wiki/index.php/PSET "PSET") (7, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("O") [PSET](/qb64wiki/index.php/PSET "PSET") (8, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("R") [PSET](/qb64wiki/index.php/PSET "PSET") (9, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("L") [PSET](/qb64wiki/index.php/PSET "PSET") (10, 0), [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)")("D") [DIM](/qb64wiki/index.php/DIM "DIM") m [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM") m = _MEMIMAGE x1$ = [_MEMGET](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")(m, m.OFFSET, [STRING](/qb64wiki/index.php/STRING "STRING") * 11) 'convert numbers to ASCII text characters [_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") m 'free memory when done [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LEN](/qb64wiki/index.php/LEN "LEN")(x1$) 'prints 11 as byte length [PRINT](/qb64wiki/index.php/PRINT "PRINT") x1$ 'prints HELLO WORLD [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Notes:* The colors in the upper left corner are the text data used. An image could hold a hidden text message this way.
  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM")
* [\_MEMNEW](/qb64wiki/index.php/MEMNEW "MEMNEW")
* [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")
* [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MEMIMAGE&oldid=8714>"




## Navigation menu








### Search





















