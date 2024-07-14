


OPTION \_EXPLICITARRAY - QB64 Phoenix Edition Wiki








# OPTION \_EXPLICITARRAY



From QB64 Phoenix Edition Wiki
(Redirected from [EXPLICITARRAY](/qb64wiki/index.php?title=EXPLICITARRAY&redirect=no "EXPLICITARRAY"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
OPTION \_EXPLICITARRAY instructs the compiler to require arrays to be properly dimensioned with [DIM](/qb64wiki/index.php/DIM "DIM") or [REDIM](/qb64wiki/index.php/REDIM "REDIM") before first use. However, it doesn't require regular variables to be declared.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 Errors](#Errors) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


OPTION \_EXPLICITARRAY
  




## Description


* Normally statements like x(2) = 3 will implicitly create an array x(). OPTION \_EXPLICITARRAY requires proper dimensioning for the array, helping to catch mistyped array and function names.
* Unlike [OPTION \_EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT"), simple variables can still be used without a declaration. Example: i = 1


### Errors


* If used, OPTION \_EXPLICITARRAY must be the very first statement in your program. No other statements can precede it (except for [$NOPREFIX](/qb64wiki/index.php/$NOPREFIX "$NOPREFIX") or comment lines started with an [apostrophe](/qb64wiki/index.php/Apostrophe "Apostrophe") or [REM](/qb64wiki/index.php/REM "REM")).
* Do not use OPTION \_EXPLICITARRAY in [$INCLUDEd](/qb64wiki/index.php/$INCLUDE "$INCLUDE") modules.


  




## Examples


*Example:* Avoiding simple typos with OPTION \_EXPLICITARRAY results shown in the QB64 IDE Status area.





| ``` OPTION _EXPLICITARRAY x = 1 'This is fine, it's not an array so not affected  [DIM](/qb64wiki/index.php/DIM "DIM") z(5) z(2) = 3 'All good here, we've explicitly DIMmed our array  y(2) = 3 'This now generates an error  ``` |
| --- |


*QB64 IDE Status will show:*
**Array 'y' (SINGLE) not defined on line 7**


  




## See also


* [OPTION \_EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [SHARED](/qb64wiki/index.php/SHARED "SHARED")
* [STATIC](/qb64wiki/index.php/STATIC "STATIC")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPTION_EXPLICITARRAY&oldid=7351>"




## Navigation menu








### Search





















