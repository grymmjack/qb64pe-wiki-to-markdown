# _DEVICEINPUT
> The _DEVICEINPUT function returns the device number when a controller device button, wheel or axis event occurs.

## SYNTAX
`device% = _DEVICEINPUT`

## PARAMETERS
* Use the device% [INTEGER](INTEGER.md) returned to find the number of the controller device being used.
* A literal specific device_number% parameter can be used to return -1 if active or 0 if inactive, e.g. [WHILE](WHILE.md) [_DEVICEINPUT](_DEVICEINPUT.md) ( 2 ) .


## DESCRIPTION
* Use [_DEVICES](_DEVICES.md) to find the number of controller devices available BEFORE using this function.
* _DEVICE$ can be used to list the device names and control types using valid [_DEVICES](_DEVICES.md) numbers.
* When a device button is pressed or a scroll wheel or axis is moved, the device number will be returned.
* Devices are numbered as 1 for keyboard and 2 for mouse. Other controller devices will be numbered 3 or higher if installed.
* [_LASTBUTTON](_LASTBUTTON.md) , [_LASTAXIS](_LASTAXIS.md) , or [_LASTWHEEL](_LASTWHEEL.md) will indicate the number of functions available with the specified device% number.
* User input events can be monitored reading valid numbered [_AXIS](_AXIS.md) , [_BUTTON](_BUTTON.md) , [_BUTTONCHANGE](_BUTTONCHANGE.md) or [_WHEEL](_WHEEL.md) functions.
* [ON](ON.md) [_DEVICEINPUT](_DEVICEINPUT.md) [GOSUB](GOSUB.md) keyboard, mouse, gamecontrol could be used to easily branch to device specific handler routines (see Example 3 below).


## EXAMPLES

```vb
FOR i% = 1 TO _DEVICES
   PRINT STR$(i%) + ") " + _DEVICE$(i%)
   PRINT "Button:"; _LASTBUTTON(i%); ",Axis:"; _LASTAXIS(i%); ",Wheel:"; _LASTWHEEL(i%)
NEXT i%

PRINT
DO
   x% = _DEVICEINPUT
   IF x% THEN PRINT "Device ="; x%;
LOOP UNTIL INKEY$ = CHR$(27)

END
```

* [_DEVICES](_DEVICES.md) , _DEVICE$
* [_LASTBUTTON](_LASTBUTTON.md) , [_LASTAXIS](_LASTAXIS.md) , [_LASTWHEEL](_LASTWHEEL.md)
* [_BUTTON](_BUTTON.md) , [_AXIS](_AXIS.md) , [_WHEEL](_WHEEL.md)
* [STRIG](STRIG.md) , [STICK](STICK.md)
* [ON](ON.md)...[GOSUB](GOSUB.md)
* Controller Devices

```vb
FOR i% = 1 TO _DEVICES
   PRINT STR$(i%) + ") " + _DEVICE$(i%)
   PRINT "Button:"; _LASTBUTTON(i%); ",Axis:"; _LASTAXIS(i%); ",Wheel:"; _LASTWHEEL(i%)
NEXT i%

PRINT
DO
   x% = _DEVICEINPUT
   IF x% THEN PRINT "Device ="; x%;
LOOP UNTIL INKEY$ = CHR$(27)

END
```



# SEE ALSO
* [_DEVICES](_DEVICES.md) , _DEVICE$
* [_LASTBUTTON](_LASTBUTTON.md) , [_LASTAXIS](_LASTAXIS.md) , [_LASTWHEEL](_LASTWHEEL.md)
* [_BUTTON](_BUTTON.md) , [_AXIS](_AXIS.md) , [_WHEEL](_WHEEL.md)
* [STRIG](STRIG.md) , [STICK](STICK.md)
* [ON](ON.md)...[GOSUB](GOSUB.md)
* Controller Devices

