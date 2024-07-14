


CALL - QB64 Phoenix Edition Wiki








# CALL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
CALL sends code execution to a subroutine procedure in a program. In **QB64** the subroutine doesn't need to be declared.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Alternative syntax](#Alternative_syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


CALL *ProcedureName* (*parameter1*, *parameter2*,...)]
### Alternative syntax


*ProcedureName* *parameter1*, *parameter2*,...]
  




## Description


* CALL requires [SUB](/qb64wiki/index.php/SUB "SUB") program parameters to be enclosed in brackets (parenthesis).
* CALL is not required to call a subprocedure. Use the SUB-procedure name and list any parameters without parenthesis.
* Neither syntax can be used to call [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") linelabel sub procedures.
* To pass parameters by value, instead of by reference, enclose passed variables in parenthesis.


### QBasic/QuickBASIC


* PDS or QuickBASIC 7 up could use [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") to pass variables by values instead of reference.
* QuickBASIC 4.5 could use [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") only for procedures created in Assembly or another language.
* QBasic required [CALL ABSOLUTE](/qb64wiki/index.php/CALL_ABSOLUTE "CALL ABSOLUTE") only. It did not have to be DECLAREd.


  




## Examples


*Example:* How parameters are passed in two [SUB](/qb64wiki/index.php/SUB "SUB") calls, one with CALL using brackets and one without CALL or brackets:





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") a [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") 'value not shared with SUB [DIM](/qb64wiki/index.php/DIM "DIM") [SHARED](/qb64wiki/index.php/SHARED "SHARED") b [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") 'value shared with any SUB a = 1 b = 2 c = 3  CALL helloworld (a) 'a passed to c parameter with CALL helloworld a        'a passed to c parameter w/o CALL  [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") helloworld (c) 'SUB parameter variables are always inside of brackets in SUB code [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello World!" [PRINT](/qb64wiki/index.php/PRINT "PRINT") a,  b, c a = a + 1 'a is a SUB value of 0 when printed which may increase inside SUB only b = b + 1 'b is a shared value which can increase anywhere c = c + 1 'c is a SUB parameter value from a in calls which may increase inside SUB only [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Returns:*





| ``` Hello World!  0            2            1 Hello World!  0            3            1  ``` |
| --- |


*Explanation:* Variable ***a*** that is outside of the subroutine isn't [SHARED](/qb64wiki/index.php/SHARED "SHARED") so it will have no effect inside the subroutine, the variable *a* inside the subroutine is only valid inside the subroutine, and whatever value *a* has outside of it makes no difference within the subroutine.
The variable ***b*** on the other hand is [SHARED](/qb64wiki/index.php/SHARED "SHARED") with the subroutines and thus can be changed in the subroutine. The variable *a* is initiated with 0 as default when created, thus it will return 0 since it wasn't changed within the subroutine.
The variable ***c*** is the [SUB](/qb64wiki/index.php/SUB "SUB") parameter variable that passes values into the sub. Its value could be changed by the passed parameter value or inside of the subroutine. The un-shared ***c*** variable value outside of the sub is irrelevant within the subroutine.
  




## See also


* [SUB](/qb64wiki/index.php/SUB "SUB"), [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CALL&oldid=7719>"




## Navigation menu








### Search





















