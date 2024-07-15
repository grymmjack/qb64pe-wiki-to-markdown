<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$DYNAMIC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_DYNAMIC rootpage-_DYNAMIC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$DYNAMIC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$DYNAMIC</a> <a href="Metacommand" title="Metacommand">metacommand</a> allows the creation of dynamic (resizable) arrays.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>{<a href="REM" title="REM">REM</a> | <a href="Apostrophe" title="Apostrophe">'</a> } <a class="mw-selflink selflink">$DYNAMIC</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>QBasic <a href="Metacommand" title="Metacommand">metacommands</a> require <a href="REM" title="REM">REM</a> or <a href="Apostrophe" title="Apostrophe">apostrophe</a> (') before them and are normally placed at the start of the main module.</li>
<li>Dynamic arrays can be resized using <a href="REDIM" title="REDIM">REDIM</a>. The array's type cannot be changed.</li>
<li>All data in the array will be lost when <a href="REDIM" title="REDIM">REDIMensioned</a> except when <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> is used.</li>
<li><a href="REDIM" title="REDIM">REDIM</a> <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> can preserve and may move the previous array data when the array boundaries change.</li>
<li><a href="PRESERVE" title="PRESERVE">_PRESERVE</a> allows the <a href="UBOUND" title="UBOUND">upper</a> and <a href="LBOUND" title="LBOUND">lower</a> boundaries of an array to be changed. The number of dimensions cannot change.</li>
<li><a class="mw-selflink selflink">$DYNAMIC</a> arrays must be <a href="REDIM" title="REDIM">REDIMensioned</a> if <a href="ERASE" title="ERASE">ERASE</a> or <a href="CLEAR" title="CLEAR">CLEAR</a> are used as the arrays are removed completely.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> <a href="REDIM" title="REDIM">REDIMing</a> a $DYNAMIC array using <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> to retain previous array values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a> <a class="mw-selflink selflink"><span style="color:#55FF55;">$DYNAMIC</span></a>             'create dynamic arrays only
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(10)            'create array with 11 elements
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
  array(i) = i: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(i); 'set and display element values
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> <a href="PRESERVE" title="PRESERVE"><span style="color:#4593D8;">_PRESERVE</span></a> array(10 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 20)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 10 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 20
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(i);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">0  1  2  3  4  5  6  7  8  9  10
0  1  2  3  4  5  6  7  8  9  10
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$STATIC" title="$STATIC">$STATIC</a>, <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a></li>
<li><a href="STATIC" title="STATIC">STATIC</a></li>
<li><a href="ERASE" title="ERASE">ERASE</a>, <a href="CLEAR" title="CLEAR">CLEAR</a></li>
<li><a href="Arrays" title="Arrays">Arrays</a>, <a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192327
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.037 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 137/1000000
Post‐expand include size: 1523/2097152 bytes
Template argument size: 146/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.142      1 -total
 19.30%    6.397      1 Template:PageSyntax
  9.39%    3.111     15 Template:Cl
  8.17%    2.707      1 Template:CodeStart
  8.06%    2.671      1 Template:PageDescription
  7.90%    2.617      1 Template:PageSeeAlso
  7.47%    2.475      1 Template:PageExamples
  7.35%    2.435      1 Template:OutputEnd
  7.26%    2.407      1 Template:Cm
  6.99%    2.316      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:293-0!canonical and timestamp 20240714192327 and revision id 8204.
 -->
</div>
</div>
</div>
</div>
</body>
</html>