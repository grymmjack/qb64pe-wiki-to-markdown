


\_OPENCLIENT - QB64 Phoenix Edition Wiki








# \_OPENCLIENT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_OPENCLIENT** function connects to a Host on the Internet as a Client and returns the Client status handle.


**HTTP functionality is current unstable, and requires [$UNSTABLE](/qb64wiki/index.php/$UNSTABLE "$UNSTABLE"):HTTP to be able to use.**


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*clientHandle&* = \_OPENCLIENT(**"TCP/IP:8080:12:30:1:10"**)
*clientHandle&* = \_OPENCLIENT(**"HTTP:url"**)
  




## Description


* An [Illegal Function Call](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") error will be triggered if the function is called with a string argument of the wrong syntax.
* Connects to a host somewhere on the internet as a client.
* Valid *clientHandle&* values are negative. 0 means that the connection failed. Always check that the handle returned is not 0.
* [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") *clientHandle&* closes the client. A failed handle of value 0 does not need to be closed.


  




## Examples


Example 1
Attempting to connect to a local host(your host) as a client. A zero return indicates failure.


| ``` client = _OPENCLIENT("TCP/IP:7319:localhost") [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") client [THEN](/qb64wiki/index.php/THEN "THEN")    [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[Connected to " + [_CONNECTIONADDRESS](/qb64wiki/index.php/CONNECTIONADDRESS "CONNECTIONADDRESS")(client) + "]" [ELSE](/qb64wiki/index.php/ELSE "ELSE") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "[Connection Failed!]" [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |


**NOTE:** Try a valid TCP/IP port setting to test this routine!


---


Example 2
Using HTTP to download from a URL.


| ``` ' Content of the HTTP response is returned. The statusCode is also assigned. [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") Download$(url [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING"), statusCode [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     h& = _OPENCLIENT("HTTP:" + url)      statusCode = [_STATUSCODE](/qb64wiki/index.php/STATUSCODE "STATUSCODE")(h&)      [WHILE](/qb64wiki/index.php/WHILE "WHILE") [NOT](/qb64wiki/index.php/NOT "NOT") [EOF](/qb64wiki/index.php/EOF "EOF")(h&)         [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 60         [GET](/qb64wiki/index.php/GET_(HTTP_statement) "GET (HTTP statement)") #h&, , s$         content$ = content$ + s$     [WEND](/qb64wiki/index.php/WEND "WEND")      [CLOSE](/qb64wiki/index.php/CLOSE "CLOSE") #h&      Download$ = content$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


  




## See also


* [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION")
* [\_CONNECTED](/qb64wiki/index.php/CONNECTED "CONNECTED"), [\_CONNECTIONADDRESS$](/qb64wiki/index.php/CONNECTIONADDRESS$ "CONNECTIONADDRESS$")
* [Email Demo](/qb64wiki/index.php/Email_Demo "Email Demo"), [Inter-Program Data Sharing Demo](/qb64wiki/index.php/Inter-Program_Data_Sharing_Demo "Inter-Program Data Sharing Demo")
* [Downloading Files](/qb64wiki/index.php/Downloading_Files "Downloading Files")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=OPENCLIENT&oldid=8005>"




## Navigation menu








### Search





















