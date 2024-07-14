


\_SNDGETPOS - QB64 Phoenix Edition Wiki








# \_SNDGETPOS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDGETPOS function returns the current playing position in seconds using a handle from [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*position* = \_SNDGETPOS(*handle&*)
  




## Description


* Returns the current playing position in seconds from an open sound file.
* If a sound isn't playing, it returns 0.
* If a sound is paused, it returns the paused position.
* For a looping sound, the value returned continues to increment and does not reset to 0 when the sound loops.
* In versions **prior to build 20170811/60**, the sound identified by *handle&* must have been opened using the ["SETPOS" capability](/qb64wiki/index.php/SNDOPEN "SNDOPEN") to use this function.


  




## Examples


*Example:* To check the current playing position in an MP3 file, use [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") with \_SNDGETPOS printed in a loop:





| ``` SoundFile& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("YourSoundFile.mp3") '<<< your MP3 sound file here! [_SNDSETPOS](/qb64wiki/index.php/SNDSETPOS "SNDSETPOS") SoundFile&, 5.5   'set to play sound 5 1/2 seconds into music [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") SoundFile&  'play sound Do: [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60    LOCATE 5, 2: PRINT "Current play position> "; _SNDGETPOS(SoundFile&) LOOP UNTIL [_KEYDOWN](/qb64wiki/index.php/KEYDOWN "KEYDOWN")(27) OR [NOT](/qb64wiki/index.php/NOT "NOT") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(SoundFile&) 'ESC or end of sound exit  ``` |
| --- |


  




## See also


* [\_SNDSETPOS](/qb64wiki/index.php/SNDSETPOS "SNDSETPOS")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDGETPOS&oldid=6245>"




## Navigation menu








### Search





















