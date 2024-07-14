


\_SNDLIMIT - QB64 Phoenix Edition Wiki








# \_SNDLIMIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDLIMIT statement stops playing a sound after it has been playing for a set number of seconds.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_SNDLIMIT *handle&*, *numberOfSeconds!*
  




## Parameters


* The *handle&* variable name is created using the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function from a loaded sound file.
* *numberOfSeconds!* is a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value of seconds that the sound will play.


  




## Description


* Sets how long a sound will be played in seconds. If the limit is set after the sound is started, the timer starts counting down from when the limit is applied, not from the start of playing.
* Set *numberOfSeconds!* to 0 seconds to remove the limit.
* Pausing or stopping the sound will also remove the limit.


  




## Examples




| ``` _SNDLIMIT h&, 5.5  ``` |
| --- |


  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDLEN](/qb64wiki/index.php/SNDLEN "SNDLEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDLIMIT&oldid=6540>"




## Navigation menu








### Search





















