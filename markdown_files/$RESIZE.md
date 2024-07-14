


$RESIZE - QB64 Phoenix Edition Wiki








# $RESIZE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $RESIZE [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") determines if a program window can be resized by the user.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


$RESIZE:{ON|OFF|STRETCH|SMOOTH}
  




## Description


* $RESIZE:ON is used to allow the program window to be resized by a program user. Otherwise it cannot be changed.
* $RESIZE:OFF (**default**) is used when the program's window size cannot be changed by the user.
* $RESIZE:STRETCH the screen will be stretched to fit the new window size with a 1 to 1 ratio of width and height.
* $RESIZE:SMOOTH the screen will be stretched also, but with linear filtering applied to the pixels.


  




## Availability


* [![v1.0](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.0")

**v1.0**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


*Example:* Resizing a program screen when the user changes it without clearing the entire screen image:





| ``` $RESIZE:ON  [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(160, 140, 32) [_DELAY](/qb64wiki/index.php/DELAY "DELAY") 0.1 [_SCREENMOVE](/qb64wiki/index.php/SCREENMOVE "SCREENMOVE") 20, 20 [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")  ' CLEAR _RESIZE FLAG BY READING IT ONCE temp& = [_RESIZE](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)")  DO      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60      [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") CheckResize([_SOURCE](/qb64wiki/index.php/SOURCE "SOURCE")) = -1 [THEN](/qb64wiki/index.php/THEN "THEN")         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 10             [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") ([RND](/qb64wiki/index.php/RND "RND") * [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(0) - 1, [RND](/qb64wiki/index.php/RND "RND") * [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(0) - 1), [RND](/qb64wiki/index.php/RND "RND") * 100 + 5, [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")([RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255)         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 1 [TO](/qb64wiki/index.php/TO "TO") 200             [PSET](/qb64wiki/index.php/PSET "PSET") ([RND](/qb64wiki/index.php/RND "RND") * [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(0) - 1, [RND](/qb64wiki/index.php/RND "RND") * [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(0) - 1), [_RGB32](/qb64wiki/index.php/RGB32 "RGB32")([RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255, [RND](/qb64wiki/index.php/RND "RND") * 255)         [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [END IF](/qb64wiki/index.php/END_IF "END IF")      [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")      k& = [_KEYHIT](/qb64wiki/index.php/KEYHIT "KEYHIT")  [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") k& = 27 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") k& = 32  [SYSTEM](/qb64wiki/index.php/SYSTEM "SYSTEM")    ' ************************************************************************************************* ' *                                                                                               * ' *  CheckResize: This FUNCTION checks if the user resized the window, and if so, recreates the   * ' *               ORIGINAL SCREEN image to the new window size.                                   * ' *                                                                                               * ' *               Developer Note: You must use $RESIZE:ON, $RESIZE:SMOOTH, or $RESIZE:SMOOTH at   * ' *                               the beginning of your project for this to work.                 * ' *                               This FUNCTION only works in QB64 version 1.000 and up.          * ' *                                                                                               * ' ************************************************************************************************* [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") CheckResize (CurrentScreen [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG"))      ' *** Define local variable for temporary screen     [DIM](/qb64wiki/index.php/DIM "DIM") TempScreen [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")      CheckResize = 0      ' *** Check to see if the user resized the window. If so, change the SCREEN image to the correct size.     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") [_RESIZE](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)") [THEN](/qb64wiki/index.php/THEN "THEN")          ' *** First, create a copy of the current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.         TempScreen = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(CurrentScreen, 32)          ' *** Set the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") to the copied image, releasing the current SCREEN image.         [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") TempScreen          ' *** Remove (FREE) the original [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.         [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") CurrentScreen          ' *** Create a new "original" [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.         CurrentScreen = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")([_RESIZEWIDTH](/qb64wiki/index.php/RESIZEWIDTH "RESIZEWIDTH"), [_RESIZEHEIGHT](/qb64wiki/index.php/RESIZEHEIGHT "RESIZEHEIGHT"), 32)          ' *** Set the [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") to the new "original" image, releasing the copied [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.         [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") CurrentScreen          '  [DRAW](/qb64wiki/index.php/DRAW "DRAW") PREVIOUS [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") ON THE NEW ONE         [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (0, 0), TempScreen, CurrentScreen          [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")          ' *** Remove (FREE) the copied [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") image.         [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") TempScreen          ' *** Tell the caller there was a resize         CheckResize = -1      [END IF](/qb64wiki/index.php/END_IF "END IF")   [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Code by waltersmind
  




## See also


* [\_RESIZE](/qb64wiki/index.php/RESIZE "RESIZE"), [\_RESIZE (function)](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)")
* [\_RESIZEWIDTH](/qb64wiki/index.php/RESIZEWIDTH "RESIZEWIDTH"), [\_RESIZEHEIGHT](/qb64wiki/index.php/RESIZEHEIGHT "RESIZEHEIGHT") (functions return the requested dimensions)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$RESIZE&oldid=8028>"




## Navigation menu








### Search





















