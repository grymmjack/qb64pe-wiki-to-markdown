<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ALPHA - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ALPHA rootpage-ALPHA skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ALPHA</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ALPHA</a> function returns the alpha channel transparency level of a color value used on a screen page or image.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result&amp;</i> = <a class="mw-selflink selflink">_ALPHA</a>(<i>color~&amp;</i> [, <i>imageHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current write page. Invalid handles will create <a href="ERROR_Codes" title="ERROR Codes">Illegal function call</a> errors.</li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 32 bit <a href="SCREEN" title="SCREEN">SCREEN</a> modes will always use an <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> <i>color~&amp;</i> value.
<ul><li>Color values that are set as a <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> always have an alpha level of 0 (transparent).</li>
<li><a href="SETALPHA" title="SETALPHA">_SETALPHA</a> can set any alpha level from 0 (or fully transparent) to 255 (or opaque).</li>
<li>Normal color values that are set by <a href="RGB" title="RGB">_RGB</a> or <a href="RGB32" title="RGB32">_RGB32</a> always have an alpha level of 255(opaque).</li></ul></li>
<li>In 4 (16 color) or 8 (256 color) bit palette screens the function will always return 255.</li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>, <a href="BLUE32" title="BLUE32">_BLUE32</a> and <a href="ALPHA32" title="ALPHA32">_ALPHA32</a> are all equivalent to <a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a> and <a class="mw-selflink selflink">_ALPHA</a> but they are highly optimized and only accept a 32-bit color (B8:G8:R8:A8). Using them (opposed to dividing then ANDing 32-bit color values manually) makes code easy to read.</li>
<li><b>NOTE: 32 bit <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page backgrounds are transparent black or <a class="mw-selflink selflink">_ALPHA</a> 0. Use <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> or <a href="CLS" title="CLS">CLS</a> for opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Alpha transparency levels are always 255 in 4 or 8 bit screen modes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
clr~&amp; = <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">192</span>) <span style="color:#919191;">'returns closest palette color attribute</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Color:"</span>; clr~&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> clr~&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Alpha:"</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALPHA</span></a>(clr~&amp;)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#FFFFFF;">Color 36</span>
<span style="color:#FF00FF;">Alpha: 255</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="RGBA" title="RGBA">_RGBA</a> cannot change the <a class="mw-selflink selflink">_ALPHA</a> level. <a href="ALPHA32" title="ALPHA32">_ALPHA32</a> would return 0 on any non-32 bit image or page.</dd></dl>
<p><i>Example 2:</i> Finding the transparency of a 32 bit screen mode's background before and after <a href="CLS" title="CLS">CLS</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
BG&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Alpha ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALPHA</span></a>(BG&amp;); <span style="color:#FFB100;">"Press a key to use CLS!"</span>
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
BG&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"CLS Alpha ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALPHA</span></a>(BG&amp;)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">CLS Alpha = 255   </pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Set the ALPHA value to 255 using <a href="CLS" title="CLS">CLS</a> to make the background opaque when overlaying pages.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ALPHA32" title="ALPHA32">_ALPHA32</a>, <a href="SETALPHA" title="SETALPHA">_SETALPHA</a></li>
<li><a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a> <span style="color:#777777;">(set color with alpha)</span></li>
<li><a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a>, <a href="CLEARCOLOR_(function)" title="CLEARCOLOR (function)">_CLEARCOLOR (function)</a></li>
<li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>. <a href="BLUE32" title="BLUE32">_BLUE32</a></li>
<li><a href="CLS" title="CLS">CLS</a>, <a href="COLOR" title="COLOR">COLOR</a>, <a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200838
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.105 seconds
Preprocessor visited node count: 338/1000000
Post‐expand include size: 2854/2097152 bytes
Template argument size: 636/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 103/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   75.810      1 -total
 17.48%   13.249      1 Template:PageDescription
 15.30%   11.598     22 Template:Text
 13.68%   10.374      1 Template:PageExamples
  6.72%    5.095      2 Template:OutputEnd
  5.67%    4.297      2 Template:CodeEnd
  5.32%    4.034     17 Template:Cl
  5.06%    3.837      2 Template:CodeStart
  4.95%    3.755      2 Template:OutputStart
  4.85%    3.677      4 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:41-0!canonical and timestamp 20240714200838 and revision id 8256.
 -->
</div>
</div>
</div>
</div>
</body>
</html>