<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STR$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STR rootpage-STR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STR$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>STR$</b> function returns the <a href="STRING" title="STRING">STRING</a> representation of a numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>result$ = <b>STR$(</b><i>number</i><b>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>number</i> is any numerical type value to convert.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns any type number value with leading sign(space/minus) or decimal point when one exists in the numerical value.</li>
<li>If <i>number</i> is positive, the <a href="STRING" title="STRING">STRING</a> value returned will have a leading space character which can be removed using <a href="LTRIM$" title="LTRIM$">LTRIM$</a>.</li>
<li>If <i>number</i> is negative, the minus sign will precede the number instead of a space which <a href="LTRIM$" title="LTRIM$">LTRIM$</a> will not remove.</li>
<li>Trimming a STR$ string number using <a href="RTRIM$" title="RTRIM$">RTRIM$</a> is not required as <a href="PRINT" title="PRINT">PRINT</a> creates the undocumented trailing number space.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>( 1.0 )
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>( 2.3 )
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>( -4.5 )
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1
 2.3
-4.5
</pre>
</td></tr></tbody></table>
<p>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = 33
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>(a) + "10" + "1" + "who" + <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>(a) + <a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>(a) + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">STR$</span></a>(a))
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 33101who 33 3333
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="VAL" title="VAL">VAL</a>, <a href="STRING" title="STRING">STRING</a></li>
<li><a href="LTRIM$" title="LTRIM$">LTRIM$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="RIGHT$" title="RIGHT$">RIGHT$</a>, <a href="LEFT$" title="LEFT$">LEFT$</a></li>
<li><a href="HEX$" title="HEX$">HEX$</a>, <a href="OCT$" title="OCT$">OCT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714131707
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.080 seconds
Preprocessor visited node count: 134/1000000
Post‐expand include size: 1539/2097152 bytes
Template argument size: 132/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   59.881      1 -total
 21.76%   13.030      1 Template:PageSeeAlso
 13.02%    7.799      1 Template:PageExamples
  8.56%    5.126      1 Template:PageSyntax
  7.60%    4.548      1 Template:PageNavigation
  7.15%    4.281      1 Template:PageDescription
  6.45%    3.865     12 Template:Cl
  5.79%    3.467      2 Template:CodeStart
  5.36%    3.209      2 Template:OutputEnd
  4.89%    2.927      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:519-0!canonical and timestamp 20240714131707 and revision id 8168.
 -->
</div>
</div>
</div>
</div>
</body>
</html>