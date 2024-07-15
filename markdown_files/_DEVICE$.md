# _DEVICE$
> The _DEVICE$ function returns a STRING value holding the controller type, name and input types of the input devices on a computer.

## SYNTAX
`device$ = _DEVICE$( device_number )`

## EXAMPLES
> Example 1: Checking for the system's input devices and the number of buttons available.

```vb
devices = _DEVICES 'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
   PRINT _DEVICE$(i)
   PRINT "Buttons:"; _LASTBUTTON(i); "Axis:"; _LASTAXIS(i); "Wheels:"; _LASTWHEEL(i)
NEXT
```

> Example 2: Finding the number of mouse buttons available in QB64. This could also be used for other devices.

```vb
devices = _DEVICES 'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
   PRINT _DEVICE$(i)
   PRINT "Buttons:"; _LASTBUTTON(i); "Axis:"; _LASTAXIS(i); "Wheels:"; _LASTWHEEL(i)
NEXT
```


```vb
devices = _DEVICES 'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
   PRINT _DEVICE$(i)
   PRINT "Buttons:"; _LASTBUTTON(i); "Axis:"; _LASTAXIS(i); "Wheels:"; _LASTWHEEL(i)
NEXT
```

* [_DEVICES](_DEVICES.md) , [_DEVICEINPUT](_DEVICEINPUT.md)
* [_LASTBUTTON](_LASTBUTTON.md) , [_LASTAXIS](_LASTAXIS.md) , [_LASTWHEEL](_LASTWHEEL.md)
* [_BUTTON](_BUTTON.md) , [_BUTTONCHANGE](_BUTTONCHANGE.md)
* [_AXIS](_AXIS.md) , [_WHEEL](_WHEEL.md)
* [_MOUSEBUTTON](_MOUSEBUTTON.md)
* [STRIG](STRIG.md) , [STICK](STICK.md)
* [ON](ON.md) [STRIG](STRIG.md)(n) , [STRIG](STRIG.md)(n)
* Controller Devices

```vb
devices = _DEVICES 'MUST be read in order for other 2 device functions to work!
PRINT "Number of input devices found ="; devices
FOR i = 1 TO devices
   PRINT _DEVICE$(i)
   PRINT "Buttons:"; _LASTBUTTON(i); "Axis:"; _LASTAXIS(i); "Wheels:"; _LASTWHEEL(i)
NEXT
```



# SEE ALSO
* [_DEVICES](_DEVICES.md) , [_DEVICEINPUT](_DEVICEINPUT.md)
* [_LASTBUTTON](_LASTBUTTON.md) , [_LASTAXIS](_LASTAXIS.md) , [_LASTWHEEL](_LASTWHEEL.md)
* [_BUTTON](_BUTTON.md) , [_BUTTONCHANGE](_BUTTONCHANGE.md)
* [_AXIS](_AXIS.md) , [_WHEEL](_WHEEL.md)
* [_MOUSEBUTTON](_MOUSEBUTTON.md)
* [STRIG](STRIG.md) , [STICK](STICK.md)
* [ON](ON.md) [STRIG](STRIG.md)(n) , [STRIG](STRIG.md)(n)
* Controller Devices

