## Function (explanatory)
---

### A BASIC function is a procedure that returns one value in it's name. A function can be used as a statement argument or be assigned to a variable .

#### EXAMPLES
##### Example 1: Some BASIC functions.
```vb
a = ABS(-1)
b = INT(2.54)
c = CINT(2.54)
PRINT "ABS(-1) gives"; a
PRINT "INT(2.54) gives"; b
PRINT "CINT(2.54) gives"; c
PRINT "ATN(1) * 4 gives"; ATN(1) * 4
```
  
##### Example 2: User-defined function.
```vb
d = dividebyhalf(4)

PRINT "dividebyhalf(4) gives"; d

FUNCTION dividebyhalf (number)
IF number <> 0 THEN
   half = number / 2
ELSE
   half = 0
END IF
dividebyhalf = half
END FUNCTION
```
  


#### SEE ALSO
* [SUB](./SUB.md) . [FUNCTION](./FUNCTION.md)
* Statement , Sub (explanatory)
* Argument
