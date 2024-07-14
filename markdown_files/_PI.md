


\_PI - QB64 Phoenix Edition Wiki








# \_PI



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_PI function returns **π** as a [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") value with an optional multiplier parameter.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*circumference* = \_PI[(*multiplier*)]
  




## Parameters


* Optional *multiplier* (*2 \* radius* in above syntax) allows multiplication of the π value.


  




## Description


* Function can be used in to supply π or multiples in a program.
* Accuracy is determined by the return variable type [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT").
* The π value can also be derived using 4 \* [ATN](/qb64wiki/index.php/ATN "ATN")(1) for a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") value.


  




## Examples


*Example:* Calculating the area of a circle using a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") variable in this case.





| ``` radius = 5 circlearea = _PI(radius ^ 2) PRINT circlearea  ``` |
| --- |




| ```  78.53982  ``` |
| --- |


  




## See also


* [\_ATAN2](/qb64wiki/index.php/ATAN2 "ATAN2"), [TAN](/qb64wiki/index.php/TAN "TAN")
* [ATN](/qb64wiki/index.php/ATN "ATN")
* [SIN](/qb64wiki/index.php/SIN "SIN"), [COS](/qb64wiki/index.php/COS "COS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=PI&oldid=7644>"




## Navigation menu








### Search





















