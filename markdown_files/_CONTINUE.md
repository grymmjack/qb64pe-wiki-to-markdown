# _CONTINUE
> The _CONTINUE statement is used in a DO...LOOP , WHILE...WEND or FOR...NEXT block to skip the remaining lines of code in a block (without exiting it) and start the next iteration. It works as a shortcut to a GOTO , but without the need for a line label .

## SYNTAX
`_CONTINUE`

## EXAMPLES
> Example:

```vb
FOR i = 1 TO 10
   IF i = 5 THEN _CONTINUE
   PRINT i;
NEXT
```


```vb
FOR i = 1 TO 10
   IF i = 5 THEN _CONTINUE
   PRINT i;
NEXT
```

* [DO](DO.md)...[LOOP](LOOP.md)
* [WHILE](WHILE.md)...[WEND](WEND.md)
* [FOR](FOR.md)...[NEXT](NEXT.md)
* [GOTO](GOTO.md)

```vb
FOR i = 1 TO 10
   IF i = 5 THEN _CONTINUE
   PRINT i;
NEXT
```



# SEE ALSO
* [DO](DO.md)...[LOOP](LOOP.md)
* [WHILE](WHILE.md)...[WEND](WEND.md)
* [FOR](FOR.md)...[NEXT](NEXT.md)
* [GOTO](GOTO.md)

