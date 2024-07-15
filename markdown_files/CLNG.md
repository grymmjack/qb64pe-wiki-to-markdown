<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CLNG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLNG rootpage-CLNG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CLNG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CLNG</a> function rounds decimal point numbers up or down to the nearest <a href="LONG" title="LONG">LONG</a> integer value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>value&amp;</i> = <a class="mw-selflink selflink">CLNG</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="TYPE" title="TYPE">TYPE</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used when integer values exceed 32767 or are less than -32768.</li>
<li>Values greater than .5 are rounded up; .5 or lower are rounded down.</li>
<li>CLNG can return normal <a href="INTEGER" title="INTEGER">INTEGER</a> values under 32768 too.</li>
<li>Use it when a number could exceed normal <a href="INTEGER" title="INTEGER">INTEGER</a> number limits.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> a&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">CLNG</span></a>(2345678.51)
 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 2345679
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CINT" title="CINT">CINT</a>, <a href="INT" title="INT">INT</a></li>
<li><a href="CSNG" title="CSNG">CSNG</a>, <a href="CDBL" title="CDBL">CDBL</a></li>
<li><a href="ROUND" title="ROUND">_ROUND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192358
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.041 seconds
Real time usage: 0.070 seconds
Preprocessor visited node count: 54/1000000
Post‐expand include size: 898/2097152 bytes
Template argument size: 44/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   50.658      1 -total
 23.07%   11.688      1 Template:PageDescription
 12.29%    6.224      1 Template:PageExamples
  8.05%    4.079      1 Template:PageSyntax
  7.88%    3.991      1 Template:PageParameters
  7.49%    3.795      3 Template:Parameter
  6.56%    3.323      1 Template:CodeStart
  5.65%    2.864      2 Template:Cl
  5.65%    2.861      1 Template:CodeEnd
  4.81%    2.438      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:411-0!canonical and timestamp 20240714192358 and revision id 6381.
 -->
</div>
</div>
</div>
</div>
</body>
</html>