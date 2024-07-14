


IMP - QB64 Phoenix Edition Wiki








# IMP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The IMP logical operator converts the result of two comparative values and returns a bit result.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result* = *firstValue* IMP *secondValue*
  




## Description


* Returns a different result from [AND](/qb64wiki/index.php/AND "AND"), [OR](/qb64wiki/index.php/OR "OR") or [XOR](/qb64wiki/index.php/XOR "XOR") - see truth table below.
* Evaluates if *firstValue* ***imp**lies* *secondValue*.
	+ If *firstValue* is true then *secondValue* must also be true.
	+ So if *firstValue* is true, and *secondValue* false, then the condition is false, otherwise it is true (see table below).




| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ [NOT](/qb64wiki/index.php/NOT "NOT") **B** │ **A** [AND](/qb64wiki/index.php/AND "AND") **B** │ **A** [OR](/qb64wiki/index.php/OR "OR") **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** [EQV](/qb64wiki/index.php/EQV "EQV") **B** │ **A** IMP **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


  




## See also


* [Binary](/qb64wiki/index.php/Binary "Binary")
* [Boolean](/qb64wiki/index.php/Boolean "Boolean")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=IMP&oldid=6033>"




## Navigation menu








### Search





















