


\_SNDPLAYFILE - QB64 Phoenix Edition Wiki








# \_SNDPLAYFILE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDPLAYFILE statement is used to play a sound file without generating a handle, automatically closing it after playback finishes.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SNDPLAYFILE *filename$*[, *ignored%*][, *volume!*]
  




## Description


* Supported file formats are **WAV, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD or RAD (v2 only)**. See [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN").
* *ignored%* is an optional parameter , accepted for historical reasons.
	+ In versions prior to **build 20170811/60**, *ignored%* identified if a sound was to be loaded with ["SYNC" capabilities](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), (-1 for true, 0 for false). This is true for all sound files in the latest versions, making this parameter safe to be ignored.
* *volume!* is a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value from 0 (silence) to 1 (full volume). If not used or outside this range, the sound will be played at full volume.
* \_SNDPLAYFILE never creates an error. If the sound cannot be played it takes no further action.
* The sound is closed automatically after it finishes playing.
* When a sound will be used often, open the file with [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") and use [\_SNDPLAYCOPY](/qb64wiki/index.php/SNDPLAYCOPY "SNDPLAYCOPY") to play the handle instead to reduce the burden on the computer.


  




## Examples


*Example:* Playing a sound file at half volume.





| ``` _SNDPLAYFILE "dog.wav", , .5  ``` |
| --- |


  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY")
* [\_SNDPLAYCOPY](/qb64wiki/index.php/SNDPLAYCOPY "SNDPLAYCOPY")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDPLAYFILE&oldid=6254>"




## Navigation menu








### Search





















