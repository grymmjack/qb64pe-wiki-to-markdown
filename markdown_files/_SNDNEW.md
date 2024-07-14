


\_SNDNEW - QB64 Phoenix Edition Wiki








# \_SNDNEW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_SNDNEW** function creates a raw empty sound in memory and returns a [LONG](/qb64wiki/index.php/LONG "LONG") handle value for later access.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*soundHandle&* = \_SNDNEW(*frames&*, *channels&*, *bits&*)
  




## Parameters


* *frames&* is the number of sample frames needed. The number needed for one second of sound is determined by your sound hardware's sample rate, hence you may use the following formula:
	+ frames& = [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE") \* neededSeconds! where you may also specify fractional seconds.
* *channels&* is the number of channels needed (1 = mono, 2 = stereo).
* *bits&* is the number of bits per channel (8 = 8-bit unsigned integer, 16 = 16-bit signed integer, 32 = 32-bit floating point).


  




## Description


* Use this function to create a raw sound in memory.
* Once the sound is created, it can be accessed and manipulated using the [\_MEM](/qb64wiki/index.php/MEM "MEM") interface statements and functions, mainly [\_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND"), [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET") & [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT").
* Using this function can generate sounds once programmatically and then play it multiple times.
* The sound memory can also be filled with sample data from other sources like files, [DATA](/qb64wiki/index.php/DATA "DATA") statements and more.
* Sound memory pointers obtained with [\_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND") must be freed using [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE") and the Sound handle value itself must be freed using [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") when no longer required.


  




## Availability


* **QB64-PE v3.5.0 and up**


  




## Examples


Example 1
Creating a sound at runtime and playing it.


| ``` [OPTION _EXPLICIT](/qb64wiki/index.php/OPTION_EXPLICIT "OPTION EXPLICIT")  [RANDOMIZE](/qb64wiki/index.php/RANDOMIZE "RANDOMIZE") [TIMER](/qb64wiki/index.php/TIMER_(function) "TIMER (function)")  [CONST](/qb64wiki/index.php/CONST "CONST") SOUND_DURATION = 5 ' duration is seconds [CONST](/qb64wiki/index.php/CONST "CONST") SAMPLE_CHANNELS = 1 ' number of channes. For stereo we need to add another _MEMPUT below and +offset by SAMPLE_BYTES [CONST](/qb64wiki/index.php/CONST "CONST") SAMPLE_BYTES = 4 ' number of bytes / sample (not frame!)  [DIM](/qb64wiki/index.php/DIM "DIM") h [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"): h = _SNDNEW(SOUND_DURATION * [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE"), SAMPLE_CHANNELS, SAMPLE_BYTES * 8) [IF](/qb64wiki/index.php/IF "IF") (h < 1) [THEN](/qb64wiki/index.php/THEN "THEN")     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to create sound!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [DIM](/qb64wiki/index.php/DIM "DIM") sndblk [AS](/qb64wiki/index.php/AS "AS") [_MEM](/qb64wiki/index.php/MEM "MEM"): sndblk = [_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND")(h, 0) [IF](/qb64wiki/index.php/IF "IF") sndblk.SIZE = 0 [THEN](/qb64wiki/index.php/THEN "THEN")     [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") h     [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Failed to access sound data!"     [END](/qb64wiki/index.php/END "END") [END IF](/qb64wiki/index.php/END_IF "END IF")  [DIM](/qb64wiki/index.php/DIM "DIM") t [AS](/qb64wiki/index.php/AS "AS") [_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") [FOR](/qb64wiki/index.php/FOR "FOR") t = 0 [TO](/qb64wiki/index.php/TO "TO") (SOUND_DURATION * [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")) - 1     [_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT") sndblk, sndblk.OFFSET + (t * SAMPLE_BYTES * SAMPLE_CHANNELS), [SIN](/qb64wiki/index.php/SIN "SIN")(2 * [_PI](/qb64wiki/index.php/PI "PI") * 440 * t / [_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")) + [RND](/qb64wiki/index.php/RND "RND") - [RND](/qb64wiki/index.php/RND "RND") [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") ' mixes noise and a sine wave [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [_SNDPLAY](/qb64wiki/index.php/SNDPLAY "SNDPLAY") h  [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP") SOUND_DURATION  [_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE") h  [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


  




## See also


* [\_MEM](/qb64wiki/index.php/MEM "MEM"), [\_MEMSOUND](/qb64wiki/index.php/MEMSOUND "MEMSOUND"), [\_MEMFREE](/qb64wiki/index.php/MEMFREE "MEMFREE")
* [\_MEMPUT](/qb64wiki/index.php/MEMPUT "MEMPUT"), [\_MEMGET](/qb64wiki/index.php/MEMGET "MEMGET"), [\_MEMGET (function)](/qb64wiki/index.php/MEMGET_(function) "MEMGET (function)")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN"), [\_SNDCLOSE](/qb64wiki/index.php/SNDCLOSE "SNDCLOSE"), [\_SNDRAW](/qb64wiki/index.php/SNDRAW "SNDRAW"), [\_SNDRATE](/qb64wiki/index.php/SNDRATE "SNDRATE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SNDNEW&oldid=8063>"




## Navigation menu








### Search





















