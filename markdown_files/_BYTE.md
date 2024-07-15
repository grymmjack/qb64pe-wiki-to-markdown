# _BYTE
> A _BYTE variable can hold signed variable values from -128 to 127 (one byte or 8 _BITs ). Unsigned from 0 to 255.

## SYNTAX
`DIM byte AS [[[_UNSIGNED]]] _BYTE`

## DESCRIPTION
* Signed [_BYTE](_BYTE.md) values can range from -128 to 127.
* [_UNSIGNED](_UNSIGNED.md) _BYTEs can hold values from 0 to 255. [_UNSIGNED](_UNSIGNED.md) expands the range of positive values.
* Can be defined in a QB64 [_DEFINE](_DEFINE.md) statement using a starting letter range of variable names.
* Also can be used in a subroutine parameter [AS](AS.md) [_BYTE](_BYTE.md) variable definitions.
* Define a byte using the suffix %% after the variable name: variable%% = -54
* Define an unsigned byte by adding the suffix ~%% after the variable name: variable~%% = 54
* When a variable has not been assigned or has no type suffix, the value defaults to [SINGLE](SINGLE.md) .


## EXAMPLES

```vb
Offset or Position:    0    1   2   3   4   5   6   7      Example: 11110000
                             ----------------------------------             --------
   Big-Endian Bit On Value:   128  64  32  16   8   4   2   1                 240
Little-Endian Bit On Value:    1    2   4   8  16  32  64  128                 15
```

* [_BIT](_BIT.md) , &B
* [_DEFINE](_DEFINE.md) , [DIM](DIM.md)
* [_UNSIGNED](_UNSIGNED.md)
* [_SHL](_SHL.md) , [_SHR](_SHR.md)
* Mathematical Operations
* Screen Memory
* Variable Types
* Converting Bytes to Bits

```vb
Offset or Position:    0    1   2   3   4   5   6   7      Example: 11110000
                             ----------------------------------             --------
   Big-Endian Bit On Value:   128  64  32  16   8   4   2   1                 240
Little-Endian Bit On Value:    1    2   4   8  16  32  64  128                 15
```



# SEE ALSO
* [_BIT](_BIT.md) , &B
* [_DEFINE](_DEFINE.md) , [DIM](DIM.md)
* [_UNSIGNED](_UNSIGNED.md)
* [_SHL](_SHL.md) , [_SHR](_SHR.md)
* Mathematical Operations
* Screen Memory
* Variable Types
* Converting Bytes to Bits

