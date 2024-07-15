<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENIMAGE rootpage-SCREENIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENIMAGE</a> function stores the current desktop image or a portion of it and returns an image handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>imageHandle&amp;</i> = <a class="mw-selflink selflink">_SCREENIMAGE</a>[(<i>column1</i>, <i>row1</i>, <i>column2</i>, <i>row2</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>imageHandle&amp;</i> is the handle to the new image in memory that will contain the desktop screenshot.</li>
<li>The optional screen <i>column</i> and <i>row</i> positions can be used to get only a portion of the desktop image.</li>
<li>The desktop image or partial image is always a 32-bit image.</li>
<li>The current screen resolution or width-to-height aspect ratio can be obtained with <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a> and <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a>.</li>
<li>Can be used to take screenshots of the desktop or used with <a href="PRINTIMAGE" title="PRINTIMAGE">_PRINTIMAGE</a> to print them.</li>
<li>It is important to free unused or uneeded image handles with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent memory overflow errors.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Determining the present screen resolution of user's PC for a screensaver program.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> desktop&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENIMAGE</span></a>
 MaxScreenX&amp; = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(desktop&amp;)
 MaxScreenY&amp; = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(desktop&amp;)
 <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> desktop&amp; 'free image after measuring screen(it is not displayed)
 <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(MaxScreenX&amp;, MaxScreenY&amp;, 256) 'program window is sized to fit
 <a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_SCREENMOVE</span></a> _MIDDLE
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="Sample_code_to_save_images_to_disk">Sample code to save images to disk</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a> (member-contributed program for legacy screen modes)</li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREENCLICK" title="SCREENCLICK">_SCREENCLICK</a>, <a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a>, <a href="SCREENX" title="SCREENX">_SCREENX</a>, <a href="SCREENY" title="SCREENY">_SCREENY</a></li>
<li><a href="WIDTH_(function)" title="WIDTH (function)">_WIDTH</a>, <a href="HEIGHT" title="HEIGHT">_HEIGHT</a></li>
<li><a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a>, <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a></li>
<li><a href="FULLSCREEN" title="FULLSCREEN">_FULLSCREEN</a>, <a href="PRINTIMAGE" title="PRINTIMAGE">_PRINTIMAGE</a></li>
<li><a href="Screen_Saver_Programs" title="Screen Saver Programs">Screen Saver Programs</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a>, <a href="Icons_and_Cursors" title="Icons and Cursors">Icons and Cursors</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034452
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 152/1000000
Post‐expand include size: 1157/2097152 bytes
Template argument size: 188/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.030      1 -total
 13.36%    2.944      1 Template:PageSyntax
 11.72%    2.583      8 Template:Parameter
 10.54%    2.322      1 Template:PageDescription
 10.30%    2.268      1 Template:PageNavigation
 10.26%    2.260      1 Template:PageExamples
  9.94%    2.190      1 Template:CodeStart
  9.59%    2.113      7 Template:Cl
  8.13%    1.791      1 Template:PageSeeAlso
  8.09%    1.783      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:270-0!canonical and timestamp 20240715034452 and revision id 8673.
 -->
</div>
</div>
</div>
</div>
</body>
</html>