# _READBIT
> The _READBIT function is used to check the state of a specified bit of a integer value.

## SYNTAX
`result = _READBIT ( numericalVariable , numericalValue )`

## PARAMETERS
* numericalVariable is the variable to read the state of a bit of and can be of the following types: [_BYTE](_BYTE.md) , [INTEGER](INTEGER.md) , [LONG](LONG.md) , or [_INTEGER64](_INTEGER64.md) .
* Integer values can be signed or [_UNSIGNED](_UNSIGNED.md) .
* numericalValue the number of the bit to be read.


## DESCRIPTION
* Used to check the current state of a bit in an integer value.
* Returns -1 if the bit is set(1), otherwise returns 0 if the bit is not set(0)
* Bits start at 0 (so a [_BYTE](_BYTE.md) has bits 0 to 7, [INTEGER](INTEGER.md) 0 to 15, and so on)


## EXAMPLES
> Example 1:

```vb
A~%% = _SETBIT(A~%%,4)
PRINT "Bit 4 is currently ";
IF _READBIT(A~%%,4) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
PRINT "And bit 2 is currently ";
IF _READBIT(A~%%,2) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
```

> Example 2:

```vb
A~%% = _SETBIT(A~%%,4)
PRINT "Bit 4 is currently ";
IF _READBIT(A~%%,4) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
PRINT "And bit 2 is currently ";
IF _READBIT(A~%%,2) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
```


```vb
A~%% = _SETBIT(A~%%,4)
PRINT "Bit 4 is currently ";
IF _READBIT(A~%%,4) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
PRINT "And bit 2 is currently ";
IF _READBIT(A~%%,2) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
```

* [_SHL](_SHL.md) , [_SHR](_SHR.md) , [INTEGER](INTEGER.md) , [LONG](LONG.md)
* [_SETBIT](_SETBIT.md) , [_BYTE](_BYTE.md) , [_INTEGER64](_INTEGER64.md)
* [_RESETBIT](_RESETBIT.md) , [_TOGGLEBIT](_TOGGLEBIT.md)

```vb
A~%% = _SETBIT(A~%%,4)
PRINT "Bit 4 is currently ";
IF _READBIT(A~%%,4) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
PRINT "And bit 2 is currently ";
IF _READBIT(A~%%,2) = -1 THEN PRINT "ON" ELSE PRINT "OFF"
```



# SEE ALSO
* [_SHL](_SHL.md) , [_SHR](_SHR.md) , [INTEGER](INTEGER.md) , [LONG](LONG.md)
* [_SETBIT](_SETBIT.md) , [_BYTE](_BYTE.md) , [_INTEGER64](_INTEGER64.md)
* [_RESETBIT](_RESETBIT.md) , [_TOGGLEBIT](_TOGGLEBIT.md)

