<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ALPHA32 - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ALPHA32 rootpage-ALPHA32 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ALPHA32</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ALPHA32</a> function returns the alpha transparency level of a 32 bit color value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>alpha&amp;</i> = <a class="mw-selflink selflink">_ALPHA32</a>(<i>color32~&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>color32&amp;</i> is the <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> 32 bit color value used to retrieve the alpha level.
<ul><li>Color values that are set as a <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> always have an alpha level of 0 (transparent).</li>
<li><a href="SETALPHA" title="SETALPHA">_SETALPHA</a> can set any alpha level from 0 (or fully transparent) to 255 (or opaque).</li>
<li>Normal color values that are set by <a href="RGB" title="RGB">_RGB</a> or <a href="RGB32" title="RGB32">_RGB32</a> always have an alpha level of 255 (opaque).</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In 4-bit (16 colors) or 8-bit (256 colors) palette screens the function will return 0.</li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>, <a href="BLUE32" title="BLUE32">_BLUE32</a> and <a class="mw-selflink selflink">_ALPHA32</a> are all equivalent to <a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a> and <a href="ALPHA" title="ALPHA">_ALPHA</a> but they are highly optimized and only accept a 32-bit color (RGBA) value. Using these in your code (opposed to dividing then ANDing 32-bit color values) makes code easy to read.</li>
<li><b>NOTE: 32 bit <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page backgrounds are transparent black or <a href="ALPHA" title="ALPHA">_ALPHA</a> 0. Use <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> or <a href="CLS" title="CLS">CLS</a> for opaque!</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Finding the alpha transparency level in a 32 bit screen using an <a href="RGBA" title="RGBA">_RGBA</a> <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> color value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
clr~&amp; = <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">192</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Color:"</span>; clr~&amp;
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> clr~&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Alpha32:"</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_ALPHA32</span></a>(clr~&amp;)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:#FFFFFF;">Color: 3237937407</span>
<span style="color:#FF00FF;">Alpha32: 192</span>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> The color value is equivalent to <a href="%26H" title="&amp;H">hexadecimal</a> &amp;HC0FF00FF where &amp;HC0 equals 192. <a href="RGB" title="RGB">_RGB</a> alphas are always &amp;HFF(255).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1060" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ALPHA" title="ALPHA">_ALPHA</a>, <a href="SETALPHA" title="SETALPHA">_SETALPHA</a></li>
<li><a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a> <span style="color:#777777;">(set color with alpha)</span></li>
<li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="RED32" title="RED32">_RED32</a>, <a href="GREEN32" title="GREEN32">_GREEN32</a>. <a href="BLUE32" title="BLUE32">_BLUE32</a></li>
<li><a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a>, <a href="CLEARCOLOR_(function)" title="CLEARCOLOR (function)">_CLEARCOLOR (function)</a></li>
<li><a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062237
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.046 seconds
Preprocessor visited node count: 186/1000000
Post‐expand include size: 1784/2097152 bytes
Template argument size: 329/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 18/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.014      1 -total
  9.67%    2.806      3 Template:Parameter
  8.93%    2.591      1 Template:PageDescription
  8.15%    2.366      1 Template:PageSyntax
  7.72%    2.240      1 Template:PageExamples
  7.36%    2.136     12 Template:Text
  7.04%    2.044      1 Template:PageNavigation
  6.78%    1.966      8 Template:Cl
  6.62%    1.922      1 Template:PageParameters
  6.32%    1.835      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:42-0!canonical and timestamp 20240715062237 and revision id 8873.
 -->
</div>
</div>
</div>
</div>
</body>
</html>