


$ERROR - QB64 Phoenix Edition Wiki








# $ERROR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **$ERROR** [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") triggers a compilation error.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


**$ERROR** *message*
  




## Description


* This metacommand does not require a comment *['](/qb64wiki/index.php/Apostrophe "Apostrophe")* or [REM](/qb64wiki/index.php/REM "REM") before it.
* *message* is any text. Quotation marks are not required.
* When QB64 tries to compile an **$ERROR** metacommand a compilation error is triggered and *message* is shown to the user. This is useful in [$IF](/qb64wiki/index.php/$IF "$IF") blocks.
* If there is a particular situation where you know your program will not work properly, you can prevent the user compiling and give them a helpful error message instead by checking for the condition with [$IF](/qb64wiki/index.php/$IF "$IF").
* An **$ERROR** directive not inside an conditional [$IF](/qb64wiki/index.php/$IF "$IF") (or [$ELSEIF](/qb64wiki/index.php/$ELSEIF "$ELSEIF")) block is useless because the program will **never** compile in that case.


  




## Examples




| ``` [$IF](/qb64wiki/index.php/$IF "$IF") VERSION < 2.1 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") WINDOWS = 0 [THEN](/qb64wiki/index.php/THEN "THEN")     $ERROR Requires Windows QB64 version 2.1 or above [$END IF](/qb64wiki/index.php/$END_IF "$END IF")   ``` |
| --- |


Output (IDE Status Area)
Compilation check failed: REQUIRES WINDOWS QB64 VERSION 2.1 OR ABOVE on line 2 (assuming your version of QB64 doesn't meet those requirements).
  




## See also


* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")
* [$IF](/qb64wiki/index.php/$IF "$IF")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$ERROR&oldid=8327>"




## Navigation menu








### Search





















