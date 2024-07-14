


STRING - QB64 Phoenix Edition Wiki








# STRING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**STRING** variables or literal values are one byte per character length text or [ASCII](/qb64wiki/index.php/ASCII "ASCII") characters.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


DIM variable AS STRING [\* byte\_length]
  




* *Byte length* is optional in [DIM](/qb64wiki/index.php/DIM "DIM") statements, but is required in [TYPE](/qb64wiki/index.php/TYPE "TYPE") definitions as a literal or [constant](/qb64wiki/index.php/CONST "CONST") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value.
* Literal strings are defined by quotation marks on each end. The quotes will not [PRINT](/qb64wiki/index.php/PRINT "PRINT") to the screen.
* Quotation marks cannot be placed inside of literal string values! Use [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) to display " quotes.
* Semicolons and commas outside of the string can be used to combine strings in a [PRINT](/qb64wiki/index.php/PRINT "PRINT") statement only.
* [LEN](/qb64wiki/index.php/LEN "LEN") determines the number of bytes and number of string characters that are in a particular string.
* Literal string ends are designated by quotation marks such as: "text". Use [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) to add quotes to string values.
* Variable suffix type definition is $ such as: text$.
* STRING values are compared according to the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code values from left to right until one string code value exceeds the other.
* **NOTE: Many QBasic keyword variable names CAN be used with a STRING suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use [DIM](/qb64wiki/index.php/DIM "DIM"), [REDIM](/qb64wiki/index.php/REDIM "REDIM"), [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL") or [TYPE](/qb64wiki/index.php/TYPE "TYPE") variable [AS](/qb64wiki/index.php/AS "AS") statements!**


  




**Creating a fixed length STRING variable in QBasic:**
* Variable$ = " " ' 1 space creates a one [byte](/qb64wiki/index.php/BYTE "BYTE") string length in a procedure(not fixed)
* Variable$ = SPACE$(n%) ' defined as a n% length string in a procedure(not fixed)
* [DIM](/qb64wiki/index.php/DIM "DIM") variable AS STRING \* n% ' fixed string length cannot be changed later
* Variable AS STRING \* n% ' fixed string length in a [SUB](/qb64wiki/index.php/SUB "SUB") parameter or [TYPE](/qb64wiki/index.php/TYPE "TYPE") definition.
* [CONST](/qb64wiki/index.php/CONST "CONST") variables can also be used after the constant value is defined.

  




**QB64 fixed length string type suffixes**
* A number after the string variable name $ suffix denotes the fixed string length: **X$2** denotes a 2 byte string.


  




**String [Concatenation](/qb64wiki/index.php/Concatenation "Concatenation") (addition)**
*Must be used when defining a string variable's literal value!*
* Concatenation uses the + addition symbol to add literal or variable parts to a string variable value.
* Quotation marks cannot be added. Use [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) as quotes are used to define the ends of strings.
* Numerical values added must be converted to strings in string variable definitions. See the [STR$](/qb64wiki/index.php/STR$ "STR$") function.
* Concatenation can be used in PRINT statements along with semicolons and commas used by [PRINT](/qb64wiki/index.php/PRINT "PRINT") ONLY.
* Semicolons or commas outside of quotes cannot be used to make a string variable's literal string value!


  

*Example 1:* Using a string type suffix with a fixed length byte size in QB64 only. The number designates the fixed string length.





| ``` var$5 = "1234567"  PRINT var$5  ``` |
| --- |




| ``` 12345 ``` |
| --- |


*Note:* The suffix must keep the same byte length or it is considered a different string variable with a different value!
  

*Example 2:* Creating a string variable value by adding variable and literal string values. This procedure is called string [concatenation](/qb64wiki/index.php/Concatenation "Concatenation").





| ``` age% = 10 a$ = "I am " + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(age%)) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) + " years old." b$ = "How old are you?" question$ = a$ + [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1) + b$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") question$  ``` |
| --- |




| ``` I am "10" years old. How old are you?  ``` |
| --- |


*Note:* Since quotation marks are used to denote the ends of literal strings, [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(34) must be used to place quotes inside them.
  

*Example 3:* How QB64 string type suffixes can fix the length by adding a number of bytes after it.





| ``` strings$5 = "Hello world"  PRINT strings$5  ``` |
| --- |




| ``` Hello ``` |
| --- |


  

*Example 4:* STRING values can be compared by the [ASC](/qb64wiki/index.php/ASC_(function) "ASC (function)") code value according to [ASCII](/qb64wiki/index.php/ASCII "ASCII").





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter a letter, number or punctuation mark from the keyboard: "; valu$ = [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$")(1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") value$ value1$ = "A" value2$ = "m" value3$ = "z"  [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") value$   [CASE](/qb64wiki/index.php/CASE "CASE") value1$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "A only"   [CASE](/qb64wiki/index.php/CASE "CASE") value1$ [TO](/qb64wiki/index.php/TO "TO") value2$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "B to m" 'A is already evaluated   [CASE](/qb64wiki/index.php/CASE "CASE") value1$, value2$, value3$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "z only" 'A and m are already evaluated   [CASE IS](/qb64wiki/index.php/CASE_IS "CASE IS") > value2$: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "greater than m but not z" 'z is already evaluated   [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): [PRINT](/qb64wiki/index.php/PRINT "PRINT") "other value" 'key entry below A including all numbers [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")  ``` |
| --- |


*Notes:* STRING values using multiple characters will be compared by the [ASCII](/qb64wiki/index.php/ASCII "ASCII") code values sequentially from left to right. Once the equivalent code value of one string is larger than the other the evaluation stops. This allows string values to be compared and sorted alphabetically using [>](/qb64wiki/index.php/Greater_Than "Greater Than") or [<](/qb64wiki/index.php/Less_Than "Less Than") and to [SWAP](/qb64wiki/index.php/SWAP "SWAP") values in [arrays](/qb64wiki/index.php/Arrays "Arrays") irregardless of the string lengths.
  




## See also


* [DIM](/qb64wiki/index.php/DIM "DIM"), [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR")
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)")
* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$"), [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")
* [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$"), [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")
* [STR$](/qb64wiki/index.php/STR$ "STR$")
* [HEX$](/qb64wiki/index.php/HEX$ "HEX$")
* [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKD$](/qb64wiki/index.php/MKD$ "MKD$"), [\_MK$](/qb64wiki/index.php/MK$ "MK$")
* [CVI](/qb64wiki/index.php/CVI "CVI"), [CVL](/qb64wiki/index.php/CVL "CVL"), [CVS](/qb64wiki/index.php/CVS "CVS"), [CVD](/qb64wiki/index.php/CVD "CVD"), [\_CV](/qb64wiki/index.php/CV "CV")
* [LEN](/qb64wiki/index.php/LEN "LEN"), [VAL](/qb64wiki/index.php/VAL "VAL")
* [ASCII](/qb64wiki/index.php/ASCII "ASCII"), [DRAW](/qb64wiki/index.php/DRAW "DRAW")
* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING"), [WRITE](/qb64wiki/index.php/WRITE "WRITE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STRING&oldid=8170>"




## Navigation menu








### Search





















