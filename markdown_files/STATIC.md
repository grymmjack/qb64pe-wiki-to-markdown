# STATIC
> The STATIC keyword is used in declaration statements to control where variables are stored.

## DESCRIPTION
* A [STATIC](STATIC.md) list can be used in [SUB](SUB.md) and [FUNCTION](FUNCTION.md) procedures to designate one or more variables to retain their values.
* Variables and arrays with static storage will retain their values in between procedure calls. The values may also be used recursively.


## EXAMPLES
> Example 1: Finding the binary bit settings from a 32 bit LONG register return using recursion.

```vb
INPUT "Enter a numerical value to see binary value: ", num&
PRINT BinStr$(num&)

END

FUNCTION BinStr$ (n&) STATIC 'comment out STATIC to see what happens!
DIM p%, s$
IF 2 ^ p% > n& THEN
 p% = 0
ELSE
 IF n& AND 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$
 IF n& > 2 ^ p% THEN
   p% = p% + 1
   s$ = BinStr$(n&) 'recursive call to itself
 ELSE: p% = 0
 END IF
END IF
IF s$ = "" THEN BinStr$ = "0" ELSE BinStr$ = s$
END FUNCTION
```

> Example 2: Using a static array to cache factorials, speeding up repeated calculations:

```vb
INPUT "Enter a numerical value to see binary value: ", num&
PRINT BinStr$(num&)

END

FUNCTION BinStr$ (n&) STATIC 'comment out STATIC to see what happens!
DIM p%, s$
IF 2 ^ p% > n& THEN
 p% = 0
ELSE
 IF n& AND 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$
 IF n& > 2 ^ p% THEN
   p% = p% + 1
   s$ = BinStr$(n&) 'recursive call to itself
 ELSE: p% = 0
 END IF
END IF
IF s$ = "" THEN BinStr$ = "0" ELSE BinStr$ = s$
END FUNCTION
```


```vb
INPUT "Enter a numerical value to see binary value: ", num&
PRINT BinStr$(num&)

END

FUNCTION BinStr$ (n&) STATIC 'comment out STATIC to see what happens!
DIM p%, s$
IF 2 ^ p% > n& THEN
 p% = 0
ELSE
 IF n& AND 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$
 IF n& > 2 ^ p% THEN
   p% = p% + 1
   s$ = BinStr$(n&) 'recursive call to itself
 ELSE: p% = 0
 END IF
END IF
IF s$ = "" THEN BinStr$ = "0" ELSE BinStr$ = s$
END FUNCTION
```

* [DIM](DIM.md) , [REDIM](REDIM.md) , [COMMON](COMMON.md)
* [SUB](SUB.md) , [FUNCTION](FUNCTION.md)
* [DECLARE](DECLARE.md) [LIBRARY](LIBRARY.md)
* [TYPE](TYPE.md) , Arrays
* $[STATIC](STATIC.md) , $[DYNAMIC](DYNAMIC.md)
* Data types

```vb
INPUT "Enter a numerical value to see binary value: ", num&
PRINT BinStr$(num&)

END

FUNCTION BinStr$ (n&) STATIC 'comment out STATIC to see what happens!
DIM p%, s$
IF 2 ^ p% > n& THEN
 p% = 0
ELSE
 IF n& AND 2 ^ p% THEN s$ = "1" + s$ ELSE s$ = "0" + s$
 IF n& > 2 ^ p% THEN
   p% = p% + 1
   s$ = BinStr$(n&) 'recursive call to itself
 ELSE: p% = 0
 END IF
END IF
IF s$ = "" THEN BinStr$ = "0" ELSE BinStr$ = s$
END FUNCTION
```



# SEE ALSO
* [DIM](DIM.md) , [REDIM](REDIM.md) , [COMMON](COMMON.md)
* [SUB](SUB.md) , [FUNCTION](FUNCTION.md)
* [DECLARE](DECLARE.md) [LIBRARY](LIBRARY.md)
* [TYPE](TYPE.md) , Arrays
* $[STATIC](STATIC.md) , $[DYNAMIC](DYNAMIC.md)
* Data types

