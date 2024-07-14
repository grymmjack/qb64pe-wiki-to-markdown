


MOD - QB64 Phoenix Edition Wiki








# MOD



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The MOD operator gives the remainder after division of one number by another (sometimes called modulus).


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*remainder* = *numerator* MOD *divisor*
  




## Parameters


* Returns the integer division remainder as a whole [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER"), [LONG](/qb64wiki/index.php/LONG "LONG") or [\_INTEGER64](/qb64wiki/index.php/INTEGER64 "INTEGER64") value.
* *numerator* is the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value to divide.
* *divisor* is the [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") value to divide by.


  




## Description


* Floating decimal point *numerator* and *divisor* values are [CINT](/qb64wiki/index.php/CINT "CINT") rounded (e.g. 19 MOD 6.7 returns 5 just like 19 MOD 7 would).
* MOD returns 0 if a number is evenly divisible by integer division ( [\](/qb64wiki/index.php/%5C "\") ) or the number divided is 0.
* ***divisor* (second value) must not be between 0 and .5**. This will create a ["Division by zero" error](/qb64wiki/index.php/ERROR_Codes "ERROR Codes") due to [CINT](/qb64wiki/index.php/CINT "CINT") rounding the value to 0.
* The result has the same sign as the numerator (e.g. -1 MOD 7 returns -1, not 6).
* Division and multiplication operations are performed before addition and subtraction in QBasic's order of operations.


  




## Examples


*Example 1:*





| ```   I% = 100 [\](/qb64wiki/index.php/%5C "\") 9   R% = 100 MOD 9   PRINT "Integer division ="; I%, "Remainder ="; R%  ``` |
| --- |




| ```   Integer division = 11        Remainder = 1  ``` |
| --- |


*Explanation:* Integer division 100 \ 9 returns 11. 11 [\*](/qb64wiki/index.php/* "*") 9 = 99. So the remainder must be 1 as 100 - 99 = 1. Normal decimal point division would return 11.11111.


  

*Example 2:* Comparing normal, integer and remainder division.





| ``` tmp1$ = " Normal:         ####.# / #### = ##.###   " tmp2$ = " Integer:        ####.# \ #### = ###      " tmp3$ = " Remainder:    ####.# MOD #### = ####     " FOR i = 1 TO 6    SELECT CASE i      CASE 1: numerator = 1: divisor = 5      CASE 2: numerator = 13: divisor = 10      CASE 3: numerator = 990: divisor = 100      CASE 4: numerator = 1100: divisor = 100      CASE 5: numerator = 4501: divisor = 1000      CASE 6: numerator = 50.6: divisor = 10    END SELECT LOCATE 5, 20: PRINT USING tmp1$; numerator; divisor; numerator / divisor LOCATE 7, 20: PRINT USING tmp2$; numerator; divisor; numerator \ divisor LOCATE 9, 20: PRINT USING tmp3$; numerator; divisor; numerator MOD divisor DO: SLEEP: LOOP UNTIL INKEY$ <> "" NEXT  ``` |
| --- |


  

*Example 3:* Integer division and MOD can be used to convert values to different base numbering systems from base 2 to 36 as [strings](/qb64wiki/index.php/STRING "STRING"):





| ``` [CLS](/qb64wiki/index.php/CLS "CLS") DO   [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Enter a base number system 2 to 36: ", b%   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") b% < 2 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") b% > 36 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Enter a positive value to convert: ";   num$ = ""   [DO](/qb64wiki/index.php/DO...LOOP "DO...LOOP"): K$ = [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$")     num$ = num$ + K$     [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") [CSRLIN](/qb64wiki/index.php/CSRLIN "CSRLIN"), [POS](/qb64wiki/index.php/POS "POS")(0): [PRINT](/qb64wiki/index.php/PRINT "PRINT") K$;   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") K$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(13)   n& = [VAL](/qb64wiki/index.php/VAL "VAL")(num$)   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") n& = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT DO](/qb64wiki/index.php/EXIT_DO "EXIT DO")   Bnum$ = BASEN$(n&, b%)   [PRINT](/qb64wiki/index.php/PRINT "PRINT") Bnum$ ', [VAL](/qb64wiki/index.php/VAL "VAL")("[&H](/qb64wiki/index.php/%26H "&H")" + Bnum$) 'tests hexadecimal base 16 only [LOOP](/qb64wiki/index.php/LOOP "LOOP")  [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") BASEN$ (number&, basenum%) [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") basenum% < 2 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") basenum% > 36 [OR](/qb64wiki/index.php/OR_(boolean) "OR (boolean)") number& = 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION") num& = number& 'protect value of number! DO   remain% = [ABS](/qb64wiki/index.php/ABS "ABS")(num&) MOD basenum% ' remainder is used to create actual digit 0 to Z   num& = num& \ basenum% ' move up one exponent of base% with integer division   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") remain% > 9 [THEN](/qb64wiki/index.php/THEN "THEN")     b$ = [CHR$](/qb64wiki/index.php/CHR$ "CHR$")(65 + (remain% - 10)) 'limited to base 36   [ELSE](/qb64wiki/index.php/ELSE "ELSE"): b$ = [LTRIM$](/qb64wiki/index.php/LTRIM$ "LTRIM$")([STR$](/qb64wiki/index.php/STR$ "STR$")(remain%)) ' make remainder a string number   [END IF](/qb64wiki/index.php/END_IF "END IF")   BN$ = b$ + BN$ ' add remainder character to base number string [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") num& = 0 BASEN$ = BN$ [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


*Note:* Base numbering systems over base 10(0 - 9) use alphabetical letters to represent digits greater than 9 like [Hexadecimal](/qb64wiki/index.php/%26H "&H")(0 - F).
  




## See also


* [Featured in our "Keyword of the Day" series](https://qb64phoenix.com/forum/showthread.php?tid=1196)
* [/ (normal division operator)](/qb64wiki/index.php// "/")
* [\ (integer division operator)](/qb64wiki/index.php/%5C "\")
* [INT](/qb64wiki/index.php/INT "INT"), [CINT](/qb64wiki/index.php/CINT "CINT"), [FIX](/qb64wiki/index.php/FIX "FIX"), [\_ROUND](/qb64wiki/index.php/ROUND "ROUND"), [\_CEIL](/qb64wiki/index.php/CEIL "CEIL")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MOD&oldid=8902>"




## Navigation menu








### Search





















