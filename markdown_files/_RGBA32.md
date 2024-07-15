<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RGBA32 - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RGBA32 rootpage-RGBA32 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RGBA32</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RGBA32</a> function returns the 32-bit <i>RGBA</i> color value with the specified red, green, blue and alpha component intensities.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>color32value~&amp;</i> = <a class="mw-selflink selflink">_RGBA32</a>(<i>red&amp;</i>, <i>green&amp;</i>, <i>blue&amp;</i>, <i>alpha&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The value returned is a 32-bit <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> color value.</li>
<li><b>Return variable types must be <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> or resulting color may lose the <a href="BLUE" title="BLUE">_BLUE</a> value.</b></li>
<li><i>red&amp;</i> specifies the red component intensity from 0 to 255.</li>
<li><i>green&amp;</i> specifies the green component intensity from 0 to 255.</li>
<li><i>blue&amp;</i> specifies the blue component intensity from 0 to 255.</li>
<li><i>alpha&amp;</i> specifies the <a href="ALPHA" title="ALPHA"><i>alpha</i></a> component transparency value from 0 (fully transparent) to 255 (opaque).</li>
<li>Alpha or intensity values outside of the valid range of 0 to 255 are clipped.</li>
<li>Returns <a href="LONG" title="LONG">LONG</a> 32-bit hexadecimal values from <b>&amp;H00<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b> with varying <a href="ALPHA" title="ALPHA">_ALPHA</a> transparency.</li>
<li>When <a href="LONG" title="LONG">LONG</a> values are <a href="PUT" title="PUT">PUT</a> to file, the ARGB values become BGRA. Use <a href="LEFT$" title="LEFT$">LEFT$</a>(<a href="MKL$" title="MKL$">MKL$</a>(<i>color32value~&amp;</i>), 3) to place 3 colors.</li>
<li><b>NOTE: Default 32-bit backgrounds are clear black or <a href="RGBA" title="RGBA">_RGBA</a>(0, 0, 0, 0). Use <a href="CLS" title="CLS">CLS</a> to make the black opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Changing the <a href="ALPHA" title="ALPHA">ALPHA</a> value to fade an image in and out using a 32 bit PNG image.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(600, 400, 32)
img&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png")  'use any 24/32 bit image
'Turn off auto display
<a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
' Fade in
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 255 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -5
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 20                          'control fade speed
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0)-(600, 400), img&amp;
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (0, 0)-(600, 400), <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(0, 0, 0, i%), BF 'decrease black box transparency
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
' Fade out
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i% = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 255 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 5
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 20                          'control fade speed
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0)-(600, 400), img&amp;
  <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (0, 0)-(600, 400), <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(0, 0, 0, i%), BF 'increase black box transparency
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB" title="RGB">_RGB</a></li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>, <a href="BLUE32" title="BLUE32">_BLUE32</a></li>
<li><a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a>, <a href="POINT" title="POINT">POINT</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a class="external text" href="http://www.w3schools.com/html/html_colornames.asp" rel="nofollow">Hexadecimal Color Values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034447
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 269/1000000
Post‐expand include size: 2322/2097152 bytes
Template argument size: 394/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.149      1 -total
 11.04%    3.218     23 Template:Cl
  9.73%    2.837      1 Template:CodeEnd
  8.45%    2.463      1 Template:PageSyntax
  8.26%    2.408      1 Template:Small
  8.05%    2.345      1 Template:PageNavigation
  7.75%    2.259      6 Template:Text
  7.70%    2.246      1 Template:PageSeeAlso
  7.65%    2.231      1 Template:CodeStart
  7.65%    2.229      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:229-0!canonical and timestamp 20240715034447 and revision id 8671.
 -->
</div>
</div>
</div>
</div>
</body>
</html>