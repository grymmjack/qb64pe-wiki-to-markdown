


\_READBIT - QB64 Phoenix Edition Wiki








# \_READBIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_READBIT function is used to check the state of a specified bit of a integer value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*result* = \_READBIT(*numericalVariable*, *numericalValue*)
  




## Parameters


* *numericalVariable* is the variable to read the state of a bit of and can be of the following types: [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG"), or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64").
* Integer values can be signed or [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED").
* *numericalValue* the number of the bit to be read.


  




## Description


* Used to check the current state of a bit in an integer value.
* Returns -1 if the bit is set(1), otherwise returns 0 if the bit is not set(0)
* Bits start at 0 (so a [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") has bits 0 to 7, [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") 0 to 15, and so on)


  




## Availability


* **Version 1.4 and up**.


  




## Examples


*Example 1:*





| ``` A~%% = [_SETBIT](/qb64wiki/index.php/SETBIT "SETBIT")(A~%%,4) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Bit 4 is currently "; IF _READBIT(A~%%,4) = -1 THEN [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ON" ELSE [PRINT](/qb64wiki/index.php/PRINT "PRINT") "OFF" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "And bit 2 is currently "; IF _READBIT(A~%%,2) = -1 THEN [PRINT](/qb64wiki/index.php/PRINT "PRINT") "ON" ELSE [PRINT](/qb64wiki/index.php/PRINT "PRINT") "OFF"  ``` |
| --- |




| ``` Bit 4 is currently ON And bit 2 is currently OFF  ``` |
| --- |


*Example 2:*





| ``` B& = 12589575 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "B& ="; B& FOR I%% = 31 TO 0 STEP -1 '32 bits for a [LONG](/qb64wiki/index.php/LONG "LONG") value  Binary$ = Binary$ + [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")([ABS](/qb64wiki/index.php/ABS "ABS")(_READBIT(B&, I%%)))) NEXT I%% [PRINT](/qb64wiki/index.php/PRINT "PRINT") "B& in binary is: "; Binary$ ``` |
| --- |




| ``` B& = 12589575 B& in binary is: 00000000110000000001101000000111  ``` |
| --- |


  




## See also


* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR"), [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG")
* [\_SETBIT](/qb64wiki/index.php/SETBIT "SETBIT"), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE"), [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64")
* [\_RESETBIT](/qb64wiki/index.php/RESETBIT "RESETBIT"), [\_TOGGLEBIT](/qb64wiki/index.php/TOGGLEBIT "TOGGLEBIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=READBIT&oldid=7384>"




## Navigation menu








### Search





















