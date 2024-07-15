<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOCK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOCK rootpage-LOCK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOCK</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LOCK</a> statement restricts access to parts of a file by other programs or processes.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LOCK</a> [#]<i>fileNumber%</i></dd>
<dd><a class="mw-selflink selflink">LOCK</a> [#]<i>fileNumber%</i>, <i>record&amp;</i></dd>
<dd><a class="mw-selflink selflink">LOCK</a> [#]<i>fileNumber%</i>, [<i>firstRecord&amp;</i>] TO <i>lastRecord&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileNumber%</i> is the file number of the file to lock.</li>
<li>In the first syntax, the entire file is locked.</li>
<li>In the second syntax, <i>record&amp;</i> is the record number of the file to lock.</li>
<li>In the third syntax, the records or bytes in the range [<i>firstRecord&amp;</i>,<i>lastRecord&amp;</i>] are locked. If <i>firstRecord&amp;</i> is omitted, it is assumed to be one (the first record or byte).</li>
<li>For files opened in <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> mode, each record corresponds to a single byte.</li>
<li><a class="mw-selflink selflink">LOCK</a> and <a href="UNLOCK" title="UNLOCK">UNLOCK</a> statements are always used in pairs and each statement must match the other one.</li>
<li>Files must be unlocked using <a href="UNLOCK" title="UNLOCK">UNLOCK</a> before other programs can access them, and before the file is closed.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Required DOS <b>SHARED.EXE</b> to be run for QBasic to use networking access modes. No longer required.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="UNLOCK" title="UNLOCK">UNLOCK</a></li>
<li><a href="OPEN" title="OPEN">OPEN</a></li>
<li><a class="mw-redirect" href="ACCESS" title="ACCESS">ACCESS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061335
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 93/1000000
Post‐expand include size: 705/2097152 bytes
Template argument size: 116/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.024      1 -total
 34.82%    5.928     11 Template:Parameter
 22.05%    3.754      1 Template:PageSyntax
 13.02%    2.217      1 Template:PageSeeAlso
 12.22%    2.080      1 Template:PageDescription
 11.36%    1.933      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:512-0!canonical and timestamp 20240715061335 and revision id 7135.
 -->
</div>
</div>
</div>
</div>
</body>
</html>