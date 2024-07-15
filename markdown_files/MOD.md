# MOD
> The MOD operator gives the remainder after division of one number by another (sometimes called modulus).

## SYNTAX
`remainder = numerator MOD divisor`

## PARAMETERS
* Returns the integer division remainder as a whole [INTEGER](INTEGER.md) , [LONG](LONG.md) or [_INTEGER64](_INTEGER64.md) value.
* numerator is the [INTEGER](INTEGER.md) value to divide.
* divisor is the [INTEGER](INTEGER.md) value to divide by.


## DESCRIPTION
* Floating decimal point numerator and divisor values are [CINT](CINT.md) rounded (e.g. 19 [MOD](MOD.md) 6.7 returns 5 just like 19 [MOD](MOD.md) 7 would).
* [MOD](MOD.md) returns 0 if a number is evenly divisible by integer division ( \ ) or the number divided is 0.
* divisor (second value) must not be between 0 and .5 . This will create a "Division by zero" error due to [CINT](CINT.md) rounding the value to 0.
* The result has the same sign as the numerator (e.g. -1 [MOD](MOD.md) 7 returns -1, not 6).
* Division and multiplication operations are performed before addition and subtraction in QBasic's order of operations.


## EXAMPLES
> Example 1:

```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```

> Explanation: Integer division 100 \ 9 returns 11. 11 * 9 = 99. So the remainder must be 1 as 100 - 99 = 1. Normal decimal point division would return 11.11111.

```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```

> Example 2: Comparing normal, integer and remainder division.

```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```

> Example 3: Integer division and MOD can be used to convert values to different base numbering systems from base 2 to 36 as strings :

```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```


```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```

* Featured in our "Keyword of the Day" series
* / (normal division operator)
* \ (integer division operator)
* [INT](INT.md) , [CINT](CINT.md) , [FIX](FIX.md) , [_ROUND](_ROUND.md) , [_CEIL](_CEIL.md)
* Mathematical Operations

```vb
I% = 100 \ 9
 R% = 100 MOD 9
 PRINT "Integer division ="; I%, "Remainder ="; R%
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* / (normal division operator)
* \ (integer division operator)
* [INT](INT.md) , [CINT](CINT.md) , [FIX](FIX.md) , [_ROUND](_ROUND.md) , [_CEIL](_CEIL.md)
* Mathematical Operations

