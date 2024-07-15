<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMFREE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMFREE rootpage-MEMFREE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMFREE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMFREE</a> statement frees the designated memory block <a href="MEM" title="MEM">_MEM</a> value and must be used with all memory functions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MEMFREE</a> <i>memoryVariable</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>ALL designated <a href="MEM" title="MEM">_MEM</a> type <i>memoryVariable</i> values must be freed to conserve memory when they are no longer used or needed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Since <a href="MEM" title="MEM">_MEM</a> type variables cannot use a suffix, use <a href="DIM" title="DIM">DIM</a> <i>memoryVariable</i> <a href="AS" title="AS">AS</a> <a href="MEM" title="MEM">_MEM</a> to create memory handle variables.</li>
<li>All values created by memory functions must be freed using <a class="mw-selflink selflink">_MEMFREE</a> with a valid <a href="MEM" title="MEM">_MEM</a> variable.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a></li>
<li><a href="MEM_(function)" title="MEM (function)">_MEM (function)</a></li>
<li><a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a></li>
<li><a href="MEMELEMENT" title="MEMELEMENT">_MEMELEMENT</a></li>
<li><a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062401
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.040 seconds
Preprocessor visited node count: 28/1000000
Post‐expand include size: 638/2097152 bytes
Template argument size: 42/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.453      1 -total
 23.55%    5.522      1 Template:PageSeeAlso
 20.48%    4.803      1 Template:PageDescription
 15.56%    3.650      1 Template:PageSyntax
 13.24%    3.105      3 Template:Parameter
 11.89%    2.789      1 Template:PageParameters
 11.26%    2.640      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:180-0!canonical and timestamp 20240715062401 and revision id 7619.
 -->
</div>
</div>
</div>
</div>
</body>
</html>