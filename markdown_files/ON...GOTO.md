## ON...GOTO
---

### ON...GOTO is a control-flow statement that branches to a line or label in a list depending on a numerical expression.

#### SYNTAX

`ON numericalExpression GOTO labelOrNumber [, labelOrNumber ][,...]`

#### DESCRIPTION
* numericalExpression represents the line or label that the program should branch to: 1 branches to the first line or label in the list, 2 branches to the second, etc.
* The procedure must be used after the number value is determined or in a loop to monitor current user events.
* Note: [SELECT](./SELECT.md) [CASE](./CASE.md) provides a much more convenient way of doing this task.


#### EXAMPLES
##### Example: Changing the program flow when a value is not 0.
```vb
CLS
a = 2
ON a GOTO hello, hereweare, 143
END
hello:
PRINT "you don't get to see this!"
END
hereweare:
PRINT "And here we are..."
END
143
PRINT "you don't get to see this neither..."
END
```
  
```vb
And here we are...
```
  
##### Explanation: Since a equals 2 it goes to the second item in the list (hereweare) and branches to there. Try changing a' to 1 or 3.


#### SEE ALSO
* [ON](./ON.md)...[GOSUB](./GOSUB.md)
* [GOTO](./GOTO.md)
* [GOSUB](./GOSUB.md)
* [SELECT](./SELECT.md) [CASE](./CASE.md)
