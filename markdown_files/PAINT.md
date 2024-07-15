<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PAINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PAINT rootpage-PAINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PAINT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">PAINT</a> statement is used to fill a delimited area in a graphic screen mode with color.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">PAINT</a> [<b>STEP</b>] (<i>column%</i>, <i>row%</i>), <i>fillColor</i>[, <i>borderColor%</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Can use the <a href="STEP" title="STEP">STEP</a> keyword for relative coordinate placements. See example 1 below.</li>
<li><i>fillColor</i> is an <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> 32-bit value to paint the inside of an object. Colors are limited to the <a href="SCREEN" title="SCREEN">SCREEN</a> mode used.</li>
<li>Optional <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> 32-bit <i>borderColor%</i> is the color of the border of the shape to be filled when this is different from the fill color.</li>
<li><i>fillColor</i> can be a string made up of a sequence of <a href="CHR$" title="CHR$">CHR$</a> values, each representing a tiling pattern to fill the shape. See Example 3 below.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Graphic <i>column%</i> and <i>row%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> pixel coordinates should be inside of a fully closed "shape", whether it's a rectangle, circle or custom-drawn shape using <a href="DRAW" title="DRAW">DRAW</a>.</li>
<li>If the coordinates passed to the <a class="mw-selflink selflink">PAINT</a> statement are on a pixel that matches the border colors, no filling will occur.</li>
<li>If the shape's border isn't continuous, the "paint" will "leak".</li>
<li>If the shape is not totally closed, every color except the border color may be painted over.</li>
<li><a href="DRAW" title="DRAW">DRAW</a> shapes can be filled using the string "P <i>fillColor</i>, <i>borderColor</i>". Use a "B" blind move to offset from the shape's border.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Painting a <a href="CIRCLE" title="CIRCLE">CIRCLE</a> immediately after it is drawn using <a href="STEP" title="STEP">STEP</a>(0, 0) to paint from the circle's center point.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
x = 200: y = 200
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (x, y), 100, 10
<a class="mw-selflink selflink"><span style="color:#4593D8;">PAINT</span></a> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(0, 0), 2, 10
</pre>
</td></tr></tbody></table>
<dl><dd><i>Results:</i> A circle located at x and y with a bright green border filled in dark green. The last coordinate used was the circle's center point and PAINT used it also with the <a href="STEP" title="STEP">STEP</a> relative coordinates being zero.</dd></dl>
<p>
<i>Example 2:</i> Routine to check a <a href="DRAW" title="DRAW">DRAW</a> string to make sure that the drawn shape is fully closed so that a PAINT does not "leak".
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
drw$ = "C15S20R9D4R6U3R3D3R7U5H3U2R9D3G2D6F1D3F5L10D1G1L4H2L7G2L3H2L3U8L2U5R1BF4"
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(drw$)
  tmp$ = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(drw$, i, 1))
  check = 1
  <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> tmp$
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "U": ver = -1: hor = 0
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "D": ver = 1: hor = 0
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "E": ver = -1: hor = 1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "F": ver = 1: hor = 1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "G": ver = 1: hor = -1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "H": ver = -1: hor = -1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "L": ver = 0: hor = -1
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "R": ver = 0: hor = 1
    <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: check = 0
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> check <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    snum$ = ""
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> j = i + 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> i + 4 'set for up to 4 digits and spaces
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> j &gt; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(drw$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a>
      n$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(drw$, j, 1)
      num = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(n$)
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (num &gt; 47 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> num &lt; 58) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> num = 32 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        snum$ = snum$ + n$
      <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a>
      <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    vertical = vertical + (ver * <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(snum$))
    horizont = horizont + (hor * <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(snum$))
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tmp$, horizont, vertical
  '<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (300, 300): <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> drw$
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> If the <a href="DRAW" title="DRAW">DRAW</a> string is fully closed, the end values should each be 0. In the example, the proper result should be 4, 4 as there is a BF4 offset for PAINT which cannot be on a border. The result is 4, 5 because the shape is not completely closed.</dd></dl>
<p>
<i>Example 3:</i> Tiling using PAINT to create a red brick pattern inside a yellow border:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Row$(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 8)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
   'make red-brick wall
    Row$(1) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FE) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FE)
    Row$(2) = Row$(1)
    Row$(3) = Row$(1)
    Row$(4) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0)
    Row$(5) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>0) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>EF) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>EF)
    Row$(6) = Row$(5)
    Row$(7) = Row$(5)
    Row$(8) = Row$(4)
    Tile$ = Row$(1) + Row$(2) + Row$(3) + Row$(4) + Row$(5) + Row$(6) + Row$(7) + Row$(8)
    <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (59, 124)-(581, 336), 14, B 'yellow box border to paint inside
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PAINT</span></a> (320, 240), Tile$, 14 'paints brick tiles within yellow border
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Generating a tiling pattern for PAINT from <a href="DATA" title="DATA">DATA</a> statements:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">ptndata:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "c4444444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "c4444444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "cccccccc"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "444c4444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "444c4444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "444c4444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "cccccccc"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "c4444444"
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> ---
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> ptndata: ptn$ = loadpattern$
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 7
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "c15l15f10g10r30g10f10l50u80r100m160,100"
<a class="mw-selflink selflink"><span style="color:#4593D8;">PAINT</span></a> (160, 90), ptn$, 15
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> loadpattern$
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> quad(0 TO 3) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
    res$ = ""
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> row$
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(row$, 3) = "---" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 7
            pixel = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>("&amp;h" + <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(row$, x + 1, 1))
            <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> bit = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> pixel <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> 2 ^ bit <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                    quad(bit) = quad(bit) <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> (2 ^ (7 - x))
                <a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a>
            <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3
            res$ = res$ + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(quad(i))
            quad(i) = 0
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
    loadpattern$ = res$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><dl><dd><i>Code provided by collaborator <a class="external free" href="https://github.com/NEONTEC75" rel="nofollow">https://github.com/NEONTEC75</a></i></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PSET" title="PSET">PSET</a>, <a href="PRESET" title="PRESET">PRESET</a></li>
<li><a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="LINE" title="LINE">LINE</a>, <a href="DRAW" title="DRAW">DRAW</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="CHR$" title="CHR$">CHR$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714184056
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.059 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 937/1000000
Post‐expand include size: 7124/2097152 bytes
Template argument size: 1144/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.676      1 -total
 21.44%    6.793    123 Template:Cl
  7.36%    2.331      1 Template:PageSyntax
  7.26%    2.299      4 Template:CodeEnd
  6.79%    2.151      4 Template:CodeStart
  6.67%    2.114      1 Template:PageSeeAlso
  6.17%    1.953     11 Template:Parameter
  6.14%    1.945      1 Template:PageNavigation
  5.70%    1.805      1 Template:PageExamples
  5.42%    1.717      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:574-0!canonical and timestamp 20240714184056 and revision id 8158.
 -->
</div>
</div>
</div>
</div>
</body>
</html>