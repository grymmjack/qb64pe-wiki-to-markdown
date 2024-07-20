## Controller Devices
---

### QB64 supports all kinds of keyboard, mouse, joystick, gamepad, steering wheel and other multi-stick controller input devices.

#### SYNTAX

`Displays all keyboard, mouse and game controller button, axis and wheel control input values when each device is being used.`

#### EXAMPLES
```vb
PRINT "Use relative mouse movement mode with ESC key exit only?(Y/N) ";
K$ = UCASE$(INPUT$(1))
PRINT K$
PRINT

FOR i = 1 TO _DEVICES 'DEVICES MUST be read first!
   PRINT STR$(i) + ") " + _DEVICE$(i) + " Buttons:"; _LASTBUTTON(i); ",Axis:"; _LASTAXIS(i); ",Wheel:"; _LASTWHEEL(i)
NEXT
IF K$ = "Y" THEN dummy = _MOUSEMOVEMENTX 'enable relative mouse movement reads
PRINT

DO
   x& = _DEVICEINPUT 'determines which device is currently being used
   IF x& = 1 THEN
       PRINT "Keyboard: ";
       FOR b = 1 TO _LASTBUTTON(x&)
           bb = _BUTTONCHANGE(b)
           IF bb THEN PRINT b; bb; _BUTTON(b);
       NEXT
       PRINT
   END IF
   IF x& > 1 THEN '  skip keyboard reads
       PRINT "Device:"; x&;
       FOR b = 1 TO _LASTBUTTON(x&)
           PRINT _BUTTONCHANGE(b); _BUTTON(b);
       NEXT
       FOR a = 1 TO _LASTAXIS(x&)
           PRINT _AXIS(a); 'mouse axis returns -1 to 1 with 0 center screen
       NEXT
       FOR w = 1 TO _LASTWHEEL(x&)
           PRINT _WHEEL(w); 'wheels 1 and 2 of mouse return relative pixel moves when enabled
       NEXT
       PRINT
   END IF
LOOP UNTIL INKEY$ = CHR$(27) 'escape key exit

END
```
  
##### ( Return to Table of Contents )


#### SEE ALSO
* [_DEVICEINPUT](./_DEVICEINPUT.md) , [_AXIS](./_AXIS.md) , [_BUTTON](./_BUTTON.md) , [_BUTTONCHANGE](./_BUTTONCHANGE.md) , [_WHEEL](./_WHEEL.md)
* [_DEVICES](./_DEVICES.md) , _DEVICE$ , [_LASTAXIS](./_LASTAXIS.md) , [_LASTBUTTON](./_LASTBUTTON.md) , [_LASTWHEEL](./_LASTWHEEL.md)
* [_MOUSEINPUT](./_MOUSEINPUT.md) , [_MOUSEX](./_MOUSEX.md) , [_MOUSEY](./_MOUSEY.md) , [_MOUSEBUTTON](./_MOUSEBUTTON.md) , [_MOUSEWHEEL](./_MOUSEWHEEL.md)
* [_MOUSEMOVE](./_MOUSEMOVE.md) , [_MOUSEHIDE](./_MOUSEHIDE.md) , [_MOUSESHOW](./_MOUSESHOW.md)
* [_MOUSEMOVEMENTX](./_MOUSEMOVEMENTX.md) , [_MOUSEMOVEMENTY](./_MOUSEMOVEMENTY.md) (relative movement)
* [STRIG](./STRIG.md) (button) , [STICK](./STICK.md) (axis)
