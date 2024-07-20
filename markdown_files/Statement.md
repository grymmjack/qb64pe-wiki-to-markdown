## Statement
---

### A statement is, as far as BASIC is concerned, a keyword that can be executed in run-time which doesn't return any value. It can contain several arguments or no arguments at all.

#### EXAMPLES
##### Example 1: Demonstrates how x- and y-coordinates are enclosed with paranteses (in graphics).
```vb
SCREEN 13
x = 160
y = 100
PSET (x, y), 15
```
  
##### Example 2: Demonstrates how row- and column-coordinates are not enclosed with paranteses (in text).
```vb
row = 12
column = 40
LOCATE row, column
PRINT "X"
```
  


#### SEE ALSO
* Function (explanatory)
* Argument
