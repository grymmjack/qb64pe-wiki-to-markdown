<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RGB32 - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RGB32 rootpage-RGB32 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RGB32</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RGB32</a> function returns the 32-bit <i>RGBA</i> color value with specified red, green and blue component intensities and optional alpha.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<p><i>Original syntax</i>:
</p>
<dl><dd><i>color32value~&amp;</i> = <a class="mw-selflink selflink">_RGB32</a>(<i>red&amp;</i>, <i>green&amp;</i>, <i>blue&amp;</i>)</dd></dl>
<p><i>Alternative Syntax 2</i>:
</p>
<dl><dd><i>color32value~&amp;</i> = <a class="mw-selflink selflink">_RGB32</a>(<i>red&amp;</i>, <i>green&amp;</i>, <i>blue&amp;</i>, <i>alpha&amp;</i>)</dd></dl>
<p><i>Alternative Syntax 3</i>:
</p>
<dl><dd><i>color32value~&amp;</i> = <a class="mw-selflink selflink">_RGB32</a>(<i>intensity&amp;</i>, <i>alpha&amp;</i>)</dd></dl>
<p><i>Alternative Syntax 4</i>:
</p>
<dl><dd><i>color32value~&amp;</i> = <a class="mw-selflink selflink">_RGB32</a>(<i>intensity&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>red&amp;</i> specifies the red <a href="LONG" title="LONG">LONG</a> component intensity from 0 to 255.</li>
<li><i>green&amp;</i> specifies the green <a href="LONG" title="LONG">LONG</a> component intensity from 0 to 255.</li>
<li><i>blue&amp;</i> specifies the blue <a href="LONG" title="LONG">LONG</a> component intensity from 0 to 255.</li>
<li><i>alpha&amp;</i> specifies the alpha <a href="LONG" title="LONG">LONG</a> component from 0 to 255.</li>
<li><i>intensity&amp;</i> specifies the red, green and blue <a href="LONG" title="LONG">LONG</a> components intensity from 0 to 255 simultaneously, to generate a shade of gray.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The value returned is always a 32-bit <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> color value, as is the <a href="POINT" title="POINT">POINT</a> value.</li>
<li><b>Return variable types must be <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> or <a href="LONG" title="LONG">LONG</a>, otherwise resulting color may lose the <a href="BLUE" title="BLUE">_BLUE</a> value.</b></li>
<li>Parameter values outside of the 0 to 255 range are clipped.</li>
<li>Returns <a href="LONG" title="LONG">LONG</a> 32 bit hexadecimal values from <b>&amp;H00<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b>.</li>
<li>When <a href="LONG" title="LONG">LONG</a> values are <a href="PUT" title="PUT">PUT</a> to file, the ARGB values become BGRA. Use <a href="LEFT$" title="LEFT$">LEFT$</a>(<a href="MKL$" title="MKL$">MKL$</a>(<i>color32value~&amp;</i>), 3) to place 3 colors.</li>
<li><b>NOTE: Default 32-bit backgrounds are clear black or <a class="mw-selflink selflink">_RGB32</a>(0, 0). Use <a href="CLS" title="CLS">CLS</a> to make the black opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li>Alternative syntaxes available with <b>version 1.3 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Converting the color port RGB intensity palette values 0 to 63 to 32 bit hexadecimal values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> hex32$(15)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> attribute = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15
  <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C7, attribute      'set color attribute to read
  red = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 4      'multiply by 4 to convert intensity to 0 to 255 RGB values
  grn = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 4
  blu = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>3C9) * 4
  hex32$(attribute) = "<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(red, grn, blu))   'always returns the 32 bit value
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> attribute
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a>" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#0000A8;">COLOR 1 = &amp;HFF0000A8</span>
<span style="color:#00A800;">COLOR 2 = &amp;HFF00A800</span>
<span style="color:#00A8A8;">COLOR 3 = &amp;HFF00A8A8</span>
<span style="color:#A80000;">COLOR 4 = &amp;HFFA80000</span>
<span style="color:#A800A8;">COLOR 5 = &amp;HFFA800A8</span>
<span style="color:#A85400;">COLOR 6 = &amp;HFFA85400</span>
<span style="color:#A8A8A8;">COLOR 7 = &amp;HFFA8A8A8</span>
<span style="color:#545454;">COLOR 8 = &amp;HFF545454</span>
<span style="color:#5454FC;">COLOR 9 = &amp;HFF5454FC</span>
<span style="color:#54FC54;">COLOR 10 = &amp;HFF54FC54</span>
<span style="color:#54FCFC;">COLOR 11 = &amp;HFF54FCFC</span>
<span style="color:#FC5454;">COLOR 12 = &amp;HFFFC5454</span>
<span style="color:#FC54FC;">COLOR 13 = &amp;HFFFC54FC</span>
<span style="color:#FCFC54;">COLOR 14 = &amp;HFFFCFC54</span>
<span style="color:#FCFCFC;">COLOR 15 = &amp;HFFFCFCFC</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> This procedure also shows how the returns from <a href="RGB" title="RGB">_RGB</a> and <a class="mw-selflink selflink">_RGB32</a> differ in a non-32 bit screen mode.</dd></dl>
<p>
<i>Example 2:</i> Working with 32 bit colors.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(0, 0, 128) 'deep blue background
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (100, 100)-(540, 380), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0), BF ' a red box
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (200, 200)-(440, 280), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 255, 0), BF ' a green box
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> 'Just so we can see our pretty background before we print anything on it.
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(255, 255, 255), 0 'White on NO BACKGROUND
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This is just a whole bunch of happy nothing!  Happy World!!"
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>:
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(0, 0, 0) 'And here, we're going with NO <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> text, with a BLACK background.
'Notice how this doesn't change the color on the screen at all, where the text is, but does toss a black background to it.
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , 15: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "NOTICE HOW OUR 0 <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> WORKS?"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , 15: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "NEAT, HUH?"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
SYSTEM
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Comparing the output of the new _RGB32 syntaxes (starting with version 1.3) and their equivalents in previous versions.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(400, 400, 32)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(255, 255, 255)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "White"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(255)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "White, too, but with less typing"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(80, 80, 80)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Dark gray"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(80)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Same gray, but with less typing"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(255, 255, 255, 120)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "White with alpha of 120 (out of 255)"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(255, 120)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "White with alpha of 120 - but with less typing"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(255, 0, 255, 110)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Magenta, 110 alpha"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB32</span></a>(255, 0, 255, 110)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Magenta too, 110 alpha - but with less typing"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RGBA32" title="RGBA32">_RGBA32</a>, <a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a></li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>, <a href="BLUE32" title="BLUE32">_BLUE32</a></li>
<li><a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a></li>
<li><a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a class="external text" href="http://www.w3schools.com/html/html_colornames.asp" rel="nofollow">Hexadecimal Color Values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154233
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.079 seconds
Preprocessor visited node count: 861/1000000
Post‐expand include size: 6827/2097152 bytes
Template argument size: 1882/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 15/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.142      1 -total
 13.06%    5.113     78 Template:Cl
 11.59%    4.537      3 Template:CodeStart
  6.35%    2.486     21 Template:Text
  5.79%    2.267      1 Template:PageSyntax
  5.34%    2.089      1 Template:PageAvailability
  5.25%    2.054     20 Template:Parameter
  4.44%    1.739      1 Template:PageSeeAlso
  4.17%    1.631      1 Template:PageParameters
  4.12%    1.614      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:227-0!canonical and timestamp 20240714154233 and revision id 8669.
 -->
</div>
</div>
</div>
</div>
</body>
</html>