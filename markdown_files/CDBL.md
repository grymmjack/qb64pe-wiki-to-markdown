<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CDBL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CDBL rootpage-CDBL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CDBL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">CDBL</a> converts a value to the closest <a href="DOUBLE" title="DOUBLE">DOUBLE</a>-precision value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>doubleValue#</i> = <a class="mw-selflink selflink">CDBL</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="TYPE" title="TYPE">TYPE</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Rounds to the closest <a href="DOUBLE" title="DOUBLE">DOUBLE</a> floating decimal point value.</li>
<li>Also can be used to define a value as <a href="DOUBLE" title="DOUBLE">DOUBLE</a>-precision up to 15 decimals.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Prints a double-precision version of the single-precision value stored in the variable named A.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> A = 454.67
 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A; <a class="mw-selflink selflink"><span style="color:#4593D8;">CDBL</span></a>(A)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 454.67 454.6700134277344
</pre>
</td></tr></tbody></table>
<dl><dd>The last 11 numbers in the double-precision number change the value in this example, since A was previously defined to only two-decimal place accuracy.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CINT" title="CINT">CINT</a>, <a href="CLNG" title="CLNG">CLNG</a></li>
<li><a href="CSNG" title="CSNG">CSNG</a>, <a href="ROUND" title="ROUND">_ROUND</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061233
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 54/1000000
Post‐expand include size: 904/2097152 bytes
Template argument size: 50/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.262      1 -total
  9.60%    2.329      1 Template:PageSyntax
  8.84%    2.146      3 Template:Parameter
  8.67%    2.104      1 Template:CodeStart
  8.23%    1.996      2 Template:Cl
  8.05%    1.953      1 Template:PageDescription
  7.95%    1.929      1 Template:PageParameters
  7.83%    1.899      1 Template:PageExamples
  7.30%    1.770      1 Template:CodeEnd
  7.06%    1.712      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:407-0!canonical and timestamp 20240715061233 and revision id 7233.
 -->
</div>
</div>
</div>
</div>
</body>
</html>