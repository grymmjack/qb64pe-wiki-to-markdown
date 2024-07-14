


END - QB64 Phoenix Edition Wiki








# END



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The END statement terminates a program without an immediate exit or ends a procedure or statement block.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


END [*returnCode%*]
END [IF](/qb64wiki/index.php/IF...THEN "IF...THEN")
END [TYPE](/qb64wiki/index.php/TYPE "TYPE")
END [SELECT](/qb64wiki/index.php/SELECT_CASE "SELECT CASE")
END [SUB](/qb64wiki/index.php/SUB "SUB")
END [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION")
END [DECLARE](/qb64wiki/index.php/DECLARE_LIBRARY "DECLARE LIBRARY")
  




## Description


* In **QB64**, END can be followed by a code that can be read by another module using the [\_SHELL](/qb64wiki/index.php/SHELL_(function) "SHELL (function)") or [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE") function (known as [**errorlevel**](https://blogs.msdn.microsoft.com/oldnewthing/20080926-00/?p=20743))
* When END is used to end a program, there is a pause and the message "Press any key to continue..." is displayed at the bottom of the program's window.
* If the program does not use END or [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM"), the program will still end with a pause and display "Press any key to continue...".
* In **QB64**, [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") will end the program immediately and close the window.
* The **QB64** [\_EXIT (function)](/qb64wiki/index.php/EXIT_(function) "EXIT (function)") can block a user's Ctrl + Break key presses and clicks on the window's close button (X button) until the program is ready to close.


  




## Examples


*Example:* In QB64 you won't return to the IDE unless you are using it to run or edit the program module.





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello world!" END [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Hello no one!"  ``` |
| --- |


*Returns:*





| ``` Hello world!      Press any key to continue...  ``` |
| --- |


*Explanation:*"Hello no one!" isn't returned because the program ended with the END statement no matter what is after that.
The message "Press any key to continue..." is displayed after the program ends, both in QBasic and in **QB64**.
  




## See also


* [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM") (immediate exit)
* [SHELL (function)](/qb64wiki/index.php/SHELL_(function) "SHELL (function)"), [\_SHELLHIDE](/qb64wiki/index.php/SHELLHIDE "SHELLHIDE")
* [EXIT](/qb64wiki/index.php/EXIT "EXIT") (statement), [\_EXIT (function)](/qb64wiki/index.php/EXIT_(function) "EXIT (function)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=END&oldid=7869>"




## Navigation menu








### Search





















