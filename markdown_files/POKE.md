


POKE - QB64 Phoenix Edition Wiki








# POKE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **POKE** statement sets the value of a specified memory address offset. **QB64 currently has limited access!**


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) 	+ [3.1 More Examples](#More_Examples) * [4 See also](#See_also) |
| --- |


## Syntax


POKE *segment\_offset*, *offset\_value*
  




## Description


* Writes a value to the *segment\_offset* address in memory.
* POKE can only be used to set a value from 0 to 255 (one byte).
* A segment should be defined using [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG"), if you don't define a segment QBasic's ordinary segment will be used.
* POKE sends byte values to memory areas. It does not directly access registers.
* Important [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") segments using [PEEK](/qb64wiki/index.php/PEEK "PEEK") and POKE include &HB800 (text segment) and &HA000 (graphics segment).
* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") should always be used to reset the default segment when access to other memory is no longer necessary.
* POKE is safer to use than [OUT](/qb64wiki/index.php/OUT "OUT") which could damage a PC register.
* **Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!**


**It is highly recommended that QB64's [\_MEM](/qb64wiki/index.php/MEM "MEM") memory system be used to avoid running out of memory.**
  




## Examples


*Example 1:* Turning keyboard Lock and Insert modes on and off.


| ```  DEF SEG = 0  oldsetting% = PEEK(1047)  POKE 1047,PEEK(1047) OR 16 ' ENABLES SCROLL LOCK  POKE 1047,PEEK(1047) OR 32 ' ENABLES NUMBER LOCK  POKE 1047,PEEK(1047) OR 64 ' ENABLES CAPS LOCK  POKE 1047,PEEK(1047) OR 128 ' ENABLES INSERT MODE  DEF SEG   ``` |
| --- |


*Note: Use [XOR](/qb64wiki/index.php/XOR "XOR") instead of [OR](/qb64wiki/index.php/OR "OR") above to alternate between on and off modes.*


| ```  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = 0  oldsetting% = [PEEK](/qb64wiki/index.php/PEEK "PEEK")(1047)  POKE 1047,PEEK(1047) AND 239 ' TURNS OFF SCROLL LOCK (239 = 255 - 16)  POKE 1047,PEEK(1047) AND 223 ' TURNS OFF NUMBER LOCK (223 = 255 - 32)  POKE 1047,PEEK(1047) AND 191 ' TURNS OFF CAPS LOCK (191 = 255 - 64)  POKE 1047,PEEK(1047) AND 127 ' TURNS OFF INSERT MODE (127 = 255 - 128)  [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


*Note: Using [AND](/qb64wiki/index.php/AND "AND") requires that the bit value is subtracted from 255 to turn off a bit.* The above examples won't work in NT.
**Warning: The keyboard lights may NOT change so it is a good idea to restore the original settings!**
  

*Example 2:* A small PEEK and POKE fractal program.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [&H](/qb64wiki/index.php/%26H "&H")A000     'set to read screen buffer [DO](/qb64wiki/index.php/DO "DO")     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") a& = 0 [TO](/qb64wiki/index.php/TO "TO") 65535         POKE a&, [PEEK](/qb64wiki/index.php/PEEK "PEEK")((a& * 2) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&H](/qb64wiki/index.php/%26H "&H")FFFF&) + 1     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 25 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")  ``` |
| --- |


  

*Example 3:* Highlighting a row of text in Screen 0





| ``` minX = 20: maxX = 60: minY = 10: maxY = 24 selection = 0 'the screen Y coordinate of the previously highlighted item [FOR](/qb64wiki/index.php/FOR "FOR") i% = 1 [TO](/qb64wiki/index.php/TO "TO") 25: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") i%, 40: [PRINT](/qb64wiki/index.php/PRINT "PRINT") i%;: [NEXT](/qb64wiki/index.php/NEXT "NEXT") [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 100   [IF](/qb64wiki/index.php/IF "IF") [_MOUSEINPUT](/qb64wiki/index.php/MOUSEINPUT "MOUSEINPUT") [THEN](/qb64wiki/index.php/THEN "THEN")     'Un-highlight any selected row     [IF](/qb64wiki/index.php/IF "IF") selection [THEN](/qb64wiki/index.php/THEN "THEN") selectRow selection, minX, maxX, 0     x = [CINT](/qb64wiki/index.php/CINT "CINT")([_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX"))     y = [CINT](/qb64wiki/index.php/CINT "CINT")([_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY"))     [IF](/qb64wiki/index.php/IF "IF") x >= minX [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") x <= maxX [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y >= minY [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") y <= maxY [THEN](/qb64wiki/index.php/THEN "THEN")       selection = y     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       selection = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     'Highlight any selected row     [IF](/qb64wiki/index.php/IF "IF") selection [THEN](/qb64wiki/index.php/THEN "THEN") SelectRow selection, minX, maxX, 2     [IF](/qb64wiki/index.php/IF "IF") [_MOUSEBUTTON](/qb64wiki/index.php/MOUSEBUTTON "MOUSEBUTTON")(1) [THEN](/qb64wiki/index.php/THEN "THEN") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") x, y, selection   [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""  [SUB](/qb64wiki/index.php/SUB "SUB") SelectRow (y, x1, x2, col) [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [&H](/qb64wiki/index.php/%26H "&H")B800 addr& = (x1 - 1 + (y - 1) * [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")) * 2 + 1 [FOR](/qb64wiki/index.php/FOR "FOR") x = x1 [TO](/qb64wiki/index.php/TO "TO") x2   oldCol = [PEEK](/qb64wiki/index.php/PEEK "PEEK")(addr&) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&B](/qb64wiki/index.php/%26B "&B")10001111   ' Mask foreground color and blink bit   POKE addr&, oldCol [OR](/qb64wiki/index.php/OR "OR") ((col [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&B](/qb64wiki/index.php/%26B "&B")111) * [&B](/qb64wiki/index.php/%26B "&B")10000) ' Apply background color   addr& = addr& + 2 [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


### More Examples


* [SelectScreen](/qb64wiki/index.php/SelectScreen "SelectScreen")


  




## See also


* [DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG"), [DEF SEG = 0](/qb64wiki/index.php/DEF_SEG_%3D_0 "DEF SEG = 0")
* [PEEK](/qb64wiki/index.php/PEEK "PEEK"), [OUT](/qb64wiki/index.php/OUT "OUT")
* [VARSEG](/qb64wiki/index.php/VARSEG "VARSEG"), [VARPTR](/qb64wiki/index.php/VARPTR "VARPTR")
* [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)"), [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT")
* [Scancodes](/qb64wiki/index.php/Scancodes "Scancodes"), [Screen Memory](/qb64wiki/index.php/Screen_Memory "Screen Memory")
* [PEEK and POKE Library](/qb64wiki/index.php/PEEK_and_POKE_Library "PEEK and POKE Library")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=POKE&oldid=7715>"




## Navigation menu








### Search





















