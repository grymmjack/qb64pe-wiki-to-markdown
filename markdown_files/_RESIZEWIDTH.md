


\_RESIZEWIDTH - QB64 Phoenix Edition Wiki








# \_RESIZEWIDTH



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_RESIZEWIDTH function returns the user resized screen pixel width if [$RESIZE](/qb64wiki/index.php/$RESIZE "$RESIZE"):ON allows it and [\_RESIZE](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)") returns -1


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*newWidth&* = \_RESIZEWIDTH
  




## Description


* [\_RESIZE](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)") function must return true (-1) before the requested screen dimensions can be returned by the function.
* The program should decide if the request is allowable for proper program interaction.


  




## Availability


* **Version 1.000 and up**.


  




## Examples


*Example:* Resize the current screen image according to user's request.





| ``` [$RESIZE](/qb64wiki/index.php/$RESIZE "$RESIZE"):ON  s& = [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(300, 300, 32) [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") s&  bee& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png") 'any image  [DO](/qb64wiki/index.php/DO "DO")     [IF](/qb64wiki/index.php/IF "IF") [_RESIZE](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)") THEN         oldimage& = s&         s& = _NEWIMAGE(_RESIZEWIDTH, _RESIZEHEIGHT, 32)         SCREEN s&         [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") oldimage&     END IF      [CLS](/qb64wiki/index.php/CLS "CLS")      'Center the QB64 bee image:     x = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)") / 2 - _WIDTH(bee&) / 2     y = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT") / 2 - _HEIGHT(bee&) / 2     [_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") (x, y), bee&     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")     [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30 [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


  




## See also


* [$RESIZE](/qb64wiki/index.php/$RESIZE "$RESIZE")
* [\_RESIZE (function)](/qb64wiki/index.php/RESIZE_(function) "RESIZE (function)")
* [\_RESIZEHEIGHT](/qb64wiki/index.php/RESIZEHEIGHT "RESIZEHEIGHT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=RESIZEWIDTH&oldid=7174>"




## Navigation menu








### Search





















