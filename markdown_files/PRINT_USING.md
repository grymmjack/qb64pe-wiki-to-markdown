## PRINT USING
---

### The PRINT USING statement is used to PRINT formatted data to the Screen using a STRING template.

#### SYNTAX

`PRINT [ text$ {;|,}] USING template$ ; variable [; ...][{;|,}]`

#### PARAMETERS
* Literal or variable [STRING](./STRING.md) text$ can be placed between [PRINT](./PRINT.md) and [USING](./USING.md) or it can be included in the template .
* A semicolon or comma may follow the text to stop or tab the print cursor before the template [PRINT](./PRINT.md) .
* The literal or variable [STRING](./STRING.md) template should use the template symbols to display each variable type in the list following it.
* The list of data variables used in the template are separated by semicolons after the template string value.
* In QB64 ONE semicolon or comma may follow the variable list to stop the print cursor for pending prints. QB only allowed a semicolon.


#### SEE ALSO
* [PRINT](./PRINT.md) , [PRINT](./PRINT.md) #, [USING](./USING.md)
* [LPRINT](./LPRINT.md) , [LPRINT](./LPRINT.md) [USING](./USING.md)
