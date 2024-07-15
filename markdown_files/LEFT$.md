# LEFT$
> The LEFT$ string function returns a number of characters from the left of a STRING .

## SYNTAX
`LEFT$ ( stringValue$ , numberOfCharacters% )`

## PARAMETERS
* stringValue$ can be any [STRING](STRING.md) literal or variable.
* numberOfCharacters% [INTEGER](INTEGER.md) determines the number of characters to return from left of string.


## DESCRIPTION
* If the number of characters exceeds the string length the entire string is returned. Use [LEN](LEN.md) to determine a string's length.
* LEFT$ returns always start at the first character of the string, even if it's a space. LTRIM$ can remove leading spaces.
* numberOfCharacters% cannot be a negative value.


## EXAMPLES
> Example 1: Getting the left portion of a string value.

```vb
name$ = "Tom Williams"

First$ = LEFT$(name$, 3)

PRINT First$
```

> Example 2: A replace function using LEFT$ and RIGHT$ with INSTR to insert a different length word into an existing string.

```vb
name$ = "Tom Williams"

First$ = LEFT$(name$, 3)

PRINT First$
```


```vb
name$ = "Tom Williams"

First$ = LEFT$(name$, 3)

PRINT First$
```

* RIGHT$ , MID$ (function)
* LTRIM$ , RTRIM$
* [INSTR](INSTR.md) , [LEN](LEN.md)

```vb
name$ = "Tom Williams"

First$ = LEFT$(name$, 3)

PRINT First$
```



# SEE ALSO
* RIGHT$ , MID$ (function)
* LTRIM$ , RTRIM$
* [INSTR](INSTR.md) , [LEN](LEN.md)

