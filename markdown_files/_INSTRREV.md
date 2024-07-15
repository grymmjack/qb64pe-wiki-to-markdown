# _INSTRREV
> The _INSTRREV function searches for a substring inside another string, but unlike INSTR it searches from right to left.

## SYNTAX
`position% = _INSTRREV ([ start% ,] baseString$ , subString$ )`

## PARAMETERS
* The optional literal or variable [INTEGER](INTEGER.md) start% indicates where in the baseString$ the search must start, counted from the left.
* The baseString$ is a literal or variable [STRING](STRING.md) value to be searched for an exact match including letter cases .
* The subString$ is a literal or variable [STRING](STRING.md) value being searched.


## DESCRIPTION
* The function returns the position% in the baseString$ where the subString$ was found, from right to left.
* position% will be 0 if the search found no matches in the base string.
* [_INSTRREV](_INSTRREV.md) returns 0 if an empty baseString$ is passed, and returns [LEN](LEN.md) ( baseString$ ) with an empty subString$ .
* The start% position is useful when making multiple searches in the same string. See the example below.
* The subString$ should be smaller or equal in length to the baseString$ , or 0 is returned.
* A start% value of 0 or less starts search from the end of the baseString$ (same as not passing a start% parameter).


## EXAMPLES
> Example 1: Separating a file name from a full path.

```vb
fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o"
file$ = MID$(fullPath$, _INSTRREV(fullPath$, "\") + 1)
PRINT file$
```

> Example 2: Searching for multiple instances of a substring inside a base string, going from the end to the start.

```vb
fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o"
file$ = MID$(fullPath$, _INSTRREV(fullPath$, "\") + 1)
PRINT file$
```


```vb
fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o"
file$ = MID$(fullPath$, _INSTRREV(fullPath$, "\") + 1)
PRINT file$
```

* Featured in our "Keyword of the Day" series
* MID$ (function) , [INSTR](INSTR.md)
* SPACE$

```vb
fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o"
file$ = MID$(fullPath$, _INSTRREV(fullPath$, "\") + 1)
PRINT file$
```



# SEE ALSO
* Featured in our "Keyword of the Day" series
* MID$ (function) , [INSTR](INSTR.md)
* SPACE$

