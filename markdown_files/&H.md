## &H
---

### The &H prefix denotes that an integer value is expressed in a Hexadecimal base 16 format. Every 2 digits represent a _BYTE .

#### SYNTAX

`a& = &H C0DEBA5E`

#### DESCRIPTION
* The base 16 numbering system uses hexadecimal digit values of 0 to F, where A = 10, B = 11, C = 12, D = 13, E = 14 and F = 15.
* Leading zero values can be omitted just like in decimal values as they add nothing to the return value.
* Decimal values returned can be any signed [INTEGER](./INTEGER.md) , [LONG](./LONG.md) integer, or [_INTEGER64](./_INTEGER64.md) value so use those type of variables when converting directly as shown above in the Syntax. The program "overflow" error limits are listed as:


#### EXAMPLES
```vb
c&& = -1: d& = -1: e% = -1: f%% = -1
hx$ = HEX$(f%%)
PRINT "Max hex _BYTE = "; hx$; " with"; LEN(hx$); "digits ="; VAL("&H" + hx$)
hx$ = HEX$(e%)
PRINT "Max hex INTEGER = "; hx$; " with"; LEN(hx$); "digits ="; VAL("&H" + hx$)
hx$ = HEX$(d&)
PRINT "Max hex LONG = "; hx$; " with"; LEN(hx$); "digits ="; VAL("&H" + hx$)
hx$ = HEX$(c&&)
PRINT "Max hex _INTEGER64 = "; hx$; " with"; LEN(hx$); "digits ="; VAL("&H" + hx$)
hx$ = HEX$(9223372036854775807)
PRINT "Max _INTEGER64 value = "; hx$; " with"; LEN(hx$); "digits"
hx$ = HEX$(-9223372036854775808)
PRINT "Min _INTEGER64 value = "; hx$; " with"; LEN(hx$); "digits"
```
  
```vb
Max hex _BYTE = FF with 2 digits = 255
Max hex INTEGER = FFFF with 4 digits = 65535
Max hex LONG = FFFFFFFF with 8 digits = 4294967295
Max hex _INTEGER64 = FFFFFFFFFFFFFFFF with 16 digits =-1
Max _INTEGER64 value = 7FFFFFFFFFFFFFFF with 16 digits
Min _INTEGER64 value = 8000000000000000 with 16 digits
```
  
```vb
FUNCTION BinStr$ (n&)
 h$ = HEX$(n&)                     'get hexadecimal string value
 FOR i = 1 TO LEN(h$)              'scan the HEX$ digits
   SELECT CASE MID$(h$, i, 1)      'read each HEX$ digit
       CASE "0": b$ = b$ + "0000"
       CASE "1": b$ = b$ + "0001"
       CASE "2": b$ = b$ + "0010"
       CASE "3": b$ = b$ + "0011"
       CASE "4": b$ = b$ + "0100"
       CASE "5": b$ = b$ + "0101"
       CASE "6": b$ = b$ + "0110"
       CASE "7": b$ = b$ + "0111"
       CASE "8": b$ = b$ + "1000"
       CASE "9": b$ = b$ + "1001"
       CASE "A": b$ = b$ + "1010"
       CASE "B": b$ = b$ + "1011"
       CASE "C": b$ = b$ + "1100"
       CASE "D": b$ = b$ + "1101"
       CASE "E": b$ = b$ + "1110"
       CASE "F": b$ = b$ + "1111"
   END SELECT
 NEXT i
 b$ = RIGHT$(b$, LEN(b$) - INSTR(b$, "1") + 1)   'eliminate leading zeroes
 IF VAL(b$) THEN BinStr$ = b$ ELSE BinStr$ = "0"       'return zero if n& = 0
END FUNCTION
```
  


#### SEE ALSO
* _BIN$ , HEX$ , OCT$ , STR$
* &B (binary), &O (octal), [VAL](./VAL.md)
* Base Comparisons
* HEX$ 32 Bit Values
