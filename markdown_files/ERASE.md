


ERASE - QB64 Phoenix Edition Wiki








# ERASE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The ERASE statement is used to clear all data from an array. [$STATIC](/qb64wiki/index.php/$STATIC "$STATIC") [array](/qb64wiki/index.php/Arrays "Arrays") dimensions are not affected.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


ERASE *arrayName* [, *arrayName2*...]
  




## Description


* All string array elements become null strings ("") and all numerical array elements become 0.
* Multiple arrays can be erased using commas between the array names.
* [Dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") arrays must be [REDIMensioned](/qb64wiki/index.php/REDIM "REDIM") if they are referenced after erased.
* Dimension subprocedure arrays as [STATIC](/qb64wiki/index.php/STATIC "STATIC") to use ERASE and not have to REDIM.
* You do not have to include array brackets in an ERASE call.


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1243)
* [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM")
* [CLEAR](/qb64wiki/index.php/CLEAR "CLEAR")
* [STATIC](/qb64wiki/index.php/STATIC "STATIC")
* [$DYNAMIC](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC")
* [Arrays](/qb64wiki/index.php/Arrays "Arrays")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ERASE&oldid=8937>"




## Navigation menu








### Search





















