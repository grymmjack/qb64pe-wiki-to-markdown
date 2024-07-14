


RIGHT$ - QB64 Phoenix Edition Wiki








# RIGHT$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **RIGHT$** function returns a set number of characters in a [STRING](/qb64wiki/index.php/STRING "STRING") variable starting from the end and counting backwards.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


**RIGHT$(***stringvalue$, numberofcharacters%***)**
  




## Parameters


* The *stringvalue$* can be any string of [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters as a [STRING](/qb64wiki/index.php/STRING "STRING") variable.
* The *numberofcharacters* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value determines the number of characters to return from the right end of the string.


  




## Description


* If the number of characters exceeds the string length([LEN](/qb64wiki/index.php/LEN "LEN")) the entire string is returned.
* RIGHT$ returns always start at the last character of the string, even if a space. [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$") can remove ending spaces.
* **Number of characters cannot be a negative value.**


  

*Example 1:* Getting the right portion of a string value such as a person's last name.





| ``` name$ = "Tom Williams"  Last$ = RIGHT$(name$, [LEN](/qb64wiki/index.php/LEN "LEN")(name$) - [INSTR](/qb64wiki/index.php/INSTR "INSTR")(name$, " ")) 'subtract space position from string length  [PRINT](/qb64wiki/index.php/PRINT "PRINT") Last$  ``` |
| --- |




| ``` Williams  ``` |
| --- |


  

*Example 2:* Adding the leading zero in single digit [HEX$](/qb64wiki/index.php/HEX$ "HEX$") values using RIGHT to take the right two hexadecimal string digits.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(640, 480, 32) '32 bit screen modes ONLY! red = 255 green = 0 blue = 128  Color32 red, green, blue [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Colored text"  [SUB](/qb64wiki/index.php/SUB "SUB") Color32 (R, G, B) R = R [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&H](/qb64wiki/index.php/%26H "&H")FF: G = G [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&H](/qb64wiki/index.php/%26H "&H")FF: B = B [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") [&H](/qb64wiki/index.php/%26H "&H")FF '    limit values to 0 to 255 hexadecimal$ = "[&H](/qb64wiki/index.php/%26H "&H")FF" + RIGHT$("0" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(R), 2) + RIGHT$("0" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(G), 2) + RIGHT$("0" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(B), 2) [PRINT](/qb64wiki/index.php/PRINT "PRINT") hexadecimal$ [COLOR](/qb64wiki/index.php/COLOR "COLOR") [VAL](/qb64wiki/index.php/VAL "VAL")(hexadecimal$) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




| ``` **&HFFFF0080** **Colored text** ``` |
| --- |


*Note:* When a single hexadecimal digit is returned the resulting value will need the leading zero added. Otherwise the hexa- decimal value created will have a byte missing from the value. EX: Color &HFF000000 is valid while &HFF000 is not.
  




## See also


* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$"), [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")
* [INSTR](/qb64wiki/index.php/INSTR "INSTR"), [HEX$](/qb64wiki/index.php/HEX$ "HEX$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RIGHT$&oldid=8163>"




## Navigation menu








### Search





















