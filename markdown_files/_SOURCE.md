


\_SOURCE - QB64 Phoenix Edition Wiki








# \_SOURCE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_SOURCE statement establishes the image SOURCE using a handle created by [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE"), [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE").


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) 	+ [3.1 More examples](#More_examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_SOURCE *handle&*
  




## Description


* The handle is a [LONG](/qb64wiki/index.php/LONG "LONG") integer value from the [\_SOURCE](/qb64wiki/index.php/SOURCE_(function) "SOURCE (function)") function or a handle created by [\_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE").
* If the handle is designated as 0, it refers to the current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.
* A source image can only supply information to a program. [POINT](/qb64wiki/index.php/POINT "POINT") and [GET](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)") might require a source other than the one currently active.


  




## Examples




| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 13 a = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(320,200,13) [_DEST](/qb64wiki/index.php/DEST "DEST") a [PSET](/qb64wiki/index.php/PSET "PSET") (100, 100), 15 _SOURCE a [_DEST](/qb64wiki/index.php/DEST "DEST") 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") [POINT](/qb64wiki/index.php/POINT "POINT")(100, 100)  ``` |
| --- |




| ```  15  ``` |
| --- |


*Explanation:* Create a new image with handle 'a', then use [\_DEST](/qb64wiki/index.php/DEST "DEST") to define the image to draw on. Draw a pixel then set the source to 'a' and use [POINT](/qb64wiki/index.php/POINT "POINT") to show what color is in that position. White (15) and is the color set with [PSET](/qb64wiki/index.php/PSET "PSET"). Use [\_DEST](/qb64wiki/index.php/DEST "DEST") 0 for the screen to display the results.
### More examples


* [Bitmaps](/qb64wiki/index.php/Bitmaps "Bitmaps")
* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")


  




## See also


* [\_DEST](/qb64wiki/index.php/DEST "DEST")
* [\_SOURCE (function)](/qb64wiki/index.php/SOURCE_(function) "SOURCE (function)")
* [POINT](/qb64wiki/index.php/POINT "POINT"), [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SOURCE&oldid=8674>"




## Navigation menu








### Search





















