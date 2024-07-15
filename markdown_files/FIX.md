# FIX
> The FIX function rounds a numerical value to the next whole number closest to zero.

## SYNTAX
`result = FIX ( expression )`

## PARAMETERS
* expression is any type of literal or variable numerical value or mathematical calculation.


## DESCRIPTION
* [FIX](FIX.md) effectively truncates (removes) the fractional part of expression , returning the integer part. This means that [FIX](FIX.md) rounds down for positive values and up for negative values.
	* This means that [FIX](FIX.md) rounds down for positive values and up for negative values.
* This means that [FIX](FIX.md) rounds down for positive values and up for negative values.
* Use [INT](INT.md) to round down negative values. Positive values are rounded down by both.


## EXAMPLES
> Example 1: Showing the behavior of FIX with positive and negative decimal point values.

```vb
PRINT FIX(2.5)
PRINT FIX(-2.5)
```

> Example 2: The NORMAL arithmetic method (round half up) can be achieved using the function in the example code below:

```vb
PRINT FIX(2.5)
PRINT FIX(-2.5)
```


```vb
PRINT FIX(2.5)
PRINT FIX(-2.5)
```

* [_CEIL](_CEIL.md)
* [INT](INT.md) , [CINT](CINT.md)
* [CLNG](CLNG.md) , [_ROUND](_ROUND.md)
* [MOD](MOD.md) , Integer Division
* Normal division

```vb
PRINT FIX(2.5)
PRINT FIX(-2.5)
```



# SEE ALSO
* [_CEIL](_CEIL.md)
* [INT](INT.md) , [CINT](CINT.md)
* [CLNG](CLNG.md) , [_ROUND](_ROUND.md)
* [MOD](MOD.md) , Integer Division
* Normal division

