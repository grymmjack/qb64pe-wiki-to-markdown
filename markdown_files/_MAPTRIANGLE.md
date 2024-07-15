# _MAPTRIANGLE
> The _MAPTRIANGLE statement maps a triangular portion of an image onto a destination image or screen page.

## PARAMETERS
* The [_SEAMLESS](_SEAMLESS.md) option makes the triangle skip the right-most and bottom-most pixels of the triangle. When you make larger objects using several triangles, there can be a "seam" where they overlap when using alpha transparency and the seam would be twice as bright. [_SEAMLESS](_SEAMLESS.md) is ignored when rendering 3D content and is not yet supported when drawing 2D hardware images.
* For 3D drawing use the _CLOCKWISE and [_ANTICLOCKWISE](_ANTICLOCKWISE.md) arguments to only draw triangles in the correct direction. See Example 4 .
* Coordinates are [SINGLE](SINGLE.md) values where whole numbers represent the exact center of a pixel of the source texture.
* source& and optional destination& are [LONG](LONG.md) image or screen page handles.
* Supports an optional final argument [_SMOOTH](_SMOOTH.md) which applies linear filtering. See Example 3 .
* Use [_SMOOTHSTRETCHED](_SMOOTHSTRETCHED.md) or [_SMOOTHSHRUNK](_SMOOTHSHRUNK.md) for when a pixelated/smooth effect is desirable but not both.


## DESCRIPTION
* This statement is used similar to [_PUTIMAGE](_PUTIMAGE.md) to place triangular sections of an image, but is more flexible.
* The [STEP](STEP.md) keyword can be used to for coordinates relative to the last graphic coordinates used.
* For 2D drawing, the destination coordinates are pixel coordinates either on-screen or on the destination image.
* For 3D drawing, the destination coordinates represent left (-x) to right (+x), bottom (-y) to top (+y) & furthest (-z) to nearest (z=-1). The center of the screen is therefore (0,0,-1). Note that a z value of 0 will result in off-screen content. The furthest visible z value is -10,000.
* When drawing software images coordinate positions are limited from -16383 to 16383
* The source coordinates can be positioned outside the boundary of the source image to achieve a tiled effect.
* If the destination& image handle is the current [SCREEN](SCREEN.md) page, [_DEST](_DEST.md) or hardware layer, then it can be omitted.
* Hardware images (created using mode 33 via [_LOADIMAGE](_LOADIMAGE.md) or [_COPYIMAGE](_COPYIMAGE.md) ) can be used as the source or destination.


## EXAMPLES
> Example 1: Rotating the an image using a rotation and zoom SUB with _MAPTRIANGLE.

```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```

> Example 2: A 3D Spinning Cube demo using a software image and _MAPTRIANGLE :

```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```

> Example 3: A 3D Spinning Cube demo using a hardware image and QB64GL hardware acceleration with _MAPTRIANGLE :

```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```

> Example 4: Using a desktop image with _MAPTRIANGLE _ANTICLOCKWISE rendering.

```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```


```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```

* [_PUTIMAGE](_PUTIMAGE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md)
* [GET](GET.md) (graphics statement) , [PUT](PUT.md) (graphics statement)
* [STEP](STEP.md) , [SIN](SIN.md) , [COS](COS.md)
* Hardware images

```vb
SCREEN _NEWIMAGE(800, 600, 32)

Image& = _LOADIMAGE("qb64_trans.png")   'any 24/32 bit image

DO
 CLS
 RotoZoom 400, 300, Image&, 1.5 + SIN(zoom), angle
 LOCATE 1, 1: PRINT "Angle:"; CINT(angle)
 PRINT "Zoom"; USING "##.###"; 1.5 + SIN(zoom)
 _DISPLAY
 angle = angle + .5: IF angle >= 360 THEN angle = angle - 360
 zoom = zoom + .01
LOOP UNTIL INKEY$ <> ""
END

SUB RotoZoom (X AS LONG, Y AS LONG, Image AS LONG, Scale AS SINGLE, Rotation AS SINGLE)
DIM px(3) AS SINGLE: DIM py(3) AS SINGLE
W& = _WIDTH(Image&): H& = _HEIGHT(Image&)
px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2
px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2
sinr! = SIN(-Rotation / 57.2957795131): cosr! = COS(-Rotation / 57.2957795131)
FOR i& = 0 TO 3
 x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y
 px(i&) = x2&: py(i&) = y2&
NEXT
_MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
_MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
END SUB
```



# SEE ALSO
* [_PUTIMAGE](_PUTIMAGE.md)
* [_LOADIMAGE](_LOADIMAGE.md)
* [_COPYIMAGE](_COPYIMAGE.md)
* [GET](GET.md) (graphics statement) , [PUT](PUT.md) (graphics statement)
* [STEP](STEP.md) , [SIN](SIN.md) , [COS](COS.md)
* Hardware images

