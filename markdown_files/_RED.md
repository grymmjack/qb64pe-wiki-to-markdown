<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RED rootpage-RED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RED</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RED</a> function returns the palette index or the red component intensity of a 32-bit image color.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>redIntensity&amp;</i> = <a class="mw-selflink selflink">_RED</a>(<i>rgbaColorIndex&amp;</i>[, <i>imageHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>rgbaColorIndex&amp;</i> is the <i>RGBA</i> color value or palette index of the color to retrieve the red component intensity from.</li>
<li>The <a href="LONG" title="LONG">LONG</a> intensity value returned ranges from 0 (no intensity, not present) to 255 (full intensity).</li>
<li><i>imageHandle&amp;</i> is optional.</li>
<li>If <i>imageHandle&amp;</i> specifies a 32-bit color image, <i>rgbaColorIndex&amp;</i> is interpreted as a 32-bit <i>RGBA</i> color value.</li>
<li>If <i>imageHandle&amp;</i> specifies an image that uses a palette, <i>rgbaColorIndex&amp;</i> is interpreted as a palette index.</li>
<li>If <i>imageHandle&amp;</i> is not specified, it is assumed to be the current write page.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error occurs.</li>
<li>If <i>rgbaColorIndex&amp;</i> is outside the range of valid indexes for a given image mode, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error occurs.</li>
<li>Uses index parameters passed by the <a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a> or <a href="RGBA32" title="RGBA32">_RGBA32</a> functions.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See the example in <a href="POINT" title="POINT">POINT</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GREEN" title="GREEN">_GREEN</a>, <a href="BLUE" title="BLUE">_BLUE</a></li>
<li><a href="RGB" title="RGB">_RGB</a>, <a href="RGB32" title="RGB32">RGB32</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062431
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 64/1000000
Post‐expand include size: 790/2097152 bytes
Template argument size: 160/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.849      1 -total
 18.95%    3.003      1 Template:PageNavigation
 16.89%    2.677     12 Template:Parameter
 15.49%    2.455      1 Template:PageSyntax
 14.01%    2.221      1 Template:PageDescription
 13.31%    2.109      1 Template:PageSeeAlso
 13.22%    2.096      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:217-0!canonical and timestamp 20240715062431 and revision id 254.
 -->
</div>
</div>
</div>
</div>
</body>
</html>