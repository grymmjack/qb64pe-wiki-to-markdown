# PAINT
> The PAINT statement is used to fill a delimited area in a graphic screen mode with color.

## SYNTAX
`PAINT [ STEP ] ( column% , row% ), fillColor [, borderColor% ]`

## PARAMETERS
* Can use the [STEP](STEP.md) keyword for relative coordinate placements. See example 1 below.
* fillColor is an [INTEGER](INTEGER.md) or [LONG](LONG.md) 32-bit value to paint the inside of an object. Colors are limited to the [SCREEN](SCREEN.md) mode used.
* Optional [INTEGER](INTEGER.md) or [LONG](LONG.md) 32-bit borderColor% is the color of the border of the shape to be filled when this is different from the fill color.
* fillColor can be a string made up of a sequence of CHR$ values, each representing a tiling pattern to fill the shape. See Example 3 below.


## DESCRIPTION
* Graphic column% and row% [INTEGER](INTEGER.md) pixel coordinates should be inside of a fully closed "shape", whether it's a rectangle, circle or custom-drawn shape using [DRAW](DRAW.md) .
* If the coordinates passed to the [PAINT](PAINT.md) statement are on a pixel that matches the border colors, no filling will occur.
* If the shape's border isn't continuous, the "paint" will "leak".
* If the shape is not totally closed, every color except the border color may be painted over.
* [DRAW](DRAW.md) shapes can be filled using the string "P fillColor , borderColor ". Use a "B" blind move to offset from the shape's border.


## EXAMPLES
> Example 1: Painting a CIRCLE immediately after it is drawn using STEP (0, 0) to paint from the circle's center point.

```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```

> Example 2: Routine to check a DRAW string to make sure that the drawn shape is fully closed so that a PAINT does not "leak".

```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```

> Example 3: Tiling using PAINT to create a red brick pattern inside a yellow border:

```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```

> Example 4: Generating a tiling pattern for PAINT from DATA statements:

```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```


```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```

* [PSET](PSET.md) , [PRESET](PRESET.md)
* [CIRCLE](CIRCLE.md) , [LINE](LINE.md) , [DRAW](DRAW.md)
* [SCREEN](SCREEN.md) , CHR$

```vb
SCREEN 12
x = 200: y = 200
CIRCLE (x, y), 100, 10
PAINT STEP(0, 0), 2, 10
```



# SEE ALSO
* [PSET](PSET.md) , [PRESET](PRESET.md)
* [CIRCLE](CIRCLE.md) , [LINE](LINE.md) , [DRAW](DRAW.md)
* [SCREEN](SCREEN.md) , CHR$

