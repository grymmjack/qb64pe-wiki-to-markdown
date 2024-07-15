# STICK
> The STICK function returns the directional axis coordinate move of game port (&H201) joystick or USB controller devices.

## DESCRIPTION
* QB64 allows any number of coordinate pairs for more than two game device controllers. [STICK](STICK.md) will not read a mouse axis.
* axis_number can be used as the next axis parameter for controllers with multiple axis using the SAME directional parameters.
* The axis_number 1 can be omitted for the main stick column and row parameter reads.
* Point of view "hats" also have 2 axis. Slide, turn or twist controls have one. The device determines the order of the axis.
* Returns coordinate values from 1 to 254. QBasic only returned values from 1 to 200.
* [STICK](STICK.md)(0) is required to get values from the other [STICK](STICK.md) functions. Always read it first!


## EXAMPLES
> Example 1: Displays the input from 3 joysticks, all with dual sticks and 3 buttons.

```vb
STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.
STICK(1) returns row coordinate of device 1.
STICK(2) returns column coordinate of device 2. (second joystick if used)
STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers)
STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)
STICK(5) returns row coordinate of device 3 if used.
```

> Example 2: Displays the Sidewinder Precision Pro Stick, Slider, Z Axis, and Hat Point of View.

```vb
STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.
STICK(1) returns row coordinate of device 1.
STICK(2) returns column coordinate of device 2. (second joystick if used)
STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers)
STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)
STICK(5) returns row coordinate of device 3 if used.
```


```vb
STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.
STICK(1) returns row coordinate of device 1.
STICK(2) returns column coordinate of device 2. (second joystick if used)
STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers)
STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)
STICK(5) returns row coordinate of device 3 if used.
```

* [STRIG](STRIG.md)
* [ON](ON.md) [STRIG](STRIG.md)(n)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* Single and Dual Stick Controllers

```vb
STICK(0) returns the column coordinate of device 1. Enables reads of the other STICK values.
STICK(1) returns row coordinate of device 1.
STICK(2) returns column coordinate of device 2. (second joystick if used)
STICK(3) returns row coordinate of device 2 if used. (QBasic maximum was 2 controllers)
STICK(4) returns column coordinate of device 3. (other joysticks if used in QB64 only!)
STICK(5) returns row coordinate of device 3 if used.
```



# SEE ALSO
* [STRIG](STRIG.md)
* [ON](ON.md) [STRIG](STRIG.md)(n)
* [_DEVICES](_DEVICES.md) , _DEVICE$ , [_LASTBUTTON](_LASTBUTTON.md)
* Single and Dual Stick Controllers

