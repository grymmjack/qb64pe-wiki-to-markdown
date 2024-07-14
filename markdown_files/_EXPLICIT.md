


OPTION \_EXPLICIT - QB64 Phoenix Edition Wiki








# OPTION \_EXPLICIT



From QB64 Phoenix Edition Wiki
(Redirected from [EXPLICIT](/qb64wiki/index.php?title=EXPLICIT&redirect=no "EXPLICIT"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
OPTION \_EXPLICIT instructs the compiler to require variable declaration with [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM") or an equivalent statement.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Errors](#Errors) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


OPTION \_EXPLICIT
  




## Description


* With OPTION \_EXPLICIT you can avoid typos by having QB64 immediately warn in the **Status area** of new variables used without previous declaration.
* The use of OPTION \_EXPLICIT does also enforce the requirement to [DIM](/qb64wiki/index.php/DIM "DIM") or [REDIM](/qb64wiki/index.php/REDIM "REDIM") any arrays before first use, no extra [OPTION \_EXPLICITARRAY](/qb64wiki/index.php/OPTION_EXPLICITARRAY "OPTION EXPLICITARRAY") is needed.
* Enable OPTION \_EXPLICIT temporarily even if a program source file doesn't contain the directive by specifying the **-e** switch when compiling via command line (*qb64 -c file.bas -e*).


### Errors


* If used, OPTION \_EXPLICIT must be the very first statement in your program. No other statements can precede it (except for [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX") or comment lines started with an [apostrophe](/qb64wiki/index.php/Apostrophe "Apostrophe") or [REM](/qb64wiki/index.php/REM "REM")).
* Do not use OPTION \_EXPLICIT in [$INCLUDEd](/qb64wiki/index.php/$INCLUDE "$INCLUDE") modules.


  




## Examples


*Example:* Avoiding simple typos with OPTION \_EXPLICIT results shown in the QB64 IDE Status area.





| ``` OPTION _EXPLICIT  [DIM](/qb64wiki/index.php/DIM "DIM") myVariable [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")  myVariable = 5  [PRINT](/qb64wiki/index.php/PRINT "PRINT") myVariabe  ``` |
| --- |


*QB64 IDE Status will show:*
**Variable 'myVariabe' (SINGLE) not defined on line 4**


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1727)
* [OPTION \_EXPLICITARRAY](/qb64wiki/index.php/OPTION_EXPLICITARRAY "OPTION EXPLICITARRAY")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [STATIC](/qb64wiki/index.php/STATIC "STATIC")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPTION_EXPLICIT&oldid=8936>"




## Navigation menu








### Search





















