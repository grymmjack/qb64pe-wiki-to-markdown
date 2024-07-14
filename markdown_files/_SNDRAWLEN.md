


\_SNDRAWLEN - QB64 Phoenix Edition Wiki








# \_SNDRAWLEN



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDRAWLEN function returns the length, in seconds, of a [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW") sound currently queued.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*length#* = \_SNDRAWLEN [*pipeHandle&*]
  




## Parameters


* The optional *pipeHandle&* parameter refers to the sound pipe opened using [\_SNDOPENRAW](/qb64wiki/index.php/SNDOPENRAW "SNDOPENRAW").


  




## Description


* Use \_SNDRAWLEN to determine the length of a sound queue during creation and when to stop playing the sound.
* Ensure that \_SNDRAWLEN is comfortably above 0 (until you've actually finished playing sound).
* If you are getting occasional random clicks, this generally means that \_SNDRAWLEN has dropped to 0.
* The [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") determines how many samples are played per second. However, the timing is achieved by the sound card and \_SNDRAWLEN, not your program.
* **Do not attempt to use [\_TIMER](/qb64wiki/index.php/TIMER "TIMER") or [\_DELAY](/qb64wiki/index.php/DELAY "DELAY") or [\_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") to control the timing of [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW") sounds. You may use them as usual for delays or to limit your program's CPU usage, but the decision of how much sound to queue should only be based on the remaining \_SNDRAWLEN**.


  




## Examples


* See the example in [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")


  




## See also


* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW")
* [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDRAWLEN&oldid=6258>"




## Navigation menu








### Search





















