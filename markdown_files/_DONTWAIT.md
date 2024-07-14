


\_DONTWAIT - QB64 Phoenix Edition Wiki








# \_DONTWAIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_DONTWAIT is used with the [SHELL](/qb64wiki/index.php/SHELL "SHELL") statement in **QB64** to specify that the program shouldn't wait until the external command/program is finished (which it otherwise does by default).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[SHELL](/qb64wiki/index.php/SHELL "SHELL") [[[\_DONTWAIT] [*commandLine$*]
  




## Description


* Runs the command/program specified in *commandline$* and lets the calling program continue at the same time in its current screen format.
* Especially useful when CMD /C or START is used in a SHELL command line to run another program.
* **QB64** automatically uses CMD /C or COMMAND /C when using SHELL.
* **QB64** program screens will not get distorted or minimized like QBasic fullscreen modes would.


  




## Examples




| ``` [SHELL](/qb64wiki/index.php/SHELL "SHELL") _DONTWAIT "notepad " + filename$  [FOR](/qb64wiki/index.php/FOR "FOR") x = 1 [TO](/qb64wiki/index.php/TO "TO") 5     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 1     [PRINT](/qb64wiki/index.php/PRINT "PRINT") x [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |


(opens up notepad at the same time as counting to 5)





| ```  1  2  3  4  5  ``` |
| --- |


  




## See also


* [SHELL](/qb64wiki/index.php/SHELL "SHELL"), [\_HIDE](/qb64wiki/index.php/HIDE "HIDE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=DONTWAIT&oldid=8316>"




## Navigation menu








### Search





















