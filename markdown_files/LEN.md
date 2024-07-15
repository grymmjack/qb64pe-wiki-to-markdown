# LEN
> The LEN function returns the number of bytes used by a variable value or the number of characters in a STRING . In QB64 it can also return the size of an array or TYPE variable.

## SYNTAX
`length% = LEN ( literalTextOrVariable )`

## EXAMPLES
> Example 1: With a string variable the byte size is the same as the number of characters.

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```

> Example 2: Testing INPUT for numerical STRING entries from a user.

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```

> Example 3: With numerical value types you MUST use a variable to find the inherent byte length when using LEN.

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```

> Example 4: Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```

> Example 5: Find the size of arrays and array elements.

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```


```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```

* [LOF](LOF.md) , [EOF](EOF.md)
* [AS](AS.md) , [TYPE](TYPE.md)
* [RANDOM](RANDOM.md) , [BINARY](BINARY.md)
* Variable Types

```vb
LastName$ = "Williams"
PRINT LEN(LastName$); "bytes"
```



# SEE ALSO
* [LOF](LOF.md) , [EOF](EOF.md)
* [AS](AS.md) , [TYPE](TYPE.md)
* [RANDOM](RANDOM.md) , [BINARY](BINARY.md)
* Variable Types

