## MID$ (function)
---

### The MID$ function returns a portion of a STRING .

#### SYNTAX

`portion$ = MID$ ( stringValue$ , startPosition% [, bytes% ])`

#### PARAMETERS
* stringValue$ can be any literal or variable non-empty [STRING](./STRING.md) value. Use [LEN](./LEN.md) to check the length of a string.
* startPosition% designates the non-zero position of the first character to be returned by the function.
* bytes% (optional) tells the function how many characters to return including the first character at startPosition% .


#### DESCRIPTION
* When the bytes% value is not passed, the function returns the remainder of the string from the starting character position.
* Number of character bytes% should be within the string's length from the start position, but will only return the string's remainder when exceeded.
* If the bytes% value is 0 or the startPosition% is 0 or greater than the length of the string, an empty string is returned (no error is triggered).
* In QB64 , the [ASC](./ASC.md) (function) reads string byte positions about 5 times faster than MID$ when parsing strings character wise. See Example 2 below.


#### EXAMPLES
```vb
PRINT TIME$

hour$ = LEFT$(TIME$, 2)
minutes$ = MID$(TIME$, 4, 2) ' skip hours and the colon (first 3 characters)

PRINT "hour = "; hour$; ": minutes = "; minutes$
```
  
```vb
11:23:30
hour = 11: minutes = 23
```
  
```vb
_TITLE "String Speed Test"
DEFLNG A-Z

'First let's build a string for testing.
Limit = 100000 'the size of the string
LoopCount = 1000 'the number of times we want to deconstruct it

FOR i = 1 TO Limit
 t$ = t$ + CHR$(RND * 255)
NEXT

'now for some times

t1# = TIMER
FOR j = 1 TO LoopCount
 FOR i = 1 TO Limit
   m$ = MID$(t$, i, 1)
 NEXT
NEXT
t2# = TIMER
FOR j = 1 TO LoopCount
 FOR i = 1 TO Limit
   m = ASC(t$, i)
 NEXT
NEXT

t3# = TIMER
$CHECKING:OFF
DIM m AS _MEM, m1 AS STRING * 1, m2 AS _UNSIGNED _BYTE
m = _MEMNEW(Limit) 'create new memory space for string
_MEMPUT m, m.OFFSET, t$ 'put string t$ into memory space
FOR j = 1 TO LoopCount
 FOR i = 1 TO Limit
   _MEMGET m, m.OFFSET + i - 1, m1
 NEXT
NEXT
t4# = TIMER
FOR j = 1 TO LoopCount
 FOR i = 1 TO Limit
   _MEMGET m, m.OFFSET + i - 1, m2
 NEXT
NEXT
t5# = TIMER

'results

PRINT USING "##.###### seconds for MID$"; t2# - t1#
PRINT USING "##.###### seconds for ASC"; t3# - t2#
PRINT USING "##.###### seconds for _MEMGET String"; t4# - t3#
PRINT USING "##.###### seconds for _MEMGET Byte"; t5# - t4#
```
  
```vb
6.593750 seconds for MID$
1.044922 seconds for ASC
0.494141 seconds for _MEMGET String
0.494141 seconds for _MEMGET Byte
```
  


#### SEE ALSO
* MID$
* [ASC](./ASC.md) , [ASC](./ASC.md) (function)
* LEFT$ , RIGHT$
* LTRIM$ , RTRIM$
* [INSTR](./INSTR.md) , [LEN](./LEN.md)
* [_MEMPUT](./_MEMPUT.md) , [_MEMGET](./_MEMGET.md)
