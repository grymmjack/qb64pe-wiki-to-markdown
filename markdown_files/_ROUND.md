<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ROUND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ROUND rootpage-ROUND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ROUND</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ROUND</a> function rounds to the closest even <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a> or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>value</i> = <a class="mw-selflink selflink">_ROUND</a>(<i>number</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can round <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> floating decimal point parameter values.</li>
<li>Can be used when numerical values exceed the limits of <a href="CINT" title="CINT">CINT</a> or <a href="CLNG" title="CLNG">CLNG</a>.</li>
<li>Rounding is done to the closest even <a href="INTEGER" title="INTEGER">integer</a> value. The same as QBasic does with <a href="%5C" title="\">integer division</a>.</li></ul>
<p>
<i>Example:</i> Displays how QB64 rounds to the closest even integer value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(0.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(1.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(2.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(3.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(4.5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROUND</span></a>(5.5)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">0
2
2
4
4
6
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a></li>
<li><a href="FIX" title="FIX">FIX</a>, <a href="CLNG" title="CLNG">CLNG</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062438
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 115/1000000
Post‐expand include size: 1327/2097152 bytes
Template argument size: 143/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.937      1 -total
 14.85%    3.703      1 Template:PageSyntax
 10.91%    2.720      1 Template:CodeStart
 10.11%    2.522      1 Template:PageNavigation
  9.72%    2.424     12 Template:Cl
  9.27%    2.311      2 Template:Parameter
  8.22%    2.050      1 Template:PageDescription
  8.19%    2.042      1 Template:PageSeeAlso
  7.77%    1.938      1 Template:CodeEnd
  7.46%    1.860      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:230-0!canonical and timestamp 20240715062438 and revision id 7392.
 -->
</div>
</div>
</div>
</div>
</body>
</html>