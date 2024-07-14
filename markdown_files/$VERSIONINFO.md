


$VERSIONINFO - QB64 Phoenix Edition Wiki








# $VERSIONINFO



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The $VERSIONINFO [metacommand](/qb64wiki/index.php/Metacommand "Metacommand") adds text metadata to the resulting executable for identification purposes across the OS. Windows-only.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


$VERSIONINFO:*key*=*value*
  




## Parameters


* Text *keys* can be: **Comments, CompanyName, FileDescription, FileVersion, InternalName, LegalCopyright, LegalTrademarks, OriginalFilename, ProductName, ProductVersion, Web**
* Numeric *keys* can be:**FILEVERSION#** and **PRODUCTVERSION#**
	+ When provided, the numerical keys **FILEVERSION#** and **PRODUCTVERSION#** will also provide values to the text keys **FileVersion** and **ProductVersion,** if the text versions are not provided separately. (QB64-PE v0.6.0 and up)


  




## Description


* Text and numerical values are string literals without quotes entered by programmer. **No variables are accepted.** (variable names would be interpreted as literals).
* Numeric key=*value* must be 4 comma-separated numerical text values entered by programmer which usually stand for major, minor, revision and build numbers).
* A manifest file is automatically embedded into the resulting .exe file so that Common Controls v6.0 gets linked at runtime, if required.
* **[Keyword not supported in Linux or macOS versions](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions "Keywords currently not supported by QB64")**


  




## Availability


* [![v1.2](/qb64wiki/images/9/91/Qb64.png)](/qb64wiki/index.php/File:Qb64.png "v1.2")

**v1.2**
* [![all](/qb64wiki/images/0/07/Qbpe.png)](/qb64wiki/index.php/File:Qbpe.png "all")

**all**
* [![Apix.png](/qb64wiki/images/5/5f/Apix.png)](/qb64wiki/index.php/File:Apix.png)
* [![yes](/qb64wiki/images/2/29/Win.png)](/qb64wiki/index.php/File:Win.png "yes")

**yes**
* [![no](/qb64wiki/images/7/7a/Lnx.png)](/qb64wiki/index.php/File:Lnx.png "no")

**no**
* [![no](/qb64wiki/images/2/22/Osx.png)](/qb64wiki/index.php/File:Osx.png "no")

**no**


  




## Examples


*Example:* Adding metadata to a Windows exe compiled with QB64:





| ``` $VERSIONINFO:CompanyName=Your company name goes here $VERSIONINFO:FILEVERSION#=1,0,0,0 $VERSIONINFO:PRODUCTVERSION#=1,0,0,0  ``` |
| --- |


  




## See also


* [$EXEICON](/qb64wiki/index.php/$EXEICON "$EXEICON")
* [\_ICON](/qb64wiki/index.php/ICON "ICON")
* [VERSIONINFO resource (MSDN)](https://msdn.microsoft.com/library/windows/desktop/aa381058(v=vs.85).aspx)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=$VERSIONINFO&oldid=7744>"




## Navigation menu








### Search





















