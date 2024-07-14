


NEXT - QB64 Phoenix Edition Wiki








# NEXT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
NEXT is used in a [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") counter loop to progress through the loop count.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[FOR](/qb64wiki/index.php/FOR "FOR") *counterVariable* = *startValue* [TO](/qb64wiki/index.php/TO "TO") *stopValue* [[[STEP *increment*]
*{code}*
⋮
NEXT [*counterVariable*]
  




## Description


* NEXT is required in a FOR loop or a ["FOR without NEXT" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* The FOR variable name is not required after NEXT.
* NEXT can be grouped with other NEXTs in nested FOR loops using colons like NEXT: NEXT
* NEXT can also end more than one nested [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") loop using comma separated variables like NEXT j, i
* NEXT increases the FOR loop count, so after the loop is over the counterVariable's value will be stopValue + 1 (or stopValue + increment).
* NEXT is also used with the [RESUME](/qb64wiki/index.php/RESUME "RESUME") statement.


  




## Examples


*Example:* Finding the FOR variable value AFTER a simple counter loop to 10.





| ``` FOR i = 1 TO 10 PRINT i; NEXT i  PRINT "AFTER the LOOP, NEXT makes the value of i ="; i  ``` |
| --- |




| ``` 1 2 3 4 5 6 7 8 9 10 AFTER the LOOP, NEXT makes the value of i = 11  ``` |
| --- |


*Result:* The last value of i = 11 although FOR only looped 10 times. **Only use the count values while inside of the loop or compensate for this behavior in your code.**


  




## See also


* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")
* [DO...LOOP](/qb64wiki/index.php/DO...LOOP "DO...LOOP")
* [RESUME NEXT](/qb64wiki/index.php/RESUME "RESUME")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=NEXT&oldid=6599>"




## Navigation menu








### Search





















