


\_INFLATE$ - QB64 Phoenix Edition Wiki








# \_INFLATE$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_INFLATE$ function decompresses a [string](/qb64wiki/index.php/STRING "STRING") compressed by the [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$") function.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*result$* = \_INFLATE$(*stringToDecompress$[, originalSize&]*)
  




## Description


* *result$* will contain the original version of *stringToDecompress$*.
* Optional parameter *originalSize&* can be used if the original size of the uncompressed data is known beforehand, which makes the decompression routine run more efficiently.
	+ If unspecified, decompression still works as expected, but may use more steps and need to allocate more memory internally.


  




## Availability


* **Version 1.4 and up**.


  




## Examples


*Example 1:* Compressing a long string of text.





| ``` a$ = "The quick brown fox jumps over the lazy dog. " [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Original string (a$): "; a$ [FOR](/qb64wiki/index.php/FOR "FOR") i = 1 [TO](/qb64wiki/index.php/TO "TO") 15     a$ = a$ + a$ [NEXT](/qb64wiki/index.php/NEXT "NEXT")  [PRINT](/qb64wiki/index.php/PRINT "PRINT") "After concatenating it into itself several times, LEN(a$) ="; [LEN](/qb64wiki/index.php/LEN "LEN")(a$)  b$ = [_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$")(a$) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "After using _DEFLATE$ to compress it, LEN ="; [LEN](/qb64wiki/index.php/LEN "LEN")(b$) [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "(compressed size is #.###% of the original)"; (([LEN](/qb64wiki/index.php/LEN "LEN")(b$) * 100) / [LEN](/qb64wiki/index.php/LEN "LEN")(a$)) c$ = _INFLATE$(b$) PRINT "After using _INFLATE$ to decompress it, LEN ="; [LEN](/qb64wiki/index.php/LEN "LEN")(c$)   ``` |
| --- |




| ``` Original string (a$): The quick brown fox jumps over the lazy dog After concatenating it into itself several times, LEN(a$) = 1474560 After using _DEFLATE$ to compress it, LEN = 4335 (compressed size is 0.295% of the original) After using _INFLATE$ to decompress it, LEN = 1474560  ``` |
| --- |


  




## See also


* [\_DEFLATE$](/qb64wiki/index.php/DEFLATE$ "DEFLATE$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=INFLATE$&oldid=7312>"




## Navigation menu








### Search





















