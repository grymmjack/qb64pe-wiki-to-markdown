## INPUT (file statement)
---

### The INPUT # file or port statement reads sequential data using one variable or a comma separated list of matching variable types.

#### SYNTAX

`INPUT # fileNumber& , variable1 [, variable2 , ..., variableN ]`

#### PARAMETERS
* fileNumber& is a positive [LONG](./LONG.md) integer value used to [OPEN](./OPEN.md) the file [FOR](./FOR.md) [INPUT](./INPUT.md) mode.
* The type of the variable used defines the value or list of values to be returned from the file. Numeric types must match the values returned.
* As reflected in the syntax you can list a number of variables with different types seperated by a comma and they will hold the values in the file (keep in mind that the information in the file should match the variable types used).


#### DESCRIPTION
* The file number can be determined by the programmer or be an unused number returned by the [FREEFILE](./FREEFILE.md) function.
* Variable types must match the numerical types being read. [STRING](./STRING.md) variables can return unquoted numeric values.
* Leading or trailing spaces of [STRING](./STRING.md) values must be inside of quotes. [WRITE](./WRITE.md) # writes strings inside of quotes automatically. [PRINT](./PRINT.md) # removes quotes.
* [INPUT](./INPUT.md) # will read each value until it encounters a comma for the next value in a list.
* Use the [EOF](./EOF.md) function to avoid reading past the end of a file.
* Files created by [WRITE](./WRITE.md) # usually have the same number of values on each file line. If [INPUT](./INPUT.md) reads more or less values, it may read beyond the end of file or return bad data.
* Use the [LINE](./LINE.md) [INPUT](./INPUT.md) (file statement) for files created with [PRINT](./PRINT.md) # or [PRINT](./PRINT.md) #, [USING](./USING.md).
* [INPUT](./INPUT.md) can read Excel CSV files, but beware of unquoted text or numerical values containing commas.


#### EXAMPLES
##### Example 1: Writes new data to a text file sequentially and reads it back to the program screen.
```vb
filename$ = "testfile.dat"
x = 1: y = 2: z$ = "Three"

OPEN filename$ FOR OUTPUT AS #1 'opens and clears an existing file or creates new empty file
WRITE #1, x, y, z$
CLOSE #1

PRINT "File created with data. Press a key!"
K$ = INPUT$(1) 'press a key

OPEN filename$ FOR INPUT AS #2 'opens a file to read it
INPUT #2, a, b, c$
CLOSE #2

PRINT a, b, c$
WRITE a, b, c$

END
```
  
```vb
1           2          Three
1,2,"Three"
```
  
```vb
1,2,"Three"
```
  
##### Example 2: Commas inside of string values will not affect the INPUT value as those commas are not WRITE separators.
```vb
x$ = "Hello, how are you?"
y$ = "I'm fine."

OPEN "testinp.dat" FOR OUTPUT AS #1
WRITE #1, x$, y$
CLOSE #1


OPEN "testinp.dat" FOR INPUT AS #1

INPUT #1, a$, b$
CLOSE #1

PRINT a$, b$
WRITE a$, b$
```
  
```vb
Hello, how are you?        I'm fine.
"Hello, how are you?","I'm fine."
```
  
```vb
"Hello, how are you?","I'm fine."
```
  


#### SEE ALSO
* [INPUT](./INPUT.md) (file mode) , [LINE](./LINE.md) [INPUT](./INPUT.md) # , [INPUT](./INPUT.md)$ (file input)
* [INPUT](./INPUT.md) , [LINE](./LINE.md) [INPUT](./INPUT.md) , [INPUT](./INPUT.md)$ (keyboard input)
* [PRINT](./PRINT.md) # , [PRINT](./PRINT.md) #, [USING](./USING.md)
* [GET](./GET.md) #
