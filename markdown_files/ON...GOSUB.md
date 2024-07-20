## ON...GOSUB
---

### ON...GOSUB is a control-flow statement that branches to a line or label in a list depending on a numerical expression.

#### SYNTAX

`ON numericalExpression GOSUB labelOrNumber [, labelOrNumber ][,...]`

#### DESCRIPTION
* numericalExpression represents the line or label that the program should branch to: 1 branches to the first line or label in the list, 2 branches to the second, etc.
* The procedure must be used after the number value is determined or in a loop to monitor current user events.
* [RETURN](./RETURN.md) returns to the next code statement after the [ON](./ON.md)...[GOSUB](./GOSUB.md) statement. [END](./END.md) or [SYSTEM](./SYSTEM.md) can be used to end program.
* Note: [SELECT](./SELECT.md) [CASE](./CASE.md) provides a much more convenient way of doing this task.


#### EXAMPLES
##### Example:
```vb
CLS
a = 2
ON a GOSUB hello, hereweare, 143
PRINT "Also notice the RETURN statement that can be used with GOSUB!"
END

hello:
PRINT "Hello, with a = 1 you get to see this!"
END

hereweare:
PRINT "with a = 2 here we are...return to line after ON."
RETURN

143
PRINT "Line 143, with a = 3 you get to see this!"
END
```
  
```vb
with a = 2 here we are...return to line after ON.
Also notice the RETURN statement that can be used with GOSUB!
```
  


#### SEE ALSO
* [ON](./ON.md)...[GOTO](./GOTO.md)
* [GOSUB](./GOSUB.md) , [GOTO](./GOTO.md)
* [SELECT](./SELECT.md) [CASE](./CASE.md) , [RETURN](./RETURN.md)
