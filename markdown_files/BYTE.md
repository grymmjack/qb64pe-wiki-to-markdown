## _BYTE
---

### A _BYTE variable can hold signed variable values from -128 to 127 (one byte or 8 _BITs ). Unsigned from 0 to 255.

#### SYNTAX

`DIM byte AS [[[_UNSIGNED]]] _BYTE`

#### DESCRIPTION
* Signed [_BYTE](./_BYTE.md) values can range from -128 to 127.
* [_UNSIGNED](./_UNSIGNED.md) _BYTEs can hold values from 0 to 255. [_UNSIGNED](./_UNSIGNED.md) expands the range of positive values.
* Can be defined in a QB64 [_DEFINE](./_DEFINE.md) statement using a starting letter range of variable names.
* Also can be used in a subroutine parameter [AS](./AS.md) [_BYTE](./_BYTE.md) variable definitions.
* Define a byte using the suffix %% after the variable name: variable%% = -54
* Define an unsigned byte by adding the suffix ~%% after the variable name: variable~%% = 54
* When a variable has not been assigned or has no type suffix, the value defaults to [SINGLE](./SINGLE.md) .


#### EXAMPLES
```vb
DIM unsig AS _UNSIGNED _BYTE
DIM sig AS _BYTE

CLS
unsig = 1
sig = 1
PRINT "&B00000001 = unsigned & signed are both" + STR$(unsig AND sig)

unsig = 127
sig = 127
PRINT "&B01111111 = unsigned & signed are both" + STR$(unsig AND sig)

unsig = 255
sig = 255
PRINT "&B11111111 = unsigned is" + STR$(unsig) + " but signed is " + STR$(sig)

unsig = 254
sig = 254
PRINT "&B11111110 = unsigned is" + STR$(unsig) + " but signed is " + STR$(sig)

unsig = 253
sig = 253
PRINT "&B11111101 = unsigned is" + STR$(unsig) + " but signed is " + STR$(sig)

PRINT
PRINT "The signed value needs the MSB bit for the sign."
PRINT "The most significant bit is furthest to the left."
```
  
```vb
&B00000001 = unsigned & signed are both 1
&B01111111 = unsigned & signed are both 127
&B11111111 = unsigned is 255 but signed is -1
&B11111110 = unsigned is 254 but signed is -2
&B11111101 = unsigned is 253 but signed is -3

The signed value needs the MSB bit for the sign.
The most significant bit is furthest to the left.
```
  


#### SEE ALSO
* [_BIT](./_BIT.md) , &B
* [_DEFINE](./_DEFINE.md) , [DIM](./DIM.md)
* [_UNSIGNED](./_UNSIGNED.md)
* [_SHL](./_SHL.md) , [_SHR](./_SHR.md)
* Mathematical Operations
* Screen Memory
* Variable Types
* Converting Bytes to Bits
