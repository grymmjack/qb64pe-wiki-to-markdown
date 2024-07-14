


PEEK - QB64 Phoenix Edition Wiki








# PEEK



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **PEEK** function returns the value that is contained at a certain memory address offset. **QB64 currently has limited access!**


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 More Examples](#More_Examples) * [2 See also](#See_also) |
| --- |


## Syntax


variable = PEEK(*segment\_offset*)
  




* Reads the specified memory *segment\_offset* value.
* Use [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") before PEEK to specify which memory segment to work in.
* PEEK only reads the memory byte value. Not certain bits. (See [AND](/qb64wiki/index.php/AND "AND"))
* Important [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") segments using PEEK and [POKE](/qb64wiki/index.php/POKE "POKE") include &HB800 (text segment) and &HA000 (graphics segment).
* To return to Basic default segment use [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") without any arguments.
* **Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!**


**It is highly recommended that QB64's [\_MEM](/qb64wiki/index.php/MEM "MEM") memory system be used to avoid running out of memory.**
  

*Example:* Checking the 8 keyboard bit settings using a PEEK return value.





| ```  SCREEN 12  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = 0 ' BIOS area  oldvalue = PEEK(1047) ' IMPORTANT! save initial setting to reset later  DO: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100    port = PEEK(1047)    IF port > 0 THEN LOCATE 26, 19: COLOR 11:       PRINT "Turn ALL Locks off to see each key's bit value!"    END IF  COLOR 14:LOCATE 2, 25  PRINT "PEEK(1047) ="; port; "present keyboard port byte value"  LOCATE 5, 35  IF (port [AND](/qb64wiki/index.php/AND "AND") 1) = 1 THEN COLOR 10: PRINT "R SHIFT PRESSED  " ELSE COLOR 12: PRINT "R SHIFT RELEASED"  LOCATE 7, 35  IF (port AND 2) = 2 THEN COLOR 10: PRINT "L SHIFT PRESSED  " ELSE COLOR 12: PRINT "L SHIFT RELEASED"  LOCATE 9, 35  IF (port AND 4) = 4 THEN COLOR 10: PRINT "CTRL KEY PRESSED " ELSE COLOR 12: PRINT "CTRL KEY RELEASED"  LOCATE 11, 35  IF (port AND 8) = 8 THEN COLOR 10: PRINT "ALT KEY PRESSED " ELSE COLOR 12: PRINT "ALT KEY RELEASED"  LOCATE 13, 35  IF (port AND 16) = 16 THEN COLOR 10: PRINT "SCROLL LOCK ON " ELSE COLOR 12: PRINT "SCROLL LOCK OFF"  LOCATE 15, 35  IF (port AND 32) = 32 THEN COLOR 10: PRINT "NUMBER LOCK ON " ELSE COLOR 12: PRINT "NUMBER LOCK OFF"  LOCATE 17, 35  IF (port AND 64) = 64 THEN COLOR 10: PRINT "CAPS LOCK ON " ELSE COLOR 12: PRINT "CAPS LOCK OFF"  LOCATE 19, 35  IF (port AND 128) = 128 THEN COLOR 10: PRINT "INSERT MODE ON " ELSE COLOR 12: PRINT "INSERT MODE OFF"  COLOR 11: LOCATE 21, 20: PRINT "Press mode keys to change or [ESC] to quit!";  LOOP UNTIL [INP](/qb64wiki/index.php/INP "INP")(&H60) = 1 ' escape key exit  [POKE](/qb64wiki/index.php/POKE "POKE") 1047, oldvalue      ' IMPORTANT reset to original settings  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


**NOTE: Keyboard Port function key settings cannot be reset on NT machines!**
### More Examples


* [SelectScreen](/qb64wiki/index.php/SelectScreen "SelectScreen")


  




## See also


* [POKE](/qb64wiki/index.php/POKE "POKE"), [INP](/qb64wiki/index.php/INP "INP")
* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG"), [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")
* [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [DEF SEG = 0](/qb64wiki/index.php/DEF_SEG_%3D_0 "DEF SEG = 0"), [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes")
* [PEEK and POKE Library](/qb64wiki/index.php/PEEK_and_POKE_Library "PEEK and POKE Library")
* [Screen Memory](/qb64wiki/index.php/Screen_Memory "Screen Memory")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PEEK&oldid=7643>"




## Navigation menu








### Search





















