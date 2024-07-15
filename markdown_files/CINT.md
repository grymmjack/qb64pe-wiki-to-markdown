<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CINT rootpage-CINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CINT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CINT</a> function rounds decimal point numbers up or down to the nearest <a href="INTEGER" title="INTEGER">INTEGER</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>value%</i> = <a class="mw-selflink selflink">CINT</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="TYPE" title="TYPE">TYPE</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Values greater than .5 are rounded up. Values lower than .5 are rounded down.</li>
<li><i>Warning:</i> Since <a class="mw-selflink selflink">CINT</a> is used for integer values, the input values cannot exceed 32767 to -32768!</li>
<li>Use <a href="CLNG" title="CLNG">CLNG</a> for <a href="LONG" title="LONG">LONG</a> integer values exceeding <a href="INTEGER" title="INTEGER">INTEGER</a> limitations.</li>
<li>Note: When decimal point values are given to BASIC functions requiring <a href="INTEGER" title="INTEGER">INTEGERs</a> the value will be <a class="mw-selflink selflink">CINTed</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Shows how CINT rounds values up or down as in "bankers' rounding".
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a% = <a class="mw-selflink selflink"><span style="color:#4593D8;">CINT</span></a>(1.49): b% = <a class="mw-selflink selflink"><span style="color:#4593D8;">CINT</span></a>(1.50): c = 11.5
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> c: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a%, b%, c
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><span style="color:red;">1       2       11.5</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ROUND" title="ROUND">_ROUND</a>, <a href="CEIL" title="CEIL">_CEIL</a></li>
<li><a href="CLNG" title="CLNG">CLNG</a>, <a href="CSNG" title="CSNG">CSNG</a>, <a href="CDBL" title="CDBL">CDBL</a></li>
<li><a href="INT" title="INT">INT</a>, <a href="FIX" title="FIX">FIX</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192355
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.129 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1050/2097152 bytes
Template argument size: 85/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  101.882      1 -total
 11.86%   12.086      1 Template:PageParameters
 11.08%   11.290      3 Template:Parameter
 10.86%   11.068      1 Template:Text
 10.79%   10.998      1 Template:PageSeeAlso
  9.56%    9.738      1 Template:OutputStart
  9.41%    9.587      1 Template:PageNavigation
  9.38%    9.553      1 Template:OutputEnd
  8.10%    8.249      1 Template:PageSyntax
  5.63%    5.733      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:286-0!canonical and timestamp 20240714192355 and revision id 7832.
 -->
</div>
</div>
</div>
</div>
</body>
</html>