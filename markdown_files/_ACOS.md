


\_ACOS - QB64 Phoenix Edition Wiki








# \_ACOS



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_ACOS function returns the angle measured in radians based on an input [COSine](/qb64wiki/index.php/COS "COS") value ranging from -1 to 1.


  






| Contents * [1 Syntax](#Syntax) * [2 Description](#Description) * [3 Availability](#Availability) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


*radian\_angle!* = \_ACOS(*cosine\_value!*)
  




## Description


* The *cosine\_value!* must be measured >= -1 and <= 1, or an error will be generated. (PRINT \_ACOS(1.2) would give the result of -1.#IND, which is basically QB64's way of telling us that the number doesn't exist, much like 1/0 would.)
* ARCCOSINE is the inverse function of [COSine](/qb64wiki/index.php/COS "COS"), which lets us turn a [COSine](/qb64wiki/index.php/COS "COS") value back into an angle.
* Note: Due to rounding with floating point math, the \_ACOS may not always give a perfect match for the COS angle which generated this. You can reduce the number of rounding errors by increasing the precision of your calculations by using [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE") or [\_FLOAT](/qb64wiki/index.php/FLOAT "FLOAT") precision variables instead of [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE").


  




## Availability


* **Version 1.000 and up.**


  




## Examples


*Example:* Converting a radian angle to its COSine and using that value to find the angle in degrees again using \_ACOS:





| ``` [DEFDBL](/qb64wiki/index.php/DEFDBL "DEFDBL") A-Z  [INPUT](/qb64wiki/index.php/INPUT "INPUT") "Give me an Angle (in Degrees) => "; Angle [PRINT](/qb64wiki/index.php/PRINT "PRINT") C = [COS](/qb64wiki/index.php/COS "COS")([_D2R](/qb64wiki/index.php/D2R "D2R")(Angle)) '_D2R is the command to convert Degrees to Radians, which is what COS expects [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The COSINE of the Angle is: "; C A = _ACOS(C) [PRINT](/qb64wiki/index.php/PRINT "PRINT") "The ACOS of "; C; " is: "; A [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Notice, A is the Angle in Radians.  If we convert it to degrees, the value is "; [_R2D](/qb64wiki/index.php/R2D "R2D")(A)  ``` |
| --- |


Example by SMcNeill


| ``` Give me an Angle (in Degrees) => ? 60  The COSINE of the Angle is:  .5000000000000001 The ACOS of  .5000000000000001  is:  1.047197551196598 Notice, A is the Angle in Radians.  If we convert it to degrees, we discover the value is  60  ``` |
| --- |


  




## See also


* [\_D2G](/qb64wiki/index.php/D2G "D2G") (degree to gradient, [\_D2R](/qb64wiki/index.php/D2R "D2R") (degree to radian)
* [\_G2D](/qb64wiki/index.php/G2D "G2D") (gradient to degree), [\_G2R](/qb64wiki/index.php/G2R "G2R") (gradient to degree
* [\_R2D](/qb64wiki/index.php/R2D "R2D") (radian to degree), [\_R2G](/qb64wiki/index.php/R2G "R2G") (radian to gradient
* [COS](/qb64wiki/index.php/COS "COS") (cosine), [SIN](/qb64wiki/index.php/SIN "SIN") (sine), [TAN](/qb64wiki/index.php/TAN "TAN") (tangent)
* [\_ASIN](/qb64wiki/index.php/ASIN "ASIN") (arc sine), [ATN](/qb64wiki/index.php/ATN "ATN") (arc tangent)
* [\_ACOSH](/qb64wiki/index.php/ACOSH "ACOSH") (arc hyperbolic cosine), [\_ASINH](/qb64wiki/index.php/ASINH "ASINH") (arc hyperbolic sine), [\_ATANH](/qb64wiki/index.php/ATANH "ATANH") (arc hyperbolic tangent)
* [\_ATAN2](/qb64wiki/index.php/ATAN2 "ATAN2") (Compute arc tangent with two parameters)
* [\_HYPOT](/qb64wiki/index.php/HYPOT "HYPOT") (hypotenuse)
* [Mathematical Operations](/qb64wiki/index.php/Mathematical_Operations "Mathematical Operations")
* [Derived Mathematical Functions](/qb64wiki/index.php/Mathematical_Operations#Derived_Mathematical_Functions "Mathematical Operations")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=ACOS&oldid=8254>"




## Navigation menu








### Search





















