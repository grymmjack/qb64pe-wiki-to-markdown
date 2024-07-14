


FUNCTION - QB64 Phoenix Edition Wiki








# FUNCTION



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
A FUNCTION block statement is used to create a function procedure to return a calculated value to a program.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


**FUNCTION procedureName**[type-suffix] [(*parameters*)]
*{code}*
'variable definitions and procedure statements
⋮
procedureName = returnValue
**END FUNCTION**
  




## Description


* The function type can be any variable type that it will return to the program and is represented by the type suffix.
* Functions hold one return value in the function's name which is a variable type. Other values can be passed through *parameters*.
* Functions are often referred to in program calculations, not called like SUB procedures. [CALL](/qb64wiki/index.php/CALL "CALL") cannot be used with functions.
* If there are no parameters passed or they are [SHARED](/qb64wiki/index.php/SHARED "SHARED") the *parameters* and parenthesis are not required.
* Variable names within the procedure do not have to match the names used in the reference parameters, just the value types.
* To pass parameter variables [by value](/qb64wiki/index.php/BYVAL "BYVAL") to protect the value in a call, parenthesis can be placed around each variable name also.
* To pass [arrays](/qb64wiki/index.php/Arrays "Arrays") to a sub-procedure use empty brackets after the name or indicate the index in the call.
* All [dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") variable values return to 0 or null strings when the procedure is exited except when a variable or the entire function is [STATIC](/qb64wiki/index.php/STATIC "STATIC"). This can save program memory as all [dynamic](/qb64wiki/index.php/$DYNAMIC "$DYNAMIC") memory used in a FUNCTION is released on procedure exit.
* FUNCTION procedure code can use [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") and [GOTO](/qb64wiki/index.php/GOTO "GOTO") line numbers or labels inside of the procedure when necessary.
* For early function exits use [EXIT](/qb64wiki/index.php/EXIT "EXIT") FUNCTION before [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION") and [GOSUB](/qb64wiki/index.php/GOSUB "GOSUB") procedures using [RETURN](/qb64wiki/index.php/RETURN "RETURN").
* **QB64 ignores all procedural DECLARE statements.** Define all *parameter* [types](/qb64wiki/index.php/Data_types "Data types") in the FUNCTION procedure.
* **Images are not deallocated when the [SUB](/qb64wiki/index.php/SUB "SUB") or FUNCTION they are created in ends. Free them with [\_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE").**
* The IDE can create the FUNCTION and END FUNCTION lines for you. Use the *New FUNCTION...* option in the Edit Menu. A box will come up for you to enter a name for the FUNCTION. Enter all code between the FUNCTION and [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION") lines.


### QBasic/QuickBASIC


* Once a FUNCTION was created and used, the QBasic IDE would DECLARE it when the file was saved. **QB64 doesn't need these declarations.**
* QBasic's IDE could place a [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT"), [DEFSNG](/qb64wiki/index.php/DEFSNG "DEFSNG"), [DEFLNG](/qb64wiki/index.php/DEFLNG "DEFLNG"), [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL") or [DEFSTR](/qb64wiki/index.php/DEFSTR "DEFSTR") statement before the FUNCTION line if it is used in the main module. It may even be the wrong variable type needed.
* QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.


  




## Examples


*Example 1:* A simple function that returns the current path. Place FUNCTION or [SUB](/qb64wiki/index.php/SUB "SUB") procedures after the program [END](/qb64wiki/index.php/END "END").





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Current path = "; PATH$ [END](/qb64wiki/index.php/END "END")  FUNCTION PATH$     f% = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE")     file$ = "D0Spath.inf" 'file name uses a zero to prevent an overwrite of existing file name     [SHELL](/qb64wiki/index.php/SHELL "SHELL") [_HIDE](/qb64wiki/index.php/HIDE "HIDE") "CD > " + file$ 'send screen information to a created text file     [OPEN](/qb64wiki/index.php/OPEN "OPEN") file$ [FOR](/qb64wiki/index.php/FOR_(file_statement) "FOR (file statement)") [INPUT](/qb64wiki/index.php/INPUT_(file_mode) "INPUT (file mode)") [AS](/qb64wiki/index.php/AS "AS") #f% 'file should exist with one line of text     [LINE INPUT](/qb64wiki/index.php/LINE_INPUT_(file_statement) "LINE INPUT (file statement)") #f%, PATH$ 'read file path text to function name     [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #f%     [KILL](/qb64wiki/index.php/KILL "KILL") file$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  

*Example 2:* Returns a [LONG](/qb64wiki/index.php/LONG "LONG") array byte size required for a certain sized graphics screen pixel area [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)").





| ``` [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a screen mode: ", mode% [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter image width: ", wide& [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter image depth: ", deep& IntegerArray& = ImageBufferSize&(wide&, deep&, mode%) \ 2 ' returns size of an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") array. [PRINT](/qb64wiki/index.php/PRINT "PRINT") IntegerArray& [END](/qb64wiki/index.php/END "END")  [DEFINT](/qb64wiki/index.php/DEFINT "DEFINT") A-Z FUNCTION ImageBufferSize& (Wide&, Deep&, ScreenMode%)     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") ScreenMode%         [CASE](/qb64wiki/index.php/CASE "CASE") 1: BPPlane = 2: Planes = 1         [CASE](/qb64wiki/index.php/CASE "CASE") 2, 3, 4, 11: BPPlane = 1: Planes = 1         [CASE](/qb64wiki/index.php/CASE "CASE") 7, 8, 9, 12: BPPlane = 1: Planes = 4         [CASE](/qb64wiki/index.php/CASE "CASE") 10: BPPlane = 1: Planes = 2         [CASE](/qb64wiki/index.php/CASE "CASE") 13: BPPlane = 8: Planes = 1         [CASE ELSE](/qb64wiki/index.php/CASE_ELSE "CASE ELSE"): BPPlane = 0     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     ImageBufferSize& = 4 + [INT](/qb64wiki/index.php/INT "INT")((Wide& * BPPlane + 7) / 8) * (Deep& * Planes) 'return the value to function name. [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Explanation:* Function calculates the array byte size required when you [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") an area of a graphics [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"). Each mode may require a different sized array. Since graphics uses [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") arrays, 2 byte elements, the size returned is divided by 2 in the IntegerArray& calculation function reference. Function returns only 4 for [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0 which is a text only mode.
  




## See also


* [SUB](/qb64wiki/index.php/SUB "SUB"), [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN")
* [EXIT](/qb64wiki/index.php/EXIT "EXIT") (statement), [END](/qb64wiki/index.php/END "END")
* [\_EXIT (function)](/qb64wiki/index.php/EXIT_(function) "EXIT (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FUNCTION&oldid=6773>"




## Navigation menu








### Search





















