


PMAP - QB64 Phoenix Edition Wiki








# PMAP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **PMAP** statement returns the physical or [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") view port coordinates.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


PMAP (*coordinate*, *function\_number%*)
  




* The *coordinate* is the coordinate point to be mapped.
* The *function* can have one of four values:


0 = Maps view port coordinate to physical x screen coordinate
1 = Maps view port coordinate to physical y screen coordinate
2 = Maps physical screen coordinate to view port x coordinate
3 = Maps physical screen coordinate to view port y coordinate
* The four PMAP functions allow the user to find equal point locations between the view coordinates created with the [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") statement and the physical screen coordinates of the viewport as defined by the [VIEW](/qb64wiki/index.php/VIEW "VIEW") statement.
* Mouse co-ordinates returned by [\_MOUSEX](/qb64wiki/index.php/MOUSEX "MOUSEX") and [\_MOUSEY](/qb64wiki/index.php/MOUSEY "MOUSEY") are the physical screen co-ordinates.


  

*Example:* Use PMAP to convert coordinate values from view to screen coordinates and from screen coordinates to view coordinates.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12  'Coordinates of upper-left corner of the window is defined in following statement are (90,100) [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW") [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") (90, 100)-(200, 200) 'coordinates of lower-right 'corner are 200, 200.  X = PMAP(90, 0)          ' X = 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") X Y = PMAP(100, 1)         ' Y = 0 [PRINT](/qb64wiki/index.php/PRINT "PRINT") Y  'These statements return the screen coordinates equal to the view coordinates 200, 200. X = PMAP(200, 0)         ' X = 639 [PRINT](/qb64wiki/index.php/PRINT "PRINT") X Y = PMAP(200, 1)         ' Y = 479 [PRINT](/qb64wiki/index.php/PRINT "PRINT") Y  'These statements return the view coordinates equal to the screen coordinates 0, 0 X = PMAP(0, 0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") X Y = PMAP(0, 0) [PRINT](/qb64wiki/index.php/PRINT "PRINT") Y  'These statements return the view coordinates equal to the screen coordinates 639, 479. X = PMAP(639, 2)         ' X = 200 [PRINT](/qb64wiki/index.php/PRINT "PRINT") X Y = PMAP(479, 3)         ' Y = 200 [PRINT](/qb64wiki/index.php/PRINT "PRINT") Y  [SLEEP](/qb64wiki/index.php/SLEEP "SLEEP")                    ' pause before clearing view port [CLS](/qb64wiki/index.php/CLS "CLS") 1                    ' clear grahic view port [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW")                   ' end graphic view port [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


*Note:* If physical screen coordinates are (0, 0) in the upper-left corner and (639, 479) in the lower-right corner, then the statements return the screen coordinate's equal to the view coordinates 90, 100.
  




## See also


* [WINDOW](/qb64wiki/index.php/WINDOW "WINDOW"), [VIEW](/qb64wiki/index.php/VIEW "VIEW")
* [VIEW PRINT](/qb64wiki/index.php/VIEW_PRINT "VIEW PRINT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PMAP&oldid=7357>"




## Navigation menu








### Search





















