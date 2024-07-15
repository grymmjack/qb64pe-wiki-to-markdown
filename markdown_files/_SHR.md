<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SHR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SHR rootpage-SHR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SHR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SHR</a> function is used to shift the bits of a numerical value to the right.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_SHR</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to shift the bits of and can be of the following types: <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>, or <a href="BYTE" title="BYTE">_BYTE</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> the number of places to shift the bits.</li>
<li>While 0 is a valid value it will have no affect on the variable being shifted.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Allows for division of a value by 2 faster than normal division (see example 2 below).</li>
<li>Bits that reach the end of a variables bit count are dropped.</li>
<li>The type of variable used to store the results should match the type of the variable being shifted.</li>
<li>NOTE: When dealing with SIGNED variables, shifting the bits right will leave the sign bit set. This is due to how C++ deals with bit shifting under the hood.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.3 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">A~%% = 128 'set left most bit of an<a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A~%%
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SHR</span></a>(A~%%,7)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SHR</span></a>(A~%%,8) 'shift the bit off the right 'edge'
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 128
 1
 0
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">A~%% = 128
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> I%% = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 8
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SHR</span></a>(A~%%, I%%)
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">NEXT</span></a> I%%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 128
  64
  32
  16
  8
  4
  2
  1
  0
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHL" title="SHL">_SHL</a>, <a href="ROL" title="ROL">_ROL</a>, <a href="ROR" title="ROR">_ROR</a></li>
<li><a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a></li>
<li><a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062546
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.040 seconds
Preprocessor visited node count: 142/1000000
Post‐expand include size: 1636/2097152 bytes
Template argument size: 184/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.491      1 -total
 10.85%    2.657      1 Template:PageSyntax
  8.96%    2.193     12 Template:Cl
  7.52%    1.841      5 Template:Parameter
  7.50%    1.838      1 Template:PageExamples
  7.35%    1.799      1 Template:PageParameters
  7.31%    1.790      2 Template:CodeStart
  6.46%    1.582      1 Template:PageDescription
  6.22%    1.524      1 Template:PageAvailability
  6.14%    1.504      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:328-0!canonical and timestamp 20240715062546 and revision id 7412.
 -->
</div>
</div>
</div>
</div>
</body>
</html>