<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SGN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SGN rootpage-SGN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SGN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>SGN</b> function returns the sign of a number value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>sign% = SGN(value)</dd></dl></dd></dl>
<p>
</p>
<ul><li>Returns -1 when a sign is negative, 0 when a value is zero, or 1 when a value is positive.</li>
<li>Function is used to store the original sign of a number.</li>
<li><b>QB64</b> allows programs to return only <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> variable values using a <a href="DEFINE" title="DEFINE">_DEFINE</a> statement.</li></ul>
<p>
<i>Example:</i> Checking and changing negative values to positive ones.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">n = -100
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SGN</span></a>(n) = -1 THEN n = <a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(n)
PRINT n
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 100
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1079" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ABS" title="ABS">ABS</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061416
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.076 seconds
Preprocessor visited node count: 40/1000000
Post‐expand include size: 790/2097152 bytes
Template argument size: 23/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   65.218      1 -total
 18.11%   11.814      1 Template:PageSeeAlso
 17.70%   11.543      1 Template:OutputStart
 17.29%   11.277      1 Template:OutputEnd
 16.61%   10.830      1 Template:PageNavigation
 13.76%    8.972      1 Template:CodeEnd
  7.86%    5.125      1 Template:CodeStart
  3.78%    2.466      3 Template:Cl
  3.19%    2.080      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:562-0!canonical and timestamp 20240715061416 and revision id 8884.
 -->
</div>
</div>
</div>
</div>
</body>
</html>