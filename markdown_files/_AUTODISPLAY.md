<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_AUTODISPLAY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-AUTODISPLAY rootpage-AUTODISPLAY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_AUTODISPLAY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_AUTODISPLAY</a> statement enables the automatic display of the screen image changes previously disabled by <a href="DISPLAY" title="DISPLAY">_DISPLAY</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_AUTODISPLAY</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">_AUTODISPLAY</a> is on by default and displays the screen at around 30 frames per second (normal vertical retrace speed).</li>
<li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a> disables automatic graphic displays, but it also eliminates having to use PCOPY or page flipping when used correctly. Placing _DISPLAY after screen draws or other screen changes assures completion of the changes before they are displayed. The speed of QB64 code execution makes this a viable option.</li>
<li>The <a href="AUTODISPLAY_(function)" title="AUTODISPLAY (function)">_AUTODISPLAY (function)</a> can be used to detect the current display behavior.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a></li>
<li><a href="AUTODISPLAY_(function)" title="AUTODISPLAY (function)">_AUTODISPLAY (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034255
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.019 seconds
Preprocessor visited node count: 13/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    7.298      1 -total
 30.01%    2.190      1 Template:PageSyntax
 22.61%    1.650      1 Template:PageNavigation
 22.55%    1.646      1 Template:PageDescription
 21.35%    1.558      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:49-0!canonical and timestamp 20240715034255 and revision id 5872.
 -->
</div>
</div>
</div>
</div>
</body>
</html>