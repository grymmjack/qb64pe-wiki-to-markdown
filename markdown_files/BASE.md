<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OPTION BASE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPTION_BASE rootpage-OPTION_BASE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">OPTION BASE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">OPTION BASE</a> statement is used to set the default lower bound of arrays.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">OPTION BASE</a> {0|1}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>This statement affects array declarations where the lower bound of a dimension is not specified.</li>
<li>When used, <a class="mw-selflink selflink">OPTION BASE</a> must come before any array declarations (<a href="DIM" title="DIM">DIM</a>) to be affected.</li>
<li>By default, the lower bound for arrays is zero, and may be changed to one using the statement.</li>
<li>Otherwise, arrays will be dimensioned from element 0 if you DIM just the upper bounds.</li>
<li>You can also set other array boundaries by using <a href="TO" title="TO">TO</a> in the DIM declaration such as <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">DIM array(5 TO 10)</span></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Set the default lower bound for array declarations to one.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OPTION BASE</span></a> 1
' Declare a 5-element one-dimensional array with element indexes of one through five.
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(5) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(array)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Set the default lower bound for array declarations to zero.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OPTION BASE</span></a> 0
' Declare an 18-element two-dimensional array with element indexes of zero through two
' for the first dimension, and 10 through 15 for the second dimension.
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(2, 10 to 15) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(array, 1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(array, 2)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 0
 10
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Arrays" title="Arrays">Arrays</a>, <a href="LBOUND" title="LBOUND">LBOUND</a>, <a href="UBOUND" title="UBOUND">UBOUND</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="STATIC" title="STATIC">STATIC</a>, <a href="COMMON" title="COMMON">COMMON</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061226
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.034 seconds
Preprocessor visited node count: 134/1000000
Post‐expand include size: 1795/2097152 bytes
Template argument size: 158/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.504      1 -total
 10.46%    2.458      1 Template:InlineCodeEnd
  9.94%    2.336      1 Template:InlineCode
  9.06%    2.130     14 Template:Cl
  7.95%    1.868      2 Template:CodeEnd
  7.93%    1.864      1 Template:PageSyntax
  7.07%    1.662      1 Template:PageSeeAlso
  7.05%    1.656      2 Template:OutputStart
  6.93%    1.630      1 Template:PageNavigation
  6.57%    1.543      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:531-0!canonical and timestamp 20240715061226 and revision id 6144.
 -->
</div>
</div>
</div>
</div>
</body>
</html>