# LTRIM$
> The LTRIM$ function removes leading space characters from a STRING value.

## SYNTAX
`return$ = LTRIM$ ( text$ )`

## DESCRIPTION
* text$ is the [STRING](STRING.md) value to trim.
* If text$ contains no leading space characters, it is returned unchanged.
* Convert fixed length [STRING](STRING.md) values by using a different return$ variable.
* Can be used to trim the leading space of a positive numerical value converted to a string value by STR$ .


## EXAMPLES
> Example 1: Trimming a positive string number.

```vb
value = 12345
number$ = LTRIM$(STR$(value)) 'converting number to string removes right PRINT space
PRINT "[" + number$ + "]"
```

> Example 2: Trimming leading spaces from text strings.

```vb
value = 12345
number$ = LTRIM$(STR$(value)) 'converting number to string removes right PRINT space
PRINT "[" + number$ + "]"
```

> Example 3: A TRIM$ function to trim spaces off of both ends of a string.

```vb
value = 12345
number$ = LTRIM$(STR$(value)) 'converting number to string removes right PRINT space
PRINT "[" + number$ + "]"
```


```vb
value = 12345
number$ = LTRIM$(STR$(value)) 'converting number to string removes right PRINT space
PRINT "[" + number$ + "]"
```

* Featured in our "Keyword of the Day" series
* _TRIM$ , RTRIM$ , STR$
* LEFT$ , RIGHT$
* HEX$ , MID$ (function)

```vb
value = 12345
number$ = LTRIM$(STR$(value)) 'converting number to string removes right PRINT space
PRINT "[" + number$ + "]"
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* _TRIM$ , RTRIM$ , STR$
* LEFT$ , RIGHT$
* HEX$ , MID$ (function)

