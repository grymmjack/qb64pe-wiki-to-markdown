


\_SNDPLAYING - QB64 Phoenix Edition Wiki








# \_SNDPLAYING



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDPLAYING function returns whether a sound is being played. Uses a handle from the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY") functions.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*isPlaying%* = \_SNDPLAYING(*handle&*)
  




## Description


* Returns false (0) if a sound is not playing or true (-1) if it is.
* If a sound is paused, \_SNDPLAYING returns 0.


  




## Examples




| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") _SNDPLAYING(h&)  ``` |
| --- |


  




## See also


* [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY"), [\_SNDPAUSE](/qb64wiki/index.php/SNDPAUSE "SNDPAUSE"), [\_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP")
* [\_SNDPAUSED](/qb64wiki/index.php/SNDPAUSED "SNDPAUSED")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDPLAYING&oldid=6255>"




## Navigation menu








### Search





















