<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENY rootpage-SCREENY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENY</a> function returns the current row pixel coordinate of the program window on the desktop.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>positionY&amp;</i> = <a class="mw-selflink selflink">_SCREENY</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Function returns the current program window's upper left corner row position on the desktop.</li>
<li>Use <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a> and <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a> to find the current user's Windows desktop resolution to adjust the position with <a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a>.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Clicks and opens program window header menu:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_SCREENMOVE</span></a> <a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_MIDDLE</span></a>
<a href="SCREENCLICK" title="SCREENCLICK"><span style="color:#4593D8;">_SCREENCLICK</span></a> <a href="SCREENX" title="SCREENX"><span style="color:#4593D8;">_SCREENX</span></a> + 10, <a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENY</span></a> + 10
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello window!"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREENX" title="SCREENX">_SCREENX</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="SCREENCLICK" title="SCREENCLICK">_SCREENCLICK</a></li>
<li><a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062446
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 67/1000000
Post‐expand include size: 1016/2097152 bytes
Template argument size: 116/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.054      1 -total
 12.41%    2.489      1 Template:PageSyntax
 11.67%    2.339      6 Template:Cl
 10.82%    2.170      1 Template:Parameter
 10.79%    2.164      1 Template:PageSeeAlso
 10.35%    2.075      1 Template:CodeStart
 10.14%    2.034      1 Template:PageNavigation
  9.98%    2.001      1 Template:PageDescription
  9.38%    1.881      1 Template:PageExamples
  8.76%    1.756      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:321-0!canonical and timestamp 20240715062446 and revision id 6526.
 -->
</div>
</div>
</div>
</div>
</body>
</html>