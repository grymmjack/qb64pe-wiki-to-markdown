# CDBL
> CDBL converts a value to the closest DOUBLE -precision value.

## SYNTAX
`doubleValue# = CDBL ( expression )`

## PARAMETERS
* expression is any [TYPE](TYPE.md) of literal or variable numerical value or mathematical calculation.


## DESCRIPTION
* Rounds to the closest [DOUBLE](DOUBLE.md) floating decimal point value.
* Also can be used to define a value as [DOUBLE](DOUBLE.md) -precision up to 15 decimals.


## EXAMPLES
> Example: Prints a double-precision version of the single-precision value stored in the variable named A.

```vb
A = 454.67
PRINT A; CDBL(A)
```


```vb
A = 454.67
PRINT A; CDBL(A)
```

* [CINT](CINT.md) , [CLNG](CLNG.md)
* [CSNG](CSNG.md) , [_ROUND](_ROUND.md)

```vb
A = 454.67
PRINT A; CDBL(A)
```



# SEE ALSO
* [CINT](CINT.md) , [CLNG](CLNG.md)
* [CSNG](CSNG.md) , [_ROUND](_ROUND.md)

