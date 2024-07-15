# WINDOW
> The WINDOW command scales the graphics coordinate system of the current _DEST image, optionally inverting the direction of the vertical axis. Any coordinates used in drawing commands made to the image are scaled such that the image seems have have the dimensions requested.

## SYNTAX
`WINDOW [ [ SCREEN ] ( x1! , y1! ) - ( x2! , y2! )]`

## PARAMETERS


## DESCRIPTION


## EXAMPLES
> Demonstrate a circle's radius only matching the scaling in the horizontal direction by comparing against a box:

```vb
SCREEN _NEWIMAGE(600, 600, 32) '600 pixels in x and y directions and displayed on screen
WINDOW SCREEN (0, 0)-(6, 6)
```


```vb
SCREEN _NEWIMAGE(600, 600, 32) '600 pixels in x and y directions and displayed on screen
WINDOW SCREEN (0, 0)-(6, 6)
```

* [PMAP](PMAP.md)
* [VIEW](VIEW.md)
* [VIEW](VIEW.md) [PRINT](PRINT.md)

```vb
SCREEN _NEWIMAGE(600, 600, 32) '600 pixels in x and y directions and displayed on screen
WINDOW SCREEN (0, 0)-(6, 6)
```



# SEE ALSO
* [PMAP](PMAP.md)
* [VIEW](VIEW.md)
* [VIEW](VIEW.md) [PRINT](PRINT.md)

