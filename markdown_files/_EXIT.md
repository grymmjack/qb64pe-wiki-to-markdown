


EXIT - QB64 Phoenix Edition Wiki








# EXIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The EXIT statement is used to exit certain QBasic procedures.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 See also](#See_also) |
| --- |


## Syntax


EXIT {DO|WHILE|FOR|SUB|FUNCTION|SELECT|CASE}
  




## Description


* EXIT leaves any of the following procedures immediately.
	+ EXIT DO exits a [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP").
	+ EXIT WHILE exits a [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND") loop.
	+ EXIT FOR exits a [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") counter loop.
	+ EXIT SUB exits a [SUB](/qb64wiki/index.php/SUB "SUB") procedure before it ends. Use before any [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures using [RETURN](/qb64wiki/index.php/RETURN "RETURN").
	+ EXIT FUNCTION exits a [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedure before it ends. The value passed by the function's name should be defined.
	+ EXIT SELECT exits a [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") block.
	+ EXIT CASE does the same as EXIT SELECT unless when used in a **SELECT EVERYCASE** block; in such case, execution proceeds to the next CASE evaluation.
* EXIT statements normally use an [IF...THEN](/qb64wiki/index.php/IF...THEN "IF...THEN") statement to evaluate a program condition that would require the EXIT.
* To exit a program and allow the last program screen to be displayed with the message "Press any key to continue...", use [END](/qb64wiki/index.php/END "END").
* To exit the program immediately, use [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM").


  




## Availability


* **EXIT SELECT/CASE** available in:
	+ **QB64 v1.5 and up**
	+ **QB64-PE all versions**
* All other variants available in all versions of QB64


  




## See also


* [\_EXIT (function)](/qb64wiki/index.php/EXIT_(function) "EXIT (function)")
* [END](/qb64wiki/index.php/END "END"), [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")
* [STOP](/qb64wiki/index.php/STOP "STOP")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=EXIT&oldid=5549>"




## Navigation menu








### Search





















