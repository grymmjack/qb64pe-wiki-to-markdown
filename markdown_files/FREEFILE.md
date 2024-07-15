<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FREEFILE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FREEFILE rootpage-FREEFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FREEFILE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">FREEFILE</a> function returns a <a href="LONG" title="LONG">LONG</a> value that is an unused file access number.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>fileHandle&amp; = <a class="mw-selflink selflink">FREEFILE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">FREEFILE</a> values should be given to unique variables so that each file has a specific variable value assigned to it.</li>
<li>Once the number is assigned in an <a href="OPEN" title="OPEN">OPEN</a> statement, the file number can later be used to read, write or <a href="CLOSE" title="CLOSE">CLOSE</a> that file.</li>
<li>File numbers <a href="CLOSE" title="CLOSE">CLOSEd</a> are made available to <a class="mw-selflink selflink">FREEFILE</a> for reuse immediately.</li>
<li><a class="mw-selflink selflink">FREEFILE</a> returns are normally sequential starting with 1. Only file numbers in use will not be returned.</li>
<li><a href="OPEN" title="OPEN">OPEN</a> each file number after each <a class="mw-selflink selflink">FREEFILE</a> return or the values returned may be the same.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1295" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a>, <a href="CLOSE" title="CLOSE">CLOSE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192438
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.050 seconds
Preprocessor visited node count: 12/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.602      1 -total
 38.02%   12.016      1 Template:PageNavigation
 27.92%    8.823      1 Template:PageSeeAlso
 22.35%    7.062      1 Template:PageDescription
  9.98%    3.155      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:472-0!canonical and timestamp 20240714192438 and revision id 8928.
 -->
</div>
</div>
</div>
</div>
</body>
</html>