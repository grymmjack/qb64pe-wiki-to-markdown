


VAL - QB64 Phoenix Edition Wiki








# VAL



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **VAL** Function returns the decimal numerical equivalent value of a [STRING](/qb64wiki/index.php/STRING "STRING") numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 See also](#See_also) |
| --- |


## Syntax


*value* = **VAL**(*string\_value$*)
  




* VAL converts string numbers to numerical values including decimal point values and prefixed "[&B](/qb64wiki/index.php/%26B "&B")" binary, "[&H](/qb64wiki/index.php/%26H "&H")" hexadecimal, "[&O](/qb64wiki/index.php/%26O "&O")" octal.
* VAL conversion stops at non-numeric characters except for letter "D" or "E" exponential notation values.


String values with "D" and "E" letters between numbers may be converted also! EX: **VAL("9D4") = 90000**
* If the first string character is not a number VAL returns 0. VAL may return erratic values with "%" or "&" starting characters.
* Binary [\_BIN$](/qb64wiki/index.php/BIN$ "BIN$") string values with the "[&B](/qb64wiki/index.php/%26B "&B")" prefix can be converted to a decimal value with digits from 0 to 1 only.
* Hexadecimal [HEX$](/qb64wiki/index.php/HEX$ "HEX$") string values with the "[&H](/qb64wiki/index.php/%26H "&H")" prefix can be converted to a decimal value with digits 0 to 9 and letters A to F, like; dec = VAL("&H"+hexvar$).
* Octal [OCT$](/qb64wiki/index.php/OCT$ "OCT$") string values with the "[&O](/qb64wiki/index.php/%26O "&O")" prefix can be converted to a decimal value with digits from 0 to 7 only.
* For character values of [ASCII](/qb64wiki/index.php/ASCII "ASCII") data use the [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)") to get the value.
* In QB64 use an [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") return variable to hold integer values returned by VAL [Hex](/qb64wiki/index.php/HEX$ "HEX$") strings: **value% = VAL("&HFFFF") = -1**


  

*Example 1:* Differences in values returned with QBasic and QB64:





| ``` [PRINT](/qb64wiki/index.php/PRINT "PRINT") VAL("[&H](/qb64wiki/index.php/%26H "&H")") '203 in QB, 0 in QB64 [PRINT](/qb64wiki/index.php/PRINT "PRINT") VAL("[&H](/qb64wiki/index.php/%26H "&H")FFFF") ' -1 QB, 65535 in QB64 [PRINT](/qb64wiki/index.php/PRINT "PRINT") VAL("[&H](/qb64wiki/index.php/%26H "&H")FFFF&") '65535 in both  ``` |
| --- |


*Explanation:* A quirk in QBasic returned VAL values of 203 for "&" and "&H" that was never fixed until PDS(7.1).
  

*Example 2:* Converting a string with some number characters





| ```  text$ = "1.23Hello"  number! = VAL(text$)  PRINT number!  ``` |
| --- |




| ``` 1.23  ``` |
| --- |


  

*Example 3:* Converting literal and variable [string](/qb64wiki/index.php/STRING "STRING") values to numerical values.





| ```  a$ = "33"  PRINT VAL("10") + VAL(a$) + 1  ``` |
| --- |




| ``` 44  ``` |
| --- |


*Explanation:* 10 + 33 + 1 = 44, the strings were converted to values.
You have to convert the string to values in order to use them in a mathematical expression also since mixing strings with numbers isn't allowed. VAL will stop at a text letter so VAL("123G56) would return 123.
If VAL wasn't used the program would break with an error, as you can't add the value 1 to a string, if the 1 was a string ("1") then the program would return "10331", but now since we used VAL, the numbers were added as they should.
  

*Example 4:* Converting a hexadecimal value to decimal value using HEX$ with VAL.





| ```  decnumber% = 96  hexnumber$ = "&H" + [HEX$](/qb64wiki/index.php/HEX$ "HEX$")(decnumber%)  'convert decimal value to hex and add hex prefix  PRINT hexnumber$  decimal% = VAL(hexnumber$)  PRINT decimal%  ``` |
| --- |




| ``` &H60  96  ``` |
| --- |


*Explanation:* [HEX$](/qb64wiki/index.php/HEX$ "HEX$") converts a decimal number to hexadecimal, but VAL will only recognize it as a valid value with the "&H" prefix. Especially since hexadecimal numbers can use "A" through "F" in them. Create a converter function from this code!
  




## See also


* [ASC (function)](/qb64wiki/index.php/ASC_(function) "ASC (function)"), [STR$](/qb64wiki/index.php/STR$ "STR$")
* [\_BIN$](/qb64wiki/index.php/BIN$ "BIN$"), [HEX$](/qb64wiki/index.php/HEX$ "HEX$"), [OCT$](/qb64wiki/index.php/OCT$ "OCT$")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=VAL&oldid=8180>"




## Navigation menu








### Search





















