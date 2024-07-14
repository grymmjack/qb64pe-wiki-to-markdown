


\_OPENHOST - QB64 Phoenix Edition Wiki








# \_OPENHOST



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_OPENHOST function opens a Host which listens for new connections and returns a Host status handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*hostHandle* = \_OPENHOST(**"TCP/IP:8080"**)
  




## Description


* Creates an [Illegal Function Call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error if called with a string argument of the wrong syntax.
* The port used in the syntax example is 8080.
* Valid *hostHandle* values are negative numbers.
* If the syntax is correct but they fail to begin/connect a *hostHandle* of 0 is returned.
* Always check if the handle returned is 0 (failed) before continuing.
* [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") *hostHandle* closes the host. A failed handle value of 0 does not need to be closed.


  




## See also


* [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION"), [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")
* [\_CONNECTED](/qb64wiki/index.php/CONNECTED "CONNECTED"), [\_CONNECTIONADDRESS](/qb64wiki/index.php/CONNECTIONADDRESS "CONNECTIONADDRESS")
* [Email Demo](/qb64wiki/index.php/Email_Demo "Email Demo"), [Inter-Program Data Sharing Demo](/qb64wiki/index.php/Inter-Program_Data_Sharing_Demo "Inter-Program Data Sharing Demo")
* [Downloading Files](/qb64wiki/index.php/Downloading_Files "Downloading Files")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPENHOST&oldid=7350>"




## Navigation menu








### Search





















