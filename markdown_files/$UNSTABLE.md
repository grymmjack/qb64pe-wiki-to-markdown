


$UNSTABLE - QB64 Phoenix Edition Wiki








# $UNSTABLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $UNSTABLE metacommand is used to enable the use of features that have not yet been made a permanent part of the language. Features hidden behind this metacommand may have breaking changes or be removed between releases.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


$UNSTABLE: {MIDI, HTTP}
  




## Parameters


* The current unstable features are as follows:
	+ **MIDI** allows usage of the [$MIDISOUNDFONT](/qb64wiki/index.php/$MIDISOUNDFONT "$MIDISOUNDFONT") metacommand
	+ **HTTP** allows opening HTTP connections using [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")


  




## Description


* $UNSTABLE exists as a way to allow usage of new language features before they are finalized as part of the language.
* Any languages features hidden behind $UNSTABLE may be changed in breaking ways in the next version of QB64-PE.
* Language features that become a permanent part of the language will no longer require $UNSTABLE to be used.
* More than one $UNSTABLE can be used in a program.


  




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


* MIDI keyword added in **QB64-PE v3.2.0**
* HTTP keyword added in **QB64-PE v3.5.0**


  




## Examples




| ``` $UNSTABLE:MIDI  ' This line is only allowed when $UNSTABLE:MIDI is used [$MIDISOUNDFONT](/qb64wiki/index.php/$MIDISOUNDFONT "$MIDISOUNDFONT"): Default  [_SNDPLAYFILE](/qb64wiki/index.php/SNDPLAYFILE "SNDPLAYFILE") "example.mid"  ``` |
| --- |


  




## See also


* [$MIDISOUNDFONT](/qb64wiki/index.php/$MIDISOUNDFONT "$MIDISOUNDFONT")
* [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$UNSTABLE&oldid=7802>"




## Navigation menu








### Search





















