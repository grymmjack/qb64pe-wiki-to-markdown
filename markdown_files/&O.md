## &O
---

### The &O prefix denotes that an integer value is expressed in a Octal base 8 format.

#### SYNTAX

`a& = &O 377`

#### DESCRIPTION
* The base 8 numbering system uses octal digit values of 0 to 7 only.
* Leading zero values can be omitted just like in decimal values as they add nothing to the return value.
* Decimal values returned can be any signed [INTEGER](./INTEGER.md) , [LONG](./LONG.md) integer, or [_INTEGER64](./_INTEGER64.md) value so use those type of variables when converting directly as shown above in the Syntax. The program "overflow" error limits are listed as:


#### EXAMPLES
```vb
c&& = -1: d& = -1: e% = -1: f%% = -1
oc$ = OCT$(f%%)
PRINT "Max octal _BYTE = "; oc$; " with"; LEN(oc$); "digits ="; VAL("&O" + oc$)
oc$ = OCT$(e%)
PRINT "Max octal INTEGER = "; oc$; " with"; LEN(oc$); "digits ="; VAL("&O" + oc$)
oc$ = OCT$(d&)
PRINT "Max octal LONG = "; oc$; " with"; LEN(oc$); "digits ="; VAL("&O" + oc$)
oc$ = OCT$(c&&)
PRINT "Max octal _INTEGER64 = "; oc$; " with"; LEN(oc$); "digits ="; VAL("&O" + oc$)
oc$ = OCT$(9223372036854775807)
PRINT "Max _INTEGER64 value = "; oc$; " with"; LEN(oc$); "digits"
oc$ = OCT$(-9223372036854775808)
PRINT "Min _INTEGER64 value = "; oc$; " with"; LEN(oc$); "digits"
```
  
```vb
Max octal _BYTE = 377 with 3 digits = 255
Max octal INTEGER = 177777 with 6 digits = 65535
Max octal LONG = 37777777777 with 11 digits = 4294967295
Max octal _INTEGER64 = 1777777777777777777777 with 22 digits =-1
Max _INTEGER64 value = 777777777777777777777 with 21 digits
Min _INTEGER64 value = 1000000000000000000000 with 22 digits
```
  


#### SEE ALSO
* _BIN$ , HEX$ , OCT$ , STR$
* &B (binary), &H (hexadecimal), [VAL](./VAL.md)
* Base Comparisons
