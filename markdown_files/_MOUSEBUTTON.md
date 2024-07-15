# _MOUSEBUTTON
> The _MOUSEBUTTON function returns the button status of a specified mouse button when read after _MOUSEINPUT .

## SYNTAX
`buttonStatus%% = _MOUSEBUTTON ( buttoNumber )`

## PARAMETERS
* [INTEGER](INTEGER.md) buttoNumber designates the mouse button to read (See [_DEVICES](_DEVICES.md) for more than 3). 1 = Left mouse button 2 = Right mouse button 3 = Center or scroll button
	* 1 = Left mouse button
	* 2 = Right mouse button
	* 3 = Center or scroll button
* 1 = Left mouse button
* 2 = Right mouse button
* 3 = Center or scroll button


## DESCRIPTION
* Returns -1 if the corresponding buttoNumber is pressed or zero when released.
* Read [_MOUSEINPUT](_MOUSEINPUT.md) first to return the current button up or down status. (See Example 2)
* Button clicks and mouse movements will be remembered and should be cleared after an [INPUT](INPUT.md) statement or other interruption.
* To clear unread mouse input, use a [_MOUSEINPUT](_MOUSEINPUT.md) loop that loops until it returns 0.
* Use _DEVICE$ to find the "[MOUSE]" [_DEVICES](_DEVICES.md) number to find the number of buttons available using [_LASTBUTTON](_LASTBUTTON.md) .
* Note: The center mouse button can also be read as [_BUTTON](_BUTTON.md) (2) on [_DEVICEINPUT](_DEVICEINPUT.md) (2) when a mouse is present.


## EXAMPLES
> Example 1: Finding the number of mouse buttons available in QB64. This could also be used for other controller devices.

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```

> Example 2: How to monitor when a button is down or wait until a mouse button is not held down.

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```

> Example 3: Checking for a click or a double-click by the user.

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```

> Example 4: Verifying that a user clicked and released a mouse button on a program button.

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```

> Example 5: Combining mouse button or keyboard selections in a menu or test:

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```


```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```

* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEWHEEL](_MOUSEWHEEL.md)
* [_MOUSEINPUT](_MOUSEINPUT.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* [_BUTTON](_BUTTON.md) , [_BUTTONCHANGE](_BUTTONCHANGE.md)
* Controller Devices

```vb
FOR d = 1 TO _DEVICES  'number of input devices found
 dev$ = _DEVICE$(d)
 IF INSTR(dev$, "[MOUSE]") THEN buttons = _LASTBUTTON(d): EXIT FOR
NEXT
PRINT buttons; "mouse buttons available"
```



# SEE ALSO
* [_MOUSEX](_MOUSEX.md) , [_MOUSEY](_MOUSEY.md) , [_MOUSEWHEEL](_MOUSEWHEEL.md)
* [_MOUSEINPUT](_MOUSEINPUT.md) , [_MOUSEMOVE](_MOUSEMOVE.md)
* [_MOUSESHOW](_MOUSESHOW.md) , [_MOUSEHIDE](_MOUSEHIDE.md)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* [_BUTTON](_BUTTON.md) , [_BUTTONCHANGE](_BUTTONCHANGE.md)
* Controller Devices

