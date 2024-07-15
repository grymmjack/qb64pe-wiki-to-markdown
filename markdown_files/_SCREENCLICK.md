<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENCLICK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENCLICK rootpage-SCREENCLICK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENCLICK</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENCLICK</a> statement simulates clicking on a pixel coordinate on the desktop screen with the left mouse button.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SCREENCLICK</a> <i>column%</i>, <i>row%</i>[, <i>button%</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>column%</i> is the horizontal pixel coordinate position on the screen.</li>
<li><i>row%</i> is the vertical pixel coordinate position on the screen.</li>
<li>Optional <i>button%</i> can be used to specify left button (1, default), right button (2) or middle button (3) (available with <b>build 20170924/68</b>).</li>
<li>Coordinates can range from 0 to the <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a> and <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a>. The desktop image acquired by <a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a> can be used to map the coordinates required.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>, <a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a>, <a href="SCREENX" title="SCREENX">_SCREENX</a>, <a href="SCREENY" title="SCREENY">_SCREENY</a></li>
<li><a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a>, <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062439
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 37/1000000
Post‐expand include size: 605/2097152 bytes
Template argument size: 36/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   14.968      1 -total
 21.83%    3.268      1 Template:PageDescription
 19.96%    2.987      1 Template:PageSyntax
 17.64%    2.640      1 Template:PageNavigation
 17.33%    2.594      6 Template:Parameter
 16.56%    2.479      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:260-0!canonical and timestamp 20240715062439 and revision id 6519.
 -->
</div>
</div>
</div>
</div>
</body>
</html>