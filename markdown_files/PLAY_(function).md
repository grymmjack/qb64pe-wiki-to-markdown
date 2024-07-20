## PLAY (function)
---

### The PLAY function returns the number of remaining notes/samples/seconds in the background music queue.

#### SYNTAX

`remaining& = PLAY ( numericExpression& )`

#### PARAMETERS
* remaining& is the number of notes/samples/seconds left to play in the background music queue.
* numericExpression& can be any numeric expression.
* See also the important version dependent notes in the Availability section.


#### DESCRIPTION
* This function may be used to detect, if the background music queue is still playing.
* When there is nothing left to play, then this function returns zero.


#### EXAMPLES
```vb
PLAY "mb l4cf.l8el4fag.l8fl4gl8agl4f.l8fl4a>cl2dl4dl4c.<l8al4afg.l8fl4gl8agl4f.l8dl4dcl2f>l4dc.<l8al4afg.l8fl4g>dc.<l8al4a>cl2dl4dc.<l8al4afg.l8fl4gl8agl4f.l8dl4dcl1f"

PRINT "Playing tune..."

DO
   smplLeft& = PLAY(0)
   timeLeft& = PLAY(1)
   LOCATE 3, 1: PRINT "Samples left to play ="; smplLeft&; " ";
   LOCATE 4, 1: PRINT "Seconds left to play ="; timeLeft&; " ";
LOOP WHILE smplLeft&

PRINT: PRINT: PRINT "And we are done!"
END
```
  


#### SEE ALSO
* [PLAY](./PLAY.md)
* [SOUND](./SOUND.md)
* [BEEP](./BEEP.md)
* [_SNDOPEN](./_SNDOPEN.md)
* [_SNDRAW](./_SNDRAW.md)
