


\_STATUSCODE - QB64 Phoenix Edition Wiki








# \_STATUSCODE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
**\_STATUSCODE** gives the HTTP status code of an HTTP response that was opened using [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT").


**HTTP functionality is current unstable, and requires [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):HTTP to be able to use.**


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) |
| --- |


## Syntax


\_STATUSCODE(*Handle*)
  




## Parameters


* *Handle* is the handle returned from [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT") when making an HTTP request.


  




## Description


**\_STATUSCODE** is used to get the HTTP status code returned on an HTTP response. A list of HTTP status codes can be read [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes "wikipedia:List of HTTP status codes"), generally speaking codes in the 200 range indicate success, 400 range indicates a client error, and 500 range indicate a server error.


  




## Availability


* **QB64-PE v3.5.0 and up**


  




## Examples




| ``` [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):HTTP  ' This URL simply returns a fake JSON response h& = [_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")("HTTP:https://httpbin.org/json")  ' Print the status code on the HTTP response [PRINT](/qb64wiki/index.php/PRINT "PRINT") _STATUSCODE(h&)  [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") h&   ``` |
| --- |


Code by Matthew Kilgore


| ``` 200  ``` |
| --- |


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=STATUSCODE&oldid=8995>"




## Navigation menu








### Search





















