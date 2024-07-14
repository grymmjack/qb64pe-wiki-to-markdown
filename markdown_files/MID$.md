


MID$ - QB64 Phoenix Edition Wiki








# MID$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **MID$** statement substitutes one or more new characters for existing characters of a previously defined [STRING](/qb64wiki/index.php/STRING "STRING").


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


MID$(*baseString$*, *startPosition%*[, *bytes%*]) = *replacementString$*
  




## Parameters


* The *baseString$* variable must exist and be large enough to contain the *replacementString$*.
* *startPosition%* specifies the string character position to start the overwrite.
* *bytes%* or number of characters is optional. Excess byte lenghts are ignored.
* The *replacementString$* should be as long as the byte length reserved.
* The length of the original string is not changed in any case. If *replacementString$* is longer, it gets clipped.


  




## Examples


Example
Using [INSTR](/qb64wiki/index.php/INSTR "INSTR") to locate the string positions and a **MID$** statement to change the words.


| ```  text$ = "The cats and dogs were playing, even though dogs don't like cats."  PRINT text$  start% = 1          ' start cannot be 0 when used in the INSTR function!  [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")    position% = [INSTR](/qb64wiki/index.php/INSTR "INSTR")(start%, text$, "dog")    IF position% THEN            ' when position is a value greater than 0      MID$(text$, position%, 3) = "rat"   ' changes "dog" to "rat" when found      start% = position% + 1     ' advance one position to search rest of string    END IF  LOOP UNTIL position% = 0       ' no other matches found  PRINT text$  ``` |
| --- |




| ``` The cats and dogs were playing, even though dogs don't like cats. The cats and rats were playing, even though rats don't like cats.  ``` |
| --- |


  




## See also


* [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [ASC](/qb64wiki/index.php/ASC "ASC"), [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")
* [INSTR](/qb64wiki/index.php/INSTR "INSTR"), [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [STR$](/qb64wiki/index.php/STR$ "STR$"), [HEX$](/qb64wiki/index.php/HEX$ "HEX$"), [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps")
* [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKD$](/qb64wiki/index.php/MKD$ "MKD$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MID$&oldid=8152>"




## Navigation menu








### Search





















