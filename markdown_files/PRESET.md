<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PRESET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRESET rootpage-PRESET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PRESET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>PRESET</b> graphic <a href="SCREEN" title="SCREEN">SCREEN</a> statement turns a pixel at a coordinate to the background color or a designated color attribute.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>PRESET</b> [STEP]<b>(</b><i>column%</i>, <i>row%</i><b>)</b>[, colorAttribute]</dd></dl></dd></dl>
<p>
<i><a href="Parameters" title="Parameters">Parameters</a>:</i>
</p>
<ul><li>Can use <a href="STEP" title="STEP">STEP</a> when relative graphics coordinates are required.</li>
<li><i>column</i> and <i>row</i> coordinates can be literal ot variable <a href="INTEGER" title="INTEGER">INTEGER</a> values which can be offscreen.</li>
<li>If the <i>colorAttribute</i> is omitted, PRESET will use the current <a href="DEST" title="DEST">destination</a> page's <a href="BACKGROUNDCOLOR" title="BACKGROUNDCOLOR">_BACKGROUNDCOLOR</a>.</li></ul>
<p>
<i>Usage:</i>
</p>
<ul><li>Color attributes are limited to those available in the <a href="SCREEN" title="SCREEN">SCREEN</a> mode used. <a href="PSET" title="PSET">PSET</a> can be used to adopt previously used colors.</li>
<li>Any color value other than 0 will be white in monochrome <a href="SCREEN" title="SCREEN">SCREEN</a> modes 2 and 11 where the <a href="COLOR" title="COLOR">COLOR</a> statement cannot be used.</li>
<li>PRESET can invisibly locate other graphics objects like <a href="CIRCLE" title="CIRCLE">CIRCLEs</a> and add color to subsequent graphic objects and <a href="DRAW" title="DRAW">DRAW</a> when used.</li>
<li>The PRESET action can be used in a graphics <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> to produce a color inverted image on any background. See Example 2.</li>
<li>The graphic cursor is set to the center of the program window on program start for <a href="STEP" title="STEP">STEP</a> relative coordinates.</li>
<li><b>PRESET can be used in any graphic screen mode, but cannot be used in the default screen mode 0 as it is text only!</b></li></ul>
<p>
<i>Example 1:</i> Using PRESET to locate a <a href="DRAW" title="DRAW">DRAW</a> statement that draws a box that is bright red.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">SCREEN 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">PRESET</span></a>(100, 100)
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "C12 U20 R20 D20 L20"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="DRAW" title="DRAW">DRAW</a> string required a color designation as PRESET defaulted to the black background color.</dd></dl>
<p>
<i>Example 2:</i> Displays the flags of countries that use simple horizontal or vertical color blocks with a highlighted arrow key menu.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> c$(21), x$(21), gg%(477)
ARRAY
SETUP
SELECTION
TERMINATE
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> ARRAY
c$(1) = "Armenia H040914"
c$(2) = "Austria H041504"
c$(3) = "Belgium V001404"
c$(4) = "Bulgaria H150204"
c$(5) = "Chad V011404"
c$(6) = "C“te D'Ivoire V061502"
c$(7) = "Estonia H090015"
c$(8) = "France V011504"
c$(9) = "Germany H000414"
c$(10) = "Hungary H041502"
c$(11) = "Ireland V021506"
c$(12) = "Italy V021504"
c$(13) = "Lithuania H140204"
c$(14) = "Luxembourg H041509"
c$(15) = "Mali V021404"
c$(16) = "Netherlands H041501"
c$(17) = "Nigeria V021502"
c$(18) = "Romania V091404"
c$(19) = "Russia H150104"
c$(20) = "Sierra Leone H021509"
c$(21) = "Yemen H041500"
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DISPLAY.FLAG (calc%)
f% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(x$(calc%), 2, 2))
s% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(x$(calc%), 4, 2))
t% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(x$(calc%), 6, 2))
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(x$(calc%), 1) = "V" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (120, 225)-(253, 465), f%, BF
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (254, 225)-(385, 465), s%, BF
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (386, 225)-(519, 465), t%, BF
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(x$(calc%), 1) = "H" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (120, 225)-(519, 305), f%, BF
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (120, 306)-(519, 386), s%, BF
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (120, 387)-(519, 465), t%, BF
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SELECTION 'menu selection using arrow keys
x% = 2: y% = 4
DO
  <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> (x% &lt;&gt; prevx% <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> y% &lt;&gt; prevy%) <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> k$ &lt;&gt; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
    k$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    x% = x% + (k$ = (<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "K") <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x% &gt; 1) + <a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(k$ = (<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "M") <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> x% &lt; 3)
    y% = y% + (k$ = (<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "H") <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% &gt; 1) + <a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(k$ = (<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "P") <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> y% &lt; 7)
    calc% = (x% - 1) * 7 + y%: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 14, 18: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> c$(calc%); <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10)
    x1% = 140 + (x% - 1) * 128
    x2% = x1% + <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(c$(calc%)) * 8 + 7
    y1% = 48 + y% * 16
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x1% &lt;&gt; prevx1% <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> y1% &lt;&gt; prevy1% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> g% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(prevx1%, prevy1%), gg%(), <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a>
      <a href="GET_(graphics_statement)" title="GET (graphics statement)"><span style="color:#4593D8;">GET</span></a>(x1%, y1%)-(x2%, y1% + 16), gg%(): g% = 1
      <a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(x1%, y1%), gg%(), <a class="mw-selflink selflink"><span style="color:#4593D8;">PRESET</span></a>
      prevx1% = x1%: prevx2% = x2%: prevy1% = y1%
      DISPLAY.FLAG calc%
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> k$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SETUP
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 6
c% = 1
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x% = 11 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 50 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 16
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> y% = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 7
    x$(c%) = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(c$(c%), 7)
    c$(c%) = <a href="RTRIM$" title="RTRIM$"><span style="color:#4593D8;">RTRIM$</span></a>(<a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(c$(c%), <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(c$(c%)) - 7))
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> y% + 4, x% + 8: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> c$(c%)
    c% = c% + 1
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y%, x%
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 3, 20: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Use the Cursor Keys to Select a Country:"
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (119, 224)-(520, 466), 7, B
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> TERMINATE
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> c% = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 219
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (116 + c%, 29 + c%)-(523 - c%, 469 - c%), 0, B
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Using the <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> PRESET action highlights the menu selection in graphic screen modes by returning a negative image.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1157" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a></li>
<li><a href="CIRCLE" title="CIRCLE">CIRCLE</a>, <a href="LINE" title="LINE">LINE</a>, <a href="PSET" title="PSET">PSET</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061400
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 659/1000000
Post‐expand include size: 5474/2097152 bytes
Template argument size: 981/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.641      1 -total
 25.01%    5.412     91 Template:Cl
 11.08%    2.397      1 Template:PageSyntax
  9.77%    2.114      1 Template:Small
  8.94%    1.935      2 Template:CodeEnd
  8.57%    1.854      2 Template:CodeStart
  7.77%    1.681      1 Template:PageNavigation
  7.45%    1.613      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:436-0!canonical and timestamp 20240715061400 and revision id 8896.
 -->
</div>
</div>
</div>
</div>
</body>
</html>