


\_SNDCLOSE - QB64 Phoenix Edition Wiki








# \_SNDCLOSE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDCLOSE statement frees and unloads an open sound using a [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY") handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


\_SNDCLOSE *handle&*
  




## Description


* If the sound is still playing, it will be freed automatically after it finishes.
	+ Closing a looping/paused/etc. sound means it is never freed until the QB64 program terminates.
* When your QB64 program terminates, all sounds are automatically freed.


  




## See also


* [\_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP"), [\_SNDPAUSE](/qb64wiki/index.php/SNDPAUSE "SNDPAUSE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDCLOSE&oldid=7674>"




## Navigation menu








### Search





















