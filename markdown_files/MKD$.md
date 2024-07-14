


MKD$ - QB64 Phoenix Edition Wiki








# MKD$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The MKD$ function encodes a [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") numerical value into an 8-byte [ASCII](/qb64wiki/index.php/ASCII "ASCII") [STRING](/qb64wiki/index.php/STRING "STRING") value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 See also](#See_also) |
| --- |


## Syntax


*result$* = MKD$(*doublePrecisionVariableOrLiteral#*)
  




## Description


* *doublePrecisionVariableOrLiteral#* is converted to eight ASCII characters. To see this in action, try PRINT MKD$(12345678).
* [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") values can range up to 15 decimal point digits. Decimal point accuracy depends on whole value places taken.
* The string value can be converted back to a DOUBLE numerical value using [CVD](/qb64wiki/index.php/CVD "CVD").
* [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") numerical variable values [PUT](/qb64wiki/index.php/PUT "PUT") into a [BINARY](/qb64wiki/index.php/BINARY "BINARY") file are automatically placed as an MKD$ [ASCII](/qb64wiki/index.php/ASCII "ASCII") string value.


  




## See also


* [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$")
* [CVD](/qb64wiki/index.php/CVD "CVD"), [CVI](/qb64wiki/index.php/CVI "CVI"), [CVS](/qb64wiki/index.php/CVS "CVS"), [CVL](/qb64wiki/index.php/CVL "CVL")
* [\_MK$](/qb64wiki/index.php/MK$ "MK$"), [\_CV](/qb64wiki/index.php/CV "CV")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MKD$&oldid=7344>"




## Navigation menu








### Search





















