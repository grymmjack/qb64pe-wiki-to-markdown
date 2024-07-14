


MKL$ - QB64 Phoenix Edition Wiki








# MKL$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The MKL$ function encodes a [LONG](/qb64wiki/index.php/LONG "LONG") numerical value into a 4-byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


*result$* = MKL$(*longVariableOrLiteral&*)
  




## Description


* *longVariableOrLiteral&* is converted to four ASCII characters. To see this in action, try PRINT MKL$(12345678).
* The numerical data usually takes up less bytes than printing the [LONG](/qb64wiki/index.php/LONG "LONG") number to a file.
* [LONG](/qb64wiki/index.php/LONG "LONG") integer values can range from -2147483648 to 2147483647.
* Since the representation of a long number can use up to 10 ASCII characters (ten bytes), writing to a file using MKL$ conversion, and then reading back with the [CVL](/qb64wiki/index.php/CVL "CVL") conversion can save up to 6 bytes of storage space.
* [CVL](/qb64wiki/index.php/CVL "CVL") can convert the value back to a [LONG](/qb64wiki/index.php/LONG "LONG") numerical value.
* [LONG](/qb64wiki/index.php/LONG "LONG") numerical variable values [PUT](/qb64wiki/index.php/PUT "PUT") into a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file are automatically placed as an MKL$ [ASCII](/qb64wiki/index.php/ASCII "ASCII") string value.


  




## Examples


See examples in:



* [SaveImage SUB](/qb64wiki/index.php/SaveImage_SUB "SaveImage SUB")
* [SaveIcon32](/qb64wiki/index.php/SaveIcon32 "SaveIcon32")


  




## See also


* [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKD$](/qb64wiki/index.php/MKD$ "MKD$")
* [CVD](/qb64wiki/index.php/CVD "CVD"), [CVI](/qb64wiki/index.php/CVI "CVI"), [CVS](/qb64wiki/index.php/CVS "CVS"), [CVL](/qb64wiki/index.php/CVL "CVL")
* [\_MK$](/qb64wiki/index.php/MK$ "MK$"), [\_CV](/qb64wiki/index.php/CV "CV")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MKL$&oldid=8661>"




## Navigation menu








### Search





















