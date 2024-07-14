


$EXEICON - QB64 Phoenix Edition Wiki








# $EXEICON



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**$EXEICON** pre-compiler metacommand embeds a designated icon file into the compiled EXE file to be viewed in Windows Explorer.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


$EXEICON**:**'*iconfile.ico*'
  




## Parameters


* **iconfile.ico** is a valid [ICO file](https://en.wikipedia.org/wiki/ICO_(file_format) "wikipedia:ICO (file format)")


  




## Description


* Calling [\_ICON](/qb64wiki/index.php/ICON "ICON") without an *imageHandle&* uses the embeded icon, if available.
	+ Starting with **build 20170906/64**, the window will automatically use the icon embedded by $EXEICON, without having to call \_ICON.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Examples


*Example:* Embeds a designated icon file into the compiled EXE which can be viewed in Windows Explorer folders.





| ``` $EXEICON:'mush.ico' [_ICON](/qb64wiki/index.php/ICON "ICON")  ``` |
| --- |


Code by Fellippe Heitor
  




## See also


* [\_ICON](/qb64wiki/index.php/ICON "ICON")
* [\_TITLE](/qb64wiki/index.php/TITLE "TITLE")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$EXEICON&oldid=8976>"




## Navigation menu








### Search





















