


SLEEP - QB64 Phoenix Edition Wiki








# SLEEP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
SLEEP pauses the program indefinitely or for a specified number of seconds, program is unpaused when the user presses a key or when the specified number of seconds has passed.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


SLEEP [seconds]
  




* Seconds are an optional [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value. If there is no parameter, then it waits for a keypress.
* Any user keypress will abort the SLEEP time.
* SLEEP does NOT clear the keyboard buffer so it can affect [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [INPUT](/qb64wiki/index.php/INPUT "INPUT"), [INPUT$](/qb64wiki/index.php/INPUT$ "INPUT$") and [LINE INPUT](/qb64wiki/index.php/LINE_INPUT "LINE INPUT") reads.
* Use an [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") keyboard buffer clearing loop when an empty keyboard buffer is necessary.
* SLEEP allows other programs to share the processor time during the interval.


  

*Example:*





| ``` [CLS](/qb64wiki/index.php/CLS "CLS") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press a key..." SLEEP [PRINT](/qb64wiki/index.php/PRINT "PRINT") "You pressed a key, now wait for 2 seconds." SLEEP 2 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "You've waited for 2 seconds." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "(or you pressed a key)"  ``` |
| --- |




| ``` Press a key... You pressed a key, now wait for 2 seconds. You've waited for 2 seconds. (or you pressed a key)  ``` |
| --- |


*Explanation:* SLEEP without any arguments waits until a key is pressed, next SLEEP statement uses the argument 2 which means that it will wait for 2 seconds, any number of seconds can be specified.
  




## See also


* [TIMER (function)](/qb64wiki/index.php/TIMER_(function) "TIMER (function)"), [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")
* [\_DELAY](/qb64wiki/index.php/DELAY "DELAY"), [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SLEEP&oldid=8062>"




## Navigation menu








### Search





















