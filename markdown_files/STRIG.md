# STRIG
> The STRIG function returns button press True or False status of game port (&H201) or USB joystick control device(s).

## DESCRIPTION
* Function returns -1 when a button event(even functions) has occurred or a button is pressed(odd functions).
* [STRIG](STRIG.md) will not read keyboard or mouse buttons detected by [_DEVICES](_DEVICES.md) .
* The device number must be used with more than 2 devices. Use device 1 function numbers for just one joystick.
* QB64 can read many buttons from many devices and allows the use of devices with more than 2 buttons.
* Returns True(-1) or False(0) button press values for 2 devices. Each leading [STRIG](STRIG.md) checks for missed button press events:


## EXAMPLES
> Example: Displays the input from 3 joysticks, all with dual sticks and 3 buttons.

```vb
STRIG(0) = -1  'lower button 1 on device 1 pressed since last STRIG(0) read
 STRIG(1) = -1  'lower button 1 on device 1 currently pressed
 STRIG(2) = -1  'lower button 1 on device 2 pressed since last STRIG(2) read
 STRIG(3) = -1  'lower button 1 on device 2 currently pressed
 STRIG(4) = -1  'upper button 2 on device 1 pressed since last STRIG(4) read
 STRIG(5) = -1  'upper button 2 on device 1 currently pressed
 STRIG(6) = -1  'upper button 2 on device 2 pressed since last STRIG(6) read
 STRIG(7) = -1  'upper button 2 on device 2 currently pressed (maximum in QBasic)
 STRIG(8) = -1  'button 3 on device 1 pressed since last STRIG(8) read  'QB64 only
 STRIG(9) = -1  'button 3 on device 1 currently pressed
 STRIG(10) = -1 'button 3 on device 2 pressed since last STRIG(10) read 'QB64 only
 STRIG(11) = -1 'button 3 on device 2 currently pressed
```


```vb
STRIG(0) = -1  'lower button 1 on device 1 pressed since last STRIG(0) read
 STRIG(1) = -1  'lower button 1 on device 1 currently pressed
 STRIG(2) = -1  'lower button 1 on device 2 pressed since last STRIG(2) read
 STRIG(3) = -1  'lower button 1 on device 2 currently pressed
 STRIG(4) = -1  'upper button 2 on device 1 pressed since last STRIG(4) read
 STRIG(5) = -1  'upper button 2 on device 1 currently pressed
 STRIG(6) = -1  'upper button 2 on device 2 pressed since last STRIG(6) read
 STRIG(7) = -1  'upper button 2 on device 2 currently pressed (maximum in QBasic)
 STRIG(8) = -1  'button 3 on device 1 pressed since last STRIG(8) read  'QB64 only
 STRIG(9) = -1  'button 3 on device 1 currently pressed
 STRIG(10) = -1 'button 3 on device 2 pressed since last STRIG(10) read 'QB64 only
 STRIG(11) = -1 'button 3 on device 2 currently pressed
```

* [STRIG](STRIG.md)(n)
* [ON](ON.md) [STRIG](STRIG.md)(n) , [STICK](STICK.md)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* Single and Dual Stick Controllers

```vb
STRIG(0) = -1  'lower button 1 on device 1 pressed since last STRIG(0) read
 STRIG(1) = -1  'lower button 1 on device 1 currently pressed
 STRIG(2) = -1  'lower button 1 on device 2 pressed since last STRIG(2) read
 STRIG(3) = -1  'lower button 1 on device 2 currently pressed
 STRIG(4) = -1  'upper button 2 on device 1 pressed since last STRIG(4) read
 STRIG(5) = -1  'upper button 2 on device 1 currently pressed
 STRIG(6) = -1  'upper button 2 on device 2 pressed since last STRIG(6) read
 STRIG(7) = -1  'upper button 2 on device 2 currently pressed (maximum in QBasic)
 STRIG(8) = -1  'button 3 on device 1 pressed since last STRIG(8) read  'QB64 only
 STRIG(9) = -1  'button 3 on device 1 currently pressed
 STRIG(10) = -1 'button 3 on device 2 pressed since last STRIG(10) read 'QB64 only
 STRIG(11) = -1 'button 3 on device 2 currently pressed
```



# SEE ALSO
* [STRIG](STRIG.md)(n)
* [ON](ON.md) [STRIG](STRIG.md)(n) , [STICK](STICK.md)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* Single and Dual Stick Controllers

