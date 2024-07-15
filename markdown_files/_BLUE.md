<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BLUE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BLUE rootpage-BLUE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BLUE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_BLUE</a> function returns the palette intensity or the blue component intensity of a 32-bit image color.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>blueintensity&amp;</i> = <a class="mw-selflink selflink">_BLUE</a>(<i>rgbaColorIndex&amp;</i>[, <i>imageHandle&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>rgbaColorIndex&amp;</i> is the <i>RGBA</i> color value or palette index of the color to retrieve the blue component intensity from.</li>
<li>The <a href="LONG" title="LONG">LONG</a> intensity value returned ranges from 0 (no intensity, not present) to 255 (full intensity).</li>
<li>If <i>imageHandle&amp;</i> specifies a 32-bit color image, <i>rgbaColorIndex&amp;</i> is interpreted as a 32-bit <i>RGBA</i> color value.</li>
<li>If <i>imageHandle&amp;</i> specifies an image that uses a palette, <i>rgbaColorIndex&amp;</i> is interpreted as a palette index.</li>
<li>If <i>imageHandle&amp;</i> is not specified, it is assumed to be the current write page.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error will occur.</li>
<li>If <i>rgbaColorIndex&amp;</i> is outside the range of valid indexes for a given image mode, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error occurs.</li>
<li>Uses index parameters passed by the <a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a> or <a href="RGBA32" title="RGBA32">_RGBA32</a> funtions.</li>
<li>An image handle is optional.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See the example for <a href="POINT" title="POINT">POINT</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RED" title="RED">_RED</a>, <a href="GREEN" title="GREEN">_GREEN</a></li>
<li><a href="RGB" title="RGB">_RGB</a>, <a href="RGB32" title="RGB32">RGB32</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714200850
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.023 seconds
Preprocessor visited node count: 60/1000000
Post‐expand include size: 775/2097152 bytes
Template argument size: 149/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   13.006      1 -total
 20.24%    2.632     11 Template:Parameter
 20.14%    2.620      1 Template:PageSyntax
 13.95%    1.814      1 Template:PageDescription
 13.46%    1.751      1 Template:PageExamples
 13.06%    1.699      1 Template:PageSeeAlso
 11.72%    1.524      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:58-0!canonical and timestamp 20240714200850 and revision id 5878.
 -->
</div>
</div>
</div>
</div>
</body>
</html>