## _BLINK (function)
---

### The _BLINK function returns the current blink setting for SCREEN 0 colors. If enabled, returns -1 (default), otherwise returns 0.

#### SYNTAX

`blinkState%% = _BLINK`

#### EXAMPLES
```vb
COLOR 16, 7

'Try uncommenting the line below:
'_BLINK OFF

IF _BLINK THEN
   PRINT "I'm blinking"
ELSE
   PRINT "I'm not blinking"
END IF
```
  


#### SEE ALSO
* Featured in our "Keyword of the Day" series
* [_BLINK](./_BLINK.md) (statement)
* [OUT](./OUT.md)
