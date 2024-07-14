


$DEBUG - QB64 Phoenix Edition Wiki








# $DEBUG



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**$DEBUG** is precompiler [metacommand](/qb64wiki/index.php/Metacommand "Metacommand"), which enables debugging features, allowing you to step through your code running line by line and to inspect variables and change their values in real time.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 $DEBUG Mode Operation](#$DEBUG_Mode_Operation) * [4 See also](#See_also) |
| --- |


## Syntax


$DEBUG
  




## Description


* **$DEBUG** injects extra code in the resulting binary, allowing the IDE to control the execution flow of your program.
* When **$DEBUG** is used, the IDE will connect to your running program using a local TCP/IP connection.
	+ You may get a prompt from your Operating System regarding this, so it may be necessary to allow the IDE to receive connections.
	+ No external connections are created, and your running program will only attempt to connect locally to the IDE.
* The default TCP/IP port starts at 9001. Multiple running instances of the IDE will attempt to open ports 9002 and up.
	+ You can change the base port in the Debug menu.
* The metacommand is supposed to be removed once your program is ready for release, although leaving it in won't have any effect if your program isn't run from the IDE.
	+ The only drawback of leaving the metacommand in is that your binary will end up being larger than required.


  




## $DEBUG Mode Operation


* To start execution in pause mode, you can use **F7** or **F8**.
* There will be an arrow next to the line number where execution is paused, indicating the next line that will be run.
* When you enable **$DEBUG** mode, you can set breakpoints by clicking the line number at which you wish to stop execution. This can also be achieved by using the **F9** key.
	+ Breakpoints are indicated by a red dot next to the line number.
	+ To clear all breakpoints, hit **F10**.
* To skip a line during execution, shift-click a line number
	+ Lines marked for skipping are indicated by an exclamation mark next to the line number.
* **F4** opens the Variable List dialog, which allows you to add variables to the Watch List.
* During execution, the Variable List dialog also allows you to set the values of variables and also to create Watchpoints.
* Watchpoints halt execution, similarly to breakpoints, but do so when a variable matches the condition you specify.
	+ You can use relational operators (=, <>, >=, <=, >, <) to create watchpoint conditions.
* After a breakpoint or a watchpoint is reached, **F5** can be used to continue execution.
* **F6** can be used when the execution pointer is inside a sub/function. When used, execution will proceed until the procedure is ended.
* **F7** can be used to run line by line, and can be used to debug code inside subs/functions (Step Into).
* **F8** can be used to run line by line without entering sub/function calls (Step Over).
* **F12** can be used to show the current call stack (which procedure calls led to the current line).


  




## See also


* [Metacommands](/qb64wiki/index.php/Metacommand "Metacommand")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$DEBUG&oldid=7476>"




## Navigation menu








### Search





















