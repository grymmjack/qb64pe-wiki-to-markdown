


\_SNDVOL - QB64 Phoenix Edition Wiki








# \_SNDVOL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDVOL statement sets the volume of a sound loaded in memory using a handle from the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SNDVOL *handle&*, *volume!*
  




## Description


* *volume!* is a value from 0 (silence) to 1 (full volume).
* In versions **prior to build 20170811/60**, the sound identified by *handle&* must have been opened using the ["VOL" capability](/qb64wiki/index.php/SNDOPEN "SNDOPEN") to use this function.
* Version **3.1.0** enables this for **"raw"** sounds.


  




## Examples




| ``` h& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("bell.wav") _SNDVOL h&, 0.5 [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") h&  ``` |
| --- |


  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDOPENRAW](/qb64wiki/index.php/SNDOPENRAW "SNDOPENRAW")
* [\_SNDBAL](/qb64wiki/index.php/SNDBAL "SNDBAL")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDVOL&oldid=8589>"




## Navigation menu








### Search





















