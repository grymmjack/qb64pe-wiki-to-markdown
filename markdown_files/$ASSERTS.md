


$ASSERTS - QB64 Phoenix Edition Wiki








# $ASSERTS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **$ASSERTS** [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") enables debug tests with the [\_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") macro.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


**$ASSERTS**
**$ASSERTS:CONSOLE**
  




## Description


* This metacommand does not require a comment *['](/qb64wiki/index.php/Apostrophe "Apostrophe")* or [REM](/qb64wiki/index.php/REM "REM") before it. There is no space between the metacommand name, the colon and the CONSOLE parameter.
* If this metacommand is used in a program and any of the set [\_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") checkpoints will fail, then the program will stop with an **\_ASSERT failed** error.
* Detailed error messages passed to the [\_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") statement will be displayed in the console window, but only if **$ASSERTS:CONSOLE** is used.


Note
This metacommand is the main switch to enable debug tests during development. Later just remove this metacommand to compile the program without debugging code, all the [\_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") statements may remain in the code for later debugging sessions, they are simply ignored without this metacommand.
  




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


  




## Examples


Example
Adding test checks for parameter inputs in a function.


| ``` $ASSERTS:CONSOLE  [DO](/qb64wiki/index.php/DO "DO")     a = [INT](/qb64wiki/index.php/INT "INT")([RND](/qb64wiki/index.php/RND "RND") * 10)     b$ = myFunc$(a)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") a, , b$     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 3 [LOOP UNTIL](/qb64wiki/index.php/DO...LOOP "DO...LOOP") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") myFunc$ (value [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"))     [_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") value > 0, "Value cannot be zero"     [_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT") value <= 10, "Value cannot exceed 10"      [IF](/qb64wiki/index.php/IF "IF") value > 1 [THEN](/qb64wiki/index.php/THEN "THEN") plural$ = "s"     myFunc$ = [STRING$](/qb64wiki/index.php/STRING$ "STRING$")(value, "*") + [STR$](/qb64wiki/index.php/STR$ "STR$")(value) + " star" + plural$ + " :-)" [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [Metacommand](/qb64wiki/index.php/Metacommand "Metacommand")
* [\_ASSERT](/qb64wiki/index.php/ASSERT "ASSERT")
* [$CHECKING](/qb64wiki/index.php/$CHECKING "$CHECKING")
* [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")
* [ERROR Codes](/qb64wiki/index.php/ERROR_Codes "ERROR Codes")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$ASSERTS&oldid=8262>"




## Navigation menu








### Search





















