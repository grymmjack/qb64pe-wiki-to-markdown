<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RGB - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RGB rootpage-RGB skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RGB</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RGB</a> function returns the closest palette attribute index (legacy SCREEN modes) OR the <a href="LONG" title="LONG">LONG</a> 32-bit color value (32-bit screens).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>colorIndex~&amp;</i> = <a class="mw-selflink selflink">_RGB</a>(<i>red&amp;</i>, <i>green&amp;</i>, <i>blue&amp;</i>[, <i>imageHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The value returned is either the closest color attribute number or a 32-bit <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> color value.</li>
<li><b>Return variable types must be <a href="LONG" title="LONG">LONG</a> or resulting color may lose the <a href="BLUE" title="BLUE">_BLUE</a> value.</b></li>
<li><i>red&amp;</i> specifies the red component intensity from 0 to 255.</li>
<li><i>green&amp;</i> specifies the green component intensity from 0 to 255.</li>
<li><i>blue&amp;</i> specifies the blue component intensity from 0 to 255.</li>
<li>Intensity values outside the valid range are clipped.</li>
<li>Returns <a href="LONG" title="LONG">LONG</a> 32-bit hexadecimal values from <b>&amp;HFF<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b>, always with full <a href="ALPHA" title="ALPHA">_ALPHA</a>.</li>
<li>When <a href="LONG" title="LONG">LONG</a> values are <a href="PUT" title="PUT">PUT</a> to file, the ARGB values become BGRA. Use <a href="LEFT$" title="LEFT$">LEFT$</a>(<a href="MKL$" title="MKL$">MKL$</a>(<i>colorIndex~&amp;</i>), 3) to place 3 colors.</li>
<li>If the <i>imageHandle&amp;</i> is omitted the image is assumed to be the current <a href="DEST" title="DEST">destination</a> or <a href="SCREEN" title="SCREEN">SCREEN</a> page.</li>
<li>Colors returned are always opaque as the transparency value is always 255. Use <a href="ALPHA" title="ALPHA">_ALPHA</a> or <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> to change it.</li>
<li><b>NOTE: Default 32-bit backgrounds are clear black or <a href="RGBA" title="RGBA">_RGBA</a>(0, 0, 0, 0). Use <a href="CLS" title="CLS">CLS</a> to make the black opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Converting the color port RGB intensity palette values 0 to 63 to 32 bit hexadecimal values.
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
  hex32$(attribute) = "<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(red, grn, blu))   'always returns the 32 bit value
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> attribute
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a>" + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_RGB</span></a>(red, grn, blu)) + " = " + hex32$(attribute)  'closest attribute
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
<dl><dd><i>Note:</i> This procedure also shows how the returns from <a class="mw-selflink selflink">_RGB</a> and <a href="RGB32" title="RGB32">_RGB32</a> differ in a non-32 bit screen mode.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a>, <a href="POINT" title="POINT">POINT</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a class="external text" href="http://www.w3schools.com/html/html_colornames.asp" rel="nofollow">Hexadecimal Color Values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062435
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.056 seconds
Preprocessor visited node count: 405/1000000
Post‐expand include size: 3404/2097152 bytes
Template argument size: 1173/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 15/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.167      1 -total
 11.34%    3.762     21 Template:Text
 10.01%    3.320      1 Template:PageDescription
  9.44%    3.132     21 Template:Cl
  7.82%    2.592      1 Template:CodeEnd
  7.42%    2.460      1 Template:PageExamples
  7.41%    2.458      1 Template:CodeStart
  7.15%    2.372      1 Template:PageSyntax
  6.81%    2.259     10 Template:Parameter
  6.51%    2.158      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:226-0!canonical and timestamp 20240715062435 and revision id 8668.
 -->
</div>
</div>
</div>
</div>
</body>
</html>