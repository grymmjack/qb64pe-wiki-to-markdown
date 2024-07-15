<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMEXISTS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMEXISTS rootpage-MEMEXISTS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMEXISTS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMEXISTS</a> function returns true (-1) if the memory block variable name specified exists in memory and false (0) if it does not.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_MEMEXISTS</a>(<i>memBlock</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>memBlock</i> variable name must have been created using <a href="DIM" title="DIM">DIM</a> memBlock <a href="AS" title="AS">AS</a> <a href="MEM" title="MEM">_MEM</a> type (<a href="DIM" title="DIM">DIM</a>.</li>
<li>The function verifies that the memory variable exists in memory before using a passed block, to avoid generating QB64 errors.</li>
<li>Typically, this function is used by a <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">LIBRARY</a> <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> which accepts a <a href="MEM" title="MEM">_MEM</a> structure as input, to avoid an error.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM_(function)" title="MEM (function)">_MEM (function)</a></li>
<li><a href="MEMELEMENT" title="MEMELEMENT">_MEMELEMENT</a>, <a href="MEMCOPY" title="MEMCOPY">_MEMCOPY</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="MEMFILL" title="MEMFILL">_MEMFILL</a>, <a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062400
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.041 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 25/1000000
Post‐expand include size: 579/2097152 bytes
Template argument size: 22/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.823      1 -total
 55.81%   16.085      1 Template:PageSeeAlso
 11.34%    3.270      1 Template:PageSyntax
 10.21%    2.944      1 Template:PageNavigation
 10.17%    2.932      1 Template:PageDescription
  9.39%    2.705      3 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:178-0!canonical and timestamp 20240715062400 and revision id 7340.
 -->
</div>
</div>
</div>
</div>
</body>
</html>