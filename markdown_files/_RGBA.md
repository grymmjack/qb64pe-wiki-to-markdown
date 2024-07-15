<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RGBA - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RGBA rootpage-RGBA skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RGBA</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RGBA</a> function returns the closest palette index (legacy SCREEN modes) OR the 32-bit <a href="LONG" title="LONG">LONG</a> color value (32-bit screens).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>colorIndex~&amp;</i> = <a class="mw-selflink selflink">_RGBA</a>(<i>red&amp;</i>, <i>green&amp;</i>, <i>blue&amp;</i>, <i>alpha&amp;</i>[, <i>imageHandle&amp;</i>]<b>)</b></dd></dl>
<p>
</p>
<ul><li>The value returned is either the closest color attribute number or a 32-bit <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> color value.</li>
<li><b>Return variable types must be <a href="LONG" title="LONG">LONG</a> or the resulting color may lose the <a href="BLUE" title="BLUE">_BLUE</a> value.</b></li>
<li><i>red&amp;</i> specifies the red component intensity from 0 to 255.</li>
<li><i>green&amp;</i> specifies the green component intensity from 0 to 255.</li>
<li><i>blue&amp;</i> specifies the blue component intensity from 0 to 255.</li>
<li>The <a href="ALPHA" title="ALPHA"><i>alpha&amp;</i></a> value can be set to make the color transparent (0), opaque (255) or somewhere in between.</li>
<li>Parameter values outside of the 0 to 255 range are clipped.</li>
<li>Returns <a href="LONG" title="LONG">LONG</a> 32-bit hexadecimal values from <b>&amp;H00<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b> with varying <a href="ALPHA" title="ALPHA">_ALPHA</a> transparency.</li>
<li>When <a href="LONG" title="LONG">LONG</a> values are <a href="PUT" title="PUT">PUT</a> to file, the ARGB values become BGRA. Use <a href="LEFT$" title="LEFT$">LEFT$</a>(<a href="MKL$" title="MKL$">MKL$</a>(<i>colorIndex~&amp;</i>), 3) to place 3 colors.</li>
<li>If <i>imageHandle&amp;</i> is omitted, the image is assumed to be the current <a href="DEST" title="DEST">destination</a> or <a href="SCREEN" title="SCREEN">SCREEN</a> page.</li>
<li>Allows the blending of pixel colors red, green and blue to create any of 16 million colors.</li>
<li><b>NOTE: Default 32-bit backgrounds are clear black or <a class="mw-selflink selflink">_RGBA</a>(0, 0, 0, 0). Use <a href="CLS" title="CLS">CLS</a> to make the black opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Setting a font's background color alpha to clear to overlay a second text color.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">scrn&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(400, 400, 32)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> scrn&amp;
fnt&amp; = <a href="LOADFONT" title="LOADFONT"><span style="color:#4593D8;">_LOADFONT</span></a>("C:\WINDOWS\FONTS\ARIAL.TTF", 26)
<a href="FONT" title="FONT"><span style="color:#4593D8;">_FONT</span></a> fnt&amp;
X% = 20
Y% = 20
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 255), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 0, 0) 'Foreground set to WHITE background to BLACK
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (X%, Y%), "Hello World"
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0), <a class="mw-selflink selflink"><span style="color:#4593D8;">_RGBA</span></a>(0, 0, 0, 0) 'Foreground set to RED background to TRANSPARENT BLACK
<a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (X% + 2, Y% + 2), "Hello World"
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> allows text or font colors to be alpha blended in 32 bit screens.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RGB" title="RGB">_RGB</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li>
<li><a href="HEX$_32_Bit_Values" title="HEX$ 32 Bit Values">HEX$ 32 Bit Values</a>, <a href="POINT" title="POINT">POINT</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a class="external text" href="http://www.w3schools.com/html/html_colornames.asp" rel="nofollow">Hexadecimal Color Values</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714104837
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 200/1000000
Post‐expand include size: 1790/2097152 bytes
Template argument size: 308/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.774      1 -total
 10.70%    2.330      1 Template:PageSyntax
 10.60%    2.309      6 Template:Text
 10.33%    2.250     13 Template:Cl
  9.62%    2.095     11 Template:Parameter
  8.50%    1.851      1 Template:PageExamples
  8.46%    1.841      1 Template:CodeEnd
  8.31%    1.810      1 Template:CodeStart
  8.25%    1.797      1 Template:Small
  7.94%    1.729      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:228-0!canonical and timestamp 20240714104837 and revision id 8670.
 -->
</div>
</div>
</div>
</div>
</body>
</html>