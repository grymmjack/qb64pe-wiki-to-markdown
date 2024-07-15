# INP
> INP returns a value from a computer register or port values at a specified physical address.

## SYNTAX
`i = INP ( address )`

## EXAMPLES
> Example 1: Reading the current RGB color settings used in a bitmap to an array.

```vb
SCREEN 12
DIM Colors%(47)
OUT &H3C7, 0 ' set color port for INP reads at attribute 0 to start
FOR i = 0 TO 47
Colors%(i) = INP(&H3C9) ' moves to next color attribute every 3 loops
NEXT
```

> Example 2: Reading the keyboard Scan Codes as an alternative to INKEY$

```vb
SCREEN 12
DIM Colors%(47)
OUT &H3C7, 0 ' set color port for INP reads at attribute 0 to start
FOR i = 0 TO 47
Colors%(i) = INP(&H3C9) ' moves to next color attribute every 3 loops
NEXT
```

> Example 3: A simple ping pong game using an array function to read multiple keys for two players.

```vb
SCREEN 12
DIM Colors%(47)
OUT &H3C7, 0 ' set color port for INP reads at attribute 0 to start
FOR i = 0 TO 47
Colors%(i) = INP(&H3C9) ' moves to next color attribute every 3 loops
NEXT
```


```vb
SCREEN 12
DIM Colors%(47)
OUT &H3C7, 0 ' set color port for INP reads at attribute 0 to start
FOR i = 0 TO 47
Colors%(i) = INP(&H3C9) ' moves to next color attribute every 3 loops
NEXT
```

* [OUT](OUT.md) (write to register) , [PEEK](PEEK.md) (read memory)
* INKEY$ , [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md)
* Bitmaps , Scancodes (keyboard)
* Port Access Libraries ([COM](COM.md) or LPT registers)

```vb
SCREEN 12
DIM Colors%(47)
OUT &H3C7, 0 ' set color port for INP reads at attribute 0 to start
FOR i = 0 TO 47
Colors%(i) = INP(&H3C9) ' moves to next color attribute every 3 loops
NEXT
```



# SEE ALSO
* [OUT](OUT.md) (write to register) , [PEEK](PEEK.md) (read memory)
* INKEY$ , [_KEYHIT](_KEYHIT.md) , [_KEYDOWN](_KEYDOWN.md)
* Bitmaps , Scancodes (keyboard)
* Port Access Libraries ([COM](COM.md) or LPT registers)

