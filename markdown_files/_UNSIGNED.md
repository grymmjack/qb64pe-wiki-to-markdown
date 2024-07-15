# _UNSIGNED
> _UNSIGNED defines a numerical value as being only positive.

## SYNTAX
`DIM variable AS [[[_UNSIGNED]]] datatype`

## DESCRIPTION
* Datatype can be any of the following: [INTEGER](INTEGER.md) , [LONG](LONG.md) , [_BIT](_BIT.md) , [_BYTE](_BYTE.md) , [_INTEGER64](_INTEGER64.md) , [_OFFSET](_OFFSET.md)
* [SINGLE](SINGLE.md) , [DOUBLE](DOUBLE.md) and [_FLOAT](_FLOAT.md) variable types cannot be [_UNSIGNED](_UNSIGNED.md).
* [_UNSIGNED](_UNSIGNED.md) can be used in a [_DEFINE](_DEFINE.md) statement to set undefined variable name first letters as all positive-only values.
* Can also be used in [DIM](DIM.md) statements or subprocedure parameter definitions following [AS](AS.md) .
* [_UNSIGNED](_UNSIGNED.md) allows larger positive numerical variable value limits than signed ones.
* The unsigned variable type suffix used is the tilde (~) , right before the number's own type suffix: variableName~&


## EXAMPLES
> Example 1: In QB64 , when a signed INTEGER value exceeds 32767, the value may become a negative value:

```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```

> Example 2: In QB64 , _UNSIGNED INTEGER values greater than 65535 cycle over again from zero:

```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```

> Example 3: Demonstrating how _UNSIGNED variables expand the INTEGER range.

```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```

> Explanation: The maximum value can only be 65535 (32767 + 32768) so the FOR loop repeats itself. Remove the _UNSIGNED parts and run it again.

```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```


```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```

* [DECLARE](DECLARE.md), [SUB](SUB.md) , [FUNCTION](FUNCTION.md)
* [DIM](DIM.md) , [_DEFINE](_DEFINE.md)
* [DEFSTR](DEFSTR.md) , [DEFLNG](DEFLNG.md) , [DEFINT](DEFINT.md) , [DEFSNG](DEFSNG.md) , [DEFDBL](DEFDBL.md)
* [INTEGER](INTEGER.md) , [LONG](LONG.md) , [_INTEGER64](_INTEGER64.md)
* [ABS](ABS.md) , [SGN](SGN.md)
* Variable Types

```vb
00000001 - unsigned & signed are both 1
                       01111111 - unsigned & signed are both 127
                       11111111 - unsigned is 255 but signed is -1
                       11111110 - unsigned is 254 but signed is -2
                       11111101 - unsigned is 253 but signed is -3
```



# SEE ALSO
* [DECLARE](DECLARE.md), [SUB](SUB.md) , [FUNCTION](FUNCTION.md)
* [DIM](DIM.md) , [_DEFINE](_DEFINE.md)
* [DEFSTR](DEFSTR.md) , [DEFLNG](DEFLNG.md) , [DEFINT](DEFINT.md) , [DEFSNG](DEFSNG.md) , [DEFDBL](DEFDBL.md)
* [INTEGER](INTEGER.md) , [LONG](LONG.md) , [_INTEGER64](_INTEGER64.md)
* [ABS](ABS.md) , [SGN](SGN.md)
* Variable Types

