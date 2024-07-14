


SQR - QB64 Phoenix Edition Wiki








# SQR



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **SQR** function returns the square root of a numerical value.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Examples](#Examples) * [4 See also](#See_also) |
| --- |


## Syntax


square\_root = **SQR(**value**)**
  




## Description


* The *square root* returned is normally a [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") or [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") numerical value.
* The *value* parameter can be any **positive** numerical type. **Negative parameter values will not work!**
* Other exponential root functions can use fractional exponents([^](/qb64wiki/index.php/%5E "^")) enclosed in **parenthesis only**. EX: root = c ^ (a / b)


  




## Examples


*Example 1:* Finding the hypotenuse of a right triangle:





| ```  A% = 3: B% = 4  PRINT "hypotenuse! ="; SQR((A% ^ 2) + (B% ^ 2))  ``` |
| --- |




| ```  hypotenuse = 5  ``` |
| --- |


  

*Example 2:* Finding the Cube root of a number.





| ```  number = 8  cuberoot = number [^](/qb64wiki/index.php/%5E "^") (1/3)  PRINT cuberoot  ``` |
| --- |




| ```  2  ``` |
| --- |


  

*Example 3:* Negative roots return fractional values of one.





| ```  number = 8  negroot = number [^](/qb64wiki/index.php/%5E "^") -2  PRINT negroot  ``` |
| --- |




| ```  .015625  ``` |
| --- |


*Explanation:* A negative root means that the exponent value is actually inverted to a fraction of 1. So x ^ -2 actually means the result will be: 1 / (x ^ 2).
  

*Example 4:* Fast Prime number checker limits the numbers checked to the square root (half way).





| ``` DEFLNG P DO PRIME = -1   'set PRIME as True INPUT "Enter any number to check up to 2 million (Enter quits): ", guess$ PR = [VAL](/qb64wiki/index.php/VAL "VAL")(guess$) IF PR [MOD](/qb64wiki/index.php/MOD "MOD") 2 THEN              'check for even number   FOR P = 3 TO SQR(PR) STEP 2 'largest number that could be a multiple is the SQR     IF PR [MOD](/qb64wiki/index.php/MOD "MOD") P = 0 THEN PRIME = 0: EXIT FOR 'MOD = 0 when evenly divisible by another   NEXT ELSE : PRIME = 0 'number to be checked is even so it cannot be a prime END IF IF PR = 2 THEN PRIME = -1 '2 is the ONLY even prime IF PR = 1 THEN PRIME = 0  'MOD returns true but 1 is not a prime by definition IF PRIME THEN PRINT "PRIME! How'd you find me? " ELSE PRINT "Not a prime, you lose!" LOOP UNTIL PR = 0  ``` |
| --- |




| ``` Enter any number to check up to 2 million (Enter quits): 12379 PRIME! How'd you find me?  ``` |
| --- |


*Note:* Prime numbers cannot be evenly divided by any other number except one.
  




## See also


* [MOD](/qb64wiki/index.php/MOD "MOD")
* [^](/qb64wiki/index.php/%5E "^")
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=SQR&oldid=7965>"




## Navigation menu








### Search





















