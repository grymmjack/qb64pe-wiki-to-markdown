


IF...THEN - QB64 Phoenix Edition Wiki








# IF...THEN



From QB64 Phoenix Edition Wiki
(Redirected from [IF](/qb64wiki/index.php?title=IF&redirect=no "IF"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
IF...THEN statements make boolean (true or false) evaluations to automate program decision making.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 Single-line](#Single-line) 	+ [1.2 Block](#Block) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


### Single-line


[IF](/qb64wiki/index.php/IF "IF") *conditionStatement* [THEN](/qb64wiki/index.php/THEN "THEN") *{code}* [ELSE](/qb64wiki/index.php/ELSE "ELSE") *{alternativeCode}*
[IF](/qb64wiki/index.php/IF "IF") *conditionStatement* [GOTO](/qb64wiki/index.php/GOTO "GOTO") *lineLabel*
### Block


[IF](/qb64wiki/index.php/IF "IF") *conditionStatement* [THEN](/qb64wiki/index.php/THEN "THEN")
*{code}*
⋮
[ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") *conditionStatement2* [THEN](/qb64wiki/index.php/THEN "THEN")
*{code}*
⋮
[ELSE](/qb64wiki/index.php/ELSE "ELSE")
*{code}*
⋮
[END IF](/qb64wiki/index.php/END_IF "END IF")
  




## Description


* The *conditionStatement* evaluation by [IF](/qb64wiki/index.php/IF "IF") must be true (-1) or a **non-zero numerical value** for the [THEN](/qb64wiki/index.php/THEN "THEN") *{code}* to be executed.
* Multiple conditional evaluations can be made using inclusive [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") or alternative [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") conditional expressions.
* [THEN](/qb64wiki/index.php/THEN "THEN") is not required when [GOTO](/qb64wiki/index.php/GOTO "GOTO") is used to send program flow to a line number or label.
* [IF](/qb64wiki/index.php/IF "IF") statements can also have alternative evaluations using [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") and [ELSE](/qb64wiki/index.php/ELSE "ELSE") conditions.
* When the [IF](/qb64wiki/index.php/IF "IF") statement and/or code to be run is more than code line, an [END IF](/qb64wiki/index.php/END_IF "END IF") statement must be used.
* With multiple code lines to run, end the IF statement with THEN and place all of the code on lines below that line.
* Multiple code line block statements require that the IF...THEN, [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF"), [ELSE](/qb64wiki/index.php/ELSE "ELSE") and [END IF](/qb64wiki/index.php/END_IF "END IF") be on separate lines.
* **The IDE may return an error of *[NEXT](/qb64wiki/index.php/NEXT "NEXT") without [FOR](/qb64wiki/index.php/FOR "FOR")* or *[LOOP](/qb64wiki/index.php/LOOP "LOOP") without [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")* when [END IF](/qb64wiki/index.php/END_IF "END IF") does not end a statement block.**
* The **QB64** IDE will indicate an error in the IF statement line until END IF closes the statement block.
* Use [colons](/qb64wiki/index.php/Colon "Colon") to execute multiple statements in a single-line IF statement.
* An **[underscore](/qb64wiki/index.php/Underscore "Underscore")** can be used anywhere after the code on a single-line to continue it to the next line in **QB64**.
* **NOTE:** [STRING](/qb64wiki/index.php/STRING "STRING") values can only be evaluated in an IF statement if a value is compared to a literal or [CHR$](/qb64wiki/index.php/CHR$ "CHR$") string value. **QB64 may not compile literal IF string statements or indicate an IDE coding error.** Use [LEN](/qb64wiki/index.php/LEN "LEN") or [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") to compare strings numerically.


  






| ```          Table 3: The relational operations for condition checking.   In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to compare. Both must represent  the same general type, i.e. they must result into either numerical values  or [STRING](/qb64wiki/index.php/STRING "STRING") values. If a test succeeds, then **true** (-1) is returned, **false** (0)      if it fails, which both can be used in further [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.  ┌─────────────────────────────────────────────────────────────────────────┐  │                          **[Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations")**                          │  ├────────────┬───────────────────────────────────────────┬────────────────┤  │ **Operation**  │                **Description**                │ **Example usage**  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [=](/qb64wiki/index.php/Equal "Equal") B    │ Tests if A is **equal** to B.                 │ [IF](/qb64wiki/index.php/IF "IF") A [=](/qb64wiki/index.php/Equal "Equal") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B   │ Tests if A is **not equal** to B.             │ [IF](/qb64wiki/index.php/IF "IF") A [<>](/qb64wiki/index.php/Not_Equal "Not Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<](/qb64wiki/index.php/Less_Than "Less Than") B    │ Tests if A is **less than** B.                │ [IF](/qb64wiki/index.php/IF "IF") A [<](/qb64wiki/index.php/Less_Than "Less Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B    │ Tests if A is **greater than** B.             │ [IF](/qb64wiki/index.php/IF "IF") A [>](/qb64wiki/index.php/Greater_Than "Greater Than") B [THEN](/qb64wiki/index.php/THEN "THEN")  │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B   │ Tests if A is **less than or equal** to B.    │ [IF](/qb64wiki/index.php/IF "IF") A [<=](/qb64wiki/index.php/Less_Than_Or_Equal "Less Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  ├────────────┼───────────────────────────────────────────┼────────────────┤  │   A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B   │ Tests if A is **greater than or equal** to B. │ [IF](/qb64wiki/index.php/IF "IF") A [>=](/qb64wiki/index.php/Greater_Than_Or_Equal "Greater Than Or Equal") B [THEN](/qb64wiki/index.php/THEN "THEN") │  └────────────┴───────────────────────────────────────────┴────────────────┘    The operations should be very obvious for numerical values. For strings    be aware that all checks are done **case sensitive** (i.e. "Foo" <> "foo").    The **equal**/**not equal** check is pretty much straight forward, but for the    **less**/**greater** checks the [ASCII](/qb64wiki/index.php/ASCII "ASCII") value of the first different character is                           used for decision making:     **E.g.** "abc" is **less** than "abd", because in the first difference (the 3rd         character) the "c" has a lower [ASCII](/qb64wiki/index.php/ASCII "ASCII") value than the "d".     This behavior may give you some subtle results, if you are not aware of                    the [ASCII](/qb64wiki/index.php/ASCII "ASCII") values and the written case:     **E.g.** "abc" is **greater** than "abD", because the small letters have higher         [ASCII](/qb64wiki/index.php/ASCII "ASCII") values than the capital letters, hence "c" > "D". You may use         [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$") or [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$") to make sure both strings have the same case.  ``` |
| --- |


  




**Boolean Conditional Operators:**
  




* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") can be used to add extra conditions to a boolean statement evaluation.
* [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") can be used to add alternate conditions to a boolean statement evaluation.
* Parenthesis are allowed inside of boolean statements to clarify an evaluation.

  




**Mathematical Logical operators:**
\* Truth table of the 6 BASIC Logical Operators:
  






| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ [NOT](/qb64wiki/index.php/NOT "NOT") **B** │ **A** [AND](/qb64wiki/index.php/AND "AND") **B** │ **A** [OR](/qb64wiki/index.php/OR "OR") **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** [EQV](/qb64wiki/index.php/EQV "EQV") **B** │ **A** [IMP](/qb64wiki/index.php/IMP "IMP") **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


\* **Note that Basic returns -1 for True and 0 for False.**
  




## Examples


*Example 1:* In a one line IF statement, only [REM](/qb64wiki/index.php/REM "REM") can be used to comment out the action without an [END IF](/qb64wiki/index.php/END_IF "END IF") error:





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number over or under 100: ", x IF x > 100 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") x IF x > 100 [THEN](/qb64wiki/index.php/THEN "THEN") [REM](/qb64wiki/index.php/REM "REM") [PRINT](/qb64wiki/index.php/PRINT "PRINT") x  *'*  ``` |
| --- |


  

*Example 2:* IF statement blocks require that the IF THEN and END IF statements be separate from the code executed.





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number over or under 100: ", x IF x > 100 [THEN](/qb64wiki/index.php/THEN "THEN")   y = 200   [PRINT](/qb64wiki/index.php/PRINT "PRINT") y   [PRINT](/qb64wiki/index.php/PRINT "PRINT") x [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  

*Example 3:* True or False evaluation of a numerical value executes only when the value is not 0. **Cannot evaluate [STRING](/qb64wiki/index.php/STRING "STRING") values.**





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number or just hit Enter: ", x IF x [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") x  ``` |
| --- |


Example will only print if a numerical value is True (positive or negative). (Equivalent to: IF x > 0 OR x < 0 THEN evaluation)
  

*Example 4:* Multiple evaluations using parenthesis to determine the order.





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number over or under 100 or 50: ", value IF (value% > 100 [AND](/qb64wiki/index.php/AND_(boolean) "AND (boolean)") value% < 200) [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") value% = 50 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "OK"  ``` |
| --- |


  

*Example 5:* Using multiple IF options in a one line statement.





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a number over or under 200: ", x IF x > 200 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "High" [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF") x < 0 [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Low" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "OK"   ``` |
| --- |


  

*Example 6:* [STRING](/qb64wiki/index.php/STRING "STRING") values can be compared using greater than, less than, not equal to or equal to operators only.





| ``` PRINT "Press a letter key: "; Key$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) PRINT Key$ IF Key$ >= [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(65) AND Key$ <= [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(90) THEN PRINT "A to Z"  ``` |
| --- |


*Explanation:* Long [STRING](/qb64wiki/index.php/STRING "STRING") expression values are compared by their cumulative [ASCII](/qb64wiki/index.php/ASCII "ASCII") code values.
  




**QBasic decimal point value comparison errors**
* Floating decimal point numerical values may not be compared as exactly the same value. QB64 will compare them the same.


*Example:* QBasic would print *unequal* in the IF comparison code below even though it is exactly the same value printed.


| ``` x# = 5 / 10 y# = 6 / 10 z# = x# + y# [PRINT](/qb64wiki/index.php/PRINT "PRINT") x#, y#, z# IF x# + y# = z# [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "equal" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "unequal"  ``` |
| --- |


Note: QB64 will make the calculation correctly and print *equal*. Change older program code that relies on the error accordingly.
  




## See also


* [ELSEIF](/qb64wiki/index.php/ELSEIF "ELSEIF"), [ELSE](/qb64wiki/index.php/ELSE "ELSE")
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)"), [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)")
* [NOT](/qb64wiki/index.php/NOT "NOT"), [GOTO](/qb64wiki/index.php/GOTO "GOTO")
* [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE")
* [Boolean](/qb64wiki/index.php/Boolean "Boolean") (numerical comparisons return a true or false value)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=IF...THEN&oldid=8134>"




## Navigation menu








### Search





















