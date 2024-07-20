## &B
---

### The &B prefix denotes that an integer value is expressed in a Binary base 2 format. Every 8 digits represent a _BYTE .

#### SYNTAX

`a& = &B 10010110`

#### DESCRIPTION
* The base 2 numbering system uses binary digit values of 0 and 1 only.
* Leading zero values can be omitted just like in decimal values as they add nothing to the return value.
* Decimal values returned can be any signed [INTEGER](./INTEGER.md) , [LONG](./LONG.md) integer, or [_INTEGER64](./_INTEGER64.md) value so use those type of variables when converting directly as shown above in the Syntax. The program "overflow" error limits are listed as:


#### EXAMPLES
```vb
c&& = -1: d& = -1: e% = -1: f%% = -1
bi$ = _BIN$(f%%)
PRINT "Max binary _BYTE = "; bi$; " with"; LEN(bi$); "digits ="; VAL("&B" + bi$)
bi$ = _BIN$(e%)
PRINT "Max binary INTEGER = "; bi$; " with"; LEN(bi$); "digits ="; VAL("&B" + bi$)
bi$ = _BIN$(d&)
PRINT "Max binary LONG = "; bi$; " with"; LEN(bi$); "digits ="; VAL("&B" + bi$)
bi$ = _BIN$(c&&)
PRINT "Max binary _INTEGER64 = "; bi$; " with"; LEN(bi$); "digits ="; VAL("&B" + bi$)
bi$ = _BIN$(9223372036854775807)
PRINT "Max _INTEGER64 value = "; bi$; " with"; LEN(bi$); "digits"
bi$ = _BIN$(-9223372036854775808)
PRINT "Min _INTEGER64 value = "; bi$; " with"; LEN(bi$); "digits"
```
  
```vb
Max binary _BYTE = 11111111 with 8 digits = 255
Max binary INTEGER = 1111111111111111 with 16 digits = 65535
Max binary LONG = 11111111111111111111111111111111 with 32 digits = 4294967295
Max binary _INTEGER64 = 1111111111111111111111111111111111111111111111111111111111111111 with 64 digits =-1
Max _INTEGER64 value = 111111111111111111111111111111111111111111111111111111111111111 with 63 digits
Min _INTEGER64 value = 1000000000000000000000000000000000000000000000000000000000000000 with 64 digits
```
  


#### SEE ALSO
* _BIN$ , HEX$ , OCT$ , STR$
* &H (hexadecimal), &O (octal), [VAL](./VAL.md)
* Base Comparisons
