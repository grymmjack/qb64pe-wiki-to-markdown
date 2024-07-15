<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PSET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PSET rootpage-PSET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PSET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>PSET</b> grahics <a href="SCREEN" title="SCREEN">SCREEN</a> statement sets a pixel to a coordinate with a default or designated color attribute.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>PSET</b> [STEP]<b>(</b><i>column%</i>, <i>row%</i><b>)</b>[, <i>colorAttribute</i>]</dd></dl></dd></dl>
<p>
<i><a href="Parameters" title="Parameters">Parameters</a>:</i>
</p>
<ul><li>Can use <a href="STEP" title="STEP">STEP</a> relative graphics coordinates from a previous graphic object.</li>
<li><i>Column</i> and <i>row</i> can be literal or variable <a href="INTEGER" title="INTEGER">INTEGER</a> coordinates values which can be offscreen.</li>
<li>If the <i>colorAttribute</i> is omitted, PSET will use the current <a href="DEST" title="DEST">destination</a> page's _DEFAULTCOLOR.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li><i>Color attributes</i> are limited to the SCREEN mode used. Any color value other than 0 will be white in <a href="SCREEN" title="SCREEN">SCREENs</a> 2 or 11.</li>
<li>PSET can locate other graphics objects and color <a href="DRAW" title="DRAW">DRAW</a> statements.</li>
<li>The PSET action can be used in a graphics <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> to produce an identical image on any background.</li>
<li>The graphic cursor is set to the center of the program window on program start for <a href="STEP" title="STEP">STEP</a> relative coordinates.</li>
<li><b>PSET can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only! (Or in any _NEWIMAGE(x, y, 0) screens which are text only as well.)</b></li></ul>
<p>
<i>Example:</i> Using PSET to locate and color a <a href="DRAW" title="DRAW">DRAW</a> statement.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">SCREEN 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a>(100, 100), 12
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "U20 R20 D20 L20"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Screen results:</i> A drawn box that is bright red.</dd></dl>
<p>
<i>Example 2:</i> Magnifying a box portion of a Mandelbrot image with PSET
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFSTR" title="DEFSTR"><span style="color:#4593D8;">DEFSTR</span></a> A-Z
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> red(15) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, green(15) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, blue(15) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15: <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> red(i): <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15: <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> green(i): <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15: <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> blue(i): <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15: <a href="PALETTE" title="PALETTE"><span style="color:#4593D8;">PALETTE</span></a> i, 65536 * blue(i) + 256&amp; * green(i) + red(i): <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 0,63,63,63,63,63,31, 0, 0,31,31,31,47,63,63,63
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 0, 0,15,31,47,63,63,63,63,31,15, 0, 0, 0, 0, 0
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 0, 0, 0, 0, 0, 0, 0, 0,31,63,63,63,63,63,42,21
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> dmag <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, dlogmag <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, mag <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> dx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, dy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> mx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, my <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, mz <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
dmag = 16
mag = 1
a = -.75
b = 0
DO
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> limitx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, limit <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> inc <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, left <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, top <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
  limitx = 150 * (<a href="LOG" title="LOG"><span style="color:#4593D8;">LOG</span></a>(mag) + 1)
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> limitx &gt; 32767 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> limitx = 32767
  limit = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(limitx)
  inc = .004 / mag
  left = a - inc * 319
  top = b + inc * 239
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> yy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, xx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, z <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> yy = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 479
    y = top - inc * yy
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> xx = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 639
        x = left + inc * xx
        z = mandel(x, y, limit)
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> z &lt; limit <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a> (xx, yy), 1 + z <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 15
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  mz = 0
  <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> readmouse(mx, my, mz)
  DO
    dx = 319 \ dmag
    dy = 239 \ dmag
    <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> readmouse(mx, my, mz)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> mz <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> rectangle(mx - dx, my - dy, mx + dx, my + dy)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> t <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
    t = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
    <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> t = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
      key$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
      <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> key$
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
          <a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(72)
          dmag = dmag \ 2
          <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> dmag &lt; 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dmag = 2
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(80)
          dmag = dmag * 2
          <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> dmag &gt; 128 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dmag = 128
      <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
    <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> rectangle(mx - dx, my - dy, mx + dx, my + dy)
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  a = a + inc * (mx - 319): b = b - inc * (my - 239)
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (mz = 1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> mag = dmag * mag <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> mag = mag / dmag
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (mag &lt; 1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> mag = 1
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> mandel% (x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, limit <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>)
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>, t <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  n = 0: a = 0: b = 0
  DO
    t = a * a - b * b + x
    b = 2 * a * b + y: a = t
    n = n + 1
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> a * a + b * b &gt; 4 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> n &gt; limit
  mandel = n
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> readmouse (x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, z <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>)
z=0
DO
if <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = z <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> 1
if <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(2) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = z <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> 2
if <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(3) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> z = z <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> 4
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>=0
x=<a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>
y=<a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> rectangle (x1 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, y1 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, x2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, y2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>)
  <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, j <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = x1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> x2
    j = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(i, y1)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a> (i, y1), j <a href="XOR_(boolean)" title="XOR (boolean)"><span style="color:#4593D8;">XOR</span></a> 15
    j = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(i, y2)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a> (i, y2), j <a href="XOR_(boolean)" title="XOR (boolean)"><span style="color:#4593D8;">XOR</span></a> 15
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = y1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> y2
    j = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(x1, i)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a> (x1, i), j <a href="XOR_(boolean)" title="XOR (boolean)"><span style="color:#4593D8;">XOR</span></a> 15
    j = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(x2, i)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PSET</span></a> (x2, i), j <a href="XOR_(boolean)" title="XOR (boolean)"><span style="color:#4593D8;">XOR</span></a> 15
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> Left click, to zoom in on the rectangle. Right click, to zoom out. Up arrow makes the rectangle bigger and down arrow makes the rectangle smaller.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRESET" title="PRESET">PRESET</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="LINE" title="LINE">LINE</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="POINT" title="POINT">POINT</a></li>
<li><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031655
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.064 seconds
Real time usage: 0.073 seconds
Preprocessor visited node count: 1520/1000000
Post‐expand include size: 11575/2097152 bytes
Template argument size: 2039/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.118      1 -total
 31.87%    8.643    214 Template:Cl
  7.27%    1.971      1 Template:PageSyntax
  6.99%    1.896      1 Template:Small
  5.81%    1.575      2 Template:CodeStart
  5.72%    1.550      1 Template:PageSeeAlso
  5.66%    1.535      1 Template:PageNavigation
  5.42%    1.471      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:435-0!canonical and timestamp 20240715031655 and revision id 8057.
 -->
</div>
</div>
</div>
</div>
</body>
</html>