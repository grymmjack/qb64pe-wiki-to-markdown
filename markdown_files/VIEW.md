


VIEW - QB64 Phoenix Edition Wiki








# VIEW



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **VIEW** statement creates a graphics view port area by defining the coordinate limits to be viewed.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


**VIEW** [[SCREEN] (column1, row1)-(column2, row2)[, [color][, border]
  




* When the SCREEN option is used, all coordinates are absolute and only graphics within the viewport area are plotted.
* When the SCREEN option is not used, all coordinates are relative to the view port with the values of column1 and row1 being automatically added before plotting the point.
* Coordinate values are for the top left and bottom right values of a box area of the screen mode used.
* The color parameter specifies a background fill color for the area. None when omitted.
* Border requires any valid color attribute to draw a line around the VIEW area if there is room for it.
* VIEW without any parameters disables the previous viewport. [RUN](/qb64wiki/index.php/RUN "RUN") and [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") can also disable any VIEW port.
* [CLS](/qb64wiki/index.php/CLS "CLS") or [CLS 1](/qb64wiki/index.php/CLS "CLS") clears the active graphics VIEW port area only. Disable a viewport before attempting to clear the entire screen!
* **Note: QB64 [RUN](/qb64wiki/index.php/RUN "RUN") statements will not close [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT"), VIEW or [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") view ports presently!**


  

*Example 1:* Using SCREEN option with absolute screen coordinates.





| ```  SCREEN 12  VIEW SCREEN (200, 200)-(400, 400), 1, 9 ' blue BG with light blue border  CIRCLE (220, 220), 20, 11 ' using the actual screen coordinates  ``` |
| --- |


  

*Example 2:* Using coordinates relative to the viewport box area.





| ```  SCREEN 12  VIEW (200, 200)-(400, 400), 1, 9  CIRCLE (20, 20), 20, 11 ' using coordinates inside of the viewport  ``` |
| --- |


*Explanation:* The relative coordinates are automatically adjusted to place the object correctly. Any values outside of the box's area will not be displayed. Both examples should display the same screen image.
  




## See also


* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT")
* [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW")
* [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN"), [CLS](/qb64wiki/index.php/CLS "CLS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=VIEW&oldid=7706>"




## Navigation menu








### Search





















