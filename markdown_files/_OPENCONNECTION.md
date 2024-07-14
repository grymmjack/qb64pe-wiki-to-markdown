


\_OPENCONNECTION - QB64 Phoenix Edition Wiki








# \_OPENCONNECTION



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_OPENCONNECTION function opens a connection from a client that the host has detected and returns a status handle.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*connectHandle* = \_OPENCONNECTION(*hostHandle*)
  




## Description


* Valid *connectHandle* values returned are negative numbers.
* If the syntax is correct but they fail to begin/connect, a *connectHandle* of 0 is returned.
* Always check if the handle returned is 0 (failed) before continuing.
* [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #*connectHandle* closes the connection. Failed connections(*connectHandle* = 0) do not need to be closed.
* As a **Host** you can check for new clients (users). Each will have a unique connection handle.
* Creates an [Illegal Function Call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error if called with a string argument of the wrong syntax.
* Handle values can be used as the open number by [GET #](/qb64wiki/index.php/GET_(TCP/IP_statement) "GET (TCP/IP statement)") read statement and [PUT #](/qb64wiki/index.php/PUT_(TCP/IP_statement) "PUT (TCP/IP statement)") write statement.


  




## See also


* [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")
* [\_CONNECTED](/qb64wiki/index.php/CONNECTED "CONNECTED"), [\_CONNECTIONADDRESS](/qb64wiki/index.php/CONNECTIONADDRESS "CONNECTIONADDRESS")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPENCONNECTION&oldid=6141>"




## Navigation menu








### Search





















