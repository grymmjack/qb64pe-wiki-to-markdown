<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>POINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-POINT rootpage-POINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">POINT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>POINT</b> function returns the pixel <a href="COLOR" title="COLOR">COLOR</a> attribute at a specified graphics coordinate or the current graphic cursor position.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>Graphic Color</dt>
<dd>color_attribute% = <b>POINT (</b><i>column%, row%</i><b>)</b></dd>
<dt>Graphic cursor position</dt>
<dd>pointer_coordinate% = <b>POINT(</b>{0|1|2|3}<b>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<p><b>Graphic Color syntax:</b>
</p>
<ul><li>The <a href="INTEGER" title="INTEGER">INTEGER</a> <i>column</i> and <i>row</i> coordinates designate the pixel position color on the screen to read.</li>
<li>The return value is an <a href="INTEGER" title="INTEGER">INTEGER</a> palette attribute value or an <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> <a href="RGBA" title="RGBA">_RGBA</a> 32 bit value in QB64.</li></ul>
<p><b>Graphic cursor position syntax:</b>
</p>
<ul><li>The <a href="INTEGER" title="INTEGER">INTEGER</a> position number can be 0 to 3 depending on the cursor position desired:
<ul><li>POINT(0) returns the current graphic cursor <a href="SCREEN" title="SCREEN">SCREEN</a> column pixel coordinate.</li>
<li>POINT(1) returns the current graphic cursor <a href="SCREEN" title="SCREEN">SCREEN</a> row pixel coordinate.</li>
<li>POINT(2) returns the current graphic cursor <a href="WINDOW" title="WINDOW">WINDOW</a> column position.</li>
<li>POINT(3) returns the current graphic cursor <a href="WINDOW" title="WINDOW">WINDOW</a> row position.</li></ul></li>
<li>If a <a href="WINDOW" title="WINDOW">WINDOW</a> view port has not been established, the coordinate returned will be the <a href="SCREEN" title="SCREEN">SCREEN</a> cursor pixel position.</li>
<li>The return value is the current graphic cursor <i>column</i> or <i>row</i> pixel position on the <a href="SCREEN" title="SCREEN">SCREEN</a> or <a href="WINDOW" title="WINDOW">WINDOW</a>.</li>
<li>Graphic cursor positions returned will be the last ones used in a graphic shape such as a <a href="CIRCLE" title="CIRCLE">CIRCLE</a> center point.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>Use <b><a href="SOURCE" title="SOURCE">_SOURCE</a></b> first to set the image handle that POINT should read or QB64 will assume the current source image.</li></ul>
<dl><dd><dl><dd><b><span style="color:green;">_SOURCE 0</span></b> 'sets POINT to read the current SCREEN image after reading a previous source image</dd></dl></dd></dl>
<ul><li><b>POINT cannot be used in SCREEN 0!</b> Use the <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN</a> function to point text character codes and colors in SCREEN 0.</li></ul>
<p>
</p>
<ul><li>The <a href="INTEGER" title="INTEGER">INTEGER</a> color attributes returned are limited by the number of colors in the legacy SCREEN mode used.</li>
<li><i>Column</i> and <i>row</i> <a href="INTEGER" title="INTEGER">INTEGER</a> parameters denote the graphic pixel coordinate to read.</li>
<li>In <b>QB64</b> the offscreen or off image value returned is -1. Use IF POINT(x, y) &lt;&gt; -1 THEN...</li>
<li>In QBasic the coordinates MUST be on the screen or an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call error</a> will occur.</li></ul>
<p>
</p>
<ul><li>Returns <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> 32 bit color values. Use <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> values when you don't want negative values.</li>
<li><b><a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> variables should be used when comparing POINT returns with <a href="RGB" title="RGB">_RGB</a> or <a href="RGB32" title="RGB32">_RGB32</a> <a href="ALPHA" title="ALPHA">_ALPHA</a> bit values</b></li>
<li>Convert 32 bit color values to RGB intensities(0 to 255) using the <a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a> and <a href="BLUE32" title="BLUE32">_BLUE32</a> functions.</li>
<li>To convert color intensities to OUT &amp;H3C9 color port palette intensity values divide the values of 0 to 255 by 4.</li>
<li>Use the <a href="PALETTECOLOR_(function)" title="PALETTECOLOR (function)">_PALETTECOLOR (function)</a> to convert color port palette intensities in 32 bit modes.</li></ul>
<p>
<i>Example 1:</i> How <a href="RGB" title="RGB">_RGB</a> 32 bit values return <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> values in QB64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> clr <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> 'DO NOT use LONG in older versions of QB64 (V .936 down)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255)  'makes the background opaque white
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "POINT(100, 100) ="; <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span></a>(100, 100)
clr = <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span></a>(100, 100)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Variable clr = ";  clr
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> clr = <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Long OK"
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span></a>(100, 100) = <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "_RGB OK"
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span></a>(100, 100) = clr <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Type OK" 'will not print with a LONG variable type
</pre>
</td></tr></tbody></table>
<dl><dd><b>Note:</b> Change the <a href="DIM" title="DIM">DIM</a> <i>clr</i> variable type to <a href="LONG" title="LONG">LONG</a> to see how the last <a class="mw-redirect" href="IF" title="IF">IF</a> statement doesn't <a href="PRINT" title="PRINT">PRINT</a> as shown in the output below:</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">POINT(100, 100) = 4294967295
Variable clr = -1
Long OK
_RGB OK
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Using a <a class="mw-selflink selflink">POINT</a> mouse routine to get the 32 bit color values of the image.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "Mouse <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span>er</a> 32"
'<a href="LINE_INPUT" title="LINE INPUT"><span style="color:#4593D8;">LINE INPUT</span></a> "Enter an image file: ", image$  'use quotes around file names with spaces
image$ = "QB64bee.png" 'any 24/32 bit image up to 320 X 240 with current <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> settings
i&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(image$, 32)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> i&amp; &gt;= -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="BEEP" title="BEEP"><span style="color:#4593D8;">BEEP</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Could <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> load image!": <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
w&amp; = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(i&amp;): h&amp; = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(i&amp;)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Make background transparent?(Y\N)";
BG$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1))
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> BG$
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 1
'<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> 'commented to keep background alpha 0
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> BG$ = "Y" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CLEARCOLOR" title="CLEARCOLOR"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 255, 255), i&amp; 'make white Background transparent
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (320 - w&amp;, 240 - h&amp;)-((2 * w&amp;) + (320 - w&amp;), (2 * h&amp;) + (240 - h&amp;)), i&amp;, 0
<a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> i&amp;
<a href="MOUSEMOVE" title="MOUSEMOVE"><span style="color:#4593D8;">_MOUSEMOVE</span></a> 320, 240 'center mouse pointer on screen
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100
  <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
    mx = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
    my = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
    c&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">POINT</span></a>(mx, my)
    r = <a href="RED32" title="RED32"><span style="color:#4593D8;">_RED32</span></a>(c&amp;)
    g = <a href="GREEN32" title="GREEN32"><span style="color:#4593D8;">_GREEN32</span></a>(c&amp;)
    b = <a href="BLUE32" title="BLUE32"><span style="color:#4593D8;">_BLUE32</span></a>(c&amp;)
    a = <a href="ALPHA32" title="ALPHA32"><span style="color:#4593D8;">_ALPHA32</span></a>(c&amp;)
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> mx; my, "R:"; r, "G:"; g, "B:"; b, "A:"; a; "  "
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 2, 2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "HTML Color: <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>" + <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(c&amp;), 6)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; ""
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Use the mouse pointer to get the background RGB of the image to make it transparent with <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a>.</dd></dl>
<p>
<i>Snippet:</i> Creating an image mask to PUT an image over other colored backgrounds. See: <a href="GET_and_PUT_Demo" title="GET and PUT Demo">GET and PUT Demo</a> to run code.
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"> FOR c = 0 TO 59    '60 X 60 area from 0 pixel
   FOR r = 0 TO 59
    IF <a class="mw-selflink selflink"><span style="color:blue;">POINT</span></a>(c, r) = 0 THEN <a href="PSET" title="PSET"><span style="color:blue;">PSET</span></a> (c, r), 15 ELSE PSET (c, r), 0
   NEXT r
 NEXT c
 <a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:blue;">GET</span></a>(0, 0)-(60, 60), Image(1500) ' save mask in an array(indexed above original image).
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> In the procedure all black areas(background) are changed to white for a PUT using AND over other colored objects. The other image colors are changed to black for a PUT of the original image using XOR. The array images can be <a href="BSAVE" title="BSAVE">BSAVEd</a> for later use. <b>QB64 can also</b> <a href="PUT" title="PUT">PUT</a><b> a full screen 12 image from an array directly into a</b> <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> <b>file.</b></dd></dl>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a></li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li>
<li><a href="ThirtyTwoBit_MEM_SUB" title="ThirtyTwoBit MEM SUB">ThirtyTwoBit MEM SUB</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMGET" title="MEMGET">_MEMGET</a></li>
<li><a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Creating_Sprite_Masks" title="Creating Sprite Masks">Creating Sprite Masks</a>, <a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031651
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.066 seconds
Real time usage: 0.085 seconds
Preprocessor visited node count: 827/1000000
Post‐expand include size: 5151/2097152 bytes
Template argument size: 950/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   46.238      1 -total
 16.92%    7.824      3 Template:CodeEnd
 13.85%    6.404     76 Template:Cl
  6.14%    2.837      1 Template:PageSyntax
  5.62%    2.599      1 Template:Small
  5.36%    2.480      1 Template:OutputStart
  5.12%    2.367      1 Template:Text
  5.03%    2.326      2 Template:CodeStart
  4.98%    2.304      1 Template:PageParameters
  4.70%    2.174      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:232-0!canonical and timestamp 20240715031651 and revision id 8665.
 -->
</div>
</div>
</div>
</div>
</body>
</html>