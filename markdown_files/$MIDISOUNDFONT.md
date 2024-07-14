


$MIDISOUNDFONT - QB64 Phoenix Edition Wiki








# $MIDISOUNDFONT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $MIDISOUNDFONT metacommand enables MIDI support for [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN").


**MIDI functionality is current unstable, and requires [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):MIDI to be able to use.**


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


$MIDISOUNDFONT: {DEFAULT|"*Filename*"}
  




## Parameters


* DEFAULT indicates that the soundfont provided by QB64-PE should be used to play MIDI files.
	+ The provided soundfont is about 1MB in size.
* *Filename* can be used to provide your own soundfont for playing MIDI files.
	+ The specified soundfont file is compiled into your program and is not required at runtime.


  




## Description


* The use of this metacommand allows [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN") to open MIDI files.
* The selected soundfont is what is used to play all MIDI files.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.2.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.2.0")

**v3.2.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples




| ``` [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):MIDI  ' This line is only allowed when [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):MIDI is used $MIDISOUNDFONT: Default  [_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE") "example.mid"  ``` |
| --- |




| ``` [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):MIDI  ' Using a custom soundfont rather than the default $MIDISOUNDFONT: "soundfont.sf2"  [_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE") "example.mid"  ``` |
| --- |


  




## See also


* [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE")
* [\_SNDOPEN](/qb64wiki/index.php/SNDOPEN "SNDOPEN")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$MIDISOUNDFONT&oldid=7799>"




## Navigation menu








### Search





















