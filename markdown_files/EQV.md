


EQV - QB64 Phoenix Edition Wiki








# EQV



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The EQV operator returns a value based on the *equivalence* of two conditions or values.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result* = *firstValue* EQV *secondValue*
  




## Description


* Returns true (-1) when both values are the same (*equivalent*).
* Turns a bit on if both bits are the same, turns a bit off if both bits are different.




| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ [NOT](/qb64wiki/index.php/NOT "NOT") **B** │ **A** [AND](/qb64wiki/index.php/AND "AND") **B** │ **A** [OR](/qb64wiki/index.php/OR "OR") **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** EQV **B** │ **A** [IMP](/qb64wiki/index.php/IMP "IMP") **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1187)
* [Binary](/qb64wiki/index.php/Binary "Binary")
* [Boolean](/qb64wiki/index.php/Boolean "Boolean")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=EQV&oldid=8919>"




## Navigation menu








### Search





















