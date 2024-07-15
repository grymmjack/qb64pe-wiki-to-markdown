<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_COPYPALETTE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COPYPALETTE rootpage-COPYPALETTE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_COPYPALETTE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_COPYPALETTE</a> statement copies the color palette intensities from one 4 or 8 BPP image to another image or a <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page using 256 or less colors.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_COPYPALETTE</a> [<i>sourceImageHandle&amp;</i>[, <i>destinationImageHandle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Palette Intensity settings are <b>not</b> used by 24/32 bit images. Use only with 4 or 8 BPP images.</li>
<li><a href="PIXELSIZE" title="PIXELSIZE">_PIXELSIZE</a> function returns 1 to indicate that _COPYPALETTE can be used. 4 indicates 24/32 bit images.</li>
<li>If <i>sourceImageHandle&amp;</i> is omitted, it is assumed to be the current read page.</li>
<li>If <i>destinationImageHandle&amp;</i> is omitted, it is assumed to be the current write page.</li>
<li>If either of the images specified by <i>sourceImageHandle&amp;</i> or <i>destinationImageHandle&amp;</i> do not use a palette, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error is returned.</li>
<li>If either <i>sourceImageHandle&amp;</i> or <i>destinationImageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error is returned.</li>
<li>When loading 4 or 8 BPP image files, it is necessary to adopt the color palette of the image or it may not have the correct colors!</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See the example in <a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="PIXELSIZE" title="PIXELSIZE">_PIXELSIZE</a></li>
<li><a href="PALETTECOLOR" title="PALETTECOLOR">_PALETTECOLOR</a>, <a href="PALETTECOLOR_(function)" title="PALETTECOLOR (function)">_PALETTECOLOR (function)</a></li>
<li><a href="PALETTE" title="PALETTE">PALETTE</a>, <a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062307
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.022 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 48/1000000
Post‐expand include size: 778/2097152 bytes
Template argument size: 164/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.016      1 -total
 30.14%    6.635      1 Template:PageExamples
 16.97%    3.737      1 Template:PageSyntax
 15.62%    3.438      1 Template:PageSeeAlso
 12.29%    2.706      8 Template:Parameter
 11.50%    2.532      1 Template:PageNavigation
  8.92%    1.963      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:105-0!canonical and timestamp 20240715062307 and revision id 8657.
 -->
</div>
</div>
</div>
</div>
</body>
</html>