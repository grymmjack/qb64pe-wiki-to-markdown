


\_BIT - QB64 Phoenix Edition Wiki








# \_BIT



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_BIT datatype can return only values of 0 (bit off) and -1 (bit on).


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *variable* [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] \_BIT [\* *numberofbits*]
[\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") *Letter*[*-Range*|,...] [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] \_BIT [\* *numberofbits*]
  




## Description


* An [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") \_BIT can hold 0 or 1 instead of 0 and -1, if you set the numberofbits you can hold larger values depending on the number of bits you have set (\_BIT \* 8 can hold the same values as [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") for example) and the information below is compromised if setting any number of bits other than 1.
* If you set the variable to any other number then the least significant bit of that number will be set as the variables number, if the bit is 1 (on) then the variable will be -1 and if the bit is 0 (off) then the variable will be 0.
* The least significant bit is the last bit on a string of bits (11111) since that bit will only add 1 to the value if set. The most significant bit is the first bit on a string of bits and changes the value more dramatically (significantly) if set on or off.
* The \_BIT datatype can be succesfully used as a [Boolean](/qb64wiki/index.php/Boolean "Boolean") (TRUE or FALSE) and it requires minimal amount of memory (the lowest amount possible actually, one byte can hold 8 bits, if you want to use bits in order to decrease memory usage, use them as arrays as a \_BIT variable by itself allocates 4 bytes - DIM bitarray(800) AS \_BIT uses 100 bytes).
* **When a variable has not been assigned or has no type suffix, the value defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**
* **[\_BIT is not supported in User Defined TYPES.](/qb64wiki/index.php/Keywords_currently_not_supported_by_QB64 "Keywords currently not supported by QB64")** Use a [\_BYTE](/qb64wiki/index.php/BYTE "BYTE") and assign up to 8 bit values as shown below.


  




* **Suffix Symbols** The \_BIT type suffix used is below the grave accent (`), usually located under the tilde (~) key (not an apostrophe). Foreign keyboards may not have the ` key. Try Alt+96 in the IDE.


You can define a bit on-the-fly by adding a ` after the variable, like this: variable` = -1
If you want an unsigned bit you can define it on-the-fly by adding ~` instead, like this: variable~` = 1
You can set the number of bits on the fly by just adding that number - this defines it as being two bits: variable`2 = -1
  




**BITS**
* The **MSB** is the most significant(largest) bit value and **LSB** is the least significant bit of a binary or register memory address value. The order in which the bits are read determines the binary or decimal byte value. There are two common ways to read a byte:


* **"Big-endian"**: MSB is the first bit encountered, decreasing to the LSB as the last bit by position, memory address or time.
* **"Little-endian"**: LSB is the first bit encountered, increasing to the MSB as the last bit by position, memory address or time.



| ```          **Offset or Position:    0    1   2   3   4   5   6   7      Example: 11110000**                               ----------------------------------             --------     **Big-Endian Bit On Value:**   128  64  32  16   8   4   2   1                 240  **Little-Endian Bit On Value:**    1    2   4   8  16  32  64  128                 15  ``` |
| --- |


The big-endian method compares exponents of 2 ^ 7 down to 2 ^ 0 while the little-endian method does the opposite.
**[BYTES](/qb64wiki/index.php/BYTE "BYTE")**
* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values consist of 2 bytes called the **HI** and **LO** bytes. Anytime that the number of binary digits is a multiple of 16 (2bytes, 4 bytes, etc.) and the HI byte's MSB is on(1), the value returned will be negative. Even with [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") values!




| ```                                  **16 BIT INTEGER OR REGISTER**               **AH (High Byte Bits)                         AL (Low Byte Bits)**    BIT:    15    14   13   12   11   10   9   8  |   7   6    5   4    3    2   1    0           ---------------------------------------|--------------------------------------    HEX:   8000  4000 2000 1000  800 400  200 100 |  80   40  20   10   8    4   2    1                                                  |    DEC: -32768 16384 8192 4096 2048 1024 512 256 | 128   64  32   16   8    4   2    1  ``` |
| --- |


The HI byte's **MSB** is often called the **sign** bit! When all 16 of the integer binary bits are on, the decimal return is -1.
  




## Examples


*Example:* Shifting bits in a value in QB64 versions prior to 1.3 (you can use [\_SHL](/qb64wiki/index.php/SHL "SHL") and [\_SHR](/qb64wiki/index.php/SHR "SHR") starting with version 1.3).





| ``` n = 24 Shift = 3  [PRINT](/qb64wiki/index.php/PRINT "PRINT") LShift(n, Shift) [PRINT](/qb64wiki/index.php/PRINT "PRINT") RShift(n, Shift) [END](/qb64wiki/index.php/END "END")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") LShift& (n [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), LS [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [IF](/qb64wiki/index.php/IF "IF") LS < 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")     LShift = [INT](/qb64wiki/index.php/INT "INT")(n * (2 ^ LS)) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  [FUNCTION](/qb64wiki/index.php/FUNCTION "FUNCTION") RShift& (n [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), RS [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"))     [IF](/qb64wiki/index.php/IF "IF") RS < 0 [THEN](/qb64wiki/index.php/THEN "THEN") [EXIT FUNCTION](/qb64wiki/index.php/EXIT_FUNCTION "EXIT FUNCTION")     RShift = [INT](/qb64wiki/index.php/INT "INT")(n / (2 ^ RS)) [END FUNCTION](/qb64wiki/index.php/END_FUNCTION "END FUNCTION")  ``` |
| --- |


Adapted from code by RThorpe


| ```  192  3  ``` |
| --- |


  




## See also


* [&B](/qb64wiki/index.php/%26B "&B") (binary), [\_BYTE](/qb64wiki/index.php/BYTE "BYTE")
* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [DIM](/qb64wiki/index.php/DIM "DIM")
* [Binary](/qb64wiki/index.php/Binary "Binary"), [Boolean](/qb64wiki/index.php/Boolean "Boolean")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")
* [Converting Bytes to Bits](/qb64wiki/index.php/Converting_Bytes_to_Bits "Converting Bytes to Bits")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BIT&oldid=8266>"




## Navigation menu








### Search





















