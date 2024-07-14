


\_LIMIT - QB64 Phoenix Edition Wiki








# \_LIMIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_LIMIT statement sets the loop repeat rate of a program to so many per second, relinquishing spare CPU cycles to other applications.


  






| Contents * [1 Syntax](#Syntax) * [2 Examples](#Examples) * [3 See also](#See_also) |
| --- |


## Syntax


\_LIMIT *framesPerSecond!*
  




* The *framesPerSecond!* [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") parameter value adjusts the loops per second of a program loop. **Do not use negative values.**
* The loop code is executed before the loop is delayed. Loop cycles below once per second may delay program [\_EXITs](/qb64wiki/index.php/EXIT "EXIT").
* \_LIMIT measures its interval from the previous time that it was called and minor adjustments are automatically made to ensure that the number of times a loop is repeated is correct overall.
* Loop cycle rates of 1000 or less can **significantly reduce CPU usage** in programs.
* Do not use it to limit a loop to **run less than once every 60 seconds** (i.e. \_LIMIT .0167 or \_LIMIT 1/60) or an [ILLEGAL FUNCTION CALL error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") will occur.
* Do not use \_LIMIT as a timing delay outside of loops. Use [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") instead.
* Use \_LIMIT to slow down old QBasic program loops that run too fast and use too much CPU.


  




## Examples


*Example:* Limits loop execution to 30 frames per second and limits the program's CPU usage.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "To Quit press ESC key!" [DO](/qb64wiki/index.php/DO "DO")     _LIMIT 30     [PRINT](/qb64wiki/index.php/PRINT "PRINT") [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(26);     [IF](/qb64wiki/index.php/IF "IF") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |




| ``` To Quit press ESC key! →→→→→→→→→→→→→→→→→→→→  ``` |
| --- |


*Note:* In the above example, \_LIMIT has to be within the loop.
  




## See also


* [\_DELAY](/qb64wiki/index.php/DELAY "DELAY")
* [TIMER](/qb64wiki/index.php/TIMER "TIMER"), [ON TIMER(n)](/qb64wiki/index.php/ON_TIMER(n) "ON TIMER(n)")
* [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LIMIT&oldid=8372>"




## Navigation menu








### Search





















