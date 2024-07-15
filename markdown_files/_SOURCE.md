<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SOURCE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SOURCE rootpage-SOURCE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SOURCE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SOURCE</a> statement establishes the image SOURCE using a handle created by <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or <a href="COPYIMAGE" title="COPYIMAGE">_COPYIMAGE</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SOURCE</a> <i>handle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The handle is a <a href="LONG" title="LONG">LONG</a> integer value from the <a href="SOURCE_(function)" title="SOURCE (function)">_SOURCE</a> function or a handle created by <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>.</li>
<li>If the handle is designated as 0, it refers to the current <a href="SCREEN" title="SCREEN">SCREEN</a> image.</li>
<li>A source image can only supply information to a program. <a href="POINT" title="POINT">POINT</a> and <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> might require a source other than the one currently active.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
a = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(320,200,13)
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> a
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (100, 100), 15
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SOURCE</span></a> a
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> 0
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(100, 100)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 15
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Create a new image with handle 'a', then use <a href="DEST" title="DEST">_DEST</a> to define the image to draw on. Draw a pixel then set the source to 'a' and use <a href="POINT" title="POINT">POINT</a> to show what color is in that position. White (15) and is the color set with <a href="PSET" title="PSET">PSET</a>. Use <a href="DEST" title="DEST">_DEST</a> 0 for the screen to display the results.</dd></dl>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="Bitmaps" title="Bitmaps">Bitmaps</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEST" title="DEST">_DEST</a></li>
<li><a href="SOURCE_(function)" title="SOURCE (function)">_SOURCE (function)</a></li>
<li><a href="POINT" title="POINT">POINT</a>, <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714092255
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 136/1000000
Post‐expand include size: 1152/2097152 bytes
Template argument size: 99/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.062      1 -total
 11.92%    2.272      1 Template:PageExamples
  9.58%    1.827      1 Template:PageSyntax
  9.34%    1.781      1 Template:PageDescription
  9.33%    1.778      1 Template:PageNavigation
  9.03%    1.722      8 Template:Cl
  8.38%    1.597      1 Template:CodeStart
  7.84%    1.495      1 Template:Parameter
  7.56%    1.441      1 Template:PageSeeAlso
  7.10%    1.354      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:351-0!canonical and timestamp 20240714092255 and revision id 8674.
 -->
</div>
</div>
</div>
</div>
</body>
</html>