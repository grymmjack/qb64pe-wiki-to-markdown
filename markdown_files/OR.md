


OR - QB64 Phoenix Edition Wiki








# OR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The OR numerical operator returns a comparative bit value of 1 if either value's bit is on.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result* = firstValue OR secondValue
  




## Description


* If both bits are off, it returns 0.
* If one or both bits are on then it returns 1.
* OR never turns off a bit and can be used only to turn a bit on.




| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ [NOT](/qb64wiki/index.php/NOT "NOT") **B** │ **A** [AND](/qb64wiki/index.php/AND "AND") **B** │ **A** OR **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** [EQV](/qb64wiki/index.php/EQV "EQV") **B** │ **A** [IMP](/qb64wiki/index.php/IMP "IMP") **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


  




## Examples


*Example 1:* OR always turns bits on! Never off.





| ```  a% = 5 ' 101 binary  b% = 4 ' 100 binary  results% = a% OR b%  ' still 101 binary using OR  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Results% ="; results%  ``` |
| --- |




| ```  Results% = 5  ``` |
| --- |


  

*Example 2:* Turning a data register bit on.





| ```    address% = 888    'parallel port data register    bytevalue% = [INP](/qb64wiki/index.php/INP "INP")(address%)    [OUT](/qb64wiki/index.php/OUT "OUT") address%, bytevalue% OR 4  ``` |
| --- |


*Explanation:* The third register bit is only turned on if it was off. This ensures that a bit is set. OR could set more bits on with a sum of bit values such as: OUT address%, 7 would turn the first, second and third bits on. 1 + 2 + 4 = 7
  




## See also


* [AND](/qb64wiki/index.php/AND "AND"), [XOR](/qb64wiki/index.php/XOR "XOR")
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)"), [OR (boolean)](/qb64wiki/index.php/OR_(boolean) "OR (boolean)")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OR&oldid=7352>"




## Navigation menu








### Search





















