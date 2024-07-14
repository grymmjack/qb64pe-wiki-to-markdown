


\_CLIPBOARD$ - QB64 Phoenix Edition Wiki








# \_CLIPBOARD$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_CLIPBOARD$** statement copies the [STRING](/qb64wiki/index.php/STRING "STRING") value into the system clipboard.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


\_CLIPBOARD$ = *string\_expression$*
  




## Description


* *string\_expression$* is the string value to be sent to the clipboard.
* The string value will replace everything previously in the clipboard.
* Assemble long text into one string variable value before using this statement.
* Add CHR$(13) + CHR$(10) CRLF characters to move to a new clipboard line.
* When copying text files, end line CRLF characters 13 and 10 do not have to be added.
* Numerical values can be converted to strings using [STR$](/qb64wiki/index.php/STR$ "STR$"), [\_MK$](/qb64wiki/index.php/MK$ "MK$"), [MKI$](/qb64wiki/index.php/MKI$ "MKI$"), [MKL$](/qb64wiki/index.php/MKL$ "MKL$"), [MKS$](/qb64wiki/index.php/MKS$ "MKS$"), [MKD$](/qb64wiki/index.php/MKD$ "MKD$"), [\_BIN$](/qb64wiki/index.php/BIN$ "BIN$"), [HEX$](/qb64wiki/index.php/HEX$ "HEX$") or [OCT$](/qb64wiki/index.php/OCT$ "OCT$").
* The clipboard can be used to copy, paste and communicate between running programs.


  




## Examples


Example
Set 2 lines of text in the clipboard using a carriage return to end text lines


| ``` [DIM](/qb64wiki/index.php/DIM "DIM") CrLf [AS](/qb64wiki/index.php/AS "AS") [STRING](/qb64wiki/index.php/STRING "STRING") * 2 'define as 2 byte STRING CrLf = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13) + [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(10) 'carriage return & line feed  _CLIPBOARD$ = "This is line 1" + CrLf + "This is line 2" [PRINT](/qb64wiki/index.php/PRINT "PRINT") [_CLIPBOARD$](/qb64wiki/index.php/CLIPBOARD$_(function) "CLIPBOARD$ (function)") 'display what is in the clipboard  ``` |
| --- |




| ``` This is line 1 This is line 2  ``` |
| --- |


  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1238)
* [\_CLIPBOARD$ (function)](/qb64wiki/index.php/CLIPBOARD$_(function) "CLIPBOARD$ (function)")
* [\_CLIPBOARDIMAGE (function)](/qb64wiki/index.php/CLIPBOARDIMAGE_(function) "CLIPBOARDIMAGE (function)"), [\_CLIPBOARDIMAGE](/qb64wiki/index.php/CLIPBOARDIMAGE "CLIPBOARDIMAGE") (statement)
* [CHR$](/qb64wiki/index.php/CHR$ "CHR$"), [ASCII](/qb64wiki/index.php/ASCII "ASCII") (code table)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=CLIPBOARD$&oldid=8918>"




## Navigation menu








### Search





















