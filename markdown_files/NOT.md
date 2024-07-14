


NOT - QB64 Phoenix Edition Wiki








# NOT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
NOT is a [boolean](/qb64wiki/index.php/Boolean "Boolean") logical operator that will change a false statement to a true one and vice-versa.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*True* = -1: *False* = NOT True
  




## Description


* In QBasic, True = -1 and False = 0 in boolean logic and evaluation statements.
* NOT evaluates a value and returns the bitwise opposite, meaning that NOT 0 = -1.
* Often called a negative logic operator, it returns the opposite of a value as true or false.
* Values are changed by their bit values so that each bit is changed to the opposite of on or off. See example 3 below.


  






| ```          Table 3: The relational operations for condition checking.   In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to compare. Both must represent  the same general type, i.e. they must result into either numerical values  or [STRING](/qb64wiki/index.php/STRING "STRING") values. If a test succeeds, then **true** (-1) is returned, **false** (0)      if it fails, which both can be used in further [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.  ┌─────────────────────────────────────────────────────────────────────────┐  │                          **[Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")**                          │  ├────────────┬───────────────────────────────────────────┬────────────────┤  │ **Operation**  │                **Description**                │ **Example usage**  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [=](/qb64wiki/index.php/Equal "Equal") B    │ Tests if A is **equal** to B.                 │ [IF](/qb64wiki/index.php/IF "IF") A [=](/qb64wiki/index.php/Equal "Equal") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B   │ Tests if A is **not equal** to B.             │ [IF](/qb64wiki/index.php/IF "IF") A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<](/qb64wiki/index.php/Less_Than "Less Than") B    │ Tests if A is **less than** B.                │ [IF](/qb64wiki/index.php/IF "IF") A [<](/qb64wiki/index.php/Less_Than "Less Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B    │ Tests if A is **greater than** B.             │ [IF](/qb64wiki/index.php/IF "IF") A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B   │ Tests if A is **less than or equal** to B.    │ [IF](/qb64wiki/index.php/IF "IF") A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B   │ Tests if A is **greater than or equal** to B. │ [IF](/qb64wiki/index.php/IF "IF") A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  └────────────┴───────────────────────────────────────────┴────────────────┘    The operations should be very obvious for numerical values. For strings    be aware that all checks are done **case sensitive** (i.e. "Foo" <> "foo").    The **equal**/**not equal** check is pretty much straight forward, but for the    **less**/**greater** checks the [ASCII](/qb64wiki/index.php/ASCII "ASCII") value of the first different character is                           used for decision making:     **E.g.** "abc" is **less** than "abd", because in the first difference (the 3rd         character) the "c" has a lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") value than the "d".     This behavior may give you some subtle results, if you are not aware of                    the [ASCII](/qb64wiki/index.php/ASCII "ASCII") values and the written case:     **E.g.** "abc" is **greater** than "abD", because the small letters have higher         [ASCII](/qb64wiki/index.php/ASCII "ASCII") values than the capital letters, hence "c" > "D". You may use         [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$") or [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") to make sure both strings have the same case.  ``` |
| --- |


  






| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ NOT **B** │ **A** [AND](/qb64wiki/index.php/AND "AND") **B** │ **A** [OR](/qb64wiki/index.php/OR "OR") **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** [EQV](/qb64wiki/index.php/EQV "EQV") **B** │ **A** [IMP](/qb64wiki/index.php/IMP "IMP") **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


  




## Examples


*Example 1:* Alternating between two conditions in a program loop.





| ``` [DO](/qb64wiki/index.php/DO "DO") switch = NOT switch       'NOT changes value from -1 to 0 and vice-versa [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 10, 38 [IF](/qb64wiki/index.php/IF "IF") switch [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "True!" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "False" [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") k$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") k$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) ' escape key quit  ``` |
| --- |


  

*Example 2:* Reading a file until it reaches the End Of File.





| ``` DO WHILE NOT EOF(1)   INPUT #1, data1, data2, data3 LOOP  ``` |
| --- |


*Explanation:* [EOF](/qb64wiki/index.php/EOF "EOF") will return 0 until a file ends. NOT converts 0 to -1 so that the loop continues to run. When EOF becomes -1, NOT converts it to 0 to end the loop.
  

*Example 3:* So why does **NOT 5 = -6**? Because NOT changes every bit of a value into the opposite:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") NOT 5 [PRINT](/qb64wiki/index.php/PRINT "PRINT") ReadBits 5 ReadBits -6  [SUB](/qb64wiki/index.php/SUB "SUB") ReadBits (n [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")) 'change type value and i bit reads for other whole type values [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 15 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1 'see the 16 bit values     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") 2 ^ i [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "1"; [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "0"; [NEXT](/qb64wiki/index.php/NEXT "NEXT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




| ``` -6  0000000000000101 1111111111111010  ``` |
| --- |


*Explanation:* The bit values of an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") are 2 [\_BYTEs](/qb64wiki/index.php/BYTE "BYTE") and each bit is an exponent of 2 from 15 to 0 (16 bits). Thus comparing the numerical value with those exponents using [AND](/qb64wiki/index.php/AND "AND") reveals the bit values as "1" for bits on or "0" for bits off as text.
QB64 can use [&B](/qb64wiki/index.php/%26B "&B") to convert the above [\_BIT](/qb64wiki/index.php/BIT "BIT") values back to [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") or [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") values as shown below:


| ``` '16 bit INTEGER values from -32768 to 32767 a% = [&B](/qb64wiki/index.php/%26B "&B")0000000000000101 [PRINT](/qb64wiki/index.php/PRINT "PRINT") a% b% = [&B](/qb64wiki/index.php/%26B "&B")1111111111111010 [PRINT](/qb64wiki/index.php/PRINT "PRINT") b% '8 bit BYTE values from -128 to 127 a%% = [&B](/qb64wiki/index.php/%26B "&B")00000101 [PRINT](/qb64wiki/index.php/PRINT "PRINT") a%% b%% = [&B](/qb64wiki/index.php/%26B "&B")11111010 [PRINT](/qb64wiki/index.php/PRINT "PRINT") b%%  ``` |
| --- |


  




## See also


* [\_BIT](/qb64wiki/index.php/BIT "BIT"), [&B](/qb64wiki/index.php/%26B "&B"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* [AND](/qb64wiki/index.php/AND "AND"), [XOR](/qb64wiki/index.php/XOR "XOR"), [OR](/qb64wiki/index.php/OR "OR")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NOT&oldid=6124>"




## Navigation menu








### Search





















