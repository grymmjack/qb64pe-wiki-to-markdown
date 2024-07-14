


MKI$ - QB64 Phoenix Edition Wiki








# MKI$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The MKI$ function encodes an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") numerical value into a 2-byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = MKI$(*integerVariableOrLiteral%*)
  




## Description


* *integerVariableOrLiteral%* is converted to two ASCII characters.
* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values can range from -32768 to 32767.
* MKI$ string values can be converted back to numerical INTEGER values using [CVI](/qb64wiki/index.php/CVI "CVI").
* The function takes up less byte space in a file than using the text numerical value when the value is over 2 digits.
* When a variable value is used with [PUT](/qb64wiki/index.php/PUT "PUT") a numerical value is converted automatically in [RANDOM](/qb64wiki/index.php/RANDOM "RANDOM") and [BINARY](/qb64wiki/index.php/BINARY "BINARY") files.


  




## Examples


*Example:* How MKI$ creates a two byte string integer value to save file space.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12    '_PRINTSTRING requires a graphic screen mode DO   [COLOR](/qb64wiki/index.php/COLOR "COLOR") 14: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 13, 20: [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter an Integer from 1 to 32767(0 quits): ", number%   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") number% < 1 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   [CLS](/qb64wiki/index.php/CLS "CLS")   A$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(number% [MOD](/qb64wiki/index.php/MOD "MOD") 256)   'first digit(0 to 255)   B$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(number% \ 256)     'second digit(0 to 127)    MKIvalue$ = A$ + B$   Q$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34)   strng$ = "[CHR$](/qb64wiki/index.php/CHR$ "CHR$")(" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(number% [MOD](/qb64wiki/index.php/MOD "MOD") 256)) + ") + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(" + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(number% \ 256)) + ")"   [COLOR](/qb64wiki/index.php/COLOR "COLOR") 11   [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (222, 252), [STR$](/qb64wiki/index.php/STR$ "STR$")(number%) + " = " + strng$   [_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") (252, 300), "MKI$ value = " + Q$ + MKIvalue$ + Q$ 'print ASCII characters [LOOP](/qb64wiki/index.php/LOOP "LOOP") [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Code by Ted Weissgerber
*Explanation:* INPUT in QB64 limits integer entries to 32767 maximum. MOD 256 finds the part of a value from 0 to 255 while the second value is the number of times that 256 can go into the value. [\_PRINTSTRING](/qb64wiki/index.php/PRINTSTRING "PRINTSTRING") can print all of the [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters.
  




## See also


* [MKD$](/qb64wiki/index.php/MKD$ "MKD$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$")
* [CVD](/qb64wiki/index.php/CVD "CVD"), [CVI](/qb64wiki/index.php/CVI "CVI"), [CVS](/qb64wiki/index.php/CVS "CVS"), [CVL](/qb64wiki/index.php/CVL "CVL")
* [\_MK$](/qb64wiki/index.php/MK$ "MK$"), [\_CV](/qb64wiki/index.php/CV "CV")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MKI$&oldid=7911>"




## Navigation menu








### Search





















