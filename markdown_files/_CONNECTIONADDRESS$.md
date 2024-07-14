


\_CONNECTIONADDRESS - QB64 Phoenix Edition Wiki








# \_CONNECTIONADDRESS



From QB64 Phoenix Edition Wiki
(Redirected from [CONNECTIONADDRESS$](/qb64wiki/index.php?title=CONNECTIONADDRESS$&redirect=no "CONNECTIONADDRESS$"))


[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_CONNECTIONADDRESS** function returns a connected user's [STRING](/qb64wiki/index.php/STRING "STRING") IP address value. For HTTP connections it returns the effective URL of the connection.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = \_CONNECTIONADDRESS[$](*connectionHandle&*)
  




## Description


* The handle can come from the [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT") or [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION").
* For **[HOSTs](/qb64wiki/index.php/OPENHOST "OPENHOST")**: It may return "TCP/IP:8080:213.23.32.5" where 8080 is the port it is listening on and 213.23.32.5 is the global IP address which any computer connected to the internet could use to locate your computer. If a connection to the internet is unavailable or your firewall blocks it, it returns your 'local IP' address (127.0.0.1). You might like to store this address somewhere where other computers can find it and connect to your host. Dynamic IPs which can change will need to be updated.
* For **[CLIENTs](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")**:
	+ For TCP/IP, it may return "TCP/IP:8080:213.23.32.5" where 8080 is the port it used to connect to the listening host and 213.23.32.5 is the IP address of the host name it resolved.
	+ For HTTP, it will return a url, such as "<https://qb64phoenix.com>". It is possible for this URL to differ from the one originally passed to [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT") if a HTTP redirect occurs when connecting to the original URL. The formatting may also differ slightly from the original URL.
* For **[CONNECTIONs](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION")** (from clients): It may return "TCP/IP:8080:34.232.321.25" where 8080 was the host listening port it connected to and 34.232.321.25 is the IP address of the client that connected. This is very useful because the host can log the IP address of clients for future reference (or banning, for example).
* The $ sygil is optional for compatibility with older versions.


  




## Examples


Example
A Host logging new chat clients in a Chat program. See the [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST") example for the rest of the code used.


| ``` f = [FREEFILE](/qb64wiki/index.php/FREEFILE "FREEFILE") [OPEN](/qb64wiki/index.php/OPEN "OPEN") "ChatLog.dat" [FOR](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [APPEND](/qb64wiki/index.php/OPEN#File_Access_Modes "OPEN") [AS](/qb64wiki/index.php/OPEN "OPEN") #f ' code at start of host section before DO loop.  newclient = [_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION")(host) ' receive any new client connection handles [IF](/qb64wiki/index.php/IF "IF") newclient [THEN](/qb64wiki/index.php/THEN "THEN")     numclients = numclients + 1 ' increment index     Users(numclients) = newclient ' place handle into array     IP$ = _CONNECTIONADDRESS(newclient)     [PRINT](/qb64wiki/index.php/PRINT "PRINT") IP$ + " has joined." ' displayed to Host only     [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #f, IP$, numclients ' print info to a log file     [PRINT](/qb64wiki/index.php/PRINT_(file_statement) "PRINT (file statement)") #Users(numclients), "Welcome!" ' from Host to new clients only [END IF](/qb64wiki/index.php/END_IF "END IF")  ``` |
| --- |




| ``` **Explanation**  The function returns the new client's IP address to the IP$ variable.  Prints the IP and the original login position to a log file. The  information can later be used by the host for reference  if necessary.  The host could set up a ban list too.  ``` |
| --- |


  




## See also


* [\_OPENCONNECTION](/qb64wiki/index.php/OPENCONNECTION "OPENCONNECTION"), [\_CONNECTED](/qb64wiki/index.php/CONNECTED "CONNECTED")
* [\_OPENHOST](/qb64wiki/index.php/OPENHOST "OPENHOST"), [\_OPENCLIENT](/qb64wiki/index.php/OPENCLIENT "OPENCLIENT")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CONNECTIONADDRESS&oldid=8288>"




## Navigation menu








### Search





















