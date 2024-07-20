## Variable
---

### A variable is a "container" name that can hold a numerical or string value which can be referenced or changed by the program (as opposed to CONSTant values which never change).

#### EXAMPLES
##### Example of different usages of variables:
```vb
max = 1000
DIM d(max)
FOR c = 1 TO max
d(c) = c + d(c - 1)
NEXT
PRINT "Show the result of the addition from 1 to n (1+2+3...+n)"
PRINT "n = (0-" + LTRIM$(STR$(max)) + "): ";
INPUT "", n
IF n <= max AND n >= 0 THEN PRINT d(n) ELSE PRINT "Invalid value (only 0 to" + STR$(max) + " is permitted)."
```
  
```vb
Show the result of the addition from 1 to n (1+2+3...+n)
n = (1-1000): 10
55
```
  


#### SEE ALSO
* Argument , Expression , Arrays
