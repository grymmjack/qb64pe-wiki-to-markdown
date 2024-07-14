


\_INSTRREV - QB64 Phoenix Edition Wiki








# \_INSTRREV



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_INSTRREV function searches for a substring inside another string, but unlike [INSTR](/qb64wiki/index.php/INSTR "INSTR") it searches from right to left.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*position%* = \_INSTRREV([*start%*,] *baseString$*, *subString$*)
  




## Parameters


* The optional literal or variable [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *start%* indicates where in the *baseString$* the search must start, counted from the left.
* The *baseString$* is a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value to be searched for an exact match including [letter cases](/qb64wiki/index.php/UCASE$ "UCASE$").
* The *subString$* is a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value being searched.


  




## Description


* The function returns the *position%* in the *baseString$* where the *subString$* was found, from right to left.
* *position%* will be 0 if the search found no matches in the base string.
* \_INSTRREV returns 0 if an empty *baseString$* is passed, and returns [LEN](/qb64wiki/index.php/LEN "LEN")(*baseString$*) with an empty *subString$*.
* The *start%* position is useful when making multiple searches in the same string. See the example below.
* The *subString$* should be smaller or equal in [length](/qb64wiki/index.php/LEN "LEN") to the *baseString$*, or 0 is returned.
* A *start%* value of 0 or less starts search from the end of the *baseString$* (same as not passing a *start%* parameter).


  




## Examples


*Example 1:* Separating a file name from a full path.





| ``` fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o" file$ = [MID$](/qb64wiki/index.php/MID$_(function) "MID$ (function)")(fullPath$, _INSTRREV(fullPath$, "\") + 1) [PRINT](/qb64wiki/index.php/PRINT "PRINT") file$  ``` |
| --- |




| ``` libqb_1_2_000000000000.o  ``` |
| --- |


  

*Example 2:* Searching for multiple instances of a substring inside a base string, going from the end to the start.





| ``` sentence$ = " This is a string full of spaces, including at start and end... " [PRINT](/qb64wiki/index.php/PRINT "PRINT") sentence$ [DO](/qb64wiki/index.php/DO "DO")     findPrevSpace% = _INSTRREV(findPrevSpace% - 1, sentence$, [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")(1))     [IF](/qb64wiki/index.php/IF "IF") findPrevSpace% = 0 [THEN](/qb64wiki/index.php/THEN "THEN")         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 4, 1         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "No more spaces"         [EXIT](/qb64wiki/index.php/EXIT "EXIT") [DO](/qb64wiki/index.php/DO "DO")     [END IF](/qb64wiki/index.php/END_IF "END IF")      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, findPrevSpace%     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "^"     totalSpaces = totalSpaces + 1      [IF](/qb64wiki/index.php/IF "IF") findPrevSpace% = 1 [THEN](/qb64wiki/index.php/THEN "THEN")         [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 4, 1         [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Last space found at position 1"         [EXIT](/qb64wiki/index.php/EXIT "EXIT") [DO](/qb64wiki/index.php/DO "DO")     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Total spaces found: "; totalSpaces  ``` |
| --- |




| ```  This is a string full of spaces, including at start and end... ^    ^  ^ ^      ^    ^  ^       ^         ^  ^     ^   ^      ^  Last space found at position 1 Total spaces found: 13  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1269)
* [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)"), [INSTR](/qb64wiki/index.php/INSTR "INSTR")
* [SPACE$](/qb64wiki/index.php/SPACE$ "SPACE$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INSTRREV&oldid=8920>"




## Navigation menu








### Search





















