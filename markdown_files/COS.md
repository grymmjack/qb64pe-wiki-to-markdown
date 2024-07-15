# COS
> The COS function returns the horizontal component or the cosine of an angle measured in radians.

## SYNTAX
`value! = COS ( radianAngle! )`

## PARAMETERS
* The radianAngle! must be measured in radians.


## DESCRIPTION
* To convert from degrees to radians, multiply degrees * π / 180.
* [COS](COS.md) INE is the horizontal component of a unit vector in the direction theta (θ).
* [COS](COS.md)(x) can be calculated in either [SINGLE](SINGLE.md) or [DOUBLE](DOUBLE.md) precision depending on its argument.


## EXAMPLES
> Example 1: Converting degree angles to radians for QBasic's trig functions and drawing the line at the angle.

```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```

> Example 2: Creating 12 analog clock hour points using CIRCLEs and PAINT

```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```

> Explanation: The 12 circles are placed at radian angles that are 1/12 of 6.28318 or .523598 radians apart.

```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```

> Example 3: Creating a rotating spiral with COS and SIN .

```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```


```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```

* [_PI](_PI.md) (QB64 function)
* [SIN](SIN.md) (sine)
* [ATN](ATN.md) (arctangent)
* [TAN](TAN.md) (tangent)
* Mathematical Operations
* Derived Mathematical Functions

```vb
SCREEN 12
PI = 4 * ATN(1)
PRINT "PI = 4 * ATN(1) ="; PI
PRINT "COS(PI) = "; COS(PI)
PRINT "SIN(PI) = "; SIN(PI)
DO
 PRINT
 INPUT "Enter the degree angle (0 quits): ", DEGREES%
 RADIANS = DEGREES% * PI / 180
 PRINT "RADIANS = DEGREES% * PI / 180 = "; RADIANS
 PRINT "X = COS(RADIANS) = "; COS(RADIANS)
 PRINT "Y = SIN(RADIANS) = "; SIN(RADIANS)
 CIRCLE (400, 240), 2, 12
 LINE (400, 240)-(400 + (50 * SIN(RADIANS)), 240 + (50 * COS(RADIANS))), 11
 DEGREES% = RADIANS * 180 / PI
 PRINT "DEGREES% = RADIANS * 180 / PI ="; DEGREES%
LOOP UNTIL DEGREES% = 0
```



# SEE ALSO
* [_PI](_PI.md) (QB64 function)
* [SIN](SIN.md) (sine)
* [ATN](ATN.md) (arctangent)
* [TAN](TAN.md) (tangent)
* Mathematical Operations
* Derived Mathematical Functions

