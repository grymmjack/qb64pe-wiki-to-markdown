


INSTR - QB64 Phoenix Edition Wiki








# INSTR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The INSTR function searches for the first occurence of a search [STRING](/qb64wiki/index.php/STRING "STRING") within a base string and returns the position it was found.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) 	+ [3.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*position%* = INSTR([*start%*,] *baseString$*, *searchString$*)
  




## Parameters


* The optional literal or variable [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") *start%* indicates where in the *baseString$* the search must start.
* The *baseString$* is a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value to be searched for an exact match including [letter cases](/qb64wiki/index.php/UCASE$ "UCASE$").
* The *searchString$* is a literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") value being searched.


  




## Description


* The function returns the *position%* in the *baseString$* where the *searchString$* was found.
* *position%* will be 0 if the search found no matches in the base string.
* INSTR returns 0 if an empty *baseString$* is passed, and returns 1 with an empty *searchString$*.
* The *start%* position is useful when making multiple searches in the same string. See the example below.
* The *searchString$* should be smaller or equal in [length](/qb64wiki/index.php/LEN "LEN") to the *baseString$*, or 0 is returned.
* Non-zero *position%* return values can be used as a new start position by adding 1 to re-search the base string. See the example below.
* In a loop, INSTR can search an entire file for occurences of certain words. See the [MID$](/qb64wiki/index.php/MID$ "MID$") statement example.


### QBasic/QuickBASIC


* The *start%* position had to be at least 1 or greater when used or there will be an [Illegal function call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error. In **QB64**, a *start%* value of 0 or negative is interpreted as 1 and doesn't generate an error.


  




## Examples


*Example:* Reading more than one instance of a word in a string using the INSTR return value as the start value plus 1.





| ``` text$ = "The cats and dogs where playing, even though dogs don't like cats." [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP")   findcats% = INSTR(findcats% + 1, text$, "cats") ' find another occurance after   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") findcats% [THEN](/qb64wiki/index.php/THEN "THEN") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "There is 'cats' in the string at position:"; findcats% [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") findcats% = 0  findmonkey% = INSTR(text$, "monkeys")  ' find any occurance? PRINT findmonkey%; "'monkeys' were found so it returned:"; findmonkey%  ``` |
| --- |




| ``` There is 'cats' in the string at position: 5 There is 'cats' in the string at position: 62  0 'monkeys' were found so INSTR returned: 0  ``` |
| --- |


*Explanation:* When the INSTR return value is 0 there are no more instances of a string in a string so the search loop is exited.
  




## See also


* [\_INSTRREV](/qb64wiki/index.php/INSTRREV "INSTRREV"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")
* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")
* [LCASE$](/qb64wiki/index.php/LCASE$ "LCASE$"), [UCASE$](/qb64wiki/index.php/UCASE$ "UCASE$")
* [STRING](/qb64wiki/index.php/STRING "STRING"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INSTR&oldid=8386>"




## Navigation menu








### Search





















