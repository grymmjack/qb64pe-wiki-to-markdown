


AND - QB64 Phoenix Edition Wiki








# AND



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The logical AND numerical operator compares two values in respect of their bits. If both bits at a certain position in both values are set, then that bit position is set in the result.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result* = *firstvalue* AND *secondvalue*
  




## Description


* AND compares the bits of the *firstvalue* against the bits of the *secondvalue*, the result is stored in the *result* variable.
* If both bits are on (1) then the result is on (1).
* All other conditions return 0 (bit is off).
* AND is often used to see if a bit is on by comparing a value to an exponent of 2.
* Can turn off a bit by subtracting the bit on value from 255 and using that value to AND a byte value.




| ```                Table 4: The logical operations and its results.         In this table, **A** and **B** are the [Expressions](/qb64wiki/index.php/Expression "Expression") to invert or combine.               Both may be results of former [Boolean](/qb64wiki/index.php/Boolean "Boolean") evaluations.   ┌────────────────────────────────────────────────────────────────────────┐   │                           **Logical Operations**                           │   ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤   │   **A**   │   **B**   │ [NOT](/qb64wiki/index.php/NOT "NOT") **B** │ **A** AND **B** │ **A** [OR](/qb64wiki/index.php/OR "OR") **B** │ **A** [XOR](/qb64wiki/index.php/XOR "XOR") **B** │ **A** [EQV](/qb64wiki/index.php/EQV "EQV") **B** │ **A** [IMP](/qb64wiki/index.php/IMP "IMP") **B** │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **true**  │ false │  true   │ true   │  false  │  true   │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **true**  │ **false** │ true  │  false  │ true   │  true   │  false  │  false  │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **true**  │ false │  false  │ true   │  true   │  false  │  true   │   ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤   │ **false** │ **false** │ true  │  false  │ false  │  false  │  true   │  true   │   └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘    **Note:** In most BASIC languages incl. QB64 these are **bitwise** operations,          hence the logic is performed for each corresponding bit in both          operators, where **true** or **false** indicates whether a bit is **set** or          **not set**. The outcome of each bit is then placed into the respective          position to build the bit pattern of the final result value.     As all [Relational Operations](/qb64wiki/index.php/Relational_Operations "Relational Operations") return negative one (-1, **all bits set**) for     **true** and zero (0, **no bits set**) for **false**, this allows us to use these     bitwise logical operations to invert or combine any relational checks,     as the outcome is the same for each bit and so always results into a             **true** (-1) or **false** (0) again for further evaluations.  ``` |
| --- |


  




## Examples


*Example 1:*





| ```          101          AND          011         -----          001  ``` |
| --- |


The 101 bit pattern equals 5 and the 011 bit pattern equals 3, it returns the bit pattern 001 which equals 1. Only the Least Significant Bits (LSB) match. So decimal values 5 AND 3 = 1.
  

*Example 2:*





| ```       11111011         AND       11101111      ----------       11101011  ``` |
| --- |


Both bits have to be set for the resulting bit to be set. You can use the AND operator to get one byte of a two byte integer this way:
firstbyte = twobyteint AND 255
Since 255 is 11111111 in binary, it will represent the first byte completely when compared with AND.
To find the second (HI) byte's decimal value of two byte [INTEGERs](/qb64wiki/index.php/INTEGER "INTEGER") use: secondbyte = twobyteint \ 256
  

*Example 3:* Finding the binary bits on in an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value.





| ```    DO   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter Integer value from -32768 to 32767 (Enter quits): ", INTvalue&   IF INTvalue& < -32768 OR INTvalue& > 32767 OR INTval& = 0 THEN [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") exponent = 15 [TO](/qb64wiki/index.php/TO "TO") 0 [STEP](/qb64wiki/index.php/STEP "STEP") -1     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") (INTvalue& AND 2 ^ exponent) [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "1"; [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "0";   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   PRINT " "  LOOP UNTIL INTvalue& = 0 'zero entry quits   ``` |
| --- |


Example output for 6055.


| ``` 0001011110100111  ``` |
| --- |


*Note:* The value of 32767 sets 15 bits. -1 sets all 16 bits. Negative values will all have the highest bit set. Use [LONG](/qb64wiki/index.php/LONG "LONG") variables for input values to prevent overflow errors.
  




## See also


* [OR](/qb64wiki/index.php/OR "OR"), [XOR](/qb64wiki/index.php/XOR "XOR"), [NOT](/qb64wiki/index.php/NOT "NOT") (logical operators)
* [AND (boolean)](/qb64wiki/index.php/AND_(boolean) "AND (boolean)")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=AND&oldid=7808>"




## Navigation menu








### Search





















