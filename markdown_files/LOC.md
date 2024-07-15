# LOC
> The LOC function returns the status of a serial (COM) port received buffer or the last read/written byte or record position in an open file.

## SYNTAX
`bytes% = LOC ( fileOrPortNumber% )`

## PARAMETERS
* fileOrPortNumber% is the number used in the port or file [OPEN](OPEN.md) [AS](AS.md) statement.
* Returns 0 if the buffer is empty. Any value above 0 indicates the [COM](COM.md) port has received data.
* Use it in conjunction with [INPUT](INPUT.md)$ to get the data bytes received.
* Can also be used to get the last read/written byte or record position in a file. See also [SEEK](SEEK.md) .


## EXAMPLES

```vb
OPEN "COM1: 9600,N,8,1,OP0" FOR RANDOM AS #1 LEN = 2048 ' random mode = input and output
 DO: t$ = INKEY$ ' get any transmit keypresses from user
   IF LEN(t$) THEN PRINT #1, t$ ' send keyboard byte to transmit buffer
   bytes% = LOC(1) ' bytes in buffer
   IF bytes% THEN ' check receive buffer for data"
     r$ = INPUT$(bytes%, 1)          ' get bytes in the receive buffer
     PRINT r$; ' print byte strings consecutively to screen"
   END IF
 LOOP UNTIL t$ = CHR$(27) 'escape key exit
CLOSE #
```

* [PRINT](PRINT.md) , [OPEN](OPEN.md) [COM](COM.md) , [PRINT](PRINT.md) (file statement)
* [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)

```vb
OPEN "COM1: 9600,N,8,1,OP0" FOR RANDOM AS #1 LEN = 2048 ' random mode = input and output
 DO: t$ = INKEY$ ' get any transmit keypresses from user
   IF LEN(t$) THEN PRINT #1, t$ ' send keyboard byte to transmit buffer
   bytes% = LOC(1) ' bytes in buffer
   IF bytes% THEN ' check receive buffer for data"
     r$ = INPUT$(bytes%, 1)          ' get bytes in the receive buffer
     PRINT r$; ' print byte strings consecutively to screen"
   END IF
 LOOP UNTIL t$ = CHR$(27) 'escape key exit
CLOSE #
```



# SEE ALSO
* [PRINT](PRINT.md) , [OPEN](OPEN.md) [COM](COM.md) , [PRINT](PRINT.md) (file statement)
* [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)

