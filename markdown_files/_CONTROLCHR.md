


\_CONTROLCHR - QB64 Phoenix Edition Wiki








# \_CONTROLCHR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CONTROLCHR statement can be used to turn OFF control character attributes and allow them to be printed.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_CONTROLCHR {OFF|ON}
  




## Description


* The [OFF](/qb64wiki/index.php/OFF "OFF") clause allows control characters 0 to 31 to be printed and not format printing as normal text characters.


For example: **PRINT CHR$(13)** 'will not move the cursor to the next line and **PRINT CHR$(9)** 'will not tab.
* The default [ON](/qb64wiki/index.php/ON "ON") statement allows [Control Characters](/qb64wiki/index.php/ASCII#Control_Characters "ASCII") to be used as control commands where some will not print or will format prints.
* **Note:** File prints may be affected also when using Carriage Return or Line Feed/Form Feed formatting.
* The QB64 IDE may allow Alt + number pad character entries, but they must be inside of [STRING](/qb64wiki/index.php/STRING "STRING") values. Otherwise the IDE may not recognize them.


  




## Examples


*Example:* Printing the 255 [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters in [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 with 32 colors.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") i [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE") [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 40, 25 [CLS](/qb64wiki/index.php/CLS "CLS") _CONTROLCHR [OFF](/qb64wiki/index.php/OFF "OFF") i = 0 [DO](/qb64wiki/index.php/DO "DO")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i);     i = i + 1     [IF](/qb64wiki/index.php/IF "IF") (i [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") &HF) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [LOOP WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") i [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 20 [DO](/qb64wiki/index.php/DO "DO")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") i [AND](/qb64wiki/index.php/AND "AND") &HF [OR](/qb64wiki/index.php/OR "OR") (i [AND](/qb64wiki/index.php/AND "AND") &H80) \ &H8, (i [AND](/qb64wiki/index.php/AND "AND") &H70) \ &H10     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(i);     i = i + 1     [IF](/qb64wiki/index.php/IF "IF") (i [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") &HF) = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1 + i \ &H10, 20 [LOOP WHILE](/qb64wiki/index.php/DO...LOOP "DO...LOOP") i [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1260)
* [\_CONTROLCHR (function)](/qb64wiki/index.php/CONTROLCHR_(function) "CONTROLCHR (function)")
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII")
* [Control Characters](/qb64wiki/index.php/ASCII#Control_Characters "ASCII")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONTROLCHR&oldid=8916>"




## Navigation menu








### Search





















