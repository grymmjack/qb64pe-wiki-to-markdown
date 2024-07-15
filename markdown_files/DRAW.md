# DRAW
> The DRAW statement uses a STRING expression to draw lines on the screen.

## SYNTAX
`DRAW drawString$`

## DESCRIPTION
* The drawString$ can be [DRAW](DRAW.md) instructions in quotation marks or a [STRING](STRING.md) variable using [DRAW](DRAW.md) instructions.
* [DRAW](DRAW.md) starting coordinates can be set using [PSET](PSET.md) , [PRESET](PRESET.md) , [CIRCLE](CIRCLE.md) or [LINE](LINE.md) ending positions.
* Other graphic objects can be located at or relative to the last [DRAW](DRAW.md) position using [STEP](STEP.md) .
* [DRAW](DRAW.md) can inherit colors from other graphic statements such as [PSET](PSET.md) , [LINE](LINE.md) and [CIRCLE](CIRCLE.md) .
* Draw strings use letters followed by the number of pixels to move, an angle, coordinate or a color value.
* Draw strings are flexible with spacing. Spacing is not required. [DRAW](DRAW.md) will look for a number value after a valid letter.
* [DRAW](DRAW.md) statements are not case sensitive. " B " (blind) before a line move designates that the line move will be hidden. Use to offset from a "P" or [PAINT](PAINT.md) border. " C n" designates the color attribute or [_RGB](_RGB.md) string numerical color value to be used in the draw statement immediately after. " M x, y" can move to another coordinate area of the screen. When a + or - sign is used before a coordinate, it is a relative coordinate move similar to using the [STEP](STEP.md) graphics keyword. [DRAW](DRAW.md) "M+=" + [VARPTR](VARPTR.md)$ (variable%) " N " before a line move designates that the graphic cursor will return to the starting position after the line is drawn. " P f [, b]" is used to paint enclosed objects. f denotes the fill color and b the border color, if needed. " S n" changes the pixel move size of the lines. Default is 4 (1 pixel) minimum. "S8" would double the pixel line moves. " X " + [VARPTR](VARPTR.md)$ (value) can draw another substring.
	* " B " (blind) before a line move designates that the line move will be hidden. Use to offset from a "P" or [PAINT](PAINT.md) border.
	* " C n" designates the color attribute or [_RGB](_RGB.md) string numerical color value to be used in the draw statement immediately after.
	* " M x, y" can move to another coordinate area of the screen. When a + or - sign is used before a coordinate, it is a relative coordinate move similar to using the [STEP](STEP.md) graphics keyword. [DRAW](DRAW.md) "M+=" + [VARPTR](VARPTR.md)$ (variable%)
	* " N " before a line move designates that the graphic cursor will return to the starting position after the line is drawn.
	* " P f [, b]" is used to paint enclosed objects. f denotes the fill color and b the border color, if needed.
	* " S n" changes the pixel move size of the lines. Default is 4 (1 pixel) minimum. "S8" would double the pixel line moves.
	* " X " + [VARPTR](VARPTR.md)$ (value) can draw another substring.
* " B " (blind) before a line move designates that the line move will be hidden. Use to offset from a "P" or [PAINT](PAINT.md) border.
* " C n" designates the color attribute or [_RGB](_RGB.md) string numerical color value to be used in the draw statement immediately after.
* " M x, y" can move to another coordinate area of the screen. When a + or - sign is used before a coordinate, it is a relative coordinate move similar to using the [STEP](STEP.md) graphics keyword. [DRAW](DRAW.md) "M+=" + [VARPTR](VARPTR.md)$ (variable%)
* " N " before a line move designates that the graphic cursor will return to the starting position after the line is drawn.
* " P f [, b]" is used to paint enclosed objects. f denotes the fill color and b the border color, if needed.
* " S n" changes the pixel move size of the lines. Default is 4 (1 pixel) minimum. "S8" would double the pixel line moves.
* " X " + [VARPTR](VARPTR.md)$ (value) can draw another substring.
* Certain letter designations create line moves on the [SCREEN](SCREEN.md). Each move is followed by the number of pixels: " D n" draws a line vertically DOWN n pixels. " E n" draws a diagonal / line going UP and RIGHT n pixels each direction. " F n" draws a diagonal \ line going DOWN and RIGHT n pixels each direction. " G n" draws a diagonal / [LINE](LINE.md) going DOWN and LEFT n pixels each direction. " H n" draws a diagonal \ [LINE](LINE.md) going UP and LEFT n pixels each direction. " L n" draws a line horizontally LEFT n pixels. " R n" draws a line horizontally RIGHT n pixels. " U n" draws a line vertically UP n pixels.
	* " D n" draws a line vertically DOWN n pixels.
	* " E n" draws a diagonal / line going UP and RIGHT n pixels each direction.
	* " F n" draws a diagonal \ line going DOWN and RIGHT n pixels each direction.
	* " G n" draws a diagonal / [LINE](LINE.md) going DOWN and LEFT n pixels each direction.
	* " H n" draws a diagonal \ [LINE](LINE.md) going UP and LEFT n pixels each direction.
	* " L n" draws a line horizontally LEFT n pixels.
	* " R n" draws a line horizontally RIGHT n pixels.
	* " U n" draws a line vertically UP n pixels.
* " D n" draws a line vertically DOWN n pixels.
* " E n" draws a diagonal / line going UP and RIGHT n pixels each direction.
* " F n" draws a diagonal \ line going DOWN and RIGHT n pixels each direction.
* " G n" draws a diagonal / [LINE](LINE.md) going DOWN and LEFT n pixels each direction.
* " H n" draws a diagonal \ [LINE](LINE.md) going UP and LEFT n pixels each direction.
* " L n" draws a line horizontally LEFT n pixels.
* " R n" draws a line horizontally RIGHT n pixels.
* " U n" draws a line vertically UP n pixels.
* Angles are used to rotate all subsequent draw moves. " A n" can use values of 1 to 3 to rotate up to 3 90 degree(270) angles. TA n" can use any n angle from -360 to 0 to 360 to rotate a [DRAW](DRAW.md) (Turn Angle). "TA0" resets to normal. When [VARPTR](VARPTR.md)$ is used, [DRAW](DRAW.md) functions such as TA angles use an equal sign: "TA=" + [VARPTR](VARPTR.md)$(angle%)
	* " A n" can use values of 1 to 3 to rotate up to 3 90 degree(270) angles.
	* TA n" can use any n angle from -360 to 0 to 360 to rotate a [DRAW](DRAW.md) (Turn Angle). "TA0" resets to normal.
	* When [VARPTR](VARPTR.md)$ is used, [DRAW](DRAW.md) functions such as TA angles use an equal sign: "TA=" + [VARPTR](VARPTR.md)$(angle%)
* " A n" can use values of 1 to 3 to rotate up to 3 90 degree(270) angles.
* TA n" can use any n angle from -360 to 0 to 360 to rotate a [DRAW](DRAW.md) (Turn Angle). "TA0" resets to normal.
* When [VARPTR](VARPTR.md)$ is used, [DRAW](DRAW.md) functions such as TA angles use an equal sign: "TA=" + [VARPTR](VARPTR.md)$(angle%)
* The graphic cursor is set to the center of the program window on program start for [STEP](STEP.md) relative coordinates.
* [DRAW](DRAW.md) can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.


## EXAMPLES
> Example 1: Placing an octagon shape DRAW across the the screen using PSET.

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Explanation: Once a DRAW string variable is created, it can be used to draw a shape throughout the program at any time.

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Example 2: Creating an analog clock's hour markers using "TA=" + VARPTR$ (angle).

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Explanation: To place 12 circles in a circle each move is 30 degrees. PSET sets the center of the circular path every loop. TA moves counter-clockwise with positive degree angles. Once TA sets the angle a blind Up move is at that angle. The hour circles use the end point of the blind line as centers using the STEP relative coordinates of 0. After the circles are drawn, a draw "P" string paints the circle centers. DRAW paint strings use the last coordinate position also.

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Example 3: Creating a moving second hand for the clock above (SCREEN 12). (See TIME$ example 1)

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Explanation: The degrees to move from the original UP line move is calculated by dividing 360/60 seconds in a full rotation. That value of 6 is made negative to use TA correctly and multiplied by the VALue of seconds from the TIME$ function. The degree angle is converted by STR$ to a string and added to the DRAW string using the STRING concatenation + operator. Do not use semicolons to create DRAW strings. Once the second hand is placed on the screen, a loop waits for the second value to change. It then erases the hand and it repeats the process again.

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Example 4: Creating digital displays using DRAW format strings to create the LED segments. (See SELECT EVERYCASE example 5)

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

> Example 5: Using 32 bit or _RGB color string values when using the DRAW C text statement

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```


```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```

* [LINE](LINE.md) , [PSET](PSET.md) , [PRESET](PRESET.md) , [CIRCLE](CIRCLE.md)
* [PAINT](PAINT.md) , [SCREEN](SCREEN.md)
* [COLOR](COLOR.md) , [PLAY](PLAY.md)
* TIME$

```vb
SCREEN 12
octagon$ = "C12 R10 F10 D10 G10 L10 H10 U10 E10"  'create a DRAW string value
SCREEN 12
FOR i% = 1 TO 11
  PSET (i% * 50, 100), 15
  _DELAY .5         ' delay for demo
  DRAW octagon$     ' DRAW the octagon using variable
  _DELAY .5         ' delay for demo
NEXT i%
```



# SEE ALSO
* [LINE](LINE.md) , [PSET](PSET.md) , [PRESET](PRESET.md) , [CIRCLE](CIRCLE.md)
* [PAINT](PAINT.md) , [SCREEN](SCREEN.md)
* [COLOR](COLOR.md) , [PLAY](PLAY.md)
* TIME$

