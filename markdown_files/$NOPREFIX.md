


$NOPREFIX - QB64 Phoenix Edition Wiki








# $NOPREFIX



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $NOPREFIX metacommand allows all QB64 functions and statements to be used without the leading underscore (\_).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 See also](#See_also) |
| --- |


## Syntax


$NOPREFIX
  




## Description


* QB64-specific keywords are by default prefixed with an underscore, in order to differentiate them from legacy keywords inherited from QBasic/QuickBASIC 4.5.
* The convention exists in order to allow older code to be loaded and compiled in QB64 without naming conflicts with existing variables or constants.
* If you are writing new code with QB64, and **not importing code** from QBasic/QuickBASIC 4.5 nor any 3rd party .bi/.bm style libraries, then $NOPREFIX allows you to reduce typing by not having to use underscores in modern keywords.


!!! WARNING !!!

* Do not use **$NOPREFIX** when working with old QBasic/QuickBASIC 4.5 code or when your program depends on 3rd party library code, otherwise you risk a lot of "Name already in use" syntax errors, as the old code or libraries may use variable, SUB or FUNCTION names which conflict with new QB64 keywords if they are not prefixed with an underscore.
* Once again, use **$NOPREFIX** only with new written QB64 code which is fully under your control without any 3rd party dependencies!

* **SUB \_GL** is an internal routine and must **always** be prefixed.
* When $NOPREFIX is used, QB64 keywords can be used both with or without the leading underscore, so that both [\_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") and [DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") are valid in the same program, for example.
* $NOPREFIX must be the first non-comment and non-whitespace line in a program.
	+ Since QB64 v2.0 (incl. all QB64-PE versions) $NOPREFIX can be placed anywhere in a program.


  




## Availability


* [![v1.4](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.4")

**v1.4**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## See also


* [Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$NOPREFIX&oldid=8497>"




## Navigation menu








### Search





















