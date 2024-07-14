


\_HIDE - QB64 Phoenix Edition Wiki








# \_HIDE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_HIDE action is used to hide the console window opened by a [SHELL](/qb64wiki/index.php/SHELL "SHELL") statement.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[SHELL](/qb64wiki/index.php/SHELL "SHELL") [**\_HIDE**] *StringCommandLine$*
  




## Description


* Allows any command line window to be hidden from view without affecting the program.
* \_HIDE must be used when sending ("piping") screen information to a file.
* **Note:** Some commands may not work without adding CMD /C to the start of the command line.


  




## Examples


*Example:* Subprogram that displays long and short filenames using the DIR /X option in SCREEN 12:





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 LFN [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") LFN     [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")([ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")("OS")) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB") ' /X not available Win 9X and ME     [SHELL](/qb64wiki/index.php/SHELL "SHELL") _HIDE "cmd /c dir /x > DOS-DATA.INF" ' load display data to a file     [OPEN](/qb64wiki/index.php/OPEN "OPEN") "DOS-DATA.INF" [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [INPUT](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #1     [IF](/qb64wiki/index.php/IF "IF") [LOF](/qb64wiki/index.php/LOF "LOF")(1) [THEN](/qb64wiki/index.php/THEN "THEN")         Header$ = [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(10) + "Short" + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(16) + "Long" + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(20) + "Last Modified"         tmp$ = "\   \  \          \      &" ' print using template format         [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") Header$         [DO UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [EOF](/qb64wiki/index.php/EOF "EOF")(1)             [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #1, line$             [IF](/qb64wiki/index.php/IF "IF") [LEN](/qb64wiki/index.php/LEN "LEN")(line$) [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 1, 1) <> [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1) [THEN](/qb64wiki/index.php/THEN "THEN") ' ignore other file data                 cnt% = cnt% + 1                 last$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 1, 17): DIR$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 23, 3)                 [IF](/qb64wiki/index.php/IF "IF") [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 37, 1) <> [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1) [THEN](/qb64wiki/index.php/THEN "THEN") ' found line with short and long name                     SHFN$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 37, [INSTR](/qb64wiki/index.php/INSTR "INSTR")(37, line$, [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1)) - 1)                     LGFN$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 50)                 [ELSE](/qb64wiki/index.php/ELSE "ELSE"): SHFN$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(line$, 50): LGFN$ = "" ' found short name only                 [END IF](/qb64wiki/index.php/END_IF "END IF")                 [IF](/qb64wiki/index.php/IF "IF") cnt% [MOD](/qb64wiki/index.php/MOD "MOD") 24 = 0 [THEN](/qb64wiki/index.php/THEN "THEN") ' pause every 24 files                     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 28, 27: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press a key for more files!"                     [DO](/qb64wiki/index.php/DO "DO"): [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30: [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> ""                     [CLS](/qb64wiki/index.php/CLS "CLS"): [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") Header$                 [END IF](/qb64wiki/index.php/END_IF "END IF")                 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") (cnt% [MOD](/qb64wiki/index.php/MOD "MOD") 24) + 3, 4                 [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") tmp$; DIR$; SHFN$; LGFN$                 [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") (cnt% [MOD](/qb64wiki/index.php/MOD "MOD") 24) + 3, 58: [PRINT](/qb64wiki/index.php/PRINT "PRINT") last$             [END IF](/qb64wiki/index.php/END_IF "END IF")         [LOOP](/qb64wiki/index.php/LOOP "LOOP")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 10: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN") + 1, 27: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Total folders and files ="; cnt%     [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #1 [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Explanation:* The above routine can also be used to place the file name info into string arrays by using the count variable cnt% to determine the index. Long file names are normally returned by **QB64**. To keep older QBasic programs compatible, you may want to only use the short names when displaying the files on the screen.


  




## See also


* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [\_DONTWAIT](/qb64wiki/index.php/DONTWAIT "DONTWAIT")
* [FILELIST$ (function)](/qb64wiki/index.php/FILELIST$_(function) "FILELIST$ (function)") ([FILES](/qb64wiki/index.php/FILES "FILES") function, member-contributed)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=HIDE&oldid=8349>"




## Navigation menu








### Search





















