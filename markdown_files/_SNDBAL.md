


\_SNDBAL - QB64 Phoenix Edition Wiki








# \_SNDBAL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDBAL statement attempts to set the balance or 3D position of a sound.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_SNDBAL *handle&*[, *x!*][, *y!*][, *z!*][, *channel&*]
  




## Parameters


* *handle&* is a valid sound handle created by the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function.
* *x!* distance values go from left (negative) to right (positive).
* *y!* distance values go from below (negative) to above (positive).
* *z!* distance values go from behind (negative) to in front (positive).
* *channel&* value 1 denotes left (mono) and 2 denotes right (stereo) channel (beginning with **build 20170811/60**)
	+ The ability to set the balance per channel is gone in version **3.1.0** and higher.


  




## Description


* Attempts to position a sound in 3D space, or as close to it as the underlying software libraries allow. In some cases, this will be true 3D positioning, in others, a mere volume adjustment based on distance alone.
* Omitted x!, y! or z! [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") values are set to 0 or not changed in **build 20170811/60 onward**.
* By setting the x! value to -1 or 1 it plays the sound at full volume from the appropriate speaker.
* Sounds at a distance of 1 or -1 are played at full volume. Sounds further than a distance of 1000 cannot be heard.
* The volume decreases linearly (at a constant gradient) over distance. Half volume = 500.
* An "**Illegal Function Call**" error can occur if another sound is using the primary or same channel position.
* Opened sound files must have the ["VOL"](/qb64wiki/index.php/SNDOPEN "SNDOPEN") capability to use this statement in versions **before build 20170811/60.**
* Version **3.1.0** enables this for **"raw"** sounds.


  




## Examples


*Example 1:* This example loads, plays, and then bounces the sound between the left and right channels.





| ``` ' This examples load, plays and then bounces the sound between the left and right channels Laff& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("KONGlaff.ogg", "stream") 'load sound file and get LONG handle value [IF](/qb64wiki/index.php/IF "IF") Laff& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") Laff& 'play sound [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to load sound file."     [END](/qb64wiki/index.php/END "END") [END](/qb64wiki/index.php/END "END") [IF](/qb64wiki/index.php/IF "IF")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Press ESC to stop." dir = 0.01 [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") laffx! <= -1 [THEN](/qb64wiki/index.php/THEN "THEN") dir = 0.01     [IF](/qb64wiki/index.php/IF "IF") laffx! >= 1 [THEN](/qb64wiki/index.php/THEN "THEN") dir = -0.01     laffx! = laffx! + dir      [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") , 1: [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "Balance = ##.##"; laffx!;     _SNDBAL Laff&, laffx! 'balance sound to left or right speaker      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [WHILE](/qb64wiki/index.php/WHILE "WHILE") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(Laff&) [AND](/qb64wiki/index.php/AND "AND") [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT") <> 27  ``` |
| --- |


  

*Example:* Loading a sound after **build 20170811/60** - no need to specify "sound capabilities" in [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN").





| ``` s& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("song.ogg") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[READ](/qb64wiki/index.php/READ "READ")Y"; s& [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") s& [_SNDLOOP](/qb64wiki/index.php/SNDLOOP "SNDLOOP") s&   xleft = -1 xright = 1 DO     k$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     [SELECT CASE](/qb64wiki/index.php/SELECT_CASE "SELECT CASE") k$         [CASE](/qb64wiki/index.php/CASE "CASE") "f"             xleft = xleft - 0.1             _SNDBAL s&, xleft, , , 1         [CASE](/qb64wiki/index.php/CASE "CASE") "g"             xleft = xleft + 0.1             _SNDBAL s&, xleft, , , 1         [CASE](/qb64wiki/index.php/CASE "CASE") "h"             xright = xright - 0.1             _SNDBAL s&, xright, , , 2         [CASE](/qb64wiki/index.php/CASE "CASE") "j"             xright = xright + 0.1             _SNDBAL s&, xright, , , 2         [CASE](/qb64wiki/index.php/CASE "CASE") "n"             volume = volume - 0.1             [_SNDVOL](/qb64wiki/index.php/SNDVOL "SNDVOL") s&, volume         [CASE](/qb64wiki/index.php/CASE "CASE") "m"             volume = volume + 0.1             [_SNDVOL](/qb64wiki/index.php/SNDVOL "SNDVOL") s&, volume         [CASE](/qb64wiki/index.php/CASE "CASE") "p"             [_SNDPAUSE](/qb64wiki/index.php/SNDPAUSE "SNDPAUSE") s&         [CASE](/qb64wiki/index.php/CASE "CASE") " "             [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") s&         [CASE](/qb64wiki/index.php/CASE "CASE") "i"             [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_SNDPLAYING](/qb64wiki/index.php/SNDPLAYING "SNDPLAYING")(s&)             [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_SNDPAUSED](/qb64wiki/index.php/SNDPAUSED "SNDPAUSED")(s&)             [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")         [CASE](/qb64wiki/index.php/CASE "CASE") "b"             [_SNDSETPOS](/qb64wiki/index.php/SNDSETPOS "SNDSETPOS") s&, 110         [CASE](/qb64wiki/index.php/CASE "CASE") "l"             [_SNDLIMIT](/qb64wiki/index.php/SNDLIMIT "SNDLIMIT") s&, 10             [PRINT](/qb64wiki/index.php/PRINT "PRINT") "LIM"             [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")         [CASE](/qb64wiki/index.php/CASE "CASE") "k"             [_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP") s&         [CASE](/qb64wiki/index.php/CASE "CASE") "c"             [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") s&             [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")             s2& = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("song.ogg")         [CASE](/qb64wiki/index.php/CASE "CASE") "d"             s2& = [_SNDCOPY](/qb64wiki/index.php/SNDCOPY "SNDCOPY")(s&)             [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") s2&     [END SELECT](/qb64wiki/index.php/END_SELECT "END SELECT")     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1     [PRINT](/qb64wiki/index.php/PRINT "PRINT") xleft, xright, volume, [_SNDGETPOS](/qb64wiki/index.php/SNDGETPOS "SNDGETPOS")(s&); "   " LOOP  ``` |
| --- |


Code by Johny B
  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDOPENRAW](/qb64wiki/index.php/SNDOPENRAW "SNDOPENRAW")
* [\_SNDVOL](/qb64wiki/index.php/SNDVOL "SNDVOL"), [\_SNDLIMIT](/qb64wiki/index.php/SNDLIMIT "SNDLIMIT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDBAL&oldid=8590>"




## Navigation menu








### Search





















