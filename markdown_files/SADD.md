<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SADD - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SADD rootpage-SADD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SADD</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>SADD</b> function returns the address of a <a href="STRING" title="STRING">STRING</a> variable as an offset from the current data segment.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>SADD(stringvariable)</dd></dl></dd></dl>
<p>
</p>
<ul><li>The argument may be a simple string variable or a single element of a string array. You may not use fixed-length strings.</li>
<li>Use this function carefully because strings can move in the BASIC string space storage area at any time.</li>
<li>Adding characters may produce a run-time error. Don't add characters to the ends of parameters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a>, <a href="DEF_SEG" title="DEF SEG">DEF SEG</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192540
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.013 seconds
Real time usage: 0.016 seconds
Preprocessor visited node count: 9/1000000
Post‐expand include size: 505/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    6.144      1 -total
 38.48%    2.364      1 Template:PageSyntax
 29.05%    1.785      1 Template:PageNavigation
 28.30%    1.739      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:497-0!canonical and timestamp 20240714192540 and revision id 7396.
 -->
</div>
</div>
</div>
</div>
</body>
</html>