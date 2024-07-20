## TIMER (function)
---

### The TIMER function returns the number of seconds past the previous midnite down to an accuracy of 1/18th (QuickBASIC) or 1/1000th (QB64) of a second.

#### DESCRIPTION
* [TIMER](./TIMER.md) return values range from 0 at midnight to 86399! A comparison value must stay within that range!
* [INTEGER](./INTEGER.md) or [LONG](./LONG.md) second values range from 0 at midnight to 86399 seconds each day.
* QBasic can return [SINGLE](./SINGLE.md) values down to about .04 or 1/18th (one tick) of a second accurately.
* QB64 can read [DOUBLE](./DOUBLE.md) accuracy down to 1 millisecond. Example: start# = [TIMER](./TIMER.md)(.001)
* Use [DOUBLE](./DOUBLE.md) variables for millisecond accuracy as [SINGLE](./SINGLE.md) values are only accurate to 100ths of a second later in the day!
* [TIMER](./TIMER.md) loops should use a midnight adjustment to avoid non-ending loops in QBasic.
* [TIMER](./TIMER.md) can also be used for timing program Events. See [ON](./ON.md) [TIMER](./TIMER.md)(n) or the [TIMER](./TIMER.md) statement.
* QB64 can use a [_DELAY](./_DELAY.md) down to .001(one millisecond) or [_LIMIT](./_LIMIT.md) loops per second. Both help limit program CPU usage.


#### EXAMPLES
##### Example 1: Delay SUB with a midnight correction for when TIMER returns to 0. QB64 can use _DELAY for delays down to .001.
```vb
DO
 PRINT "Hello";
 Delay .5  'accuracy down to .05 seconds or 1/18th of a second in QBasic
 PRINT "World!";
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit

END

SUB Delay (dlay!)
start! = TIMER
DO WHILE start! + dlay! >= TIMER
 IF start! > TIMER THEN start! = start! - 86400
LOOP
END SUB
```
  
##### Example 2: Looping one TIMER tick of 1/18th of a second (ticks per second can be changed)
```vb
DEF SEG = 0 ' set to PEEK and POKE TIMER Ticks
DO ' main program loop
 ' program code
 POKE 1132, 0 ' zero Timer ticks
 DO ' delay loop
   x% = PEEK(1132)
   IF x% <> px% THEN PRINT x%;
   px% = x%
 LOOP UNTIL x% >= 18 '18 ticks in one second
 PRINT "code " ' program code
LOOP UNTIL INKEY$ = CHR$(27)
DEF SEG ' reset segment to default

END
```
  
```vb
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 code
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 code
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 code
```
  
##### Example 3: Using a DOUBLE variable for TIMER (.001) millisecond accuracy in QB64 throughout the day.
```vb
ts! = TIMER(.001)     'single variable
td# = TIMER(.001)     'double variable

PRINT "Single ="; ts!
PRINT "Double ="; td#
```
  
```vb
Single = 77073.09
Double = 77073.094
```
  


#### SEE ALSO
* [_DELAY](./_DELAY.md) , [_LIMIT](./_LIMIT.md) , [SLEEP](./SLEEP.md)
* [RANDOMIZE](./RANDOMIZE.md) , Scancodes
* [ON](./ON.md) [TIMER](./TIMER.md)(n) , [TIMER](./TIMER.md)
