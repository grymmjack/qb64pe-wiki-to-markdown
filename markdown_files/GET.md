# GET
> The GET # statement reads data from a file or port device by bytes or record positions.

## SYNTAX
`GET # fileNumber& , [ position ][, { targetVariable | targetArray() }]`

## DESCRIPTION
* fileNumber& is the file or port number used in the [OPEN](OPEN.md) [AS](AS.md) [BINARY](BINARY.md) or [RANDOM](RANDOM.md) statement.
* The [INTEGER](INTEGER.md) or [LONG](LONG.md) byte position in a [BINARY](BINARY.md) file or the record position in a [RANDOM](RANDOM.md) file must be greater than zero .
* The position can be omitted if the [GET](GET.md) operations are consecutive based on the targetVariable [TYPE](TYPE.md) byte size.
* The targetVariable type or [FIELD](FIELD.md) variable size determines the byte size and the next position in the file.
* The first byte position in a file is 1.
* [GET](GET.md) does not require a byte or record position or targetVariable (or comma) when using a [FIELD](FIELD.md) statement.
* QB64 can [PUT](PUT.md) the entire contents of an array to a file and later [GET](GET.md) those contents to a targetArray() (include brackets).
* [GET](GET.md) may ignore the end of a file and return bad data. If the [EOF](EOF.md) function returns -1 after a [GET](GET.md) operation, it indicates that the data has ended.


## EXAMPLES
> Example 1: Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.

```vb
DO UNTIL EOF(1)
  GET #1, , value%
  IF NOT(EOF(1)) THEN PUT #2, , value%
LOOP
```

> Example 2: Placing the contents of a numerical array into a BINARY file. You may want to put the array size at the beginning too.

```vb
DO UNTIL EOF(1)
  GET #1, , value%
  IF NOT(EOF(1)) THEN PUT #2, , value%
LOOP
```


```vb
DO UNTIL EOF(1)
  GET #1, , value%
  IF NOT(EOF(1)) THEN PUT #2, , value%
LOOP
```

* [PUT](PUT.md) # , [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)
* [INPUT](INPUT.md) # , [GET](GET.md) (TCP/IP statement)
* [FIELD](FIELD.md) , [RANDOM](RANDOM.md) , [BINARY](BINARY.md)
* [LEN](LEN.md) , [LOF](LOF.md) , [EOF](EOF.md)

```vb
DO UNTIL EOF(1)
  GET #1, , value%
  IF NOT(EOF(1)) THEN PUT #2, , value%
LOOP
```



# SEE ALSO
* [PUT](PUT.md) # , [SEEK](SEEK.md) , [SEEK](SEEK.md) (function)
* [INPUT](INPUT.md) # , [GET](GET.md) (TCP/IP statement)
* [FIELD](FIELD.md) , [RANDOM](RANDOM.md) , [BINARY](BINARY.md)
* [LEN](LEN.md) , [LOF](LOF.md) , [EOF](EOF.md)

