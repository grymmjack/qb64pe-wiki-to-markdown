


\_MAPTRIANGLE - QB64 Phoenix Edition Wiki








# \_MAPTRIANGLE



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The \_MAPTRIANGLE statement maps a triangular portion of an image onto a destination image or screen page.


  






| Contents * [1 Syntax](#Syntax) 	+ [1.1 2D drawing](#2D_drawing) 	+ [1.2 3D drawing (hardware images only)](#3D_drawing_(hardware_images_only)) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 Examples](#Examples) * [5 See also](#See_also) |
| --- |


## Syntax


### 2D drawing


\_MAPTRIANGLE [{\_SEAMLESS}] **(***sx1***,** *sy1***)-(***sx2***,** *sy2***)-(***sx3***,** *sy3***),** *source&* **TO (***dx1***,** *dy1***)-(***dx2***,** *dy2***)-(***dx3***,** *dy3***)**[, *destination&*][,{\_SMOOTH|\_SMOOTHSHRUNK|\_SMOOTHSTRETCHED}
### 3D drawing (hardware images only)


\_MAPTRIANGLE [{\_CLOCKWISE|\_ANTICLOCKWISE}] [{\_SEAMLESS}] **(***sx1***,** *sy1***)-(***sx2***,** *sy2***)-(***sx3***,** *sy3***),** *source&* **TO (***dx1***,** *dy1***,** *dz1***)-(***dx2***,** *dy2***,** *dz2***)-(***dx3***,** *dy3***,** *dz3***)**[, *destination&*][,{\_SMOOTH|\_SMOOTHSHRUNK|\_SMOOTHSTRETCHED}
  




## Parameters


* The **\_SEAMLESS** option makes the triangle skip the right-most and bottom-most pixels of the triangle. When you make larger objects using several triangles, there can be a "seam" where they overlap when using alpha transparency and the seam would be twice as bright. **\_SEAMLESS** is ignored when rendering 3D content and is not yet supported when drawing 2D hardware images.
* For 3D drawing use the **\_CLOCKWISE** and **\_ANTICLOCKWISE** arguments to only draw triangles in the correct direction. See *Example 4*.
* Coordinates are [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") values where whole numbers represent the exact center of a pixel of the source texture.
* *source&* and optional *destination&* are [LONG](/qb64wiki/index.php/LONG "LONG") image or screen page handles.
* Supports an optional final argument **\_SMOOTH** which applies linear filtering. See *Example 3*.
* Use **\_SMOOTHSTRETCHED** or **\_SMOOTHSHRUNK** for when a pixelated/smooth effect is desirable but not both.


  




## Description


* This statement is used similar to [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") to place triangular sections of an image, but is more flexible.
* The [STEP](/qb64wiki/index.php/STEP "STEP") keyword can be used to for coordinates relative to the last graphic coordinates used.
* For 2D drawing, the destination coordinates are pixel coordinates either on-screen or on the destination image.
* For 3D drawing, the destination coordinates represent left (-x) to right (+x), bottom (-y) to top (+y) & furthest (-z) to nearest (z=-1). The center of the screen is therefore (0,0,-1). Note that a z value of 0 will result in off-screen content. The furthest visible z value is -10,000.
* When drawing **software images** coordinate positions are **limited from -16383 to 16383**
* The source coordinates can be positioned outside the boundary of the *source* image to achieve a tiled effect.
* If the *destination&* image handle is the current [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") page, [\_DEST](/qb64wiki/index.php/DEST "DEST") or hardware layer, then it can be omitted.
* **Hardware images** (created using mode 33 via [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") or [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")) can be used as the source or destination.


  




## Examples


*Example 1:* Rotating the an image using a rotation and zoom SUB with \_MAPTRIANGLE.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  Image& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png")   'any 24/32 bit image  [DO](/qb64wiki/index.php/DO "DO")   [CLS](/qb64wiki/index.php/CLS "CLS")   RotoZoom 400, 300, Image&, 1.5 + [SIN](/qb64wiki/index.php/SIN "SIN")(zoom), angle   [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "Angle:"; [CINT](/qb64wiki/index.php/CINT "CINT")(angle)   [PRINT](/qb64wiki/index.php/PRINT_USING "PRINT USING") "Zoom"; [USING](/qb64wiki/index.php/PRINT_USING "PRINT USING") "##.###"; 1.5 + [SIN](/qb64wiki/index.php/SIN "SIN")(zoom)   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY")   angle = angle + .5: [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") angle >= 360 [THEN](/qb64wiki/index.php/THEN "THEN") angle = angle - 360   zoom = zoom + .01 [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [END](/qb64wiki/index.php/END "END")  [SUB](/qb64wiki/index.php/SUB "SUB") RotoZoom (X [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Y [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Image [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG"), Scale [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"), Rotation [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")) [DIM](/qb64wiki/index.php/DIM "DIM") px(3) [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE"): [DIM](/qb64wiki/index.php/DIM "DIM") py(3) [AS](/qb64wiki/index.php/AS "AS") [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE") W& = [_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(Image&): H& = [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(Image&) px(0) = -W& / 2: py(0) = -H& / 2: px(1) = -W& / 2:py(1) = H& / 2 px(2) = W& / 2: py(2) = H& / 2: px(3) = W& / 2: py(3) = -H& / 2 sinr! = [SIN](/qb64wiki/index.php/SIN "SIN")(-Rotation / 57.2957795131): cosr! = [COS](/qb64wiki/index.php/COS "COS")(-Rotation / 57.2957795131) [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") i& = 0 [TO](/qb64wiki/index.php/TO "TO") 3   x2& = (px(i&) * cosr! + sinr! * py(i&)) * Scale + X: y2& = (py(i&) * cosr! - px(i&) * sinr!) * Scale + Y   px(i&) = x2&: py(i&) = y2& [NEXT](/qb64wiki/index.php/NEXT "NEXT") _MAPTRIANGLE (0, 0)-(0, H& - 1)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2)) _MAPTRIANGLE (0, 0)-(W& - 1, 0)-(W& - 1, H& - 1), Image& TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2)) [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Code by Galleon


| ```         **Triangle sections of image in code above     __**                                                      **|\2|**                                                   **1→|_\|**  ``` |
| --- |


  

*Example 2:* A 3D Spinning Cube demo using a software image and \_MAPTRIANGLE:





| ``` ' Copyright (C) 2011 by Andrew L. Ayers  [DIM](/qb64wiki/index.php/DIM "DIM") OBJECT(9, 9, 4, 2) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  ' OBJECTS DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#OBJECTS,#PLANES PER OBJECT,#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XYZ TRIPLE)  [DIM](/qb64wiki/index.php/DIM "DIM") DPLANE2D(4, 1) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") ' [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") PLANE COORDINATES  ' DPLANE2D DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XY [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"))  [DIM](/qb64wiki/index.php/DIM "DIM") DPLANE3D(4, 2) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") ' 3D PLANE COORDINATES  ' DPLANE3D DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XYZ TRIPLE)  [DIM](/qb64wiki/index.php/DIM "DIM") PLANECOL(9) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") STAB(359), CTAB(359) ' SINE/COSINE TABLES D& = 400: MX& = 0: MY& = 0: MZ& = -100 ' ' COMPUTE SINE/COSINE TABLES [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t& = 0 [TO](/qb64wiki/index.php/TO "TO") 359   STAB(t&) = [SIN](/qb64wiki/index.php/SIN "SIN")((6.282 / 360) * t&)   CTAB(t&) = [COS](/qb64wiki/index.php/COS "COS")((6.282 / 360) * t&) [NEXT](/qb64wiki/index.php/NEXT "NEXT") ' ' BUILD CUBE IN OBJECT ARRAY ' PLANE 0 OBJECT(0, 0, 0, 0) = -30: OBJECT(0, 0, 0, 1) = 30: OBJECT(0, 0, 0, 2) = -30 OBJECT(0, 0, 1, 0) = -30: OBJECT(0, 0, 1, 1) = -30: OBJECT(0, 0, 1, 2) = -30 OBJECT(0, 0, 2, 0) = 30: OBJECT(0, 0, 2, 1) = -30: OBJECT(0, 0, 2, 2) = -30 OBJECT(0, 0, 3, 0) = 30: OBJECT(0, 0, 3, 1) = 30: OBJECT(0, 0, 3, 2) = -30 OBJECT(0, 0, 4, 0) = 0: OBJECT(0, 0, 4, 1) = 0: OBJECT(0, 0, 4, 2) = -30 ' PLANE 1 OBJECT(0, 1, 0, 0) = 30: OBJECT(0, 1, 0, 1) = 30: OBJECT(0, 1, 0, 2) = -30 OBJECT(0, 1, 1, 0) = 30: OBJECT(0, 1, 1, 1) = -30: OBJECT(0, 1, 1, 2) = -30 OBJECT(0, 1, 2, 0) = 30: OBJECT(0, 1, 2, 1) = -30: OBJECT(0, 1, 2, 2) = 30 OBJECT(0, 1, 3, 0) = 30: OBJECT(0, 1, 3, 1) = 30: OBJECT(0, 1, 3, 2) = 30 OBJECT(0, 1, 4, 0) = 30: OBJECT(0, 1, 4, 1) = 0: OBJECT(0, 1, 4, 2) = 0 ' PLANE 2 OBJECT(0, 2, 0, 0) = 30: OBJECT(0, 2, 0, 1) = 30: OBJECT(0, 2, 0, 2) = 30 OBJECT(0, 2, 1, 0) = 30: OBJECT(0, 2, 1, 1) = -30: OBJECT(0, 2, 1, 2) = 30 OBJECT(0, 2, 2, 0) = -30: OBJECT(0, 2, 2, 1) = -30: OBJECT(0, 2, 2, 2) = 30 OBJECT(0, 2, 3, 0) = -30: OBJECT(0, 2, 3, 1) = 30: OBJECT(0, 2, 3, 2) = 30 OBJECT(0, 2, 4, 0) = 0: OBJECT(0, 2, 4, 1) = 0: OBJECT(0, 2, 4, 2) = 30 ' PLANE 3 OBJECT(0, 3, 0, 0) = -30: OBJECT(0, 3, 0, 1) = 30: OBJECT(0, 3, 0, 2) = 30 OBJECT(0, 3, 1, 0) = -30: OBJECT(0, 3, 1, 1) = -30: OBJECT(0, 3, 1, 2) = 30 OBJECT(0, 3, 2, 0) = -30: OBJECT(0, 3, 2, 1) = -30: OBJECT(0, 3, 2, 2) = -30 OBJECT(0, 3, 3, 0) = -30: OBJECT(0, 3, 3, 1) = 30: OBJECT(0, 3, 3, 2) = -30 OBJECT(0, 3, 4, 0) = -30: OBJECT(0, 3, 4, 1) = 0: OBJECT(0, 3, 4, 2) = 0 ' PLANE 4 OBJECT(0, 4, 0, 0) = -30: OBJECT(0, 4, 0, 1) = -30: OBJECT(0, 4, 0, 2) = -30 OBJECT(0, 4, 1, 0) = -30: OBJECT(0, 4, 1, 1) = -30: OBJECT(0, 4, 1, 2) = 30 OBJECT(0, 4, 2, 0) = 30: OBJECT(0, 4, 2, 1) = -30: OBJECT(0, 4, 2, 2) = 30 OBJECT(0, 4, 3, 0) = 30: OBJECT(0, 4, 3, 1) = -30: OBJECT(0, 4, 3, 2) = -30 OBJECT(0, 4, 4, 0) = 0: OBJECT(0, 4, 4, 1) = -30: OBJECT(0, 4, 4, 2) = 0 ' PLANE 5 OBJECT(0, 5, 0, 0) = -30: OBJECT(0, 5, 0, 1) = 30: OBJECT(0, 5, 0, 2) = -30 OBJECT(0, 5, 1, 0) = 30: OBJECT(0, 5, 1, 1) = 30: OBJECT(0, 5, 1, 2) = -30 OBJECT(0, 5, 2, 0) = 30: OBJECT(0, 5, 2, 1) = 30: OBJECT(0, 5, 2, 2) = 30 OBJECT(0, 5, 3, 0) = -30: OBJECT(0, 5, 3, 1) = 30: OBJECT(0, 5, 3, 2) = 30 OBJECT(0, 5, 4, 0) = 0: OBJECT(0, 5, 4, 1) = 30: OBJECT(0, 5, 4, 2) = 0 ' SET UP PLANE [COLOR](/qb64wiki/index.php/COLOR "COLOR")S ON CUBE ' PLANECOL(0) = 3 PLANECOL(1) = 4 PLANECOL(2) = 5 PLANECOL(3) = 6 PLANECOL(4) = 7 PLANECOL(5) = 8 ' [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "QB64 _MAPTRIANGLE CUBE DEMO" [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32) TextureImage& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png") 'any 24/32 bit image '[_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Image&  DO   ' LIMIT [TO](/qb64wiki/index.php/TO "TO") 25 FPS   [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 25   ' ERASE LAST IMAGE   [CLS](/qb64wiki/index.php/CLS "CLS")    ' CALCULATE POSITION OF NEW IMAGE   [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") OB& = 0 [TO](/qb64wiki/index.php/TO "TO") 0 ' UP [TO](/qb64wiki/index.php/TO "TO") 9 OBJECTS     SP = STAB(PIT(OB&)): CP = CTAB(PIT(OB&))     SY = STAB(YAW(OB&)): CY = CTAB(YAW(OB&))     SR = STAB(ROL(OB&)): CR = CTAB(ROL(OB&))     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") PL& = 0 [TO](/qb64wiki/index.php/TO "TO") 5 ' CONSISTING OF UP [TO](/qb64wiki/index.php/TO "TO") 9 PLANES       '       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") PN& = 0 [TO](/qb64wiki/index.php/TO "TO") 3 ' EACH PLANE WITH UP [TO](/qb64wiki/index.php/TO "TO") 4 [POINT](/qb64wiki/index.php/POINT "POINT")S (#5 [TO](/qb64wiki/index.php/TO "TO") [PAINT](/qb64wiki/index.php/PAINT "PAINT"))         '         ' TRANSLATE, [THEN](/qb64wiki/index.php/THEN "THEN") ROTATE         TX& = OBJECT(OB&, PL&, PN&, 0)         TY& = OBJECT(OB&, PL&, PN&, 1)         TZ& = OBJECT(OB&, PL&, PN&, 2)         RX& = (TZ& * CP - TY& * SP) * SY - ((TZ& * SP + TY& * CP) * SR + TX& * CR) * CY         RY& = (TZ& * SP + TY& * CP) * CR - TX& * SR         RZ& = (TZ& * CP - TY& * SP) * CY + ((TZ& * SP + TY& * CP) * SR + TX& * CR) * SY         '         ' ROTATE, [THEN](/qb64wiki/index.php/THEN "THEN") TRANSLATE         RX& = RX& + MX&         RY& = RY& + MY&         RZ& = RZ& + MZ&         '         DPLANE3D(PN&, 0) = RX&: DPLANE3D(PN&, 1) = RY&: DPLANE3D(PN&, 2) = RZ&         DPLANE2D(PN&, 0) = 399 + (D& * RX& / RZ&)         DPLANE2D(PN&, 1) = 299 + (D& * RY& / RZ&)       [NEXT](/qb64wiki/index.php/NEXT "NEXT")       '       ' CHECK [TO](/qb64wiki/index.php/TO "TO") SEE [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") PLANE IS VISIBLE       x1& = DPLANE3D(0, 0): y1& = DPLANE3D(0, 1): Z1& = DPLANE3D(0, 2)       x2& = DPLANE3D(1, 0): y2& = DPLANE3D(1, 1): Z2& = DPLANE3D(1, 2)       x3& = DPLANE3D(2, 0): y3& = DPLANE3D(2, 1): Z3& = DPLANE3D(2, 2)       T1& = -x1& * (y2& * Z3& - y3& * Z2&)       T2& = x2& * (y3& * Z1& - y1& * Z3&)       T3& = x3& * (y1& * Z2& - y2& * Z1&)       '       VISIBLE& = T1& - T2& - T3&       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") VISIBLE& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")         ' DRAW PLANE         xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)         xx2% = DPLANE2D(1, 0): yy2% = DPLANE2D(1, 1)         xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)         col% = PLANECOL(PL&)          _MAPTRIANGLE (0, 0)-(0, 255)-(255, 255), TextureImage& TO(xx3%, yy3%)-(xx2%, yy2%)-(xx1%, yy1%)         ' CALL DrawTriangle(xx1%, yy1%, xx2%, yy2%, xx3%, yy3%, col%)         xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)         xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)         xx4% = DPLANE2D(3, 0): yy4% = DPLANE2D(3, 1)         _MAPTRIANGLE (0, 0)-(255, 255)-(255, 0), TextureImage& TO(xx3%, yy3%)-(xx1%, yy1%)-(xx4%, yy4%)         'CALL DrawTriangle(xx1%, yy1%, xx3%, yy3%, xx4%, yy4%, col%)       [END IF](/qb64wiki/index.php/END_IF "END IF")     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     '     ' ROTATE OBJECT     PIT(OB&) = PIT(OB&) + 5     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") PIT(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") PIT(OB&) = 0     YAW(OB&) = YAW(OB&) + 7     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") YAW(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") YAW(OB&) = 0     ROL(OB&) = ROL(OB&) + 9     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ROL(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") ROL(OB&) = 0   [NEXT](/qb64wiki/index.php/NEXT "NEXT")   '   ' Calculate Frames per Second   frames% = frames% + 1   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") oldtime$ <> [TIME$](/qb64wiki/index.php/TIME$ "TIME$") [THEN](/qb64wiki/index.php/THEN "THEN")     fps% = frames%     frames% = 1     oldtime$ = [TIME$](/qb64wiki/index.php/TIME$ "TIME$")   [END IF](/qb64wiki/index.php/END_IF "END IF")   [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255): [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "FPS :"; fps%   '   ' Show Image on Screen   [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 80: [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0: [CLS](/qb64wiki/index.php/CLS "CLS")   [SUB](/qb64wiki/index.php/SUB "SUB") DrawHline (fromx%, tox%, yy%, col%)   '[DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [&H](/qb64wiki/index.php/%26H "&H")A000   '[IF](/qb64wiki/index.php/IF...THEN "IF...THEN") fromx% > tox% [THEN](/qb64wiki/index.php/THEN "THEN") [SWAP](/qb64wiki/index.php/SWAP "SWAP") fromx%, tox%   'yyy& = yy%   'sloc& = yyy& * 320 + fromx%   'eloc& = sloc& + (tox% - fromx%)   '[FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t& = sloc& [TO](/qb64wiki/index.php/TO "TO") eloc&   '  [POKE](/qb64wiki/index.php/POKE "POKE") t&, col%   '[NEXT](/qb64wiki/index.php/NEXT "NEXT")   '[DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG")   [LINE](/qb64wiki/index.php/LINE "LINE") (fromx%, yy%)-(tox%, yy%), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) 'col% [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") DrawTriangle (x1%, y1%, x2%, y2%, x3%, y3%, col%)   DO     sflag% = 0     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y1% > y2% [THEN](/qb64wiki/index.php/THEN "THEN")       sflag% = 1       [SWAP](/qb64wiki/index.php/SWAP "SWAP") y1%, y2%       [SWAP](/qb64wiki/index.php/SWAP "SWAP") x1%, x2%     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2% > y3% [THEN](/qb64wiki/index.php/THEN "THEN")       sflag% = 1       [SWAP](/qb64wiki/index.php/SWAP "SWAP") y2%, y3%       [SWAP](/qb64wiki/index.php/SWAP "SWAP") x2%, x3%     [END IF](/qb64wiki/index.php/END_IF "END IF")   [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") sflag% = 0   '   [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2% = y3% [THEN](/qb64wiki/index.php/THEN "THEN")     ' Draw a flat bottomed triangle     ydiff1% = y2% - y1%     ydiff2% = y3% - y1%     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")       slope1! = (x2% - x1%) / ydiff1%     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       slope1! = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")       slope2! = (x3% - x1%) / ydiff2%     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       slope2! = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     sx! = x1%: ex! = x1%     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y2%       [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)       sx! = sx! + slope1!       ex! = ex! + slope2!     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB")   [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y1% = y2% [THEN](/qb64wiki/index.php/THEN "THEN")       '       ' Draw a flat topped triangle       ydiff1% = y3% - y1%       ydiff2% = y3% - y2%       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope1! = (x3% - x1%) / ydiff1%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope1! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope2! = (x3% - x2%) / ydiff2%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope2! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       sx! = x1%: ex! = x2%       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y3%         [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)         sx! = sx! + slope1!         ex! = ex! + slope2!       [NEXT](/qb64wiki/index.php/NEXT "NEXT")       x1% = sx!: x2% = ex!       [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB")     [ELSE](/qb64wiki/index.php/ELSE "ELSE")       ' Draw a general purpose triangle       ' First draw the flat bottom portion (top half)       ydiff1% = y2% - y1%       ydiff2% = y3% - y1%       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope1! = (x2% - x1%) / ydiff1%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope1! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope2! = (x3% - x1%) / ydiff2%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope2! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       sx! = x1%: ex! = x1%       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y2%         [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)         sx! = sx! + slope1!         ex! = ex! + slope2!       [NEXT](/qb64wiki/index.php/NEXT "NEXT")       ' Then draw the flat topped portion (bottom half)       x1% = x2%       x2% = ex!       y1% = y2%       ydiff1% = y3% - y1%       ydiff2% = y3% - y2%       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope1! = (x3% - x1%) / ydiff1%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope1! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope2! = (x3% - x2%) / ydiff2%       [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope2! = 0       [END IF](/qb64wiki/index.php/END_IF "END IF")       sx! = x1%: ex! = x2%       [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y3%         [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)         sx! = sx! + slope1!         ex! = ex! + slope2!       [NEXT](/qb64wiki/index.php/NEXT "NEXT")       x1% = sx!: x2% = ex!     [END IF](/qb64wiki/index.php/END_IF "END IF")   [END IF](/qb64wiki/index.php/END_IF "END IF")   ' [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Demo by Andrew L. Ayers
  

*Example 3:* A 3D Spinning Cube demo using a hardware image and **QB64GL** hardware acceleration with \_MAPTRIANGLE:





| ``` ' Copyright (C) 2011 by Andrew L. Ayers  [DIM](/qb64wiki/index.php/DIM "DIM") OBJECT(9, 9, 4, 2) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG")  ' OBJECTS DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#OBJECTS,#PLANES PER OBJECT,#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XYZ TRIPLE)  [DIM](/qb64wiki/index.php/DIM "DIM") DPLANE2D(4, 1) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") ' [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") PLANE COORDINATES  ' DPLANE2D DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XY [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE"))  [DIM](/qb64wiki/index.php/DIM "DIM") DPLANE3D(4, 2) [AS](/qb64wiki/index.php/AS "AS") [LONG](/qb64wiki/index.php/LONG "LONG") ' 3D PLANE COORDINATES  ' DPLANE3D DEFINED [AS](/qb64wiki/index.php/AS "AS") FOLLOWS: '   (#[POINT](/qb64wiki/index.php/POINT "POINT")S PER PLANE, XYZ TRIPLE)  [DIM](/qb64wiki/index.php/DIM "DIM") PLANECOL(9) [AS](/qb64wiki/index.php/AS "AS") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER") [DIM](/qb64wiki/index.php/DIM "DIM") STAB(359), CTAB(359) ' SINE/COSINE TABLES D& = 400: MX& = 0: MY& = 0: MZ& = -100 ' ' COMPUTE SINE/COSINE TABLES [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t& = 0 [TO](/qb64wiki/index.php/TO "TO") 359     STAB(t&) = [SIN](/qb64wiki/index.php/SIN "SIN")((6.282 / 360) * t&)     CTAB(t&) = [COS](/qb64wiki/index.php/COS "COS")((6.282 / 360) * t&) [NEXT](/qb64wiki/index.php/NEXT "NEXT") ' ' BUILD CUBE IN OBJECT ARRAY ' PLANE 0 OBJECT(0, 0, 0, 0) = -30: OBJECT(0, 0, 0, 1) = 30: OBJECT(0, 0, 0, 2) = -30 OBJECT(0, 0, 1, 0) = -30: OBJECT(0, 0, 1, 1) = -30: OBJECT(0, 0, 1, 2) = -30 OBJECT(0, 0, 2, 0) = 30: OBJECT(0, 0, 2, 1) = -30: OBJECT(0, 0, 2, 2) = -30 OBJECT(0, 0, 3, 0) = 30: OBJECT(0, 0, 3, 1) = 30: OBJECT(0, 0, 3, 2) = -30 OBJECT(0, 0, 4, 0) = 0: OBJECT(0, 0, 4, 1) = 0: OBJECT(0, 0, 4, 2) = -30 ' PLANE 1 OBJECT(0, 1, 0, 0) = 30: OBJECT(0, 1, 0, 1) = 30: OBJECT(0, 1, 0, 2) = -30 OBJECT(0, 1, 1, 0) = 30: OBJECT(0, 1, 1, 1) = -30: OBJECT(0, 1, 1, 2) = -30 OBJECT(0, 1, 2, 0) = 30: OBJECT(0, 1, 2, 1) = -30: OBJECT(0, 1, 2, 2) = 30 OBJECT(0, 1, 3, 0) = 30: OBJECT(0, 1, 3, 1) = 30: OBJECT(0, 1, 3, 2) = 30 OBJECT(0, 1, 4, 0) = 30: OBJECT(0, 1, 4, 1) = 0: OBJECT(0, 1, 4, 2) = 0 ' PLANE 2 OBJECT(0, 2, 0, 0) = 30: OBJECT(0, 2, 0, 1) = 30: OBJECT(0, 2, 0, 2) = 30 OBJECT(0, 2, 1, 0) = 30: OBJECT(0, 2, 1, 1) = -30: OBJECT(0, 2, 1, 2) = 30 OBJECT(0, 2, 2, 0) = -30: OBJECT(0, 2, 2, 1) = -30: OBJECT(0, 2, 2, 2) = 30 OBJECT(0, 2, 3, 0) = -30: OBJECT(0, 2, 3, 1) = 30: OBJECT(0, 2, 3, 2) = 30 OBJECT(0, 2, 4, 0) = 0: OBJECT(0, 2, 4, 1) = 0: OBJECT(0, 2, 4, 2) = 30 ' PLANE 3 OBJECT(0, 3, 0, 0) = -30: OBJECT(0, 3, 0, 1) = 30: OBJECT(0, 3, 0, 2) = 30 OBJECT(0, 3, 1, 0) = -30: OBJECT(0, 3, 1, 1) = -30: OBJECT(0, 3, 1, 2) = 30 OBJECT(0, 3, 2, 0) = -30: OBJECT(0, 3, 2, 1) = -30: OBJECT(0, 3, 2, 2) = -30 OBJECT(0, 3, 3, 0) = -30: OBJECT(0, 3, 3, 1) = 30: OBJECT(0, 3, 3, 2) = -30 OBJECT(0, 3, 4, 0) = -30: OBJECT(0, 3, 4, 1) = 0: OBJECT(0, 3, 4, 2) = 0 ' PLANE 4 OBJECT(0, 4, 0, 0) = -30: OBJECT(0, 4, 0, 1) = -30: OBJECT(0, 4, 0, 2) = -30 OBJECT(0, 4, 1, 0) = -30: OBJECT(0, 4, 1, 1) = -30: OBJECT(0, 4, 1, 2) = 30 OBJECT(0, 4, 2, 0) = 30: OBJECT(0, 4, 2, 1) = -30: OBJECT(0, 4, 2, 2) = 30 OBJECT(0, 4, 3, 0) = 30: OBJECT(0, 4, 3, 1) = -30: OBJECT(0, 4, 3, 2) = -30 OBJECT(0, 4, 4, 0) = 0: OBJECT(0, 4, 4, 1) = -30: OBJECT(0, 4, 4, 2) = 0 ' PLANE 5 OBJECT(0, 5, 0, 0) = -30: OBJECT(0, 5, 0, 1) = 30: OBJECT(0, 5, 0, 2) = -30 OBJECT(0, 5, 1, 0) = 30: OBJECT(0, 5, 1, 1) = 30: OBJECT(0, 5, 1, 2) = -30 OBJECT(0, 5, 2, 0) = 30: OBJECT(0, 5, 2, 1) = 30: OBJECT(0, 5, 2, 2) = 30 OBJECT(0, 5, 3, 0) = -30: OBJECT(0, 5, 3, 1) = 30: OBJECT(0, 5, 3, 2) = 30 OBJECT(0, 5, 4, 0) = 0: OBJECT(0, 5, 4, 1) = 30: OBJECT(0, 5, 4, 2) = 0 ' SET UP PLANE [COLOR](/qb64wiki/index.php/COLOR "COLOR")S ON CUBE ' PLANECOL(0) = 3 PLANECOL(1) = 4 PLANECOL(2) = 5 PLANECOL(3) = 6 PLANECOL(4) = 7 PLANECOL(5) = 8 ' [_TITLE](/qb64wiki/index.php/TITLE "TITLE") "QB64 _MAPTRIANGLE CUBE DEMO" [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  TextureImage& = [_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")("qb64_trans.png", 32) 'any 24/32 bit image [_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") 128, , TextureImage& TextureImage& = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(TextureImage&, 33)'copy of hardware image  '[_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE") , Image&  DO      ' LIMIT [TO](/qb64wiki/index.php/TO "TO") 25 FPS     '[_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 25     ' [ERASE](/qb64wiki/index.php/ERASE "ERASE") LAST IMAGE     '[CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 0, 160)      ' CALCULATE POSITION OF NEW IMAGE     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") OB& = 0 [TO](/qb64wiki/index.php/TO "TO") 0 ' UP [TO](/qb64wiki/index.php/TO "TO") 9 OBJECTS         SP = STAB(PIT(OB&)): CP = CTAB(PIT(OB&))         SY = STAB(YAW(OB&)): CY = CTAB(YAW(OB&))         SR = STAB(ROL(OB&)): CR = CTAB(ROL(OB&))         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") PL& = 0 [TO](/qb64wiki/index.php/TO "TO") 5 ' CONSISTING OF UP [TO](/qb64wiki/index.php/TO "TO") 9 PLANES             '             [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") PN& = 0 [TO](/qb64wiki/index.php/TO "TO") 3 ' EACH PLANE WITH UP [TO](/qb64wiki/index.php/TO "TO") 4 [POINT](/qb64wiki/index.php/POINT "POINT")S (#5 [TO](/qb64wiki/index.php/TO "TO") [PAINT](/qb64wiki/index.php/PAINT "PAINT"))                 '                 ' TRANSLATE, [THEN](/qb64wiki/index.php/THEN "THEN") ROTATE                 TX& = OBJECT(OB&, PL&, PN&, 0)                 TY& = OBJECT(OB&, PL&, PN&, 1)                 TZ& = OBJECT(OB&, PL&, PN&, 2)                 RX& = (TZ& * CP - TY& * SP) * SY - ((TZ& * SP + TY& * CP) * SR + TX& * CR) * CY                 RY& = (TZ& * SP + TY& * CP) * CR - TX& * SR                 RZ& = (TZ& * CP - TY& * SP) * CY + ((TZ& * SP + TY& * CP) * SR + TX& * CR) * SY                 '                 ' ROTATE, [THEN](/qb64wiki/index.php/THEN "THEN") TRANSLATE                 RX& = RX& + MX&                 RY& = RY& + MY&                 RZ& = RZ& + MZ&                 '                 DPLANE3D(PN&, 0) = RX&: DPLANE3D(PN&, 1) = RY&: DPLANE3D(PN&, 2) = RZ&                 DPLANE2D(PN&, 0) = 399 + (D& * RX& / RZ&)                 DPLANE2D(PN&, 1) = 299 + (D& * RY& / RZ&)             [NEXT](/qb64wiki/index.php/NEXT "NEXT")             '             ' CHECK [TO](/qb64wiki/index.php/TO "TO") SEE [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") PLANE [IS](/qb64wiki/index.php/IS "IS") VISIBLE             x1& = DPLANE3D(0, 0): y1& = DPLANE3D(0, 1): Z1& = DPLANE3D(0, 2)             x2& = DPLANE3D(1, 0): y2& = DPLANE3D(1, 1): Z2& = DPLANE3D(1, 2)             x3& = DPLANE3D(2, 0): y3& = DPLANE3D(2, 1): Z3& = DPLANE3D(2, 2)             T1& = -x1& * (y2& * Z3& - y3& * Z2&)             T2& = x2& * (y3& * Z1& - y1& * Z3&)             T3& = x3& * (y1& * Z2& - y2& * Z1&)             '             VISIBLE& = T1& - T2& - T3&             [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") VISIBLE& > 0 [THEN](/qb64wiki/index.php/THEN "THEN")                 ' [DRAW](/qb64wiki/index.php/DRAW "DRAW") PLANE                 xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)                 xx2% = DPLANE2D(1, 0): yy2% = DPLANE2D(1, 1)                 xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)                 col% = PLANECOL(PL&)                  [_BLEND](/qb64wiki/index.php/BLEND "BLEND") TextureImage&                 _MAPTRIANGLE (0, 0)-(0, 255)-(255, 255), TextureImage& TO(xx1%, yy1%)-(xx2%, yy2%)-(xx3%, yy3%)                  ' [CALL](/qb64wiki/index.php/CALL "CALL") DrawTriangle(xx1%, yy1%, xx2%, yy2%, xx3%, yy3%, col%)                 xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)                 xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)                 xx4% = DPLANE2D(3, 0): yy4% = DPLANE2D(3, 1)                  [_DONTBLEND](/qb64wiki/index.php/DONTBLEND "DONTBLEND") TextureImage&                 _MAPTRIANGLE (0, 0)-(255, 255)-(255, 0), TextureImage& TO(xx3%, yy3%)-(xx1%, yy1%)-(xx4%, yy4%), , _SMOOTH                 '[CALL](/qb64wiki/index.php/CALL "CALL") DrawTriangle(xx1%, yy1%, xx3%, yy3%, xx4%, yy4%, col%)             [END IF](/qb64wiki/index.php/END_IF "END IF")         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         '         ' ROTATE OBJECT         PIT(OB&) = PIT(OB&) + 5         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") PIT(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") PIT(OB&) = 0         YAW(OB&) = YAW(OB&) + 7         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") YAW(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") YAW(OB&) = 0         ROL(OB&) = ROL(OB&) + 9         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ROL(OB&) > 359 [THEN](/qb64wiki/index.php/THEN "THEN") ROL(OB&) = 0     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     '     ' Calculate Frames per Second     frames% = frames% + 1     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") oldtime$ <> [TIME$](/qb64wiki/index.php/TIME$ "TIME$") [THEN](/qb64wiki/index.php/THEN "THEN")         fps% = frames%         frames% = 1         oldtime$ = [TIME$](/qb64wiki/index.php/TIME$ "TIME$")     [END IF](/qb64wiki/index.php/END_IF "END IF")     [COLOR](/qb64wiki/index.php/COLOR "COLOR") [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255): [LOCATE](/qb64wiki/index.php/LOCATE "LOCATE") 1, 1: [PRINT](/qb64wiki/index.php/PRINT "PRINT") "FPS :"; fps%     '     ' Show Image on Screen     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") [INKEY$](/qb64wiki/index.php/INKEY$ "INKEY$") <> "" [WIDTH](/qb64wiki/index.php/WIDTH "WIDTH") 80: [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") 0: [CLS](/qb64wiki/index.php/CLS "CLS")  [SUB](/qb64wiki/index.php/SUB "SUB") DrawHline (fromx%, tox%, yy%, col%) '[DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") = [&H](/qb64wiki/index.php/%26H "&H")A000 '[IF](/qb64wiki/index.php/IF...THEN "IF...THEN") fromx% > tox% [THEN](/qb64wiki/index.php/THEN "THEN") [SWAP](/qb64wiki/index.php/SWAP "SWAP") fromx%, tox% 'yyy& = yy% 'sloc& = yyy& * 320 + fromx% 'eloc& = sloc& + (tox% - fromx%) '[FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") t& = sloc& [TO](/qb64wiki/index.php/TO "TO") eloc& '  [POKE](/qb64wiki/index.php/POKE "POKE") t&, col% '[NEXT](/qb64wiki/index.php/NEXT "NEXT") '[DEF SEG](/qb64wiki/index.php/DEF_SEG "DEF SEG") [LINE](/qb64wiki/index.php/LINE "LINE") (fromx%, yy%)-(tox%, yy%), [_RGB](/qb64wiki/index.php/RGB "RGB")(255, 255, 255) 'col% [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  [SUB](/qb64wiki/index.php/SUB "SUB") DrawTriangle (x1%, y1%, x2%, y2%, x3%, y3%, col%) DO     sflag% = 0     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y1% > y2% [THEN](/qb64wiki/index.php/THEN "THEN")         sflag% = 1         [SWAP](/qb64wiki/index.php/SWAP "SWAP") y1%, y2%         [SWAP](/qb64wiki/index.php/SWAP "SWAP") x1%, x2%     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2% > y3% [THEN](/qb64wiki/index.php/THEN "THEN")         sflag% = 1         [SWAP](/qb64wiki/index.php/SWAP "SWAP") y2%, y3%         [SWAP](/qb64wiki/index.php/SWAP "SWAP") x2%, x3%     [END IF](/qb64wiki/index.php/END_IF "END IF") [LOOP](/qb64wiki/index.php/LOOP "LOOP") [UNTIL](/qb64wiki/index.php/UNTIL "UNTIL") sflag% = 0 ' [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y2% = y3% [THEN](/qb64wiki/index.php/THEN "THEN")     ' Draw a flat bottomed triangle     ydiff1% = y2% - y1%     ydiff2% = y3% - y1%     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope1! = (x2% - x1%) / ydiff1%     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope1! = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")         slope2! = (x3% - x1%) / ydiff2%     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         slope2! = 0     [END IF](/qb64wiki/index.php/END_IF "END IF")     sx! = x1%: ex! = x1%     [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y2%         [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)         sx! = sx! + slope1!         ex! = ex! + slope2!     [NEXT](/qb64wiki/index.php/NEXT "NEXT")     [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB") [ELSE](/qb64wiki/index.php/ELSE "ELSE")     [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") y1% = y2% [THEN](/qb64wiki/index.php/THEN "THEN")         '         ' Draw a flat topped triangle         ydiff1% = y3% - y1%         ydiff2% = y3% - y2%         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope1! = (x3% - x1%) / ydiff1%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope1! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope2! = (x3% - x2%) / ydiff2%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope2! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         sx! = x1%: ex! = x2%         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y3%             [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)             sx! = sx! + slope1!             ex! = ex! + slope2!         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         x1% = sx!: x2% = ex!         [EXIT SUB](/qb64wiki/index.php/EXIT_SUB "EXIT SUB")     [ELSE](/qb64wiki/index.php/ELSE "ELSE")         ' Draw a general purpose triangle         ' First draw the flat bottom portion (top half)         ydiff1% = y2% - y1%         ydiff2% = y3% - y1%         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope1! = (x2% - x1%) / ydiff1%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope1! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope2! = (x3% - x1%) / ydiff2%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope2! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         sx! = x1%: ex! = x1%         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y2%             [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)             sx! = sx! + slope1!             ex! = ex! + slope2!         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         ' Then draw the flat topped portion (bottom half)         x1% = x2%         x2% = ex!         y1% = y2%         ydiff1% = y3% - y1%         ydiff2% = y3% - y2%         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff1% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope1! = (x3% - x1%) / ydiff1%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope1! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         [IF](/qb64wiki/index.php/IF...THEN "IF...THEN") ydiff2% <> 0 [THEN](/qb64wiki/index.php/THEN "THEN")             slope2! = (x3% - x2%) / ydiff2%         [ELSE](/qb64wiki/index.php/ELSE "ELSE")             slope2! = 0         [END IF](/qb64wiki/index.php/END_IF "END IF")         sx! = x1%: ex! = x2%         [FOR](/qb64wiki/index.php/FOR...NEXT "FOR...NEXT") y% = y1% [TO](/qb64wiki/index.php/TO "TO") y3%             [CALL](/qb64wiki/index.php/CALL "CALL") DrawHline([CINT](/qb64wiki/index.php/CINT "CINT")(sx!), [CINT](/qb64wiki/index.php/CINT "CINT")(ex!), y%, col%)             sx! = sx! + slope1!             ex! = ex! + slope2!         [NEXT](/qb64wiki/index.php/NEXT "NEXT")         x1% = sx!: x2% = ex!     [END IF](/qb64wiki/index.php/END_IF "END IF") [END IF](/qb64wiki/index.php/END_IF "END IF") ' [END SUB](/qb64wiki/index.php/END_SUB "END SUB")  ``` |
| --- |


Adapted from a demo by Andrew L. Ayers
  

*Example 4:* Using a desktop image with \_MAPTRIANGLE \_ANTICLOCKWISE rendering.





| ``` [SCREEN](/qb64wiki/index.php/SCREEN "SCREEN") [_NEWIMAGE](/qb64wiki/index.php/NEWIMAGE "NEWIMAGE")(800, 600, 32)  ss32 = [_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE") 'take a 32bit software screenshot [_SETALPHA](/qb64wiki/index.php/SETALPHA "SETALPHA") 128, , ss32 'make it a bit transparent ss33 = [_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")(ss32, 33) 'convert it to a hardware image (mode 33) [_FREEIMAGE](/qb64wiki/index.php/FREEIMAGE "FREEIMAGE") ss32 'we don't need this anymore  DO     [CLS](/qb64wiki/index.php/CLS "CLS") , [_RGB](/qb64wiki/index.php/RGB "RGB")(0, 128, 255) 'use our software screen as a blue backdrop      'rotate our destination points     'the QB64 3D co-ordinate system is the same as  OpenGL's:     '    negative z is in front of you, if it doesn't have a negative z value you won't see it!     '    x goes from left to right, 0 is the middle of the screen     '    y goes from bottom to top, 0 is the middle of the screen     scale = 10     dist = -10     angle = angle + 0.1     x1 = [SIN](/qb64wiki/index.php/SIN "SIN")(angle) * scale     z1 = [COS](/qb64wiki/index.php/COS "COS")(angle) * scale     x2 = [SIN](/qb64wiki/index.php/SIN "SIN")(angle + 3.14) * scale 'adding 3.14 adds 180 degrees     z2 = [COS](/qb64wiki/index.php/COS "COS")(angle + 3.14) * scale     'what we performed above is a 2D/horizontal rotation of points     '(3D rotations are beyond the scope of this example)      'draw the triangle     '_ANTICLOCKWISE makes it only draw when our triangle is facing the correct direction     '_SMOOTH applies linear filtering to avoid a pixelated look      _MAPTRIANGLE **_ANTICLOCKWISE** ([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(ss33) / 2, 0)-(0, [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(ss33))-([_WIDTH](/qb64wiki/index.php/WIDTH_(function) "WIDTH (function)")(ss33),_     [_HEIGHT](/qb64wiki/index.php/HEIGHT "HEIGHT")(ss33)), ss33 TO(0, scale, dist)-(x1, -scale, z1 + dist)-(x2, -scale, z2 + dist), , **_SMOOTH**      [_LIMIT](/qb64wiki/index.php/LIMIT "LIMIT") 30     [_DISPLAY](/qb64wiki/index.php/DISPLAY "DISPLAY") [LOOP](/qb64wiki/index.php/LOOP "LOOP")  ``` |
| --- |


**Tip:** If you are using Linux you might want to replace "[\_SCREENIMAGE](/qb64wiki/index.php/SCREENIMAGE "SCREENIMAGE")" with a [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE") command if you don't see anything.
  




## See also


* [\_PUTIMAGE](/qb64wiki/index.php/PUTIMAGE "PUTIMAGE")
* [\_LOADIMAGE](/qb64wiki/index.php/LOADIMAGE "LOADIMAGE")
* [\_COPYIMAGE](/qb64wiki/index.php/COPYIMAGE "COPYIMAGE")
* [GET (graphics statement)](/qb64wiki/index.php/GET_(graphics_statement) "GET (graphics statement)"), [PUT (graphics statement)](/qb64wiki/index.php/PUT_(graphics_statement) "PUT (graphics statement)")
* [STEP](/qb64wiki/index.php/STEP "STEP"), [SIN](/qb64wiki/index.php/SIN "SIN"), [COS](/qb64wiki/index.php/COS "COS")
* [Hardware images](/qb64wiki/index.php/Hardware_images "Hardware images")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=MAPTRIANGLE&oldid=8868>"




## Navigation menu








### Search





















