# SPACE$
> The SPACE$ function returns a STRING consisting of a number of space characters.

## SYNTAX
`result$ = SPACE$( count& )`

## PARAMETERS
* count& is the number of space characters to repeat. Cannot use negative values!


## DESCRIPTION
* Semicolons can be used to combine spaces with text [STRING](STRING.md) or numerical values.
* Concatenation using + can be used to combine [STRING](STRING.md) text values only.
* Spaces are often used to erase previous text PRINTs from the screen.
* The function result can also be used to [GET](GET.md) and [PUT](PUT.md) a number of bytes as zero characters: bytes$ = SPACE$(numbytes)
* Spaces can also be made using [SPC](SPC.md) , CHR$ (32) or [STRING](STRING.md)$ (n%, 32).


## EXAMPLES
> Example 1: How to space text in a PRINT statement using SPACE$ with string concatenation .

```vb
FOR count% = 0 TO 3
   PRINT "abc" + SPACE$( count% ) + "def"
NEXT count%
```

> Example 2: In SCREEN 0 SPACE$ can be used to change the background color to make an American flag.

```vb
FOR count% = 0 TO 3
   PRINT "abc" + SPACE$( count% ) + "def"
NEXT count%
```


```vb
FOR count% = 0 TO 3
   PRINT "abc" + SPACE$( count% ) + "def"
NEXT count%
```

* [PRINT](PRINT.md) , [PRINT](PRINT.md) [USING](USING.md)
* [STRING](STRING.md)$ , [CLS](CLS.md)
* [SPC](SPC.md) , [TAB](TAB.md)

```vb
FOR count% = 0 TO 3
   PRINT "abc" + SPACE$( count% ) + "def"
NEXT count%
```



# SEE ALSO
* [PRINT](PRINT.md) , [PRINT](PRINT.md) [USING](USING.md)
* [STRING](STRING.md)$ , [CLS](CLS.md)
* [SPC](SPC.md) , [TAB](TAB.md)

