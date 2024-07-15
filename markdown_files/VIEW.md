<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>VIEW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-VIEW rootpage-VIEW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">VIEW</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>VIEW</b> statement creates a graphics view port area by defining the coordinate limits to be viewed.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>VIEW</b> [[SCREEN] (column1, row1)-(column2, row2)[, [color][, border]</dd></dl></dd></dl>
<p>
</p>
<ul><li>When the SCREEN option is used, all coordinates are absolute and only graphics within the viewport area are plotted.</li>
<li>When the SCREEN option is not used, all coordinates are relative to the view port with the values of column1 and row1 being automatically added before plotting the point.</li>
<li>Coordinate values are for the top left and bottom right values of a box area of the screen mode used.</li>
<li>The color parameter specifies a background fill color for the area. None when omitted.</li>
<li>Border requires any valid color attribute to draw a line around the VIEW area if there is room for it.</li>
<li>VIEW without any parameters disables the previous viewport. <a href="RUN" title="RUN">RUN</a> and <a href="SCREEN" title="SCREEN">SCREEN</a> can also disable any VIEW port.</li>
<li><a href="CLS" title="CLS">CLS</a> or <a href="CLS" title="CLS">CLS 1</a> clears the active graphics VIEW port area only. Disable a viewport before attempting to clear the entire screen!</li>
<li><b>Note: QB64 <a href="RUN" title="RUN">RUN</a> statements will not close <a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a>, <a class="mw-selflink selflink">VIEW</a> or <a href="WINDOW" title="WINDOW">WINDOW</a> view ports presently!</b></li></ul>
<p>
<i>Example 1:</i> Using SCREEN option with absolute screen coordinates.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 VIEW SCREEN (200, 200)-(400, 400), 1, 9 ' blue BG with light blue border
 CIRCLE (220, 220), 20, 11 ' using the actual screen coordinates
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Using coordinates relative to the viewport box area.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> SCREEN 12
 VIEW (200, 200)-(400, 400), 1, 9
 CIRCLE (20, 20), 20, 11 ' using coordinates inside of the viewport
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The relative coordinates are automatically adjusted to place the object correctly. Any values outside of the box's area will not be displayed. Both examples should display the same screen image.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a></li>
<li><a href="WINDOW" title="WINDOW">WINDOW</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="CLS" title="CLS">CLS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062229
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.025 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 641/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   14.175      1 -total
 31.76%    4.502      1 Template:PageSyntax
 17.11%    2.425      2 Template:CodeStart
 16.31%    2.312      2 Template:CodeEnd
 15.16%    2.149      1 Template:PageSeeAlso
 14.43%    2.046      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:456-0!canonical and timestamp 20240715062229 and revision id 7706.
 -->
</div>
</div>
</div>
</div>
</body>
</html>