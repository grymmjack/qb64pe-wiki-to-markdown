## OR (boolean)
---

### The OR conditional operator evaluates an expression to true (-1) if any of the arguments is also true.

#### SYNTAX

`IF expression1 OR expression2 THEN {code}`

#### DESCRIPTION
* [OR](./OR.md) adds an alternative to another conditional evaluation. If either element in the evaluation is true then the evaluation is true.
* Parenthesis may be used to clarify the order of comparisons in an evaluation.
* Not to be confused with the [AND](./AND.md) and [OR](./OR.md) numerical operations.


#### EXAMPLES
##### Example:
```vb
a% = 100
b% = 50

IF (a% > b% AND a% < 100) OR b% = 50 THEN PRINT "True"
```
  
```vb
True
```
  


#### SEE ALSO
* [AND](./AND.md) , [OR](./OR.md)
* [AND](./AND.md) (boolean) , [XOR](./XOR.md) (boolean)
* [IF](./IF.md)...[THEN](./THEN.md)
