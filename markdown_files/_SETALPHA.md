<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SETALPHA - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SETALPHA rootpage-SETALPHA skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SETALPHA</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SETALPHA</a> statement sets the alpha channel transparency level of some or all of the pixels of an image.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SETALPHA</a> <i>alpha&amp;</i>[, <i>color1&amp;</i>][ <a href="TO" title="TO">TO</a> <i>colour2&amp;</i>] [, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>alpha&amp;</i> is the new alpha level to set, ranging from 0 (transparent) to 255 (opaque).</li>
<li><i>color1&amp;</i> designates the 32-bit <a href="LONG" title="LONG">LONG</a> color value or range of color values <i>color1&amp;</i> TO <i>colour2&amp;</i> to set the transparency.</li>
<li>If no color value or range of colors is given, the entire image's alpha is changed, including any <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> settings.</li>
<li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current write page or <a href="DEST" title="DEST">destination</a> image.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In the first syntax, the alpha level of all pixels is set to <i>alpha&amp;</i>.</li>
<li>In the second syntax, the alpha level of all pixels matching the color <i>color1&amp;</i> is set to <i>alpha&amp;</i>.</li>
<li>In the third syntax, the alpha level of all pixels with red, green, blue and alpha channels in the range [<i>color1&amp;</i> TO <i>color2&amp;</i>] are set.</li>
<li>The <a href="ALPHA" title="ALPHA">_ALPHA</a> setting makes a 32-bit color transparent, opaque or something in between. Zero is clear and 255 totally blocks underlying images. Use it to see through backgrounds or image colors.</li>
<li>If <i>alpha&amp;</i> is outside that range, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li>If the image specified by <i>imageHandle&amp;</i> uses a palette, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error will occur.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li><b>NOTE: 32-bit <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page backgrounds are transparent black or <a href="ALPHA" title="ALPHA">_ALPHA</a> 0. Use <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> or <a href="CLS" title="CLS">CLS</a> for opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Using a _SETALPHA color range to fade an image in and out while not affecting the transparent white background.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">main = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> main
<a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_SCREENMOVE</span></a> <a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_MIDDLE</span></a>
Image1&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png") '&lt;&lt;&lt; PNG file with white background to hide
<a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> Image1&amp;
clr~&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(0, 0) 'find background color of image
<a href="CLEARCOLOR" title="CLEARCOLOR"><span style="color:#4593D8;">_CLEARCOLOR</span></a> clr~&amp;, Image1&amp; 'set background color as transparent
topclr~&amp; = clr~&amp; - <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(1, 1, 1, 0)  'get topmost color range just below full white
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> main
a&amp; = 0
d = 1
DO
  <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10 'regulate speed of fade in and out
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> ', <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 0, 0)
  a&amp; = a&amp; + d
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a&amp; = 255 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> d = -d
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_SETALPHA</span></a> a&amp;, 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> topclr~&amp;, Image1&amp; 'affects all colors below bright white
  <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 342), Image1&amp;
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Alpha: "; a&amp;
  <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> a&amp; = 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="POINT" title="POINT">POINT</a> value minus <a href="RGBA" title="RGBA">_RGBA</a>(1, 1, 1, 0) subtracts a small amount from the bright white color value so that the top <a class="mw-selflink selflink">_SETALPHA</a> color range will not affect the <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> transparency of the bright white PNG background.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ALPHA" title="ALPHA">_ALPHA</a>, <a href="ALPHA32" title="ALPHA32">_ALPHA32</a></li>
<li><a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a></li>
<li><a href="CLEARCOLOR_(function)" title="CLEARCOLOR (function)">_CLEARCOLOR (function)</a></li>
<li><a href="BLEND" title="BLEND">_BLEND</a>, <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062448
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.068 seconds
Preprocessor visited node count: 253/1000000
Post‐expand include size: 2133/2097152 bytes
Template argument size: 433/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   43.863      1 -total
 20.51%    8.997      1 Template:PageSeeAlso
 16.39%    7.189      1 Template:CodeEnd
  9.97%    4.373     23 Template:Cl
  7.52%    3.300      1 Template:PageDescription
  6.95%    3.049      1 Template:PageSyntax
  6.95%    3.048      1 Template:PageNavigation
  6.40%    2.806     17 Template:Parameter
  5.54%    2.428      1 Template:CodeStart
  5.39%    2.363      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:324-0!canonical and timestamp 20240715062448 and revision id 6531.
 -->
</div>
</div>
</div>
</div>
</body>
</html>