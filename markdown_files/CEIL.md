## _CEIL
---

### The _CEIL function rounds a numeric value up to the next whole number or INTEGER value.

#### SYNTAX

`result = _CEIL ( expression )`

#### EXAMPLES
##### Example: Displaying the rounding behavior of INT , CINT and FIX vs _CEIL .
```vb
PRINT INT(2.5), CINT(2.5), FIX(2.5), _CEIL(2.5)
PRINT INT(-2.5), CINT(-2.5), FIX(-2.5), _CEIL(-2.5)
```
  
```vb
2        2         2         3
-3       -2        -2        -2
```
  


#### SEE ALSO
* [INT](./INT.md) , [FIX](./FIX.md)
* [CINT](./CINT.md) , [CLNG](./CLNG.md) ,
* [CSNG](./CSNG.md) , [CDBL](./CDBL.md)
* [_ROUND](./_ROUND.md)
