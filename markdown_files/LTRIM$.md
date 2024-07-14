


LTRIM$ - QB64 Phoenix Edition Wiki








# LTRIM$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LTRIM$ function removes leading space characters from a [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*return$* = LTRIM$(*text$*)
  




## Description


* *text$* is the [STRING](/qb64wiki/index.php/STRING "STRING") value to trim.
* If *text$* contains no leading space characters, it is returned unchanged.
* Convert fixed length [STRING](/qb64wiki/index.php/STRING "STRING") values by using a different *return$* variable.
* Can be used to trim the leading space of a positive numerical value converted to a string value by [STR$](/qb64wiki/index.php/STR$ "STR$").


  




## Examples


*Example 1:* Trimming a positive string number.





| ``` value = 12345 number$ = LTRIM$([STR$](/qb64wiki/index.php/STR$ "STR$")(value)) 'converting number to string removes right PRINT space [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[" + number$ + "]"  ``` |
| --- |




| ``` [12345]  ``` |
| --- |


  

*Example 2:* Trimming leading spaces from text strings.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") LTRIM$("some text") [PRINT](/qb64wiki/index.php/PRINT "PRINT") LTRIM$("   some text")  ``` |
| --- |




| ``` some text some text  ``` |
| --- |


  

*Example 3:* A TRIM$ function to trim spaces off of both ends of a string.





| ``` text$ = "        Text String           " trimmed$ = TRIM$(text$) [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(26) + trimmed$ + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") TRIM$(text$) TRIM$ = LTRIM$([RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$")(text$)) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |




| ``` →Text String←  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1246)
* [\_TRIM$](/qb64wiki/index.php/TRIM$ "TRIM$"), [RTRIM$](/qb64wiki/index.php/RTRIM$ "RTRIM$"), [STR$](/qb64wiki/index.php/STR$ "STR$")
* [LEFT$](/qb64wiki/index.php/LEFT$ "LEFT$"), [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")
* [HEX$](/qb64wiki/index.php/HEX$ "HEX$"), [MID$ (function)](/qb64wiki/index.php/MID$_(function) "MID$ (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LTRIM$&oldid=8910>"




## Navigation menu








### Search





















