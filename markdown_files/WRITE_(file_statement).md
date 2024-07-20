## WRITE (file statement)
---

### The WRITE # file statement writes a list of comma separated variable values to a sequential file or port.

#### SYNTAX

`WRITE # filenumber& [, expressionList ]`

#### DESCRIPTION
* filenumber& is the number of the file or device OPENed in the [OUTPUT](./OUTPUT.md) or [APPEND](./APPEND.md) modes. See: [FREEFILE](./FREEFILE.md) .
* expressionList is a comma-separated list of values to be written to the file or device.
* [WRITE](./WRITE.md) can place any number and types of variable values needed in a file record separated by commas.
* String values will have quotation marks although quotes are not required to read strings in CSV files with [INPUT](./INPUT.md) #.
* Data files using [WRITE](./WRITE.md) normally will have the same number of values listed on each file line.
* Data containing commas must be in quotation marks. Number commas are illegal!
* [WRITE](./WRITE.md) created files are normally read with [INPUT](./INPUT.md) #.
* CSV files created can be read by Excel using a .CSV file name extension. Strings may or may not include quotation marks.
* Semicolons cannot be used in or following the [WRITE](./WRITE.md) statement!


#### SEE ALSO
* [PRINT](./PRINT.md) #
* [INPUT](./INPUT.md) #
* [LINE](./LINE.md) [INPUT](./INPUT.md) #
* SQL Client
