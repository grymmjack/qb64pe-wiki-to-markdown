


\_BIN$ - QB64 Phoenix Edition Wiki








# \_BIN$



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
This function returns the binary (base 2) representation of any numeric value.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Availability](#Availability) * [5 Examples](#Examples) * [6 See also](#See_also) |
| --- |


## Syntax


*binvalue$* = \_BIN$(*number*)
  




## Parameters


* *number* can be any [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG") or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") value, positive or negative.
* *number* can also be any [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") value, but only the integer part of the value is converted in that case. That is, from the value *-123.45* the function would convert the *-123* only.


  




## Description


* The function returns the base 2 (binary) representation of the given *number* as [STRING](/qb64wiki/index.php/STRING "STRING").
* Different from [STR$](/qb64wiki/index.php/STR$ "STR$"), this function does not return a leading sign placeholder space, so no [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$") to strip that space from positive numbers is necessary.
* [VAL](/qb64wiki/index.php/VAL "VAL") can convert the returned bin string value back to a decimal value by prefixing the string with "[&B](/qb64wiki/index.php/%26B "&B")".
	+ Eg. decimal = [VAL](/qb64wiki/index.php/VAL "VAL")("&B" + binvalue$).


  




## Availability


* **QB64 v2.1 and up**
* **QB64-PE all versions**


  




## Examples


Example 1
Comparing decimal, hexadecimal, octal and binary string values from 0 to 15.


| ``` tabletop$ = " Decimal | Hexadecimal | Octal | Binary " tablesep$ = "---------+-------------+-------+--------" tableout$ = "  \ \    |      \\     |   \\  |  \  \  " 'the PRINT USING template  [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 2, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") tabletop$ [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 3, 10: [PRINT](/qb64wiki/index.php/PRINT "PRINT") tablesep$ [FOR](/qb64wiki/index.php/FOR "FOR") n% = 0 [TO](/qb64wiki/index.php/TO "TO") 15     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 4 + n%, 10: [PRINT USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") tableout$; [STR$](/qb64wiki/index.php/STR$ "STR$")(n%); [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(n%); [OCT$](/qb64wiki/index.php/OCT$ "OCT$")(n%); _BIN$(n%) [NEXT](/qb64wiki/index.php/NEXT "NEXT") n%  ``` |
| --- |


Note
Although the decimal numbers 0-15 have a maximum width of 2 digits only, an extra space in the *tableout$* template is needed when using the (fixed width string) slash output format, as [STR$](/qb64wiki/index.php/STR$ "STR$") values contain a leading sign placeholder space.


| ```           Decimal | Hexadecimal | Octal | Binary          ---------+-------------+-------+--------             0     |      0      |   0   |  0             1     |      1      |   1   |  1             2     |      2      |   2   |  10             3     |      3      |   3   |  11             4     |      4      |   4   |  100             5     |      5      |   5   |  101             6     |      6      |   6   |  110             7     |      7      |   7   |  111             8     |      8      |   10  |  1000             9     |      9      |   11  |  1001             10    |      A      |   12  |  1010             11    |      B      |   13  |  1011             12    |      C      |   14  |  1100             13    |      D      |   15  |  1101             14    |      E      |   16  |  1110             15    |      F      |   17  |  1111  ``` |
| --- |


  




Example 2
Converting a binary value to decimal.


| ``` binvalue$ = _BIN$(255) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Bin: "; binvalue$ [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Converting Bin value to Decimal:"; [VAL](/qb64wiki/index.php/VAL "VAL")("&B" + binvalue$)  ``` |
| --- |




| ``` Bin: 11111111 Converting Bin value to Decimal: 255  ``` |
| --- |


  




## See also


* [HEX$](/qb64wiki/index.php/HEX$ "HEX$"), [OCT$](/qb64wiki/index.php/OCT$ "OCT$"), [STR$](/qb64wiki/index.php/STR$ "STR$")
* [&B](/qb64wiki/index.php/%26B "&B") (binary), [&H](/qb64wiki/index.php/%26H "&H") (hexadecimal), [&O](/qb64wiki/index.php/%26O "&O") (octal), [VAL](/qb64wiki/index.php/VAL "VAL")
* [Base Comparisons](/qb64wiki/index.php/Base_Comparisons "Base Comparisons")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BIN$&oldid=8268>"




## Navigation menu








### Search





















