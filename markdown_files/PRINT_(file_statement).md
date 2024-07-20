## PRINT (file statement)
---

### The PRINT # statement prints numeric or string expressions to a sequential file, IO port or device.

#### SYNTAX

`PRINT # fileNumber& , [ [ expression ] [{;|,] ... ]`

#### PARAMETERS
* fileNumber& is the file number of a file or device opened for writing. See [OPEN](./OPEN.md) .
* expression is a numeric or string expression to be written to the file. Quotes will be removed from strings.
* The print statement can be followed by a semicolon to stop the print cursor or a comma to tab the next print.


#### SEE ALSO
* [SPC](./SPC.md) , SPACE$ , [TAB](./TAB.md)
* [PRINT](./PRINT.md) #, [USING](./USING.md)
* [PRINT](./PRINT.md)
* [WRITE](./WRITE.md) # , [INPUT](./INPUT.md) #
* [LINE](./LINE.md) [INPUT](./INPUT.md) #
* [OPEN](./OPEN.md) , [LPRINT](./LPRINT.md) , [WRITE](./WRITE.md)
