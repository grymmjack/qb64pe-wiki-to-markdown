## LPRINT USING
---

### The LPRINT USING statement sends formatted data to LPT1, the parallel port printer.

#### SYNTAX

`LPRINT [ text$ {;|,}] USING template$ ; variable [; ...][{;|,}]`

#### PARAMETERS
* Literal or variable [STRING](./STRING.md) text$ can be placed between [LPRINT](./LPRINT.md) and [USING](./USING.md) or it can be included in the template$ .
* A semicolon or comma may follow the text$ to stop or tab the print cursor before the template$ [LPRINT](./LPRINT.md) .
* The literal or variable [STRING](./STRING.md) template$ should use the template symbols to display each variable type in the list following it.
* The list of data variables used in the template$ are separated by semicolons after the template string value.
* A semicolon or comma may follow the variable list to stop or tab the print cursor for pending prints.


#### DESCRIPTION
* The variable list should be listed in the order that they are used in the template from left to right.
* If the template string is omitted or symbols don't match the variable(s) an "Illegal Function Call" [ERROR](./ERROR.md) will occur.
* No more than 25 # digit places are allowed in a template number or an error will occur.
* Can convert numerical exponential or scientific notation values to normal decimal point values using less digits.
* NOTE: If the numerical value exceeds the template's digit range a % symbol will appear in the leftmost digit area.


#### SEE ALSO
* [PRINT](./PRINT.md) [USING](./USING.md)
* [LPRINT](./LPRINT.md)
* [PRINT](./PRINT.md)
