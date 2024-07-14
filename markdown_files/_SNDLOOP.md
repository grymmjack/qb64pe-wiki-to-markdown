


\_SNDLOOP - QB64 Phoenix Edition Wiki








# \_SNDLOOP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SNDLOOP statement is like [\_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") but the sound is looped. Uses a handle from the [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SNDLOOP *handle&*
  




## Description


* Plays the sound identified by *handle&* in a loop.


  




## Examples


*Example:* Loading a sound or music file and playing it in a loop until a key is pressed.





| ``` bg = [_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")("back.ogg") '<<<<<<<<<< change to your sound file name _SNDLOOP bg  DO     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 10   'keep CPU resources used low [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" 'key press program exit [_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP") bg [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") bg  ``` |
| --- |


  




## See also


* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDSTOP](/qb64wiki/index.php/SNDSTOP "SNDSTOP")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDLOOP&oldid=6247>"




## Navigation menu








### Search





















