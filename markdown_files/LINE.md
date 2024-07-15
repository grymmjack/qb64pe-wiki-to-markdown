# LINE
> The LINE statement is used in graphic SCREEN modes to create lines or boxes.

## SYNTAX
`LINE [STEP] [ ( column1 , row1 ) ] - [STEP] ( column2 , row2 ), color [, [{B|BF}], style% ]`

## PARAMETERS
* The [STEP](STEP.md) keyword make column and row coordinates relative to the previously coordinates set by any graphic statement.
* The optional parameters ( column1 , row1 ) set the line's starting point.
* The dash and second coordinate parameters ( column2 , row2 ) must be designated to complete the line or box.
* The [INTEGER](INTEGER.md) color attribute or [LONG](LONG.md) [_RGB32](_RGB32.md) 32 bit color value sets the drawing color.  If omitted, the current destination page's [_DEFAULTCOLOR](_DEFAULTCOLOR.md) is used.
* Optional B keyword creates a rectangle ( b ox) using the start and end coordinates as diagonal corners. BF creates a b ox f illed.
* The style% signed [INTEGER](INTEGER.md) value sets a dotted pattern to draw the line or rectangle outline.


## DESCRIPTION
* Creates a colored line between the given coordinates. Can be drawn partially off screen.
* B creates a box outline with each side parallel to the program screen sides. BF creates a filled box.
* style% can be used to create a dotted pattern to draw the line. B can be used with a style% to draw the rectangle outline using the desired pattern. BF ignores the style% parameter. See examples 2, 3 and 4 below.
	* B can be used with a style% to draw the rectangle outline using the desired pattern.
	* BF ignores the style% parameter. See examples 2, 3 and 4 below.
* B can be used with a style% to draw the rectangle outline using the desired pattern.
* BF ignores the style% parameter. See examples 2, 3 and 4 below.
* The graphic cursor is set to the center of the program window on program start. Using the [STEP](STEP.md) keyword makes the coordinates relative to the current graphic cursor.
* [LINE](LINE.md) can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only.


## EXAMPLES
> Example 1: Following one line with another by omitting the second line's first coordinate parameter bracket entirely:

```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```

> Example 2: Creating styled lines and boxes with the LINE statement. Different style values create different dashed line spacing.

```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```

> Example 3: The style value sets each 16 pixel line section as the value's bits are set on or off:

```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```

> Example 4: Using binary code to design a style pattern:

```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```


```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```

* [SCREEN](SCREEN.md) , [COLOR](COLOR.md)
* [DRAW](DRAW.md) , [CIRCLE](CIRCLE.md) , [STEP](STEP.md)
* [PSET](PSET.md) , [PRESET](PRESET.md)
* [AND](AND.md) , [OR](OR.md) (logical operators)

```vb
SCREEN 12

LINE (100, 100)-(200, 200), 10    'creates a line
LINE -(400, 200), 12              'creates a second line from end of first

END
```



# SEE ALSO
* [SCREEN](SCREEN.md) , [COLOR](COLOR.md)
* [DRAW](DRAW.md) , [CIRCLE](CIRCLE.md) , [STEP](STEP.md)
* [PSET](PSET.md) , [PRESET](PRESET.md)
* [AND](AND.md) , [OR](OR.md) (logical operators)

