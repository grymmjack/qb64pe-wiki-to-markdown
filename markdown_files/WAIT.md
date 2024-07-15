<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>WAIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WAIT rootpage-WAIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">WAIT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">WAIT</a> statement waits until the value read from an I/O port has certain bits set.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">WAIT</a> <i>port%</i>, <i>andMask%</i>[, <i>xorMask%</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <a class="mw-selflink selflink">WAIT</a> statement reads a value from <i>port%</i> using <a href="INP" title="INP">INP</a>.</li>
<li>If <i>xorMask%</i> is specified, the value is <a class="mw-redirect" href="XOR" title="XOR">XOR</a>'d with <i>xorMask%</i>. It has the effect of "toggle these bits".</li>
<li>The value is then <a href="AND" title="AND">AND</a>'d with <i>andMask%</i>. It has the effect of "check if these bits are set".</li>
<li>If the final value is non-zero, <a class="mw-selflink selflink">WAIT</a> returns. Otherwise, another value is read from <i>port%</i> and checked again.</li>
<li>The <a class="mw-selflink selflink">WAIT</a> statement returns immediately if <i>port%</i> is not supported.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd>Waiting for vertical retrace</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' Either statement can be used to try to reduce screen flickering.
' If both statements are used, try changing the order.
WAIT &amp;H3DA, 8 ' finishes whenever the screen isn't being written to
WAIT &amp;H3DA, 8, 8 ' finishes whenever the screen is being written to
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INP" title="INP">INP</a>, <a href="OUT" title="OUT">OUT</a></li>
<li><a href="Scancodes" title="Scancodes">Scancodes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714084657
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 56/1000000
Post‐expand include size: 746/2097152 bytes
Template argument size: 60/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.574      1 -total
 15.19%    2.821      1 Template:PageSyntax
 13.98%    2.597      9 Template:Parameter
 12.73%    2.364      1 Template:PageDescription
 11.84%    2.199      1 Template:PageExamples
 11.12%    2.065      1 Template:CodeEnd
 10.12%    1.879      1 Template:CodeStart
  8.93%    1.658      1 Template:PageNavigation
  8.66%    1.609      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:549-0!canonical and timestamp 20240714084657 and revision id 6630.
 -->
</div>
</div>
</div>
</div>
</body>
</html>