<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FREEIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FREEIMAGE rootpage-FREEIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FREEIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_FREEIMAGE</b> statement releases the designated file image created by the <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a> functions from memory when they are no longer needed.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_FREEIMAGE</a> [<i>handle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>handle&amp;</i> is omitted, the current destination image is freed from memory.</li>
<li>Freeing the destination image or source image will result in the display page being selected instead.</li>
<li><b>Invalid image handle values of -1 or 0 cannot be freed or an <a href="ERROR_Codes" title="ERROR Codes">"Illegal Function" error</a> will occur.</b> Check the handle value first.</li>
<li><b><a href="SCREEN" title="SCREEN">SCREEN</a> modes in use cannot be freed or an <a href="ERROR_Codes" title="ERROR Codes">"Illegal Function" error</a> will occur.</b> Change SCREEN modes before freeing.</li>
<li>Once a specific image handle is no longer used or referenced by your program, it can be freed with <a class="mw-selflink selflink">_FREEIMAGE</a>.</li>
<li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a class="mw-selflink selflink">_FREEIMAGE</a>.</b></li>
<li><b>It is important to free unused or unneeded images with <a class="mw-selflink selflink">_FREEIMAGE</a> to prevent memory overflow errors.</b></li>
<li><b>Do not try to free image handles currently being used as the active <a href="SCREEN" title="SCREEN">SCREEN</a>. Change screen modes first.</b></li>
<li><b>Note that calling _FREEIMAGE only frees the handle.  It does NOT reset the variable used to store the handle back to 0.  (This is because 0 is often used as a short cut value for the current display, such as with _DEST 0.)</b></li></ul>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Loading a program splash screen and freeing image when no longer necessary:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">s&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<span style="color:#FFB100;">"SPLASH.BMP"</span>, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">'load 32 bit(24 BPP) image</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> s&amp; &lt; <span style="color:#F580B1;">-1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> s&amp; <span style="color:#919191;">'use image as a 32 bit SCREEN</span>
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">6</span> <span style="color:#919191;">'display splash screen for 6 seconds</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">0</span> <span style="color:#919191;">'MUST change screen mode before freeing a SCREEN image!</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> s&amp; &lt; <span style="color:#F580B1;">-1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_FREEIMAGE</span></a> s&amp; <span style="color:#919191;">'handle value MUST be less than -1 or error!</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> A valid image file name must be used by <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or the invalid handle memory value will not need to be freed.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a></li>
<li><a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154222
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 194/1000000
Post‐expand include size: 1796/2097152 bytes
Template argument size: 409/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 202/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.532      1 -total
 11.62%    2.038      1 Template:PageSyntax
 10.20%    1.788     11 Template:Text
 10.19%    1.786     10 Template:Cl
  9.54%    1.672      2 Template:Parameter
  8.46%    1.484      1 Template:PageDescription
  8.44%    1.480      1 Template:CodeStart
  8.22%    1.442      1 Template:PageNavigation
  8.14%    1.427      1 Template:PageExamples
  8.11%    1.421      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:150-0!canonical and timestamp 20240714154222 and revision id 8684.
 -->
</div>
</div>
</div>
</div>
</body>
</html>