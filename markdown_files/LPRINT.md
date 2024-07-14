


LPRINT - QB64 Phoenix Edition Wiki








# LPRINT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The LPRINT statement sends string text or numerical values to a parallel port (LPT1) printer in QBasic or a USB printer in **QB64**.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


LPRINT [*expression*] [{;|,}]
  




## Description


* *expression* is one or more text or numerical expressions separated by a semi-colon (;) or comma (,).
* Syntax is the same as [PRINT](/qb64wiki/index.php/PRINT "PRINT"), but cannot use a port number.
* Program does not have to [OPEN](/qb64wiki/index.php/OPEN "OPEN") the LPT1: parallel port.
* Assumes a 80 character wide page. **[WIDTH LPRINT is not supported in QB64.](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64 "Keywords currently not supported by QB64")**
* [LPRINT USING](/qb64wiki/index.php/LPRINT_USING "LPRINT USING") can print formatted text data to a page identically to how [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") formats a program screen.
* [COLORed](/qb64wiki/index.php/COLOR "COLOR") text and images can be printed using [\_PRINTIMAGE](/qb64wiki/index.php/PRINTIMAGE "PRINTIMAGE") which stretches them to fit the default printer's paper size.
* LPRINT will only print to the default USB or LPT printer set up in Windows. **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**.
* Note: Printer *escape codes* starting with [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(27) will not work with LPRINT and may produce text printing errors.


  




## See also


* [LPRINT USING](/qb64wiki/index.php/LPRINT_USING "LPRINT USING")
* [\_PRINTIMAGE](/qb64wiki/index.php/PRINTIMAGE "PRINTIMAGE") (prints color images to page size)
* [PRINT](/qb64wiki/index.php/PRINT "PRINT"), [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING")
* [Windows Printer Settings](/qb64wiki/index.php/Windows_Printer_Settings "Windows Printer Settings")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=LPRINT&oldid=7904>"




## Navigation menu








### Search





















