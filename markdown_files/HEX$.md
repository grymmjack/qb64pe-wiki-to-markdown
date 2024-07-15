# HEX$
> This function returns the hexadecimal (base 16) representation of any numeric value.

## SYNTAX
`hexvalue$ = HEX$ ( number )`

## PARAMETERS
* number can be any [INTEGER](INTEGER.md) , [LONG](LONG.md) or [_INTEGER64](_INTEGER64.md) value, positive or negative.
* number can also be any [SINGLE](SINGLE.md) , [DOUBLE](DOUBLE.md) or [_FLOAT](_FLOAT.md) value, but only the integer part of the value is converted in that case. That is, from the value -123.45 the function would convert the -123 only.


## DESCRIPTION
* The function returns the base 16 (hexadecimal) representation of the given number as [STRING](STRING.md) .
* Different from STR$ , this function does not return a leading sign placeholder space, so no LTRIM$ to strip that space from positive numbers is necessary.
* [VAL](VAL.md) can convert the returned hex string value back to a decimal value by prefixing the string with " &H ". Eg. decimal = [VAL](VAL.md) ("&H" + hexvalue$) .
	* Eg. decimal = [VAL](VAL.md) ("&H" + hexvalue$) .
* Eg. decimal = [VAL](VAL.md) ("&H" + hexvalue$) .


## EXAMPLES

```vb
tabletop$ = " Decimal | Hexadecimal | Octal | Binary "
tablesep$ = "---------+-------------+-------+--------"
tableout$ = "  \ \    |      \\     |   \\  |  \  \  " 'the PRINT USING template

LOCATE 2, 10: PRINT tabletop$
LOCATE 3, 10: PRINT tablesep$
FOR n% = 0 TO 15
   LOCATE 4 + n%, 10: PRINT USING tableout$; STR$(n%); HEX$(n%); OCT$(n%); _BIN$(n%)
NEXT n%
```


```vb
tabletop$ = " Decimal | Hexadecimal | Octal | Binary "
tablesep$ = "---------+-------------+-------+--------"
tableout$ = "  \ \    |      \\     |   \\  |  \  \  " 'the PRINT USING template

LOCATE 2, 10: PRINT tabletop$
LOCATE 3, 10: PRINT tablesep$
FOR n% = 0 TO 15
   LOCATE 4 + n%, 10: PRINT USING tableout$; STR$(n%); HEX$(n%); OCT$(n%); _BIN$(n%)
NEXT n%
```

* _BIN$ , OCT$ , STR$
* &B (binary), &H (hexadecimal), &O (octal), [VAL](VAL.md)
* Base Comparisons
* HEX$ 32 Bit Values

```vb
tabletop$ = " Decimal | Hexadecimal | Octal | Binary "
tablesep$ = "---------+-------------+-------+--------"
tableout$ = "  \ \    |      \\     |   \\  |  \  \  " 'the PRINT USING template

LOCATE 2, 10: PRINT tabletop$
LOCATE 3, 10: PRINT tablesep$
FOR n% = 0 TO 15
   LOCATE 4 + n%, 10: PRINT USING tableout$; STR$(n%); HEX$(n%); OCT$(n%); _BIN$(n%)
NEXT n%
```



# SEE ALSO
* _BIN$ , OCT$ , STR$
* &B (binary), &H (hexadecimal), &O (octal), [VAL](VAL.md)
* Base Comparisons
* HEX$ 32 Bit Values

