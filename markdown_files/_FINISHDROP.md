


\_FINISHDROP - QB64 Phoenix Edition Wiki








# \_FINISHDROP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_FINISHDROP statement resets [\_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES") and clears the [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") list of items (files/folders).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


\_FINISHDROP
  




## Description


* When using [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE") with an index (which goes from 1 to [\_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES")), you must call \_FINISHDROP after you finish working with the list in order to prepare for the next drag/drop operation.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* **Version 1.3 and up**.


  




## Examples


*Example:* Accepting files dragged from a folder and processing the list received by specifying an index.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(128, 25, 0)  [_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP") 'enables drag/drop functionality [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Drag files from a folder and drop them in this window..."  [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") [_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES") [THEN](/qb64wiki/index.php/THEN "THEN")         [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") [_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES")             a$ = [_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE")(i)             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [PRINT](/qb64wiki/index.php/PRINT "PRINT") i,             [IF](/qb64wiki/index.php/IF "IF") [_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS")(a$) [THEN](/qb64wiki/index.php/THEN "THEN")                 [COLOR](/qb64wiki/index.php/COLOR "COLOR") 2: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "file",             [ELSE](/qb64wiki/index.php/ELSE "ELSE")                 [IF](/qb64wiki/index.php/IF "IF") [_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")(a$) [THEN](/qb64wiki/index.php/THEN "THEN")                     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 3: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "folder",                 [ELSE](/qb64wiki/index.php/ELSE "ELSE")                     [COLOR](/qb64wiki/index.php/COLOR "COLOR") 4: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "not found", 'highly unlikely, but who knows?                 [END IF](/qb64wiki/index.php/END_IF "END IF")             [END IF](/qb64wiki/index.php/END_IF "END IF")             [COLOR](/qb64wiki/index.php/COLOR "COLOR") 15             [PRINT](/qb64wiki/index.php/PRINT "PRINT") a$         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         _FINISHDROP 'If _FINISHDROP isn't called here then _TOTALDROPPEDFILES never gets reset.     [END IF](/qb64wiki/index.php/END_IF "END IF")      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


  




## See also


* [\_ACCEPTFILEDROP](/qb64wiki/index.php/ACCEPTFILEDROP "ACCEPTFILEDROP"), [\_TOTALDROPPEDFILES](/qb64wiki/index.php/TOTALDROPPEDFILES "TOTALDROPPEDFILES"), [\_DROPPEDFILE](/qb64wiki/index.php/DROPPEDFILE "DROPPEDFILE")
* [\_FILEEXISTS](/qb64wiki/index.php/FILEEXISTS "FILEEXISTS"), [\_DIREXISTS](/qb64wiki/index.php/DIREXISTS "DIREXISTS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=FINISHDROP&oldid=8333>"




## Navigation menu








### Search





















