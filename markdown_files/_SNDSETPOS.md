


\_SNDSETPOS - QB64 Phoenix Edition Wiki








# \_SNDSETPOS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDSETPOS statement changes the current/starting playing position in seconds of a sound.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SNDSETPOS *handle&*, *position!*
  




## Description


* Changes the current/starting playing position in seconds (a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value) of a sound in memory.
* If *position!* is past the length of the sound, playback will be interrupted.
* Function cannot be called while a looping sound is being played (see [\_SNDLOOP](/qb64wiki/index.php/SNDLOOP "SNDLOOP")).
* In versions **prior to build 20170811/60**, the sound identified by *handle&* must have been opened using the ["SETPOS" capability](/qb64wiki/index.php/SNDOPEN "SNDOPEN") to use this statement.


  




## Examples


*Example:* To check the current playing position in an MP3 file, use [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") with [\_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS") printed in a loop





| ``` SoundFile& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("YourSoundFile.mp3") '<<< your MP3 sound file here! _SNDSETPOS SoundFile&, 5.5   'set to play sound 5 1/2 seconds into music [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") SoundFile&  'play sound Do: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60    LOCATE 5, 2: PRINT "Current play position> "; [_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS")(SoundFile&) LOOP UNTIL [_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")(27) OR [NOT](/qb64wiki/index.php/NOT "NOT") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(SoundFile&) 'ESC or end of sound exit  ``` |
| --- |


  




## See also


* [\_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS"), [\_SNDLEN](/qb64wiki/index.php/SNDLEN "SNDLEN")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDLIMIT](/qb64wiki/index.php/SNDLIMIT "SNDLIMIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDSETPOS&oldid=6259>"




## Navigation menu








### Search





















