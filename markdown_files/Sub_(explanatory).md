## Sub (explanatory)
---

### SUBs , short for subroutines, are like statements but are user-defined. You define a SUB by using the SUB statement. When a subroutine is called, then it will execute the code within the SUB until it reaches END SUB or EXIT SUB .

#### EXAMPLES
```vb
printsometext
CALL printmoretext


SUB printsometext
PRINT "This is within the printsometext sub."
EXIT SUB
PRINT "This is never shown as it encounters EXIT SUB first."
END SUB

SUB printmoretext
PRINT "This is within the printmoretext sub."
END SUB
```
  
```vb
demo hal, bal 'the variables hal and bal are used as arguments when calling the sub.

PRINT hal, bal 'the variables have now been changed by the sub.

hal = 0
bal = 0

demo 1, 2

PRINT hal, bal 'the variables have not been changed by the sub as the variables wasn't used as arguments.

SUB demo (hal, bal)

hal = 3
bal = 4

END SUB
```
  


#### SEE ALSO
* [SUB](./SUB.md) , [FUNCTION](./FUNCTION.md)
* Function (explanatory) , Statement
* Argument
