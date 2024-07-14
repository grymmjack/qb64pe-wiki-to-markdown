


STATIC - QB64 Phoenix Edition Wiki








# STATIC



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The STATIC keyword is used in declaration statements to control where variables are stored.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


Variables
STATIC *variableName*[()] [[[AS *dataType*][, ...]
Subs & Functions
{[SUB](/qb64wiki/index.php/SUB "SUB")|[FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")} *procedureName* [(*parameterList*)] **STATIC**
Library function block
[DECLARE STATIC LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
## Description


* A STATIC list can be used in [SUB](/qb64wiki/index.php/SUB "SUB") and [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures to designate one or more variables to retain their values.
* Variables and arrays with static storage will retain their values in between procedure calls. The values may also be used recursively.


* *variableName* may include a type suffix or use [AS](/qb64wiki/index.php/AS "AS") to specify a type other than the default [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") type.
* Arrays with static storage are declared by specifying empty parenthesis following the array name. See [Arrays](/qb64wiki/index.php/Arrays "Arrays")

* STATIC can be used after the name of a [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") in the procedure to force all variables to retain their values.
* **Recursive procedures may be required to be STATIC to avoid a Stack Overflow! QB64 programs may just close!**
* [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC") defined program [arrays](/qb64wiki/index.php/Arrays "Arrays") cannot be [re-sized](/qb64wiki/index.php/REDIM "REDIM") or use [\_PRESERVE](/qb64wiki/index.php/PRESERVE "PRESERVE").


  




## Examples


*Example 1: Finding the binary bit settings from a 32 bit [LONG](/qb64wiki/index.php/LONG "LONG") register return using recursion.*





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a numerical value to see binary value: ", num& [PRINT](/qb64wiki/index.php/PRINT "PRINT") BinStr$(num&)  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") BinStr$ (n&) STATIC 'comment out STATIC to see what happens! [DIM](/qb64wiki/index.php/DIM "DIM") p%, s$ [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") 2 ^ p% > n& [THEN](/qb64wiki/index.php/THEN "THEN")   p% = 0 [ELSE](/qb64wiki/index.php/ELSE "ELSE")   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n& [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 2 ^ p% [THEN](/qb64wiki/index.php/THEN "THEN") s$ = "1" + s$ [ELSE](/qb64wiki/index.php/ELSE "ELSE") s$ = "0" + s$   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n& > 2 ^ p% [THEN](/qb64wiki/index.php/THEN "THEN")     p% = p% + 1     s$ = BinStr$(n&) 'recursive call to itself   [ELSE](/qb64wiki/index.php/ELSE "ELSE"): p% = 0   [END IF](/qb64wiki/index.php/END_IF "END IF") [END IF](/qb64wiki/index.php/END_IF "END IF") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") s$ = "" [THEN](/qb64wiki/index.php/THEN "THEN") BinStr$ = "0" [ELSE](/qb64wiki/index.php/ELSE "ELSE") BinStr$ = s$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Explanation:* The [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") above returns a [STRING](/qb64wiki/index.php/STRING "STRING") value representing the bits ON in an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value. The string can be printed to the screen to see what is happening in a port register. **STATIC** keeps the function from overloading the memory "Stack" and is normally REQUIRED when recursive calls are used in QBasic! **QB64 procedures will close without warning or error!**
  

*Example 2:* Using a static array to cache factorials, speeding up repeated calculations:





| ```   [PRINT](/qb64wiki/index.php/PRINT "PRINT") Factorial(0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") Factorial(5) [PRINT](/qb64wiki/index.php/PRINT "PRINT") Factorial(50  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Factorial# ( n [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") )     [CONST](/qb64wiki/index.php/CONST "CONST") maxNToCache = 50     STATIC resultCache() [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")     STATIC firstCall [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")      ' The lookup table is initially empty, so re-size it..     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") firstCall = 0 [THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")         firstCall = -1         [REDIM](/qb64wiki/index.php/REDIM "REDIM") resultCache(maxNToCache) [AS](/qb64wiki/index.php/AS "AS") [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")          ' ..and pre-calculate some factorials.         resultCache(0) = 1         resultCache(1) = 1         resultCache(2) = 2     [END IF](/qb64wiki/index.php/IF...THEN "IF...THEN")      ' See if we have the result cached. If so, we're done.     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n <= maxNToCache [THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") resultCache(n) <> 0 [THEN](/qb64wiki/index.php/IF...THEN "IF...THEN")             Factorial = resultCache(n)             [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")         [END IF](/qb64wiki/index.php/IF...THEN "IF...THEN")     [END IF](/qb64wiki/index.php/IF...THEN "IF...THEN")      ' If not, we use recursion to calculate the result, then cache it for later use:     resultCache(n) = [INT](/qb64wiki/index.php/INT "INT")(n) * Factorial([INT](/qb64wiki/index.php/INT "INT")(n) - 1)     Factorial = resultCache(n) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")   ``` |
| --- |




| ```  1  120  3.041409320171338D+64  ``` |
| --- |


  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [COMMON](/qb64wiki/index.php/COMMON "COMMON")
* [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")
* [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
* [TYPE](/qb64wiki/index.php/TYPE "TYPE"), [Arrays](/qb64wiki/index.php/Arrays "Arrays")
* [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC"), [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC")
* [Data types](/qb64wiki/index.php/Data_types "Data types")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STATIC&oldid=8367>"




## Navigation menu








### Search





















