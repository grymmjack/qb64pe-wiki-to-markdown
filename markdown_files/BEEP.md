


BEEP - QB64 Phoenix Edition Wiki








# BEEP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The BEEP statement produces a beep sound through the sound card.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) 	+ [2.1 QBasic/QuickBASIC](#QBasic/QuickBASIC) * [3 See also](#See_also) |
| --- |


## Syntax


BEEP
  




## Description


* BEEP can be placed anywhere to alert the user that there is something to do or an error has occurred.
* **QB64** produces the actual "beep" sound through the PC's sound card, to emulate QBasic's beeping through the [PC speaker](https://en.wikipedia.org/wiki/PC_speaker "wikipedia:PC speaker").


### QBasic/QuickBASIC


* Older programs may attempt to produce a BEEP by printing [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(7) to the screen. This is no longer supported in QB64 after **version 1.000**.
	+ You may have to replace instances of PRINT CHR$(7) in older programs to the BEEP statement to maintain the legacy functionality.


  




## See also


* [SOUND](/qb64wiki/index.php/SOUND "SOUND"), [PLAY](/qb64wiki/index.php/PLAY "PLAY")
* [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") (play sound files)
* [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW") (play frequency waves)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BEEP&oldid=8979>"




## Navigation menu








### Search





















