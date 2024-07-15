<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CSNG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CSNG rootpage-CSNG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CSNG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">CSNG</a> converts a numerical value to the closest <a href="SINGLE" title="SINGLE">SINGLE</a>-precision number.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>singleValue!</i> = <a class="mw-selflink selflink">CSNG</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="TYPE" title="TYPE">TYPE</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the closest <a href="SINGLE" title="SINGLE">SINGLE</a> decimal point value.</li>
<li>Also used to define a value as <a href="SINGLE" title="SINGLE">SINGLE</a>-precision up to 7 decimals.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> A# = 975.3421222#
 PRINT A#, CSNG(A#)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">975.3421222      975.3421
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CDBL" title="CDBL">CDBL</a>, <a href="CLNG" title="CLNG">CLNG</a></li>
<li><a href="CINT" title="CINT">CINT</a>, <a href="INT" title="INT">INT</a></li>
<li><a href="ROUND" title="ROUND">_ROUND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061244
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.036 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 40/1000000
Post‐expand include size: 804/2097152 bytes
Template argument size: 32/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.498      1 -total
 22.80%    8.548      1 Template:PageDescription
  8.85%    3.317      1 Template:PageSyntax
  8.14%    3.053      1 Template:PageExamples
  7.78%    2.916      3 Template:Parameter
  7.34%    2.752      1 Template:CodeStart
  7.30%    2.736      1 Template:PageParameters
  7.26%    2.723      1 Template:OutputStart
  6.80%    2.548      1 Template:OutputEnd
  6.50%    2.439      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:444-0!canonical and timestamp 20240715061244 and revision id 7246.
 -->
</div>
</div>
</div>
</div>
</body>
</html>