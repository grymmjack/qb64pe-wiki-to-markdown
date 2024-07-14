


\_BYTE - QB64 Phoenix Edition Wiki








# \_BYTE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
A \_BYTE variable can hold signed variable values from -128 to 127 (one byte or 8 [\_BITs](/qb64wiki/index.php/BIT "BIT")). [Unsigned](/qb64wiki/index.php/UNSIGNED "UNSIGNED") from 0 to 255.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


[DIM](/qb64wiki/index.php/DIM "DIM") *byte* [AS](/qb64wiki/index.php/AS "AS") [[[\_UNSIGNED] \_BYTE
  




## Description


* Signed \_BYTE values can range from -128 to 127.
* [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") \_BYTEs can hold values from 0 to 255. [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") expands the range of positive values.
* Can be defined in a **QB64** [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE") statement using a starting letter range of variable names.
* Also can be used in a subroutine parameter [AS](/qb64wiki/index.php/AS "AS") \_BYTE variable definitions.
* Define a byte using the suffix %% after the variable name: *variable%%* = -54
* Define an unsigned byte by adding the suffix ~%% after the variable name: variable~%% = 54
* **When a variable has not been assigned or has no type suffix, the value defaults to [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").**


  




**[BITS](/qb64wiki/index.php/BIT "BIT")**
* The **MSB** is the most significant(largest) bit value and **LSB** is the least significant bit of a binary or register memory address value. The order in which the bits are read determines the binary or decimal byte value. There are two common ways to read a byte:


* **"Big-endian"**: MSB is the first bit encountered, decreasing to the LSB as the last bit by position, memory address or time.
* **"Little-endian"**: LSB is the first bit encountered, increasing to the MSB as the last bit by position, memory address or time.



| ```          **Offset or Position:    0    1   2   3   4   5   6   7      Example: 11110000**                               ----------------------------------             --------     **Big-Endian Bit On Value:**   128  64  32  16   8   4   2   1                 240  **Little-Endian Bit On Value:**    1    2   4   8  16  32  64  128                 15  ``` |
| --- |


The big-endian method compares exponents of 2 ^ 7 down to 2 ^ 0 while the little-endian method does the opposite.
  




**BYTES**
* [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") values consist of 2 bytes called the **HI** and **LO** bytes. Anytime that the number of binary digits is a multiple of 16 (2bytes, 4 bytes, etc.) and the HI byte's MSB is on(1), the value returned will be negative. Even with [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") values!




| ```                                  **16 BIT INTEGER OR REGISTER**               **AH (High Byte Bits)                         AL (Low Byte Bits)**    BIT:    15    14   13   12   11   10   9   8  |   7   6    5   4    3    2   1    0           ---------------------------------------|--------------------------------------    HEX:   8000  4000 2000 1000  800 400  200 100 |  80   40  20   10   8    4   2    1  ``` | DEC: -32768 16384 8192 4096 2048 1024 512 256 | 128 64 32 16 8 4 2 1 |
| --- | --- |


The HI byte's **MSB** is often called the **sign** bit! When all 16 of the integer binary bits are on, the decimal return is -1.
  




## Examples


How negative assignments affect the \_UNSIGNED value returned by a byte (8 bits).


| ``` [DIM](/qb64wiki/index.php/DIM "DIM") unsig [AS](/qb64wiki/index.php/AS "AS") [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") _BYTE [DIM](/qb64wiki/index.php/DIM "DIM") sig [AS](/qb64wiki/index.php/AS "AS") _BYTE  [CLS](/qb64wiki/index.php/CLS "CLS") unsig = 1 sig = 1 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "&B00000001 = unsigned & signed are both" + [STR$](/qb64wiki/index.php/STR$ "STR$")(unsig [AND](/qb64wiki/index.php/AND "AND") sig)  unsig = 127 sig = 127 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "&B01111111 = unsigned & signed are both" + [STR$](/qb64wiki/index.php/STR$ "STR$")(unsig [AND](/qb64wiki/index.php/AND "AND") sig)  unsig = 255 sig = 255 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "&B11111111 = unsigned is" + [STR$](/qb64wiki/index.php/STR$ "STR$")(unsig) + " but signed is " + [STR$](/qb64wiki/index.php/STR$ "STR$")(sig)  unsig = 254 sig = 254 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "&B11111110 = unsigned is" + [STR$](/qb64wiki/index.php/STR$ "STR$")(unsig) + " but signed is " + [STR$](/qb64wiki/index.php/STR$ "STR$")(sig)  unsig = 253 sig = 253 [PRINT](/qb64wiki/index.php/PRINT "PRINT") "&B11111101 = unsigned is" + [STR$](/qb64wiki/index.php/STR$ "STR$")(unsig) + " but signed is " + [STR$](/qb64wiki/index.php/STR$ "STR$")(sig)  [PRINT](/qb64wiki/index.php/PRINT "PRINT") [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The signed value needs the MSB bit for the sign." [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The most significant bit is furthest to the left."  ``` |
| --- |




| ``` &B00000001 = unsigned & signed are both 1 &B01111111 = unsigned & signed are both 127 &B11111111 = unsigned is 255 but signed is -1 &B11111110 = unsigned is 254 but signed is -2 &B11111101 = unsigned is 253 but signed is -3  The signed value needs the MSB bit for the sign. The most significant bit is furthest to the left.  ``` |
| --- |


  




## See also


* [\_BIT](/qb64wiki/index.php/BIT "BIT"), [&B](/qb64wiki/index.php/%26B "&B")
* [\_DEFINE](/qb64wiki/index.php/DEFINE "DEFINE"), [DIM](/qb64wiki/index.php/DIM "DIM")
* [\_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED")
* [\_SHL](/qb64wiki/index.php/SHL "SHL"), [\_SHR](/qb64wiki/index.php/SHR "SHR")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Screen Memory](/qb64wiki/index.php/Screen_Memory "Screen Memory")
* [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types")
* [Converting Bytes to Bits](/qb64wiki/index.php/Converting_Bytes_to_Bits "Converting Bytes to Bits")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=BYTE&oldid=8275>"




## Navigation menu








### Search





















