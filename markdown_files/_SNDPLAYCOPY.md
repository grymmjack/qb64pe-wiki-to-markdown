


\_SNDPLAYCOPY - QB64 Phoenix Edition Wiki








# \_SNDPLAYCOPY



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDPLAYCOPY statement copies a sound, plays it, and automatically closes the copy using a handle parameter passed from [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") or [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY")


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_SNDPLAYCOPY *handle&*[, [*volume!*][, *x!*][, *y!*][, *z!*
  




## Parameters


* The [LONG](/qb64wiki/index.php/LONG "LONG") *handle&* value is returned by [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") using a specific sound file.
* The *volume!* parameter can be any [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value from 0 (no volume) to 1 (full volume).
* *x!* distance values go from left (negative) to right (positive) (beginning with **v3.3.x**).
* *y!* distance values go from below (negative) to above (positive) (beginning with **v3.3.x**).
* *z!* distance values go from behind (negative) to in front (positive) (beginning with **v3.3.x**).


  




## Description


* Makes coding easier by doing all of the following automatically:


1. Copies/duplicates the source handle (see [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY")).
2. Changes the volume of the copy if volume is passed.
3. Applies stereo panning or a 3D position if x, y, z is passed.
4. Plays the copy.
5. Closes the copy.

* This statement is a better choice than [\_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE") if the sound will be played often, reducing the burden on the computer.
* By setting the x! value to -1 or 1 it plays the sound at full volume from the appropriate speaker.
* Omitted x!, y! or z! values are set to 0.


  




## Examples


*Example 1:* Playing a previously opened sound from left and right speakers.





| ``` [DIM](/qb64wiki/index.php/DIM "DIM") [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") h, i  h = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("explosion.wav")  [IF](/qb64wiki/index.php/IF "IF") h > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [FOR](/qb64wiki/index.php/FOR "FOR") i = 0 [TO](/qb64wiki/index.php/TO "TO") 9         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 1          [IF](/qb64wiki/index.php/IF "IF") i [MOD](/qb64wiki/index.php/MOD "MOD") 2 = 0 [THEN](/qb64wiki/index.php/THEN "THEN")             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Playing from right"             _SNDPLAYCOPY h, , 1         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Playing from left"             _SNDPLAYCOPY h, , -1         [END IF](/qb64wiki/index.php/END_IF "END IF")     [NEXT](/qb64wiki/index.php/NEXT "NEXT") [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


  

*Example 2:* Playing a sound at random volumes.





| ``` chomp& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("chomp.wav") [IF](/qb64wiki/index.php/IF "IF") chomp& > 0 [THEN](/qb64wiki/index.php/THEN "THEN") _SNDPLAYCOPY chomp&, 0.5 + [RND](/qb64wiki/index.php/RND "RND") * 0.49  ``` |
| --- |


  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")
* [\_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY")
* [\_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDPLAYCOPY&oldid=7416>"




## Navigation menu








### Search





















