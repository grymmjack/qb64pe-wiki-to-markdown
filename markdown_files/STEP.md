


STEP - QB64 Phoenix Edition Wiki








# STEP



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **STEP** keyword is used in [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") loops to skip through the count or to count down instead of up. Used in graphics to designate a relative coordinate position of a graphics object function.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


FOR counter\_variable = start\_point TO stop\_point [**STEP *interval***]
CIRCLE **STEP(0, 0)**, 10, 12
  




* The FOR counter variable is used to designate and pass the current FOR incremented value.
* FOR loops without the optional STEP value increment by + 1 every loop.
* The STEP increment value can be any literal or variable numerical type. It cannot be changed inside of the loop!
* Start and stop point values can be any literal or variable type and they cannot be changed inside of the loop.
* STEP interval designates the portion to add or subtract from the FOR variable value.


* When the STEP interval is positive, the start value should be less than the stop value ot the loop will be ignored.
* When the STEP interval is negative, the start value should be greater than the stop value or the loop will be ignored.

* In graphics statements, STEP can be used before a pair of coordinate brackets to indicate that the coordinates are relative to the last graphics statement position. IE the position will be that number of pixels away from the last graphical object.


  

*Example:* Stepping down 2 in a FOR counter loop.





| ``` [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i = 10 [TO](/qb64wiki/index.php/TO "TO") 0 STEP -2   [PRINT](/qb64wiki/index.php/PRINT "PRINT") i; [NEXT](/qb64wiki/index.php/NEXT "NEXT")  ``` |
| --- |




| ``` 10 8 6 4 2 0  ``` |
| --- |


*Note:* The value of i = -2 after the loop is done.
  




*Graphics Syntax:* LINE STEP(column1%, row1%)-(column2%, row2%), color\_attribute%
  




* STEP coordinate positions are relative positive or negative pixel moves from the previous graphics object's last coordinate. After a CIRCLE statement, the relative coordinates would be from its center.
* STEP can be used before the [LINE](/qb64wiki/index.php/LINE "LINE"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [PSET](/qb64wiki/index.php/PSET "PSET"), [PRESET](/qb64wiki/index.php/PRESET "PRESET"), [PAINT](/qb64wiki/index.php/PAINT "PAINT") or [DRAW](/qb64wiki/index.php/DRAW "DRAW") graphics object coordinates.


  



*Graphics Example:* Using STEP coordinates to PAINT a circle's interior.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 12 [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE") (100, 100), 50, 12 [PAINT](/qb64wiki/index.php/PAINT "PAINT") STEP(0, 0), 13, 12  ``` |
| --- |


*Explanation:* PAINT uses the CIRCLE's center coordinate position to paint the interior.
  




## See also


* [FOR...NEXT](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT")
* [DRAW](/qb64wiki/index.php/DRAW "DRAW")
* [LINE](/qb64wiki/index.php/LINE "LINE"), [CIRCLE](/qb64wiki/index.php/CIRCLE "CIRCLE"), [PSET](/qb64wiki/index.php/PSET "PSET"), [PAINT](/qb64wiki/index.php/PAINT "PAINT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STEP&oldid=7684>"




## Navigation menu








### Search





















