# GOSUB
> GOSUB sends the program flow to a sub procedure identified by a line number or label.

## SYNTAX
`GOSUB { lineNumber | label }`

## DESCRIPTION
* Use [RETURN](RETURN.md) in a sub procedure to return to the next line of code after the original [GOSUB](GOSUB.md) call. [END](END.md) or [SYSTEM](SYSTEM.md) can also be used to end program.
* [GOSUB](GOSUB.md) and [GOTO](GOTO.md) can be used within [SUB](SUB.md) or [FUNCTION](FUNCTION.md) procedures, but cannot refer to a label located outside the procedure.


## EXAMPLES
> Example: Simple usage of GOSUB

```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```


```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```

> Example: What happens if two GOSUB executes then two RETURN's?

```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```

> Explanation: When a = 1 it uses GOSUB to go to "here:", then it uses GOTO to go back to "start:". a is increased by one so when a = 2 it uses GOSUB to go to "there:", and uses RETURN to go the last GOSUB (which is on the IF a = 2 line), it then encounters another RETURN which makes it return to the first GOSUB call we used on the IF a = 1 line.

```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```


```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```

* [ON](ON.md)...[GOSUB](GOSUB.md)
* [ON](ON.md)...[GOTO](GOTO.md) , [GOTO](GOTO.md)
* [ON](ON.md) [ERROR](ERROR.md) , [RESUME](RESUME.md)
* [ON](ON.md) [TIMER](TIMER.md)(n)
* Line number

```vb
PRINT "1. It goes to the subroutine."
GOSUB subroutine
PRINT "3. And it returns."
END

subroutine:
PRINT "2. It is at the subroutine."
RETURN
```



# SEE ALSO
* [ON](ON.md)...[GOSUB](GOSUB.md)
* [ON](ON.md)...[GOTO](GOTO.md) , [GOTO](GOTO.md)
* [ON](ON.md) [ERROR](ERROR.md) , [RESUME](RESUME.md)
* [ON](ON.md) [TIMER](TIMER.md)(n)
* Line number

