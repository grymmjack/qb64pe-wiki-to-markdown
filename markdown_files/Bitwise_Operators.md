## Bitwise Operators
---

### Bitwise operators are much like the regular mathematics operators (+, * etc.) but are defined in terms of the individual bits of their operands. The full list of bitwise operators, with a brief summary of its operation:

#### DESCRIPTION


#### EXAMPLES
```vb
x& = VAL("&B101010") 'Arbitrary collection of bits
y& = VAL("&B001100") 'A bit mask
PRINT "Input 1: "; BinStr$(x&, 6) '6 indicates we want 6 bits of output
PRINT "Input 2: "; BinStr$(y&, 6)
PRINT "Output:  "; BinStr$(x& AND y&, 6)

'Converts the number n& to a string of binary digits, digits& long (padding or truncating as necessary).
FUNCTION BinStr$ (n&, digits&)
   FOR i& = digits& - 1 TO 0 STEP -1
       IF (n& AND 2 ^ i&) THEN B$ = B$ + "1" ELSE B$ = B$ + "0"
   NEXT
   BinStr$ = B$
END FUNCTION
```
  
```vb
Input 1: 101010
Input 2: 001100
Output:  001000
```
  
```vb
'The trick here is to give each flag a value corresponding to a different bit being 1
FLAG_A& = VAL("&B0001")
FLAG_B& = VAL("&B0010")
FLAG_C& = VAL("&B0100")
FLAG_D& = VAL("&B1000")

flags& = FLAG_A& OR FLAG_C& 'Set flags A, C

'Use each flag as a bitmask to test for its presence:
IF flags& AND FLAG_A& THEN PRINT "Flag A is set"
IF flags& AND FLAG_B& THEN PRINT "Flag B is set"
IF flags& AND FLAG_C& THEN PRINT "Flag C is set"
IF flags& AND FLAG_D& THEN PRINT "Flag D is set"
```
  
```vb
Flag A is set
Flag C is set
```
  
```vb
'The trick here is to give each flag a value corresponding to a different bit being 1
FLAG_A& = VAL("&B0001")
FLAG_B& = VAL("&B0010")
FLAG_C& = VAL("&B0100")
FLAG_D& = VAL("&B1000")

flags& = FLAG_A& OR FLAG_C& 'Set flags A, C
flags& = flags& XOR FLAG_A& XOR FLAG_B& 'Toggle flags A, B

'Use each flag as a bitmask to test for its presence:
IF flags& AND FLAG_A& THEN PRINT "Flag A is set"
IF flags& AND FLAG_B& THEN PRINT "Flag B is set"
IF flags& AND FLAG_C& THEN PRINT "Flag C is set"
IF flags& AND FLAG_D& THEN PRINT "Flag D is set"
```
  
```vb
Flag B is set
Flag C is set
```
  

