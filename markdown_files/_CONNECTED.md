


\_CONNECTED - QB64 Phoenix Edition Wiki








# \_CONNECTED



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_CONNECTED function returns the status of a TCP/IP or HTTP connection handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result&* = \_CONNECTED(*connectionHandle&*)
  




## Description


* The handle can come from the [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT") or [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION").
* Returns -1 if still connected or 0 if connection has ended/failed.
* Do not rely solely on this function to check for ending communication.
* Use "time-out" checking as well and [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") any suspect connections.
* If this function indicates the handle is not connected, any unread messages can still be read using [GET #](/qb64wiki/index.php/GET_(TCP/IP_statement) "GET (TCP/IP statement)").
* Even if this function indicates the handle is not connected, it is important to [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") the connection anyway or important resources cannot be reallocated.


  




## See also


* [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION"), [\_CONNECTIONADDRESS$](/qb64wiki/index.php/CONNECTIONADDRESS$ "CONNECTIONADDRESS$")
* [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")
* [Downloading Files](/qb64wiki/index.php/Downloading_Files "Downloading Files")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONNECTED&oldid=5912>"




## Navigation menu








### Search





















