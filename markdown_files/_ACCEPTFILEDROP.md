


\_ACCEPTFILEDROP - QB64 Phoenix Edition Wiki








# \_ACCEPTFILEDROP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ACCEPTFILEDROP statement prepares a program window to receive files dropped from Windows Explorer in a drag/drop operation.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_ACCEPTFILEDROP [{ON|OFF}]
  




## Description


* Calling the statement with no parameters turns drag/dropping ON.
* To know when files have been dropped into your program's window, check that [\_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES") is greater than 0.
* Use [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") to read the list, either sequentially or by index.
* If using [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") with an index, you must call [\_FINISHDROP](/qb64wiki/index.php/FINISHDROP "FINISHDROP") after you finish working with the list.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* **Version 1.3 and up**.


  




## Examples


*Example:* Accepting files dragged from a folder and processing the list received sequentially.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(128, 25, 0)  _ACCEPTFILEDROP 'enables drag/drop functionality [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Drag files from a folder and drop them in this window..."  [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") [_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES") [THEN](/qb64wiki/index.php/THEN "THEN")         [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES")             a$ = [_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") 'reads the list sequentially; when the result is empty ("") it means the list is over             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [PRINT](/qb64wiki/index.php/PRINT "PRINT") i,             [IF](/qb64wiki/index.php/IF "IF") [_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")(a$) [THEN](/qb64wiki/index.php/THEN "THEN")                 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "file",             [ELSE](/qb64wiki/index.php/ELSE "ELSE")                 [IF](/qb64wiki/index.php/IF "IF") [_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")(a$) [THEN](/qb64wiki/index.php/THEN "THEN")                     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "folder",                 [ELSE](/qb64wiki/index.php/ELSE "ELSE")                     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "not found", 'highly unlikely, but who knows?                 [END IF](/qb64wiki/index.php/END_IF "END IF")             [END IF](/qb64wiki/index.php/END_IF "END IF")             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [END IF](/qb64wiki/index.php/END_IF "END IF")      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


  




## See also


* [\_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES"), [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE"), [\_FINISHDROP](/qb64wiki/index.php/FINISHDROP "FINISHDROP")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ACCEPTFILEDROP&oldid=8253>"




## Navigation menu








### Search





















