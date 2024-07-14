


READ - QB64 Phoenix Edition Wiki








# READ



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **READ** statement reads values from a [DATA](/qb64wiki/index.php/DATA "DATA") field and assigns them to one or a comma separated list of variables.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


READ value1$[, value2!, value3%, ...]
  




* READ statements assign variables to [DATA](/qb64wiki/index.php/DATA "DATA") statement values on a one-to-one basis sequentially.
* A single READ statement may access one or more [DATA](/qb64wiki/index.php/DATA "DATA") values. They are accessed in the order set.
* Several READ statements may access the same [DATA](/qb64wiki/index.php/DATA "DATA") statement block at the following sequential position.
* [DATA](/qb64wiki/index.php/DATA "DATA") can be READ using [STRING](/qb64wiki/index.php/STRING "STRING") or numerical [TYPE](/qb64wiki/index.php/TYPE "TYPE") variables singularly or in a comma separated list:


[STRING](/qb64wiki/index.php/STRING "STRING") READ variables can read quoted or unquoted text or numerical DATA values!
Numerical type READ variables can only read **unquoted** numerical DATA values!
**If they do not agree, a ["Syntax error"](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") may result when run reading string data as numerical values!**
* If the number of variables specified is fewer than the number of elements in the DATA statement(s), subsequent READ statements begin reading data at the next unread element. If there are no subsequent READ statements, the extra data is ignored.
* If variable reads exceed the number of elements in the DATA field(s), an ["Out of data" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur!
* Use the [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE") statement to reread DATA statements from the start, with or without a line label as required.
* [ACCESS](/qb64wiki/index.php/ACCESS "ACCESS") READ can be used in an [OPEN](/qb64wiki/index.php/OPEN "OPEN") statement to limit file access to read only, preserving file data.
* **WARNING! Do not place DATA fields after [SUB](/qb64wiki/index.php/SUB "SUB") or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures! QB64 will FAIL to compile properly!**


QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.
  

*Example 1:* Placing data into an array.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") A(10) AS [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") I = 1 [TO](/qb64wiki/index.php/TO "TO") 10    READ A(I) [NEXT](/qb64wiki/index.php/NEXT "NEXT") I [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") J = 1 [TO](/qb64wiki/index.php/TO "TO") 10    [PRINT](/qb64wiki/index.php/PRINT "PRINT") A(J); [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END](/qb64wiki/index.php/END "END")  [DATA](/qb64wiki/index.php/DATA "DATA") 3.08, 5.19, 3.12, 3.98, 4.24 [DATA](/qb64wiki/index.php/DATA "DATA") 5.08, 5.55, 4.00, 3.16, 3.37  ``` |
| --- |




| ```  3.08  5.19  3.12  3.98  4.24  5.08  5.55  4  3.16  3.37  ``` |
| --- |


*Explanation:* This program reads the values from the DATA statements into array A. After execution, the value of A(1) is 3.08, and so on. The DATA statements may be placed anywhere in the program; they may even be placed ahead of the READ statement.
  

*Example 2:* Reading three pieces of data at once.





| ```  PRINT " CITY ", " STATE  ", " ZIP"  PRINT [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(30, "-")  'divider    READ C$, S$, Z&  PRINT C$, S$, Z&   [DATA](/qb64wiki/index.php/DATA "DATA") "DENVER,", COLORADO, 80211  ``` |
| --- |




| ```   CITY        STATE       ZIP  ------------------------------  DENVER,     COLORADO     80211  ``` |
| --- |


*Note:* String DATA values do not require quotes unless they contain commas, end spaces or QBasic keywords.
  




## See also


* [DATA](/qb64wiki/index.php/DATA "DATA"), [RESTORE](/qb64wiki/index.php/RESTORE "RESTORE")
* [$EMBED](/qb64wiki/index.php/$EMBED "$EMBED"). [\_EMBEDDED$](/qb64wiki/index.php/EMBEDDED$ "EMBEDDED$")




---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=READ&oldid=8698>"




## Navigation menu








### Search





















