<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MAPTRIANGLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MAPTRIANGLE rootpage-MAPTRIANGLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MAPTRIANGLE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MAPTRIANGLE</a> statement maps a triangular portion of an image onto a destination image or screen page.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<h3><span class="mw-headline" id="2D_drawing">2D drawing</span></h3>
<dl><dd><a class="mw-selflink selflink">_MAPTRIANGLE</a> [{_SEAMLESS}] <b>(</b><i>sx1</i><b>,</b> <i>sy1</i><b>)-(</b><i>sx2</i><b>,</b> <i>sy2</i><b>)-(</b><i>sx3</i><b>,</b> <i>sy3</i><b>),</b> <i>source&amp;</i> <b>TO (</b><i>dx1</i><b>,</b> <i>dy1</i><b>)-(</b><i>dx2</i><b>,</b> <i>dy2</i><b>)-(</b><i>dx3</i><b>,</b> <i>dy3</i><b>)</b>[, <i>destination&amp;</i>][,{_SMOOTH|_SMOOTHSHRUNK|_SMOOTHSTRETCHED}</dd></dl>
<h3><span id="3D_drawing_.28hardware_images_only.29"></span><span class="mw-headline" id="3D_drawing_(hardware_images_only)">3D drawing (hardware images only)</span></h3>
<dl><dd><a class="mw-selflink selflink">_MAPTRIANGLE</a> [{_CLOCKWISE|_ANTICLOCKWISE}] [{_SEAMLESS}] <b>(</b><i>sx1</i><b>,</b> <i>sy1</i><b>)-(</b><i>sx2</i><b>,</b> <i>sy2</i><b>)-(</b><i>sx3</i><b>,</b> <i>sy3</i><b>),</b> <i>source&amp;</i> <b>TO (</b><i>dx1</i><b>,</b> <i>dy1</i><b>,</b> <i>dz1</i><b>)-(</b><i>dx2</i><b>,</b> <i>dy2</i><b>,</b> <i>dz2</i><b>)-(</b><i>dx3</i><b>,</b> <i>dy3</i><b>,</b> <i>dz3</i><b>)</b>[, <i>destination&amp;</i>][,{_SMOOTH|_SMOOTHSHRUNK|_SMOOTHSTRETCHED}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <b>_SEAMLESS</b> option makes the triangle skip the right-most and bottom-most pixels of the triangle. When you make larger objects using several triangles, there can be a "seam" where they overlap when using alpha transparency and the seam would be twice as bright. <b>_SEAMLESS</b> is ignored when rendering 3D content and is not yet supported when drawing 2D hardware images.<b></b></li>
<li>For 3D drawing use the <b>_CLOCKWISE</b> and <b>_ANTICLOCKWISE</b> arguments to only draw triangles in the correct direction. See <i>Example 4</i>.</li>
<li>Coordinates are <a href="SINGLE" title="SINGLE">SINGLE</a> values where whole numbers represent the exact center of a pixel of the source texture.</li>
<li><i>source&amp;</i> and optional <i>destination&amp;</i> are <a href="LONG" title="LONG">LONG</a> image or screen page handles.</li>
<li>Supports an optional final argument <b>_SMOOTH</b> which applies linear filtering. See <i>Example 3</i>.</li>
<li>Use <b>_SMOOTHSTRETCHED</b> or <b>_SMOOTHSHRUNK</b> for when a pixelated/smooth effect is desirable but not both.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>This statement is used similar to <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> to place triangular sections of an image, but is more flexible.</li>
<li>The <a href="STEP" title="STEP">STEP</a> keyword can be used to for coordinates relative to the last graphic coordinates used.</li>
<li>For 2D drawing, the destination coordinates are pixel coordinates either on-screen or on the destination image.</li>
<li>For 3D drawing, the destination coordinates represent left (-x) to right (+x), bottom (-y) to top (+y) &amp; furthest (-z) to nearest (z=-1). The center of the screen is therefore (0,0,-1). Note that a z value of 0 will result in off-screen content. The furthest visible z value is -10,000.</li>
<li>When drawing <b>software images</b> coordinate positions are <b>limited from -16383 to 16383</b></li>
<li>The source coordinates can be positioned outside the boundary of the <i>source</i> image to achieve a tiled effect.</li>
<li>If the <i>destination&amp;</i> image handle is the current <a href="SCREEN" title="SCREEN">SCREEN</a> page, <a href="DEST" title="DEST">_DEST</a> or hardware layer, then it can be omitted.</li>
<li><b>Hardware images</b> (created using mode 33 via <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>) can be used as the source or destination.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Rotating the an image using a rotation and zoom SUB with _MAPTRIANGLE.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
Image&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png")   'any 24/32 bit image
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  RotoZoom 400, 300, Image&amp;, 1.5 + <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(zoom), angle
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Angle:"; <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(angle)
  <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT</span></a> "Zoom"; <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">USING</span></a> "##.###"; 1.5 + <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(zoom)
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
  angle = angle + .5: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> angle &gt;= 360 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> angle = angle - 360
  zoom = zoom + .01
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> RotoZoom (X <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Image <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Scale <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, Rotation <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> px(3) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> py(3) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
W&amp; = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(Image&amp;): H&amp; = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(Image&amp;)
px(0) = -W&amp; / 2: py(0) = -H&amp; / 2: px(1) = -W&amp; / 2:py(1) = H&amp; / 2
px(2) = W&amp; / 2: py(2) = H&amp; / 2: px(3) = W&amp; / 2: py(3) = -H&amp; / 2
sinr! = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(-Rotation / 57.2957795131): cosr! = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(-Rotation / 57.2957795131)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3
  x2&amp; = (px(i&amp;) * cosr! + sinr! * py(i&amp;)) * Scale + X: y2&amp; = (py(i&amp;) * cosr! - px(i&amp;) * sinr!) * Scale + Y
  px(i&amp;) = x2&amp;: py(i&amp;) = y2&amp;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(0, H&amp; - 1)-(W&amp; - 1, H&amp; - 1), Image&amp; TO(px(0), py(0))-(px(1), py(1))-(px(2), py(2))
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(W&amp; - 1, 0)-(W&amp; - 1, H&amp; - 1), Image&amp; TO(px(0), py(0))-(px(3), py(3))-(px(2), py(2))
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">        <b>Triangle sections of image in code above     __ </b>
                                                    <b>|\2|</b>
                                                 <b> 1→|_\|</b>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> A 3D Spinning Cube demo using a software image and <a class="mw-selflink selflink">_MAPTRIANGLE</a>:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' Copyright (C) 2011 by Andrew L. Ayers
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> OBJECT(9, 9, 4, 2) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
' OBJECTS DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#OBJECTS,#PLANES PER OBJECT,#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XYZ TRIPLE)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> DPLANE2D(4, 1) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> ' <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> PLANE COORDINATES
' DPLANE2D DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XY <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> DPLANE3D(4, 2) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> ' 3D PLANE COORDINATES
' DPLANE3D DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XYZ TRIPLE)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> PLANECOL(9) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> STAB(359), CTAB(359) ' SINE/COSINE TABLES
D&amp; = 400: MX&amp; = 0: MY&amp; = 0: MZ&amp; = -100
'
' COMPUTE SINE/COSINE TABLES
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 359
  STAB(t&amp;) = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>((6.282 / 360) * t&amp;)
  CTAB(t&amp;) = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>((6.282 / 360) * t&amp;)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
'
' BUILD CUBE IN OBJECT ARRAY
' PLANE 0
OBJECT(0, 0, 0, 0) = -30: OBJECT(0, 0, 0, 1) = 30: OBJECT(0, 0, 0, 2) = -30
OBJECT(0, 0, 1, 0) = -30: OBJECT(0, 0, 1, 1) = -30: OBJECT(0, 0, 1, 2) = -30
OBJECT(0, 0, 2, 0) = 30: OBJECT(0, 0, 2, 1) = -30: OBJECT(0, 0, 2, 2) = -30
OBJECT(0, 0, 3, 0) = 30: OBJECT(0, 0, 3, 1) = 30: OBJECT(0, 0, 3, 2) = -30
OBJECT(0, 0, 4, 0) = 0: OBJECT(0, 0, 4, 1) = 0: OBJECT(0, 0, 4, 2) = -30
' PLANE 1
OBJECT(0, 1, 0, 0) = 30: OBJECT(0, 1, 0, 1) = 30: OBJECT(0, 1, 0, 2) = -30
OBJECT(0, 1, 1, 0) = 30: OBJECT(0, 1, 1, 1) = -30: OBJECT(0, 1, 1, 2) = -30
OBJECT(0, 1, 2, 0) = 30: OBJECT(0, 1, 2, 1) = -30: OBJECT(0, 1, 2, 2) = 30
OBJECT(0, 1, 3, 0) = 30: OBJECT(0, 1, 3, 1) = 30: OBJECT(0, 1, 3, 2) = 30
OBJECT(0, 1, 4, 0) = 30: OBJECT(0, 1, 4, 1) = 0: OBJECT(0, 1, 4, 2) = 0
' PLANE 2
OBJECT(0, 2, 0, 0) = 30: OBJECT(0, 2, 0, 1) = 30: OBJECT(0, 2, 0, 2) = 30
OBJECT(0, 2, 1, 0) = 30: OBJECT(0, 2, 1, 1) = -30: OBJECT(0, 2, 1, 2) = 30
OBJECT(0, 2, 2, 0) = -30: OBJECT(0, 2, 2, 1) = -30: OBJECT(0, 2, 2, 2) = 30
OBJECT(0, 2, 3, 0) = -30: OBJECT(0, 2, 3, 1) = 30: OBJECT(0, 2, 3, 2) = 30
OBJECT(0, 2, 4, 0) = 0: OBJECT(0, 2, 4, 1) = 0: OBJECT(0, 2, 4, 2) = 30
' PLANE 3
OBJECT(0, 3, 0, 0) = -30: OBJECT(0, 3, 0, 1) = 30: OBJECT(0, 3, 0, 2) = 30
OBJECT(0, 3, 1, 0) = -30: OBJECT(0, 3, 1, 1) = -30: OBJECT(0, 3, 1, 2) = 30
OBJECT(0, 3, 2, 0) = -30: OBJECT(0, 3, 2, 1) = -30: OBJECT(0, 3, 2, 2) = -30
OBJECT(0, 3, 3, 0) = -30: OBJECT(0, 3, 3, 1) = 30: OBJECT(0, 3, 3, 2) = -30
OBJECT(0, 3, 4, 0) = -30: OBJECT(0, 3, 4, 1) = 0: OBJECT(0, 3, 4, 2) = 0
' PLANE 4
OBJECT(0, 4, 0, 0) = -30: OBJECT(0, 4, 0, 1) = -30: OBJECT(0, 4, 0, 2) = -30
OBJECT(0, 4, 1, 0) = -30: OBJECT(0, 4, 1, 1) = -30: OBJECT(0, 4, 1, 2) = 30
OBJECT(0, 4, 2, 0) = 30: OBJECT(0, 4, 2, 1) = -30: OBJECT(0, 4, 2, 2) = 30
OBJECT(0, 4, 3, 0) = 30: OBJECT(0, 4, 3, 1) = -30: OBJECT(0, 4, 3, 2) = -30
OBJECT(0, 4, 4, 0) = 0: OBJECT(0, 4, 4, 1) = -30: OBJECT(0, 4, 4, 2) = 0
' PLANE 5
OBJECT(0, 5, 0, 0) = -30: OBJECT(0, 5, 0, 1) = 30: OBJECT(0, 5, 0, 2) = -30
OBJECT(0, 5, 1, 0) = 30: OBJECT(0, 5, 1, 1) = 30: OBJECT(0, 5, 1, 2) = -30
OBJECT(0, 5, 2, 0) = 30: OBJECT(0, 5, 2, 1) = 30: OBJECT(0, 5, 2, 2) = 30
OBJECT(0, 5, 3, 0) = -30: OBJECT(0, 5, 3, 1) = 30: OBJECT(0, 5, 3, 2) = 30
OBJECT(0, 5, 4, 0) = 0: OBJECT(0, 5, 4, 1) = 30: OBJECT(0, 5, 4, 2) = 0
' SET UP PLANE <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a>S ON CUBE
'
PLANECOL(0) = 3
PLANECOL(1) = 4
PLANECOL(2) = 5
PLANECOL(3) = 6
PLANECOL(4) = 7
PLANECOL(5) = 8
'
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "QB64 _MAPTRIANGLE CUBE DEMO"
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
TextureImage&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png") 'any 24/32 bit image
'<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Image&amp;
DO
  ' LIMIT <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 25 FPS
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 25
  ' ERASE LAST IMAGE
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  ' CALCULATE POSITION OF NEW IMAGE
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> OB&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 ' UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9 OBJECTS
    SP = STAB(PIT(OB&amp;)): CP = CTAB(PIT(OB&amp;))
    SY = STAB(YAW(OB&amp;)): CY = CTAB(YAW(OB&amp;))
    SR = STAB(ROL(OB&amp;)): CR = CTAB(ROL(OB&amp;))
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> PL&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 5 ' CONSISTING OF UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9 PLANES
      '
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> PN&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3 ' EACH PLANE WITH UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4 <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S (#5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a>)
        '
        ' TRANSLATE, <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ROTATE
        TX&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 0)
        TY&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 1)
        TZ&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 2)
        RX&amp; = (TZ&amp; * CP - TY&amp; * SP) * SY - ((TZ&amp; * SP + TY&amp; * CP) * SR + TX&amp; * CR) * CY
        RY&amp; = (TZ&amp; * SP + TY&amp; * CP) * CR - TX&amp; * SR
        RZ&amp; = (TZ&amp; * CP - TY&amp; * SP) * CY + ((TZ&amp; * SP + TY&amp; * CP) * SR + TX&amp; * CR) * SY
        '
        ' ROTATE, <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> TRANSLATE
        RX&amp; = RX&amp; + MX&amp;
        RY&amp; = RY&amp; + MY&amp;
        RZ&amp; = RZ&amp; + MZ&amp;
        '
        DPLANE3D(PN&amp;, 0) = RX&amp;: DPLANE3D(PN&amp;, 1) = RY&amp;: DPLANE3D(PN&amp;, 2) = RZ&amp;
        DPLANE2D(PN&amp;, 0) = 399 + (D&amp; * RX&amp; / RZ&amp;)
        DPLANE2D(PN&amp;, 1) = 299 + (D&amp; * RY&amp; / RZ&amp;)
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
      '
      ' CHECK <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> SEE <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> PLANE IS VISIBLE
      x1&amp; = DPLANE3D(0, 0): y1&amp; = DPLANE3D(0, 1): Z1&amp; = DPLANE3D(0, 2)
      x2&amp; = DPLANE3D(1, 0): y2&amp; = DPLANE3D(1, 1): Z2&amp; = DPLANE3D(1, 2)
      x3&amp; = DPLANE3D(2, 0): y3&amp; = DPLANE3D(2, 1): Z3&amp; = DPLANE3D(2, 2)
      T1&amp; = -x1&amp; * (y2&amp; * Z3&amp; - y3&amp; * Z2&amp;)
      T2&amp; = x2&amp; * (y3&amp; * Z1&amp; - y1&amp; * Z3&amp;)
      T3&amp; = x3&amp; * (y1&amp; * Z2&amp; - y2&amp; * Z1&amp;)
      '
      VISIBLE&amp; = T1&amp; - T2&amp; - T3&amp;
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> VISIBLE&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        ' DRAW PLANE
        xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)
        xx2% = DPLANE2D(1, 0): yy2% = DPLANE2D(1, 1)
        xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)
        col% = PLANECOL(PL&amp;)
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(0, 255)-(255, 255), TextureImage&amp; TO(xx3%, yy3%)-(xx2%, yy2%)-(xx1%, yy1%)
        ' CALL DrawTriangle(xx1%, yy1%, xx2%, yy2%, xx3%, yy3%, col%)
        xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)
        xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)
        xx4% = DPLANE2D(3, 0): yy4% = DPLANE2D(3, 1)
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(255, 255)-(255, 0), TextureImage&amp; TO(xx3%, yy3%)-(xx1%, yy1%)-(xx4%, yy4%)
        'CALL DrawTriangle(xx1%, yy1%, xx3%, yy3%, xx4%, yy4%, col%)
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    '
    ' ROTATE OBJECT
    PIT(OB&amp;) = PIT(OB&amp;) + 5
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> PIT(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> PIT(OB&amp;) = 0
    YAW(OB&amp;) = YAW(OB&amp;) + 7
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> YAW(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> YAW(OB&amp;) = 0
    ROL(OB&amp;) = ROL(OB&amp;) + 9
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ROL(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ROL(OB&amp;) = 0
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  '
  ' Calculate Frames per Second
  frames% = frames% + 1
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> oldtime$ &lt;&gt; <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    fps% = frames%
    frames% = 1
    oldtime$ = <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255): <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "FPS :"; fps%
  '
  ' Show Image on Screen
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a> 80: <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DrawHline (fromx%, tox%, yy%, col%)
  '<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>A000
  '<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> fromx% &gt; tox% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> fromx%, tox%
  'yyy&amp; = yy%
  'sloc&amp; = yyy&amp; * 320 + fromx%
  'eloc&amp; = sloc&amp; + (tox% - fromx%)
  '<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t&amp; = sloc&amp; <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> eloc&amp;
  '  <a href="POKE" title="POKE"><span style="color:#4593D8;">POKE</span></a> t&amp;, col%
  '<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  '<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (fromx%, yy%)-(tox%, yy%), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255) 'col%
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DrawTriangle (x1%, y1%, x2%, y2%, x3%, y3%, col%)
  DO
    sflag% = 0
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y1% &gt; y2% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      sflag% = 1
      <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> y1%, y2%
      <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> x1%, x2%
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2% &gt; y3% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      sflag% = 1
      <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> y2%, y3%
      <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> x2%, x3%
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> sflag% = 0
  '
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2% = y3% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    ' Draw a flat bottomed triangle
    ydiff1% = y2% - y1%
    ydiff2% = y3% - y1%
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      slope1! = (x2% - x1%) / ydiff1%
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
      slope1! = 0
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      slope2! = (x3% - x1%) / ydiff2%
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
      slope2! = 0
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    sx! = x1%: ex! = x1%
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y2%
      <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
      sx! = sx! + slope1!
      ex! = ex! + slope2!
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y1% = y2% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      '
      ' Draw a flat topped triangle
      ydiff1% = y3% - y1%
      ydiff2% = y3% - y2%
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope1! = (x3% - x1%) / ydiff1%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope1! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope2! = (x3% - x2%) / ydiff2%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope2! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      sx! = x1%: ex! = x2%
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y3%
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
        sx! = sx! + slope1!
        ex! = ex! + slope2!
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
      x1% = sx!: x2% = ex!
      <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
      ' Draw a general purpose triangle
      ' First draw the flat bottom portion (top half)
      ydiff1% = y2% - y1%
      ydiff2% = y3% - y1%
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope1! = (x2% - x1%) / ydiff1%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope1! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope2! = (x3% - x1%) / ydiff2%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope2! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      sx! = x1%: ex! = x1%
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y2%
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
        sx! = sx! + slope1!
        ex! = ex! + slope2!
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
      ' Then draw the flat topped portion (bottom half)
      x1% = x2%
      x2% = ex!
      y1% = y2%
      ydiff1% = y3% - y1%
      ydiff2% = y3% - y2%
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope1! = (x3% - x1%) / ydiff1%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope1! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope2! = (x3% - x2%) / ydiff2%
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope2! = 0
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
      sx! = x1%: ex! = x2%
      <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y3%
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
        sx! = sx! + slope1!
        ex! = ex! + slope2!
      <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
      x1% = sx!: x2% = ex!
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  '
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> A 3D Spinning Cube demo using a hardware image and <b>QB64GL</b> hardware acceleration with <a class="mw-selflink selflink">_MAPTRIANGLE</a>:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' Copyright (C) 2011 by Andrew L. Ayers
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> OBJECT(9, 9, 4, 2) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
' OBJECTS DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#OBJECTS,#PLANES PER OBJECT,#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XYZ TRIPLE)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> DPLANE2D(4, 1) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> ' <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> PLANE COORDINATES
' DPLANE2D DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XY <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> DPLANE3D(4, 2) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> ' 3D PLANE COORDINATES
' DPLANE3D DEFINED <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> FOLLOWS:
'   (#<a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S PER PLANE, XYZ TRIPLE)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> PLANECOL(9) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> STAB(359), CTAB(359) ' SINE/COSINE TABLES
D&amp; = 400: MX&amp; = 0: MY&amp; = 0: MZ&amp; = -100
'
' COMPUTE SINE/COSINE TABLES
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 359
    STAB(t&amp;) = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>((6.282 / 360) * t&amp;)
    CTAB(t&amp;) = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>((6.282 / 360) * t&amp;)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
'
' BUILD CUBE IN OBJECT ARRAY
' PLANE 0
OBJECT(0, 0, 0, 0) = -30: OBJECT(0, 0, 0, 1) = 30: OBJECT(0, 0, 0, 2) = -30
OBJECT(0, 0, 1, 0) = -30: OBJECT(0, 0, 1, 1) = -30: OBJECT(0, 0, 1, 2) = -30
OBJECT(0, 0, 2, 0) = 30: OBJECT(0, 0, 2, 1) = -30: OBJECT(0, 0, 2, 2) = -30
OBJECT(0, 0, 3, 0) = 30: OBJECT(0, 0, 3, 1) = 30: OBJECT(0, 0, 3, 2) = -30
OBJECT(0, 0, 4, 0) = 0: OBJECT(0, 0, 4, 1) = 0: OBJECT(0, 0, 4, 2) = -30
' PLANE 1
OBJECT(0, 1, 0, 0) = 30: OBJECT(0, 1, 0, 1) = 30: OBJECT(0, 1, 0, 2) = -30
OBJECT(0, 1, 1, 0) = 30: OBJECT(0, 1, 1, 1) = -30: OBJECT(0, 1, 1, 2) = -30
OBJECT(0, 1, 2, 0) = 30: OBJECT(0, 1, 2, 1) = -30: OBJECT(0, 1, 2, 2) = 30
OBJECT(0, 1, 3, 0) = 30: OBJECT(0, 1, 3, 1) = 30: OBJECT(0, 1, 3, 2) = 30
OBJECT(0, 1, 4, 0) = 30: OBJECT(0, 1, 4, 1) = 0: OBJECT(0, 1, 4, 2) = 0
' PLANE 2
OBJECT(0, 2, 0, 0) = 30: OBJECT(0, 2, 0, 1) = 30: OBJECT(0, 2, 0, 2) = 30
OBJECT(0, 2, 1, 0) = 30: OBJECT(0, 2, 1, 1) = -30: OBJECT(0, 2, 1, 2) = 30
OBJECT(0, 2, 2, 0) = -30: OBJECT(0, 2, 2, 1) = -30: OBJECT(0, 2, 2, 2) = 30
OBJECT(0, 2, 3, 0) = -30: OBJECT(0, 2, 3, 1) = 30: OBJECT(0, 2, 3, 2) = 30
OBJECT(0, 2, 4, 0) = 0: OBJECT(0, 2, 4, 1) = 0: OBJECT(0, 2, 4, 2) = 30
' PLANE 3
OBJECT(0, 3, 0, 0) = -30: OBJECT(0, 3, 0, 1) = 30: OBJECT(0, 3, 0, 2) = 30
OBJECT(0, 3, 1, 0) = -30: OBJECT(0, 3, 1, 1) = -30: OBJECT(0, 3, 1, 2) = 30
OBJECT(0, 3, 2, 0) = -30: OBJECT(0, 3, 2, 1) = -30: OBJECT(0, 3, 2, 2) = -30
OBJECT(0, 3, 3, 0) = -30: OBJECT(0, 3, 3, 1) = 30: OBJECT(0, 3, 3, 2) = -30
OBJECT(0, 3, 4, 0) = -30: OBJECT(0, 3, 4, 1) = 0: OBJECT(0, 3, 4, 2) = 0
' PLANE 4
OBJECT(0, 4, 0, 0) = -30: OBJECT(0, 4, 0, 1) = -30: OBJECT(0, 4, 0, 2) = -30
OBJECT(0, 4, 1, 0) = -30: OBJECT(0, 4, 1, 1) = -30: OBJECT(0, 4, 1, 2) = 30
OBJECT(0, 4, 2, 0) = 30: OBJECT(0, 4, 2, 1) = -30: OBJECT(0, 4, 2, 2) = 30
OBJECT(0, 4, 3, 0) = 30: OBJECT(0, 4, 3, 1) = -30: OBJECT(0, 4, 3, 2) = -30
OBJECT(0, 4, 4, 0) = 0: OBJECT(0, 4, 4, 1) = -30: OBJECT(0, 4, 4, 2) = 0
' PLANE 5
OBJECT(0, 5, 0, 0) = -30: OBJECT(0, 5, 0, 1) = 30: OBJECT(0, 5, 0, 2) = -30
OBJECT(0, 5, 1, 0) = 30: OBJECT(0, 5, 1, 1) = 30: OBJECT(0, 5, 1, 2) = -30
OBJECT(0, 5, 2, 0) = 30: OBJECT(0, 5, 2, 1) = 30: OBJECT(0, 5, 2, 2) = 30
OBJECT(0, 5, 3, 0) = -30: OBJECT(0, 5, 3, 1) = 30: OBJECT(0, 5, 3, 2) = 30
OBJECT(0, 5, 4, 0) = 0: OBJECT(0, 5, 4, 1) = 30: OBJECT(0, 5, 4, 2) = 0
' SET UP PLANE <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a>S ON CUBE
'
PLANECOL(0) = 3
PLANECOL(1) = 4
PLANECOL(2) = 5
PLANECOL(3) = 6
PLANECOL(4) = 7
PLANECOL(5) = 8
'
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "QB64 <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> CUBE DEMO"
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
TextureImage&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png", 32) 'any 24/32 bit image
<a href="SETALPHA" title="SETALPHA"><span style="color:#4593D8;">_SETALPHA</span></a> 128, , TextureImage&amp;
TextureImage&amp; = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(TextureImage&amp;, 33)'copy of hardware image
'<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Image&amp;
DO
    ' LIMIT <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 25 FPS
    '<a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 25
    ' <a href="ERASE" title="ERASE"><span style="color:#4593D8;">ERASE</span></a> LAST IMAGE
    '<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 0, 160)
    ' CALCULATE POSITION OF NEW IMAGE
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> OB&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 ' UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9 OBJECTS
        SP = STAB(PIT(OB&amp;)): CP = CTAB(PIT(OB&amp;))
        SY = STAB(YAW(OB&amp;)): CY = CTAB(YAW(OB&amp;))
        SR = STAB(ROL(OB&amp;)): CR = CTAB(ROL(OB&amp;))
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> PL&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 5 ' CONSISTING OF UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9 PLANES
            '
            <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> PN&amp; = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3 ' EACH PLANE WITH UP <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4 <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>S (#5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a>)
                '
                ' TRANSLATE, <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ROTATE
                TX&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 0)
                TY&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 1)
                TZ&amp; = OBJECT(OB&amp;, PL&amp;, PN&amp;, 2)
                RX&amp; = (TZ&amp; * CP - TY&amp; * SP) * SY - ((TZ&amp; * SP + TY&amp; * CP) * SR + TX&amp; * CR) * CY
                RY&amp; = (TZ&amp; * SP + TY&amp; * CP) * CR - TX&amp; * SR
                RZ&amp; = (TZ&amp; * CP - TY&amp; * SP) * CY + ((TZ&amp; * SP + TY&amp; * CP) * SR + TX&amp; * CR) * SY
                '
                ' ROTATE, <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> TRANSLATE
                RX&amp; = RX&amp; + MX&amp;
                RY&amp; = RY&amp; + MY&amp;
                RZ&amp; = RZ&amp; + MZ&amp;
                '
                DPLANE3D(PN&amp;, 0) = RX&amp;: DPLANE3D(PN&amp;, 1) = RY&amp;: DPLANE3D(PN&amp;, 2) = RZ&amp;
                DPLANE2D(PN&amp;, 0) = 399 + (D&amp; * RX&amp; / RZ&amp;)
                DPLANE2D(PN&amp;, 1) = 299 + (D&amp; * RY&amp; / RZ&amp;)
            <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
            '
            ' CHECK <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> SEE <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> PLANE <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> VISIBLE
            x1&amp; = DPLANE3D(0, 0): y1&amp; = DPLANE3D(0, 1): Z1&amp; = DPLANE3D(0, 2)
            x2&amp; = DPLANE3D(1, 0): y2&amp; = DPLANE3D(1, 1): Z2&amp; = DPLANE3D(1, 2)
            x3&amp; = DPLANE3D(2, 0): y3&amp; = DPLANE3D(2, 1): Z3&amp; = DPLANE3D(2, 2)
            T1&amp; = -x1&amp; * (y2&amp; * Z3&amp; - y3&amp; * Z2&amp;)
            T2&amp; = x2&amp; * (y3&amp; * Z1&amp; - y1&amp; * Z3&amp;)
            T3&amp; = x3&amp; * (y1&amp; * Z2&amp; - y2&amp; * Z1&amp;)
            '
            VISIBLE&amp; = T1&amp; - T2&amp; - T3&amp;
            <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> VISIBLE&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                ' <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> PLANE
                xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)
                xx2% = DPLANE2D(1, 0): yy2% = DPLANE2D(1, 1)
                xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)
                col% = PLANECOL(PL&amp;)
                <a href="BLEND" title="BLEND"><span style="color:#4593D8;">_BLEND</span></a> TextureImage&amp;
                <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(0, 255)-(255, 255), TextureImage&amp; TO(xx1%, yy1%)-(xx2%, yy2%)-(xx3%, yy3%)
                ' <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawTriangle(xx1%, yy1%, xx2%, yy2%, xx3%, yy3%, col%)
                xx1% = DPLANE2D(0, 0): yy1% = DPLANE2D(0, 1)
                xx3% = DPLANE2D(2, 0): yy3% = DPLANE2D(2, 1)
                xx4% = DPLANE2D(3, 0): yy4% = DPLANE2D(3, 1)
                <a href="DONTBLEND" title="DONTBLEND"><span style="color:#4593D8;">_DONTBLEND</span></a> TextureImage&amp;
                <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (0, 0)-(255, 255)-(255, 0), TextureImage&amp; TO(xx3%, yy3%)-(xx1%, yy1%)-(xx4%, yy4%), , _SMOOTH
                '<a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawTriangle(xx1%, yy1%, xx3%, yy3%, xx4%, yy4%, col%)
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        '
        ' ROTATE OBJECT
        PIT(OB&amp;) = PIT(OB&amp;) + 5
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> PIT(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> PIT(OB&amp;) = 0
        YAW(OB&amp;) = YAW(OB&amp;) + 7
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> YAW(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> YAW(OB&amp;) = 0
        ROL(OB&amp;) = ROL(OB&amp;) + 9
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ROL(OB&amp;) &gt; 359 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ROL(OB&amp;) = 0
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    '
    ' Calculate Frames per Second
    frames% = frames% + 1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> oldtime$ &lt;&gt; <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        fps% = frames%
        frames% = 1
        oldtime$ = <a href="TIME$" title="TIME$"><span style="color:#4593D8;">TIME$</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255): <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "FPS :"; fps%
    '
    ' Show Image on Screen
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
<a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a> 80: <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 0: <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DrawHline (fromx%, tox%, yy%, col%)
'<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>A000
'<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> fromx% &gt; tox% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> fromx%, tox%
'yyy&amp; = yy%
'sloc&amp; = yyy&amp; * 320 + fromx%
'eloc&amp; = sloc&amp; + (tox% - fromx%)
'<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t&amp; = sloc&amp; <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> eloc&amp;
'  <a href="POKE" title="POKE"><span style="color:#4593D8;">POKE</span></a> t&amp;, col%
'<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
'<a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (fromx%, yy%)-(tox%, yy%), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255) 'col%
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DrawTriangle (x1%, y1%, x2%, y2%, x3%, y3%, col%)
DO
    sflag% = 0
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y1% &gt; y2% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        sflag% = 1
        <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> y1%, y2%
        <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> x1%, x2%
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2% &gt; y3% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        sflag% = 1
        <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> y2%, y3%
        <a href="SWAP" title="SWAP"><span style="color:#4593D8;">SWAP</span></a> x2%, x3%
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> sflag% = 0
'
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y2% = y3% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    ' Draw a flat bottomed triangle
    ydiff1% = y2% - y1%
    ydiff2% = y3% - y1%
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope1! = (x2% - x1%) / ydiff1%
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope1! = 0
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        slope2! = (x3% - x1%) / ydiff2%
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slope2! = 0
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    sx! = x1%: ex! = x1%
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y2%
        <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
        sx! = sx! + slope1!
        ex! = ex! + slope2!
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y1% = y2% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        '
        ' Draw a flat topped triangle
        ydiff1% = y3% - y1%
        ydiff2% = y3% - y2%
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope1! = (x3% - x1%) / ydiff1%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope1! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope2! = (x3% - x2%) / ydiff2%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope2! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        sx! = x1%: ex! = x2%
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y3%
            <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
            sx! = sx! + slope1!
            ex! = ex! + slope2!
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        x1% = sx!: x2% = ex!
        <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        ' Draw a general purpose triangle
        ' First draw the flat bottom portion (top half)
        ydiff1% = y2% - y1%
        ydiff2% = y3% - y1%
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope1! = (x2% - x1%) / ydiff1%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope1! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope2! = (x3% - x1%) / ydiff2%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope2! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        sx! = x1%: ex! = x1%
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y2%
            <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
            sx! = sx! + slope1!
            ex! = ex! + slope2!
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        ' Then draw the flat topped portion (bottom half)
        x1% = x2%
        x2% = ex!
        y1% = y2%
        ydiff1% = y3% - y1%
        ydiff2% = y3% - y2%
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff1% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope1! = (x3% - x1%) / ydiff1%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope1! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> ydiff2% &lt;&gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            slope2! = (x3% - x2%) / ydiff2%
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            slope2! = 0
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        sx! = x1%: ex! = x2%
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = y1% <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y3%
            <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> DrawHline(<a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(sx!), <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(ex!), y%, col%)
            sx! = sx! + slope1!
            ex! = ex! + slope2!
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        x1% = sx!: x2% = ex!
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
'
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Using a desktop image with _MAPTRIANGLE _ANTICLOCKWISE rendering.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 32)
ss32 = <a href="SCREENIMAGE" title="SCREENIMAGE"><span style="color:#4593D8;">_SCREENIMAGE</span></a> 'take a 32bit software screenshot
<a href="SETALPHA" title="SETALPHA"><span style="color:#4593D8;">_SETALPHA</span></a> 128, , ss32 'make it a bit transparent
ss33 = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(ss32, 33) 'convert it to a hardware image (mode 33)
<a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> ss32 'we don't need this anymore
DO
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 128, 255) 'use our software screen as a blue backdrop
    'rotate our destination points
    'the QB64 3D co-ordinate system is the same as  OpenGL's:
    '    negative z is in front of you, if it doesn't have a negative z value you won't see it!
    '    x goes from left to right, 0 is the middle of the screen
    '    y goes from bottom to top, 0 is the middle of the screen
    scale = 10
    dist = -10
    angle = angle + 0.1
    x1 = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(angle) * scale
    z1 = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(angle) * scale
    x2 = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(angle + 3.14) * scale 'adding 3.14 adds 180 degrees
    z2 = <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(angle + 3.14) * scale
    'what we performed above is a 2D/horizontal rotation of points
    '(3D rotations are beyond the scope of this example)
    'draw the triangle
    '_ANTICLOCKWISE makes it only draw when our triangle is facing the correct direction
    '_SMOOTH applies linear filtering to avoid a pixelated look
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> <b>_ANTICLOCKWISE</b> (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(ss33) / 2, 0)-(0, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(ss33))-(<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(ss33),_
    <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(ss33)), ss33 TO(0, scale, dist)-(x1, -scale, z1 + dist)-(x2, -scale, z2 + dist), , <b>_SMOOTH</b>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><b>Tip:</b> If you are using Linux you might want to replace "<a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>" with a <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> command if you don't see anything.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="STEP" title="STEP">STEP</a>, <a href="SIN" title="SIN">SIN</a>, <a href="COS" title="COS">COS</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192742
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.122 seconds
Real time usage: 0.135 seconds
Preprocessor visited node count: 3216/1000000
Post‐expand include size: 23319/2097152 bytes
Template argument size: 4349/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   57.172      1 -total
 28.30%   16.182    427 Template:Cl
  4.23%    2.419     34 Template:Parameter
  3.81%    2.180      1 Template:PageSyntax
  3.72%    2.127      1 Template:PageSeeAlso
  3.20%    1.829      1 Template:PageParameters
  3.01%    1.718      1 Template:PageNavigation
  2.96%    1.692      1 Template:PageExamples
  2.84%    1.624      4 Template:CodeEnd
  2.79%    1.597      3 Template:Small
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:171-0!canonical and timestamp 20240714192742 and revision id 8868.
 -->
</div>
</div>
</div>
</div>
</body>
</html>