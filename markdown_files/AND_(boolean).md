## AND (boolean)
---

### The AND conditonal operator is used to include another evaluation in an IF...THEN or Boolean statement.

#### SYNTAX

`IF condition AND condition2`

#### DESCRIPTION
* If condition [AND](./AND.md) condition2 are true then the evaluation returns true (-1).
* condition and condition2 can also contain their own [AND](./AND.md) evaluations.
* Both the [IF](./IF.md) evaluation and the [AND](./AND.md) evaluation must be true for the statement to be true.
* Statements can use parenthesis to clarify an evaluation.
* [AND](./AND.md) (boolean) and [OR](./OR.md) (boolean) cannot be used to combine command line operations.
* Not to be confused with the [AND](./AND.md) and [OR](./OR.md) numerical operations.


#### EXAMPLES
##### Example: Using AND in an IF statement.
```vb
a% = 100
b% = 50

IF a% > b% AND a% < 200 THEN PRINT "True"
```
  
```vb
True
```
  
##### Explanation: Both condition evaluations must be true for the code to be executed.
##### Example: Using a AND a more complex way.
```vb
a% = 100
b% = 50
c% = 25
d% = 50
e% = 100

IF (a% > b% AND b% > c%) AND (c% < d% AND d% < e%) THEN
PRINT "True"
ELSE
PRINT "False"
END IF
```
  
```vb
True
```
  
##### Explanation: The evaluations in the paranteses are evaluated first then the evaluation of the paranteses takes place, since all evaluations return True the IF...THEN evaluation returns True. If any of the evaluations returned False then the IF...THEN evaluation would also return False.


#### SEE ALSO
* [AND](./AND.md) , [OR](./OR.md) (logical operators)
* [OR](./OR.md) (boolean) , [XOR](./XOR.md) (boolean)
* [IF](./IF.md)...[THEN](./THEN.md)
