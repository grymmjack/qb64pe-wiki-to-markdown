


\_KEYCLEAR - QB64 Phoenix Edition Wiki








# \_KEYCLEAR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
\_KEYCLEAR clears all keyboard input buffers.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_KEYCLEAR [*buffer&*]
  




## Parameters


* *buffer&* indicates the buffer to be cleared:
	+ 1 - Clear the regular keyboard buffer, as used by all input command except the following: \_KEYHIT, \_KEYDOWN, INP(&H60. This is the same as the the emulated BIOS keyboard buffer, so legacy code reading from it via PEEK/POKE/CALL ABSOLUTE will also be affected.
	+ 2 - Clear the buffer used by \_KEYHIT.
	+ 3 - Clear INP(&H60) buffer. (see **Warning** in the the description below)
* If no parameter is passed, all three buffers are cleared.


  




## Description


* The **\_KEYCLEAR** command clears the specified keyboard input buffer. In effect, it is as if a loop has been used to read from the buffer until it is empty. All keys cleared are lost.
* **Warning:** The buffer read by INP(&H60) does not behave as the other buffers do. Whilst reading from the others will eventually empty after reading all data, this buffer will continue to return the last value. For this reason, \_KEYCLEAR is of little effect, but is included for completeness (an internal flag indicating new data on the port is cleared). However, using [INP](/qb64wiki/index.php/INP "INP") for anything is strongly discouraged, and is for backwards compatibility only.
* This command is best used just before getting input, in order to clear stray key presses from commands such as SLEEP, or just random keyboard bashing by the user. The programmer also ought to be aware of key release events in the \_KEYHIT buffer; consider the following code:




| ``` INPUT "Name: ", name$ _KEYCLEAR _DELAY 2 'Simulate doing some processing that takes some time. PRINT _KEYHIT  ``` |
| --- |


* The INPUT statement finishes as soon as the Enter key is struck; the program then proceeds to clear all input buffers. Because this is executed so quickly, it is likely that the user will release the Enter key after the \_KEYCLEAR command is executed, leaving a -13 (Enter key release) event in the \_KEYHIT buffer.
* As mentioned above, it is best to place the \_KEYCLEAR after the processing, immediately before the PRINT \_KEYHIT command:




| ``` INPUT "Name: ", name$ _DELAY 2 'Simulate doing some processing that takes some time. _KEYCLEAR PRINT _KEYHIT  ``` |
| --- |


  




## Examples


Example:





| ``` PRINT "Press a key" SLEEP 'Wait for keypress 'Three alternative _KEYCLEAR calls. Try uncommenting different ones to see the effect. '_KEYCLEAR '_KEYCLEAR 1 '_KEYCLEAR 2 PRINT "In regular buffer, there is "; INKEY$ 'read regular buffer PRINT "In _KEYHIT buffer, there is "; _KEYHIT 'read the _KEYHIT buffer  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1105)
* [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")
* [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$"), [\_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=KEYCLEAR&oldid=8886>"




## Navigation menu








### Search





















