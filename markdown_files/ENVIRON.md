


ENVIRON - QB64 Phoenix Edition Wiki








# ENVIRON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ENVIRON statement is used to temporarily set or change an environmental string value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


ENVIRON *stringExpression$*
  




## Description


* The *stringExpression$* must include the environmental parameter ID and the setting:
	+ Using an **=** sign: ENVIRON "parameterID=setting"
	+ Using a space: ENVIRON "parameterID setting"
* If the parameter ID did not previously exist in the environmental string table, it is appended to the end of the table.
* If a parameter ID did exist, it is deleted and the new value is appended to end of the list.
* Any changes made at runtime are discarded when your program ends.


  




## See also


* [ENVIRON$](/qb64wiki/index.php/ENVIRON$ "ENVIRON$")
* [Windows Environment](/qb64wiki/index.php/Windows_Environment "Windows Environment")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ENVIRON&oldid=553>"




## Navigation menu








### Search





















