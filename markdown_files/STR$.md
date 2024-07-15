# STR$
> The STR$ function returns the STRING representation of a numerical value.

## SYNTAX
`result$ = STR$( number )`

## PARAMETERS
* number is any numerical type value to convert.


## DESCRIPTION
* Returns any type number value with leading sign(space/minus) or decimal point when one exists in the numerical value.
* If number is positive, the [STRING](STRING.md) value returned will have a leading space character which can be removed using LTRIM$ .
* If number is negative, the minus sign will precede the number instead of a space which LTRIM$ will not remove.
* Trimming a STR$ string number using RTRIM$ is not required as [PRINT](PRINT.md) creates the undocumented trailing number space.


## EXAMPLES

```vb
PRINT STR$( 1.0 )
PRINT STR$( 2.3 )
PRINT STR$( -4.5 )
```


```vb
PRINT STR$( 1.0 )
PRINT STR$( 2.3 )
PRINT STR$( -4.5 )
```

* [VAL](VAL.md) , [STRING](STRING.md)
* LTRIM$ , MID$ (function)
* RIGHT$ , LEFT$
* HEX$ , OCT$

```vb
PRINT STR$( 1.0 )
PRINT STR$( 2.3 )
PRINT STR$( -4.5 )
```



# SEE ALSO
* [VAL](VAL.md) , [STRING](STRING.md)
* LTRIM$ , MID$ (function)
* RIGHT$ , LEFT$
* HEX$ , OCT$

