# CHR$
> The CHR$ function returns the character associated with a certain character code as a STRING .

## SYNTAX
`result$ = CHR$ ( code% )`

## DESCRIPTION
* Valid ASCII code% numbers range from 0 to 255.
* The character code of a character can be found using the [ASC](ASC.md) (function) .
* Some control codes below 32 will not [PRINT](PRINT.md) or will move the screen cursor, unless [_CONTROLCHR](_CONTROLCHR.md) [OFF](OFF.md) is used.


## EXAMPLES
> Example 1: Outputs the characters of several character codes:

```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```

> Example 2: To cut down on typing CHR$(???) all day, define often used characters as variables such as Q$ = CHR$(34) as shown.

```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```

> Example 3: Using ASC and CHR$ to encrypt a text file size up to 32K bytes

```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```

> Example 4: Decrypting the above encrypted text file (32K byte file size limit).

```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```


```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```

* [ASC](ASC.md) , [ASC](ASC.md) (function)
* INKEY$
* ASCII character codes

```vb
PRINT CHR$(65); CHR$(65 + 32)
PRINT CHR$(66); CHR$(66 + 32)
```



# SEE ALSO
* [ASC](ASC.md) , [ASC](ASC.md) (function)
* INKEY$
* ASCII character codes

