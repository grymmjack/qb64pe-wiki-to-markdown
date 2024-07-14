


STR$ - QB64 Phoenix Edition Wiki








# STR$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **STR$** function returns the [STRING](/qb64wiki/index.php/STRING "STRING") representation of a numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


result$ = **STR$(***number***)**
  




## Parameters


* *number* is any numerical type value to convert.


  




## Description


* Returns any type number value with leading sign(space/minus) or decimal point when one exists in the numerical value.
* If *number* is positive, the [STRING](/qb64wiki/index.php/STRING "STRING") value returned will have a leading space character which can be removed using [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$").
* If *number* is negative, the minus sign will precede the number instead of a space which [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$") will not remove.
* Trimming a STR$ string number using [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$") is not required as [PRINT](/qb64wiki/index.php/PRINT "PRINT") creates the undocumented trailing number space.


  




## Examples




| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") STR$( 1.0 ) [PRINT](/qb64wiki/index.php/PRINT "PRINT") STR$( 2.3 ) [PRINT](/qb64wiki/index.php/PRINT "PRINT") STR$( -4.5 )  ``` |
| --- |




| ```  1  2.3 -4.5  ``` |
| --- |


  






| ``` a = 33 [PRINT](/qb64wiki/index.php/PRINT "PRINT") STR$(a) + "10" + "1" + "who" + STR$(a) + STR$(a) + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")(STR$(a))  ``` |
| --- |




| ```  33101who 33 3333  ``` |
| --- |


  




## See also


* [VAL](/qb64wiki/index.php/VAL "VAL"), [STRING](/qb64wiki/index.php/STRING "STRING")
* [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$"), [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$")
* [HEX$](/qb64wiki/index.php/HEX$ "HEX$"), [OCT$](/qb64wiki/index.php/OCT$ "OCT$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STR$&oldid=8168>"




## Navigation menu








### Search





















