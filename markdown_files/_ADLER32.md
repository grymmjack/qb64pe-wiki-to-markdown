


\_ADLER32 - QB64 Phoenix Edition Wiki








# \_ADLER32



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_ADLER32** function returns the [Adler-32](https://en.wikipedia.org/wiki/Adler-32 "wikipedia:Adler-32") checksum of any arbitrary string.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*chksum~&* = \_ADLER32(*dataString$*)
  




## Parameters


* *chksum~&* is the [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") checksum returned (one (1), if the given *dataString$* was empty).
* *dataString$* is any literal or variable [STRING](/qb64wiki/index.php/STRING "STRING") to build the checksum from.


  




## Description


* The **Adler-32** checksum uses a relative simple but very fast algorithm, it has the following known properties:
	+ All single bit flips will be detected.
	+ All double bit flips will be detected.
	+ Burst errors up to seven bits are always detected.
* For more informations have a closer look at [Chapters 5-7 here](https://www.intel.com/content/www/us/en/content-details/709921/intel-quickassist-technology-intel-qat-using-adler-32-checksum-and-crc32-hash-to-ensure-data-compression-integrity.html).


  




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
Showing how the Adler-32 checksum can detect differences in two strings.


| ``` 'this is the correct text t$ = "QB64 Phoenix Edition" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Correct Text: "; t$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Adler-32 Sum: "; [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")("00000000" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(_ADLER32(t$)), 8) [PRINT](/qb64wiki/index.php/PRINT "PRINT") 'this text differs in just 1 bit from the above, by changing 4 to 5 'ASC("4") = 52 = &B00110100 'ASC("5") = 53 = &B00110101 t$ = "QB65 Phoenix Edition" [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Mangled Text: "; t$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Adler-32 Sum: "; [RIGHT$](/qb64wiki/index.php/RIGHT$ "RIGHT$")("00000000" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(_ADLER32(t$)), 8) [END](/qb64wiki/index.php/END "END")  ``` |
| --- |


Example by RhoSigma


| ``` Correct Text: QB64 Phoenix Edition Adler-32 Sum: 41F806E5  Mangled Text: QB65 Phoenix Edition Adler-32 Sum: 420906E6  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=2681)
* [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$"), [\_INFLATE$](/qb64wiki/index.php/INFLATE$ "INFLATE$")
* [\_CRC32](/qb64wiki/index.php/CRC32 "CRC32"), [\_MD5$](/qb64wiki/index.php/MD5$ "MD5$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ADLER32&oldid=8942>"




## Navigation menu








### Search





















