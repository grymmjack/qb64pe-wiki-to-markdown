<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ABS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ABS rootpage-ABS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ABS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ABS</a> function returns the unsigned numerical value of a variable or literal value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>positive</i> = <a class="mw-selflink selflink">ABS</a>(<i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">ABS</a> always returns positive numerical values. The value can be any numerical type.</li>
<li>Often used to keep a value positive when necessary in a program.</li>
<li>Use <a href="SGN" title="SGN">SGN</a> to determine a value's sign when necessary.</li>
<li><b>QB64</b> allows programs to return only positive <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> variable values using a <a href="DIM" title="DIM">DIM</a> or <a href="DEFINE" title="DEFINE">_DEFINE</a> statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Finding the absolute value of positive and negative numerical values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = -6
b = -7
c = 8
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> a &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> a = <a class="mw-selflink selflink"><span style="color:#4593D8;">ABS</span></a>(a)
b = <a class="mw-selflink selflink"><span style="color:#4593D8;">ABS</span></a>(b)
c = <a class="mw-selflink selflink"><span style="color:#4593D8;">ABS</span></a>(c)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a, b, c
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 6        7        8
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SGN" title="SGN">SGN</a>, <a href="DIM" title="DIM">DIM</a></li>
<li><a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061220
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 75/1000000
Post‐expand include size: 1044/2097152 bytes
Template argument size: 69/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.726      1 -total
 18.24%    6.697      1 Template:PageNavigation
 11.71%    4.300      1 Template:PageSyntax
  9.96%    3.657      1 Template:CodeStart
  9.14%    3.358      1 Template:PageDescription
  8.64%    3.175      2 Template:Parameter
  8.24%    3.026      6 Template:Cl
  8.22%    3.019      1 Template:PageExamples
  5.61%    2.062      1 Template:OutputStart
  5.53%    2.031      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:390-0!canonical and timestamp 20240715061220 and revision id 5857.
 -->
</div>
</div>
</div>
</div>
</body>
</html>