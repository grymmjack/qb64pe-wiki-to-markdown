


\_TOTALDROPPEDFILES - QB64 Phoenix Edition Wiki








# \_TOTALDROPPEDFILES



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_TOTALDROPPEDFILES function returns the number of items (files or folders) dropped in a program's window after [\_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP") is enabled.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*totalFilesReceived&* = \_TOTALDROPPEDFILES
  




## Description


* After [\_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP") is enabled, \_TOTALDROPPEDFILES will return 0 until the user drops files or folders into the program's window.
* When using [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") to read the list sequentially, \_TOTALDROPPEDFILES will be reset to 0 after the last item is retrieved (after [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") returns an empty string "").
* If using [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") with an index, you must call [\_FINISHDROP](/qb64wiki/index.php/FINISHDROP "FINISHDROP") after you finish working with the list.
* When using [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") to read the list with an index, \_TOTALDROPPEDFILES will **not** be reset (and the list of items won't be cleared) until [\_FINISHDROP](/qb64wiki/index.php/FINISHDROP "FINISHDROP") is called.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* **QB64 v1.3 and up**
* **QB64-PE all versions**


  




## Examples


* See example for [\_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP")


  




## See also


* [\_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP"), [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE"), [\_FINISHDROP](/qb64wiki/index.php/FINISHDROP "FINISHDROP")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=TOTALDROPPEDFILES&oldid=7452>"




## Navigation menu








### Search





















