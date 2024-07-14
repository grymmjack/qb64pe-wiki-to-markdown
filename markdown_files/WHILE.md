


WHILE...WEND - QB64 Phoenix Edition Wiki








# WHILE...WEND



From QB64 Phoenix Edition Wiki
(Redirected from [WHILE](/qb64wiki/index.php?title=WHILE&redirect=no "WHILE"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The WHILE...WEND statement is used to repeat a block of statements while the condition is met.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[WHILE](/qb64wiki/index.php/WHILE "WHILE") *condition*
.
.
.
[WEND](/qb64wiki/index.php/WEND "WEND")
  




## Description


* *condition* is a numeric expression used to determine if the loop will execute.
* *statements* will execute repeatedly while *condition* is a non-zero value.
* [EXIT](/qb64wiki/index.php/EXIT "EXIT") WHILE can be used for emergency exits from the loop in QB64 only.
* A [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP") can use the same DO WHILE condition to get the same results.
* WHILE loops only run if the WHILE condition is True.


  






| ```          Table 3: The relational operations for condition checking.   In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to compare. Both must represent  the same general type, i.e. they must result into either numerical values  or [STRING](/qb64wiki/index.php/STRING "STRING") values. If a test succeeds, then **true** (-1) is returned, **false** (0)      if it fails, which both can be used in further [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.  ┌─────────────────────────────────────────────────────────────────────────┐  │                          **[Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")**                          │  ├────────────┬───────────────────────────────────────────┬────────────────┤  │ **Operation**  │                **Description**                │ **Example usage**  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [=](/qb64wiki/index.php/Equal "Equal") B    │ Tests if A is **equal** to B.                 │ [IF](/qb64wiki/index.php/IF "IF") A [=](/qb64wiki/index.php/Equal "Equal") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B   │ Tests if A is **not equal** to B.             │ [IF](/qb64wiki/index.php/IF "IF") A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<](/qb64wiki/index.php/Less_Than "Less Than") B    │ Tests if A is **less than** B.                │ [IF](/qb64wiki/index.php/IF "IF") A [<](/qb64wiki/index.php/Less_Than "Less Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B    │ Tests if A is **greater than** B.             │ [IF](/qb64wiki/index.php/IF "IF") A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B   │ Tests if A is **less than or equal** to B.    │ [IF](/qb64wiki/index.php/IF "IF") A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B   │ Tests if A is **greater than or equal** to B. │ [IF](/qb64wiki/index.php/IF "IF") A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  └────────────┴───────────────────────────────────────────┴────────────────┘    The operations should be very obvious for numerical values. For strings    be aware that all checks are done **case sensitive** (i.e. "Foo" <> "foo").    The **equal**/**not equal** check is pretty much straight forward, but for the    **less**/**greater** checks the [ASCII](/qb64wiki/index.php/ASCII "ASCII") value of the first different character is                           used for decision making:     **E.g.** "abc" is **less** than "abd", because in the first difference (the 3rd         character) the "c" has a lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") value than the "d".     This behavior may give you some subtle results, if you are not aware of                    the [ASCII](/qb64wiki/index.php/ASCII "ASCII") values and the written case:     **E.g.** "abc" is **greater** than "abD", because the small letters have higher         [ASCII](/qb64wiki/index.php/ASCII "ASCII") values than the capital letters, hence "c" > "D". You may use         [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$") or [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") to make sure both strings have the same case.  ``` |
| --- |


  




## Examples


*Example 1:* Reading an entire file. Example assumes the program has a [file opened](/qb64wiki/index.php/OPEN "OPEN") as #1





| ``` [OPEN](/qb64wiki/index.php/OPEN "OPEN") "Readme.txt" FOR [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") AS #1 WHILE [NOT](/qb64wiki/index.php/NOT "NOT") [EOF](/qb64wiki/index.php/EOF "EOF")(1)     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 1                                    'limit line prints to one per second     [LINE INPUT #](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)")1, text$     IF [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) THEN [EXIT](/qb64wiki/index.php/EXIT "EXIT") [WHILE](/qb64wiki/index.php/WHILE "WHILE")        'ESC key exits     [PRINT](/qb64wiki/index.php/PRINT "PRINT") text$ [WEND](/qb64wiki/index.php/WEND "WEND")  ``` |
| --- |


*Example 2:* Clearing the keyboard buffer.





| ``` [WHILE](/qb64wiki/index.php/WHILE "WHILE") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" : [WEND](/qb64wiki/index.php/WEND "WEND")  ``` |
| --- |


  




## See also


* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP")
* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")
* [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL")
* [\_CONTINUE](/qb64wiki/index.php/CONTINUE "CONTINUE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=WHILE...WEND&oldid=7708>"




## Navigation menu








### Search





















