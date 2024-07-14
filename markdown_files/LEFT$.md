


LEFT$ - QB64 Phoenix Edition Wiki








# LEFT$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LEFT$ string function returns a number of characters from the left of a [STRING](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


LEFT$(*stringValue$*, *numberOfCharacters%*)
  




## Parameters


* *stringValue$* can be any [STRING](/qb64wiki/index.php/STRING "STRING") literal or variable.
* *numberOfCharacters%* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") determines the number of characters to return from left of string.


  




## Description


* If the number of characters exceeds the string length the entire string is returned. Use [LEN](/qb64wiki/index.php/LEN "LEN") to determine a string's length.
* LEFT$ returns always start at the first character of the string, even if it's a space. [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$") can remove leading spaces.
* ***numberOfCharacters%* cannot be a negative value.**


  




## Examples


*Example 1:* Getting the left portion of a string value.





| ``` name$ = "Tom Williams"  First$ = LEFT$(name$, 3)  PRINT First$  ``` |
| --- |




| ``` Tom  ``` |
| --- |


  

*Example 2:* A replace function using LEFT$ and [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$") with [INSTR](/qb64wiki/index.php/INSTR "INSTR") to insert a different length word into an existing string.





| ``` text$ = "This is my sentence to change my words." [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$ oldword$ = "my" newword$ = "your"  x = Replace(text$, oldword$, newword$) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") x [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$; x  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Replace (text$, old$, new$) 'can also be used as a [SUB](/qb64wiki/index.php/SUB "SUB") without the count assignment [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   find = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(start + 1, text$, old$) 'find location of a word in text   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") find [THEN](/qb64wiki/index.php/THEN "THEN")     count = count + 1     first$ = LEFT$(text$, find - 1) 'text before word including spaces     last$ = [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")(text$, [LEN](/qb64wiki/index.php/LEN "LEN")(text$) - (find + [LEN](/qb64wiki/index.php/LEN "LEN")(old$) - 1)) 'text after word     text$ = first$ + new$ + last$   [END IF](/qb64wiki/index.php/END_IF "END IF")   start = find [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") find Replace = count 'function returns the number of replaced words. Comment out in SUB [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




| ``` This is my sentence to change my words. This is your sentence to change your words. ``` |
| --- |


*Note:* The [MID$](/qb64wiki/index.php/MID$ "MID$") statement can only substitute words or sections of the original string length. It cannot change the string length.
  




## See also


* [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$"), [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")
* [INSTR](/qb64wiki/index.php/INSTR "INSTR"), [LEN](/qb64wiki/index.php/LEN "LEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LEFT$&oldid=8144>"




## Navigation menu








### Search





















