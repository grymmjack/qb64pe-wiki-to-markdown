


\_MD5$ - QB64 Phoenix Edition Wiki








# \_MD5$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_MD5$** function returns the [MD5](https://en.wikipedia.org/wiki/MD5 "wikipedia:MD5") hash value of any arbitrary string.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*md5hash$* = \_MD5$(*dataString$*)
  




## Parameters


* *md5hash$* is the hash value returned as hexadecimal [STRING](/qb64wiki/index.php/STRING "STRING"), if the given *dataString$* was empty the unusual but absolutely correct hash value is:
	+ D41D8CD98F00B204E9800998ECF8427E
* *dataString$* is any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") to build the hash value from.


  




## Description


* MD5 can be used as a checksum to verify data integrity against unintentional corruption.
* Historically it was widely used as a cryptographic hash function, however it has been found to suffer from extensive vulnerabilities.
* It remains suitable for other non-cryptographic purposes and may be preferred due to lower computational requirements than more recent Secure Hash Algorithms.


  




## Availability


* [![none](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "none")

**none**
* [![v3.12.0](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "v3.12.0")

**v3.12.0**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![yes](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "yes")

**yes**
* [![yes](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "yes")

**yes**


  




## Examples


Example
Showing how the MD5 hash value can detect differences in two strings.


| ``` 'this is the correct text t$ = "QB64 Phoenix Edition" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Correct Text: "; t$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    MD5 hash: "; _MD5$(t$) [PRINT](/qb64wiki/index.php/PRINT "PRINT") 'this text differs in just 1 bit from the above, by changing 4 to 5 'ASC("4") = 52 = &B00110100 'ASC("5") = 53 = &B00110101 t$ = "QB65 Phoenix Edition" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Mangled Text: "; t$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "    MD5 hash: "; _MD5$(t$) [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma


| ``` Correct Text: QB64 Phoenix Edition     MD5 hash: E512ECA19E9487D7C2F564E848314238  Mangled Text: QB65 Phoenix Edition     MD5 hash: 3EF03E7B0DB46F7D1FA6B9626563C10B  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2681)
* [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$"), [\_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")
* [\_ADLER32](/qb64wiki/index.php/ADLER32 "ADLER32"), [\_CRC32](/qb64wiki/index.php/CRC32 "CRC32")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MD5$&oldid=8944>"




## Navigation menu








### Search





















