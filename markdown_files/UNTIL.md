


UNTIL - QB64 Phoenix Edition Wiki








# UNTIL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **UNTIL** condition is used in [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP") exit verifications.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


DO [UNTIL] evaluation
.
.
.
LOOP UNTIL evaluation
  




* Only one conditional evaluation can be made at the start or the end of a [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP").
* DO UNTIL evaluates a condition before and inside of the loop. The loop may not run at all.
* LOOP UNTIL evaluates a condition inside of the loop. It has to loop once.
* Skips the loop or loops until an evaluation becomes True.


  






| ```          Table 3: The relational operations for condition checking.   In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to compare. Both must represent  the same general type, i.e. they must result into either numerical values  or [STRING](/qb64wiki/index.php/STRING "STRING") values. If a test succeeds, then **true** (-1) is returned, **false** (0)      if it fails, which both can be used in further [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.  ┌─────────────────────────────────────────────────────────────────────────┐  │                          **[Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")**                          │  ├────────────┬───────────────────────────────────────────┬────────────────┤  │ **Operation**  │                **Description**                │ **Example usage**  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [=](/qb64wiki/index.php/Equal "Equal") B    │ Tests if A is **equal** to B.                 │ [IF](/qb64wiki/index.php/IF "IF") A [=](/qb64wiki/index.php/Equal "Equal") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B   │ Tests if A is **not equal** to B.             │ [IF](/qb64wiki/index.php/IF "IF") A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<](/qb64wiki/index.php/Less_Than "Less Than") B    │ Tests if A is **less than** B.                │ [IF](/qb64wiki/index.php/IF "IF") A [<](/qb64wiki/index.php/Less_Than "Less Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B    │ Tests if A is **greater than** B.             │ [IF](/qb64wiki/index.php/IF "IF") A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B   │ Tests if A is **less than or equal** to B.    │ [IF](/qb64wiki/index.php/IF "IF") A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B   │ Tests if A is **greater than or equal** to B. │ [IF](/qb64wiki/index.php/IF "IF") A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  └────────────┴───────────────────────────────────────────┴────────────────┘    The operations should be very obvious for numerical values. For strings    be aware that all checks are done **case sensitive** (i.e. "Foo" <> "foo").    The **equal**/**not equal** check is pretty much straight forward, but for the    **less**/**greater** checks the [ASCII](/qb64wiki/index.php/ASCII "ASCII") value of the first different character is                           used for decision making:     **E.g.** "abc" is **less** than "abd", because in the first difference (the 3rd         character) the "c" has a lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") value than the "d".     This behavior may give you some subtle results, if you are not aware of                    the [ASCII](/qb64wiki/index.php/ASCII "ASCII") values and the written case:     **E.g.** "abc" is **greater** than "abD", because the small letters have higher         [ASCII](/qb64wiki/index.php/ASCII "ASCII") values than the capital letters, hence "c" > "D". You may use         [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$") or [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") to make sure both strings have the same case.  ``` |
| --- |


  




## See also


* [WHILE](/qb64wiki/index.php/WHILE "WHILE")
* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP")
* [WHILE...WEND](/qb64wiki/index.php/WHILE...WEND "WHILE...WEND")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=UNTIL&oldid=7458>"




## Navigation menu








### Search





















