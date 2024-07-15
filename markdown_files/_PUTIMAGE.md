<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PUTIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PUTIMAGE rootpage-PUTIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PUTIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_PUTIMAGE</a> puts an area of a source image to an area of a destination image in one operation, like <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> and <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> [STEP] [(<i>dx1</i>, <i>dy1</i>)-[STEP][(<i>dx2</i>, <i>dy2</i>)[, <i>sourceHandle&amp;</i>][, <i>destHandle&amp;</i>][, ][STEP][(<i>sx1</i>, <i>sy1</i>)[-STEP][(<i>sx2</i>, <i>sy2</i>)[, <i>_SMOOTH</i>]</dd></dl>
<h3><span class="mw-headline" id="Sample_usage">Sample usage</span></h3>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> <span style="color:#777777;">'full source image to fit full destination area after <a href="SOURCE" title="SOURCE">_SOURCE</a> and <a href="DEST" title="DEST">_DEST</a> are set</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> , <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i> <span style="color:#777777;">'size full source to fit full destination area</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> (<i>dx1</i>, <i>dy1</i>), <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i> <span style="color:#777777;">'full source to top-left corner destination position</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> (<i>dx1</i>, <i>dy1</i>)-(<i>dx2</i>, <i>dy2</i>), <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i> <span style="color:#777777;">'size full source to destination coordinate area</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> (<i>dx1</i>, <i>dy1</i>), <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i>, (<i>sx1</i>, <i>sy1</i>)-(<i>sx2</i>, <i>sy2</i>) <span style="color:#777777;">'portion of source to the top-left corner of the destination page</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> , <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i>, (<i>sx1</i>, <i>sy1</i>)-(<i>sx2</i>, <i>sy2</i>) <span style="color:#777777;">'portion of source to full destination area</span></dd></dl></dd></dl>
<dl><dd><dl><dd><a class="mw-selflink selflink">_PUTIMAGE</a> (<i>dx1</i>, <i>dy1</i>)-(<i>dx2</i>, <i>dy2</i>), <i>sourceHandle&amp;</i>, <i>destHandle&amp;</i>,(<i>sx1</i>, <i>sy1</i>) <span style="color:#777777;">'right side of source from top-left corner to destination</span></dd></dl></dd></dl>
<p>
</p>
<dl><dd><dl><dd>Note: The top-left corner position designates the leftmost and topmost portion of the image to use.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Relative coordinates to a previous graphical object can be designated using <a href="STEP" title="STEP">STEP</a> as opposed to literal surface coordinates (version <b>1.000</b> and up).</li>
<li>Coordinates <i>dx</i> and <i>dy</i> map the box area of the <a href="DEST" title="DEST">destination</a> area to use. When omitted the entire desination area is used. If only one coordinate is used, the source is placed with its original dimensions. Coordinates can be set to flip or resize the image.
<ul><li><i>dx1</i> = the column coordinate at which the insertion of the source will begin (leftmost); when larger than <i>dx2</i>, reverses image.</li>
<li><i>dy1</i> = the row coordinate at which the insertion of the source will begin (topmost); when larger than <i>dy2</i>, inverts image.</li>
<li><i>dx2</i> = the column coordinate at which the insertion of the source will end (rightmost); further apart, widens image.</li>
<li><i>dy2</i> = the row coordinate at which the insertion of the source will end (bottommost); closer together, shrinks image</li></ul></li>
<li><i>sourceHandle&amp;</i> = the <a href="LONG" title="LONG">LONG</a> handle of the <a href="SOURCE" title="SOURCE">source</a> image created with <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>.</li>
<li><i>destHandle&amp;</i> = the <a href="LONG" title="LONG">LONG</a> handle of the <a href="DEST" title="DEST">destination</a> image may be created with <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="SCREEN" title="SCREEN">SCREEN</a> or <a href="DEST" title="DEST">destination</a> 0.</li>
<li>Coordinates <i>sx</i> and <i>sy</i> <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> the box area of the <a href="SOURCE" title="SOURCE">source</a> image to transfer to the <a href="DEST" title="DEST">destination</a> image, page or <a href="SCREEN" title="SCREEN">screen</a>:
<ul><li><i>sx1</i> = the column coordinate of the left-most pixel to include of the source. When omitted, the entire image is used</li>
<li><i>sy1</i> = the row coordinate of the upper-most pixel to include of the source. When omitted, the entire image is used</li>
<li><i>sx2</i> = the column coordinate of the right-most pixel to include of the source. Can be omitted to get rest of image.</li>
<li><i>sy2</i> = the row coordinate of the bottom-most pixel to include of the source. Can be omitted to get rest of image.</li></ul></li>
<li><i>_SMOOTH</i> applies linear filtering (<b>version 1.000 and up</b>).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>_PUTIMAGE can be used without any handle parameters if the <a href="SOURCE" title="SOURCE">_SOURCE</a> and/or <a href="DEST" title="DEST">_DEST</a> are already defined.</li>
<li>If the area of the source is bigger or smaller than the area of the destination then the image is adjusted to fit that area.</li>
<li>Supports 32 bit alpha blending, color key transparency, true type fonts, stretching, mirroring/flipping, and a variety of graphics file formats including gif, png, bmp &amp; jpg. <b>32 bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> and are transparent when placed over other surfaces.</b> Use <a href="CLS" title="CLS">CLS</a> or <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> to make a new surface background <a href="ALPHA" title="ALPHA">_ALPHA</a> 255 or opaque.</li>
<li>All graphical surfaces, including screen pages, can be acted upon in the same manner, and are referred to as "images".</li>
<li><b>Hardware images</b> (created using mode <b>33</b> via <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>) can be used as the source or destination.</li>
<li><a href="Handle" title="Handle">Handles</a> are used to identify graphical surfaces. Positive values are used to refer to screen pages. -1 (negative one) indicates an invalid surface. It is recommended to store image handles in <a href="LONG" title="LONG">LONG</a> variables. Passing an invalid handle generates an <a href="ERROR_Codes" title="ERROR Codes">"Invalid handle"</a> error.</li>
<li>When handles are not passed (or cannot be passed) to subs/functions then the default destination image or source image is referenced. These are set to the active page when the SCREEN statement is called, but can be changed to any image. So it is possible to read from one image using <a href="POINT" title="POINT">POINT</a> and write to a different one with <a href="PSET" title="PSET">PSET</a>.</li>
<li><b><a href="PRINT" title="PRINT">PRINTed</a> text cannot be transferred and positioned accurately.</b> Use <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> for graphical text or font placement.</li>
<li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li>
<li><b>It is important to free discarded or unused images with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent CPU memory overflow errors.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
 a&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 200, 13) ' creates a 640 * 200 image with the <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> handle a&amp;
 <a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> a&amp; ' makes image a&amp; the default drawing output.
 <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (10, 10)-(100, 100), 12, BF ' draws a filled box (BF) into destination
 <a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0)-(320, 200), a&amp;, 0, (0, 0)-(320, 200)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i></dd>
<dd>1) A graphics mode is set by using <a href="SCREEN" title="SCREEN">SCREEN</a> 13 which can use up to 256 colors.</dd>
<dd>2) A new image is created that is 640 X 200 and uses the palette compatible with SCREEN 13 (256 colors).</dd>
<dd>3) <a href="DEST" title="DEST">_DEST</a> a&amp; makes the image with handle 'a&amp;' the default image to draw on instead of the screen (which is <a href="DEST" title="DEST">_DEST</a> 0).</dd>
<dd>4) Next a filled box (BF) is drawn from 10, 10 to 100, 100 with red color (12) to the destination image (set by <a href="DEST" title="DEST">_DEST</a> a&amp;)</dd>
<dd>5) Now we put the image from 0, 0 to 320, 200 from the image with the handle 'a&amp;' to the screen (always handle 0) and puts this image into the coordinates 0, 0 to 320, 200. If we want to stretch the image we can alter these coordinates.</dd></dl>
<dl><dd><b>Note:</b> All arguments are optional. If you want to simply put the whole image of the source to the whole image of the destination then you omit the area (x, y)-(x2, y2) on both sides, the last line of the example can be replaced by <a class="mw-selflink selflink">_PUTIMAGE</a> , a&amp;, 0 which indeed will stretch the image since image a&amp; is bigger than the screen (the screen is 320 * 200 and a&amp; is 640 * 200)</dd></dl>
<p>
<i>Example 2: </i>You don't need to do anything special to use a .PNG image with alpha/transparency. Here's a simple example:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 255, 0)
i = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<b>"QB64.PNG"</b>) 'any 32 bit image (ie. with alpha channel)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0), i ' places image at upper left corner of window w/o stretching it
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When QB64 loads a 256 color .PNG file containing a transparent color, that color will be treated as transparent when _PUTIMAGE is used to put it onto another image. So actually, you can use a 256-color .PNG file containing transparency information in a 256 color screen mode in QB64.</dd></dl>
<p>
<i>Example 3:</i> Flipping and enlarging an image with _PUTIMAGE by swapping or increasing the desination coordinates.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFLNG" title="DEFLNG"><span style="color:#4593D8;">DEFLNG</span></a> A-Z
dest_handle = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> dest_handle  '32 bit Screen 12 dimensions
source_handle = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<b>"QB64.PNG"</b>, 32) 'any 32 bit image (ie. with alpha channel)
dx1 = 0: dy1 = 0
dx2 = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(source_handle) - 1: dy2 = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(source_handle) - 1 'image dimensions - 1
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 29, 33: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press any Key!";
'normal image coordinate values based on the dimensions of the image:
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (dx1, dy1)-(dx2, dy2), source_handle, dest_handle
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Normal layout"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_PUTIMAGE (dx1, dy1)-(dx2, dy2), source_handle, dest_handle"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
'to flip the image on the x axis, swap the dx coordinate values:
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (dx2, dy1)-(dx1, dy2), source_handle, dest_handle
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Flip by X axis"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_PUTIMAGE (dx2, dy1)-(dx1, dy2), source_handle, dest_handle"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
'to flip image on y axis, swap the dy coordinate values:
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (dx1, dy2)-(dx2, dy1), source_handle, dest_handle
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Flip by Y axis"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_PUTIMAGE (dx1, dy2)-(dx2, dy1), source_handle, dest_handle "
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
'to flip both, swap both the dx and dy coordinate values:
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (dx2, dy2)-(dx1, dy1), source_handle, dest_handle
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Flip on both axis"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_PUTIMAGE (dx2, dy2)-(dx1, dy1), source_handle, dest_handle"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
'to enlarge, double the second set of values plus any offset of the first coordinates:
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (dx1, dy1)-((2 * dx2) + dx1, (2 * dy2) + dy1), source_handle, dest_handle
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 34: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Double image size"
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 24, 2:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_PUTIMAGE (dx1, dy1)-((2 * dx2) + dx1, (2 * dy2) + dy1), s_handle, d_handle
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Using _PUTIMAGE to scroll a larger image created on a separate <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page with QB64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
ws&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(2560, 1440, 32) 'large image page
s&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(1280, 720, 32)' program screen
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> ws&amp; 'create large image of random filled circles
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 50
    x = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 2560
    y = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 1440
    clr&amp; = <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 255, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 255)
    <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x, y), <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>(1) * 300, clr&amp;
    <a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (x, y), clr&amp;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This is a demo of some screen scrolling.   Use the number pad keys to scroll.  4 goes left, 6 goes right.  8 up, 2 down. ESC key will close this program."
x = 0: y = 0
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> s&amp;
DO
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0), ws&amp;, 0, (x, y)-(x + 1279, y + 719)
    a$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> a$
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "4": x = x - 10: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> x = 0
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "6": x = x + 10: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x &gt; 1280 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> x = 1280
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "8": y = y - 10: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> y = 0
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "2": y = y + 10: <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y &gt; 720 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> y = 720
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(32): <a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 5:</i> _PUTIMAGE can be used with no parameters at all if the <a href="SOURCE" title="SOURCE">_SOURCE</a> and <a href="DEST" title="DEST">_DEST</a> are already set.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
h&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 256)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> h&amp;
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (10, 10), "This _PUTIMAGE used no parameters!"
<a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> h&amp;
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> 0
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PUTIMAGE</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="Bitmaps" title="Bitmaps">Bitmaps</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1119" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>, <a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="MAPTRIANGLE" title="MAPTRIANGLE">_MAPTRIANGLE</a>, <a href="STEP" title="STEP">STEP</a></li>
<li><a href="DEST" title="DEST">_DEST</a>, <a href="SOURCE" title="SOURCE">_SOURCE</a>, <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154148
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.064 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 1279/1000000
Post‐expand include size: 7527/2097152 bytes
Template argument size: 1885/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.005      1 -total
 15.82%    4.905     99 Template:Cl
  8.56%    2.654      1 Template:PageSyntax
  7.92%    2.456     32 Template:Parameter
  5.74%    1.780      7 Template:Text
  5.73%    1.778      2 Template:Small
  5.47%    1.695      1 Template:PageSeeAlso
  5.40%    1.674      1 Template:PageNavigation
  4.85%    1.505      1 Template:PageParameters
  4.80%    1.488      5 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:257-0!canonical and timestamp 20240714154148 and revision id 8888.
 -->
</div>
</div>
</div>
</div>
</body>
</html>