


\_SNDCOPY - QB64 Phoenix Edition Wiki








# \_SNDCOPY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDCOPY function copies a sound to a new handle so that two or more of the same sound can be played at once. The passed handle parameter is from the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*copyHandle&* = \_SNDCOPY(*handle&*)
  




## Description


* Returns a new handle to the a copy in memory of the sound data referred to by the source handle.
* No changes to the source handle (such as a volume change) are inherited.
* The sound data referred to by the handle and its copies are not freed until all of them are closed.
* In versions **prior to build 20170811/60**, the sound identified by *handle&* must have been opened using the ["SYNC" capability](/qb64wiki/index.php/SNDOPEN "SNDOPEN") to use this function.


  




## See also


* [\_SNDPLAYCOPY](/qb64wiki/index.php/SNDPLAYCOPY "SNDPLAYCOPY")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDCOPY&oldid=381>"




## Navigation menu








### Search





















