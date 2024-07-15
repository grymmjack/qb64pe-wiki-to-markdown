# FIELD
> The FIELD statement creates a STRING type definition for a random -access file buffer.

## SYNTAX
`FIELD [#] fileNumber& , fieldWidth1% AS variable1$ [, fieldWidthN% AS variableN$ ]`

## DESCRIPTION
* fileNumber% is a file number used in the [OPEN](OPEN.md) statement or a value from the [FREEFILE](FREEFILE.md) function.
* Combined size of the fieldWidth% parameters must not exceed the [LEN](LEN.md) = recordsize in the [RANDOM](RANDOM.md) [OPEN](OPEN.md) statement or a "[FIELD](FIELD.md) overflow" error will occur.
* Variables are limited to [STRING](STRING.md) types. Use [TYPE](TYPE.md) instead of [FIELD](FIELD.md) if you want to use numerical values.
* Once a [FIELD](FIELD.md) is defined in a statement, [GET](GET.md) can read and [PUT](PUT.md) can write data without placeholders or variables.
* [LSET](LSET.md) , [RSET](RSET.md) , [PRINT](PRINT.md) # , [PRINT](PRINT.md) # [USING](USING.md) , and [WRITE](WRITE.md) # can be used to place characters in the file buffer before a [PUT](PUT.md) .
* All field definitions for a file are removed when the file is closed or [RESET](RESET.md) and all strings are set to null ("").
* Do not re-assign a field defined variable value or use it in an [INPUT](INPUT.md) statement if you want the variable to remain a field .


## EXAMPLES
> Example: Comparing a TYPE definition with a FIELD string definition. Demo using a TYPE definition to create a file:

```vb
TYPE ClientType
  CName AS STRING * 30     '30 bytes
  Address AS STRING * 30   '30 bytes
  City   AS STRING * 15    '15 bytes
  State  AS STRING * 2     ' 2 bytes
  Zip    AS STRING * 5     ' 5 bytes
END TYPE      ' total size = 82 bytes
DIM Client AS ClientType
RecordLEN = LEN(Client)       'find the size of each TYPE record

OPEN "ADDRESS.DAT" FOR RANDOM AS #1 LEN = RecordLEN
RESTORE ClientData         'restore to start of DATA
record = 0
DO
  READ CName$, Address$, City$, State$, Zip$       'read DATA
  IF CName$ = "END" THEN EXIT DO
  record = record + 1               'increment record number
  Client.CName = CName$
  Client.Address = Address$
  Client.City = City$
  Client.State = State$
  Client.Zip = Zip$
  PUT #1, record, Client     'PUT by record number
LOOP
CLOSE #1
END

ClientData:
  DATA "Bob White","104 Birdland Rd.","Bellview","PA","15236"
  DATA "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"
  DATA "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"
  DATA "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"
  DATA "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"
  DATA "END",0,0,0,0
```

> Demo using the FIELD statement to read the file:

```vb
TYPE ClientType
  CName AS STRING * 30     '30 bytes
  Address AS STRING * 30   '30 bytes
  City   AS STRING * 15    '15 bytes
  State  AS STRING * 2     ' 2 bytes
  Zip    AS STRING * 5     ' 5 bytes
END TYPE      ' total size = 82 bytes
DIM Client AS ClientType
RecordLEN = LEN(Client)       'find the size of each TYPE record

OPEN "ADDRESS.DAT" FOR RANDOM AS #1 LEN = RecordLEN
RESTORE ClientData         'restore to start of DATA
record = 0
DO
  READ CName$, Address$, City$, State$, Zip$       'read DATA
  IF CName$ = "END" THEN EXIT DO
  record = record + 1               'increment record number
  Client.CName = CName$
  Client.Address = Address$
  Client.City = City$
  Client.State = State$
  Client.Zip = Zip$
  PUT #1, record, Client     'PUT by record number
LOOP
CLOSE #1
END

ClientData:
  DATA "Bob White","104 Birdland Rd.","Bellview","PA","15236"
  DATA "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"
  DATA "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"
  DATA "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"
  DATA "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"
  DATA "END",0,0,0,0
```


```vb
TYPE ClientType
  CName AS STRING * 30     '30 bytes
  Address AS STRING * 30   '30 bytes
  City   AS STRING * 15    '15 bytes
  State  AS STRING * 2     ' 2 bytes
  Zip    AS STRING * 5     ' 5 bytes
END TYPE      ' total size = 82 bytes
DIM Client AS ClientType
RecordLEN = LEN(Client)       'find the size of each TYPE record

OPEN "ADDRESS.DAT" FOR RANDOM AS #1 LEN = RecordLEN
RESTORE ClientData         'restore to start of DATA
record = 0
DO
  READ CName$, Address$, City$, State$, Zip$       'read DATA
  IF CName$ = "END" THEN EXIT DO
  record = record + 1               'increment record number
  Client.CName = CName$
  Client.Address = Address$
  Client.City = City$
  Client.State = State$
  Client.Zip = Zip$
  PUT #1, record, Client     'PUT by record number
LOOP
CLOSE #1
END

ClientData:
  DATA "Bob White","104 Birdland Rd.","Bellview","PA","15236"
  DATA "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"
  DATA "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"
  DATA "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"
  DATA "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"
  DATA "END",0,0,0,0
```

* [OPEN](OPEN.md) , [TYPE](TYPE.md)
* [GET](GET.md) , [PUT](PUT.md)
* [LSET](LSET.md) , [RSET](RSET.md)

```vb
TYPE ClientType
  CName AS STRING * 30     '30 bytes
  Address AS STRING * 30   '30 bytes
  City   AS STRING * 15    '15 bytes
  State  AS STRING * 2     ' 2 bytes
  Zip    AS STRING * 5     ' 5 bytes
END TYPE      ' total size = 82 bytes
DIM Client AS ClientType
RecordLEN = LEN(Client)       'find the size of each TYPE record

OPEN "ADDRESS.DAT" FOR RANDOM AS #1 LEN = RecordLEN
RESTORE ClientData         'restore to start of DATA
record = 0
DO
  READ CName$, Address$, City$, State$, Zip$       'read DATA
  IF CName$ = "END" THEN EXIT DO
  record = record + 1               'increment record number
  Client.CName = CName$
  Client.Address = Address$
  Client.City = City$
  Client.State = State$
  Client.Zip = Zip$
  PUT #1, record, Client     'PUT by record number
LOOP
CLOSE #1
END

ClientData:
  DATA "Bob White","104 Birdland Rd.","Bellview","PA","15236"
  DATA "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"
  DATA "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"
  DATA "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"
  DATA "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"
  DATA "END",0,0,0,0
```



# SEE ALSO
* [OPEN](OPEN.md) , [TYPE](TYPE.md)
* [GET](GET.md) , [PUT](PUT.md)
* [LSET](LSET.md) , [RSET](RSET.md)

