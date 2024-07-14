


SUB - QB64 Phoenix Edition Wiki








# SUB



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
A **SUB** procedure is a procedure within a program that can calculate and return multiple parameter values just like a full program.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


SUB ProcedureName [(*1stParam*[, *2ndParam* ... [, *lastParam*)]
...
... 'procedure variable definitions and statements
...
[END SUB](/qb64wiki/index.php/END_SUB "END SUB")
  




## Parameters


* Parameters passed after the procedure call must match the variable types in the SUB parameters in order.
* If there are no *parameter*s passed or they are [SHARED](/qb64wiki/index.php/SHARED "SHARED") the parameters and parenthesis are not required in the procedure.
* Parameter [Variable](/qb64wiki/index.php/Variable "Variable") names in the procedure do not have to match the names used in the [CALL](/qb64wiki/index.php/CALL "CALL"), just the value types.


  




## Description


* All [dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") [variable](/qb64wiki/index.php/Variable "Variable") values return to 0 or null strings when the procedure is exited except for [STATIC](/qb64wiki/index.php/STATIC "STATIC") variable values.
* SUB procedures can return multiple values through the parameters unlike functions.
* SUB procedures return to the next code statement after the call in the main or other procedures.
* [EXIT](/qb64wiki/index.php/EXIT "EXIT") SUB can be used to exit early or to exit before [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures using [RETURN](/qb64wiki/index.php/RETURN "RETURN").
* [TYPE](/qb64wiki/index.php/TYPE "TYPE") and [DECLARE LIBRARY](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY") declarations can be made inside of SUB procedures in QB64 only.
* SUB procedures can save program memory as all memory used in a SUB is released on procedure exit except for [STATIC](/qb64wiki/index.php/STATIC "STATIC") values.
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") can be used to define all new or old QB64 variable [TYPE](/qb64wiki/index.php/TYPE "TYPE") definitions instead of DEF\*\*\*.
* [$INCLUDE](/qb64wiki/index.php/$INCLUDE "$INCLUDE") text library files with needed SUB and [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures can be included in programs after all sub-procedures.
* **QB64 ignores all procedural DECLARE statements.** Define all *parameter* [TYPEs](/qb64wiki/index.php/TYPE "TYPE") in the SUB procedure.
* **Images are not deallocated when the SUB or [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**


  

*Example 1:* Text [PRINT](/qb64wiki/index.php/PRINT "PRINT") screen centering using [PEEK](/qb64wiki/index.php/PEEK "PEEK") to find the SCREEN mode width. Call and SUB procedure code:





| ``` [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 Center 10, 15, "This text is centered." ' example module sub call [END](/qb64wiki/index.php/END "END")  [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z ' only code allowed before SUB line is a DEF statement or a comment SUB Center (Tclr, Trow, Text$) Columns = [_WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") / [_FONTWIDTH](/qb64wiki/index.php/FONTWIDTH "FONTWIDTH") 'Convert _WIDTH (in pixels) to width in characters Middle = (Columns \ 2) + 1 ' reads any screen mode width Tcol = Middle - ([LEN](/qb64wiki/index.php/LEN "LEN")(Text$) \ 2) [COLOR](/qb64wiki/index.php/COLOR "COLOR") Tclr: [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") Trow, Tcol: [PRINT](/qb64wiki/index.php/PRINT "PRINT") Text$; ' end semicolon prevents screen roll [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


*Explanation:* The procedure centers text printed to the screen. The parameters are the text color, row and the text itself as a string or string variable. The maximum width of the screen mode in characters is found and divided in half to find the center point. The text string's length is also divided in half and subtracted from the screen's center position. The procedure will also work when the [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") statement has been used. When adding variables to Text$ use the + concatenation operator. Not semicolons!
  

*Example 2:* SUB and [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") procedures always return to the place they were called in the main or other sub-procedures:





| ``` a = 10 Add1 a [PRINT](/qb64wiki/index.php/PRINT "PRINT") a  'Add1 returns final 'a' value here  [END](/qb64wiki/index.php/END "END")  SUB Add1 (n) n = n + 1 Add2 n [PRINT](/qb64wiki/index.php/PRINT "PRINT") "exit 1" [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  SUB Add2 (m) m = m + 2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "exit 2" [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |




| ``` exit 2 exit 1  13  ``` |
| --- |


*Note:* Parameter **a** is used to call the sub-procedures even though parameters **n** and **m** are used internally.
  




## See also


* [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION"), [CALL](/qb64wiki/index.php/CALL "CALL")
* [BYVAL](/qb64wiki/index.php/BYVAL "BYVAL"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [EXIT](/qb64wiki/index.php/EXIT "EXIT"), [END](/qb64wiki/index.php/END "END")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SUB&oldid=7432>"




## Navigation menu








### Search





















