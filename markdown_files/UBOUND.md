<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>UBOUND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UBOUND rootpage-UBOUND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">UBOUND</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">UBOUND</a> function returns the largest valid index (upper bound) of an array dimension.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result%</i> = <a class="mw-selflink selflink">UBOUND</a>(arrayName[, dimension%])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>arrayName</i> specifies the name of the array.</li></ul>
<ul><li><i>dimension%</i> specifies the dimension number, starting with <b>1</b> for the first dimension.
<ul><li>If omitted, <i>dimension%</i> is assumed to be <b>1</b>.</li>
<li>If <i>dimension%</i> is less than <b>1</b> or is greater than the number of dimensions, a <a href="ERROR_Codes" title="ERROR Codes">subscript out of range</a> error occurs.</li></ul></li></ul>
<ul><li><a class="mw-selflink selflink">UBOUND</a>, along with <a href="LBOUND" title="LBOUND">LBOUND</a>, is used to determine the range of valid indexes of an array.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> myArray(5) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> myOtherArray(1 to 2, 3 to 4) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">UBOUND</span></a>(myArray)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">UBOUND</span></a>(myOtherArray, 2)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 5
 4
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Arrays" title="Arrays">Arrays</a>, <a href="LBOUND" title="LBOUND">LBOUND</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="COMMON" title="COMMON">COMMON</a>, <a href="STATIC" title="STATIC">STATIC</a>, <a href="SHARED" title="SHARED">SHARED</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034236
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 111/1000000
Post‐expand include size: 1278/2097152 bytes
Template argument size: 131/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.273      1 -total
 11.96%    2.783      1 Template:PageSyntax
  9.47%    2.204     10 Template:Cl
  9.23%    2.148      1 Template:PageDescription
  8.69%    2.022      1 Template:PageNavigation
  8.59%    1.999      4 Template:Parameter
  8.29%    1.929      1 Template:CodeStart
  7.98%    1.856      1 Template:CodeEnd
  7.92%    1.843      1 Template:PageExamples
  7.48%    1.741      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:491-0!canonical and timestamp 20240715034236 and revision id 6627.
 -->
</div>
</div>
</div>
</div>
</body>
</html>