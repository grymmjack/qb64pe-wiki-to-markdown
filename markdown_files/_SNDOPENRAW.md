


\_SNDOPENRAW - QB64 Phoenix Edition Wiki








# \_SNDOPENRAW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDOPENRAW function opens a new channel to fill with \_SNDRAW content to manage multiple dynamically generated sounds.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*pipeHandle&* = \_SNDOPENRAW
  




## Description


* You can manage multiple dynamically generated sounds at once without having to worry about mixing.
* Use [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") to remove the pipe sound handles from memory.


  




## Examples


*Example:* Combining 2 sounds without worrying about mixing:





| ``` a = _SNDOPENRAW b = _SNDOPENRAW  [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") x = 1 [TO](/qb64wiki/index.php/TO "TO") 100000     [_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW") [SIN](/qb64wiki/index.php/SIN "SIN")(x / 10), , a 'fill with a tone     [_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW") [RND](/qb64wiki/index.php/RND "RND") * 1 - 0.5, , b 'fill with static [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") a [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") b  ``` |
| --- |


Code by Galleon
  




## See also


* [\_SNDRAWDONE](/qb64wiki/index.php/SNDRAWDONE "SNDRAWDONE")
* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")
* [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDOPENRAW&oldid=7960>"




## Navigation menu








### Search





















